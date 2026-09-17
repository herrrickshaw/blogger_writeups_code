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
import glob
import html
import itertools
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_labels_by_slug():
    """slug -> topic labels, from this archive's local post metadata. The
    entity graph (index_graph.py's output, what `posts` is built from in
    main()) doesn't carry Blogger labels at all -- the topic accordion above
    gets its labels live from Blogger's own feeds at view time instead. The
    flat "All articles" list is server-rendered, though, so it needs labels
    available at build time; meta/*.json already has them (same source
    build_md_summary.py uses)."""
    out = {}
    for f in glob.glob(str(ROOT / "meta" / "*.json")):
        try:
            m = json.loads(Path(f).read_text(encoding="utf-8"))
        except Exception:
            continue
        if m.get("slug"):
            out[m["slug"]] = m.get("labels") or []
    return out

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
    ("Environment & Clearances", "Environment%20%26%20Clearances"),
    ("Macroeconomics & Monetary Policy", "Macroeconomics%20%26%20Monetary%20Policy"),
    ("AI Tracker", "AI%20Tracker"),
    ("Healthcare", "Healthcare"),
    ("Ethanol & Biofuels", "Ethanol%20%26%20Biofuels"),
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


ACCORDION_JS = "<script>//<![CDATA[\n// Populates each topic from Blogger's own label feed at view time, so this\n// list can never fall behind the blog the way the hand-kept accordion did\n// (it was 18 articles stale when retired). JSONP rather than fetch() so the\n// same block works on the blog, from a saved file, or hosted anywhere else --\n// Blogger's feeds predate CORS but have always supported callback=.\n(function(){\n  var BASE='https://masaladeutsch.blogspot.com', n=0;\n  window.gsAcc = window.gsAcc || {};\n  function jsonp(url, cb){\n    var name='cb'+(n++); window.gsAcc[name]=cb;\n    var s=document.createElement('script');\n    s.src=url+'&callback=gsAcc.'+name;\n    s.onerror=function(){ cb(null); };\n    document.head.appendChild(s);\n  }\n  function feed(lbl, extra, cb){\n    jsonp(BASE+'/feeds/posts/summary/-/'+encodeURIComponent(lbl)\n      +'?alt=json-in-script'+extra, cb);\n  }\n  function fill(d){\n    var ul=d.querySelector('ul'); if(ul.getAttribute('data-done')) return;\n    ul.setAttribute('data-done','1');\n    feed(d.getAttribute('data-label'),'&orderby=published&max-results=150',function(res){\n      if(!res){ ul.innerHTML='<li>Could not load - open the topic page instead.</li>'; return; }\n      var es=res.feed.entry||[]; ul.innerHTML='';\n      for(var i=0;i<es.length;i++){\n        var e=es[i], href='';\n        for(var j=0;j<(e.link||[]).length;j++)\n          if(e.link[j].rel==='alternate') href=e.link[j].href;\n        var li=document.createElement('li'), a=document.createElement('a');\n        a.href=href; a.textContent=e.title.$t; li.appendChild(a);\n        var t=document.createElement('span'); t.className='gs-acc-d';\n        t.textContent=' · '+(e.published.$t||'').slice(0,10);\n        li.appendChild(t); ul.appendChild(li);\n      }\n      if(!es.length) ul.innerHTML='<li>No posts carry this label yet.</li>';\n    });\n  }\n  var ds=document.querySelectorAll('details.gs-acc');\n  for(var k=0;k<ds.length;k++)(function(d){\n    feed(d.getAttribute('data-label'),'&max-results=0',function(res){\n      if(res) d.querySelector('.gs-acc-n').textContent =\n        res.feed.openSearch$totalResults.$t;\n    });\n    d.addEventListener('toggle',function(){ if(d.open) fill(d); });\n  })(ds[k]);\n})();\n//]]></script>"

