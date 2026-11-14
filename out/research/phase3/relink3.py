#!/usr/bin/env python3
"""Phase 3: repoint links from posts folded into a merged post (phase3_map.json) to that post.

    python3 out/research/phase3/relink3.py OUT_DATE        # e.g. 2026-11-15; run after the merged posts are written

Inputs: out/gsc_index/phase2_map.json (guide slug -> hub key, or null = no hub: unwrap links),
        out/research/phase2-hubs/hubs_published.json (hub key -> live URL; written by find_hubs.py),
        meta/manifest.json, posts/, and any pending out/update-*-<slug>.html (newest wins, so pending edits are kept).
Writes out/update-OUT_DATE-<slug>.html for each post that changes and prints posts needing a human look.
Links are matched by path (/YYYY/MM/slug.html) whatever the domain, since live posts still use the old blogspot host.
"""
import json, pathlib, re, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "tools"))
from blogger_api import migrate_links  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT_DATE = sys.argv[1]
MAP = json.load(open(ROOT / "out/gsc_index/phase3_map.json"))   # folded slug -> surviving slug
M = {p["slug"]: p for p in json.load(open(ROOT / "meta/manifest.json"))["posts"].values()}
HUBURL = {s: M[s]["url"] for s in set(MAP.values())}           # surviving slug -> live URL
PATH = {s: re.sub(r"^https?://[^/]+", "", M[s]["url"]) for s in MAP if s in M}
TARGET = {s: (HUBURL[k] if k else None) for s, k in MAP.items()}
HUB_SLUGS = {re.sub(r"^.*/", "", u)[:-5] for u in HUBURL.values()}


def href_re(path):
    return r'href="https?://[^/"]+' + re.escape(path) + r'(?:#[^"]*)?"'


def latest_source(slug):
    ups = sorted(ROOT.glob(f"out/update-*-{slug}.html"), key=lambda p: p.name)
    ups = [u for u in ups if not u.name.startswith(f"update-{OUT_DATE}-")]
    return ups[-1] if ups else ROOT / f"posts/{slug}.html"


def dedupe(t):
    """Within one related box or paragraph, keep the first link to a hub; drop later duplicates and their separator."""
    report = []
    def fix_block(m):
        blk = m.group(0)
        for u in set(HUBURL.values()):
            pat = r'<a\b[^>]*href="' + re.escape(u) + r'"[^>]*>(.*?)</a>'
            hits = list(re.finditer(pat, blk, re.S))
            if len(hits) < 2:
                continue
            for h in reversed(hits[1:]):
                pre = blk[:h.start()]
                sep = re.search(r'(\s*(?:&middot;|·|,|\||&bull;)\s*)$', pre)
                if sep:  # list-style: drop separator + anchor
                    blk = pre[:sep.start()] + blk[h.end():]
                else:    # prose: keep the words, drop the second link
                    blk = blk[:h.start()] + h.group(1) + blk[h.end():]
            report.append(u)
        return blk
    t = re.sub(r'<(p|li|div)\b[^>]*>(?:(?!</?(?:p|li|div)\b).)*', fix_block, t, flags=re.S)
    return t, report


def fix(slug, t):
    n0 = t
    if slug == "article-index-start-here":
        for s, p in PATH.items():
            t = re.sub(r'<li\b[^>]*>(?:(?!</li>).)*?class="ctitle" ' + href_re(p) + r'(?:(?!</li>).)*?</li>\s*', "", t, flags=re.S)
            t = re.sub(r'<li>\s*(?:<time\b[^>]*>[^<]*</time>\s*)?<a ' + href_re(p) + r'>(?:(?!</li>).)*?</li>\s*', "", t, flags=re.S)
            t = re.sub(r'\s*<a class="crel-a" ' + href_re(p) + r'>.*?</a>', "", t, flags=re.S)
        return t, n0 != t, []
    for s, p in PATH.items():
        ar = re.compile(r'<a\b[^>]*' + href_re(p) + r'[^>]*>(.*?)</a>', re.S)
        if not ar.search(t):
            continue
        tu = TARGET[s]
        if tu and slug not in HUB_SLUGS:
            t = ar.sub(lambda m: re.sub(href_re(p), f'href="{tu}"', m.group(0)), t)
            continue
        t = re.sub(r'<a\b[^>]*' + href_re(p) + r'[^>]*>.*?</a>\s*(?:&middot;|·)\s*', "", t, flags=re.S)
        t = re.sub(r'\s*(?:&middot;|·)\s*<a\b[^>]*' + href_re(p) + r'[^>]*>.*?</a>', "", t, flags=re.S)
        t = ar.sub(lambda m: m.group(1), t)
    t, rep = dedupe(t)
    return t, n0 != t, rep


changed, review = [], []
for slug in sorted(M):
    if slug in MAP or slug == "article-index-start-here":   # the index is rebuilt by rebuild_index.py
        continue
    src = latest_source(slug)
    if not src.exists():
        continue
    t = src.read_text()
    if not any(re.search(href_re(p), t) for p in PATH.values()):
        continue
    new, ch, rep = fix(slug, t)
    left = [s for s, p in PATH.items() if re.search(href_re(p), new)]
    if ch:
        new = migrate_links(new)   # never re-publish the old blogspot domain
        (ROOT / f"out/update-{OUT_DATE}-{slug}.html").write_text(new)
        changed.append(slug)
        print(f"{slug}  (from {src.relative_to(ROOT)})" + (f"  STILL LINKS {left}" if left else "") + (f"  deduped {len(rep)}" if rep else ""))
        if rep or left:
            review.append(slug)
print(f"{len(changed)} files written; {len(review)} to review by hand: {review}")
