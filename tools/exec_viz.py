#!/usr/bin/env python3
"""Visual-first building blocks for posts: top-line KPIs, insight sections and phone-readable charts.

    import sys; sys.path.insert(0, "tools"); from exec_viz import *
    body = STYLE + top_line([...]) + insight("Headline that states the takeaway", bars(...), "What it means.", "What to do.")

Why this exists: the 14 Nov 2026 audit (docs/MOBILE_READABILITY.md) rendered all 526 posts at 375px.
88% of the inline SVG charts were drawn about 700px wide and shrunk to fit, so their labels
rendered at a median 6.1px. These charts are HTML and CSS instead: bar length is a percentage,
every label is real text at body size, and nothing scales down on a phone. Only the line chart
is SVG, and it ships two drawings (360 and 640 wide) so its labels stay at 12-13px on both.

House rules the functions enforce (see docs/VISUAL_STORY_STYLE.md):
  - The chart title states the takeaway ("Brazil and Europe cap chloride at 1 to 1.5 mg/kg"),
    never a label ("Chloride limits"). Titles over 90 characters raise.
  - Muted grey for every mark except one accent: the finding the title is about.
  - No gridlines; a hairline baseline at most; values printed on the marks that matter.
  - Every chart can carry a collapsed "Show the numbers" table (numbers()), never an open grid.
  - No JavaScript: the main site (vertistratsolution.com) strips scripts from posts.
"""
import html as _html
import re
import itertools as _it

ACCENT, GREY, INK, SOFT, LINE = "#2251FF", "#A9B4BF", "#0B1F2D", "#43535F", "#D9E1E8"
_ids = _it.count(1)

STYLE = f"""<style>
.xv-top,.xv,.xv-flow,.xv-so,.xv-n{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif}}
.xv-top{{border-left:4px solid {ACCENT};background:#F4F7FB;padding:1rem 1.1rem;margin:1.2rem 0 1.8rem;border-radius:0 10px 10px 0}}
.xv-top .xv-eb{{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:{SOFT};font-weight:700;margin:0 0 .6rem}}
.xv-top ul{{list-style:none;margin:0;padding:0}}
.xv-top li{{margin:0 0 .85rem;padding:0;line-height:1.45;color:{INK};font-size:1rem}}
.xv-top li:last-child{{margin-bottom:0}}
.xv-top .xv-k{{display:block;font-size:1.65rem;font-weight:800;letter-spacing:-.02em;line-height:1.15;color:{INK}}}
.xv{{margin:1.1rem 0 1.4rem;padding:0;max-width:640px}}
.xv figcaption{{margin:0 0 .7rem}}
.xv .xv-t{{display:block;font-size:1.05rem;font-weight:700;line-height:1.35;color:{INK}}}
.xv .xv-u{{display:block;font-size:.82rem;color:{SOFT};margin-top:.15rem;line-height:1.4}}
.xv .xv-key{{font-size:.8rem;color:{SOFT};margin:0 0 .5rem;line-height:1.4}}
.xv .xv-key i{{display:inline-block;width:2px;height:.9em;background:{INK};vertical-align:-.1em;margin-right:.35em}}
.xv .xv-r{{margin:0 0 .7rem}}
.xv .xv-l{{display:flex;justify-content:space-between;align-items:baseline;gap:.75rem;font-size:.88rem;line-height:1.3;color:{INK};margin:0 0 .22rem}}
.xv .xv-l>span{{min-width:0}}
.xv .xv-l small{{color:{SOFT};font-size:.92em}}
.xv .xv-tk{{position:relative;display:flex;align-items:center;min-height:16px}}
.xv .xv-b{{display:block;height:14px;min-width:3px;background:{GREY};border-radius:0 4px 4px 0;flex:none}}
.xv .xv-b.xv-float{{border-radius:4px}}
.xv .xv-hi .xv-b{{background:{ACCENT}}}
.xv .xv-v{{font-size:.88rem;font-weight:600;color:{INK};white-space:nowrap;font-variant-numeric:tabular-nums;flex:none}}
.xv .xv-hi .xv-v{{font-weight:800}}
.xv .xv-tk.xv-div{{display:block;height:14px}}
.xv .xv-div .xv-b{{position:absolute;top:0;border-radius:4px}}
.xv .xv-div .xv-neg{{background:#7d8a96}}
.xv .xv-hi .xv-div .xv-neg,.xv .xv-hi.xv-divrow .xv-neg{{background:{ACCENT}}}
.xv .xv-none{{display:block;flex:1;height:12px;border:1.5px dashed {ACCENT};background:#E9EEFF;border-radius:4px}}
.xv .xv-m{{position:absolute;top:-3px;bottom:-3px;width:2px;background:{INK}}}
.xv .xv-svg{{display:block;width:100%;height:auto}}
.xv .xv-svg.xv-wide{{display:none}}
@media (min-width:600px){{.xv .xv-svg.xv-narrow{{display:none}}.xv .xv-svg.xv-wide{{display:block}}}}
.xv .xv-leg{{font-size:.8rem;color:{SOFT};margin:.1rem 0 .5rem}}
.xv .xv-leg span{{margin-right:.9rem;white-space:nowrap}}
.xv .xv-leg i{{display:inline-block;width:14px;height:3px;border-radius:2px;vertical-align:middle;margin-right:.35rem}}
.xv .xv-s{{font-size:.75rem;color:{SOFT};margin:.6rem 0 0;line-height:1.45}}
.xv-flow{{list-style:none;margin:1rem 0 1.4rem;padding:0 0 0 18px;border-left:2px solid {LINE};max-width:640px}}
.xv-flow li{{position:relative;margin:0 0 1rem;padding:0 0 0 .4rem;line-height:1.45;font-size:.92rem;color:{INK}}}
.xv-flow li::before{{content:"";position:absolute;left:-24px;top:.3rem;width:10px;height:10px;border-radius:50%;background:{GREY};box-shadow:0 0 0 3px #fff}}
.xv-flow li.xv-hi::before{{background:{ACCENT}}}
.xv-flow b{{display:block;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:{SOFT}}}
.xv-sec .xv-so{{font-size:.98rem;line-height:1.55;color:{INK};background:#F4F7FB;border-radius:8px;padding:.75rem .9rem;margin:.4rem 0 1.6rem}}
.xv-sec .xv-so p{{margin:0;max-width:none}}
.xv-sec .xv-so p+p{{margin-top:.55rem}}
.xv-sec .xv-so b{{color:{INK}}}
.xv-n{{margin:.2rem 0 1.4rem;font-size:.85rem}}
.xv-n summary{{cursor:pointer;color:#0b5394;font-weight:600;padding:.3rem 0}}
.xv-n table{{margin:.5rem 0 0}}
</style>
"""