ACCORDION_CSS = "<style>/*gs-acc-v1*/\n.gs-accwrap{margin:1rem 0 2rem}\n.gs-acc{border-top:1px solid #e2e2e2}\n.gs-acc:last-of-type{border-bottom:1px solid #e2e2e2}\n.gs-acc summary{cursor:pointer;padding:.85rem .2rem;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-weight:700;font-size:1rem;color:#0B1F2D;list-style:none;display:flex;align-items:baseline;gap:.55rem}\n.gs-acc summary::-webkit-details-marker{display:none}\n.gs-acc summary::after{content:'+';margin-left:auto;color:#2251FF;font-weight:600}\n.gs-acc[open] summary::after{content:'\\2212'}\n.gs-acc-n{font-weight:600;font-size:.78rem;color:#8a8a8a}\n.gs-acc-hub{font-size:.72rem;font-weight:600;color:#2251FF;text-decoration:none}\n.gs-acc ul{margin:.2rem 0 1rem;padding-left:1.2rem}\n.gs-acc li{font-size:.92rem;line-height:1.5;margin-bottom:.3rem}\n.gs-acc-d{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:.72rem;color:#8a8a8a;white-space:nowrap}\n</style>"


PITCH_CSS = "<style>/*gs-pitch-v1*/\n.gs-pitch{padding:0 0 1.2rem;border-bottom:1px solid #e2e2e2;margin:0 0 1.6rem}\n.gs-pitch p{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:.95rem;color:#595959;line-height:1.55;max-width:42rem;margin:0}\n.gs-theme-lbl{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#595959;margin:0 0 .7rem}\n.gs-theme-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:1rem;margin:0 0 2rem}\n.gs-tcard{display:block;background:#F4F7FB;border-radius:4px;padding:.9rem 1rem 1rem;text-decoration:none;color:inherit;border:1px solid transparent;transition:border-color .15s}\n.gs-tcard:hover{border-color:#0a4c6a}\n.gs-tcard h3{font-family:Georgia,'Times New Roman',serif;font-weight:400;font-size:1rem;color:#0B1F2D;margin:0 0 .55rem;line-height:1.3}\n.gs-tcard ul{list-style:none;margin:0;padding:0}\n.gs-tcard li{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:.78rem;color:#595959;line-height:1.5;padding:.15rem 0;border-top:1px solid #e2e2e2}\n.gs-tcard li:first-child{border-top:none}\n.gs-tcard .more{display:block;margin-top:.5rem;font-size:.72rem;font-weight:600;color:#2251FF}\n</style>"

PITCH_JS = "<script>//<![CDATA[\n// Same JSONP label-feed pattern as the topic accordion below: each theme\n// card pulls its own 2 latest live headlines at view time, so this section\n// can never go stale the way a hand-kept summary would.\n(function(){\n  var BASE='https://masaladeutsch.blogspot.com', n=0;\n  window.gsPitchCb = window.gsPitchCb || {};\n  function jsonp(url, cb){\n    var name='p'+(n++); window.gsPitchCb[name]=cb;\n    var s=document.createElement('script');\n    s.src=url+'&callback=gsPitchCb.'+name;\n    s.onerror=function(){ cb(null); };\n    document.head.appendChild(s);\n  }\n  var cards=document.querySelectorAll('.gs-tcard[data-label]');\n  for(var i=0;i<cards.length;i++)(function(card){\n    var label=card.getAttribute('data-label'), ul=card.querySelector('ul');\n    jsonp(BASE+'/feeds/posts/summary/-/'+encodeURIComponent(label)+'?alt=json-in-script&orderby=published&max-results=2',function(res){\n      var es=res&&res.feed.entry;\n      if(!es||!es.length){ ul.innerHTML='<li>New articles coming soon.</li>'; return; }\n      ul.innerHTML='';\n      for(var j=0;j<es.length;j++){ var li=document.createElement('li'); li.textContent=es[j].title.$t; ul.appendChild(li); }\n    });\n  })(cards[i]);\n})();\n//]]></script>"

PITCH_THEMES = [
    "Energy & Fuels", "Trade & Tariffs", "Industrial Policy",
    "Agriculture & Fertilisers", "Markets & Finance", "Climate & Carbon",
]


