#!/usr/bin/env python3
"""Merge JPlag + copyfind output into one dated markdown report.

Classifies each flagged pair against meta/manifest.json: a pair where one
side isn't a live slug is very likely the recurring "stale local draft"
artifact (see DESIGN_LOG.md), not real duplicate content between two live
posts -- that distinction is the main point of the report.
"""
import csv, json, os, sys

def load_live_slugs(repo_root):
    manifest = json.load(open(os.path.join(repo_root, 'meta', 'manifest.json')))
    slugs = set()
    for v in manifest['posts'].values():
        slug = v.get('url', '').rstrip('/').split('/')[-1].replace('.html', '')
        slugs.add(slug)
    return slugs


def main():
    csv_path, copyfind_path, out_path = sys.argv[1:4]
    repo_root = os.path.join(os.path.dirname(__file__), '..', '..')
    live = load_live_slugs(repo_root)

    rows = list(csv.DictReader(open(csv_path)))
    rows.sort(key=lambda r: -float(r['maxSimilarity']))
    copyfind = {}
    if os.path.exists(copyfind_path):
        for r in json.load(open(copyfind_path)):
            copyfind[(r['a'], r['b'])] = r

    stale_pairs, live_pairs = [], []
    for r in rows:
        s1 = r['submissionName1'].replace('.txt', '')
        s2 = r['submissionName2'].replace('.txt', '')
        one_stale = (s1 not in live) != (s2 not in live)  # exactly one side not live
        (stale_pairs if one_stale else live_pairs).append(r)

    lines = [f"# Internal duplication check", ""]
    lines.append(f"{len(rows)} pairs at or above 0.15 similarity, out of {len(live)} live posts checked pairwise via JPlag (text mode) + a WCopyfind-equivalent phrase pass (pl-copyfind) on the flagged pairs.")
    lines.append("")

    lines.append("## Likely stale local drafts (one side isn't a live post)")
    lines.append("These are the recurring pattern where a superseded/duplicate local file sits in `posts/` alongside the real live post under a different slug -- not actual duplicate content between two published articles. Worth a `git rm` pass on the non-live side after a quick diff, same as prior cleanups this session.")
    lines.append("")
    if stale_pairs:
        for r in stale_pairs:
            s1, s2 = r['submissionName1'].replace('.txt', ''), r['submissionName2'].replace('.txt', '')
            stale_side = s1 if s1 not in live else s2
            live_side = s2 if s1 not in live else s1
            lines.append(f"- **{float(r['maxSimilarity']):.2f}** stale `{stale_side}` <-> live `{live_side}`")
    else:
        lines.append("_none this run_")
    lines.append("")

    lines.append("## Overlap between two live, distinct posts")
    lines.append("Genuine candidates worth a human look -- either intentional companion-piece cross-referencing (fine, matches house style) or unintentional content reuse (worth trimming one side).")
    lines.append("")
    if live_pairs:
        for r in live_pairs:
            s1, s2 = r['submissionName1'].replace('.txt', ''), r['submissionName2'].replace('.txt', '')
            cf = copyfind.get((r['submissionName1'], r['submissionName2'])) or copyfind.get((r['submissionName2'], r['submissionName1']))
            sample = f" -- sample: \"{cf['sample'][0][:140]}...\"" if cf and cf.get('sample') else ""
            lines.append(f"- **{float(r['maxSimilarity']):.2f}** `{s1}` <-> `{s2}`{sample}")
    else:
        lines.append("_none this run_")
    lines.append("")

    with open(out_path, 'w') as f:
        f.write('\n'.join(lines))
    print(f"wrote {out_path}: {len(stale_pairs)} stale-draft pairs, {len(live_pairs)} live-vs-live pairs")


if __name__ == '__main__':
    main()
