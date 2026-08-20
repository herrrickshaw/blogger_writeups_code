#!/usr/bin/env python3
"""Merge JPlag + copyfind + copydetect output into one dated markdown report.

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


def load_jplag_pairs(csv_path):
    pairs = {}
    for r in csv.DictReader(open(csv_path)):
        s1 = r['submissionName1'].replace('.txt', '')
        s2 = r['submissionName2'].replace('.txt', '')
        key = tuple(sorted([s1, s2]))
        pairs[key] = float(r['maxSimilarity'])
    return pairs


def load_copydetect_pairs(csv_path):
    pairs = {}
    if not os.path.exists(csv_path):
        return pairs
    for r in csv.DictReader(open(csv_path)):
        s1 = r['testFile'].replace('.txt', '')
        s2 = r['refFile'].replace('.txt', '')
        key = tuple(sorted([s1, s2]))
        pairs[key] = max(float(r['testSimilarity']), float(r['refSimilarity']))
    return pairs


def main():
    csv_path, copyfind_path, copydetect_path, out_path = sys.argv[1:5]
    repo_root = os.path.join(os.path.dirname(__file__), '..', '..')
    live = load_live_slugs(repo_root)

    jplag = load_jplag_pairs(csv_path)
    copydetect = load_copydetect_pairs(copydetect_path)
    all_keys = set(jplag) | set(copydetect)

    copyfind = {}
    if os.path.exists(copyfind_path):
        for r in json.load(open(copyfind_path)):
            copyfind[(r['a'].replace('.txt', ''), r['b'].replace('.txt', ''))] = r

    merged = []
    for key in all_keys:
        jp = jplag.get(key)
        cd = copydetect.get(key)
        best = max(v for v in (jp, cd) if v is not None)
        merged.append((key, best, jp, cd))
    merged.sort(key=lambda x: -x[1])

    stale_pairs, live_pairs = [], []
    for key, best, jp, cd in merged:
        s1, s2 = key
        one_stale = (s1 not in live) != (s2 not in live)
        (stale_pairs if one_stale else live_pairs).append((key, best, jp, cd))

    def tool_tag(jp, cd):
        tags = []
        if jp is not None:
            tags.append(f"JPlag {jp:.2f}")
        if cd is not None:
            tags.append(f"copydetect {cd:.2f}")
        return ", ".join(tags)

    lines = [f"# Internal duplication check", ""]
    lines.append(
        f"{len(merged)} pairs flagged (at or above 0.15) by JPlag (text mode) and/or "
        f"copydetect (winnowing fingerprints), out of {len(live)} live posts checked pairwise. "
        f"A WCopyfind-equivalent phrase pass (pl-copyfind) confirms actual matched text on "
        f"the pairs JPlag flags."
    )
    lines.append("")

    lines.append("## Likely stale local drafts (one side isn't a live post)")
    lines.append("These are the recurring pattern where a superseded/duplicate local file sits in `posts/` alongside the real live post under a different slug -- not actual duplicate content between two published articles. Worth a `git rm` pass on the non-live side after a quick diff, same as prior cleanups this session.")
    lines.append("")
    if stale_pairs:
        for key, best, jp, cd in stale_pairs:
            s1, s2 = key
            stale_side = s1 if s1 not in live else s2
            live_side = s2 if s1 not in live else s1
            lines.append(f"- **{best:.2f}** ({tool_tag(jp, cd)}) stale `{stale_side}` <-> live `{live_side}`")
    else:
        lines.append("_none this run_")
    lines.append("")

    lines.append("## Overlap between two live, distinct posts")
    lines.append("Genuine candidates worth a human look -- either intentional companion-piece cross-referencing (fine, matches house style) or unintentional content reuse (worth trimming one side).")
    lines.append("")
    if live_pairs:
        for key, best, jp, cd in live_pairs:
            s1, s2 = key
            cf = copyfind.get((s1, s2)) or copyfind.get((s2, s1))
            sample = f" -- sample: \"{cf['sample'][0][:140]}...\"" if cf and cf.get('sample') else ""
            lines.append(f"- **{best:.2f}** ({tool_tag(jp, cd)}) `{s1}` <-> `{s2}`{sample}")
    else:
        lines.append("_none this run_")
    lines.append("")

    with open(out_path, 'w') as f:
        f.write('\n'.join(lines))
    print(f"wrote {out_path}: {len(stale_pairs)} stale-draft pairs, {len(live_pairs)} live-vs-live pairs")


if __name__ == '__main__':
    main()
