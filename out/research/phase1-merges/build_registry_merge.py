#!/usr/bin/env python3
"""Phase 1 merge (10 Nov 2026): fold the Rajya Sabha Question Registry into the Lok Sabha one.

Target  posts/lok-sabha-question-registry-1843-scheme.html
Absorbs posts/rajya-sabha-question-registry-scheme.html
Output  out/update-2026-11-10-lok-sabha-question-registry-1843-scheme.html

The two posts share one template and one data shape (D = {s: schemes, m: ministries, r: rows}).
The merged page carries both Houses in one array with a House field and a House filter. To keep
the page small, the answer-PDF URL is stored as the path between a per-House prefix and suffix,
and member names as an index into D.p. No row is dropped; the assertions below check that.
"""
import collections, html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[3]
LS_SLUG, RS_SLUG = "lok-sabha-question-registry-1843-scheme", "rajya-sabha-question-registry-scheme"
OUT = ROOT / f"out/update-2026-11-10-{LS_SLUG}.html"
T = (ROOT / f"posts/{LS_SLUG}.html").read_text()
TR = (ROOT / f"posts/{RS_SLUG}.html").read_text()


def data(t):
    i = t.find("var D={")
    D, n = json.JSONDecoder().raw_decode(t[i + 6:])
    s = t.rfind("<script", 0, i)
    e = t.find("</script>", i) + len("</script>")
    return D, s, e


L, ls_s, ls_e = data(T)
R, _, _ = data(TR)
PRE = [("https://sansad.in/getFile/lsapps/loksabhaquestions/annex/", "?source=lsapps"),
       ("https://sansad.in/getFile/annex/", "?source=pqars")]

S = sorted(set(L["s"]) | set(R["s"]))
M = sorted(set(L["m"]) | set(R["m"]))
P = sorted({r[8] for r in L["r"]} | {r[8] for r in R["r"]})
rows = []
for h, D in ((0, L), (1, R)):
    pre, suf = PRE[h]
    for r in D["r"]:
        url = r[7]
        part = url[len(pre):-len(suf)] if url.startswith(pre) and url.endswith(suf) else url  # full URL kept if off-pattern
        rows.append([r[0], sorted(S.index(D["s"][k]) for k in r[1]), M.index(D["m"][r[2]]), r[3], r[4], r[5], r[6],
                     part, P.index(r[8]), h])
rows.sort(key=lambda r: (r[0], -r[9]), reverse=True)
assert len(rows) == len(L["r"]) + len(R["r"]) == 3773
# round-trip check: every original row is reconstructable
def back(r):
    pre, suf = PRE[r[9]]
    url = r[7] if r[7].startswith("http") else pre + r[7] + suf
    return (r[0], tuple(sorted(S[k] for k in r[1])), M[r[2]], r[3], r[4], r[5], r[6], url, P[r[8]])
orig = collections.Counter((r[0], tuple(sorted(D["s"][k] for k in r[1])), D["m"][r[2]], r[3], r[4], r[5], r[6], r[7], r[8])
                           for D in (L, R) for r in D["r"])
assert collections.Counter(back(r) for r in rows) == orig, "round-trip mismatch"

n_ls, n_rs = len(L["r"]), len(R["r"])
st_ls, st_rs = sum(r[4] for r in L["r"]), sum(r[4] for r in R["r"])
cnt = lambda D, name: sum(1 for r in D["r"] if any(D["s"][k] == name for k in r[1]))
ud_ls, ud_rs = cnt(L, "UDAN / RCS (VGF)"), cnt(R, "UDAN / RCS (VGF)")
dmin = min(r[0] for r in rows); dmax = max(r[0] for r in rows)
assert (n_ls, n_rs, st_ls, st_rs, ud_ls, ud_rs) == (1890, 1883, 104, 141, 273, 293)
tot, st, ud = n_ls + n_rs, st_ls + st_rs, ud_ls + ud_rs

js_data = json.dumps({"s": S, "m": M, "p": P, "h": ["Lok Sabha", "Rajya Sabha"], "pre": PRE, "r": rows},
                     ensure_ascii=False, separators=(",", ":"))
