#!/usr/bin/env python3
"""Render a post's <figure class="gb-figure">...</figure> block (or any
--selector match) to a PNG so a chart fix can be visually confirmed instead
of guessed at. This sandbox has no network access to the live blog, so this
is local-only rendering of the raw HTML/SVG -- no fetch involved.

Usage:
    python3 tools/render_svg_figure.py posts/foo.html --out /tmp/foo.png
    python3 tools/render_svg_figure.py posts/foo.html --index 1 --out /tmp/foo2.png
    python3 tools/render_svg_figure.py posts/foo.html --all --outdir /tmp/foo/
"""
import argparse
import os
import re

from playwright.sync_api import sync_playwright

FIGURE_RE = re.compile(r'<figure\b[^>]*>.*?</figure>', re.S)
SVG_RE = re.compile(r'<svg\b[^>]*>.*?</svg>', re.S)


def find_blocks(html):
    """Every <figure> block, plus any bare <svg> not already inside one of
    those figures (some posts drop a chart straight into a <div> instead)."""
    figures = FIGURE_RE.findall(html)
    covered_spans = [m.span() for m in FIGURE_RE.finditer(html)]

    def inside_a_figure(pos):
        return any(a <= pos < b for a, b in covered_spans)

    extra_svgs = [m.group(0) for m in SVG_RE.finditer(html) if not inside_a_figure(m.start())]
    return figures + extra_svgs


CHROMIUM_CANDIDATES = [
    '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
]


def find_chromium():
    for c in CHROMIUM_CANDIDATES:
        if os.path.exists(c):
            return c
    import glob
    hits = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome')
    if hits:
        return hits[0]
    return None  # let Playwright try its own default


def render(html_fragment, out_path, width=760, height=900):
    wrapper = (
        '<!doctype html><html><head><meta charset="utf-8">'
        '<style>body{margin:0;padding:20px;background:#fff;'
        'font-family:Georgia,"Times New Roman",serif}</style></head>'
        f'<body>{html_fragment}</body></html>'
    )
    tmp_path = out_path + '.src.html'
    open(tmp_path, 'w', encoding='utf-8').write(wrapper)
    exe = find_chromium()
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        page = browser.new_page(viewport={'width': width, 'height': height})
        page.goto(f'file://{os.path.abspath(tmp_path)}')
        page.screenshot(path=out_path, full_page=True)
        browser.close()
    os.remove(tmp_path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('post', help='path to posts/*.html or a raw fragment file')
    ap.add_argument('--index', type=int, default=0, help='which <figure> block (0-based) if there are several')
    ap.add_argument('--all', action='store_true', help='render every <figure> block found')
    ap.add_argument('--out', help='output PNG path (single-figure mode)')
    ap.add_argument('--outdir', help='output directory (with --all)')
    ap.add_argument('--fragment', action='store_true', help='treat the whole file as a fragment to render as-is, no <figure> extraction')
    args = ap.parse_args()

    html = open(args.post, encoding='utf-8').read()

    if args.fragment:
        render(html, args.out or (args.post + '.png'))
        print(f'wrote {args.out or (args.post + ".png")}')
        return

    figures = find_blocks(html)
    if not figures:
        raise SystemExit(f'no <figure> or bare <svg> blocks found in {args.post}')

    if args.all:
        outdir = args.outdir or '.'
        os.makedirs(outdir, exist_ok=True)
        for i, fig in enumerate(figures):
            out = os.path.join(outdir, f'figure-{i}.png')
            render(fig, out)
            print(f'wrote {out}')
        return

    if args.index >= len(figures):
        raise SystemExit(f'only {len(figures)} <figure> block(s) found; --index {args.index} out of range')
    out = args.out or (args.post + f'.figure{args.index}.png')
    render(figures[args.index], out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
