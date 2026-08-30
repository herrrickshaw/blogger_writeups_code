#!/usr/bin/env python3
"""Build a boilerplate-stripped plain-text corpus for the plagiarism-check pipeline.

Uses trafilatura's structural content extraction instead of a hand-maintained
list of boilerplate marker strings (the original approach here, kept working
but fragile -- every new bit of site chrome needed its own marker added).
trafilatura already drops nav/accessibility-bar/language-picker chrome
automatically; only the two truly identical cross-post sentences (the AI
disclosure paragraph and the generic government-data disclaimer) still need
an explicit filter, since those really are inside the article body.
"""
import glob, os, shutil, sys
import trafilatura

BOILERPLATE_MARKERS = [
    'AI Disclosure:',
    'This analysis is based on publicly available government and market data',
    'This analysis draws on publicly available government and market data',
]


def is_boilerplate(paragraph: str) -> bool:
    return any(marker in paragraph for marker in BOILERPLATE_MARKERS)


def clean_text(html_path: str) -> str:
    raw = open(html_path, encoding='utf-8', errors='ignore').read()
    extracted = trafilatura.extract(raw, include_tables=True, favor_recall=False)
    if not extracted:
        return ''
    paragraphs = [p for p in extracted.split('\n') if p.strip() and not is_boilerplate(p)]
    return '\n\n'.join(paragraphs)


if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else 'out/plagcheck/txt'
    shutil.rmtree(out_dir, ignore_errors=True)  # drop stale .txt for posts removed since the last run
    os.makedirs(out_dir, exist_ok=True)
    posts_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'posts')
    n = 0
    for path in sorted(glob.glob(os.path.join(posts_dir, '*.html'))):
        slug = os.path.splitext(os.path.basename(path))[0]
        text = clean_text(path)
        if len(text) < 200:
            continue  # too short to be a real article body (e.g. stray fragment file)
        with open(os.path.join(out_dir, slug + '.txt'), 'w', encoding='utf-8') as f:
            f.write(text)
        n += 1
    print(f'wrote {n} cleaned text files to {out_dir}')
