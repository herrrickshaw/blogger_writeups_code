#!/usr/bin/env python3
"""Rebuild the article-index post body while keeping what was injected after the original build.

tools/build_index_page.py makes a clean index, but the live index post
(posts/article-index-start-here.html) also carries pieces added later by other tools: the
.artx wrapper and its typography/table CSS, the Google Translate widget, and the AI
disclosure at the foot. Replacing the live body with a fresh build drops them.

This script diffs the live body against a fresh build and takes the fresh build everywhere
except where the live body has one of those injected pieces, which it keeps.

    python3 tools/index_graph.py --json /tmp/graph.json
    python3 tools/build_index_page.py --graph /tmp/graph.json --out /tmp/fresh-index.html
    python3 tools/splice_index_injections.py --fresh /tmp/fresh-index.html --out out/article-index-updated.html

Never writes to posts/ or to the live blog. Publish the output with tools/blogger_api.py update.
"""
import argparse
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKERS = ("gs-typo-unify", ".artx", "google_translate", "ai-disclosure", "gs-table-v1", ".post-body", 'class="artx')


def merge(live: str, fresh: str) -> str:
    a, b = live.splitlines(keepends=True), fresh.splitlines(keepends=True)
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        old_chunk = "".join(a[i1:i2])
        injected = any(m in old_chunk for m in MARKERS)
        if tag == "equal":
            out.append(old_chunk)
        elif tag == "insert":
            out.append("".join(b[j1:j2]))
        elif tag == "delete":
            if injected:
                out.append(old_chunk)
        else:  # replace
            out.append(old_chunk if injected else "".join(b[j1:j2]))
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", default=str(ROOT / "posts" / "article-index-start-here.html"))
    ap.add_argument("--fresh", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    live = Path(args.live).read_text(encoding="utf-8")
    fresh = Path(args.fresh).read_text(encoding="utf-8")
    merged = merge(live, fresh)
    for m in ("gs-typo-unify-v1", "google_translate_element", "data-gs-ai-disclosure-v1", 'class="artx idx"'):
        if m in live and m not in merged:
            sys.exit(f"refusing to write: injected piece lost: {m}")
    live_links = set(re.findall(r'href="(https://blog\.vertistratsolution\.com/20\d\d/\d\d/[^"#]+\.html)"', live))
    new_links = set(re.findall(r'href="(https://blog\.vertistratsolution\.com/20\d\d/\d\d/[^"#]+\.html)"', merged))
    dropped = live_links - new_links
    Path(args.out).write_text(merged, encoding="utf-8")
    print(f"wrote {args.out} ({len(merged):,} bytes): {len(new_links)} article links, {len(new_links - live_links)} added, {len(dropped)} dropped")
    if dropped:
        print("dropped links (check they are retired posts):")
        for u in sorted(dropped)[:20]:
            print("  ", u)


if __name__ == "__main__":
    main()