script = """<script type="text/javascript">
(function(){
var D=""" + js_data + """;
var S=D.s,M=D.m,P=D.p,RW=D.r,PAGE=300;
var q=document.getElementById('pq'),sf=document.getElementById('ps'),
    mf=document.getElementById('pm'),tf=document.getElementById('pf'),
    yf=document.getElementById('pt'),hf=document.getElementById('ph'),cn=document.getElementById('pc'),
    ls=document.getElementById('plist');
function quarter(d){return d.slice(0,4)+'Q'+((((+d.slice(5,7))-1)/3|0)+1);}
function url(r){var x=r[7];if(x.indexOf('http')===0)return x;var p=D.pre[r[9]];return p[0]+x+p[1];}
var qs=[];RW.forEach(function(r){var x=quarter(r[0]);if(qs.indexOf(x)<0)qs.push(x);});
qs.forEach(function(v){q.add(new Option(v,v));});
S.forEach(function(v,i){sf.add(new Option(v,i));});
M.forEach(function(v,i){mf.add(new Option(v,i));});
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
var shown=PAGE;
function match(){
  var Q=q.value,Sv=sf.value,Mv=mf.value,T=tf.value.toLowerCase(),Y=yf.value,H=hf.value;
  return RW.filter(function(r){
    if(H!==''&&r[9]!==+H)return false;
    if(Q&&quarter(r[0])!==Q)return false;
    if(Sv!==''&&r[1].indexOf(+Sv)<0)return false;
    if(Mv!==''&&r[2]!==+Mv)return false;
    if(Y!==''&&r[4]!==+Y)return false;
    if(T&&(r[6]+' '+P[r[8]]).toLowerCase().indexOf(T)<0)return false;
    return true;});
}
function render(){
  var f=match(),out=[],cur='',n=Math.min(shown,f.length);
  for(var i=0;i<n;i++){
    var r=f[i],Q=quarter(r[0]);
    if(Q!==cur){cur=Q;var c=0;for(var j=i;j<f.length;j++){if(quarter(f[j][0])===Q)c++;}
      out.push('<div class="qh">'+Q+' <span class="n">&middot; '+c+
        (c===1?' question':' questions')+'</span></div>');}
    var chips='';for(var k=0;k<r[1].length;k++)chips+='<span class="chip">'+esc(S[r[1][k]])+'</span>';
    var house=r[9]===0?'LS'+r[3]:'RS Sess.'+r[3];
    out.push('<div class="row'+(r[9]===1?' rs':'')+'"><div class="top"><span class="date">'+r[0]+'</span>'+chips+
      '<span class="min">'+esc(M[r[2]])+'</span>'+
      '<span class="qn">'+house+' &middot; '+(r[4]?'<span class="star">&#9733; STARRED</span>':'Unstarred')+
      ' Q.'+r[5]+'</span></div><div class="ttl">'+
      '<a href="'+esc(url(r))+'" target="_blank" rel="noopener">'+esc(r[6])+'</a></div>'+
      '<div class="mem">Asked by '+esc(P[r[8]])+' &middot; '+D.h[r[9]]+'</div></div>');
  }
  if(n<f.length)out.push('<button class="more" id="pmore">Show '+
    Math.min(PAGE,f.length-n)+' more &mdash; '+(f.length-n)+' still hidden</button>');
  ls.innerHTML=out.join('');
  cn.textContent=f.length.toLocaleString()+' of '+RW.length.toLocaleString();
  var b=document.getElementById('pmore');
  if(b)b.onclick=function(){shown+=PAGE;render();};
}
function reset(){shown=PAGE;render();}
[q,sf,mf,yf,hf].forEach(function(e){e.addEventListener('change',reset);});
var tm;tf.addEventListener('input',function(){clearTimeout(tm);tm=setTimeout(reset,180);});
render();
})();
</script>"""

t = T[:ls_s] + script + T[ls_e:]


def rep(old, new, n=1):
    global t
    c = t.count(old)
    assert c == n, (c, old[:80])
    t = t.replace(old, new)


