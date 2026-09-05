#!/usr/bin/env python3
"""Ask a panel of non-Claude models to review the blog the way an AdSense
"low value content" reviewer would, from a dossier built out of the repo.

Companion to tools/multi_model_factcheck.py (same credentials file, same
providers). That tool checks one article's facts; this one checks the SITE:
trust pages, navigation, thin/duplicate/AI-scaled content signals, ad
placement, disclosure wording, E-E-A-T. Report-only -- it writes markdown for
a human to read and never edits anything.

    python3 tools/adsense_panel_review.py                # full panel run
    python3 tools/adsense_panel_review.py --dry-run      # build dossier, no API calls
    python3 tools/adsense_panel_review.py --dossier-only # write the dossier to paste
                                                         # into any chat model by hand

Needs ~/.config/market-secrets/credentials.env with GEMINI_API_KEY,
GROQ_API_KEY and MISTRAL_API_KEY (MOONSHOT_API_KEY / CEREBRAS_API_KEY are
optional). Run from the archive clone on a machine whose network can reach
those APIs; the sandbox that authored this cannot.

Output: out/adsense_panel_review.md (+ out/adsense_panel_dossier.txt).
Model output is an opinion, not a verified fact -- the same contract as the
fact-check tool.
"""
import argparse
import html
import json
import pathlib
import re
import statistics
import sys
import time
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import multi_model_factcheck as mm  # noqa: E402  (creds, key, extract_text, UA, models)

ROOT = HERE.parent
OUT_MD = ROOT / "out" / "adsense_panel_review.md"
OUT_DOSSIER = ROOT / "out" / "adsense_panel_dossier.txt"
SITE = "https://masaladeutsch.blogspot.com"

PROMPT = """You are reviewing a website exactly as a Google AdSense policy reviewer
would after the site received a "Low value content" rejection ("Your site does
not yet meet the criteria of use in the Google publisher network"). Judge it
against the AdSense Program Policies and Google's publisher content
guidelines: minimum content requirements, unique/original high-quality
content, thin or scaled/auto-generated content, duplicate content, required
trust pages (about, contact, privacy policy) reachable from navigation, ad
placement and density, user experience, and E-E-A-T (experience, expertise,
authoritativeness, trust).

Work ONLY from the dossier below. It contains measured facts about the site,
the full text of its four policy pages, the homepage's descriptive card, the
per-article disclosure line, and two complete sample articles (one short
chart-led piece, one typical long piece). Where something cannot be judged
from the dossier (mobile rendering, load speed, actual ad rendering, Blogger
console settings), say "cannot assess from dossier" instead of guessing.

Answer in exactly this structure. Quote the dossier when you cite evidence.
Do not pad a section: write "none" if you have nothing for it.

VERDICT: <likely to pass / borderline / likely to fail> -- <two sentences why>

BLOCKERS (would most likely still fail a review):
- <issue> -- <evidence from dossier> -- <specific fix> [confidence: high/medium/low]

IMPROVEMENTS (worth fixing before requesting review):
- <issue> -- <evidence> -- <fix> [confidence]

WHAT IS FINE (explicitly acceptable as it stands):
- <item> -- <evidence>

DISCLOSURE WORDING: <does the per-article line and the Editorial Policy page
read as honest human authorship with AI assistance, or as AI content at
scale? one paragraph, with a suggested rewrite only if needed>

DOSSIER:
{text}"""

# Pages as published (Blogger page slugs)
PAGES = [("About", "out/pages/about.html", "/p/about.html"),
         ("Contact", "out/pages/contact.html", "/p/contact.html"),
         ("Privacy Policy", "out/pages/privacy-policy.html", "/p/privacy-policy.html"),
         ("Editorial Policy & Disclaimer", "out/pages/disclaimer.html", "/p/disclaimer.html")]
THIN_SAMPLE = "india-environmental-clearances-state"   # ~470 words of prose, chart-led
SAMPLE_CHARS = 14000                                    # per sample article, keeps total < ~45k chars


def words(path):
    return len(mm.extract_text(path).split())


def live_posts():
    """(slug, title, path) for every live post, using the freshest local copy:
    a batch file in out/ads-v0/ or out/disclosure-v2/ that is newer than the
    posts/ mirror wins, because the mirror lags live until the next snapshot."""
    m = json.load(open(ROOT / "meta" / "manifest.json", encoding="utf-8"))["posts"]
    rows = []
    for v in m.values():
        p = ROOT / "posts" / f"{v['slug']}.html"
        if not p.exists():
            continue
        for d in ("ads-v0", "disclosure-v2"):
            c = ROOT / "out" / d / f"post-{v['slug']}.html"
            if c.exists() and c.stat().st_mtime > p.stat().st_mtime:
                p = c
                break
        rows.append((v["slug"], v["title"], p))
    return rows


