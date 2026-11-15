#!/usr/bin/env python3
"""Repair links to posts removed in phase 1 (out/gsc_index/phase1_remove.json: removed slug -> surviving slug or null).

    python3 tools/relink_retired.py --list                  # live posts that still link to a removed post
    python3 tools/relink_retired.py --write                 # write out/update-<today>-<slug>.html for those without a verified edition

A link to a removed post is pointed at the post that absorbed it; when nothing absorbed it (null), or the survivor is the
page itself, the anchor is dropped and its text kept. Nothing under posts/ or meta/ is touched. The function `repair()` is
also called by tools/viz_publish.py so verified editions get the same repair at publish time."""
import argparse, glob, json, pathlib, re, sys, datetime as dt

ROOT = pathlib.Path(__file__).resolve().parents[1]
P1 = json.load(open(ROOT / "out/gsc_index/phase1_remove.json"))
MANIFEST = {p["slug"]: p for p in json.load(open(ROOT / "meta/manifest.json"))["posts"].values()}
ANCHOR = re.compile(r'<a\b([^>]*?)href="(https?://[^"/]+(?:/\d{4}/\d\d)?/([a-z0-9-]+)\.html)(#[^"]*)?"([^>]*)>(.*?)</a>', re.S)


def repair(html, self_slug=None):
    def sub(m):
        slug = m.group(3)
        if slug not in P1:
            return m.group(0)
        tgt = P1[slug]
        if not tgt or tgt == self_slug or tgt not in MANIFEST:
            return m.group(6)
        return f'<a{m.group(1)}href="{MANIFEST[tgt]["url"]}"{m.group(5)}>{m.group(6)}</a>'
    return ANCHOR.sub(sub, html)


def current_source(slug):
    """Newest unpublished update file if one exists, else the live archive copy."""
    ups = sorted(glob.glob(str(ROOT / f"out/update-*-{slug}.html")))
    return pathlib.Path(ups[-1]) if ups else ROOT / f"posts/{slug}.html"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--list", action="store_true"); ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    today = dt.date.today().isoformat()
    n = 0
    for s in sorted(MANIFEST):
        if s in P1:
            continue
        src = current_source(s)
        if not src.exists():
            continue
        h = src.read_text(encoding="utf-8")
        new = repair(h, s)
        if new == h:
            continue
        n += 1
        done = (ROOT / f"out/viz/{s}/.verified").exists()
        print(f"{s}  [{'edition: repaired at publish' if done else src.name}]")
        if a.write and not done:
            (ROOT / f"out/update-{today}-{s}.html").write_text(new, encoding="utf-8")
    print(f"{n} posts")


if __name__ == "__main__":
    main()
