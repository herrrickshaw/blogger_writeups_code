#!/usr/bin/env python3
"""Extract geography and an entity graph from the archived posts.

    python3 tools/index_graph.py --report          # what it found, human-readable
    python3 tools/index_graph.py --json out.json   # machine-readable, for the index builder

WHAT IT EXTRACTS

  geography  Countries and Indian states each post is ABOUT. Mentions are scored
             with headings weighted x4 over body text, because a post that names
             Germany in its subhead is about Germany and one that mentions it once
             in a source note is not. India is tracked separately: nearly every
             post is about India, so counting it as a geography would produce one
             bucket of 97 and twelve of nothing.

  entities   The nouns that actually connect these posts to each other: HS codes
             and chapters, named commodities, and named schemes and institutions.
             Deliberately NOT free-text keywords — those produce edges between any
             two posts that both say "policy".

WHY THE BODY TEXT IS DOWN-WEIGHTED SO HARD
    Four of the HSN registry posts repeat one boilerplate sentence 2,648 times
    inside their tables. Any raw term count is dominated by table furniture. The
    fix is heading weighting plus per-post presence rather than frequency: a term
    counts once per post, not once per occurrence.
"""
import argparse
import collections
import glob
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

COUNTRIES = {
    "China": ["china", "chinese"], "United States": ["united states", "u.s.", " usa", "america"],
    "Russia": ["russia"], "Germany": ["germany", "german"], "Japan": ["japan"],
    "South Korea": ["south korea", "korea"], "Brazil": ["brazil"], "Netherlands": ["netherland"],
    "United Kingdom": ["united kingdom", " uk ", "britain"], "France": ["france"],
    "Singapore": ["singapore"], "UAE": ["united arab emirates", "uae"], "Saudi Arabia": ["saudi"],
    "Nepal": ["nepal"], "Bhutan": ["bhutan"], "Sri Lanka": ["sri lanka"],
    "Bangladesh": ["bangladesh"], "Pakistan": ["pakistan"], "Myanmar": ["myanmar"],
    "Australia": ["australia"], "Indonesia": ["indonesia"], "Vietnam": ["vietnam"],
    "Iraq": ["iraq"], "Iran": ["iran"], "Qatar": ["qatar"], "Norway": ["norway", "norwegian"],
    "Switzerland": ["switzerland", "swiss"], "Italy": ["italy"], "Spain": ["spain"],
    "Turkiye": ["turkiye", "turkey"], "Egypt": ["egypt"], "Nigeria": ["nigeria"],
    "South Africa": ["south africa"], "Tanzania": ["tanzania"], "Kenya": ["kenya"],
    "Canada": ["canada"], "Mexico": ["mexico"], "Poland": ["poland"],
    "European Union": ["european union", " eu ", "europe"],
}
STATES = {
    "Maharashtra": ["maharashtra"], "Gujarat": ["gujarat"], "Uttar Pradesh": ["uttar pradesh"],
    "Madhya Pradesh": ["madhya pradesh"], "Tamil Nadu": ["tamil nadu"], "Karnataka": ["karnataka"],
    "Rajasthan": ["rajasthan"], "Punjab": ["punjab"], "Haryana": ["haryana"], "Bihar": ["bihar"],
    "West Bengal": ["west bengal"], "Odisha": ["odisha"], "Telangana": ["telangana"],
    "Andhra Pradesh": ["andhra pradesh"], "Kerala": ["kerala"], "Assam": ["assam"],
    "Chhattisgarh": ["chhattisgarh"], "Jharkhand": ["jharkhand"], "Uttarakhand": ["uttarakhand"],
    "Goa": ["goa"], "Himachal Pradesh": ["himachal"],
}
ENTITIES = {
    "Ethanol": ["ethanol"], "Compressed biogas": ["compressed biogas", "cbg"],
    "LNG": ["lng"], "Natural gas": ["natural gas"], "Crude oil": ["crude oil", "crude"],
    "Diesel": ["diesel", "hsd"], "Petrol": ["petrol", "motor spirit"],
    "Urea": ["urea"], "Fertiliser subsidy": ["fertiliser subsid", "nutrient based subsid"],
    "Green hydrogen": ["green hydrogen"], "Carbon credits": ["carbon credit", "ccts"],
    "CBAM": ["cbam"], "PLI scheme": ["production linked", "pli "],
    "GST": ["gst"], "Customs duty": ["customs duty", "basic customs"],
    "Anti-dumping": ["anti-dumping", "antidumping"],
    "WPI": ["wpi", "wholesale price index"], "CPI": ["cpi", "consumer price index"],
    "Rupee": ["rupee", "inr/usd"], "FDI": ["foreign direct investment", "fdi"],
    "MSP": ["minimum support price", " msp"], "FCI": ["food corporation", "fci"],
    "City gas distribution": ["city gas", "cgd"], "PNGRB": ["pngrb"], "PPAC": ["ppac"],
    "TradeStat": ["tradestat", "dgci"], "Electric vehicles": ["electric vehicle", "ev "],
    "Textiles": ["textile", "apparel"], "Rare earths": ["rare earth"],
    "Specialty chemicals": ["speciality chemical", "specialty chemical"],
    "Import substitution": ["import substitution"],
    "Sugar": ["sugarcane", "sugar mill"], "Coal": ["coal"], "Steel": ["steel"],
}


