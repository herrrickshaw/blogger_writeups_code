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


# ---------------------------------------------------------------- mechanical extraction (no model needed)
def _clean(h):
    return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()


def tables(body_html):
    """Every table in the body as {id, title, head, rows}; title is the nearest heading above it."""
    out = []
    for m in re.finditer(r"<table\b.*?</table>", body_html, re.S):
        rows = []
        for r in re.findall(r"<tr\b.*?</tr>", m.group(0), re.S):
            cells = [_clean(c) for c in re.findall(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", r, re.S)]
            if any(cells):
                rows.append(cells)
        if len(rows) < 2:
            continue
        hs = re.findall(r'<(?:h[1-6]|div class="gb-h2")[^>]*>(.*?)</(?:h[1-6]|div)>', body_html[:m.start()], re.S)
        out.append({"id": f"T{len(out) + 1}", "title": _clean(hs[-1]) if hs else "", "head": rows[0], "rows": rows[1:]})
    return out


_HEAD = r'(?:<h[1-6][^>]*>|<div class="gb-h2"[^>]*>)'


def _section(body_html, heading_re):
    """HTML of the first section whose heading matches heading_re, without the heading: (title, inner_html) or None."""
    m = re.search(rf"({_HEAD})(?=[^<]*(?:<[^>]+>[^<]*)*?(?:{heading_re}))(.*?)</(?:h[1-6]|div)>", body_html, re.S | re.I)
    for h in re.finditer(rf"{_HEAD}(.*?)</(?:h[1-6]|div)>", body_html, re.S):
        if re.search(heading_re, _clean(h.group(1)), re.I):
            nxt = re.search(_HEAD, body_html[h.end():])
            inner = body_html[h.end(): h.end() + nxt.start()] if nxt else body_html[h.end():]
            return _clean(h.group(1)), inner.strip()
    return None


def caveat(body_html):
    """The original's 'what this could not establish' block when it sits in the body: (title, html) or None.
    A heading section when there is one, otherwise the paragraph or box that contains the phrase."""
    pat = r"(?:could|does|did|can)(?:\s*not|n.t)\s+establish|not established|what this (?:piece )?(?:leaves|cannot)"
    sec = _section(body_html, pat)
    if sec:
        return sec
    m = re.search(pat, body_html, re.I)
    if not m:
        return None
    starts = [x for x in re.finditer(r"<(p|div|li)\b[^>]*>", body_html[:m.start()])]
    if not starts:
        return None
    st = starts[-1]
    end = body_html.find(f"</{st.group(1)}>", m.end())
    if end < 0:
        return None
    return "What this piece could not establish", body_html[st.start(): end + len(st.group(1)) + 3]


def fixes(body_html):
    return _section(body_html, r"what would fix|proposed fixes|what should change|^fixes\b|recommendations")


def update_notes(body_html):
    """Dated 'Updated <date>' notices (div or p), kept in the edition verbatim."""
    return "".join(m.group(0) for m in re.finditer(r"<(div|p)\b[^>]*>\s*(?:<b>|<strong>)?\s*Updated \d{1,2} [A-Z][a-z]+ 20\d\d.*?</\1>", body_html, re.S))
