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
import re
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


def _weekday_date(iso):
    """'2026-10-25' -> 'Sunday 25 October 2026'."""
    import datetime as _dt
    d = _dt.date(int(iso[:4]), int(iso[5:7]), int(iso[8:10]))
    return f"{d.strftime('%A')} {d.day} {_MON[d.month - 1]} {d.year}"


def _pretty_month(ym):
    y, m = ym[:4], int(ym[5:7])
    return f"{_MON[m-1]} {y}"


ACCORDION_JS = "<script>//<![CDATA[\n// Populates each topic from Blogger's own label feed at view time, so this\n// list can never fall behind the blog the way the hand-kept accordion did\n// (it was 18 articles stale when retired). JSONP rather than fetch() so the\n// same block works on the blog, from a saved file, or hosted anywhere else --\n// Blogger's feeds predate CORS but have always supported callback=.\n(function(){\n  var BASE='https://blog.vertistratsolution.com', n=0;\n  window.gsAcc = window.gsAcc || {};\n  function jsonp(url, cb){\n    var name='cb'+(n++); window.gsAcc[name]=cb;\n    var s=document.createElement('script');\n    s.src=url+'&callback=gsAcc.'+name;\n    s.onerror=function(){ cb(null); };\n    document.head.appendChild(s);\n  }\n  function feed(lbl, extra, cb){\n    jsonp(BASE+'/feeds/posts/summary/-/'+encodeURIComponent(lbl)\n      +'?alt=json-in-script'+extra, cb);\n  }\n  function fill(d){\n    var ul=d.querySelector('ul'); if(ul.getAttribute('data-done')) return; ul.setAttribute('aria-busy','true');\n    ul.setAttribute('data-done','1');\n    feed(d.getAttribute('data-label'),'&orderby=published&max-results=150',function(res){\n      if(!res){ ul.innerHTML='<li>Could not load - open the topic page instead.</li>'; return; }\n      var es=res.feed.entry||[]; ul.innerHTML='';\n      for(var i=0;i<es.length;i++){\n        var e=es[i], href='';\n        for(var j=0;j<(e.link||[]).length;j++)\n          if(e.link[j].rel==='alternate') href=e.link[j].href;\n        var li=document.createElement('li'), a=document.createElement('a');\n        a.href=href; a.textContent=e.title.$t; li.appendChild(a);\n        var t=document.createElement('span'); t.className='gs-acc-d';\n        t.textContent=' · '+(e.published.$t||'').slice(0,10);\n        li.appendChild(t); ul.appendChild(li);\n      }\n      if(!es.length) ul.innerHTML='<li>No posts carry this label yet.</li>';\n      ul.removeAttribute('aria-busy');\n    });\n  }\n  var ds=document.querySelectorAll('details.gs-acc');\n  for(var k=0;k<ds.length;k++)(function(d){\n    feed(d.getAttribute('data-label'),'&max-results=0',function(res){\n      if(res) d.querySelector('.gs-acc-n').textContent =\n        res.feed.openSearch$totalResults.$t + ' articles';\n    });\n    d.addEventListener('toggle',function(){ if(d.open) fill(d); });\n  })(ds[k]);\n})();\n//]]></script>"

ACCORDION_CSS = "<style>/*gs-acc-v1*/\n.gs-accwrap{margin:1rem 0 2rem}\n.gs-acc{border-top:1px solid #e2e2e2}\n.gs-acc:last-of-type{border-bottom:1px solid #e2e2e2}\n.gs-acc summary{cursor:pointer;min-height:44px;box-sizing:border-box;padding:.85rem .2rem;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-weight:700;font-size:1rem;color:#0B1F2D;list-style:none;display:flex;align-items:baseline;gap:.55rem}\n.gs-acc summary::-webkit-details-marker{display:none}\n.gs-acc summary::after{content:'+';margin-left:auto;color:#2251FF;font-weight:600}\n.gs-acc[open] summary::after{content:'\\2212'}\n.gs-acc-n{font-weight:600;font-size:.85rem;color:#595959}\n.gs-acc-hubp{margin:.1rem 0 .5rem;max-width:none}\n.gs-acc-hub{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:.88rem;font-weight:600;color:#12408f;text-decoration:underline;text-underline-offset:2px}\n.gs-acc ul{margin:.2rem 0 1rem;padding-left:1.2rem}\n.gs-acc li{font-size:.92rem;line-height:1.5;margin-bottom:.3rem}\n.gs-acc-d{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:.82rem;color:#595959;white-space:nowrap}\n</style>"


