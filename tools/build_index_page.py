#!/usr/bin/env python3
"""Build the article index page: by topic, by geography, and as an entity graph.

    python3 tools/index_graph.py --json /tmp/graph.json
    python3 tools/build_index_page.py --graph /tmp/graph.json --out out/post-index.html

THREE WAYS IN, BECAUSE ONE IS NEVER RIGHT FOR EVERYONE
    by topic      thirteen Blogger labels, which are live hub pages and stay
                  current on their own as posts are added
    by geography  the countries and Indian states a piece is actually about
    by connection an entity co-occurrence graph, plus per-post related links

THE GRAPH IS DRAWN, NOT EMBEDDED
    The diagram is static inline SVG with a deterministic circular layout: no
    JavaScript, no external library, no layout engine whose output changes
    between builds. Node radius encodes the number of posts, edge opacity the
    number of posts two entities share. A force-directed layout would look more
    organic and would land differently on every rebuild, which makes it
    impossible to tell a data change from a jitter.
"""
import argparse
import collections
import html
import itertools
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LABEL_HUBS = [
    ("Trade & Tariffs", "Trade%20%26%20Tariffs"),
    ("Industrial Policy", "Industrial%20Policy"),
    ("Agriculture & Fertilisers", "Agriculture%20%26%20Fertilisers"),
    ("Energy & Fuels", "Energy%20%26%20Fuels"),
    ("Import Substitution", "Import%20Substitution"),
    ("Markets & Finance", "Markets%20%26%20Finance"),
    ("Chemicals", "Chemicals"),
    ("Prices & Inflation", "Prices%20%26%20Inflation"),
    ("Textiles", "Textiles"),
    ("Gas & LNG", "Gas%20%26%20LNG"),
    ("Climate & Carbon", "Climate%20%26%20Carbon"),
    ("Mobility & EV", "Mobility%20%26%20EV"),
    ("AI Tools", "AI%20Tools"),
]
E = lambda s: html.escape(s, quote=True)
_MON = ["January","February","March","April","May","June","July","August",
        "September","October","November","December"]


def _pretty_date(iso):
    if not iso or len(iso) < 10:
        return "?"
    y, m, d = iso[:4], int(iso[5:7]), int(iso[8:10])
    return f"{d} {_MON[m-1]} {y}"


def _pretty_month(ym):
    y, m = ym[:4], int(ym[5:7])
    return f"{_MON[m-1]} {y}"


