#!/usr/bin/env python3
"""Structure-aware HTML -> plain text for a masaladeutsch post.

Unlike a naive tag-strip (which glues headings, table cells and paragraphs
into one run-on string -- exactly what fed LanguageTool garbage phrase-
repetition/run-on hits earlier), this walks the DOM and emits one block per
block-level element, with table rows/cells kept on their own lines. Output
is "one clean document": a headline line, then blank-line-separated
paragraphs/headings, with tables rendered as pipe-separated rows so they
don't get grammar-checked as prose but still read cleanly for a summary.
"""
import glob, html, json, re, sys
from html.parser import HTMLParser

BLOCK_TAGS = {'p', 'h1', 'h2', 'h3', 'h4', 'li', 'div', 'tr', 'blockquote'}
SKIP_CONTENT_TAGS = {'script', 'style', 'noscript', 'template', 'iframe'}
INLINE_BREAK_TAGS = {'br'}


class BlockExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.cur = []
        self.skip_depth = 0
        self.tag_stack = []
        self.in_table = False
        self.row_cells = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        if tag in SKIP_CONTENT_TAGS:
            self.skip_depth += 1
            return
        if tag == 'table':
            self.in_table = True
        if tag == 'tr':
            self.row_cells = []
        if tag in BLOCK_TAGS or tag in ('td', 'th'):
            self._flush_text()

    def handle_endtag(self, tag):
        if self.tag_stack and tag in self.tag_stack:
            while self.tag_stack and self.tag_stack[-1] != tag:
                self.tag_stack.pop()
            if self.tag_stack:
                self.tag_stack.pop()
        if tag in SKIP_CONTENT_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if tag in ('td', 'th'):
            cell = self._flush_text()
            if cell:
                self.row_cells.append(cell)
            return
        if tag == 'tr':
            if self.row_cells:
                self.blocks.append(' | '.join(self.row_cells))
            self.row_cells = []
            return
        if tag == 'table':
            self.in_table = False
            return
        if tag in BLOCK_TAGS:
            self._flush_text()

    def handle_data(self, data):
        if self.skip_depth:
            return
        self.cur.append(data)

    def _flush_text(self):
        text = ''.join(self.cur).strip()
        text = re.sub(r'\s+', ' ', text)
        self.cur = []
        if text and not self.in_table:
            self.blocks.append(text)
        return text if self.in_table else None


def extract(raw_html):
    p = BlockExtractor()
    p.feed(raw_html)
    p._flush_text()
    # de-duplicate consecutive identical blocks (real accidental doubles,
    # not table-cell adjacency, since cells no longer merge into blocks)
    out = []
    for b in p.blocks:
        if out and out[-1] == b:
            continue
        out.append(b)
    return out


def build_document(title, blocks):
    return title.strip() + '\n\n' + '\n\n'.join(blocks)


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--file', required=True)
    ap.add_argument('--title', default='')
    args = ap.parse_args()
    raw = open(args.file, encoding='utf-8', errors='ignore').read()
    blocks = extract(raw)
    print(build_document(args.title, blocks))
