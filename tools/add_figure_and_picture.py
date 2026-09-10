#!/usr/bin/env python3
"""Insert a real, sourced picture (Wikimedia Commons, or Adobe Stock as fallback)
and/or a data figure (inline SVG chart built only from numbers already published
in that same post) into any archived post still missing one or both.

This script does NOT choose the picture or design the chart -- that editorial
work (finding a topically-correct, correctly-licensed image; picking which of
the post's own already-published numbers to chart) happens once per post and
is recorded in a staging file at fixes/figure_picture_staging.json:

    {
      "<slug>": {
        "picture_html": "<figure ...>...</figure>",   // omit/null if post already has a picture
        "chart_html": "<figure ...><svg ...>...</svg>...</figure>"  // omit/null if already has a chart
      },
      ...
    }

This script only does the MECHANICAL part, following the same safety pattern as
backfill_elements.py: self-contained balanced-tag snippets, a before/after tag-
balance check, --publish writing the local file only after a verified live
publish (so a mid-batch ceiling hit never marks a post "done" that isn't).

    python3 tools/add_figure_and_picture.py --plan
    python3 tools/add_figure_and_picture.py --apply          # write locally, do not publish
    python3 tools/add_figure_and_picture.py --publish --limit 20
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"
STAGING = ROOT / "fixes" / "figure_picture_staging.json"

sys.path.insert(0, str(ROOT / "tools"))
import blogger_api as B  # noqa: E402


def tag_counts(src):
    # paired tags only -- img/br/hr are void elements with no balance to check
    counts = {}
    for tag in ("div", "p", "a", "script", "table", "tr", "td", "th", "ul", "li",
                "strong", "b", "i", "h1", "h2", "h3", "figure", "figcaption", "svg"):
        o = len(re.findall(rf"<{tag}(?:\s[^>]*)?>", src))
        c = len(re.findall(rf"</{tag}>", src))
        counts[tag] = (o, c)
    return counts


def diff_counts(before, after):
    bad = []
    for tag, (bo, bc) in before.items():
        ao, ac = after[tag]
        if (bo - bc) != (ao - ac):
            bad.append(tag)
    return bad


def has_chart(src):
    return bool(re.search(r'<canvas|<svg[^>]*viewBox|chart\.js|new Chart\(|d3\.select', src, re.I))


def has_picture(src):
    return bool(re.search(r'<img\s[^>]*src=', src, re.I))


def insert_picture(src, picture_html):
    """Right after the first substantive paragraph following </h1> -- matches
    the placement already established in posts like rooftop-solar-is-working."""
    h1_end = re.search(r"</h1>", src)
    search_from = h1_end.end() if h1_end else 0
    m = re.search(r"</p>", src[search_from:])
    if not m:
        return None, "no </p> found after <h1> to anchor the picture"
    pos = search_from + m.end()
    return src[:pos] + "\n" + picture_html + src[pos:], None


def insert_chart(src, chart_html):
    """Right after the LAST </table> in the post (summarizes the table just
    shown); falls back to right before the AI-disclosure paragraph if the post
    has no table."""
    tables = list(re.finditer(r"</table>", src))
    if tables:
        pos = tables[-1].end()
        return src[:pos] + "\n" + chart_html + src[pos:], None
    m = re.search(r'<p class="disclaimer"', src)
    if m:
        return src[:m.start()] + chart_html + "\n" + src[m.start():], None
    return None, "no </table> and no disclaimer paragraph to anchor the chart"


def apply_fixes(src, fix):
    before = tag_counts(src)
    out = src
    applied, skipped = [], []

    if fix.get("picture_html") and not has_picture(src):
        result, err = insert_picture(out, fix["picture_html"])
        if result is None:
            skipped.append(f"picture ({err})")
        else:
            out = result
            applied.append("picture")

    if fix.get("chart_html") and not has_chart(src):
        result, err = insert_chart(out, fix["chart_html"])
        if result is None:
            skipped.append(f"chart ({err})")
        else:
            out = result
            applied.append("chart")

    if not applied:
        return None, None, "nothing could be applied: " + ("; ".join(skipped) if skipped else "already complete")

    after = tag_counts(out)
    bad = diff_counts(before, after)
    if bad:
        return None, None, f"tag balance changed unexpectedly: {bad}"
    return out, applied, ("; ".join(skipped) if skipped else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--publish", action="store_true")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--slug", help="process only this one slug (for testing)")
    args = ap.parse_args()
    if not (args.plan or args.apply or args.publish):
        args.plan = True

    if not STAGING.exists():
        print(f"no staging file at {STAGING} -- nothing to do")
        return 1
    staging = json.loads(STAGING.read_text())

    man = json.loads((ROOT / "meta" / "manifest.json").read_text())["posts"]
    slug_to_id = {rec["slug"]: pid for pid, rec in man.items()}

    slugs = [args.slug] if args.slug else sorted(staging.keys())
    done = 0
    still_pending = {}
    for slug in slugs:
        fix = staging.get(slug)
        if not fix:
            continue
        f = POSTS / f"{slug}.html"
        if not f.exists():
            print(f"  SKIP {slug}: no local post file")
            still_pending[slug] = fix
            continue
        src = f.read_text(encoding="utf-8", errors="replace")
        fixed, applied, note = apply_fixes(src, fix)
        if fixed is None:
            print(f"  SKIP {slug}: {note}")
            continue

        if args.limit and done >= args.limit:
            still_pending[slug] = fix
            continue

        tail = f"  ({note})" if note else ""
        print(f"  {slug}: +{','.join(applied)}{tail}")
        if args.plan:
            done += 1
            still_pending[slug] = fix  # plan never consumes the staging entry
            continue

        if args.publish:
            pid = slug_to_id.get(slug)
            meta_path = ROOT / "meta" / f"{slug}.json"
            if not pid or not meta_path.exists():
                print(f"    WARNING: {slug} has no manifest/meta entry -- writing locally only")
                f.write_text(fixed, encoding="utf-8")
                done += 1
                continue
            meta = json.loads(meta_path.read_text())
            try:
                ok = B.do_update(meta["id"], meta["url"], meta["title"], fixed,
                                  published=meta.get("published"), labels=meta.get("labels"))
            except B.Ceiling as e:
                print(f"\ndaily write ceiling reached after {done} publishes: {e}")
                still_pending[slug] = fix
                for remaining in slugs[slugs.index(slug) + 1:]:
                    if remaining in staging:
                        still_pending[remaining] = staging[remaining]
                STAGING.write_text(json.dumps(still_pending, indent=1))
                print("remaining posts kept in staging -- re-run --publish tomorrow")
                return 3
            if not ok:
                print(f"    WARNING: {slug} published but verify failed -- check manually, "
                      f"leaving in staging, not writing local file")
                still_pending[slug] = fix
                continue
            f.write_text(fixed, encoding="utf-8")
        else:
            f.write_text(fixed, encoding="utf-8")
        done += 1

    if not args.plan:
        STAGING.write_text(json.dumps(still_pending, indent=1))

    print(f"\n{'planned' if args.plan else 'processed'}: {done} posts"
          f"{'' if args.plan else f', {len(still_pending)} remaining in staging'}")


if __name__ == "__main__":
    main()