def svg_graph(posts, min_posts=5, max_nodes=18):
    """Circular entity co-occurrence graph as static SVG."""
    cnt = collections.Counter(e for p in posts.values() for e in p["entities"])
    nodes = [e for e, n in cnt.most_common(max_nodes) if n >= min_posts]
    idx = {e: i for i, e in enumerate(nodes)}
    co = collections.Counter()
    for p in posts.values():
        for a, b in itertools.combinations(sorted(set(p["entities"]) & set(nodes)), 2):
            co[(a, b)] += 1
    if not nodes:
        return "<p>no graph</p>"
    # Labels sit outside the ring, so the canvas has to be wider than the ring
    # by the longest label. Measured, not guessed: at 13px Georgia the longest
    # subject name here needs ~180px, and a 268px ring on a 760px canvas
    # overflowed by one label.
    W, H = 920, 780
    cx, cy = W / 2, H / 2
    R = 232
    pos = {}
    for e, i in idx.items():
        a = -math.pi / 2 + 2 * math.pi * i / len(nodes)
        pos[e] = (cx + R * math.cos(a), cy + R * math.sin(a), a)
    mx = max(co.values()) if co else 1
    parts = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" '
             f'aria-label="Entity co-occurrence graph across the blog\'s articles" '
             f'style="max-width:920px;display:block;margin:0 auto">']
    parts.append('<title>How the subjects connect</title>')
    for (a, b), n in sorted(co.items(), key=lambda x: x[1]):
        if n < 2:
            continue
        x1, y1, _ = pos[a]; x2, y2, _ = pos[b]
        o = 0.10 + 0.55 * (n / mx)
        w = 0.6 + 3.0 * (n / mx)
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                     f'stroke="#0a4c6a" stroke-opacity="{o:.2f}" stroke-width="{w:.1f}"/>')
    mxc = max(cnt[e] for e in nodes)
    for e in nodes:
        x, y, a = pos[e]
        r = 5 + 13 * (cnt[e] / mxc)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#8a4b08" '
                     f'stroke="#fff" stroke-width="2"/>')
        deg = math.degrees(a)
        right = -90 <= deg <= 90
        tx = x + (r + 8) * math.cos(a)
        ty = y + (r + 8) * math.sin(a)
        anchor = "start" if right else "end"
        parts.append(f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="{anchor}" '
                     f'dominant-baseline="middle" font-size="13" font-family="Georgia,serif" '
                     f'fill="#1a1a1a">{E(e)} <tspan fill="#595959">{cnt[e]}</tspan></text>')
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--graph", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--shell-head", default=None)
    ap.add_argument("--shell-tail", default=None)
    args = ap.parse_args()

    posts = json.loads(Path(args.graph).read_text(encoding="utf-8"))
    # utility pages are navigation, not articles
    for s in ("article-index-start-here", "about-author"):
        posts.pop(s, None)

    by_country = collections.defaultdict(list)
    by_state = collections.defaultdict(list)
    for slug, p in posts.items():
        for c in p["countries"]:
            by_country[c].append(slug)
        for s in p["states"]:
            by_state[s].append(slug)

    o = []
    A = o.append
    A('<p class="eyebrow">Masala Deutsch &middot; Article index</p>')
    A('<h1>Every piece on this blog, three ways in</h1>')
    dates = sorted(p["published"] for p in posts.values() if p["published"])
    first, last = (dates[0], dates[-1]) if dates else ("", "")
    months = collections.Counter(p["published"][:7] for p in posts.values() if p["published"])
    A(f'<p class="standfirst">Every piece published on this blog since it opened on '
      f'{_pretty_date(first)} &mdash; {len(posts)} articles on India&rsquo;s trade, energy and '
      'industrial policy, each checked against official statistics. Browse by date, by topic, by '
      'the country or state a piece is about, or by how the subjects connect to each other.</p>')
    A('<div class="stats">'
      f'<div class="stat"><b>{len(posts)}</b><span>Articles</span></div>'
      f'<div class="stat"><b>{len(LABEL_HUBS)}</b><span>Topic hubs</span></div>'
      f'<div class="stat"><b>{len(by_country)}</b><span>Countries covered</span></div>'
      f'<div class="stat"><b>{_pretty_date(first)}</b><span>First post &mdash; the blog opens</span></div>'
      '</div>')

    # ---- by date ----------------------------------------------------------
    A('<h2>By date</h2>')
    A('<p class="h2sub">The whole publishing history, including the part where nothing happened.</p>')
    gap_note = ""
    if len(dates) > 1:
        d0, d1 = dates[0][:10], dates[1][:10]
        y0, y1 = int(d0[:4]), int(d1[:4])
        if y1 - y0 >= 1:
            gap_note = (f'<p>The blog opened on <b>{_pretty_date(dates[0])}</b> with a single post, '
                        f'and then published nothing for <b>{y1 - y0} years</b>. The archive proper '
                        f'begins on <b>{_pretty_date(dates[1])}</b>. That gap is left visible here '
                        'rather than smoothed away: the counts below are what was actually '
                        'published, not a reconstruction.</p>')
    A(gap_note)
    A('<div class="tw"><table>')
    A('<thead><tr><th>Month</th><th>Articles</th><th>Running total</th></tr></thead><tbody>')
    run = 0
    for m in sorted(months):
        run += months[m]
        A(f'<tr><td>{_pretty_month(m)}</td><td>{months[m]}</td><td>{run}</td></tr>')
    A('</tbody></table></div>')
    A('<p class="exsrc">Counted from each post&rsquo;s Blogger publication date as recorded in the '
      'archive manifest. Three earlier drafts and duplicate variants were withdrawn before this '
      'index was built and are not listed; they have no live URL to link to.</p>')

    # ---- topics -----------------------------------------------------------
    A('<h2>By topic</h2>')
    A('<p class="h2sub">Live hub pages. Each updates itself as new pieces are labelled.</p>')
    A('<div class="chips">')
    # Alphabetical, case-insensitive, to match the site-wide topic browse.
    # Ordering by post count put the biggest topics first, which reads as a
    # ranking nobody asked for and moves whenever a post is labelled.
    for name, slugpart in sorted(LABEL_HUBS, key=lambda t: t[0].lower()):
        n = 0
        A(f'<a class="chip" href="https://masaladeutsch.blogspot.com/search/label/{slugpart}">{E(name)}</a>')
    A('</div>')

    # ---- AI tracker ---------------------------------------------------------
    # A standing serial, not a one-off analysis. It sits in its own section
    # because a reader looking for "the latest edition" should not have to find
    # it among 96 dated articles, and because each new edition replaces the last
    # at the same URL rather than adding a row to the list.
    trk = next((p for s_, p in posts.items() if "ai-high-demand-launch-tracker" in s_), None)
    if trk:
        A('<h2>AI Tools</h2>')
        A('<p class="h2sub">The weekly AI tools update. Newest edition at a fixed address.</p>')
        A('<div class="serial">')
        A(f'<p class="ptitle"><a href="{E(trk["url"])}">{E(trk["title"])}</a></p>')
        A('<p class="pmeta">Updated in place each edition &mdash; the link above always '
          'points at the current one.</p>')
        A('<p>Ranks AI launches across five fixed categories &mdash; coding and developer '
          'tools, agentic platforms, foundation models, consumer AI, automation &mdash; by '
          'traction that can be checked. Star counts come from the GitHub API rather than '
          'from roundups, and anything that cannot be verified to that standard is labelled '
          'as unverified rather than ranked alongside what can.</p>')
        A(f'<p class="prel"><span>Hub</span> <a href="https://masaladeutsch.blogspot.com/'
          f'search/label/AI%20Tools">All AI Tools editions</a></p>')
        A('</div>')

    # ---- geography --------------------------------------------------------
    A('<h2>By geography</h2>')
    A('<p class="h2sub">The country or state a piece is actually about, not every place it mentions.</p>')
    A('<p>Almost everything here is about India, so India is not a category &mdash; it would '
      'hold every article and tell you nothing. What follows is the <i>second</i> geography: '
      'the counterpart economy a trade piece measures against, or the Indian state whose '
      'policy is under examination.</p>')

    A('<h3>Counterpart economies</h3>')
    A('<div class="geo">')
    for c, slugs in sorted(by_country.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        if len(slugs) < 1:
            continue
        A(f'<div class="geoblock"><p class="geoh">{E(c)} <span>{len(slugs)}</span></p><ul>')
        for s in sorted(slugs, key=lambda s: posts[s]["title"]):
            A(f'<li><a href="{E(posts[s]["url"])}">{E(posts[s]["title"])}</a></li>')
        A('</ul></div>')
    A('</div>')

    A('<h3>Indian states</h3>')
    A('<div class="geo">')
    for c, slugs in sorted(by_state.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        A(f'<div class="geoblock"><p class="geoh">{E(c)} <span>{len(slugs)}</span></p><ul>')
        for s in sorted(slugs, key=lambda s: posts[s]["title"]):
            A(f'<li><a href="{E(posts[s]["url"])}">{E(posts[s]["title"])}</a></li>')
        A('</ul></div>')
    A('</div>')

    # ---- graph ------------------------------------------------------------
    A('<h2>By connection</h2>')
    A('<p class="h2sub">Which subjects keep turning up together.</p>')
    A('<p>Each dot is a subject that appears across several articles; its size is the number '
      'of articles. A line means two subjects share articles, and the heavier the line the '
      'more they share. The clusters are not designed &mdash; they fall out of what has '
      'actually been written.</p>')
    A('<div class="exhibit">')
    A('<p class="exno">Figure</p>')
    A('<p class="extitle">Subject co-occurrence across the archive</p>')
    A('<p class="exsub">Subjects appearing in at least five articles. Lines drawn where two '
      'subjects share two or more articles.</p>')
    A(svg_graph(posts))
    A('<p class="exsrc">Built from the headings and body text of every archived post by '
      '<code>tools/index_graph.py</code>. Headings are weighted four times body text, and each '
      'subject counts once per article rather than once per mention &mdash; several posts '
      'contain long tables whose repeated cell text would otherwise dominate any count. '
      'Layout is fixed and deterministic, so a change in the diagram means a change in the '
      'writing, not a reshuffle.</p>')
    A('</div>')

    # ---- full list with related -------------------------------------------
    A('<h2>All articles</h2>')
    A('<p class="h2sub">Newest first, with the closest related pieces.</p>')
    A('<div class="allposts">')
    for slug, p in sorted(posts.items(), key=lambda kv: kv[1]["published"], reverse=True):
        A('<div class="pitem">')
        A(f'<p class="ptitle"><a href="{E(p["url"])}">{E(p["title"])}</a></p>')
        bits = []
        if p["published"]:
            bits.append(E(p["published"]))
        if p["countries"]:
            bits.append(E(", ".join(p["countries"][:3])))
        if p["states"]:
            bits.append(E(", ".join(p["states"][:3])))
        A(f'<p class="pmeta">{" &middot; ".join(bits)}</p>')
        rel = [r for r in p["related"] if r["slug"] in posts][:3]
        if rel:
            links = " &middot; ".join(
                f'<a href="{E(posts[r["slug"]]["url"])}">{E(posts[r["slug"]]["title"][:58])}</a>'
                for r in rel)
            A(f'<p class="prel"><span>Related</span> {links}</p>')
        A('</div>')
    A('</div>')

    body = "\n".join(o)
    head = Path(args.shell_head).read_text(encoding="utf-8") if args.shell_head else ""
    tail = Path(args.shell_tail).read_text(encoding="utf-8") if args.shell_tail else ""
    extra = """<style>/*gs-index-v1*/
.artx .chips{display:flex;flex-wrap:wrap;gap:.5rem;margin:1rem 0 2rem}
.artx .chip{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
 font-size:.82rem;font-weight:600;color:#0B1F2D;background:#F4F7FB;padding:.5rem .9rem;
 border-radius:2px;text-decoration:none;border:1px solid #e2e6ee}
.artx .chip:hover{background:#e6ecf5}
.artx .geo{display:grid;gap:1.4rem 2rem;grid-template-columns:repeat(auto-fit,minmax(17rem,1fr));margin:1.2rem 0 2rem}
.artx .geoblock ul{margin:.35rem 0 0;padding-left:1.05rem}
.artx .geoblock li{font-size:.9rem;line-height:1.45;margin-bottom:.28rem;max-width:none}
.artx .geoh{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
 font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#0a4c6a;
 margin:0;border-bottom:1px solid #e2e2e2;padding-bottom:.3rem}
.artx .geoh span{color:#8a8a8a;font-weight:600}
.artx .serial{border-left:3px solid #8a4b08;padding:.2rem 0 .2rem 1.1rem;margin:1.1rem 0 2rem}
.artx .allposts{margin:1.2rem 0 0}
.artx .pitem{padding:.85rem 0;border-top:1px solid #ececec}
.artx .ptitle{margin:0;font-size:1.02rem;line-height:1.35;max-width:46rem}
.artx .pmeta{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
 font-size:.74rem;color:#7a7a7a;margin:.2rem 0 0}
.artx .prel{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
 font-size:.78rem;color:#595959;margin:.3rem 0 0;max-width:46rem}
.artx .prel span{font-weight:700;text-transform:uppercase;letter-spacing:.09em;font-size:.66rem;
 color:#8a4b08;margin-right:.35rem}
</style>
"""
    Path(args.out).write_text(head + extra + body + tail, encoding="utf-8")
    print(f"wrote {args.out} ({len(head)+len(extra)+len(body)+len(tail):,} bytes, {len(posts)} posts)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
