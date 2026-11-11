import json,re,sys
ROOT='/home/user/blogger_writeups_code/'
SP='/tmp/claude-0/-home-user--github/bf61733e-4e03-51c3-9ac3-07a35af41a6a/scratchpad/'
t=open(ROOT+'posts/indias-wholesale-prices-next-to.html').read()
fy=open(ROOT+'posts/fourteen-years-of-indian-wholesale.html').read()
data=json.load(open(SP+'wpi_data.json')); cpi=data['cpi']; D=data['D']
FY_URL='https://masaladeutsch.blogspot.com/2026/08/fourteen-years-of-indian-wholesale.html'
def rep(s,a,b,n=1):
    c=s.count(a)
    assert c==n,(c,a[:80]); return s.replace(a,b)

# ---------- 1. 10 Nov note ----------
note=('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px">'
'<b>Updated 10 November 2026.</b> This page now carries two earlier posts from this blog, which have been retired: '
'<i>Fourteen Years of Indian Wholesale Prices</i> (the April 2012 to April 2026 commodity record and three corrections) and '
'<i>CPI &amp; WPI Trends &mdash; India</i> (the state-wise consumer price panel and the full WPI history). '
'Their content is in the sections from <a href="#fourteen-years">Fourteen years at home</a> onward. '
'The latest prints are newer than any table below. Wholesale inflation was <b>11.39% in September 2026</b> (provisional, released 14 October; index 112.5 on the 2022-23 base), after 9.78% in July (final) and 9.92% in August. '
'In September Fuel &amp; Power eased to 25.85%, while Manufactured Products rose to 9.76% and Primary Articles to 8.67%, so the rise is now broader than fuel. '
'All-India consumer inflation (CPI, base 2024) was <b>5.54% in September 2026</b> (index 109.49), with Tamil Nadu the hottest tracked state at 6.81% and Delhi the coolest at 3.40%, according to MoSPI&rsquo;s data service. '
'Sources: <a href="https://www.devdiscourse.com/article/business/3992075-wpi-inflation-climbs-to-1139-in-september-from-992-in-august">Devdiscourse</a>, '
'<a href="https://www.psuconnect.in/news/wpi-inflation-rises-to-11-39-in-september-2026">PSU Connect</a>, '
'<a href="https://www.deccanherald.com/business/wholesale-inflation-surges-to-1139-in-september-4183260">Deccan Herald</a>.</div>\n')
anchor='<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px"><b>Updated 22 October 2026.</b>'
t=rep(t,anchor,note+anchor)

# ---------- 2. repoint links to the absorbed post ----------
t=rep(t,'Applying the rule of 72 used in <a href="'+FY_URL+'">the earlier wholesale piece</a>',
        'Applying the rule of 72 used in <a href="#doubling">the fourteen-year section below</a>')
t=rep(t,'The Office of the Economic Adviser index file used in this blog&rsquo;s earlier wholesale-price piece gives',
        'The Office of the Economic Adviser index file used in the fourteen-year section below gives')
t=rep(t,'so it is not identical to the number in <a href="'+FY_URL+'">Fourteen Years of Indian Wholesale Prices</a>, which used the OEA file throughout.',
        'so it is not identical to the 8.69% in <a href="#fourteen-years">the fourteen-year record below</a>, which uses the OEA file throughout.')
assert FY_URL not in t

# ---------- 3. absorbed sections ----------
# fourteen-years SVG figure (verbatim)
svg=re.search(r'<figure class="gb-figure".*?</figure>',fy,re.S).group(0)
# take the body block from "Three corrections" to the wpi-note paragraph end
a=fy.index('<h2>Three corrections we owe our own earlier posts</h2>')
b=fy.index('<p class="wpi-note">')
body=fy[a:b]
body=body.replace('<div class="wpi-fix">','<div class="note">').replace('<div class="wpi-key">','<div class="note">').replace('<p class="wpi-fix">','<p class="note">')
assert 'wpi-' not in body, re.findall(r'wpi-\w+',body)
FERT='<a href="https://masaladeutsch.blogspot.com/2026/08/imported-fertiliser-fuel-prices-diesel.html">fertiliser-and-fuel post</a>'
body=rep(body,'The fertiliser-and-fuel post said','The '+FERT+' said')
# headings -> gpx kicker + h2sub, with ids
H={'<h2>Three corrections we owe our own earlier posts</h2>':('corrections','Three corrections','Owed to this blog&rsquo;s own earlier posts.'),
 '<h2>The rebasing, and why you cannot just draw one long line</h2>':('rebasing','The rebasing','Why you cannot just draw one long line.'),
 '<h2>Fourteen years, April to April, on the 2011-12 base</h2>':('april-to-april','Fourteen years, April to April','Index levels on the 2011-12 base.'),
 '<h2>The doubling test: 72 divided by the rate</h2>':('doubling','The doubling test','72 divided by the rate.'),
 '<h2>The calm is an average, not a description of today</h2>':('calm-is-an-average','The calm is an average','Not a description of today.'),
 '<h2>Where things stand on the current 2022-23 base</h2>':('current-base','The current 2022-23 base','Where things stand now.')}