PITCH_CSS = "<style>/*gs-pitch-v1*/\n.gs-pitch{padding:0 0 1.2rem;border-bottom:1px solid #e2e2e2;margin:0 0 1.6rem}\n.gs-pitch p{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:.95rem;color:#595959;line-height:1.55;max-width:42rem;margin:0}\n.gs-theme-lbl{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:.78rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#595959;margin:0 0 .7rem}\n.gs-theme-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:1rem;margin:0 0 2rem}\n.gs-tcard{display:block;background:#F4F7FB;border-radius:4px;padding:.9rem 1rem 1rem;text-decoration:none;color:inherit;border:1px solid transparent;transition:border-color .15s}\n.gs-tcard:hover{border-color:#0a4c6a}\n.gs-tcard h3{font-family:Georgia,'Times New Roman',serif;font-weight:400;font-size:1rem;color:#0B1F2D;margin:0 0 .55rem;line-height:1.3}\n.gs-tcard ul{list-style:none;margin:0;padding:0}\n.gs-tcard li{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:.86rem;color:#595959;line-height:1.5;padding:.15rem 0;border-top:1px solid #e2e2e2}\n.gs-tcard li:first-child{border-top:none}\n.gs-tcard{position:relative}\n.gs-tcard h3 a{color:#0B1F2D;text-decoration:none}\n.gs-tcard h3 a::after{content:'';position:absolute;inset:0}\n.gs-tcard li a{position:relative;z-index:1;color:#12408f;text-decoration:underline;text-underline-offset:2px}\n.gs-tcard:focus-within{border-color:#8a4b08;outline:3px solid #8a4b08;outline-offset:2px}\n.gs-tcard .more{display:block;margin-top:.5rem;font-size:.82rem;font-weight:600;color:#12408f}\n</style>"

PITCH_JS = "<script>//<![CDATA[\n// Same JSONP label-feed pattern as the topic accordion below: each theme\n// card pulls its own 2 latest live headlines at view time, so this section\n// can never go stale the way a hand-kept summary would.\n(function(){\n  var BASE='https://blog.vertistratsolution.com', n=0;\n  window.gsPitchCb = window.gsPitchCb || {};\n  function jsonp(url, cb){\n    var name='p'+(n++); window.gsPitchCb[name]=cb;\n    var s=document.createElement('script');\n    s.src=url+'&callback=gsPitchCb.'+name;\n    s.onerror=function(){ cb(null); };\n    document.head.appendChild(s);\n  }\n  var cards=document.querySelectorAll('.gs-tcard[data-label]');\n  for(var i=0;i<cards.length;i++)(function(card){\n    var label=card.getAttribute('data-label'), ul=card.querySelector('ul');\n    jsonp(BASE+'/feeds/posts/summary/-/'+encodeURIComponent(label)+'?alt=json-in-script&orderby=published&max-results=2',function(res){\n      var es=res&&res.feed.entry;\n      if(!es||!es.length){ ul.innerHTML='<li>New articles coming soon.</li>'; return; }\n      ul.innerHTML='';\n      for(var j=0;j<es.length;j++){ var li=document.createElement('li'), a=document.createElement('a'), href='';\n        for(var q=0;q<(es[j].link||[]).length;q++) if(es[j].link[q].rel==='alternate') href=es[j].link[q].href;\n        a.href=href; a.textContent=es[j].title.$t; li.appendChild(a); ul.appendChild(li); }\n    });\n  })(cards[i]);\n})();\n//]]></script>"

PITCH_THEMES = [
    "Energy & Fuels", "Trade & Tariffs", "Industrial Policy",
    "Agriculture & Fertilisers", "Markets & Finance", "Climate & Carbon",
]

# gs-chrono-filter-v1 (2026-09-19): month/date/topic filters over the "All
# articles" list. Options are built in JS from the rows' own data-ym/
# data-date/data-topic attributes rather than hand-listed here, so the
# filter never goes stale as posts are added -- the same self-maintaining
# pattern as the topic accordion above, just without the network round trip
# (this data is already on the page, unlike live label counts).
FILTER_BAR = (
    '<div class="gs-filter-bar" role="search" aria-label="Search and filter articles">'
    '<div class="gs-f-field gs-f-q"><label for="gs-f-q">Search titles and article text</label>'
    '<input type="search" id="gs-f-q" autocomplete="off" placeholder="e.g. steel, FDI, ethanol"></div>'
    '<div class="gs-f-field"><label for="gs-f-month">Month</label><select id="gs-f-month"><option value="">All months</option></select></div>'
    '<div class="gs-f-field"><label for="gs-f-date">Date</label><select id="gs-f-date"><option value="">All dates</option></select></div>'
    '<div class="gs-f-field"><label for="gs-f-topic">Topic</label><select id="gs-f-topic"><option value="">All topics</option></select></div>'
    '<button type="button" class="gs-filter-reset" id="gs-f-reset">Clear search and filters</button>'
    '<p class="gs-filter-count" id="gs-f-count" role="status" aria-live="polite"></p>'
    '<p class="gs-fulltext" id="gs-f-full" hidden>Showing matches from titles, headings and each article&#8217;s most distinctive terms. '
    '<a id="gs-f-full-a" href="https://blog.vertistratsolution.com/search" rel="noopener">Search every word of every article on Blogger</a>.</p>'
    '</div>'
)

# gs-content-search-v1: per-article keyword index. A literal all-words index is
# about 800 KB for 367 posts (more than the whole page), so the on-page search
# covers headings, captions and the highest TF-IDF terms of each post, and the
# fulltext link above hands anything else to Blogger's own search.
_STOP = set("""this that with from have been were will would could should their there which these those
than then them they what when where while about after before between because into over under also such
only more most some many much very each other both same does done doing being india indian indias per cent
crore lakh billion million tonnes tonne state states year years fiscal data table figure source sources
article articles posts post blog read note notes click here share tools disclosure disclaimer assistance
researched written drawing publicly available government cited above several reached search engine summary
rather directly index start masaladeutsch updated revised version changed""".split())
_TOK = re.compile(r"[a-z][a-z0-9\-]{3,}|\d{6,8}")
_HEAD = re.compile(r"<h[1-3][^>]*>(.*?)</h[1-3]>|<caption[^>]*>(.*?)</caption>", re.S | re.I)