def site_facts():
    rows = live_posts()
    counts = {s: words(p) for s, _, p in rows}
    wc = sorted(counts.values())
    thin = sorted((n, s) for s, n in counts.items() if n < 700)
    titles = [t.strip().lower() for _, t, _ in rows]
    dups = sorted({t for t in titles if titles.count(t) > 1})
    manual_ads = sum(1 for _, _, p in rows if "adsbygoogle" in p.read_text(encoding="utf-8", errors="replace"))
    ext_tools = sum(1 for _, _, p in rows if "jyoti-ai.com" in p.read_text(encoding="utf-8", errors="replace"))
    theme = (ROOT / "theme" / "theme.xml").read_text(encoding="utf-8", errors="replace")
    nav = re.search(r"pageListJson'><!\[CDATA\[(.*?)\]\]>", theme, re.S)
    nav_titles = []
    if nav:
        try:
            nav_titles = [v["title"] for v in json.loads(nav.group(1)).values()]
        except json.JSONDecodeError:
            nav_titles = ["(unparseable)"]
    foot = re.findall(r"class='site-foot-links'.*?</nav>", theme, re.S)
    foot_links = [html.unescape(t) for t in re.findall(r">([^<]+)</a>", foot[0])] if foot else []
    auto_ads = "adsbygoogle.js?client=" in theme[:3000]
    card = re.search(r"How this site works</div>(.*?)</div>\]\]>", theme, re.S)
    card_text = _plain(card.group(1)) if card else "(card not found in theme)"
    disc = ""
    for _, _, p in rows[:1]:
        m = re.search(r'<p class="disclaimer" data-gs-ai-disclosure[^>]*>(.*?)</p>', p.read_text(encoding="utf-8", errors="replace"), re.S)
        disc = _plain(m.group(1)) if m else "(none found)"
    return {
        "live_posts": len(rows), "median_words": int(statistics.median(wc)) if wc else 0,
        "under_700": thin, "under_1000": sum(1 for n in wc if n < 1000),
        "duplicate_titles": dups, "posts_with_manual_ad_units": manual_ads,
        "posts_with_external_assistive_links": ext_tools,
        "nav_titles": nav_titles, "footer_links": foot_links, "auto_ads_in_theme_head": auto_ads,
        "homepage_card": card_text, "disclosure_line": disc,
    }


def _plain(s):
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def build_dossier():
    f = site_facts()
    rows = live_posts()
    # typical article: the one closest to the median word count
    byw = sorted(((words(p), s, p) for s, _, p in rows), key=lambda r: abs(r[0] - f["median_words"]))
    typical = byw[0]
    thin_path = ROOT / "posts" / f"{THIN_SAMPLE}.html"
    parts = []
    parts.append("=== SITE ===\n"
                 f"URL: {SITE}  (Google Blogger, custom theme, English, India economics/policy analysis)\n"
                 f"Live posts: {f['live_posts']}  |  median visible words per post: {f['median_words']}\n"
                 f"Posts under 1,000 words: {f['under_1000']}  |  under 700 words: {len(f['under_700'])} "
                 f"({', '.join(f'{s} ({n}w)' for n, s in f['under_700'])})\n"
                 f"Duplicate titles among live posts: {f['duplicate_titles'] or 'none'}\n"
                 f"Top navigation: {', '.join(f['nav_titles']) or '(none)'}\n"
                 f"Footer links: {', '.join(f['footer_links']) or '(none)'}\n"
                 f"Pages: {', '.join(f'{t} ({SITE}{u})' for t, _, u in PAGES)}\n"
                 f"Ads: Auto ads script in theme head: {f['auto_ads_in_theme_head']}; posts carrying manual in-body ad units: "
                 f"{f['posts_with_manual_ad_units']} of {f['live_posts']} (ads are placed by Auto ads only)\n"
                 f"Every article carries: skip link, text-size + read-aloud accessibility bar with 3 external assistive-tech links "
                 f"({f['posts_with_external_assistive_links']} posts), Google Translate widget, 'All Articles (Index)' link, "
                 f"and a closing script that renders a per-post index plus an Amazon Associates 'further reading' box with disclosure.\n"
                 f"Homepage: post list shows snippets only; below it a 'How this site works' card and 32 topic chips.\n"
                 f"Homepage card text: {f['homepage_card']}\n"
                 f"Per-article disclosure line (identical on all posts): {f['disclosure_line']}\n"
                 "Recent history relevant to review: two duplicate copies of two new posts were live for under a day and were "
                 "deleted; a resume-style 'About the Author' POST was retired in favour of the About PAGE; nine short chart/registry "
                 "posts had their ad units removed; the per-article AI line was reworded (old wording said the article was 'researched "
                 "and written with AI assistance' and that 'AI-generated text can occasionally misstate figures or hallucinate').\n"
                 "Not in dossier / cannot be measured here: mobile rendering, page speed, Blogger search-description and robots "
                 "settings, ads.txt, AdSense console ad-load setting.")
    for title, path, url in PAGES:
        parts.append(f"=== PAGE: {title} ({SITE}{url}) ===\n" + mm.extract_text(ROOT / path))
    parts.append(f"=== SAMPLE ARTICLE A (short, chart-led): {THIN_SAMPLE} ({words(thin_path)} words) ===\n"
                 + mm.extract_text(thin_path)[:SAMPLE_CHARS])
    parts.append(f"=== SAMPLE ARTICLE B (typical length): {typical[1]} ({typical[0]} words; truncated to {SAMPLE_CHARS} chars) ===\n"
                 + mm.extract_text(typical[2])[:SAMPLE_CHARS])
    return "\n\n".join(parts), f