for k,(i,h,sub) in H.items():
    body=rep(body,k,'<h2 id="%s">%s</h2>\n<p class="h2sub">%s</p>'%(i,h,sub))
# tables: add thead/tbody
def fix_table(m):
    tb=m.group(0)
    rows=re.findall(r'<tr>.*?</tr>',tb,re.S)
    return '<table>\n<thead>'+rows[0]+'</thead>\n<tbody>\n'+'\n'.join(rows[1:])+'\n</tbody>\n</table>'
body=re.sub(r'<table>.*?</table>',fix_table,body,flags=re.S)
# add Sept 2026 column to current-base table
sep={'All Commodities':'+11.39','Primary Articles':'+8.67','Fuel &amp; Power':'+25.85','Manufactured Products':'+9.76'}
cb=body.index('<h2 id="current-base">'); seg=body[cb:]
seg=rep(seg,'<th>Since Apr 2023, %</th></tr></thead>','<th>Since Apr 2023, %</th><th>YoY Sep 2026, % (provisional)</th></tr></thead>')
def addsep(m):
    name=m.group(1); return m.group(0)[:-5]+'<td>'+sep.get(name,'&mdash;')+'</td></tr>'
seg=re.sub(r'<tr><td>([^<]+)</td>(?:<td>[^<]*</td>){3}</tr>',addsep,seg,count=8)
seg=rep(seg,'<p>June 2026, index and year-on-year rate (YoY computed from the index and cross-checked against the published release):</p>',
 '<p>June 2026, index and year-on-year rate (YoY computed from the index and cross-checked against the published release), with the September 2026 rates as reported for the four headline series. The September item-level rates for food, diesel, urea and DAP were not in the coverage used here:</p>')
body=body[:cb]+seg

stats=('<div class="stats">\n'
'<div class="stat"><b>+79.0%</b><span>Diesel (HSD), April 2012 to April 2026, WPI 2011-12 base</span></div>\n'
'<div class="stat"><b>+13.8%</b><span>Urea over the same fourteen years &mdash; the subsidy absorbs the border price</span></div>\n'
'<div class="stat"><b>11.39%</b><span>Headline WPI inflation, September 2026 (provisional), 2022-23 base</span></div>\n'
'<div class="stat"><b>25.85%</b><span>Fuel &amp; Power, September 2026 &mdash; down from 27.41% in June, still the largest driver</span></div>\n'
'</div>\n')
intro=('<h2 id="fourteen-years">Fourteen years at home</h2>\n<p class="h2sub">The domestic record, April 2012 to June 2026.</p>\n'
'<p>The international view above uses India&rsquo;s April prints. This section takes the full record from the publisher itself, the Office of the Economic Adviser, commodity by commodity. In June 2026 headline WPI inflation was <b>9.87%</b> on an All-Commodities index of 110.2, up from 9.68% in May. Fuel &amp; Power inflation was <b>27.41%</b>, Primary Articles 7.00% and Manufactured Products 7.48%. The Office named the drivers: mineral oils (petroleum products), food articles, basic metals and chemicals. By September the headline rate had reached 11.39%, and the rise had spread beyond fuel.</p>\n'
+stats+svg.replace('<figure class="gb-figure" style="margin:1.5rem 0 1.75rem;text-align:center">','<figure class="gb-figure exhibit" style="margin:1.5rem 0 1.75rem;text-align:center">')+'\n')