esc = _html.escape


def _title(t):
    if len(_html.unescape(t)) > 90:
        raise ValueError(f"chart title over 90 characters: {t!r}")
    return t


def _fmt(v, unit=""):
    if float(v) < 0:
        out = _fmt(-v, unit)
        return "-" + out
    s = f"{v:,.0f}" if float(v).is_integer() else f"{v:,.2f}".rstrip("0").rstrip(".")      # never round a figure into a different number
    if not unit:
        return s
    m = re.fullmatch(r"([$\u20b9\u20ac\u00a3])\s*(.*)", unit.strip())      # "$/kg" -> "$4.21/kg"; "\u20b9 crore" -> "\u20b958,711 crore"
    if m:
        rest = m.group(2)
        return f"{m.group(1)}{s}" + (rest if not rest or rest.startswith("/") else f" {rest}")
    if re.match(r"[A-Za-z]", unit):                                           # "USD/t", "mmscmd" -> "419 USD/t"
        return f"{s} {unit}"
    return s + unit


def _fig(title, sub, inner, source):
    i = next(_ids)
    sub = f'<span class="xv-u">{sub}</span>' if sub else ""
    src = f'<p class="xv-s">{source}</p>' if source else ""
    return (f'<figure class="xv" aria-labelledby="xv{i}"><figcaption><span class="xv-t" id="xv{i}">{_title(title)}</span>'
            f'{sub}</figcaption>{inner}{src}</figure>\n')


def top_line(items, eyebrow="Top line"):
    """items: three (big_number, sentence) pairs. The number goes first and large."""
    if not 1 <= len(items) <= 3:
        raise ValueError("the top line takes at most 3 bullets")
    li = "".join(f'<li><span class="xv-k">{k}</span>{t}</li>' for k, t in items)
    return f'<div class="xv-top"><p class="xv-eb">{eyebrow}</p><ul>{li}</ul></div>\n'


