#!/usr/bin/env python3
"""Assign topic labels to every live post, so Blogger's label pages become hubs.

    python3 tools/apply_labels.py --plan          # show the assignment, write nothing
    python3 tools/apply_labels.py --apply         # write, skipping posts already labelled
    python3 tools/apply_labels.py --apply --limit 30

WHY
    Blogger generates a crawlable archive page per label (/search/label/<name>).
    This blog had ZERO labels on 99 posts, so twelve coherent topic clusters
    existed in the writing and nowhere in the navigation: no hub pages, and no
    internal links between related posts other than one hand-maintained index.

HOW THE ASSIGNMENT IS MADE
    Scored on H1/H2/H3 text only, not the body. Headings state what a piece is
    about; bodies on this blog contain long HSN tables whose repeated cell text
    swamps any term count (one boilerplate sentence appears 2,648 times across
    four posts). The H1 is weighted x3.

    A post takes every cluster scoring at least a third of its best score, up to
    three labels. Single-label posts are the common case; the multi-label ones
    are genuinely cross-cutting (ethanol is both Energy and Agriculture).

SAFETY
    - Sends `published` back explicitly, so a label write cannot re-date a post.
    - Skips any post that already has labels, so it is safe to re-run after
      hitting the daily write ceiling. Resume by running it again tomorrow.
    - --plan changes nothing and is the default way to review the taxonomy.
"""
import argparse
import collections
import glob
import html
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import blogger_api as B  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# Label -> heading keywords. Label names are reader-facing: they become the
# visible hub titles and the URL segment, so they are short and unambiguous.
TAXONOMY = {
    "Import Substitution": ["import substitution", "import-substitution", "hsn",
                            "localisation", "domestic capacity", "registry"],
    "Chemicals":           ["chemical", "petrochem", "dyes", "pigment",
                            "speciality", "specialty", "polymer", "acid"],
    "Energy & Fuels":      ["ethanol", "cbg", "biogas", "blending", "biofuel",
                            "crude", "petroleum", "refinery", "diesel", "petrol"],
    "Gas & LNG":           ["lng", "natural gas", "cgd", "pngrb", "regas",
                            "city gas", "pipeline", "gail"],
    "Agriculture & Fertilisers": ["fertiliser", "urea", "agri", "grain", "farm",
                                  "annadata", "kisan", "crop", "sugar", "paddy"],
    "Textiles":            ["textile", "apparel", "fibre", "charkha", "cotton", "mmf"],
    "Prices & Inflation":  ["wpi", "cpi", "inflation", "wholesale price",
                            "consumer price", "price index", "deflator"],
    "Climate & Carbon":    ["carbon", "ccts", "cbam", "green hydrogen",
                            "green credit", "emission", "climate", "esg"],
    "Mobility & EV":       ["electric vehicle", " ev ", "vehicle", "mobility",
                            "ev battery", "vehicle battery", "charging", "automobile"],
    "Trade & Tariffs":     ["export", "import", "tariff", "trade balance",
                            "trade deficit", "customs", "fta", "wto"],
    "Markets & Finance":   ["bond", "equity", "portfolio", "capital gains",
                            "yield", "securitis", "rupee", "currency", "fdi"],
    # "pli" as a bare 3-letter fragment matched inside ordinary words --
    # "split", "supplies", "multiply" -- and mislabelled unrelated posts
    # (caught on the-503020-rule-is-elizabeth-warrens.html, via "wants
    # split"). Space-bound / phrase-bound instead.
    "Industrial Policy":   [" pli ", "pli scheme", "production linked incentive",
                            "production-linked incentive", "scheme", "incentive",
                            "subsidy", "policy", "cluster", "investment promotion",
                            "sabha"],
}


# Utility pages are not topics. Left to the keyword scorer, "About the Author"
# scores Industrial Policy on the phrase "investment promotion" in the job
# title, and the index page scores whatever its longest section list mentions.
# Both would then appear in topic hubs alongside actual analysis.
OVERRIDE = {
    "about-author":                    [],
    "article-index-start-here":        [],
    # utility page, not an article -- was missing from this list, so it was
    # getting auto-scored against the topic taxonomy like a real post
    "the-masala-deutsch-shop-books-things": [],
    "ai-high-demand-launch-tracker":   ["AI Tracker"],
    "cgd-geographical-areas-district": ["Gas & LNG", "Industrial Policy"],
    "cold-chain-fuel-outlet-integrated-map": ["Gas & LNG", "Agriculture & Fertilisers"],
}


def headings(path):
    s = Path(path).read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", s, flags=re.S | re.I)
    rest = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", s, flags=re.S | re.I)
    rest += re.findall(r'class="(?:extitle|h2sub|standfirst)"[^>]*>(.*?)</p>', s, flags=re.S)
    strip = lambda xs: [html.unescape(re.sub(r"<[^>]+>", " ", x)) for x in xs]
    return " ".join(strip(h1) * 3 + strip(rest)).lower()


def labels_for(text, max_labels=3):
    score = {lab: sum(text.count(k) for k in keys) for lab, keys in TAXONOMY.items()}
    best = max(score.values())
    if best == 0:
        return []
    cut = max(1, best / 3)
    picked = sorted((l for l, s in score.items() if s >= cut),
                    key=lambda l: -score[l])[:max_labels]
    return picked


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    if not (args.plan or args.apply):
        ap.error("pass --plan or --apply")

    manifest = json.loads((ROOT / "meta" / "manifest.json").read_text())["posts"]
    by_slug = {r["slug"]: r for r in manifest.values()}

    plan = []
    for f in sorted(glob.glob(str(ROOT / "posts" / "*.html"))):
        slug = Path(f).stem
        rec = by_slug.get(slug)
        if not rec:
            continue                      # archived file with no live post
        labs = OVERRIDE[slug] if slug in OVERRIDE else labels_for(headings(f))
        plan.append((slug, rec["id"], labs))

    tally = collections.Counter(l for _, _, ls in plan for l in ls)
    print(f"posts: {len(plan)}   unlabelled by the rules: "
          f"{sum(1 for _, _, l in plan if not l)}\n")
    for lab, n in tally.most_common():
        print(f"   {n:3}  {lab}")
    if args.plan:
        print()
        for slug, _, labs in plan:
            print(f"   {slug[:52]:54} {', '.join(labs) or '— none —'}")
        return 0

    done = skipped = 0
    for slug, pid, labs in plan:
        if args.limit and done >= args.limit:
            print(f"\nstopping at --limit {args.limit}")
            break
        if not labs:
            continue
        try:
            p = B.api(f"/blogs/{B.BLOG_ID}/posts/{pid}")
        except SystemExit as e:
            print(f"  skip {slug}: {e}")
            continue
        if p.get("labels"):
            skipped += 1
            continue                      # already done — makes this resumable
        try:
            B.api(f"/blogs/{B.BLOG_ID}/posts/{pid}",
                  data={"id": pid, "title": p["title"], "content": p["content"],
                        "published": p["published"], "labels": labs},
                  method="PUT")
        except B.Ceiling as e:
            print(f"\ndaily write ceiling reached after {done} writes: {e}")
            print("re-run tomorrow — already-labelled posts are skipped")
            return 3
        done += 1
        print(f"  {done:3} {slug[:48]:50} {', '.join(labs)}")
        time.sleep(B.WRITE_GAP_SECONDS)
    print(f"\nlabelled {done} | already had labels {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
