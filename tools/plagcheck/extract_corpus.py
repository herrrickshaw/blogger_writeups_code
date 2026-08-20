#!/usr/bin/env python3
"""Build a boilerplate-stripped plain-text corpus for the plagiarism-check pipeline.

Every post shares identical UI chrome (accessibility bar, language picker,
AI-disclosure paragraph, index-link, revision line). Feeding that straight
into a similarity checker would just report 183-way "matches" on the
boilerplate, drowning any real signal. This reuses tools/extract_post.py's
block extraction, then drops blocks that are pure chrome.
"""
import glob, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import extract_post

BOILERPLATE_MARKERS = [
    'Text Size', 'Small text', 'Medium text', 'Large text',
    'Read this article aloud', 'Stop reading aloud', 'More tools:',
    'Jyoti AI', 'Trestle Labs', "Let's Talk Sign", 'Select Language',
    'Skip to article content', 'All Articles (Index)',
    'AI Disclosure:', 'as an Amazon Associate',
    'Updated <time', 'Revised <time', 'gs-typo-unify',
    'This analysis is based on publicly available government and market data',
    'This analysis draws on publicly available government and market data',
]


def is_boilerplate(block: str) -> bool:
    if len(block) < 40:
        return True  # headers/labels, not prose
    return any(marker in block for marker in BOILERPLATE_MARKERS)


def clean_text(html_path: str) -> str:
    raw = open(html_path, encoding='utf-8', errors='ignore').read()
    blocks = extract_post.extract(raw)
    kept = [b for b in blocks if not is_boilerplate(b)]
    return '\n\n'.join(kept)


if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else 'out/plagcheck/txt'
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
