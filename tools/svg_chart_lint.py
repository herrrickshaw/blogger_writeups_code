#!/usr/bin/env python3
"""Scan posts/*.html for inline SVG charts with likely label collisions or
viewBox overflow -- the "text on top of text" / "graph cut off" bug class.

Approach: parse each <svg viewBox="..."> block's <text> elements (x, y,
text-anchor, font-size, font-weight, content), estimate each one's rendered
bounding box with a per-character width table, and flag:

  - COLLISION: two text elements on (near) the same baseline whose estimated
    x-ranges overlap.
  - OVERFLOW: a text element's estimated x-range extends outside the SVG's
    own viewBox (or width attribute when there's no viewBox), i.e. it will be
    clipped by the SVG viewport.

This is a heuristic, not a renderer: character-width estimates are close
enough (calibrated against Playwright screenshots of real posts) to be a
useful triage tool, not a guarantee. Always visually confirm a fix with
scripts/render_svg_figure.py before publishing.

Usage:
    python3 tools/svg_chart_lint.py                  # scan all of posts/
    python3 tools/svg_chart_lint.py posts/foo.html    # scan one file
    python3 tools/svg_chart_lint.py --json out.json   # machine-readable report
"""
import argparse
import glob
import json
import re
import sys

TEXT_RE = re.compile(
    r'<text\b([^>]*)>(.*?)</text>', re.S
)
ATTR_RE = re.compile(r'([\w:-]+)\s*=\s*"([^"]*)"')
SVG_RE = re.compile(
    r'<svg\b([^>]*)>(.*?)</svg>', re.S
)
TAG_RE = re.compile(r'<[^>]+>')

# Per-character width as a fraction of font-size, roughly calibrated for the
# Georgia/system-sans mixes this blog uses. Digits and most lowercase letters
# cluster tightly; a flat-ish table beats a single multiplier because these
# charts are dense with digits, currency symbols and punctuation.
CHAR_W = {
    **{c: 0.50 for c in "0123456789"},
    **{c: 0.28 for c in "ilIj.,:;'|!"},
    **{c: 0.62 for c in "mMW"},
    **{c: 0.40 for c in " "},
}
DEFAULT_W = 0.52
BOLD_BUMP = 1.08  # font-weight >= 600 renders a touch wider


def text_width(s, font_size, weight_bold):
    s = re.sub(r'&\w+;', 'X', s)  # entities ~1 glyph each
    w = sum(CHAR_W.get(ch, DEFAULT_W) for ch in s) * font_size
    return w * BOLD_BUMP if weight_bold else w


def parse_attrs(attr_str):
    return dict(ATTR_RE.findall(attr_str))


def text_bbox(attrs, content, font_size_default=11):
    x = float(attrs.get('x', 0))
    fs = float(attrs.get('font-size', font_size_default))
    weight = attrs.get('font-weight', '400')
    bold = weight in ('600', '700', 'bold', '800', '900')
    anchor = attrs.get('text-anchor', 'start')
    plain = TAG_RE.sub('', content).strip()
    w = text_width(plain, fs, bold)
    if anchor == 'end':
        x0, x1 = x - w, x
    elif anchor == 'middle':
        x0, x1 = x - w / 2, x + w / 2
    else:
        x0, x1 = x, x + w
    y = float(attrs.get('y', 0))
    return x0, x1, y, fs, plain


def find_charts(html):
    for m in SVG_RE.finditer(html):
        svg_attrs = parse_attrs(m.group(1))
        vb = svg_attrs.get('viewBox', '')
        parts = vb.split()
        if len(parts) == 4:
            vb_x0, vb_y0, vb_w, vb_h = map(float, parts)
        else:
            vb_x0, vb_y0 = 0.0, 0.0
            vb_w = float(svg_attrs.get('width', 700) or 700)
            vb_h = float(svg_attrs.get('height', 400) or 400)
        yield m.start(), vb_x0, vb_x0 + vb_w, vb_y0, vb_y0 + vb_h, m.group(2)


