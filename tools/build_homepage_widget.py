#!/usr/bin/env python3
"""Build a compact topic accordion for Blogger's homepage sidebar.

    python3 tools/build_homepage_widget.py --out out/homepage-accordion-widget.html

This is NOT a post -- Blogger sidebar gadgets ("HTML/JavaScript" widgets) live
outside the Posts API entirely and can only be added through Blogger's Layout
editor in the browser (Layout -> Add a Gadget -> HTML/JavaScript -> paste the
file's contents -> Save). blogger_api.py cannot publish this; there is no
--publish flag here on purpose.

Reuses the exact self-updating JSONP-against-Blogger's-own-label-feeds pattern
from build_index_page.py's full-page accordion (see that file for the design
rationale: a hand-kept list drifts, this can't). This version is scaled down
for a ~300px sidebar rather than the 760px post column: smaller type, tighter
spacing, and each topic previews only its 6 newest posts with a link to the
full label hub page, rather than up to 150.

Class names are prefixed gs-side-* (not gs-acc-*) so this can safely render
on the same page as the full accordion (e.g. a visitor viewing the Article
Index post, which has the full one in its body, would also see this widget
in the sidebar) without any CSS collision between the two.
"""
import argparse
import html
from pathlib import Path

E = lambda s: html.escape(s, quote=True)

# Same 17 label hubs build_index_page.py uses, kept as a literal copy rather
# than an import so this script has no dependency on that one's module path.
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

INDEX_URL = "https://masaladeutsch.blogspot.com/2026/08/article-index-start-here.html"

CSS = """<style>/*gs-side-acc-v1*/
.gs-side-wrap{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;max-width:320px}
.gs-side-title{font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#595959;margin:0 0 .6rem}
.gs-side-acc{border-top:1px solid #e2e2e2}
.gs-side-acc:last-of-type{border-bottom:1px solid #e2e2e2}
.gs-side-acc summary{cursor:pointer;padding:.55rem .1rem;font-weight:600;font-size:.85rem;color:#0B1F2D;list-style:none;display:flex;align-items:baseline;gap:.4rem}
.gs-side-acc summary::-webkit-details-marker{display:none}
.gs-side-acc summary::after{content:'+';margin-left:auto;color:#2251FF;font-weight:600;font-size:.85rem}
.gs-side-acc[open] summary::after{content:'\\2212'}
.gs-side-n{font-weight:600;font-size:.68rem;color:#8a8a8a}
.gs-side-acc ul{margin:.1rem 0 .7rem;padding-left:1rem}
.gs-side-acc li{font-size:.8rem;line-height:1.4;margin-bottom:.32rem}
.gs-side-acc li a{color:#0B1F2D;text-decoration:none}
.gs-side-acc li a:hover{color:#2251FF;text-decoration:underline}
.gs-side-more{display:block;font-size:.7rem;font-weight:600;color:#2251FF;text-decoration:none;margin:.1rem 0 .3rem}
.gs-side-foot{font-size:.72rem;margin-top:.7rem;padding-top:.6rem;border-top:1px solid #e2e2e2}
.gs-side-foot a{color:#2251FF;font-weight:600;text-decoration:none}
</style>"""

JS = """<script>//<![CDATA[
// Same JSONP-against-Blogger's-own-label-feeds pattern as the full-page
// accordion on the Article Index post (tools/build_index_page.py). Reading
// Blogger's own feed at view time, not a snapshot baked in at build time,
// is what keeps this from ever drifting stale the way a hand-kept sidebar
// list would.
(function(){
  var BASE='https://masaladeutsch.blogspot.com', n=0;
  window.gsSideAcc = window.gsSideAcc || {};
  function jsonp(url, cb){
    var name='s'+(n++); window.gsSideAcc[name]=cb;
    var s=document.createElement('script');
    s.src=url+'&callback=gsSideAcc.'+name;
    s.onerror=function(){ cb(null); };
    document.head.appendChild(s);
  }
  function feed(lbl, extra, cb){
    jsonp(BASE+'/feeds/posts/summary/-/'+encodeURIComponent(lbl)
      +'?alt=json-in-script'+extra, cb);
  }
  function fill(d){
    var ul=d.querySelector('ul'); if(ul.getAttribute('data-done')) return;
    ul.setAttribute('data-done','1');
    var label=d.getAttribute('data-label'), hub=d.getAttribute('data-hub');
    feed(label,'&orderby=published&max-results=6',function(res){
      if(!res){ ul.innerHTML='<li>Could not load &mdash; <a href="'+hub+'">open the topic page</a>.</li>'; return; }
      var es=res.feed.entry||[]; ul.innerHTML='';
      for(var i=0;i<es.length;i++){
        var e=es[i], href='';
        for(var j=0;j<(e.link||[]).length;j++)
          if(e.link[j].rel==='alternate') href=e.link[j].href;
        var li=document.createElement('li'), a=document.createElement('a');
        a.href=href; a.textContent=e.title.$t; li.appendChild(a);
        ul.appendChild(li);
      }
      if(!es.length){ ul.innerHTML='<li>No posts carry this label yet.</li>'; return; }
      var more=document.createElement('a');
      more.className='gs-side-more'; more.href=hub; more.textContent='All '+label+' articles \\u2192';
      ul.parentNode.insertBefore(more, ul.nextSibling);
    });
  }
  var ds=document.querySelectorAll('details.gs-side-acc');
  for(var k=0;k<ds.length;k++)(function(d){
    feed(d.getAttribute('data-label'),'&max-results=0',function(res){
      if(res) d.querySelector('.gs-side-n').textContent =
        res.feed.openSearch$totalResults.$t;
    });
    d.addEventListener('toggle',function(){ if(d.open) fill(d); });
  })(ds[k]);
})();
//]]></script>"""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="out/homepage-accordion-widget.html")
    args = ap.parse_args()

    o = []
    A = o.append
    A(CSS)
    A('<div class="gs-side-wrap">')
    A('<p class="gs-side-title">Browse by topic</p>')
    for name, slugpart in sorted(LABEL_HUBS, key=lambda t: t[0].lower()):
        hub = f"https://masaladeutsch.blogspot.com/search/label/{slugpart}"
        A(f'<details class="gs-side-acc" data-label="{E(name)}" data-hub="{E(hub)}">'
          f'<summary>{E(name)} <span class="gs-side-n"></span></summary>'
          '<ul><li>Loading&#8230;</li></ul></details>')
    A(f'<p class="gs-side-foot"><a href="{E(INDEX_URL)}">Full article index &#8594;</a></p>')
    A('</div>')
    A(JS)

    body = "\n".join(o)
    Path(args.out).write_text(body, encoding="utf-8")
    print(f"wrote {args.out} ({len(body):,} bytes, {len(LABEL_HUBS)} topics)")
    print("This is a sidebar gadget snippet, not a post -- paste it into Blogger:")
    print("  Layout -> Add a Gadget -> HTML/JavaScript -> paste this file's contents -> Save")


if __name__ == "__main__":
    main()