fmt = lambda x: f"{x:,}"
# header
s0 = t.find('<p style="order:4" class="dek">'); e0 = t.find("</p>", s0) + 4
t = t[:s0] + (
    f'<p style="order:4" class="dek"><strong>UDAN/RCS draws more parliamentary questions than any other scheme in both Houses</strong> '
    f'&mdash; {fmt(ud_ls)} of the {fmt(n_ls)} Lok Sabha questions and {fmt(ud_rs)} of the {fmt(n_rs)} Rajya Sabha questions captured here, '
    f'{fmt(ud)} of {fmt(tot)} in all. This registry covers questions on investment policies, schemes and incentives in both Houses '
    f'({dmin} &rarr; {dmax}), each mapped to its scheme and answering ministry, with a link to the official answer PDF on sansad.in. '
    f'{fmt(st)} were starred (answered orally on the floor): {st_ls} in the Lok Sabha and {st_rs} in the Rajya Sabha. '
    'The starred/unstarred split comes from case-sensitive text matching on the question-type field, which is known to miscount '
    'a small number of mixed-case rows, so treat it as approximate.</p>') + t[e0:]
rep('<h1 style="order:3">Lok Sabha Question Registry</h1>', '<h1 style="order:3">Parliament Question Registry &mdash; Lok Sabha &amp; Rajya Sabha</h1>')
rep('<figcaption style="font-size:.8em;color:#868e96;font-family:-apple-system,\'Segoe UI\',sans-serif;margin-top:.5rem;max-width:640px;margin-left:auto;margin-right:auto">The new Parliament House, New Delhi, seat of the Lok Sabha since 2023.',
    '<figcaption style="font-size:.8em;color:#868e96;font-family:-apple-system,\'Segoe UI\',sans-serif;margin-top:.5rem;max-width:640px;margin-left:auto;margin-right:auto">The new Parliament House, New Delhi, seat of both Houses since 2023.')

# chart: replace the Lok Sabha-only UDAN chart with a both-Houses chart
fs = t.find('<figure class="gb-figure"'); fe = t.find("</figure>", fs) + len("</figure>")
W = 560
wl, wr = round(W * n_ls / max(n_ls, n_rs)), round(W * n_rs / max(n_ls, n_rs))
ul, ur = round(W * ud_ls / max(n_ls, n_rs)), round(W * ud_rs / max(n_ls, n_rs))
svg = f'''<figure class="gb-figure" style="margin:1.5rem 0 1.75rem;text-align:center">
<svg role="img" aria-label="Scheme questions by House: Lok Sabha {n_ls}, of which UDAN {ud_ls}; Rajya Sabha {n_rs}, of which UDAN {ud_rs}" style="width:100%;height:auto;max-width:700px;display:block;margin:0 auto" viewBox="0 0 700 360" xmlns="http://www.w3.org/2000/svg" font-family="Georgia, 'Times New Roman', serif">
  <rect x="0" y="0" width="700" height="360" fill="#f8f9fa" />
  <text x="40" y="46" font-size="21" font-weight="bold" fill="#1a1a1a">UDAN/RCS leads in both Houses</text>
  <text x="40" y="68" font-size="13" fill="#555555">Scheme and incentive questions captured, 2019&#8211;2026; dark part = UDAN/RCS</text>
  <text x="40" y="118" font-size="14" fill="#1a1a1a" font-weight="bold">Lok Sabha: {fmt(n_ls)} questions</text>
  <rect x="40" y="128" width="{wl}" height="40" fill="#9fc0dc" />
  <rect x="40" y="128" width="{ul}" height="40" fill="#0b5794" />
  <text x="{40 + ul + 8}" y="154" font-size="14" fill="#0b2a44" font-weight="bold">UDAN/RCS {ud_ls}</text>
  <text x="40" y="218" font-size="14" fill="#1a1a1a" font-weight="bold">Rajya Sabha: {fmt(n_rs)} questions</text>
  <rect x="40" y="228" width="{wr}" height="40" fill="#9fc0dc" />
  <rect x="40" y="228" width="{ur}" height="40" fill="#0b5794" />
  <text x="{40 + ur + 8}" y="254" font-size="14" fill="#0b2a44" font-weight="bold">UDAN/RCS {ud_rs}</text>
  <line x1="40" y1="300" x2="600" y2="300" stroke="#cccccc" stroke-width="1" />
  <text x="40" y="324" font-size="12.5" fill="#555555">Starred (oral) questions: {st_ls} in the Lok Sabha, {st_rs} in the Rajya Sabha. Next-largest schemes:</text>
  <text x="40" y="342" font-size="12.5" fill="#555555">PM MITRA (160 LS, 100 RS), Jal Jeevan Mission (141, 128), ethanol blending (136, 121).</text>
</svg>
<figcaption style="font-size:.8em;color:#868e96;font-family:-apple-system,'Segoe UI',sans-serif;margin-top:.5rem">UDAN/RCS accounts for {ud_ls} of {fmt(n_ls)} Lok Sabha and {ud_rs} of {fmt(n_rs)} Rajya Sabha questions in this registry, about one in seven in each House.</figcaption>
</figure>'''
t = t[:fs] + svg + t[fe:]