# ---------- 4. state CPI + full WPI history ----------
order=sorted(cpi,key=lambda k:-(cpi[k][17]/cpi[k][5]-1))
rows=[]
for k in order:
    v=cpi[k]; yoy=(v[17]/v[5]-1)*100
    nm='Delhi' if k=='NCT of Delhi' else k
    cls=' class="hl"' if k=='All India' else ''
    rows.append('<tr%s><td>%s</td><td>%.2f</td><td>%.2f</td><td>%.2f</td></tr>'%(cls,nm,yoy,v[5],v[17]))
cpitab=('<div class="exhibit">\n<p class="exno">State consumer prices</p>\n<p class="extitle">Telangana, Andhra Pradesh and Tamil Nadu ran hottest; Delhi coolest</p>\n'
'<p class="exsub">Consumer Price Index, base 2024 = 100, thirteen states and the all-India benchmark, ranked by June 2026 year-on-year inflation.</p>\n'
'<div class="tw">\n<table>\n<thead><tr><th>State</th><th>YoY Jun 2026, %</th><th>Index, Jun 2025</th><th>Index, Jun 2026</th></tr></thead>\n<tbody>\n'
+'\n'.join(rows)+'\n</tbody>\n</table>\n</div>\n'
'<p class="exsrc">MoSPI, Consumer Price Index (base 2024), combined, state-wise, retrieved through MoSPI&rsquo;s data service on 18 July 2026. Year-on-year rates are the author&rsquo;s calculation on the index. By September 2026 the all-India rate was 5.54%, Tamil Nadu 6.81% and Delhi 3.40%; the full state panel for September was not refreshed.</p>\n</div>\n')

# full-history SVG
W=560; pl=48; pr=16; N=len(D['oldIdx']); pw=W-pl-pr
off=D['oldLabels'].index(D['newLabels'][0])
X=lambda i: pl+i/(N-1)*pw
t1,h1,lo1,hi1=86,170,95,215
y1=lambda v: t1+h1-(v-lo1)/(hi1-lo1)*h1
t2,h2,lo2,hi2=322,170,-8,34
y2=lambda v: t2+h2-(v-lo2)/(hi2-lo2)*h2
def path(vals,start,y):
    d='';on=False
    for i,v in enumerate(vals):
        if v is None: on=False; continue
        d+=('L' if on else 'M')+'%.1f,%.1f '%(X(start+i),y(v)); on=True
    return d.strip()
g=[]
g.append('<rect x="0" y="0" width="560" height="560" fill="#f8f9fa" />')
g.append('<text x="16" y="30" font-size="20" font-weight="bold" fill="#1a1a1a">India&#8217;s WPI, April 2012 to June 2026</text>')
g.append('<text x="16" y="52" font-size="14" fill="#595959" font-style="italic">Levels do not splice across the rebasing; rates do.</text>')
g.append('<text x="%d" y="%d" font-size="14" fill="#1a1a1a" font-weight="bold">Index level</text>'%(pl,t1-6))
for v in (100,125,150,175,200):
    g.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#dde1e6" stroke-width="1" />'%(pl,W-pr,y1(v),y1(v)))
    g.append('<text x="%d" y="%.1f" font-size="13" fill="#595959" text-anchor="end">%d</text>'%(pl-6,y1(v)+4,v))
g.append('<path d="%s" fill="none" stroke="#0b5794" stroke-width="2" />'%path(D['oldIdx'],0,y1))
g.append('<path d="%s" fill="none" stroke="#8a4b08" stroke-width="2" stroke-dasharray="5 3" />'%path(D['newIdx'],off,y1))
g.append('<text x="%.1f" y="%.1f" font-size="13" fill="#0b5794" text-anchor="end">2011-12 base: 167.6</text>'%(X(N-1)-4,y1(167.6)-12))
g.append('<text x="%.1f" y="%.1f" font-size="13" fill="#8a4b08" text-anchor="end">2022-23 base: 110.2</text>'%(X(off)-6,y1(100)+4))
g.append('<text x="%d" y="%d" font-size="14" fill="#1a1a1a" font-weight="bold">Year-on-year inflation, %%</text>'%(pl,t2-6))
for v in (-5,0,10,20,30):
    g.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="%s" stroke-width="1" />'%(pl,W-pr,y2(v),y2(v),'#888' if v==0 else '#dde1e6'))
    g.append('<text x="%d" y="%.1f" font-size="13" fill="#595959" text-anchor="end">%d%%</text>'%(pl-6,y2(v)+4,v))
