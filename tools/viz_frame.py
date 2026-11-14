"""Split a live post into the parts a visual-first edition keeps and the part it replaces.

    from viz_frame import split, text_of
    f = split(html)      # f.head, f.mid, f.body, f.keep_front, f.tail   (None if the frame is not standard)

A post is  head + mid + body + tail, where
  head  the page wrapper, styles, kicker, <h1> and standfirst block, up to the end of the title div
  lead  a hero figure between the title and the skip link (the edition may drop it: its chart becomes a section)
  mid   from the skip link to the end of the Google-translate widget (skip link, text-size bar, translate script)
  body  what the edition replaces (the article proper); picture figures and the "Updated" note are kept via keep_front
  tail  the first of: the "what this piece does not establish" card, the related-links box, the sources card
The edition is rebuilt as  head + [lead] + mid + STYLE + top line + kept pictures + insight sections + tail.
Posts that do not match this shape are not rewritten automatically (tools/viz_triage.py marks them)."""
import html as _html
import re
from collections import namedtuple

Frame = namedtuple("Frame", "head lead mid body keep_front notes tail")

_H1_END = re.compile(r"</h1>\s*(?:<p class=\"standfirst\">.*?</p>\s*)?(?:</div>\s*)?", re.S)
_TRANSLATE_END = re.compile(r"translate\.google\.com/translate_a/element\.js\?cb=googleTranslateElementInit\"></script>\s*", re.S)
_TAIL_MARKS = [
    r'<div class="gb-card gb-note">\s*<strong[^>]*>\s*What this piece (?:could not|does not|did not) establish',
    r'<div class="gb-related">',
    r'<div class="gb-card gb-note">\s*<strong[^>]*>\s*Documents',
    r'<h2 class="gb-h2">Sources and caveats</h2>',
    r'(?:<hr>\s*)?<h[23][^>]*>\s*Related on this blog',
    r'<h[23][^>]*>\s*(?:Sources|Documents(?: &amp;|&) sources)',
]


def split(html):
    h = _H1_END.search(html)
    t = _TRANSLATE_END.search(html, h.end()) if h else None
    if not (h and t):
        return None
    tails = [m.start() for p in _TAIL_MARKS for m in [re.search(p, html[t.end():], re.S)] if m]
    if not tails:
        return None
    tail_at = t.end() + min(tails)
    body = html[t.end():tail_at]
    if len(visible(body).split()) < 500:      # the match cut the article short: not a standard frame
        return None
    # keep photographs (and their credit lines) and an "Updated ..." note out of the rewrite
    keep = "".join(re.findall(r'<figure[^>]*>(?:(?!</figure>).)*?<img\b.*?</figure>', body, re.S))
    sk = html.find('<a href="#" id="gs-skip-link"', h.end(), t.end())
    sk = h.end() if sk < 0 else sk
    notes = "".join(re.findall(r'<div class="warn"[^>]*>\s*<b>Updated .*?</div>', body, re.S))   # dated update notes stay
    return Frame(html[:h.end()], html[h.end():sk], html[sk:t.end()], body, keep, notes, html[tail_at:])


def visible(html):
    """Reader-visible text: scripts, styles and svg removed, tags stripped, entities decoded."""
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S)
    s = re.sub(r"<svg.*?</svg>", lambda m: " ".join(re.findall(r">([^<]+)<", m.group(0))), s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", _html.unescape(s)).strip()


text_of = visible

_NUM = re.compile(r"(?<![\w.])[-+]?\d[\d,]*(?:\.\d+)?")


def numbers(text):
    """Canonical numeric tokens in text: commas removed, trailing zeros after a point dropped."""
    out = set()
    for m in _NUM.finditer(text):
        t = m.group(0).lstrip("+-").replace(",", "").rstrip(".")
        if "." in t:
            t = t.rstrip("0").rstrip(".")
        out.add(t)
    return out


def outline(body_html):
    """A compact, readable outline of a post body for the agent writing its edition: headings, paragraphs,
    list items, and tables as pipe rows. SVG charts are summarised by their text. Links are kept as [text](url)."""
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body_html, flags=re.S)
    s = re.sub(r"<svg.*?</svg>", lambda m: "\n[chart: " + " ".join(re.findall(r">([^<]+)<", m.group(0)))[:600] + "]\n", s, flags=re.S)
    s = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f"[{re.sub('<[^>]+>', '', m.group(2))}]({m.group(1)})", s, flags=re.S)
    s = re.sub(r"</t[dh]>\s*<t[dh][^>]*>", " | ", s)
    s = re.sub(r"<tr[^>]*>\s*<t[dh][^>]*>", "\n| ", s)
    s = re.sub(r"</tr>", " |", s)
    s = re.sub(r"<h([1-6])[^>]*>", lambda m: "\n\n" + "#" * int(m.group(1)) + " ", s)
    s = re.sub(r"<div class=\"gb-h2\"[^>]*>", "\n\n## ", s)
    s = re.sub(r"<li[^>]*>", "\n- ", s)
    s = re.sub(r"</(p|div|h[1-6]|ul|ol|table|figure|figcaption|section)>", "\n", s)
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = _html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    return re.sub(r"\n{3,}", "\n\n", s).strip()


def body_links(body_html):
    """External links in the original body: [(url, text)], first occurrence of each url."""
    seen, out = set(), []
    for u, t in re.findall(r'<a [^>]*href="(https?://[^"#]+)[^"]*"[^>]*>(.*?)</a>', body_html, re.S):
        if "blog.vertistratsolution.com" in u or u in seen:
            continue
        seen.add(u)
        out.append((u, re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", "", t))).strip()))
    return out