def _post(url, body, headers, label):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers)
    try:
        return json.loads(urllib.request.urlopen(req, timeout=180).read()), None
    except urllib.error.HTTPError as e:
        return None, f"[{label} API error {e.code}: {e.read().decode()[:300]}]"
    except (urllib.error.URLError, OSError) as e:
        return None, f"[{label} network error: {e}]"


def ask_openai_compat(label, url, model, k, text):
    d, err = _post(url, {"model": model, "temperature": 0.1,
                         "messages": [{"role": "user", "content": PROMPT.format(text=text)}]},
                   {"Content-Type": "application/json", "Authorization": f"Bearer {k}", "User-Agent": mm.UA}, label)
    if err:
        return err
    try:
        return d["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError):
        return f"[{label} unexpected response: {json.dumps(d)[:300]}]"


def ask_gemini(k, text):
    d, err = _post(f"https://generativelanguage.googleapis.com/v1beta/models/{mm.GEMINI_MODEL}:generateContent?key={k}",
                   {"contents": [{"parts": [{"text": PROMPT.format(text=text)}]}],
                    "generationConfig": {"temperature": 0.1}},
                   {"Content-Type": "application/json", "User-Agent": mm.UA}, "Gemini")
    if err:
        return err
    cand = (d.get("candidates") or [{}])[0]
    return "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", [])).strip() or "[empty response]"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="build the dossier and report sizes; no API calls")
    ap.add_argument("--dossier-only", action="store_true", help="write out/adsense_panel_dossier.txt and stop")
    args = ap.parse_args()

    dossier, facts = build_dossier()
    OUT_DOSSIER.parent.mkdir(parents=True, exist_ok=True)
    OUT_DOSSIER.write_text(dossier, encoding="utf-8")
    print(f"dossier: {len(dossier):,} chars (~{len(dossier)//4:,} tokens) -> {OUT_DOSSIER}")
    print(f"  live posts {facts['live_posts']}, median {facts['median_words']} words, "
          f"{len(facts['under_700'])} under 700 words, nav: {', '.join(facts['nav_titles'])}")
    if args.dry_run or args.dossier_only:
        return

    blob = mm.creds()
    panel = [
        ("Mistral " + mm.MISTRAL_MODEL, lambda t, k=mm.key("MISTRAL_API_KEY", blob):
            ask_openai_compat("Mistral", mm.MISTRAL_URL, mm.MISTRAL_MODEL, k, t)),
        ("Groq " + mm.GROQ_MODELS[0], lambda t, k=mm.key("GROQ_API_KEY", blob):
            ask_openai_compat("Groq", "https://api.groq.com/openai/v1/chat/completions", mm.GROQ_MODELS[0], k, t)),
        ("Gemini " + mm.GEMINI_MODEL, lambda t, k=mm.key("GEMINI_API_KEY", blob): ask_gemini(k, t)),
    ]
    kk = mm.key_optional("MOONSHOT_API_KEY", blob)
    if kk:
        panel.append(("Kimi " + mm.KIMI_MODEL, lambda t, k=kk: ask_openai_compat("Kimi", mm.KIMI_URL, mm.KIMI_MODEL, k, t)))
    ck = mm.key_optional("CEREBRAS_API_KEY", blob)
    if ck:
        panel.append(("Cerebras " + mm.CEREBRAS_MODEL, lambda t, k=ck: ask_openai_compat("Cerebras", mm.CEREBRAS_URL, mm.CEREBRAS_MODEL, k, t)))

    stamp = time.strftime("%Y-%m-%d %H:%M %Z")
    out = [f"# AdSense panel review -- {stamp}\n",
           f"Dossier: {len(dossier):,} chars; {facts['live_posts']} live posts, median {facts['median_words']} words, "
           f"{len(facts['under_700'])} under 700 words. Full dossier: `out/adsense_panel_dossier.txt`.\n",
           "Model output is opinion, not verified fact. Read the BLOCKERS across models for agreement first.\n"]
    for label, fn in panel:
        print(f"asking {label} ...", flush=True)
        ans = fn(dossier)
        out.append(f"\n## {label}\n\n{ans}\n")
        time.sleep(2)
    OUT_MD.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