def _row(accented, tip, label, value, track, cls="xv-tk"):
    """One bar row: the label and its value share the top line (value right-aligned), the bar runs full width below."""
    return (f'<div class="xv-r{" xv-hi" if accented else ""}" title="{esc(_html.unescape(tip))}"><div class="xv-l"><span>{label}</span>'
            f'<b class="xv-v">{value}</b></div><div class="{cls}">{track}</div></div>')


def bars(title, rows, *, unit="", sub="", source="", accent=None, ref=None, vmax=None, fmt=None, from_zero=False):
    """Horizontal bars, label above each bar so long labels never squeeze the plot.

    rows:   (label, value[, note[, shown]]); value None draws a dashed "no value" track; value may be a (low, high)
            pair (floating bar, or with from_zero=True a bar from zero, solid to the low end and lighter to the high
            end); a negative value draws left of a zero line (the other bars right of it). `shown` is the exact text
            to print as the value (keeps the original's currency signs and digit grouping).
    accent: label (or list of labels) drawn in the accent colour; everything else is grey.
    ref:    (value, text) draws a thin marker on every track and explains it once above the chart.
    """
    acc = {accent} if isinstance(accent, str) else set(accent or ())
    vals = [x for r in rows if r[1] is not None for x in (r[1] if isinstance(r[1], tuple) else (r[1],))]
    neg = min(vals + [0]) < 0
    lo_all = min(vals + [0]) if neg else 0
    hi_all = max(vals + ([ref[0]] if ref else []) + ([0] if neg else []))      # all-negative rows: the zero line is the right edge
    top = vmax or hi_all
    span = (top - lo_all) or 1
    zero = 100 * (-lo_all) / span if neg else 0
    plain = fmt is None
    fmt = fmt or (lambda v: _fmt(v, unit))
    sym = (re.match(r"[$\u20b9\u20ac\u00a3]", unit.strip()) or [""])[0] if plain else ""
    fmt_lo = (lambda v: _fmt(v, sym)) if plain else fmt        # "\u20b932,000\u2013\u20b934,000 crore": the symbol on both ends, the unit word once
    out = []
    if ref:
        out.append(f'<p class="xv-key"><i></i>{ref[1]}</p>')
    for r in rows:
        lab, v = r[0], r[1]
        note = f" <small>{r[2]}</small>" if len(r) > 2 and r[2] else ""
        shown = r[3] if len(r) > 3 and r[3] else None
        pos = lambda x: (100 * (x - lo_all) / span) if neg else (100 * x / top)
        mark = f'<i class="xv-m" style="left:{pos(ref[0]):.2f}%" aria-hidden="true"></i>' if ref else ""
        cls = "xv-tk xv-div" if neg else "xv-tk"
        if v is None:
            val, tip, bar = shown or "none", f"{lab}: none", '<i class="xv-none" aria-hidden="true"></i>'
            cls = "xv-tk"
        elif isinstance(v, tuple):
            lo, hv = v
            val, tip = shown or f"{fmt_lo(lo)}&ndash;{fmt(hv)}", f"{lab}: {fmt(lo)} to {fmt(hv)}"
            if from_zero:
                c = ACCENT if lab in acc else GREY
                cut = 100 * lo / hv if hv else 100
                bar = (f'<i class="xv-b" style="width:{max(pos(hv), .6):.2f}%;background:linear-gradient(90deg,{c} {cut:.1f}%,'
                       f'{c}55 {cut:.1f}%)"></i>')
            else:
                bar = f'<i class="xv-b xv-float" style="margin-left:{pos(lo):.2f}%;width:{max(pos(hv) - pos(lo), .6):.2f}%"></i>'
        elif neg:
            val, tip = shown or fmt(v), f"{lab}: {fmt(v)}"
            w = max(100 * abs(v) / span, .6)
            left = zero if v >= 0 else zero - w
            bar = (f'<i class="xv-b{"" if v >= 0 else " xv-neg"}" style="left:{left:.2f}%;width:{w:.2f}%;'
                   f'{"border-radius:0 4px 4px 0" if v >= 0 else "border-radius:4px 0 0 4px"}"></i>'
                   f'<i class="xv-m" style="left:{zero:.2f}%" aria-hidden="true"></i>')
        else:
            val, tip = shown or fmt(v), f"{lab}: {fmt(v)}"
            bar = f'<i class="xv-b" style="width:{max(pos(v), .6):.2f}%"></i>'
        out.append(_row(lab in acc, tip, lab + note, val, bar + mark, cls))
    return _fig(title, sub, "".join(out), source)


