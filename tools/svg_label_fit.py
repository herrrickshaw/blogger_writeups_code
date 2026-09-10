#!/usr/bin/env python3
"""Reusable label-placement geometry for the hand-built SVG bar charts across
posts/ -- the fix for the "text on top of text" / "graph cut off" bug class
that tools/svg_chart_lint.py detects.

Core rule (matches the dataviz skill's guidance): prefer placing a value
label just OUTSIDE its bar; if there isn't room before the canvas edge, move
it INSIDE the bar (white text) if it fits there with padding; if it fits
neither space at the default size, shrink the font just enough to fit inside
rather than ever clipping or overlapping another label. Nothing this module
produces should be able to overflow the canvas or its own bar.
"""
import re

CHAR_W = {
    **{c: 0.50 for c in "0123456789"},
    **{c: 0.28 for c in "ilIj.,:;'|!"},
    **{c: 0.62 for c in "mMW"},
    **{c: 0.40 for c in " "},
}
DEFAULT_W = 0.52
BOLD_BUMP = 1.08
MIN_FONT_SIZE = 8.0


def text_width(s, font_size, bold=True):
    s = re.sub(r'&\w+;', 'X', s)
    w = sum(CHAR_W.get(ch, DEFAULT_W) for ch in s) * font_size
    return w * BOLD_BUMP if bold else w


def wrap_text_lines(text, max_width, font_size, bold=False):
    """Greedy word-wrap into lines that each fit max_width at font_size.
    Returns a list of line strings (never splits a single word, so a word
    wider than max_width on its own still gets its own line rather than
    being dropped or overflowing silently -- caller should still watch for
    that degenerate case with very small max_width)."""
    words = text.split(' ')
    lines, cur = [], ''
    for w in words:
        trial = (cur + ' ' + w).strip()
        if cur and text_width(trial, font_size, bold) > max_width:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def wrap_svg_text(x, y, text, max_width, font_size, anchor='middle',
                   line_height=None, bold=False):
    """Build a multi-line SVG <text> (with <tspan> per line) that fits
    max_width, replacing a single too-long line. y is the baseline of the
    FIRST line; subsequent lines step down by line_height (default 1.25em)."""
    if line_height is None:
        line_height = font_size * 1.25
    lines = wrap_text_lines(text, max_width, font_size, bold)
    tspans = ''.join(
        f'<tspan x="{x}" dy="{0 if i == 0 else line_height}">{line}</tspan>'
        for i, line in enumerate(lines)
    )
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{font_size}">{tspans}</text>', len(lines)


def fit_value_label(label, bar_x0, bar_x1, canvas_x0, canvas_x1, direction,
                     font_size=11.0, pad_outside=6.0, pad_inside=4.0):
    """Decide where a bar's value label goes and at what size.

    direction: 'right' for a bar that grows rightward from its base (the
    label's natural outside position is to the right of bar_x1); 'left' for
    a bar growing leftward (label's natural outside position is left of
    bar_x0).

    Returns dict(x, anchor, font_size, inside: bool) -- inside=True means
    render in white/contrast color; False means keep the bar's own hue.
    """
    label_w = text_width(label, font_size)
    bar_w = bar_x1 - bar_x0

    if direction == 'right':
        space_outside = canvas_x1 - bar_x1
        if label_w + pad_outside <= space_outside:
            return {'x': bar_x1 + pad_outside, 'anchor': 'start',
                    'font_size': font_size, 'inside': False}
        if label_w + 2 * pad_inside <= bar_w:
            return {'x': bar_x1 - pad_inside, 'anchor': 'end',
                    'font_size': font_size, 'inside': True}
        # neither fits at default size: shrink to whichever space is larger
        if space_outside >= bar_w:
            fs = font_size * max(0.0, space_outside - pad_outside) / max(label_w, 1)
            fs = max(MIN_FONT_SIZE, min(font_size, fs))
            return {'x': bar_x1 + pad_outside, 'anchor': 'start',
                    'font_size': round(fs, 1), 'inside': False}
        fs = font_size * max(0.0, bar_w - 2 * pad_inside) / max(label_w, 1)
        fs = max(MIN_FONT_SIZE, min(font_size, fs))
        return {'x': bar_x1 - pad_inside, 'anchor': 'end',
                'font_size': round(fs, 1), 'inside': True}

    else:  # direction == 'left'
        space_outside = bar_x0 - canvas_x0
        if label_w + pad_outside <= space_outside:
            return {'x': bar_x0 - pad_outside, 'anchor': 'end',
                    'font_size': font_size, 'inside': False}
        if label_w + 2 * pad_inside <= bar_w:
            return {'x': bar_x0 + pad_inside, 'anchor': 'start',
                    'font_size': font_size, 'inside': True}
        if space_outside >= bar_w:
            fs = font_size * max(0.0, space_outside - pad_outside) / max(label_w, 1)
            fs = max(MIN_FONT_SIZE, min(font_size, fs))
            return {'x': bar_x0 - pad_outside, 'anchor': 'end',
                    'font_size': round(fs, 1), 'inside': False}
        fs = font_size * max(0.0, bar_w - 2 * pad_inside) / max(label_w, 1)
        fs = max(MIN_FONT_SIZE, min(font_size, fs))
        return {'x': bar_x0 + pad_inside, 'anchor': 'start',
                'font_size': round(fs, 1), 'inside': True}
