#!/usr/bin/env python3
"""Rebuild the article-index post body so it matches what is actually live.

Two jobs:
  1. Repoint entries whose post has moved (Blogger never releases a slug, so a
     republished post leaves a dead link behind in the index).
  2. Add live posts that were never listed, into the right topic section.

Reads the current index body from ../posts/, writes the updated body to
out/article-index-updated.html for injection into Blogger. Never edits the live
site itself.

    python3 tools/update_index.py
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "posts" / "article-index-start-here.html"
MANIFEST = ROOT / "meta" / "manifest.json"
OUT = ROOT / "out"

# Section ids as they appear in the index body.
SECTIONS = {
    "t0": "Currency & Monetary Policy",
    "t1": "Trade & Import Substitution",
    "t2": "Chemicals & Petrochemicals",
    "t3": "Energy, Fuels & Mobility",
    "t4": "Agriculture & Food Security",
    "t5": "Textiles",
    "t6": "Climate, Carbon & Circularity",
    "t7": "Industrial Policy & Clearances",
    "t8": "Prices & Macro Indicators",
    "t9": "Markets",
}

# Where each unlisted post belongs. Assigned by hand — a keyword guess would put
# "Rooftop Solar" under Climate and the ethanol post under Agriculture, both of
# which read wrong next to their neighbours.
PLACEMENT = {
    "europes-export-credit-agencies-are": "t1",
    "fourteen-years-of-indian-wholesale": "t8",
    "indias-ethanol-surplus-isnt-going-to": "t3",
    "indias-oil-fields-are-running-down-3696": "t3",
    "indias-state-incentive-war-gujarats": "t7",
    "rooftop-solar-is-working-household": "t3",
    "where-indias-green-hydrogen-bets-are": "t3",
}

# Posts that moved: old URL still in the index -> slug of the live post.
MOVED = {
    "https://masaladeutsch.blogspot.com/2026/08/chemical-import-substitution-full-hsn-8.html":
        "chemical-import-substitution-hsn-8-registry",
    "https://masaladeutsch.blogspot.com/2026/07/india-mineral-oil-hsn-ch27-trade.html":
        "india-mineral-oil-hsn-ch27-trade",
}

ITEM = (
    '<a class="ix-item" href="{url}">'
    '<span class="ix-t">{title}</span>'
    '<span class="ix-d">{date}</span></a>'
)


def esc(s):
    return (
        s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        .replace("—", "&mdash;").replace("’", "&#8217;").replace("×", "&times;")
    )


def main():
    body = INDEX.read_text(encoding="utf-8")
    live = {r["slug"]: r for r in json.loads(MANIFEST.read_text())["posts"].values()}
    before_items = len(re.findall(r'class="ix-item"', body))

    # 1. repoint moved posts
    repointed = 0
    for old_url, slug in MOVED.items():
        rec = live.get(slug)
        if rec is None:
            sys.exit(f"moved target {slug!r} is not live — refusing to write a dead link")
        if old_url not in body:
            print(f"  note  {old_url} not in index (already fixed?)")
            continue
        body = body.replace(old_url, rec["url"])
        repointed += 1
        print(f"  move  {old_url.rsplit('/', 1)[-1]} -> {rec['url'].rsplit('/', 1)[-1]}")

    # 2. add unlisted posts
    added = 0
    for slug, sec in PLACEMENT.items():
        rec = live.get(slug)
        if rec is None:
            sys.exit(f"{slug!r} is not live — refusing to add a dead link")
        if rec["url"] in body:
            print(f"  note  {slug} already listed")
            continue
        item = ITEM.format(
            url=rec["url"], title=esc(rec["title"]), date=rec["published"][:10]
        )
        # Append inside the section's item container, immediately before the
        # </div></details> that closes it.
        pat = re.compile(
            r'(<details class="ix-sec" id="' + sec + r'"[\s\S]*?)(</div></details>)'
        )
        m = pat.search(body)
        if not m:
            sys.exit(f"could not locate section {sec} for {slug}")
        body = body[: m.start(2)] + item + body[m.start(2):]
        added += 1
        print(f"  add   [{SECTIONS[sec]}] {rec['title'][:56]}")

    after_items = len(re.findall(r'class="ix-item"', body))
    assert after_items == before_items + added, "item count drifted"

    # every href in the result must be a live post (or the index itself)
    urls = set(re.findall(r'href="(https://masaladeutsch\.blogspot\.com/[^"]+)"', body))
    live_urls = {r["url"] for r in live.values()}
    dead = [u for u in urls if u not in live_urls]
    if dead:
        sys.exit("still-dead links:\n  " + "\n  ".join(dead))

    missing = [r["url"] for s, r in live.items() if r["url"] not in urls
               and s != "article-index-start-here"]

    OUT.mkdir(exist_ok=True)
    dest = OUT / "article-index-updated.html"
    dest.write_text(body, encoding="utf-8")
    print(f"\n{repointed} repointed, {added} added | items {before_items} -> {after_items}")
    print(f"dead links: 0 | live posts still unlisted: {len(missing)}")
    for u in missing:
        print("   unlisted:", u)
    print(f"\nwrote {dest}")


if __name__ == "__main__":
    main()