def emit_pitch(A):
    """Elevator-pitch + theme cards, in-page (not a Blogger Layout gadget --
    those live outside the Posts API and can only be hand-edited through the
    Blogger UI forever after). Lives inside this index post instead, so it
    ships through the same build-and-publish pipeline as everything else and
    stays trivially editable.
    """
    A(PITCH_CSS)
    A('<div class="gs-pitch"><p>Six years of trade, energy, industrial-policy and fertiliser data, '
      'read from primary sources (PIB, Parliament replies, RBI, government dashboards) rather than '
      'press releases. New this month: plain-language explainers on personal finance, alongside the '
      'usual HSN-coded deep dives.</p></div>')
    A('<p class="gs-theme-lbl">Browse by theme</p>')
    A('<div class="gs-theme-grid">')
    for name in PITCH_THEMES:
        slugpart = next((s for n, s in LABEL_HUBS if n == name), name.replace(" & ", " %26 ").replace(" ", "%20"))
        A(f'<a class="gs-tcard" data-label="{E(name)}" '
          f'href="https://masaladeutsch.blogspot.com/search/label/{slugpart}">'
          f'<h3>{E(name)}</h3><ul><li>Loading&#8230;</li></ul>'
          f'<span class="more">All {E(name)} articles &#8594;</span></a>')
    A('</div>')
    A(PITCH_JS)


