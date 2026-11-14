#!/usr/bin/env python3
"""Build a static, server-rendered topic hub for the GitHub Pages front door.

Why this exists: the blog's own browse-by-topic block is a Blogger theme
gadget, and the Blogger API v3 has no theme/template resource (verified
against the discovery document -- resources are blogUserInfos, blogs,
comments, pageViews, pages, postUserInfos, posts, users). Theme edits are
only possible through blogger.com, which is unavailable. On posts the topic
list is therefore injected by accordion.js at runtime, so it is invisible to
crawlers and to readers without JavaScript.

GitHub Pages is a surface we can actually deploy to. This writes a plain
HTML page -- no JavaScript needed to read it -- listing every published
article grouped by topic, generated from meta/manifest.json so it cannot
drift from what is actually published.

    python3 tools/build_topic_hub.py --out <path-to-pages-repo>/topics.html
"""
import argparse
import html
import json
import pathlib
import re
import urllib.parse
from collections import defaultdict
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
BLOG = "https://blog.vertistratsolution.com"
# "Shop" is a page, not a subject; it has its own front-door link.
EXCLUDE_LABELS = {"Shop"}

CSS = """
:root{color-scheme:only light}
*{box-sizing:border-box}
/* Must beat the author `display` rules below: the UA stylesheet gives [hidden]
   only display:none, which any explicit display (e.g. ul.posts li{display:flex})
   silently overrides -- so the search would count matches while showing
   everything. */
[hidden]{display:none!important}
body{margin:0;padding:2rem 1rem 3rem;background:#fff;color:#1a1a1a;
 font-family:Georgia,"Times New Roman",serif;line-height:1.6}
main{max-width:46rem;margin:0 auto}
h1{font-size:2rem;line-height:1.2;margin:.2rem 0 .6rem;letter-spacing:-.01em}
.lede{font-size:1.05rem;line-height:1.6;color:#43535F;margin:0 0 1.4rem}
a{color:#2251FF}
.sans{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.cta{display:inline-block;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
 font-weight:700;font-size:.9rem;background:#0B1F2D;color:#fff;padding:.7rem 1.2rem;
 border-radius:2px;text-decoration:none;margin:.4rem .6rem .4rem 0}
.cta.alt{background:#F4F7FB;color:#0B1F2D;border:1px solid #e2e6ee}
.jump{border-top:1px solid #e2e2e2;border-bottom:1px solid #e2e2e2;padding:1rem 0;margin:1.6rem 0 2rem}
.jump-lbl{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
 font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:#8a4b08;font-weight:700;margin:0 0 .6rem}
.chip{display:inline-block;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
 font-size:.8rem;font-weight:600;color:#0B1F2D;background:#F4F7FB;border:1px solid #e2e6ee;
 padding:.35rem .7rem;border-radius:2px;text-decoration:none;margin:0 .35rem .4rem 0}
.chip:hover{background:#e6ecf5}
.chip .n{color:#8a8a8a;font-weight:400}
section.topic{margin:0 0 2.2rem;scroll-margin-top:1rem}
section.topic h2{font-size:.78rem;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
 letter-spacing:.14em;text-transform:uppercase;color:#8a4b08;margin:0 0 .1rem;
 border-bottom:2px solid #0B1F2D;padding-bottom:.4rem;display:flex;justify-content:space-between;
 align-items:baseline;gap:1rem}
section.topic h2 .n{color:#8a8a8a;font-weight:400;letter-spacing:0;text-transform:none;font-size:.75rem;
 white-space:nowrap}
ul.posts{list-style:none;margin:.7rem 0 0;padding:0}
ul.posts li{margin:0 0 .55rem;padding-left:0;display:flex;gap:.8rem;align-items:baseline}
ul.posts .d{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
 font-size:.72rem;color:#8a8a8a;white-space:nowrap;min-width:5.6rem;font-variant-numeric:tabular-nums}
ul.posts a{text-decoration:none}
ul.posts a:hover{text-decoration:underline}
.top{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
 font-size:.72rem;color:#8a8a8a;text-decoration:none;margin-left:.6rem}
.foot{margin-top:2.6rem;font-size:.8rem;color:#8a8a8a;border-top:1px solid #e2e2e2;padding-top:1rem}
/* Search is a progressive enhancement: the markup below is hidden until the
   script runs, so a reader without JavaScript never sees a dead control. */
.search[hidden]{display:none}
.search{margin:1.6rem 0 0}
.search label{display:block;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
 font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:#8a4b08;font-weight:700;margin:0 0 .5rem}
.search input{width:100%;font-family:Georgia,"Times New Roman",serif;font-size:1rem;color:#1a1a1a;
 background:#fff;border:1px solid #c9d0dc;border-radius:2px;padding:.7rem .85rem;-webkit-appearance:none}
.search input:focus{outline:2px solid #2251FF;outline-offset:1px;border-color:#2251FF}
.search .count{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
 font-size:.78rem;color:#43535F;margin:.55rem 0 0;min-height:1.2em}
.search .count b{color:#0B1F2D}
.nomatch{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
 font-size:.9rem;color:#43535F;background:#F4F7FB;border:1px solid #e2e6ee;padding:1rem;border-radius:2px}
mark{background:#fff2b8;color:inherit;padding:0 .05em}
ul.posts .e{flex:1}
.secs{display:block;margin:.2rem 0 .5rem;padding-left:.1rem}
.secs .sec{display:block;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
 font-size:.78rem;color:#43535F;line-height:1.45;padding-left:1.15rem;position:relative}
.secs .sec::before{content:"\2014";position:absolute;left:0;color:#b9c2cc}
@media (max-width:520px){
 ul.posts li{display:block}
 ul.posts .d{display:block;min-width:0;margin-bottom:.1rem}
}
"""