def waterfall(title, start, steps, end_label, *, unit="", sub="", source="", accent=None):
    """start: (label, value); steps: [(label, delta)]; the end bar is computed and checked.
    The accent goes on the end bar unless accent names a step (the biggest driver, say)."""
    pts, run = [], start[1]
    for lab, d in steps:
        pts.append((lab, run, run + d, d))
        run += d
    top = max([start[1], run] + [max(a, b) for _, a, b, _ in pts])
    sc = lambda v: 100 * v / top
    acc = accent or end_label
    out = [_row(acc == start[0], f"{start[0]}: {_fmt(start[1], unit)}", start[0], _fmt(start[1], unit),
                f'<i class="xv-b" style="width:{sc(start[1]):.2f}%"></i>')]
    for lab, a, b, d in pts:
        lo, w = min(a, b), abs(b - a)
        sign = "+" if d >= 0 else "&minus;"
        shade = "" if d >= 0 else ";background:#7d8a96"
        out.append(_row(acc == lab, f"{lab}: {'+' if d >= 0 else '-'}{_fmt(abs(d), unit)}", lab, f"{sign}{_fmt(abs(d), unit)}",
                        f'<i class="xv-b xv-float" style="margin-left:{sc(lo):.2f}%;width:{max(sc(w), .6):.2f}%{shade}"></i>'))
    out.append(_row(acc == end_label, f"{end_label}: {_fmt(run, unit)}", f"<b>{end_label}</b>", _fmt(run, unit),
                    f'<i class="xv-b" style="width:{sc(run):.2f}%"></i>'))
    return _fig(title, sub, "".join(out), source)


def _us(unit):
    """Unit as a suffix: a word unit gets a space ("3,177 thousand tonnes"), % and symbols do not."""
    return " " + unit if unit and re.match(r"[A-Za-z]", unit) else unit


def _lv(s, unit):
    """A formatted number with its unit: symbols go in front (\u20b9 lakh crore -> \u20b916.32 lakh crore), words after."""
    m = re.fullmatch(r"([$\u20b9\u20ac\u00a3])\s*(.*)", (unit or "").strip())
    if m:
        rest = m.group(2)
        return f"{m.group(1)}{s}" + (rest if not rest or rest.startswith("/") else f" {rest}")
    return s + _us(unit)


