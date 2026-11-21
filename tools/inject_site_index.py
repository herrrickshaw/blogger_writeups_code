#!/usr/bin/env python3
"""Append the site-index accordion to the foot of every live post.

    python3 tools/inject_site_index.py --plan     # who gets it, who is skipped
    python3 tools/inject_site_index.py --apply    # write, resumable

WHY ONE LINE PER POST AND NOT THE ACCORDION ITSELF
    The theme cannot be edited (browser access to blogger.com is revoked and
    Blogger has no theme API — seven endpoints tested 2026-08-08), so the only
    surface present on every article is the post body. Pasting the full
    accordion into ~97 posts would mean ~97 edits every time it changes. Each
    post instead gets a two-tag stub:

        <div id="gs-idx"></div><script defer src=".../accordion.js"></script>

    The script lives once, on GitHub Pages, and builds the accordion at view
    time from the blog's own feeds — it discovers the label list from the main
    feed, so even a brand-new topic appears on every page with zero edits.

SAFETY
    - Marker gs-idx: posts already carrying it are skipped, so the run is
      resumable after the daily write ceiling and idempotent if re-run.
    - published and labels are sent back explicitly on every PUT; a PUT is a
      whole-resource replace and omitting either would silently destroy it.
    - The index post is excluded (it has the richer accordion already) and so
      is anything unpublished.
"""
import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
ROOT = Path(__file__).resolve().parent.parent
import blogger_api as B  # noqa: E402

STUB = ('\n<div id="gs-idx"></div>'
        '<script defer="defer" '
        'src="https://blog.vertistratsolution.com/accordion.js"></script>')
SKIP_SLUGS = {"article-index-start-here"}


def live_posts():
    tok, out = None, []
    while True:
        q = "?maxResults=100&fetchBodies=false&status=LIVE" + (
            f"&pageToken={tok}" if tok else "")
        page = B.api(f"/blogs/{B.BLOG_ID}/posts{q}")
        out += page.get("items", [])
        tok = page.get("nextPageToken")
        if not tok:
            return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--recheck", action="store_true",
                    help="GET every live post instead of trusting the archived "
                         "copies in posts/ from the last snapshot")
    args = ap.parse_args()
    if not (args.plan or args.apply):
        ap.error("pass --plan or --apply")

    posts = live_posts()
    todo = [p for p in posts
            if p["url"].rsplit("/", 1)[-1].removesuffix(".html") not in SKIP_SLUGS]
    if not args.recheck:
        # One GET per post for ~340 posts is slow and times out; the archived
        # copy from the last snapshot already says which posts carry the stub.
        def archived_has_stub(p):
            f = ROOT / "posts" / (p["url"].rsplit("/", 1)[-1].removesuffix(".html") + ".html")
            return f.exists() and 'id="gs-idx"' in f.read_text(encoding="utf-8")
        todo = [p for p in todo if not archived_has_stub(p)]
    print(f"live posts {len(posts)} | eligible {len(todo)}")
    if args.plan:
        for p in todo[:10]:
            print("  ", p["title"][:64])
        print(f"   ... and {len(todo)-10} more")
        return 0

    done = skipped = 0
    for p in todo:
        full = B.api(f"/blogs/{B.BLOG_ID}/posts/{p['id']}")
        if 'id="gs-idx"' in full["content"]:
            skipped += 1
            continue
        try:
            B.api(f"/blogs/{B.BLOG_ID}/posts/{p['id']}",
                  data={"id": p["id"], "title": full["title"],
                        "content": full["content"] + STUB,
                        "published": full["published"],
                        "labels": full.get("labels") or []},
                  method="PUT")
        except B.Ceiling as e:
            print(f"\ndaily write ceiling after {done} writes: {e}")
            print("re-run tomorrow — done posts are skipped by marker")
            return 3
        done += 1
        print(f"  {done:3} {full['title'][:60]}")
        time.sleep(B.WRITE_GAP_SECONDS)
    print(f"\ninjected {done} | already had it {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