g.append('<path d="%s" fill="none" stroke="#a5402c" stroke-width="2" />'%path(D['oldYoY'],0,y2))
g.append('<path d="%s" fill="none" stroke="#8a4b08" stroke-width="2" stroke-dasharray="5 3" />'%path(D['newYoY'],off,y2))
pk=max(range(N),key=lambda i: D['oldYoY'][i] or -99)
g.append('<text x="%.1f" y="%.1f" font-size="13" fill="#a5402c" text-anchor="middle">%.1f%%, %s</text>'%(X(pk),y2(D['oldYoY'][pk])-8,D['oldYoY'][pk],D['oldLabels'][pk].replace(' ',' 20')))
for i in range(0,N,48):
    lab='20'+D['oldLabels'][i][-2:]
    anc='start' if i==0 else 'middle'
    for yy in (t1+h1+18,t2+h2+18):
        g.append('<text x="%.1f" y="%d" font-size="13" fill="#595959" text-anchor="%s">%s</text>'%(X(i),yy,anc,lab))
for yy in (t1+h1+18,t2+h2+18):
    g.append('<text x="%.1f" y="%d" font-size="13" fill="#595959" text-anchor="end">2026</text>'%(X(N-1),yy))
g.append('<text x="16" y="534" font-size="12.5" fill="#595959">Solid: 2011-12 base, Apr 2012&#8211;Apr 2026. Dashed: 2022-23 base,</text>')
g.append('<text x="16" y="551" font-size="12.5" fill="#595959">Apr 2023&#8211;Jun 2026. Source: Office of the Economic Adviser, DPIIT.</text>')
fsvg=('<figure class="gb-figure exhibit" style="margin:1.5rem 0 1.75rem;text-align:center">\n'
'<svg role="img" aria-label="India WPI index level and year-on-year inflation, April 2012 to June 2026, on both base years" style="width:100%;height:auto;max-width:640px;display:block;margin:0 auto" viewBox="0 0 560 560" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Helvetica, Arial, sans-serif">\n'
+'\n'.join(g)+'\n</svg>\n'
'<figcaption style="font-size:.8em;color:#868e96;font-family:-apple-system,\'Segoe UI\',sans-serif;margin-top:.5rem">A decade of near-zero wholesale inflation, then the 2021&ndash;22 spike, a dip below zero in 2023, and the 2026 turn. Year-on-year rates are computed from the index and match the published rates to the second decimal.</figcaption>\n</figure>\n')

fullsec=('<h2 id="full-history">The full WPI history</h2>\n<p class="h2sub">Both base years, every month, April 2012 to June 2026.</p>\n'
'<p>The tables above sample April. The chart below draws every month on both bases. The two index lines sit at different heights because a rebasing resets the index to 100 on a new basket; the two inflation lines can be read across the break. The peak on the 2011-12 base came in May 2022. Inflation then went below zero from April to October 2023 and turned up sharply in 2026: 8.69% in April 2026 on the old base, and 8.36%, 9.68% and 9.87% for April, May and June on the new one.</p>\n'
+fsvg+
'<h2 id="state-cpi">Consumer prices by state</h2>\n<p class="h2sub">No state WPI exists; state CPI does.</p>\n'
'<p>WPI is compiled nationally only, so the state picture has to come from the consumer side. MoSPI&rsquo;s state-wise CPI on the 2024 base shows the south running hottest. Telangana, Andhra Pradesh and Tamil Nadu were the only tracked states above 5% in June 2026, against 4.38% for all-India. Delhi was lowest at 2.96%. By September all-India had risen to 5.54% and Tamil Nadu led at 6.81%.</p>\n'
+cpitab+
'<div class="note"><b>Two caveats on the state series.</b> CPI year-on-year inflation can only be computed from January 2026 onward on the 2024 base, because that series has no 2024 comparison months. The rates above therefore compare June 2026 with June 2025 on the new base. They are not spliced to the older series. Treat any single-month move within a state as provisional until it is revised.</div>\n')

new_block=intro+body+fullsec
t=rep(t,'<p class="sources"><b>Sources.</b>',new_block+'\n<p class="sources"><b>Sources.</b>')