def _line_svg(series, accent, W, fs, unit, yfmt, cls):
    one = len(series) == 1          # a single line needs no name beside it: the title says what it is
    longest = max(len((f"{_html.unescape(k)} " if not one else "") + _lv(yfmt(s[-1][1]), unit)) for k, s in series.items())
    H, L, T, B = (230 if W < 500 else 260), 8, 22, 26
    R = min(int(longest * fs * 0.6) + 14, W // 2)
    xs = [x for s in series.values() for x, _ in s]
    ys = [y for s in series.values() for _, y in s]
    x0, x1 = min(xs), max(xs)
    y0, y1 = min(0, min(ys)), max(ys) * 1.08
    px = lambda x: L + (W - L - R) * (x - x0) / ((x1 - x0) or 1)
    py = lambda y: T + (H - T - B) * (1 - (y - y0) / ((y1 - y0) or 1))
    s = [f'<svg class="xv-svg {cls}" viewBox="0 0 {W} {H}" role="img" aria-hidden="{"true" if cls == "xv-wide" else "false"}" '
         f'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif">',
         f'<line x1="{L}" x2="{W - R}" y1="{py(y0):.1f}" y2="{py(y0):.1f}" stroke="{LINE}" stroke-width="1"/>',
         f'<text x="{L}" y="{T - 8}" font-size="{fs - 1}" fill="{SOFT}">{_lv(yfmt(y1 / 1.08), unit)}</text>',
         f'<line x1="{L}" x2="{W - R}" y1="{py(y1 / 1.08):.1f}" y2="{py(y1 / 1.08):.1f}" stroke="{LINE}" stroke-width="1"/>',
         f'<text x="{L}" y="{H - 6}" font-size="{fs - 1}" fill="{SOFT}">{x0:g}</text>',
         f'<text x="{W - R}" y="{H - 6}" font-size="{fs - 1}" fill="{SOFT}" text-anchor="end">{x1:g}</text>']
    order = [k for k in series if k != accent] + ([accent] if accent in series else [])
    ends = []
    for k in order:
        pts = series[k]
        c, w = (ACCENT, 2.5) if k == accent else (GREY, 2)
        d = " ".join(f"{'M' if i == 0 else 'L'}{px(x):.1f},{py(y):.1f}" for i, (x, y) in enumerate(pts))
        s.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round">'
                 f'<title>{esc(_html.unescape(k))}: {yfmt(pts[0][1])} to {_lv(yfmt(pts[-1][1]), unit)}</title></path>')
        xe, ye = pts[-1]
        s.append(f'<circle cx="{px(xe):.1f}" cy="{py(ye):.1f}" r="4" fill="{c}" stroke="#fff" stroke-width="2"/>')
        ends.append([py(ye), k, yfmt(ye), k == accent])
    ends.sort()
    for i in range(1, len(ends)):                      # keep end labels at least one line apart
        ends[i][0] = max(ends[i][0], ends[i - 1][0] + fs + 2)
    for y, k, v, a in ends:
        s.append(f'<text x="{W - R + 8}" y="{y + fs / 3:.1f}" font-size="{fs}" fill="{INK}" font-weight="{800 if a else 500}">'
                 f'{esc(_html.unescape(k)) + " " if not one else ""}{_lv(v, unit)}</text>')
    s.append("</svg>")
    return "".join(s)


def line(title, series, *, accent=None, unit="", sub="", source="", yfmt=None):
    """series: {name: [(x, y), ...]}. Grey lines, one accent line, end labels instead of a legend box
    for up to 4 series (a compact legend is added as well, so colour never carries identity alone)."""
    yfmt = yfmt or (lambda v: _fmt(v))
    leg = ""
    if len(series) > 1:
        leg = '<p class="xv-leg">' + "".join(
            f'<span><i style="background:{ACCENT if k == accent else GREY}"></i>{k}</span>' for k in series) + "</p>"
    inner = leg + _line_svg(series, accent, 360, 13, unit, yfmt, "xv-narrow") + _line_svg(series, accent, 640, 13, unit, yfmt, "xv-wide")
    return _fig(title, sub, inner, source)


def flow(events):
    """A vertical timeline: events are (when, text) or (when, text, True) for the accented one."""
    hi = ' class="xv-hi"'
    li = "".join(f'<li{hi if len(e) > 2 and e[2] else ""}><b>{e[0]}</b>{e[1]}</li>' for e in events)
    return f'<ol class="xv-flow">{li}</ol>\n'


def numbers(head, rows, summary="Show the numbers"):
    """The chart's data as a small table, collapsed by default (the accessible table view)."""
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return (f'<details class="xv-n"><summary>{summary}</summary><div class="gb-tblwrap"><table class="gb-table">'
            f'<thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div></details>\n')


def insight(headline, chart, means, todo, anchor=""):
    """One section: an insight headline, one chart, then exactly two sentences: what it means, what to do."""
    _title(headline)
    for s in (means, todo):
        plain = _html.unescape(s).strip()
        if plain.count(". ") > 0 or not plain.endswith("."):
            raise ValueError(f"insight text must be one sentence ending in a full stop: {plain!r}")
    a = f' id="{anchor}"' if anchor else ""
    return (f'<section class="xv-sec"><h2 class="gb-h2"{a}>{headline}</h2>\n{chart}'
            f'<div class="xv-so"><p><b>What it means:</b> {means}</p><p><b>What to do:</b> {todo}</p></div></section>\n')


def sources_block(links, summary="Sources cited in the article"):
    """The original body's external links, kept as a collapsed list: links = [(url, text)] from viz_frame.body_links."""
    if not links:
        return ""
    li = "".join(f'<li><a href="{esc(u)}">{esc(t or u)}</a></li>' for u, t in links)
    return f'<details class="xv-n"><summary>{summary}</summary><ul>{li}</ul></details>\n'
