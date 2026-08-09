#!/usr/bin/env python3
"""Cross-vendor fact/interpretation check on a published post.

Sends the post's plain text to models from OUTSIDE the Claude family and asks
each, independently, to flag (a) factual errors — a claimed number, date, or
event that is wrong or unverifiable — and (b) errors of interpretation — a
correct fact used to support a conclusion it doesn't actually support (a false
causal link, an overstated trend, a mismatched comparison).

No DeepSeek key exists on this machine (checked ~/.config/market-secrets/
credentials.env), so the panel is the two vendors that ARE configured there:

    Gemini   gemini-flash-latest (ungrounded — see note in ask_gemini)
    Groq     llama-3.3-70b-versatile (see note by GROQ_MODELS)

Report-only. This never edits the post — it writes a markdown report for a
human to read, the same "model output is not a verified fact" contract as
tools/adoption_check.py.

    python3 tools/multi_model_factcheck.py --file posts/<slug>.html
    python3 tools/multi_model_factcheck.py --slug <slug>              # same
    python3 tools/multi_model_factcheck.py --all                      # loop, one report per post
"""
import argparse
import glob
import html
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "out" / "factcheck"
CREDS = pathlib.Path(os.path.expanduser("~/.config/market-secrets/credentials.env"))

# gemini-2.0-flash returns a hard "limit: 0" free-tier quota on this key (not a
# transient rate limit); gemini-flash-latest is what this key actually has quota for.
GEMINI_MODEL = "gemini-flash-latest"
GROQ_MODELS = ["llama-3.3-70b-versatile"]
# openai/gpt-oss-120b and qwen/qwen3.6-27b share an org-wide free-tier cap of
# 8000 tokens/minute on this account, which a full-length post plus prompt
# (~9-11k tokens) blows past every time (413). llama-3.3-70b-versatile is the
# only Groq model on this key with headroom for a full post, so it's the only
# one used — a full-text check from one model beats a truncated one from two.

# Groq's Cloudflare front returns 403 "error code: 1010" to urllib's default
# User-Agent (a browser-signature block, unrelated to auth/quota) — reproduced
# with curl vs urllib against the same key. A normal UA clears it.
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

PROMPT = """You are fact-checking a published article for an India-focused economics
blog. Read the article text below and report two DISTINCT kinds of problems only.
Do not summarize the article and do not comment on style.

1. FACTUAL ERRORS — a specific number, date, name, or event stated in the
   article that is wrong, outdated, or that you cannot verify against what you
   know. Quote the exact claim.
2. INTERPRETATION ERRORS — a fact that is probably correct but is used to
   support a conclusion it does not actually support: a false causal claim, an
   apples-to-oranges comparison, an extrapolation beyond what the data shows,
   or double-counting. Quote the claim and explain the gap in reasoning.

If you find nothing in a category, write "none found" — do not invent a
problem to fill the section. Do not flag stylistic or formatting issues.

Answer in exactly this structure:

FACTUAL ERRORS:
- <claim> — <what's wrong, and why> [confidence: high/medium/low]
(repeat, or "none found")

INTERPRETATION ERRORS:
- <claim> — <the reasoning gap> [confidence: high/medium/low]
(repeat, or "none found")

ARTICLE TEXT:
{text}"""


def creds():
    if not CREDS.exists():
        sys.exit(f"credentials file not found: {CREDS}")
    return CREDS.read_text()


def key(name, blob):
    m = re.search(rf"^{name}=(.*)$", blob, re.M)
    if not m:
        sys.exit(f"{name} not in {CREDS}")
    return m.group(1).strip()


def extract_text(path):
    s = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<style.*?</style>", " ", s, flags=re.S | re.I)
    # keep table rows readable as "cell | cell | cell" rather than one run-on blob
    s = re.sub(r"</t[dh]>", " | ", s, flags=re.I)
    s = re.sub(r"</tr>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


def ask_gemini(k, text):
    body = {
        "contents": [{"parts": [{"text": PROMPT.format(text=text)}]}],
        "generationConfig": {"temperature": 0.1},
        # No google_search grounding: this key's free-tier grounded-search quota
        # is exhausted (429, RESOURCE_EXHAUSTED) while plain generateContent
        # works fine. Ungrounded, same as both Groq calls below — the model
        # checks the article against its training knowledge, not live search.
    }
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={k}",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "User-Agent": UA})
    try:
        d = json.loads(urllib.request.urlopen(req, timeout=120).read())
    except urllib.error.HTTPError as e:
        return f"[Gemini API error {e.code}: {e.read().decode()[:300]}]"
    except urllib.error.URLError as e:
        return f"[Gemini network error: {e}]"
    cand = (d.get("candidates") or [{}])[0]
    return "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", [])).strip() or "[empty response]"


def ask_groq(k, model, text):
    body = {
        "model": model,
        "messages": [{"role": "user", "content": PROMPT.format(text=text)}],
        "temperature": 0.1,
    }
    req = urllib.request.Request(
        "https://api.groq.com/openai/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {k}", "User-Agent": UA})
    try:
        d = json.loads(urllib.request.urlopen(req, timeout=120).read())
    except urllib.error.HTTPError as e:
        return f"[Groq/{model} API error {e.code}: {e.read().decode()[:300]}]"
    except urllib.error.URLError as e:
        return f"[Groq/{model} network error: {e}]"
    try:
        return d["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError):
        return f"[Groq/{model} unexpected response: {json.dumps(d)[:300]}]"


def run_one(path, gk, qk):
    text = extract_text(path)
    slug = pathlib.Path(path).stem
    print(f"… {slug}  ({len(text)} chars)")

    results = [("Gemini " + GEMINI_MODEL, ask_gemini(gk, text))]
    for m in GROQ_MODELS:
        results.append((f"Groq {m}", ask_groq(qk, m, text)))
        time.sleep(1)  # be polite to the free tier

    md = [f"# Fact/interpretation check — {slug}", "",
          "> **Model output, not verified fact.** Every flagged claim needs primary-source",
          "> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)",
          "> before it changes anything in the post. Models disagreeing with each other or with",
          "> the post is a prompt to check, not a verdict.",
          "", f"Source: `posts/{slug}.html`", ""]
    for name, out in results:
        md += [f"## {name}", "", out, ""]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{slug}.md"
    out_path.write_text("\n".join(md), encoding="utf-8")
    print(f"  -> {out_path.relative_to(ROOT)}")
    return out_path


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--file", help="path to a post HTML file")
    g.add_argument("--slug", help="post slug under posts/")
    g.add_argument("--all", action="store_true", help="run every post in posts/")
    args = ap.parse_args()

    blob = creds()
    gk = key("GEMINI_API_KEY", blob)
    qk = key("GROQ_API_KEY", blob)

    if args.all:
        files = sorted(glob.glob(str(ROOT / "posts" / "*.html")))
    elif args.slug:
        files = [str(ROOT / "posts" / f"{args.slug}.html")]
    else:
        files = [args.file]

    for f in files:
        if not pathlib.Path(f).exists():
            print(f"skip (not found): {f}", file=sys.stderr)
            continue
        run_one(f, gk, qk)


if __name__ == "__main__":
    main()