def _post_text(slug):
    f = ROOT / "posts" / f"{slug}.html"
    if not f.exists():
        return "", ""
    raw = f.read_text(encoding="utf-8", errors="replace")
    raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
    heads = " ".join(a or b for a, b in _HEAD.findall(raw))
    clean = lambda t: html.unescape(re.sub(r"<[^>]+>", " ", t)).lower()
    return clean(heads), clean(raw)


def build_keywords(slugs, top=40):
    """slug -> space-separated lowercase terms: every word in the post's headings
    and captions plus its `top` highest TF-IDF body terms (6-8 digit codes such
    as HS-8 lines are kept)."""
    texts = {s: _post_text(s) for s in slugs}
    toks = {s: [t for t in _TOK.findall(b) if t not in _STOP] for s, (_, b) in texts.items()}
    df = collections.Counter(t for ts in toks.values() for t in set(ts))
    n = max(len(toks), 1)
    out = {}
    for s, ts in toks.items():
        tf = collections.Counter(ts)
        score = {t: c * math.log(n / df[t]) for t, c in tf.items() if df[t] < 0.5 * n}
        best = [t for t, _ in sorted(score.items(), key=lambda kv: (-kv[1], kv[0]))[:top]]
        hw = [t for t in _TOK.findall(texts[s][0]) if t not in _STOP]
        codes = list(dict.fromkeys(t for t in ts if t.isdigit()))[:25]
        out[s] = " ".join(dict.fromkeys(hw + best + codes))
    return out

FILTER_JS = """<script>//<![CDATA[
(function(){
  var chrono = document.querySelector('.chrono'); if(!chrono) return;
  var rows = Array.prototype.slice.call(chrono.querySelectorAll('.crow'));
  var months = Array.prototype.slice.call(chrono.querySelectorAll('.cmonth'));
  var days = Array.prototype.slice.call(chrono.querySelectorAll('.cdayg'));
  var MONTHS=['January','February','March','April','May','June','July','August',
    'September','October','November','December'];
  function uniqSorted(key, cmp){
    var seen={}, out=[];
    rows.forEach(function(r){ var v=r.getAttribute(key);
      if(v && !seen[v]){ seen[v]=1; out.push(v); } });
    out.sort(cmp); return out;
  }
  function countBy(key,val){ return rows.filter(function(r){return r.getAttribute(key)===val;}).length; }
  function fill(sel, values, labelFn){
    values.forEach(function(v){ var o=document.createElement('option');
      o.value=v; o.textContent=labelFn(v); sel.appendChild(o); });
  }
  var yms = uniqSorted('data-ym', function(a,b){return b.localeCompare(a);});
  var dates = uniqSorted('data-date', function(a,b){return b.localeCompare(a);});
  var topics = uniqSorted('data-topic', function(a,b){return a.localeCompare(b);});
  var selM=document.getElementById('gs-f-month'), selD=document.getElementById('gs-f-date'),
      selT=document.getElementById('gs-f-topic'), q=document.getElementById('gs-f-q'),
      countEl=document.getElementById('gs-f-count'), emptyEl=document.getElementById('gs-f-empty'),
      fullEl=document.getElementById('gs-f-full'), fullA=document.getElementById('gs-f-full-a');
  fill(selM, yms, function(ym){ var y=ym.slice(0,4), m=+ym.slice(5,7)-1;
    return MONTHS[m]+' '+y+' ('+countBy('data-ym',ym)+')'; });
  fill(selD, dates, function(d){ var y=d.slice(0,4), m=+d.slice(5,7)-1, day=+d.slice(8,10);
    return day+' '+MONTHS[m]+' '+y+' ('+countBy('data-date',d)+')'; });
  fill(selT, topics, function(t){ return t+' ('+countBy('data-topic',t)+')'; });
  // gs-content-search-v1: the page's own keyword index answers instantly; Blogger's
  // feed `q=` search (full text, same origin) adds matches on any other word.
  var srv={q:'',slugs:null}, srvTimer=null, srvCtl=null;
  function pathOf(u){ try{ return new URL(u, location.href).pathname; }catch(e){ return u; } }
  var rowByPath={}; rows.forEach(function(r){ var a=r.querySelector('a.ctitle'); if(a) rowByPath[pathOf(a.href)]=r; });
  function lookup(){
    var qs=(q.value||'').trim();
    if(srvCtl){ srvCtl.abort(); srvCtl=null; }
    if(qs.length<3 || !window.fetch || !window.AbortController || location.protocol==='file:'){ srv={q:qs,slugs:null}; return; }
    srvCtl=new AbortController();
    fetch('/feeds/posts/summary?alt=json&max-results=500&q='+encodeURIComponent(qs), {signal:srvCtl.signal})
      .then(function(r){ if(!r.ok) throw new Error(r.status); return r.json(); })
      .then(function(j){
        var set={}; ((j.feed&&j.feed.entry)||[]).forEach(function(e){
          (e.link||[]).forEach(function(l){ if(l.rel==='alternate') set[pathOf(l.href)]=1; }); });
        srv={q:qs,slugs:set}; apply();
      })
      .catch(function(){ srv={q:qs,slugs:null}; });
  }
  function apply(){
    var m=selM.value, d=selD.value, t=selT.value, terms=(q.value||'').toLowerCase().split(/\\s+/).filter(Boolean), shown=0;
    rows.forEach(function(r){
      var hay=r._hay||(r._hay=(r.textContent||'').toLowerCase());
      var kw=r._kw||(r._kw=(r.getAttribute('data-kw')||'').toLowerCase());
      var inTitle=terms.every(function(w){ return hay.indexOf(w)!==-1; });
      var viaSrv=false;
      if(srv.slugs && srv.q===(q.value||'').trim()){
        var a_=r.querySelector('a.ctitle'); viaSrv=!!(a_ && srv.slugs[pathOf(a_.href)]);
      }
      var inText=inTitle || viaSrv || terms.every(function(w){ return hay.indexOf(w)!==-1 || kw.indexOf(w)!==-1; });
      var ok=(!m || r.getAttribute('data-ym')===m) && (!d || r.getAttribute('data-date')===d)
           && (!t || r.getAttribute('data-topic')===t) && inText;
      r.style.display = ok ? '' : 'none'; if(ok) shown++;
      r.classList.toggle('via-text', !!(ok && terms.length && !inTitle));
    });
    days.forEach(function(g){
      var any=Array.prototype.some.call(g.querySelectorAll('.crow'), function(r){ return r.style.display!=='none'; });
      g.style.display = any ? '' : 'none';
    });
    months.forEach(function(g){
      var any=Array.prototype.some.call(g.querySelectorAll('.crow'), function(r){ return r.style.display!=='none'; });
      g.style.display = any ? '' : 'none';
    });
    var active = m||d||t||terms.length;
    countEl.textContent = active ? ('Showing '+shown+' of '+rows.length+' articles') : '';
    if(emptyEl) emptyEl.style.display = shown ? 'none' : 'block';
    if(fullEl){
      var qs=(q.value||'').trim();
      fullEl.hidden = !qs || !!(srv.slugs && srv.q===qs);
      if(qs) fullA.href='https://blog.vertistratsolution.com/search?q='+encodeURIComponent(qs);
    }
  }
  [selM,selD,selT].forEach(function(el){ el.addEventListener('change', apply); });
  q.addEventListener('input', function(){ apply(); clearTimeout(srvTimer); srvTimer=setTimeout(lookup, 350); });
  var resetBtn=document.getElementById('gs-f-reset');
  if(resetBtn) resetBtn.addEventListener('click', function(){
    selM.value=''; selD.value=''; selT.value=''; q.value=''; apply(); q.focus();
  });
})();
//]]></script>"""


