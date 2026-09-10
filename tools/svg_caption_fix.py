#!/usr/bin/env python3
"""Fix the single most common chart bug in this archive: a chart's closing
source-note/caption line(s) are single <text> elements too long for the
canvas at their font-size, so they run off both edges. Wraps them into
<tspan> lines via svg_label_fit.wrap_svg_text, then grows the SVG's own
viewBox/background-rect height to fit the extra lines -- nothing below a
caption ever needs to move because these captions are always the last
elements before </svg> in this codebase's chart template.

Usage as a library (typical case -- see any recent commit for a worked
example):

    from svg_caption_fix import fix_stacked_captions
    fix_stacked_captions(
        'posts/foo.html',
        old_canvas=(700, 395),      # current viewBox/bg-rect w,h (must match exactly once)
        captions=[
            {'old_y': 368, 'text': 'Ratios are drawn from ...'},
            {'old_y': 381, 'text': 'Sources: Deutsche Bank/ICIS ...'},
        ],
        start_y=340,                # baseline of the first wrapped line
        max_width=620,
        gap_between=15,             # extra vertical gap before each *next* caption block
    )

Each caption's 'text' must be the exact HTML-entity-encoded text as it
appears between <text ...> and </text> in the file (so it can be matched
verbatim) -- copy it straight out of a `grep -n` on the file.
"""
import re
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from svg_label_fit import wrap_svg_text, wrap_text_lines

FONT_SIZE = 10.0
LINE_HEIGHT = FONT_SIZE * 1.25
CAPTION_FILL = '#868e96'


def _find_svg_open(body, w, h):
    """Locate the exact <svg ...viewBox="0 0 W H"...><rect .../> opening for
    a chart with these exact canvas dimensions. Raises if not found or if
    the match is ambiguous (more than one chart in the file shares W,H --
    pass a more specific old_canvas or call with occurrence= to disambiguate)."""
    pattern = re.compile(
        r'<svg\b[^>]*viewBox="0 0 ' + re.escape(f'{w} {h}') + r'"[^>]*>\s*'
        r'<rect x="0" y="0" width="' + re.escape(str(w)) + r'" height="' + re.escape(str(h)) + r'"[^/]*/>'
    )
    matches = list(pattern.finditer(body))
    if not matches:
        raise ValueError(f'no <svg viewBox="0 0 {w} {h}"><rect .../> found')
    return matches, pattern


def fix_stacked_captions(path, old_canvas, captions, start_y, max_width=620,
                          gap_between=15, bottom_margin=12, occurrence=0):
    body = open(path, encoding='utf-8').read()
    w, h = old_canvas

    matches, pattern = _find_svg_open(body, w, h)
    if len(matches) > 1 and occurrence is None:
        raise ValueError(
            f'{len(matches)} charts share canvas {w}x{h} in {path} -- '
            f'pass occurrence=0,1,... to pick one'
        )
    m = matches[occurrence if occurrence is not None else 0]
    old_open_block = m.group(0)

    y = start_y
    new_texts = []
    total_lines = 0
    for cap in captions:
        new_text, n = wrap_svg_text(350, y, cap['text'], max_width, FONT_SIZE,
                                     anchor=cap.get('anchor', 'middle'),
                                     line_height=LINE_HEIGHT)
        new_text = new_text.replace('<text ', f'<text fill="{CAPTION_FILL}" ', 1)
        new_texts.append(new_text)
        total_lines += n
        y += (n - 1) * LINE_HEIGHT + gap_between

    new_h = int(y - gap_between + bottom_margin)
    new_h = max(new_h, h)  # never shrink

    new_open_block = old_open_block.replace(f'viewBox="0 0 {w} {h}"', f'viewBox="0 0 {w} {new_h}"')
    new_open_block = re.sub(
        rf'(<rect x="0" y="0" width="{w}" height=")"?{h}"?', rf'\g<1>{new_h}"', new_open_block
    )

    body = body[:m.start()] + new_open_block + body[m.end():]

    for cap, new_text in zip(captions, new_texts):
        old_full = f'<text x="350" y="{cap["old_y"]}" text-anchor="{cap.get("anchor", "middle")}" font-size="{int(FONT_SIZE) if FONT_SIZE == int(FONT_SIZE) else FONT_SIZE}" fill="{CAPTION_FILL}">{cap["text"]}</text>'
        if old_full not in body:
            raise ValueError(f'could not find exact caption text to replace:\n{old_full!r}')
        body = body.replace(old_full, new_text, 1)

    open(path, 'w', encoding='utf-8').write(body)
    return new_h, total_lines


if __name__ == '__main__':
    print(__doc__)