# controls: House filter
rep('<select id="pq" aria-label="Filter by quarter">',
    '<select id="ph" aria-label="Filter by House"><option value="">Both Houses</option><option value="0">Lok Sabha</option><option value="1">Rajya Sabha</option></select>\n<select id="pq" aria-label="Filter by quarter">')
rep('.pqx .more{', '.pqx .row.rs{border-left-color:#1a8f4c}\n.pqx .more{')

# intro paragraph inside .pqx, with the update note above it
i1 = t.find('<p class="dek">This registry is the parliamentary companion'); i2 = t.find("</p>", i1) + 4
note = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px">'
        f'<b>Updated 10 November 2026.</b> This page now combines the Lok Sabha registry with what was a separate post, the Rajya Sabha Question Registry '
        f'({fmt(n_rs)} questions); that post has been retired. Use the House filter to see one chamber. The data is unchanged: both Houses run to the end of '
        'the 2026 Monsoon Session (12&ndash;13 August), and the registry will be rebuilt after the Winter Session.</div>\n')
intro = ('<p class="dek">This registry is the parliamentary companion to the '
         '<a href="https://masaladeutsch.blogspot.com/2026/08/quarterly-reportage-4034-scheme.html" style="color:var(--acc)">Quarterly Reportage</a>: '
         'where the reportage tracks what government <em>announced</em>, this tracks what Parliament <em>asked</em>, in both Houses, and the ministry&rsquo;s '
         'answer of record. Questions are classified by the same scheme-keyword map, so the two views filter identically. Use it to find the answer, then '
         'read the answer. The underlying data analysis and build scripts are backed up at '
         '<a href="https://github.com/herrrickshaw" style="color:var(--acc)">github.com/herrrickshaw</a>.</p>')
t = t[:i1] + note + intro + t[i2:]

