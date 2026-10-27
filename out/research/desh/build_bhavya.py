import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-bhavya-industrial-parks.html'

# ---------------------------------------------------------------- data
OUTLAY_CR = 33660
PARKS = 100
ACRES = 34000
JOBS = 15_00_000
HA_PER_ACRE = 0.404686
BHAVYA_HA = ACRES * HA_PER_ACRE
IILB_PARKS, IILB_HA, IILB_AVAIL_HA = 4523, 7.70e5, 1.35e5      # India Industrial Land Bank, 23 Dec 2025 (PIB)
IILB_PLOTS, IILB_VACANT = 6.45e5, 1.25e5
SHARE_OF_AVAIL = BHAVYA_HA / IILB_AVAIL_HA * 100
assert round(BHAVYA_HA) == 13759 and round(SHARE_OF_AVAIL) == 10

# State comparison. Proposals: first round, closed 31 Jul 2026 (87 in all; only the top six were reported).
# Pending: this blog's IEM analysis, Part A filed minus Part B implemented, 2020-2025, Rs crore.
# Idle SEZs: Lok Sabha reply, 31 Jul 2026 (only the top five states were reported).
STATES = [  # state, proposals (None = not among the six reported), pending Rs cr, idle SEZs (None = not among the five reported)
    ("Maharashtra", 14, 454589, None),
    ("Karnataka", None, 312828, 11),
    ("Odisha", None, 232433, None),
    ("Telangana", None, 65501, 12),
    ("Madhya Pradesh", 11, 57617, None),
    ("Tamil Nadu", 7, 51463, 9),
    ("Haryana", None, 30823, 14),
    ("Uttar Pradesh", 7, 24909, 9),
    ("Andhra Pradesh", 6, 23909, None),
    ("Gujarat", 6, -277616, None),
]
REPORTED = sum(p for _, p, _, _ in STATES if p)
assert REPORTED == 51


