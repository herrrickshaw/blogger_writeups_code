#!/usr/bin/env python3
"""Add the "repository and data access on request" note to every how-to-use post.

Writes out/update-<date>-<slug>.html (never posts/): the source is the newest out/update-*-<slug>.html if one
exists, else posts/<slug>.html. The note goes just before the "About this article" disclaimer. Idempotent (skips a
source that already carries the marker). The blog has no comment box, so the link goes to the Contact page.

    python3 tools/add_access_note.py            # list what would be written
    python3 tools/add_access_note.py --write
"""
import glob
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATE = "2026-11-16"
MARK = 'data-gs-access-note="1"'
CONTACT = "https://blog.vertistratsolution.com/p/contact.html"
NOTE = (f'<div {MARK} style="border-left:4px solid #8a4b08;background:rgba(138,75,8,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px">'
        f'<b>Repository and data access.</b> Need the GitHub repository or the data files behind this guide? '
        f'Both are available on request: <a href="{CONTACT}">ask through the Contact page</a> and name the guide and what you need.</div>\n')


def source(slug):
    ups = sorted(glob.glob(str(ROOT / f"out/update-*-{slug}.html")))
    return pathlib.Path(ups[-1]) if ups else ROOT / f"posts/{slug}.html"


def main():
    write = "--write" in sys.argv
    retired = set(json.loads((ROOT / "out/gsc_index/phase1_remove.json").read_text()))
    slugs = sorted(p.stem for p in (ROOT / "posts").glob("how-to-use-*.html") if p.stem not in retired)
    done = skipped = 0
    for s in slugs:
        src = source(s)
        t = src.read_text(encoding="utf-8")
        if MARK in t:
            skipped += 1
            print("already has note:", s)
            continue
        m = re.search(r'<p class="disclaimer"', t)
        if not m or t.count('<p class="disclaimer"') != 1:
            print("NO UNIQUE ANCHOR:", s, src.name)
            continue
        out = ROOT / f"out/update-{DATE}-{s}.html"
        if write:
            out.write_text(t[:m.start()] + NOTE + t[m.start():], encoding="utf-8")
        done += 1
    print(f"{'wrote' if write else 'would write'} {done}, skipped {skipped}, of {len(slugs)}")


if __name__ == "__main__":
    main()