def slugify(label):
    return "t-" + "".join(c.lower() if c.isalnum() else "-" for c in label).strip("-")


def sections_for(slug):
    """h2 headings inside a post body, used as searchable sub-entries."""
    f = ROOT / "posts" / f"{slug}.html"
    if not f.exists():
        return []
    src = f.read_text(encoding="utf-8", errors="replace")
    src = re.sub(r"<script\b.*?</script>", "", src, flags=re.S | re.I)
    src = re.sub(r"<style\b.*?</style>", "", src, flags=re.S | re.I)
    out = []
    for m in re.finditer(r"<h2\b[^>]*>(.*?)</h2>", src, re.S):
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
        t = re.sub(r"\s+", " ", t)
        if 4 < len(t) < 110 and t not in out:
            out.append(t)
    return out


def load_posts():
    m = json.loads((ROOT / "meta" / "manifest.json").read_text())
    posts = m if isinstance(m, list) else m.get("posts", m)
    posts = posts if isinstance(posts, list) else list(posts.values())
    return [p for p in posts if isinstance(p, dict) and p.get("url") and p.get("title")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    posts = load_posts()
    by_topic = defaultdict(list)
    for p in posts:
        for lab in p.get("labels") or []:
            if lab not in EXCLUDE_LABELS:
                by_topic[lab].append(p)

    topics = sorted(by_topic, key=str.lower)
    for t in topics:
        by_topic[t].sort(key=lambda p: p.get("published", ""), reverse=True)

    labelled = {p["url"] for ps in by_topic.values() for p in ps}
    built = datetime.now().strftime("%d %B %Y")

    chips = "".join(
        f'<a class="chip" href="#{slugify(t)}">{html.escape(t)} '
        f'<span class="n">{len(by_topic[t])}</span></a>'
        for t in topics)

    secs = []
    for t in topics:
        items = ""
        for p in by_topic[t]:
            heads = sections_for(p.get("slug", ""))
            sec_html = "".join('<span class="sec">%s</span>' % html.escape(x) for x in heads)
            items += (
                '<li><span class="d">{d}</span><span class="e">'
                '<a href="{u}">{ttl}</a>'
                '<span class="secs" hidden="hidden">{secs}</span>'
                '</span></li>').format(
                    d=(p.get("published", "")[:10] or ""),
                    u=html.escape(p["url"], quote=True),
                    ttl=html.escape(p["title"]),
                    secs=sec_html)
        secs.append(
            f'<section class="topic" id="{slugify(t)}">'
            f'<h2>{html.escape(t)}'
            f'<span class="n"><span class="ct">{len(by_topic[t])} article{"s" if len(by_topic[t])!=1 else ""}</span>'
            f' &middot; <a class="top" href="{BLOG}/search/label/{urllib.parse.quote(t)}">on the blog &rarr;</a>'
            f'</span></h2>'
            f'<ul class="posts">{items}</ul></section>')

    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Every article by topic — Masala Deutsch</title>
<meta name="description" content="Every article on blog.vertistratsolution.com, grouped by topic: {len(topics)} topics, {len(labelled)} articles. A plain, static index that needs no JavaScript.">
<link rel="canonical" href="https://herrrickshaw.github.io/masaladeutsch/topics.html">
<meta property="og:title" content="Every article by topic — Masala Deutsch">
<meta property="og:description" content="{len(topics)} topics, {len(labelled)} articles, grouped and dated.">
<meta property="og:type" content="website">
<style>{CSS}</style>
</head>
<body>
<main>
<h1>Every article by topic</h1>
<p class="lede">The full archive of <a href="{BLOG}">Masala Deutsch</a>, grouped.
{len(labelled)} articles across {len(topics)} topics, newest first within each.
This page is plain HTML &mdash; it needs no JavaScript and does not go stale silently,
because it is generated from the published-post manifest. Search reaches inside the
articles too: section headings are indexed, so a term that appears only in one part
of a piece will still find it.</p>

<p>
<a class="cta" href="{BLOG}">Read the blog</a>
<a class="cta alt" href="{BLOG}/2026/08/article-index-start-here.html">Full index, by date and connection</a>
<a class="cta alt" href="./">Front page</a>
</p>

<div class="search" id="search" hidden="hidden">
<label for="q">Search titles and topics</label>
<input type="search" id="q" name="q" autocomplete="off" spellcheck="false"
 placeholder="Norway, urea, Hormuz, tariff stack&hellip;" aria-describedby="qcount">
<p class="count" id="qcount" role="status" aria-live="polite"></p>
</div>

<nav class="jump" id="jump" aria-label="Jump to a topic">
<p class="jump-lbl">Jump to a topic</p>
{chips}
</nav>

<p class="nomatch" id="nomatch" hidden="hidden">No article title or topic matches that.
Try a shorter word, or <a href="#" id="clearq">clear the search</a>.</p>

{"".join(secs)}

<p class="foot">Generated {built} from the blog's published-post manifest by
<code>tools/build_topic_hub.py</code> in the archive repo. Topic links go to the
blog's own label archives, which update themselves as pieces are labelled.
The search box filters this page in the browser; every article is in the HTML
either way.</p>
</main>
<script>
/* Client-side filter over markup that is already complete without it.
   Nothing here fetches or generates content -- it only hides rows. */
(function () {{
  var box = document.getElementById('search'),
      q = document.getElementById('q'),
      count = document.getElementById('qcount'),
      jump = document.getElementById('jump'),
      none = document.getElementById('nomatch'),
      clear = document.getElementById('clearq'),
      secs = [].slice.call(document.querySelectorAll('section.topic')),
      total = document.querySelectorAll('ul.posts li').length;

  var rows = secs.map(function (s) {{
    return {{
      sec: s,
      topic: (s.querySelector('h2') ? s.querySelector('h2').firstChild.nodeValue || '' : '').toLowerCase(),
      n: s.querySelector('h2 .n .ct'),
      nFull: s.querySelector('h2 .n .ct') ? s.querySelector('h2 .n .ct').textContent : '',
      items: [].slice.call(s.querySelectorAll('li')).map(function (li) {{
        var a = li.querySelector('a'), box = li.querySelector('.secs');
        var heads = box ? [].slice.call(box.querySelectorAll('.sec')) : [];
        return {{
          li: li, a: a, box: box, heads: heads,
          text: (a ? a.textContent : '').toLowerCase(),
          html: a ? a.textContent : '',
          secText: heads.map(function (h) {{ return h.textContent.toLowerCase(); }})
        }};
      }})
    }};
  }});

  function esc(s) {{ return s.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&'); }}

  function paint(term) {{
    var t = term.trim().toLowerCase(), shown = 0, re = t ? new RegExp('(' + esc(t) + ')', 'ig') : null;
    rows.forEach(function (r) {{
      var hit = 0, topicHit = t && r.topic.indexOf(t) !== -1;
      r.items.forEach(function (it) {{
        var titleHit = t && it.text.indexOf(t) !== -1;
        var secHits = [];
        if (t) {{
          for (var k = 0; k < it.secText.length; k++) {{
            if (it.secText[k].indexOf(t) !== -1) {{ secHits.push(k); }}
          }}
        }}
        var m = !t || topicHit || titleHit || secHits.length > 0;
        it.li.hidden = !m;
        if (m) {{ hit++; }}
        it.a.innerHTML = (t && re && !topicHit && titleHit)
          ? it.html.replace(re, '<mark>$1</mark>')
          : it.html;
        // show the sections that matched, so the reader sees why the article did
        if (it.box) {{
          it.heads.forEach(function (h, k) {{
            var on = secHits.indexOf(k) !== -1;
            h.hidden = !on;
            h.innerHTML = on && re ? h.textContent.replace(re, '<mark>$1</mark>') : h.textContent;
          }});
          it.box.hidden = secHits.length === 0;
        }}
      }});
      r.sec.hidden = hit === 0;
      if (r.n) {{
        r.n.textContent = t
          ? hit + ' of ' + r.items.length + ' shown'
          : r.nFull;
      }}
      shown += hit;
    }});
    if (jump) {{ jump.hidden = !!t; }}
    if (none) {{ none.hidden = shown !== 0; }}
    count.innerHTML = t
      ? '<b>' + shown + '</b> of ' + total + ' entries match &ldquo;' + t.replace(/&/g, '&amp;').replace(/</g, '&lt;') + '&rdquo;'
      : '';
    var u = new URL(location.href);
    if (t) {{ u.searchParams.set('q', term.trim()); }} else {{ u.searchParams.delete('q'); }}
    history.replaceState(null, '', u);
  }}

  box.hidden = false;                       // only now is the control real
  q.addEventListener('input', function () {{ paint(q.value); }});
  q.addEventListener('keydown', function (e) {{
    if (e.key === 'Escape') {{ q.value = ''; paint(''); }}
  }});
  if (clear) {{
    clear.addEventListener('click', function (e) {{
      e.preventDefault(); q.value = ''; paint(''); q.focus();
    }});
  }}
  var pre = new URLSearchParams(location.search).get('q');
  if (pre) {{ q.value = pre; paint(pre); }}
}})();
</script>
</body>
</html>
"""
    out = pathlib.Path(args.out)
    out.write_text(doc, encoding="utf-8")
    print(f"wrote {out}  {len(doc):,} bytes")
    print(f"  {len(topics)} topics, {len(labelled)} distinct articles, "
          f"{sum(len(v) for v in by_topic.values())} topic-article rows")
    thin = [t for t in topics if len(by_topic[t]) == 1]
    if thin:
        print(f"  single-article topics: {', '.join(thin)}")


if __name__ == "__main__":
    main()