# ---------- 5. sources ----------
src_add=(' Fourteen-year record &mdash; Office of the Economic Adviser, DPIIT, Ministry of Commerce &amp; Industry, monthly WPI index files for base 2011-12 (April 2012 to April 2026) and base 2022-23 (April 2023 to June 2026), retrieved from eaindustry.nic.in on 5 August 2026; and the WPI press release for June 2026 (embargoed to 14 July 2026), which supplied the published inflation rates used to check the computed ones. Cumulative changes are computed from the published index levels; year-on-year rates are the index over its value twelve months earlier. September 2026 WPI &mdash; press coverage of the 14 October 2026 release (Devdiscourse, PSU Connect, Deccan Herald). State consumer prices &mdash; MoSPI, <i>Consumer Price Index</i>, base 2024, combined, state-wise, January 2025 to June 2026, retrieved through MoSPI&rsquo;s data service on 18 July 2026; September 2026 all-India and state rates from the same service on 26 October 2026.')
t=rep(t,' No figure on this page has been estimated, interpolated or extrapolated, and no figure is taken from a commercial data vendor.</p>',
      src_add+' No figure on this page has been estimated, interpolated or extrapolated, and no figure is taken from a commercial data vendor.</p>')

# ---------- 6. what would fix this ----------
old_ul=t[t.index('<h2>What would fix this</h2>\n<ul>'):]
old_ul=old_ul[:old_ul.index('</ul>')+5]
new_ul=('<h2>What would fix this</h2>\n<ul>\n'
'<li><b>The Office of the Economic Adviser in DPIIT should publish a domestic-output Producer Price Index alongside the WPI</b>, so India has a producer-side series built like the ones most peers use and comparisons with the US, euro area, Japan or Korea do not have to be hedged as related but different instruments.</li>\n'
'<li><b>The Office of the Economic Adviser should publish official linking factors between the 2011&ndash;12 and 2022&ndash;23 WPI bases for the all-commodities index and its major groups</b>, so users wanting one long series do not splice levels themselves and draw a cliff that does not exist in prices.</li>\n'
'<li><b>The Office of the Economic Adviser should add a year-on-year inflation column for every commodity row in its downloadable WPI index files, not just the headline groups</b>, so items like DAP and diesel can be quoted without a reader recomputing rates from index levels.</li>\n'
'<li><b>The Office of the Economic Adviser should flag each monthly WPI value as provisional or final in its files and publish a standing revision table with the weighted response rate</b>, so revisions such as April 2026&rsquo;s move from 8.26% to 8.36% are visible without comparing old press releases.</li>\n'
'<li><b>MoSPI should label every WPI value served through its statistical API as compiled by the Office of the Economic Adviser, DPIIT, with its vintage and provisional or final status, and update it when the Office revises</b>, so April 2026 does not read 167.0 in one official source and 167.6 in the other.</li>\n'
'<li><b>The Office of the Economic Adviser should publish official calendar-year average WPI inflation rates</b>, so international comparisons can use the same annual-average convention as other economies rather than an April-on-April anchor that does not match peers&rsquo; series.</li>\n'
'<li><b>MoSPI should publish a linking factor between the old CPI series and the 2024-base series for every state</b>, so state inflation can be computed for 2025 and not only from January 2026 onward.</li>\n'
'<li><b>MoSPI should show a last-updated date and the latest available period for every series served through its data API</b>, so users can see when a series lags; the foreign-exchange reserves series returned June 2025 when 2026 was requested.</li>\n'
'</ul>')
t=rep(t,old_ul,new_ul)

# ---------- 7. revised line ----------
t=rep(t,'<p class="revised" data-gs-revision-v1="1">Revised <time datetime="2026-08-08" itemprop="dateModified">8 August 2026</time> &middot; v6.0.0 &middot;',
      '<p class="revised" data-gs-revision-v1="1">Revised <time datetime="2026-11-10" itemprop="dateModified">10 November 2026</time> &middot; v7.0.0 &middot; absorbs the retired posts on fourteen years of Indian wholesale prices and on CPI and WPI trends &middot;')
for slug in ('cpi-wpi-trends-mospi-bulletin','fourteen-years-of-indian-wholesale'):
    assert slug not in t, slug
open(ROOT+'out/update-2026-11-10-indias-wholesale-prices-next-to.html','w').write(t)
print(len(t))