def parts(path):
    s = Path(path).read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r'class="disclaimer".*?</p>', " ", s, flags=re.S)
    heads = re.findall(r"<h[1-3][^>]*>(.*?)</h[1-3]>", s, flags=re.S | re.I)
    heads += re.findall(r'class="(?:standfirst|extitle|h2sub|eyebrow)"[^>]*>(.*?)</p>', s, flags=re.S)
    strip = lambda x: html.unescape(re.sub(r"<[^>]+>", " ", x))
    body = strip(s)
    return strip(" ".join(heads)).lower(), body.lower(), body


def score(gaz, head, body):
    """Presence-weighted: headings count 4, body counts 1, capped per post."""
    out = {}
    for name, keys in gaz.items():
        h = sum(head.count(k) for k in keys)
        b = sum(body.count(k) for k in keys)
        v = h * 4 + min(b, 6)          # cap body so table repetition cannot dominate
        if v:
            out[name] = v
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--json", metavar="PATH")
    args = ap.parse_args()

    manifest = json.loads((ROOT / "meta" / "manifest.json").read_text())["posts"]
    by_slug = {r["slug"]: r for r in manifest.values()}

    posts = {}
    for f in sorted(glob.glob(str(ROOT / "posts" / "*.html"))):
        slug = Path(f).stem
        rec = by_slug.get(slug)
        if not rec:
            continue
        head, body, _ = parts(f)
        g = score(COUNTRIES, head, body)
        st = score(STATES, head, body)
        en = score(ENTITIES, head, body)
        posts[slug] = {
            "title": rec["title"], "url": rec["url"], "published": rec.get("published", "")[:10],
            # A geography counts as a subject only if it clears a floor. Every
            # trade post mentions China somewhere; few are about China.
            "countries": sorted([k for k, v in g.items() if v >= 6], key=lambda k: -g[k]),
            "states": sorted([k for k, v in st.items() if v >= 4], key=lambda k: -st[k]),
            "entities": sorted([k for k, v in en.items() if v >= 5], key=lambda k: -en[k])[:8],
            "_g": g, "_e": en,
        }

    # Edges: two posts are related if they share entities. Weight by how rare the
    # shared entity is across the corpus, so "GST" links less strongly than
    # "Rare earths".
    df = collections.Counter()
    for p in posts.values():
        for e in p["entities"]:
            df[e] += 1
    N = len(posts)
    for slug, p in posts.items():
        sims = []
        for other, q in posts.items():
            if other == slug:
                continue
            shared = set(p["entities"]) & set(q["entities"])
            if not shared:
                continue
            w = sum(1.0 / df[e] for e in shared)
            geo = set(p["countries"]) & set(q["countries"])
            w += 0.25 * len(geo)
            sims.append((w, other, sorted(shared)))
        sims.sort(reverse=True)
        p["related"] = [{"slug": s, "shared": sh, "w": round(w, 3)} for w, s, sh in sims[:4]]
        p.pop("_g"); p.pop("_e")

    if args.json:
        Path(args.json).write_text(json.dumps(posts, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"wrote {args.json} ({len(posts)} posts)")

    if args.report:
        cg = collections.Counter(c for p in posts.values() for c in p["countries"])
        cs = collections.Counter(c for p in posts.values() for c in p["states"])
        ce = collections.Counter(e for p in posts.values() for e in p["entities"])
        print(f"posts {len(posts)}\n")
        print("== COUNTRIES (posts about) ==")
        for k, v in cg.most_common(20):
            print(f"   {v:3}  {k}")
        print("\n== INDIAN STATES ==")
        for k, v in cs.most_common(15):
            print(f"   {v:3}  {k}")
        print("\n== ENTITIES ==")
        for k, v in ce.most_common(25):
            print(f"   {v:3}  {k}")
        nogeo = [s for s, p in posts.items() if not p["countries"] and not p["states"]]
        print(f"\nposts with no geography beyond India: {len(nogeo)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