# notes: method, limits, UDAN, starred, purpose, AI
m1 = t.find('<p class="note">\n<strong>Method.</strong>'); m2 = t.find('</div>', m1)
notes = f'''<p class="note">
<strong>Method.</strong> Lok Sabha questions were harvested from sansad.in&#39;s Lok Sabha Q&amp;A index by subject keyword (17th Lok Sabha:
2019&ndash;2024; 18th: 2024 to date), and Rajya Sabha questions from the rsdoc.nic.in per-question index with the same keyword lists, from 2019.
Both were then classified against the same scheme-regex map and acronym-veto list as the Quarterly Reportage &mdash; so &ldquo;Sanchar Mitra&rdquo; does not
file under PM MITRA and IIT (ISM) Dhanbad does not file under the Semiconductor Mission here either. Generated 2026-08-19 by
<code>scripts/build_pq_registry.py</code> (Lok Sabha) and <code>scripts/build_rs_pq_registry.py</code> (Rajya Sabha) in
<a href="https://github.com/herrrickshaw/digital-twin-for-ipa" style="color:var(--acc)">digital-twin-for-ipa</a>; the two were combined into one page on
10 November 2026 with no rows added or removed.
</p>

<p class="note" style="border-top:none;margin-top:0">
<strong>Known limits, stated rather than hidden.</strong> Both indexes match keywords against the <em>subject line only</em>, so a question whose subject
names no scheme is not captured even when its answer discusses one at length &mdash; coverage is of scheme-titled questions, not of every mention.
Ministries answer as of their date; figures in older answers are superseded by newer ones. A row whose subject has nothing to do with its chip (the
coloured scheme tag) is a classification bug, not a parliamentary fact. The two Houses&rsquo; counts are not strictly comparable: the Rajya Sabha series
starts in January 2019 and the Lok Sabha series in June 2019.
</p>

<p class="note" style="border-top:none;margin-top:0">
<strong>Why UDAN/RCS draws this much scrutiny.</strong> At {fmt(ud)} of {fmt(tot)} questions &mdash; {ud_ls} in the Lok Sabha and {ud_rs} in the Rajya
Sabha, the most in each &mdash; UDAN&rsquo;s lead isn&rsquo;t really about the scheme&rsquo;s size in rupee terms; several other schemes in this registry carry
larger outlays. It&rsquo;s about how the scheme is structured. UDAN&rsquo;s viability-gap funding subsidises specific, named air routes between specific, named
airports, so a route delay, a suspension, an airline leaving a route or a new route being announced is a local event with an obvious member to ask about it.
A sector-wide capital subsidy or a national tax credit pays out through a formula with no geographic face and generates far fewer individually triggered
questions. That logic is often argued for the Lok Sabha, whose members represent constituencies, but the counts here show Rajya Sabha members, who
represent states, ask about UDAN just as often.
</p>

<p class="note" style="border-top:none;margin-top:0">
<strong>Why starred vs. unstarred matters.</strong> A starred question is one the member has flagged for an oral answer on the floor of the House, which
also opens it to supplementary questions from other members in real time &mdash; the government has to defend the number, not just table it. An unstarred
question gets a written answer laid on the table with no floor debate. Of the {fmt(tot)} questions here, {st} were starred ({st_ls} of {fmt(n_ls)} in the
Lok Sabha, {st_rs} of {fmt(n_rs)} in the Rajya Sabha). Oral slots are scarce, so a scheme that keeps attracting them is, by revealed preference, a live
political concern rather than a routine ask.
</p>

<p class="note" style="border-top:none;margin-top:0">
<strong>What this registry is for, on this blog specifically.</strong> Like the Quarterly Reportage, this isn&rsquo;t a standalone reference &mdash; it&rsquo;s
the search index this blog&rsquo;s own articles use to find the parliamentary reply behind a disbursement figure. A scheme&rsquo;s announced outlay is usually
easy to find in a PIB release; how much of it has actually reached beneficiaries is, far more often, buried in a written Lok Sabha or Rajya Sabha answer.
Where an article here cites a specific answer date, question number or minister for a disbursement figure, it was very likely found through this same
subject-line classification rather than read directly off sansad.in.
</p>

<p class="note" style="border-top:none;margin-top:0"><em>This page was built with AI assistance from the public sansad.in and rsdoc.nic.in question
indexes linked above. AI-generated text can misstate figures even when working from real source material &mdash; verify any number that matters to a
decision against the linked answer PDF.</em></p>

'''
t = t[:m1] + notes + t[m2:]

# what would fix this: both Secretariats
rep("<li><b>The Lok Sabha Secretariat should make the full text of answers searchable on sansad.in, not only the subject line</b>",
    "<li><b>The Lok Sabha and Rajya Sabha Secretariats should make the full text of answers searchable on sansad.in, not only the subject line</b>")
rep("<li><b>The Lok Sabha Secretariat should publish a bulk, machine-readable download of every question and answer &mdash; number, date, ministry, member, subject, starred or unstarred, and answer text &mdash; for the 17th and 18th Lok Sabha</b>",
    "<li><b>The two Secretariats should publish a bulk, machine-readable download of every question and answer &mdash; number, date, ministry, member, subject, starred or unstarred, and answer text &mdash; for the 17th and 18th Lok Sabha and the matching Rajya Sabha sessions</b>")
rep("<li><b>The Lok Sabha Secretariat should tag each question with the government schemes it concerns",
    "<li><b>Both Secretariats should tag each question with the government schemes it concerns")
# related: add the Most Discussed Schemes analysis
rep("ranking every party by focus rather than volume; see that piece's own scope note on why its totals are larger than this registry's.</div>",
    "ranking every party by focus rather than volume; see that piece's own scope note on why its totals are larger than this registry's. "
    "<a href=\"https://masaladeutsch.blogspot.com/2026/08/the-most-discussed-schemes-in.html\">The Most Discussed Schemes in Parliament</a> &mdash; the analysis "
    "this registry feeds.</div>")
assert "rajya-sabha-question-registry-scheme" not in t
OUT.write_text(t)
print(f"rows {len(rows)} (LS {n_ls}, RS {n_rs}); starred {st}; UDAN {ud}; data {len(js_data):,} chars; page {len(t):,} chars -> {OUT}")
