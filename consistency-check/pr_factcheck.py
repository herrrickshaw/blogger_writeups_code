#!/usr/bin/env python3
"""Cross-vendor fact/interpretation check on new post drafts in a pull request.

Stage 1.5 of the draft-review pipeline (see draft-review.yml and pr_review.py):
sits between the deterministic static-rule check and the PR-comment routing
step. Sends each changed out/**/*.html draft's plain text to Gemini, Mistral,
and OpenAI independently, and asks each to flag factual and interpretation
errors -- the same two-category prompt tools/multi_model_factcheck.py already
uses against published posts, reused here rather than reinvented, and pointed
at drafts before they're merged instead of after they're live.

Unlike tools/multi_model_factcheck.py (which reads local credentials from
~/.config/market-secrets/credentials.env on the maintainer's own machine),
this script reads API keys from environment variables, because a GitHub
Actions runner has no access to that file. It expects (any subset of):

    GEMINI_API_KEY, MISTRAL_API_KEY, OPENAI_API_KEY

as GitHub Actions repository secrets, wired into the workflow's `env:` block.
A provider whose key is unset or empty is skipped, not treated as an error --
this degrades cleanly to "checked with whatever's configured" rather than
failing outright, the same shape as multi_model_factcheck.py's optional-vs-
required provider split.

CLAUDE.md's rule 3 applies here exactly as it does to the existing tool:
"model output is not a verified fact... every flagged claim needs primary-
source confirmation before it changes anything." This script never fails the
CI check on its own findings (see the routing note in draft-review.yml) --
it only adds a clearly-labelled section to the PR comment for a human to
weigh, and never edits, drafts, or publishes anything itself.

    python3 tools/../consistency-check/pr_factcheck.py --base-ref <sha> --head-ref <sha>
"""
import argparse
import html
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

GEMINI_MODEL = "gemini-flash-latest"
MISTRAL_MODEL = "mistral-small-latest"
# Pin to a specific, long-stable OpenAI model rather than an alias that could
# silently change. If your account has access to something newer/cheaper,
# update this constant -- it isn't read from an env var on purpose, so a
# model swap is a reviewed code change, not a silent config drift.
OPENAI_MODEL = "gpt-4o-mini"

MAX_CHARS = 100_000  # see multi_model_factcheck.py's note on per-request ceilings

PROMPT = """You are fact-checking a DRAFT article before it is published, for an
India-focused economics and industrial-policy blog. Read the draft text below and
report two DISTINCT kinds of problems only. Do not summarize the article and do
not comment on style.

1. FACTUAL ERRORS — a specific number, date, name, or event stated in the
   draft that is wrong, outdated, or that you cannot verify against what you
   know. Quote the exact claim.
2. INTERPRETATION ERRORS — a fact that is probably correct but is used to
   support a conclusion it does not actually support: a false causal claim, an
   apples-to-oranges comparison, an extrapolation beyond what the data shows,
   or double-counting. Quote the claim and explain the gap in reasoning.

If you find nothing in a category, write "none found" — do not invent a
problem to fill the section. Do not flag stylistic or formatting issues, and
do not flag a claim that the draft itself already attributes to a named
source with an appropriate hedge (e.g. "trade press reports," "not
independently verified") -- that is the draft being careful, not being wrong.

Answer in exactly this structure:

FACTUAL ERRORS:
- <claim> — <what's wrong, and why> [confidence: high/medium/low]
(repeat, or "none found")

INTERPRETATION ERRORS:
- <claim> — <the reasoning gap> [confidence: high/medium/low]
(repeat, or "none found")

DRAFT TEXT:
{text}"""


