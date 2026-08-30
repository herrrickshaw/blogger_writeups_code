#!/usr/bin/env python3
"""Second-opinion AdSense content-policy check via Gemini.

Complements tools/adsense_api.py (which reads the real account/site status
from Google) with an independent LLM read of whether a given post's *content*
would plausibly satisfy AdSense's publisher-content and thin-content
policies (support.google.com/adsense/answer/10015918 and .../48182,
support.google.com/publisherpolicies/answer/11035931). This is a model
opinion, not an official verdict -- only Google's own crawl decides the
real site status; use this to catch pages worth a human look before that
crawl runs, not as proof of compliance.

Reuses the same Gemini credential/prompt pattern as multi_model_factcheck.py.

    python3 tools/adsense_content_check.py --slug <slug>
    python3 tools/adsense_content_check.py --slugs slug1,slug2,slug3
"""
import argparse, html, json, os, pathlib, re, sys, time, urllib.error, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CREDS = pathlib.Path(os.path.expanduser("~/.config/market-secrets/credentials.env"))
GEMINI_MODEL = "gemini-flash-latest"
MISTRAL_MODEL = "mistral-small-latest"
MISTRAL_URL = "https://api.mistral.ai/v1/chat/completions"
UA = "masaladeutsch-adsense-check/1.0"

PROMPT = """You are reviewing one page of a published blog for compliance with Google
AdSense's content policies, specifically:
- "ads may not be placed on screens without publisher-content or with low-value content"
- pages must have "enough unique content" -- not thin, scraped, or doorway pages
- content should provide genuine informational or analytical value to a reader

Read the page text below (this is the FULL extracted body text, boilerplate
already stripped) and answer in exactly this structure:

VERDICT: <PASS or BORDERLINE or FAIL>
WORD COUNT ESTIMATE: <number>
REASONING: <2-3 sentences on whether this reads as substantive, original,
value-adding content vs thin/low-value content, per the policies above>
SPECIFIC CONCERNS: <any concrete issue -- e.g. mostly boilerplate, no real
analysis, feels like a stub -- or "none">

PAGE TEXT:
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
    s = re.sub(r"</t[dh]>", " | ", s, flags=re.I)
    s = re.sub(r"</tr>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


def ask_gemini(k, text, retries=3):
    body = {
        "contents": [{"parts": [{"text": PROMPT.format(text=text)}]}],
        "generationConfig": {"temperature": 0.1},
    }
    req_data = json.dumps(body).encode()
    for attempt in range(retries):
        req = urllib.request.Request(
            f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={k}",
            data=req_data,
            headers={"Content-Type": "application/json", "User-Agent": UA})
        try:
            d = json.loads(urllib.request.urlopen(req, timeout=120).read())
            cand = (d.get("candidates") or [{}])[0]
            return "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", [])).strip() or "[empty response]"
        except urllib.error.HTTPError as e:
            body_txt = e.read().decode()[:300]
            if e.code in (429, 500, 503) and attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            return f"[Gemini API error {e.code}: {body_txt}]"
        except (urllib.error.URLError, OSError) as e:
            if attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            return f"[Gemini network error: {e}]"


def ask_mistral(k, text):
    body = {
        "model": MISTRAL_MODEL,
        "messages": [{"role": "user", "content": PROMPT.format(text=text)}],
        "temperature": 0.1,
    }
    req = urllib.request.Request(
        MISTRAL_URL, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {k}", "User-Agent": UA})
    try:
        d = json.loads(urllib.request.urlopen(req, timeout=120).read())
        return d["choices"][0]["message"]["content"].strip()
    except urllib.error.HTTPError as e:
        return f"[Mistral API error {e.code}: {e.read().decode()[:300]}]"
    except (urllib.error.URLError, OSError, KeyError, IndexError) as e:
        return f"[Mistral error: {e}]"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug")
    ap.add_argument("--slugs", help="comma-separated list")
    ap.add_argument("--model", choices=["gemini", "mistral"], default="gemini")
    args = ap.parse_args()
    slugs = [args.slug] if args.slug else args.slugs.split(",")

    blob = creds()
    for slug in slugs:
        slug = slug.strip()
        path = ROOT / "posts" / f"{slug}.html"
        if not path.exists():
            print(f"=== {slug}: FILE NOT FOUND ===")
            continue
        text = extract_text(str(path))
        print(f"=== {slug} ({len(text)} raw chars) ===")
        if args.model == "gemini":
            print(ask_gemini(key("GEMINI_API_KEY", blob), text))
        else:
            print(ask_mistral(key("MISTRAL_API_KEY", blob), text))
        print()


if __name__ == "__main__":
    main()
