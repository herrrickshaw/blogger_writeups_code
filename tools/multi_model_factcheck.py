#!/usr/bin/env python3
"""Cross-vendor fact/interpretation check on a published post.

Sends the post's plain text to models from OUTSIDE the Claude family and asks
each, independently, to flag (a) factual errors — a claimed number, date, or
event that is wrong or unverifiable — and (b) errors of interpretation — a
correct fact used to support a conclusion it doesn't actually support (a false
causal link, an overstated trend, a mismatched comparison).

No DeepSeek key exists on this machine (checked ~/.config/market-secrets/
credentials.env). The panel:

    Gemini    gemini-flash-latest (ungrounded — see note in ask_gemini)
    Groq      llama-3.3-70b-versatile (see note by GROQ_MODELS)
    Kimi      kimi-k2-0711-preview via Moonshot AI (see note by KIMI_MODEL) —
              key added 2026-08-09; account had zero balance as of that date,
              so calls 429 with "insufficient balance" until it's funded.

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

# Not data articles — a résumé/bio page and the site's own article-index/nav
# page. Fact-checking normal CV phrasing or a link list against "is this
# verifiable" produces noise, not findings (confirmed on about-author.html:
# both models flagged ordinary résumé bullets as unverified claims).
SKIP_SLUGS = {"about-author", "article-index-start-here"}

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

# Moonshot AI (Kimi), OpenAI-compatible endpoint. api.moonshot.ai accepted this
# key (not api.moonshot.cn — a 401 there, different account namespace).
KIMI_MODEL = "kimi-k2-0711-preview"
KIMI_URL = "https://api.moonshot.ai/v1/chat/completions"

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


def key_optional(name, blob):
    m = re.search(rf"^{name}=(.*)$", blob, re.M)
    return m.group(1).strip() if m else None


def extract_text(path):
    s = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<style.*?</style>", " ", s, flags=re.S | re.I)
    # Drop struck-through/retracted content outright. Without this, a post's own
    # correction notice (old wrong number, struck through, annotated "retracted")
    # gets read as a live claim and re-flagged as a fresh error — confirmed on
    # chemical-import-substitution-analysis.html, which already self-corrected
    # the exact numbers both models re-reported.
    s = re.sub(r"<s>.*?</s>", " ", s, flags=re.S | re.I)
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


def ask_kimi(k, text):
    body = {
        "model": KIMI_MODEL,
        "messages": [{"role": "user", "content": PROMPT.format(text=text)}],
        "temperature": 0.1,
    }
    req = urllib.request.Request(
        KIMI_URL, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {k}", "User-Agent": UA})
    try:
        d = json.loads(urllib.request.urlopen(req, timeout=120).read())
    except urllib.error.HTTPError as e:
        return f"[Kimi API error {e.code}: {e.read().decode()[:300]}]"
    except urllib.error.URLError as e:
        return f"[Kimi network error: {e}]"
    try:
        return d["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError):
        return f"[Kimi unexpected response: {json.dumps(d)[:300]}]"


def already_done(slug):
    """A clean prior report (no API error in it) — skip on resumed --all runs."""
    p = OUT_DIR / f"{slug}.md"
    return p.exists() and "API error" not in p.read_text(encoding="utf-8")


def run_one(path, gk, qk, kk):
    text = extract_text(path)
    slug = pathlib.Path(path).stem
    print(f"… {slug}  ({len(text)} chars)")

    results = [("Gemini " + GEMINI_MODEL, ask_gemini(gk, text))]
    for m in GROQ_MODELS:
        results.append((f"Groq {m}", ask_groq(qk, m, text)))
        time.sleep(1)  # be polite to the free tier
    if kk:
        results.append((f"Kimi {KIMI_MODEL}", ask_kimi(kk, text)))
        time.sleep(1)

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
    all_failed = all("API error" in out or "network error" in out for _, out in results)
    print(f"  -> {out_path.relative_to(ROOT)}" + ("  [ALL CALLS FAILED]" if all_failed else ""))
    return out_path, all_failed


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--file", help="path to a post HTML file")
    g.add_argument("--slug", help="post slug under posts/")
    g.add_argument("--all", action="store_true", help="run every post in posts/ not already cleanly done")
    ap.add_argument("--force", action="store_true", help="with --all, re-run posts that already have a clean report")
    args = ap.parse_args()

    blob = creds()
    gk = key("GEMINI_API_KEY", blob)
    qk = key("GROQ_API_KEY", blob)
    kk = key_optional("MOONSHOT_API_KEY", blob)

    if args.all:
        files = sorted(glob.glob(str(ROOT / "posts" / "*.html")))
        files = [f for f in files if pathlib.Path(f).stem not in SKIP_SLUGS]
        if not args.force:
            before = len(files)
            files = [f for f in files if not already_done(pathlib.Path(f).stem)]
            print(f"resuming: {before - len(files)} already done, {len(files)} remaining")
    elif args.slug:
        files = [str(ROOT / "posts" / f"{args.slug}.html")]
    else:
        files = [args.file]

    consecutive_failures = 0
    for i, f in enumerate(files):
        if not pathlib.Path(f).exists():
            print(f"skip (not found): {f}", file=sys.stderr)
            continue
        _, all_failed = run_one(f, gk, qk, kk)
        if args.all and all_failed:
            consecutive_failures += 1
            if consecutive_failures >= 2:
                remaining = len(files) - i - 1
                print(f"stopping early: {consecutive_failures} posts in a row failed on every "
                      f"model — likely a quota wall, not a transient error. {remaining} posts "
                      f"left; re-run --all once quotas reset (this run already skips done posts).")
                break
        else:
            consecutive_failures = 0


if __name__ == "__main__":
    main()