def emit_accordion(A, hubs):
    """Self-updating topic accordion, driven by Blogger's label feeds.

    Each <details> starts empty and fills on first open; counts load
    immediately. Without JavaScript the summary still carries a working link
    to the label hub, so the worst case is navigation, never a dead section.
    """
    A(ACCORDION_CSS)
    A('<div class="gs-accwrap">')
    for name, slugpart in sorted(hubs, key=lambda t: t[0].lower()):
        A(f'<details class="gs-acc" data-label="{E(name)}">'
          f'<summary>{E(name)} <span class="gs-acc-n"></span>'
          f'<a class="gs-acc-hub" '
          f'href="https://masaladeutsch.blogspot.com/search/label/{slugpart}">'
          f'open topic page &#8594;</a></summary>'
          '<ul><li>Loading&#8230;</li></ul></details>')
    A('</div>')
    A(ACCORDION_JS)


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
    labels_by_slug = load_labels_by_slug()

    by_country = collections.defaultdict(list)
    by_state = collections.defaultdict(list)
    for slug, p in posts.items():
        for c in p["countries"]:
            by_country[c].append(slug)
        for s in p["states"]:
            by_state[s].append(slug)

    o = []
    A = o.append
    # Self-referencing topnav link every other post carries (consistency-check's
    # index-link rule) and the house gb-table border style (table-units-in-header
    # and the site-wide table-borders standard) -- both were being hand-patched
    # into out/post-index.html after every rebuild until 2026-09-17. Baked in
    # here so a plain rebuild no longer regresses either check.
    A('<div class="topnav-index-link" style="font-size:.82em;margin:6px 0 14px">'
      '<a href="https://masaladeutsch.blogspot.com/2026/08/article-index-start-here.html" '
      'style="color:#0b5394;text-decoration:none">&#8592; All Articles (Index)</a></div>')
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

    emit_pitch(A)

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
    A('<style>/*gs-tw-table-v1*/\n'
      '.gb-table{border-collapse:collapse;width:100%;font-size:.85em;font-family:-apple-system,\'Segoe UI\',sans-serif;margin:1.25rem 0}\n'
      '.gb-table thead th{background:#212529;color:#fff;padding:.5rem .75rem;text-align:left;white-space:nowrap}\n'
      '.gb-table td{padding:.5rem .75rem;border-bottom:1px solid #dee2e6;color:#212529;word-wrap:break-word}\n'
      '.gb-table tbody tr:nth-child(even){background:#f8f9fa}\n'
      '.gb-tblwrap{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:0 0 1em}\n'
      '</style>')
    A('<div class="tw gb-tblwrap"><table class="gb-table">')
    A('<thead><tr><th>Month</th><th>Articles</th><th>Running total</th></tr></thead><tbody>')
    run = 0
    for m in sorted(months):
        run += months[m]
        A(f'<tr><td>{_pretty_month(m)}</td><td>{months[m]}</td><td>{run}</td></tr>')
    A('</tbody></table></div>')
    A('<p class="exsrc">Counted from each post&rsquo;s Blogger publication date as recorded in the '
      'archive manifest. A number of earlier drafts and duplicate variants -- accidental multi-publishes, '
      'superseded draft versions -- were withdrawn from Blogger over time and are not listed; they have '
      'no live URL to link to.</p>')

    # ---- topics -----------------------------------------------------------
    A('<h2>By topic</h2>')
    A('<p class="h2sub">Live hub pages. Each updates itself as new pieces are labelled.</p>')
    # The accordion replaces the chip row. It reads Blogger's label feeds at
    # view time, so its counts and its post lists are always current -- the
    # failure mode of every hand-kept list this page has had.
    emit_accordion(A, LABEL_HUBS)

    # ---- AI tracker ---------------------------------------------------------
    # A standing serial, not a one-off analysis. It sits in its own section
    # because a reader looking for "the latest edition" should not have to find
    # it among 96 dated articles, and because each new edition replaces the last
    # at the same URL rather than adding a row to the list.
    trk = next((p for s_, p in posts.items() if "ai-high-demand-launch-tracker" in s_), None)
    if trk:
        A('<h2>AI Tracker</h2>')
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
          f'search/label/AI%20Tracker">All AI Tracker editions</a></p>')
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
    # Flat date -> topic -> title rows (see chrono_list_mockup.html, inspired
    # by jungle.vc/resources), not cards: the scan is date and headline first,
    # everything else -- geography, related pieces -- demoted to a quieter
    # line underneath rather than competing on the same visual level.
    A('<h2>All articles</h2>')
    A('<p class="h2sub">Newest first.</p>')
    A('<div class="chrono">')
    for slug, p in sorted(posts.items(), key=lambda kv: kv[1]["published"], reverse=True):
        labels = labels_by_slug.get(slug) or []
        tag, tag_cls = (labels[0], "ctag") if labels else ("Unlabelled", "ctag none")
        date_str = _pretty_date(p["published"]) if p["published"] else "?"
        A('<div class="crow">')
        A(f'<span class="cdate">{E(date_str)}</span>')
        A(f'<span class="{tag_cls}">{E(tag)}</span>')
        A(f'<a class="ctitle" href="{E(p["url"])}">{E(p["title"])}</a>')
        geo = (p["countries"][:2] + p["states"][:2])
        rel = [r for r in p["related"] if r["slug"] in posts][:3]
        if geo or rel:
            A('<span class="csub">')
            if geo:
                A(f'<span class="cgeo">{E(", ".join(geo))}</span>')
            if rel:
                links = " &middot; ".join(
                    f'<a href="{E(posts[r["slug"]]["url"])}">{E(posts[r["slug"]]["title"][:52])}</a>'
                    for r in rel)
                sep = ' <span class="cdot">&middot;</span> ' if geo else ''
                A(f'{sep}<span class="crel-lbl">Related</span> {links}')
            A('</span>')
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
.artx .chrono{border-top:1px solid #e2e2e2;margin:1.2rem 0 0}
.artx .crow{display:grid;grid-template-columns:6.4rem 11rem 1fr;align-items:baseline;
 column-gap:1.1rem;row-gap:.2rem;padding:.85rem .2rem;border-bottom:1px solid #e2e2e2;
 transition:background-color .12s ease}
.artx .crow:hover{background:#F4F7FB}
.artx .crow:hover .ctitle{color:#2251FF}
.artx .cdate{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
 font-size:.74rem;color:#595959;font-variant-numeric:tabular-nums;white-space:nowrap;padding-top:.15rem}
.artx .ctag{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
 font-size:.68rem;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#2251FF;
 padding-top:.15rem}
.artx .ctag.none{color:#8a8a8a;font-weight:600;letter-spacing:.03em;text-transform:none}
.artx .ctitle{grid-column:3;font-family:Georgia,'Times New Roman',serif;font-size:1.02rem;
 line-height:1.4;color:#0B1F2D;text-decoration:none;transition:color .12s ease}
.artx .csub{grid-column:3;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,
 sans-serif;font-size:.76rem;color:#8a8a8a;line-height:1.5}
.artx .csub a{color:#8a8a8a}
.artx .csub .crel-lbl{font-weight:700;text-transform:uppercase;letter-spacing:.08em;font-size:.64rem;
 color:#8a4b08}
.artx .csub .cdot{margin:0 .1rem}
@media (max-width:640px){
 .artx .crow{grid-template-columns:1fr;row-gap:.25rem;padding:1rem .2rem}
 .artx .ctitle,.artx .csub{grid-column:1}
}
</style>
"""
    Path(args.out).write_text(head + extra + body + tail, encoding="utf-8")
    print(f"wrote {args.out} ({len(head)+len(extra)+len(body)+len(tail):,} bytes, {len(posts)} posts)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
