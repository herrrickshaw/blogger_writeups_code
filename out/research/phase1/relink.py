#!/usr/bin/env python3
"""Phase 1 (10 Nov 2026): repoint or remove internal links to posts being merged away or unpublished.

For every live post (or its pending out/update-2026-11-10-<slug>.html, if a merge produced one):
  * article index: drop the whole <li> for any removed post (merged or not), and any related-link anchor to one;
  * links to a merged-away post elsewhere: repoint to the target post's URL;
  * links to an unpublished post with no target: in "Related on this blog" boxes, drop the anchor and its
    &middot; separator; in running text, unwrap the anchor and keep its words.
Writes out/update-2026-11-10-<slug>.html only for posts that changed and prints a report.
"""
import json, re, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
R = json.load(open(sys.argv[1]))                      # {slug: target_slug_or_null}
M = {p["slug"]: p for p in json.load(open(ROOT / "meta/manifest.json"))["posts"].values()}
URL = {s: M[s]["url"] for s in R}
TURL = {s: (M[t]["url"] if t else None) for s, t in R.items()}

def anchor_re(u):
    return re.compile(r'<a\b[^>]*href="' + re.escape(u) + r'(?:#[^"]*)?"[^>]*>(.*?)</a>', re.S)

def fix(slug, t):
    n0 = t
    if slug == "article-index-start-here":
        for s, u in URL.items():
            # whole index rows: <li ...> ... href=u ... </li> where the row's title link is u
            t = re.sub(r'<li\b[^>]*>(?:(?!</li>).)*?class="ctitle" href="' + re.escape(u) + r'"(?:(?!</li>).)*?</li>\s*', "", t, flags=re.S)
            t = re.sub(r'<li>\s*<a href="' + re.escape(u) + r'">(?:(?!</li>).)*?</li>\s*', "", t, flags=re.S)
            t = re.sub(r'\s*<a class="crel-a" href="' + re.escape(u) + r'">.*?</a>', "", t, flags=re.S)
        return t, n0 != t
    for s, u in URL.items():
        ar = anchor_re(u)
        if not ar.search(t):
            continue
        tu = TURL[s]
        if tu and tu not in (M.get(slug, {}).get("url"),):
            t = ar.sub(lambda m: m.group(0).replace(u, tu), t)
            continue
        # no target (or the target is this very post): remove from related boxes, unwrap in prose
        def repl(m):
            return m.group(1)
        # related box pattern: anchor followed or preceded by &middot;
        t = re.sub(r'<a\b[^>]*href="' + re.escape(u) + r'"[^>]*>.*?</a>\s*&middot;\s*', "", t, flags=re.S)
        t = re.sub(r'\s*&middot;\s*<a\b[^>]*href="' + re.escape(u) + r'"[^>]*>.*?</a>', "", t, flags=re.S)
        t = ar.sub(repl, t)
    t = t.replace("&mdash; two more pieces on this blog's tech and IT-services beat.",
                  "&mdash; another piece on this blog's tech and IT-services beat.")
    return t, n0 != t

changed = []
for slug, p in sorted(M.items()):
    if slug in R:
        continue
    upd = ROOT / f"out/update-2026-11-10-{slug}.html"
    src = upd if upd.exists() else ROOT / f"posts/{slug}.html"
    if not src.exists():
        continue
    t = src.read_text()
    if not any(u in t for u in URL.values()):
        continue
    new, ch = fix(slug, t)
    left = [s for s, u in URL.items() if u in new and not (TURL[s] and TURL[s] in new and False)]
    left = [s for s, u in URL.items() if u in new]
    if ch:
        upd.write_text(new)
        changed.append((slug, str(src.relative_to(ROOT)), left))
for c in changed:
    print(f"{c[0]}  (from {c[1]})" + (f"  STILL LINKS: {c[2]}" if c[2] else ""))
print(f"{len(changed)} files written")