def lint_svg(body_offset, vb_x0, vb_x1, vb_y0, vb_y1, inner):
    issues = []
    texts = []
    for tm in TEXT_RE.finditer(inner):
        attrs = parse_attrs(tm.group(1))
        if 'x' not in attrs or 'y' not in attrs:
            continue
        x0, x1, y, fs, plain = text_bbox(attrs, tm.group(2))
        if not plain:
            continue
        texts.append((x0, x1, y, fs, plain, tm.start()))

    # overflow: bbox outside the declared canvas (with a tiny 1px tolerance)
    for x0, x1, y, fs, plain, pos in texts:
        if x0 < vb_x0 - 1:
            issues.append({
                'type': 'OVERFLOW_LEFT', 'text': plain,
                'x0': round(x0, 1), 'canvas_x0': vb_x0,
            })
        if x1 > vb_x1 + 1:
            issues.append({
                'type': 'OVERFLOW_RIGHT', 'text': plain,
                'x1': round(x1, 1), 'canvas_x1': vb_x1,
                'overflow_px': round(x1 - vb_x1, 1),
            })

    # collision: same-baseline (within half a line-height) x-range overlap
    texts_sorted = sorted(texts, key=lambda t: t[2])
    for i in range(len(texts_sorted)):
        x0a, x1a, ya, fsa, pa, _ = texts_sorted[i]
        for j in range(i + 1, len(texts_sorted)):
            x0b, x1b, yb, fsb, pb, _ = texts_sorted[j]
            if yb - ya > max(fsa, fsb) * 0.6:
                break  # sorted by y; no further candidates this close
            if x0a < x1b and x0b < x1a:
                overlap = min(x1a, x1b) - max(x0a, x0b)
                if overlap > 1:
                    issues.append({
                        'type': 'COLLISION',
                        'text_a': pa, 'text_b': pb,
                        'overlap_px': round(overlap, 1),
                        'y': round(ya, 1),
                    })
    return issues


def lint_file(path):
    html = open(path, encoding='utf-8').read()
    results = []
    for _, vb_x0, vb_x1, vb_y0, vb_y1, inner in find_charts(html):
        issues = lint_svg(0, vb_x0, vb_x1, vb_y0, vb_y1, inner)
        if issues:
            results.append({'viewBox': [vb_x0, vb_y0, vb_x1 - vb_x0, vb_y1 - vb_y0], 'issues': issues})
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='*', help='specific post(s); default: all posts/*.html')
    ap.add_argument('--json', help='write machine-readable report to this path')
    ap.add_argument('--min-overflow', type=float, default=2.0,
                     help='ignore OVERFLOW_RIGHT/LEFT smaller than this many px (default 2)')
    args = ap.parse_args()

    files = args.files or sorted(glob.glob('posts/*.html'))
    report = {}
    total_issues = 0
    for f in files:
        try:
            charts = lint_file(f)
        except Exception as e:
            print(f'  ! {f}: parse error {e}', file=sys.stderr)
            continue
        kept = []
        for c in charts:
            issues = [
                i for i in c['issues']
                if i['type'] not in ('OVERFLOW_LEFT', 'OVERFLOW_RIGHT')
                or i.get('overflow_px', 999) >= args.min_overflow
            ]
            if issues:
                kept.append({**c, 'issues': issues})
        if kept:
            report[f] = kept
            total_issues += sum(len(c['issues']) for c in kept)

    for f, charts in report.items():
        print(f'=== {f}')
        for c in charts:
            for i in c['issues']:
                if i['type'] == 'COLLISION':
                    print(f'  COLLISION  "{i["text_a"]}"  overlaps  "{i["text_b"]}"  ({i["overlap_px"]}px, y={i["y"]})')
                else:
                    side = 'right' if i['type'] == 'OVERFLOW_RIGHT' else 'left'
                    print(f'  OVERFLOW-{side.upper():<5} "{i["text"]}"  by {i.get("overflow_px", "?")}px past canvas edge')

    print(f'\n{len(report)} file(s) with issues, {total_issues} issue(s) total, out of {len(files)} scanned.')
    if args.json:
        json.dump(report, open(args.json, 'w'), indent=2)
        print(f'wrote {args.json}')


if __name__ == '__main__':
    main()