def emit_pitch(A):
    """Elevator-pitch + theme cards, in-page (not a Blogger Layout gadget --
    those live outside the Posts API and can only be hand-edited through the
    Blogger UI forever after). Lives inside this index post instead, so it
    ships through the same build-and-publish pipeline as everything else and
    stays trivially editable.
    """
    A(PITCH_CSS)
    A('<div class="gs-pitch"><p>Trade, energy, industrial-policy, fertiliser and macro data, '
      'read from primary sources (PIB, Parliament replies, RBI, government dashboards) rather than '
      'press releases. Most pieces end with a section of concrete proposals, labelled as this blog\'s '
      'own and not as anything an agency has adopted.</p></div>')
    A('<h2 class="gs-theme-lbl" id="gs-themes-lbl">Browse by theme</h2>')
    A('<div class="gs-theme-grid" role="group" aria-labelledby="gs-themes-lbl">')
    for name in PITCH_THEMES:
        slugpart = next((s for n, s in LABEL_HUBS if n == name), name.replace(" & ", " %26 ").replace(" ", "%20"))
        A(f'<div class="gs-tcard" data-label="{E(name)}">'
          f'<h3><a href="https://blog.vertistratsolution.com/search/label/{slugpart}">'
          f'{E(name)}<span class="sr-only"> &mdash; all articles on this topic</span></a></h3>'
          f'<ul aria-live="polite"><li>Loading latest headlines&#8230;</li></ul></div>')
    A('</div>')
    A(PITCH_JS)


