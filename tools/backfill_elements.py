#!/usr/bin/env python3
"""Backfill the three standard house-style elements on any post missing them:
the Google Translate widget (right after <h1>), the index-page backlink (the
very first thing in the post body), and the AI-disclosure paragraph (right
before the gs-idx site-index stub near the end).

Detection matches tools/audit_blog.py's own "adoption" check exactly, so a
post this script still flags as missing something is really missing it, not
just differently formatted.

    python3 tools/backfill_elements.py --plan          # show what would change, write nothing
    python3 tools/backfill_elements.py --apply         # write locally to posts/, do NOT publish
    python3 tools/backfill_elements.py --publish        # write locally AND publish via blogger_api
    python3 tools/backfill_elements.py --publish --limit 10

SAFETY
    - Every insertion is a self-contained, already-balanced snippet (no tag
      is opened without being closed in the same snippet), so it cannot
      unbalance a post's existing tag count.
    - Every post is tag-balance-checked after insertion, before it is written
      or published; a post that fails the check is skipped and reported,
      never written.
    - --publish sends `published` back explicitly (via blogger_api's
      do_update), so this cannot re-date a post.
    - Resumable: re-running only touches posts still missing an element.
"""
import argparse
import glob
import json
import pathlib
import re
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"

sys.path.insert(0, str(ROOT / "tools"))
import blogger_api as B  # noqa: E402

SKIP_SLUGS = {"about-author", "article-index-start-here"}

TRANSLATE_SNIPPET = (
    '<div id="google_translate_element" style="margin:8px 0 16px;"></div>'
    '<script type="text/javascript">function googleTranslateElementInit(){'
    'new google.translate.TranslateElement({pageLanguage:"en",'
    'layout:google.translate.TranslateElement.InlineLayout.SIMPLE,'
    'autoDisplay:false},"google_translate_element");}</script>'
    '<script type="text/javascript" '
    'src="https://translate.google.com/translate_a/element.js?'
    'cb=googleTranslateElementInit"></script>'
)

INDEX_LINK_SNIPPET = (
    '<div class="topnav-index-link" style="font-size:.82em;margin:6px 0 14px">'
    '<a href="https://masaladeutsch.blogspot.com/2026/08/article-index-start-here.html" '
    'style="color:#0b5394;text-decoration:none">&larr; All Articles (Index)</a></div>\n'
)

DISCLOSURE_SNIPPET = (
    '<p class="disclaimer" data-gs-ai-disclosure-v1="1"><strong>AI Disclosure:</strong> '
    "This article was researched and written with AI assistance (Claude), drawing on "
    "publicly available government, industry, and academic sources cited above. "
    "AI-generated text can occasionally misstate figures or &ldquo;hallucinate&rdquo; "
    "details even when working from real source material &mdash; readers should treat "
    "this piece as a synthesis aid, verify any figure that matters to a decision against "
    "the cited primary source, and focus on the underlying material rather than this "
    "summary alone.</p>\n"
)


def tag_counts(src):
    counts = {}
    for tag in ("div", "p", "a", "script", "table", "tr", "td", "th", "ul", "li",
                "strong", "b", "i", "h1", "h2", "h3"):
        o = len(re.findall(rf"<{tag}(?:\s[^>]*)?>", src))
        c = len(re.findall(rf"</{tag}>", src))
        counts[tag] = (o, c)
    return counts


def diff_counts(before, after):
    bad = []
    for tag, (bo, bc) in before.items():
        ao, ac = after[tag]
        # a clean insertion adds the same number to opens and closes for any
        # tag it touches; it must never change the OPEN-CLOSE balance itself
        if (bo - bc) != (ao - ac):
            bad.append(tag)
    return bad


def missing(src):
    need = []
    if "google_translate_element" not in src:
        need.append("translate")
    if "article-index-start-here" not in src:
        need.append("index_link")
    if "gs-ai-disclosure" not in src:
        need.append("disclosure")
    return need


def apply_fixes(src, need):
    """Apply each requested fix independently -- a post missing an </h1> (a
    few use a custom 'hero' title block instead of a plain h1) can still get
    its index-link and disclosure additions; only the translate insertion is
    skipped for that post, and it's reported, not silently dropped."""
    before = tag_counts(src)
    out = src
    applied, skipped = [], []

    if "index_link" in need:
        out = INDEX_LINK_SNIPPET + out
        applied.append("index_link")

    if "translate" in need:
        m = re.search(r"</h1>", out)
        if m:
            out = out[: m.end()] + TRANSLATE_SNIPPET + out[m.end():]
            applied.append("translate")
        else:
            skipped.append("translate (no </h1> found)")

    if "disclosure" in need:
        m = re.search(r'<div id="gs-idx">', out)
        if m:
            out = out[: m.start()] + DISCLOSURE_SNIPPET + out[m.start():]
            applied.append("disclosure")
        else:
            skipped.append("disclosure (no gs-idx stub found)")

    if not applied:
        return None, None, "nothing could be applied: " + "; ".join(skipped)

    after = tag_counts(out)
    bad = diff_counts(before, after)
    if bad:
        return None, None, f"tag balance changed unexpectedly: {bad}"
    return out, applied, ("; ".join(skipped) if skipped else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--apply", action="store_true", help="write locally, do not publish")
    ap.add_argument("--publish", action="store_true", help="write locally and publish")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()
    if not (args.plan or args.apply or args.publish):
        args.plan = True

    man = json.loads((ROOT / "meta" / "manifest.json").read_text())["posts"]
    targets = []
    for rec in sorted(man.values(), key=lambda r: r["slug"]):
        slug = rec["slug"]
        if slug in SKIP_SLUGS:
            continue
        f = POSTS / f"{slug}.html"
        if not f.exists():
            continue
        src = f.read_text(encoding="utf-8", errors="replace")
        need = missing(src)
        if need:
            targets.append((slug, src, need))

    print(f"{len(targets)} posts need at least one element\n")

    done = 0
    for slug, src, need in targets:
        if args.limit and done >= args.limit:
            print(f"stopping at --limit {args.limit}")
            break
        fixed, applied, note = apply_fixes(src, need)
        if fixed is None:
            print(f"  SKIP {slug}: {note}")
            continue
        tail = f"  ({note})" if note else ""
        print(f"  {slug}: +{','.join(applied)}{tail}")
        if args.plan:
            done += 1
            continue

        f = POSTS / f"{slug}.html"

        if args.publish:
            # Write locally only AFTER a successful publish -- if the write
            # ceiling hits mid-batch, a post whose publish failed must still
            # look "missing" to missing() on the next run, not silently
            # look fixed because the local file was updated first.
            meta_path = ROOT / "meta" / f"{slug}.json"
            meta = json.loads(meta_path.read_text())
            try:
                ok = B.do_update(meta["id"], meta["url"], meta["title"], fixed,
                                  published=meta.get("published"))
            except B.Ceiling as e:
                print(f"\ndaily write ceiling reached after {done} publishes: {e}")
                print("posts not yet reached remain untouched, locally and live -- "
                      "re-run --publish to pick up where this left off")
                return 3
            if not ok:
                print(f"    WARNING: {slug} published but verify failed -- check manually, "
                      f"not writing local file until confirmed")
                continue
            f.write_text(fixed, encoding="utf-8")
        else:
            f.write_text(fixed, encoding="utf-8")
        done += 1

    print(f"\n{'planned' if args.plan else 'processed'}: {done} posts")


if __name__ == "__main__":
    main()