def chart_land():
    W, L, top, bh, gap, lab = 400, 10, 24, 18, 9, 196
    rows = [("Industrial park land mapped (IILB)", IILB_HA / 1e5, "#495057"),
            ("Of which available now", IILB_AVAIL_HA / 1e5, "#1c5d99"),
            ("BHAVYA, 100 parks by 2031-32", BHAVYA_HA / 1e5, "#a5402c")]
    H = top + len(rows) * (bh + gap) + 22
    sc = (W - L - lab - 44) / 8
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Industrial park land in lakh hectares: 7.70 mapped in the India Industrial Land Bank, 1.35 available, and 0.14 planned under BHAVYA.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Industrial park land, lakh hectares</text>']
    for i, (n, v, col) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{max(v * sc, 1.5):.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 13}" font-size="10" fill="#212529">{v:.2f}</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">IILB: 4,523 parks, 23 Dec 2025 (PIB). BHAVYA: 34,000 acres (Cabinet, Mar 2026).</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_states():
    W, L, top, bh, gap, lab = 400, 10, 30, 16, 8, 104
    rows = [r for r in STATES if r[2] > 0]
    H = top + len(rows) * (bh + gap) + 34
    sc = (W - L - lab - 92) / 470000
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Filed but unbuilt industrial investment by state, 2020 to 2025, with BHAVYA first-round proposals where reported.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Factory investment filed but not yet built, 2020&ndash;2025</text>',
         f'<text x="{L}" y="24" font-size="9.5" fill="#6c757d">Rs thousand crore; label shows BHAVYA first-round proposals</text>']
    for i, (n, p, pend, idle) in enumerate(rows):
        y = top + i * (bh + gap)
        col = "#1c5d99" if p else "#868e96"
        s.append(f'<text x="{L + lab - 6}" y="{y + 12}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{pend * sc:.1f}" height="{bh}" fill="{col}"/>')
        tag = f"{pend / 1000:,.0f} &middot; {p} proposals" if p else f"{pend / 1000:,.0f} &middot; not in top six"
        s.append(f'<text x="{L + lab + pend * sc + 4:.1f}" y="{y + 12}" font-size="9.5" fill="#212529">{tag}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Pending = IEM Part A filed minus Part B implemented (DPIIT), this blog&rsquo;s analysis.</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Proposals: 87 in round one; only the six largest states were reported.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_scheme():
    return table(["Feature", "BHAVYA (Bharat Audyogik Vikas Yojna)"], [
        ("Approved; notified", "Union Cabinet, 18 March 2026; notified 10 April 2026"),
        ("Outlay and period", "Rs 33,660 crore, central sector scheme, 2026-27 to 2031-32"),
        ("Parks", "100 plug-and-play parks; 50 in phase one, chosen in two rounds by challenge"),
        ("Size", "100 to 1,000 acres; from 25 acres in hill and north-eastern states, union territories and small states; greenfield or eligible brownfield"),
        ("Central support", "Up to Rs 1 crore an acre for core, value-added and social infrastructure (such as worker housing); up to 25% of support may go to external links such as roads and rail"),
        ("Who builds", "National Industrial Corridor Development Corporation (NICDC) with states and private developers"),
        ("Targets", "34,000 acres of investment-ready land and 15 lakh direct jobs by 2031-32"),
        ("Round one", "1 June &ndash; 31 July 2026: 87 proposals, up to 20 to be selected"),
        ("Round two", "1 August &ndash; 30 September 2026"),
    ])


def t_record():
    return table(["Earlier programme", "What it set out to do", "Where it stood in 2026"], [
        ("Special Economic Zones (SEZ Act, 2005)", "Duty-free export enclaves", "372 notified; 95 not operating on 31 July 2026"),
        ("Industrial corridors (NICDC), first cities from 2014; 12 more approved 2024", "Greenfield industrial cities with trunk infrastructure", "469 plots on about 5,348 acres allotted across the programme (report, 2026); in Dholera, 504 acres allotted and 1,083 acres of industrial land ready (May 2026)"),
        ("PM MITRA textile parks, approved 2021", "7 large textile parks, about Rs 4,445 crore of central support", "Virudhunagar (Tamil Nadu): 190 acres allotted to 23 investors in February 2026, completion targeted for December 2027; states had spent Rs 565 crore across the parks by February 2026"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>Rs 33,660 cr</b><span>for 100 ready-to-occupy industrial parks by 2031-32, about Rs {OUTLAY_CR / PARKS:.0f} crore a park</span></div>
<div class="gb-stat"><b>34,000 acres</b><span>of land planned under BHAVYA, about {SHARE_OF_AVAIL:.0f}% of the 1.35 lakh hectares already available in mapped parks</span></div>
<div class="gb-stat"><b>1.25 lakh</b><span>vacant plots in India&rsquo;s 4,523 mapped industrial parks (December 2025)</span></div>
<div class="gb-stat"><b>87</b><span>park proposals from states in the first round; up to 20 will be chosen</span></div>
</div>'''

body = f"""
{stats}

<p>The Union Budget of July 2024 promised &ldquo;plug and play&rdquo; industrial parks in or near 100 cities, built with the states and private developers. In March 2026 the Cabinet turned that into the Bharat Audyogik Vikas Yojna, BHAVYA: Rs 33,660 crore over six years to build 100 parks where a manufacturer can lease a plot that already has roads, power, water, effluent treatment and worker housing. States sent 87 proposals in the first round, which closed on 31 July, and a second round closed on 30 September. The first selections are due within a year of the scheme&rsquo;s notification in April.</p>
<p>The scheme&rsquo;s premise is that India lacks industrial land that is ready to use. The government&rsquo;s own land bank shows it does not lack industrial land as such: its mapped industrial parks already have 1.35 lakh hectares available and more than 1.25 lakh vacant plots. This piece sets out what BHAVYA offers, how it compares with the land already on the map, where states are proposing parks against where factory investment is actually waiting, and what earlier park programmes suggest about delivery.</p>

<h2 class="gb-h2">What the scheme offers</h2>
{t_scheme()}
<p>The arithmetic is simple. At up to Rs 1 crore an acre, 34,000 acres would use almost exactly the Rs 33,660 crore outlay, so the average park would be about 340 acres and cost the Centre about Rs {OUTLAY_CR / PARKS:.0f} crore. The jobs target works out to about {JOBS / ACRES:.0f} direct jobs an acre, or about Rs {OUTLAY_CR * 1e7 / JOBS / 1e5:.2f} lakh of central money per job. Those are the government&rsquo;s targets, not results.</p>

<h2 class="gb-h2">Land is not what is missing</h2>
{chart_land()}
<p>The India Industrial Land Bank, the government&rsquo;s map of industrial parks, listed 4,523 parks on about 7.70 lakh hectares in December 2025, with 1.35 lakh hectares available for industry and 1.25 lakh of 6.45 lakh plots vacant. BHAVYA&rsquo;s 34,000 acres is about {BHAVYA_HA:,.0f} hectares: about {SHARE_OF_AVAIL:.0f}% of the land already available and under 2% of all mapped park land.</p>
<p>So the case for BHAVYA has to rest on quality, not quantity. Much of the available land sits in older state estates without dependable power, water, effluent treatment or connections to ports and highways, which is the gap &ldquo;plug and play&rdquo; is meant to close. That is a reasonable bet, but it means the test of the scheme is not how many acres it adds. It is whether its parks fill faster than the parks that already exist, and the land bank does not yet publish occupancy over time in a way that would show it.</p>

<h2 class="gb-h2">Where states want parks, and where investment is waiting</h2>
{chart_states()}
<p>This blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/where-indias-factories-actually-get.html">analysis of DPIIT&rsquo;s industrial filings</a> measures demand directly. Large manufacturers file an Industrial Entrepreneurs Memorandum (IEM) when they plan a project (Part A) and again when it is built (Part B). Filed but unbuilt investment in 2020&ndash;2025 was largest in Maharashtra (Rs 4.55 lakh crore), Karnataka (Rs 3.13 lakh crore) and Odisha (Rs 2.32 lakh crore).</p>
<p>The first-round proposals line up only partly. Maharashtra leads both lists, with 14 proposals. Madhya Pradesh sent the second most, 11, against a much smaller backlog of about Rs 58,000 crore. Karnataka and Odisha, the second and third largest backlogs, were not among the six states whose proposal counts were reported, which means each sent five or fewer. Gujarat, with six proposals, is building faster than it files: its implemented investment in the period exceeded its filings by about Rs 2.78 lakh crore, as earlier projects came through.</p>
{table(["State", "BHAVYA round-one proposals", "Filed but unbuilt investment, 2020&ndash;25 (Rs crore)", "Idle SEZs, 31 Jul 2026"],
       [(n, str(p) if p else "5 or fewer", f"{pend:,}" if pend > 0 else f"&minus;{abs(pend):,} (building ahead of filings)", str(idle) if idle else "&mdash;") for n, p, pend, idle in STATES])}
<p class="gb-note">Only the six largest proposal counts and the five largest idle-SEZ counts were reported; a dash means the state was not among them, not that it has none. Filed-but-unbuilt investment is the difference between Part A and Part B filings in the period, so it approximates rather than measures the backlog; IEMs cover only large manufacturing projects.</p>
<p>Two things stand out. Haryana, Telangana and Karnataka already have the most notified SEZs that are not operating (14, 12 and 11), which is a reason to ask what a new park would do there that an idle zone cannot. And a proposal count measures states&rsquo; appetite for central money as much as demand from industry; the scheme&rsquo;s scoring on connectivity, site suitability and the industrial ecosystem is where demand should count.</p>

<h2 class="gb-h2">What earlier park programmes suggest</h2>
{t_record()}
<p>The pattern is slow filling, not a lack of approvals. The industrial corridor programme, which BHAVYA&rsquo;s implementer NICDC also runs, has allotted about 5,348 acres in total across its cities, against BHAVYA&rsquo;s target of 34,000 acres in six years. When the corridor programme&rsquo;s apex monitoring body reviewed BHAVYA in August, the Finance Minister said the focus must move beyond approvals to completing infrastructure, allotting land, attracting investment and starting production. That is the right test, and it is not one the scheme&rsquo;s published targets yet measure.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The India Industrial Land Bank should publish, for each park, vacant plots and hectares at the end of every quarter, so that occupancy in BHAVYA parks can be compared with existing parks over time.</li>
<li>DPIIT should publish every BHAVYA proposal and its evaluation score, not only those selected, so states&rsquo; proposals can be compared with demand.</li>
<li>For each selected park, NICDC should report land allotted, investment committed, units in production and jobs every six months, against the scheme&rsquo;s own targets.</li>
<li>Where a state proposes a BHAVYA park, it should also report the occupancy of its existing state industrial estates and any idle SEZs within the same district.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The Cabinet release, the scheme guidelines and the land bank&rsquo;s pages could not be opened directly; figures come from their text as indexed by search engines and from news reports. Proposal counts for states outside the top six, the second round&rsquo;s results and any selections had not been published by 27 October 2026. The corridor programme&rsquo;s programme-wide allotment figure comes from a single, undated report.</p>
"""

sources = ("BHAVYA: Cabinet decision of 18 March 2026 (PIB; PM India), as reported by Business Today, Forbes India, The Tribune, Upstox and NBM&amp;CW; notification date 10 April 2026 and scheme details per PIB-based summaries; DPIIT operational guidelines (May 2026) via Devdiscourse, Fibre2Fashion and Goodreturns; first-round proposals (87; Maharashtra 14, Madhya Pradesh 11, Uttar Pradesh 7, Tamil Nadu 7, Andhra Pradesh 6, Gujarat 6) per PTI via Punjab Kesari, The Pioneer and Swarajya (August 2026); NICDIT Apex Monitoring Authority review (August 2026). "
           "Budget 2024-25 announcement of plug-and-play parks in or near 100 cities: Deccan Herald, Vision IAS, KPMG. "
           "India Industrial Land Bank figures (4,523 parks, 7.70 lakh ha, 1.35 lakh ha available, 6.45 lakh plots, 1.25 lakh vacant): PIB, &ldquo;Industrial Parks Facilitating Smarter Infrastructure and Stronger Industrial Growth&rdquo; (23 December 2025). "
           "NICDC: report dated 31 May 2026 (nicdc.in) for Dholera and Shendra-Bidkin; programme-wide allotment (469 plots, about 5,348 acres) per Equitypandit. PM MITRA: ANI and Fibre2Fashion (Virudhunagar, February 2026); programme figures per a February 2026 summary; outlay per the 2021 Cabinet approval (Business Standard). "
           "SEZ status: Ministry of Commerce and Industry Lok Sabha reply (31 July 2026), as reported by PSUWatch. Filed and implemented investment: this blog&rsquo;s analysis of DPIIT IEM Parts A and B, 2020&ndash;2025. "
           "Per-acre, per-park and per-job figures and the land shares are this blog&rsquo;s arithmetic. Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/where-indias-factories-actually-get.html", "Where India&rsquo;s Factories Actually Get Built &mdash; IEM State &amp; Sector Analysis"),
    ("https://masaladeutsch.blogspot.com/2026/09/a-textile-sez-built-to-re-employ-mill.html", "A Textile SEZ Built to Re-Employ Mill Workers Has Shrunk 87% Since 2007"),
    ("https://masaladeutsch.blogspot.com/2026/09/where-indias-fdi-actually-lands-state.html", "Where India&rsquo;s FDI Actually Lands: 24 Quarters of DPIIT&rsquo;s Own State-and-District Data"),
]

build("Industrial Policy · 27 October 2026",
      "India Will Spend Rs 33,660 Crore on Ready-Made Factory Parks. Its Existing Parks Have 1.25 Lakh Empty Plots",
      "BHAVYA, approved in March, will fund 100 plug-and-play industrial parks by 2031-32. The land it adds is about a tenth of what mapped parks already have available, so its test is whether its parks fill faster. The first proposals come mostly from states other than those where factory investment is waiting.",
      body, sources, related, OUT)
print("ha", round(BHAVYA_HA), "share", round(SHARE_OF_AVAIL, 1), "per park", OUTLAY_CR / PARKS, "jobs/acre", round(JOBS / ACRES), "lakh per job", round(OUTLAY_CR * 1e7 / JOBS / 1e5, 2))