def _sh(*args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def changed_out_html_files(base_ref, head_ref):
    out = _sh("git", "diff", "--name-only", f"{base_ref}...{head_ref}")
    return [
        line for line in out.splitlines()
        if line and line.startswith("out/") and line.endswith(".html")
    ]


def file_at(ref, path):
    try:
        return _sh("git", "show", f"{ref}:{path}")
    except subprocess.CalledProcessError:
        return None


def extract_text(html_body):
    """Same HTML-to-plain-text approach as multi_model_factcheck.py's
    extract_text(), so a draft is fact-checked the same way its published
    version will be later -- strips script/style, keeps table cells readable,
    drops struck-through/retracted text so a self-correction isn't re-flagged."""
    s = html_body
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<style.*?</style>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<s>.*?</s>", " ", s, flags=re.S | re.I)
    s = re.sub(r"</t[dh]>", " | ", s, flags=re.I)
    s = re.sub(r"</tr>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()[:MAX_CHARS]


def ask_gemini(k, text):
    body = {
        "contents": [{"parts": [{"text": PROMPT.format(text=text)}]}],
        "generationConfig": {"temperature": 0.1},
    }
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={k}",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "User-Agent": UA},
    )
    try:
        d = json.loads(urllib.request.urlopen(req, timeout=120).read())
    except urllib.error.HTTPError as e:
        return f"[Gemini API error {e.code}: {e.read().decode()[:300]}]"
    except (urllib.error.URLError, OSError) as e:
        return f"[Gemini network error: {e}]"
    cand = (d.get("candidates") or [{}])[0]
    return "".join(
        p.get("text", "") for p in cand.get("content", {}).get("parts", [])
    ).strip() or "[empty response]"


def _openai_compatible(url, model, k, text, label):
    body = {
        "model": model,
        "messages": [{"role": "user", "content": PROMPT.format(text=text)}],
        "temperature": 0.1,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {k}",
            "User-Agent": UA,
        },
    )
    try:
        d = json.loads(urllib.request.urlopen(req, timeout=120).read())
    except urllib.error.HTTPError as e:
        return f"[{label} API error {e.code}: {e.read().decode()[:300]}]"
    except (urllib.error.URLError, OSError) as e:
        return f"[{label} network error: {e}]"
    try:
        return d["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError):
        return f"[{label} unexpected response: {json.dumps(d)[:300]}]"


def ask_mistral(k, text):
    return _openai_compatible(
        "https://api.mistral.ai/v1/chat/completions", MISTRAL_MODEL, k, text, "Mistral"
    )


def ask_openai(k, text):
    return _openai_compatible(
        "https://api.openai.com/v1/chat/completions", OPENAI_MODEL, k, text, "OpenAI"
    )


PROVIDERS = [
    ("Gemini", "GEMINI_API_KEY", ask_gemini),
    ("Mistral", "MISTRAL_API_KEY", ask_mistral),
    ("OpenAI", "OPENAI_API_KEY", ask_openai),
]


def render_markdown(per_file_results, configured, skipped):
    lines = []
    if skipped:
        lines.append(
            f"_Skipped (no API key configured): {', '.join(skipped)}._\n"
        )
    if not configured:
        lines.append(
            "No fact-check providers configured — add `GEMINI_API_KEY`, "
            "`MISTRAL_API_KEY`, and/or `OPENAI_API_KEY` as repository secrets "
            "to enable this stage."
        )
        return "\n".join(lines)
    if not per_file_results:
        lines.append("No changed `out/**` drafts to fact-check.")
        return "\n".join(lines)
    lines.append(
        "> ⚠️ **Model output is not a verified fact.** Every claim below needs "
        "primary-source confirmation before it changes anything (see `CLAUDE.md` "
        "rule 3) — treat this as a second set of eyes, not a verdict.\n"
    )
    for f, by_provider in per_file_results.items():
        lines.append(f"**`{f}`**\n")
        for provider, resp in by_provider.items():
            lines.append(f"<details><summary>{provider}</summary>\n\n{resp}\n\n</details>\n")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base-ref", required=True)
    ap.add_argument("--head-ref", required=True)
    args = ap.parse_args()

    keys = {}
    skipped = []
    for label, env_name, _fn in PROVIDERS:
        v = os.environ.get(env_name, "").strip()
        if v:
            keys[label] = v
        else:
            skipped.append(label)

    files = changed_out_html_files(args.base_ref, args.head_ref)
    results = {}
    if keys:
        for f in files:
            body = file_at(args.head_ref, f)
            if body is None:
                continue
            text = extract_text(body)
            if not text:
                continue
            results[f] = {}
            for label, _env_name, fn in PROVIDERS:
                if label not in keys:
                    continue
                results[f][label] = fn(keys[label], text)

    print(render_markdown(results, configured=bool(keys), skipped=skipped))
    # This stage never fails the check -- see the module docstring and
    # CLAUDE.md rule 3. Findings are advisory only.
    sys.exit(0)


if __name__ == "__main__":
    main()