def emit_accordion(A, hubs):
    """Self-updating topic accordion, driven by Blogger's label feeds.

    Each <details> starts empty and fills on first open; counts load
    immediately. Without JavaScript the summary still carries a working link
    to the label hub, so the worst case is navigation, never a dead section.
    """
    A(ACCORDION_CSS)
    A('<div class="gs-accwrap" role="group" aria-label="Topics, each opening a list of its articles">')
    for name, slugpart in sorted(hubs, key=lambda t: t[0].lower()):
        A(f'<details class="gs-acc" data-label="{E(name)}">'
          f'<summary>{E(name)} <span class="gs-acc-n"></span></summary>'
          f'<p class="gs-acc-hubp"><a class="gs-acc-hub" '
          f'href="https://blog.vertistratsolution.com/search/label/{slugpart}">'
          f'Open the {E(name)} topic page</a></p>'
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
    parts.append('<desc>A ring of the most frequent subjects, sized by the number of articles, with lines '
                 'joining subjects that share articles. The same information is in the table below the figure.</desc>')
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
    # text alternative: every node with its article count and its strongest partners
    rows_ = []
    for e in nodes:
        partners = sorted(((n, (b if a == e else a)) for (a, b), n in co.items() if e in (a, b) and n >= 2), reverse=True)[:3]
        ptxt = "; ".join(f"{E(o)} ({n})" for n, o in partners) or "&ndash;"
        rows_.append(f"<tr><th scope=\"row\">{E(e)}</th><td>{cnt[e]}</td><td>{ptxt}</td></tr>")
    parts.append('<details class="gs-gtable"><summary>Read this figure as a table</summary>'
                 '<div class="tw" role="region" aria-label="Subjects and their strongest connections" tabindex="0"><table>'
                 '<caption class="sr-only">Subjects, the number of articles each appears in, and the subjects it most often appears with</caption>'
                 '<thead><tr><th scope="col">Subject</th><th scope="col">Articles</th><th scope="col">Most often with (shared articles)</th></tr></thead>'
                 '<tbody>' + "".join(rows_) + '</tbody></table></div></details>')
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
    # The archive keeps files for posts later withdrawn from Blogger; list only
    # what the manifest says is live, and where the same title is live twice
    # (an accidental double publish) show the earlier post once.
    mf = ROOT / "meta" / "manifest.json"
    if mf.exists():
        live = {m["slug"] for m in json.loads(mf.read_text(encoding="utf-8"))["posts"].values()}
        posts = {k: v for k, v in posts.items() if k in live}
    seen_title = {}
    for slug, p_ in sorted(posts.items(), key=lambda kv: kv[1]["published"] or ""):
        key = re.sub(r"\s+", " ", p_["title"].strip().lower())
        seen_title.setdefault(key, slug)
    keep = set(seen_title.values())
    posts = {k: v for k, v in posts.items() if k in keep}
    labels_by_slug = load_labels_by_slug()

    by_country = collections.defaultdict(list)
    by_state = collections.defaultdict(list)
    for slug, p in posts.items():
        for c in p["countries"]:
            by_country[c].append(slug)
        for s in p["states"]:
            by_state[s].append(slug)

    keywords = build_keywords(list(posts))
    o = []
    A = o.append
    A('<a class="gs-skip" href="#gs-all">Skip to the article list and search</a>')
    # Self-referencing topnav link every other post carries (consistency-check's
    # index-link rule) and the house gb-table border style (table-units-in-header
    # and the site-wide table-borders standard) -- both were being hand-patched
    # into out/post-index.html after every rebuild until 2026-09-17. Baked in
    # here so a plain rebuild no longer regresses either check.
    A('<div class="topnav-index-link" style="font-size:.82em;margin:6px 0 14px">'
      '<a href="https://blog.vertistratsolution.com/2026/08/article-index-start-here.html" '
      'style="color:#0b5394;text-decoration:none">&#8592; All Articles (Index)</a></div>')
    A('<p class="eyebrow">VertiStrat Solutions &middot; Article index</p>')
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

    has_tracker = any("ai-high-demand-launch-tracker" in s_ for s_ in posts)
    A('<nav class="gs-jump" aria-label="On this page"><p class="gs-jump-lbl">Jump to</p><ul>'
      '<li><a href="#gs-latest">Latest articles</a></li>'
      '<li><a href="#gs-all">Search all articles</a></li>'
      '<li><a href="#gs-topic">By topic</a></li>'
      '<li><a href="#gs-date">By date</a></li>'
      + ('<li><a href="#gs-tracker">AI Tracker</a></li>' if has_tracker else '') +
      '<li><a href="#gs-geo">By geography</a></li>'
      '<li><a href="#gs-graph">By connection</a></li></ul></nav>')

    emit_pitch(A)

    # ---- latest -------------------------------------------------------------
    A('<h2 id="gs-latest">Latest articles</h2>')
    A('<p class="h2sub">The eight most recent pieces.</p>')
    A('<ul class="gs-latest">')
    for slug, p_ in sorted(posts.items(), key=lambda kv: kv[1]["published"], reverse=True)[:8]:
        iso = p_["published"][:10]
        A(f'<li><time datetime="{E(iso)}">{E(_pretty_date(p_["published"]))}</time> '
          f'<a href="{E(p_["url"])}">{E(p_["title"])}</a></li>')
    A('</ul>')

    # ---- by date ----------------------------------------------------------
    A('<h2 id="gs-date">By date</h2>')
    A('<p class="h2sub">Month by month, newest first. Each month links to its articles below, listed day by day.</p>')
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
    A('<div class="tw gb-tblwrap" role="region" aria-label="Articles per month" tabindex="0"><table class="gb-table">')
    A('<caption class="sr-only">Articles published per month, with a running total</caption>')
    # gs-datewise-v1 (2026-10-25): month rows link to that month's block in "All
    # articles", and each month shows how many days had a post and its busiest
    # day, so the table works as a date-wise and month-wise way in, not only a tally.
    days_by_month = collections.defaultdict(collections.Counter)
    for p_ in posts.values():
        if p_["published"]:
            days_by_month[p_["published"][:7]][p_["published"][:10]] += 1
    A('<thead><tr><th scope="col">Month</th><th scope="col">Articles</th><th scope="col">Days with a post</th>'
      '<th scope="col">Busiest day</th><th scope="col">Running total</th></tr></thead><tbody>')
    run = 0
    totals = {}
    for m in sorted(months):
        run += months[m]
        totals[m] = run
    for m in sorted(months, reverse=True):
        dm = days_by_month[m]
        bd, bn = max(dm.items(), key=lambda kv: (kv[1], kv[0]))
        A(f'<tr><th scope="row"><a href="#gs-m-{E(m)}">{_pretty_month(m)}</a></th><td>{months[m]}</td><td>{len(dm)}</td>'
          f'<td><a href="#gs-d-{E(bd)}">{E(_pretty_date(bd))}</a> ({bn})</td><td>{totals[m]}</td></tr>')
    A('</tbody></table></div>')
    A('<p class="exsrc">Counted from each post&rsquo;s Blogger publication date as recorded in the '
      'archive manifest. A number of earlier drafts and duplicate variants -- accidental multi-publishes, '
      'superseded draft versions -- were withdrawn from Blogger over time and are not listed; they have '
      'no live URL to link to.</p>')

    # ---- topics -----------------------------------------------------------
    A('<h2 id="gs-topic">By topic</h2>')
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
        A('<h2 id="gs-tracker">AI Tracker</h2>')
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
        A(f'<p class="prel"><span>Hub</span> <a href="https://blog.vertistratsolution.com/'
          f'search/label/AI%20Tracker">All AI Tracker editions</a></p>')
        A('</div>')

    # ---- geography --------------------------------------------------------
    A('<h2 id="gs-geo">By geography</h2>')
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
    A('<h2 id="gs-graph">By connection</h2>')
    A('<p class="h2sub">Which subjects keep turning up together.</p>')
    A('<p>Each dot is a subject that appears across several articles; its size is the number '
      'of articles. A line means two subjects share articles, and the heavier the line the '
      'more they share. The clusters are not designed &mdash; they fall out of what has '
      'actually been written.</p>')
    A('<div class="exhibit">')
    A('<p class="exno">Figure</p>')
    A('<p class="extitle">Subject co-occurrence across the archive</p>')
    A('<p class="exsub">Subjects appearing in at least five articles. Lines drawn where two '
      'subjects share two or more articles. The diagram is small on a phone; the table under it has the same information.</p>')
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
    #
    # gs-chrono-group-v1 (2026-09-19): the flat list was 300+ rows of a tiny
    # grey date next to every headline -- scannable post by post, but with no
    # way to tell "what came out in a given month" without reading every row.
    # A sticky month/year header, inserted whenever the month changes, gives
    # the list the same date anchors the "By date" table above already has,
    # while leaving each row's own date untouched.
    A('<h2 id="gs-all">All articles</h2>')
    A('<p class="h2sub">Newest first, grouped by month and then by day. Search the titles and article text, or filter by month, day or topic.</p>')
    A(FILTER_BAR)
    A('<div class="chrono">')
    ordered = sorted(posts.items(), key=lambda kv: kv[1]["published"], reverse=True)
    month_counts = collections.Counter(p["published"][:7] for _, p in ordered if p["published"])
    day_counts = collections.Counter(p["published"][:10] for _, p in ordered if p["published"])
    cur_ym = object()
    cur_day = object()
    open_month = False
    for slug, p in ordered:
        ym = p["published"][:7] if p["published"] else None
        day = p["published"][:10] if p["published"] else None
        if ym != cur_ym:
            if open_month:
                A('</ul></div></div>')
            cur_ym = ym
            cur_day = object()
            label = _pretty_month(ym) if ym else "Undated"
            n = month_counts[ym] if ym else sum(1 for _, pp in ordered if not pp["published"])
            hid = f'gs-m-{ym or "undated"}'
            A(f'<div class="cmonth" data-ym="{E(ym or "")}"><h3 class="cgroup" id="{E(hid)}">'
              f'<span>{E(label)}</span><span class="cgroup-n">{n} article{"s" if n != 1 else ""}</span></h3>')
            open_month = True
            first_day = True
        if day != cur_day:
            if not first_day:
                A('</ul></div>')
            first_day = False
            cur_day = day
            did = f'gs-d-{day or "undated"}'
            nd = day_counts[day] if day else sum(1 for _, pp in ordered if not pp["published"])
            dlabel = _weekday_date(day) if day else "Undated"
            A(f'<div class="cdayg" data-date="{E(day or "")}"><h4 class="cday" id="{E(did)}">{E(dlabel)}'
              f'<span class="cday-n"> &middot; {nd} article{"s" if nd != 1 else ""}</span></h4>'
              f'<ul class="crows" aria-labelledby="{E(did)}">')
        labels = labels_by_slug.get(slug) or []
        tag, tag_cls = (labels[0], "ctag") if labels else ("Unlabelled", "ctag none")
        date_str = _pretty_date(p["published"]) if p["published"] else "?"
        A(f'<li class="crow" data-ym="{E(ym or "")}" data-date="{E(day or "")}" data-topic="{E(tag)}"'
          f' data-kw="{E(keywords.get(slug, ""))}">')
        A(f'<time class="cdate" datetime="{E(day or "")}">{E(date_str)}</time>')
        A(f'<span class="{tag_cls}"><span class="sr-only">Topic: </span>{E(tag)}</span>')
        A(f'<a class="ctitle" href="{E(p["url"])}">{E(p["title"])}</a>')
        geo = (p["countries"][:2] + p["states"][:2])
        rel = [r for r in p["related"] if r["slug"] in posts][:3]
        if geo or rel:
            A('<span class="csub">')
            if geo:
                A(f'<span class="cgeo"><span class="sr-only">About: </span>{E(", ".join(geo))}</span>')
            if rel:
                def _rl(r):
                    t_ = posts[r["slug"]]["title"]
                    return f'<a class="crel-a" href="{E(posts[r["slug"]]["url"])}">{E(t_)}</a>'
                links = " ".join(_rl(r) for r in rel)
                A(f'<span class="crel-lbl">Related</span> {links}')
            A('</span>')
        A('</li>')
    if open_month:
        A('</ul></div></div>')
    A('<p class="gs-filter-empty" id="gs-f-empty" role="status">No articles match this search and filter combination.</p>')
    A('</div>')
    A(FILTER_JS)

    body = "\n".join(o)
    head = Path(args.shell_head).read_text(encoding="utf-8") if args.shell_head else ""
    # The body already carries the topnav index link (above); drop any copy the
    # shell head brings so the live page does not show it twice.
    head = re.sub(r'<div class="topnav-index-link"[^>]*>.*?</div>\s*', "", head, flags=re.S)
    head = head.replace('<div class="artx idx">', '<div class="artx idx" lang="en">', 1)
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
 font-size:.8rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#0a4c6a;
 margin:0;border-bottom:1px solid #e2e2e2;padding-bottom:.3rem}
.artx .geoh span{color:#595959;font-weight:600}
.artx .serial{border-left:3px solid #8a4b08;padding:.2rem 0 .2rem 1.1rem;margin:1.1rem 0 2rem}
.artx .gs-filter-bar{display:grid;grid-template-columns:repeat(auto-fit,minmax(11.5rem,1fr));align-items:end;gap:.8rem;background:#F4F7FB;
 border:1px solid #e2e6ee;border-radius:8px;padding:.65rem .8rem;margin:14px 0 0;
 font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
.artx .gs-filter-bar label{font-size:.78rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;
 color:#3d3d3d;margin:0}
.artx .gs-filter-bar select,.artx .gs-filter-bar input[type=search]{font-family:inherit;font-size:.95rem;color:#0B1F2D;background:#fff;
 border:1px solid #767676;border-radius:5px;padding:.4rem .6rem;min-height:44px;box-sizing:border-box;width:100%;max-width:none}
.artx .gs-filter-reset{font-family:inherit;font-size:.88rem;font-weight:600;color:#12408f;
 background:#fff;border:1px solid #12408f;border-radius:5px;cursor:pointer;padding:.4rem .8rem;min-height:44px;width:100%}
.artx .gs-filter-reset:hover{background:#e6ecf5}
.artx .gs-filter-count{font-size:.9rem;color:#3d3d3d;grid-column:1/-1;margin:0;min-height:1.2em}
.artx .gs-fulltext{grid-column:1/-1;margin:0;font-size:.88rem;color:#3d3d3d}
.artx .gs-fulltext a{color:#0B3D91;text-decoration:underline}
.artx .crow.via-text::after{content:"Matched in article text";display:block;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:.72rem;letter-spacing:.04em;text-transform:uppercase;color:#595959;margin-top:.15rem}
.artx .gs-filter-empty{display:none;padding:1.2rem .2rem;color:#595959;font-size:.9rem;font-style:italic}
.artx .chrono{border-top:1px solid #e2e2e2;margin:1.2rem 0 0}
.artx .cgroup{position:sticky;top:0;z-index:1;display:flex;align-items:baseline;
 justify-content:space-between;gap:.6rem;background:#0B1F2D;color:#fff;
 padding:.55rem .7rem;margin:0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',
 Helvetica,Arial,sans-serif;font-size:.9rem;font-weight:700;letter-spacing:.03em}
.artx .cgroup-n{font-weight:600;letter-spacing:0;color:#d5dbe2;white-space:nowrap}
.artx .crow{display:grid;grid-template-columns:6.4rem 11rem 1fr;align-items:baseline;
 column-gap:1.1rem;row-gap:.2rem;padding:.85rem .2rem;border-bottom:1px solid #e2e2e2;
 transition:background-color .12s ease}
.artx .crow:hover{background:#F4F7FB}
.artx .crow:hover .ctitle{color:#12408f;text-decoration:underline}
.artx .cdate{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
 font-size:.84rem;color:#595959;font-variant-numeric:tabular-nums;white-space:nowrap;
 padding-top:.15rem}
.artx .ctag{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
 font-size:.78rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#12408f;
 padding-top:.15rem}
.artx .ctag.none{color:#595959;font-weight:600;letter-spacing:.03em;text-transform:none}
.artx .ctitle{grid-column:3;font-family:Georgia,'Times New Roman',serif;font-size:1.02rem;
 line-height:1.4;color:#0B1F2D;text-decoration:none;transition:color .12s ease}
.artx .csub{grid-column:3;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,
 sans-serif;font-size:.86rem;color:#595959;line-height:1.55}
.artx .csub a{color:#3d3d3d;text-decoration:underline;text-underline-offset:2px}
.artx .csub .crel-lbl{font-weight:700;text-transform:uppercase;letter-spacing:.07em;font-size:.8rem;
 color:#8a4b08}
.artx .csub .cdot{margin:0 .1rem}
@media (max-width:640px){
 .artx .crow{grid-template-columns:1fr;row-gap:.25rem;padding:1rem .2rem}
 .artx .ctitle,.artx .csub{grid-column:1}
 .artx .gs-filter-bar{grid-template-columns:1fr}
 .artx .gs-filter-count{order:99}
}

/*gs-a11y-index-v1*/
.sr-only{position:absolute!important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.artx .gs-skip{position:absolute;left:-9999px;top:0;z-index:1000;background:#0B1F2D;color:#fff;
 font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:1rem;
 padding:.7rem 1rem;border-radius:0 0 6px 0}
.artx .gs-skip:focus{left:0}
.artx a:focus-visible,.artx button:focus-visible,.artx summary:focus-visible,.artx select:focus-visible,
.artx input:focus-visible,.artx [tabindex]:focus-visible{outline:3px solid #8a4b08;outline-offset:2px;border-radius:2px}
.artx .gs-jump{margin:1.2rem 0 .4rem;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
.artx .gs-jump-lbl{font-size:.8rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#3d3d3d;margin:0 0 .4rem}
.artx .gs-jump ul{display:flex;flex-wrap:wrap;gap:.5rem;list-style:none;margin:0;padding:0;max-width:none}
.artx .gs-jump li{max-width:none;margin:0}
.artx .gs-jump a{display:inline-block;min-height:44px;box-sizing:border-box;padding:.65rem .9rem;border:1px solid #12408f;
 border-radius:5px;font-size:.92rem;font-weight:600;color:#12408f;text-decoration:none;background:#fff}
.artx .gs-jump a:hover{background:#e6ecf5}
.artx .gs-latest{list-style:none;margin:0 0 1rem;padding:0;max-width:none}
.artx .gs-latest li{max-width:none;padding:.7rem 0;border-bottom:1px solid #e2e2e2;font-size:1.02rem;line-height:1.4}
.artx .gs-latest time{display:block;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
 font-size:.84rem;color:#595959;margin-bottom:.1rem}
.artx .gs-f-field{display:flex;flex-direction:column;gap:.25rem}
.artx .cmonth{margin-top:.6rem}
.artx .cgroup{margin:0}
.artx .cday{margin:.7rem 0 .1rem;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
 font-size:.86rem;font-weight:700;color:#3d3d3d;border-bottom:1px solid #e2e2e2;padding-bottom:.2rem}
.artx .cday-n{font-weight:400;color:#595959}
.artx .cdayg .cdate{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.artx .crows{list-style:none;margin:0;padding:0;max-width:none}
.artx .crow{max-width:none}
.artx .ctitle{text-decoration:underline;text-decoration-color:#c7cbd1;text-underline-offset:3px}
.artx .ctitle:hover,.artx .ctitle:focus-visible{text-decoration-color:currentColor}
.artx .gs-gtable{margin:1rem 0 0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
.artx .gs-gtable summary{cursor:pointer;min-height:44px;box-sizing:border-box;padding:.6rem 0;font-weight:700;font-size:.95rem;color:#12408f}
.artx .gs-gtable th[scope=row]{text-align:left;font-weight:600;white-space:normal}
.artx .gs-gtable td:last-child{text-align:left;white-space:normal}
.artx tbody th[scope=row]{text-align:left;font-weight:600;padding:.46rem .65rem;border-bottom:1px dotted #d9d9d9}
.artx .tw[tabindex]{outline-offset:2px}
.artx .csub .cgeo{display:block;margin-bottom:.15rem}
.artx .csub .crel-a{display:inline-block;margin-right:1rem;max-width:30ch;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;vertical-align:bottom}
.artx .csub .crel-a:focus,.artx .csub .crel-a:hover{max-width:none;white-space:normal}
.artx .eyebrow{font-size:.8rem}
.artx h2{font-size:.88rem}
.artx .stat span{font-size:.88rem}
.artx .exno{font-size:.78rem}
.artx .exsrc{font-size:.82rem}
.artx thead th{font-size:.78rem}
.artx .revised,.artx .sources{font-size:.84rem}
.artx .gs-filter-empty{font-size:1rem}
/*gs-a11y-index-v2: WCAG 2.2 target size (2.5.8, 24 by 24 CSS px) for every link in the lists, and no clipped link text*/
.artx .ctitle{display:inline-block;min-height:24px;box-sizing:border-box;padding:.1rem 0}
.artx .csub{line-height:1.9}
.artx .csub .crel-a{max-width:none;white-space:normal;overflow:visible;text-overflow:clip;overflow-wrap:anywhere;vertical-align:baseline;min-height:24px;box-sizing:border-box;padding:.1rem 0;margin-right:1rem}
.artx .gs-acc-hub,.artx .topnav-index-link a,.artx .ptitle a,.artx .prel a,.artx .gs-gtable td a,.artx .gs-gtable th a,.artx .gs-latest a{display:inline-block;min-height:24px;box-sizing:border-box;padding:.1rem 0}
.artx .tw td a,.artx .tw th a,.artx .geoblock li a,.artx h3 a{display:inline-block;min-height:24px;box-sizing:border-box;padding:.1rem 0}
@media (prefers-reduced-motion:reduce){.artx *{transition:none!important;scroll-behavior:auto!important}}
@media (forced-colors:active){.artx .cgroup,.artx .gs-skip{border:1px solid CanvasText}}
</style>
"""
    Path(args.out).write_text(head + extra + body + tail, encoding="utf-8")
    print(f"wrote {args.out} ({len(head)+len(extra)+len(body)+len(tail):,} bytes, {len(posts)} posts)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
