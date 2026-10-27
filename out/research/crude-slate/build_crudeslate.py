import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-crude-slate.html'

# ---------------------------------------------------------------- data
# Indian Basket weighting (PPAC as reported by Business Standard, Apr 2026): share of Oman/Dubai (sour marker) vs Dated Brent (sweet marker)
BASKET = [("Until Feb 2026", 79, 21), ("From Mar 2026", 39, 61)]
OCT_SPLIT = (65.27, 34.73)          # Oct 2026 as reported by an exam-prep summary; which side is which not stated
# Russian crude into India, Kpler (million b/d) and share of imports
RUS = [("Jul 2026", 2.82, 55.9), ("Aug 2026", 2.08, None), ("Sep 2026", 1.82, 35.0)]
ME_SEP = 2.8                        # Middle East, Sep 2026, Reuters ship tracking
TOTAL_SEP = RUS[2][1] / (RUS[2][2] / 100)
RUS_ME_SHARE = (RUS[2][1] + ME_SEP) / TOTAL_SEP * 100
# US crude into India, Kpler via Indian Oil & Gas (thousand b/d)
US = [("Oct 2025", 565), ("Jan 2026", 295), ("Mar 2026", 165), ("Jul 2026", 125), ("Aug 2026", 75)]
US_DROP = (1 - US[-1][1] / US[0][1]) * 100
# Urals delivered India vs Dated Brent ($/bbl; negative = discount)
URALS = [("Feb-arrival cargoes (priced Jan 2026)", "about &minus;10"), ("March 2026", "above Dated Brent for the first time since Platts began assessing it in 2023"),
         ("Sep-arrival cargoes", "&minus;1 to &minus;2"), ("Oct-delivery offers (Aug 2026)", "up to +1")]
# Import bill (PPAC)
BASKET_PRICE = [("Sep 2025", 69.61), ("Aug 2026", 90.19), ("Sep 2026", 116.09)]
SEP_BILL, SEP_BILL_CHG, SEP_MT, SEP_MT_PREV = 15.4, 47, 21.7, 20.3
H1_BILL, H1_BILL_PREV, H1_MT, H1_MT_PREV, DEP = 90.6, 61.9, 122.7, 121.8, 88.1
VOL_CHG = (SEP_MT / SEP_MT_PREV - 1) * 100
PRICE_CHG = (BASKET_PRICE[2][1] / BASKET_PRICE[0][1] - 1) * 100
# Crude quality (assays as published): API gravity, sulphur wt%
GRADES = [("WTI Midland (US)", 41.67, 0.14, "WTI / Dated Brent", "Ceypetco assay annex"),
          ("Murban (UAE)", 40.5, 0.743, "Murban futures (Abu Dhabi)", "Ceypetco assay annex"),
          ("Urals (Russia)", 31.5, None, "Dated Brent", "Index summaries; published sulphur figures vary"),
          ("Basrah Medium (Iraq)", 27.9, 3.00, "Oman/Dubai (official selling price)", "Iraq SOMO spec via S&amp;P Global, 2020")]
def kg_per_bbl(api):
    sg = 141.5 / (131.5 + api)
    return sg * 158.987                 # kg of crude in one 159-litre barrel
S_KG = {g: kg_per_bbl(api) * s / 100 for g, api, s, _, _ in GRADES if s is not None}
H2_PER_T_S = 2.016 / 32.06 * 1000      # kg H2 per tonne S, to form H2S alone (stoichiometric floor)
RATIO = S_KG["Basrah Medium (Iraq)"] / S_KG["Murban (UAE)"]


def chart_basket():
    W, L, top, bh, gap, lab = 400, 10, 44, 24, 16, 96
    H = top + len(BASKET) * (bh + gap) + 30
    sc = (W - L - lab - 10) / 100
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Indian Basket weights: until February 2026, 79% Oman/Dubai and 21% Dated Brent; from March 2026, 39% Oman/Dubai and 61% Dated Brent.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">How the Indian Basket price is weighted, %</text>',
         f'<rect x="{L}" y="22" width="9" height="9" fill="#a5402c"/><text x="{L + 13}" y="30" font-size="9.5" fill="#212529">Oman/Dubai (sour marker)</text>',
         f'<rect x="{L + 160}" y="22" width="9" height="9" fill="#1c5d99"/><text x="{L + 173}" y="30" font-size="9.5" fill="#212529">Dated Brent (sweet marker)</text>']
    for i, (n, sour, sweet) in enumerate(BASKET):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 16}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        x = L + lab
        for v, col in ((sour, "#a5402c"), (sweet, "#1c5d99")):
            s.append(f'<rect x="{x:.1f}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
            s.append(f'<text x="{x + v * sc / 2:.1f}" y="{y + 16}" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">{v}</text>')
            x += v * sc
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">PPAC formula as reported by Business Standard (April 2026). The weights follow</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">how imports are priced, not how much sulphur they carry.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_flows():
    W, L, top, bh, gap, lab = 400, 10, 40, 15, 6, 92
    rows = [(f"Russia, {n}", v * 1000, "#a5402c") for n, v, _ in RUS] + [(f"US, {n}", v, "#1c5d99") for n, v in US]
    H = top + len(rows) * (bh + gap) + 30
    sc = (W - L - lab - 60) / 2900
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Crude imports into India from Russia, July to September 2026, and from the United States, October 2025 to August 2026, thousand barrels a day.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Crude into India from Russia and the US, thousand b/d</text>',
         f'<text x="{L}" y="26" font-size="9.5" fill="#6c757d">Tanker-tracking estimates (Kpler)</text>']
    for i, (n, v, col) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 11}" font-size="9.5" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{max(v * sc, 1.5):.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 11}" font-size="9.5" fill="#212529">{v:,.0f}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Russia: Kpler via Business Standard and Hellenic Shipping News; US: Kpler via</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Indian Oil &amp; Gas (August 2026). Monthly estimates, not customs data.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_grades():
    rows = []
    for g, api, s, ref, src in GRADES:
        sk = f"{S_KG[g]:.2f}" if s is not None else "&mdash;"
        rows.append((g, f"{api:.1f}" if g != "Urals (Russia)" else "about 31&ndash;32", f"{s:.2f}" if s is not None else "medium sour; figures vary", sk, ref))
    return table(["Grade", "API gravity", "Sulphur, % by weight", "Sulphur per barrel, kg", "Priced against"], rows)


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>61%</b><span>weight of Dated Brent, a sweet marker, in the Indian Basket since March 2026, up from 21%</span></div>
<div class="gb-stat"><b>~{RUS_ME_SHARE:.0f}%</b><span>of September&rsquo;s crude imports came from Russia and the Middle East, whose main grades are sour</span></div>
<div class="gb-stat"><b>&minus;{US_DROP:.0f}%</b><span>fall in US crude arriving in India between October 2025 and August 2026</span></div>
<div class="gb-stat"><b>${BASKET_PRICE[2][1]:.2f}</b><span>a barrel: Indian Basket in September 2026, against ${BASKET_PRICE[0][1]:.2f} a year earlier</span></div>
</div>'''

body = f"""
{stats}

<p>Exam-prep summaries in October reported the Indian Basket, the benchmark price of the crude India imports, at a ratio of about 65:35. It is easy to read that as two-thirds of India&rsquo;s crude now being sweet, low-sulphur oil. It is not. The basket is a price formula, and in March 2026 the Petroleum Planning and Analysis Cell (PPAC) changed it so that Dated Brent, the sweet benchmark, carries 61% of the weight instead of 21%. The reason was pricing, not chemistry: much of what India now buys, Russian Urals above all, is sour crude that is sold against Brent.</p>
<p>This piece follows this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/where-worlds-oil-sits-when-it-isnt.html">piece on oil storage and the Hormuz shock</a> and its <a href="https://masaladeutsch.blogspot.com/2026/08/petroleum-trade-pairings-and-us-crude.html">piece on petroleum trade pairings and US crude</a>. It sets out what the basket measures, how India&rsquo;s crude sources have moved in 2026, and what the physical mix means for refiners&rsquo; costs and the hydrogen they need to remove sulphur.</p>

<h2 class="gb-h2">The basket follows prices, not sulphur</h2>
{chart_basket()}
<p>Until February 2026 the basket weighted the Oman and Dubai average, the sour markers, at 79% and Dated Brent at 21%. Business Standard reported in April that the old formula had drifted from what refiners actually paid: under it the basket briefly reached about $156 a barrel during the Hormuz disruption, and Kpler data suggested more than half of India&rsquo;s imports were priced off Brent once Russian purchases surged. PPAC moved to 61% Brent and 39% Oman/Dubai from March. The October figure of {OCT_SPLIT[0]}:{OCT_SPLIT[1]} that circulated in exam-prep notes did not say which side was which; it is consistent with the new, Brent-heavy formula.</p>
<p>So a higher Brent weight means more of India&rsquo;s crude is <em>priced</em> like sweet crude. It does not mean more of it <em>is</em> sweet. Urals is a medium-sour crude, and Iraq&rsquo;s and Saudi Arabia&rsquo;s main grades are sour. On the usual definition, sweet crude has less than 0.5% sulphur; of the grades below, only US WTI Midland qualifies.</p>
{t_grades()}
<p class="gb-note">Sulphur per barrel is this blog&rsquo;s arithmetic from API gravity and sulphur content (a 159-litre barrel). Assays vary by cargo and over time; the Basrah figures are the 2020 specification.</p>

<h2 class="gb-h2">Where India&rsquo;s crude came from in 2026</h2>
{chart_flows()}
<p>India&rsquo;s sources swung twice this year. When the Strait of Hormuz came under attack from late February, refiners leaned on Russia, and Kpler put Russian crude at a record 2.82 million barrels a day in July, about 56% of imports. The discount that made those barrels attractive had already gone: Urals cargoes traded about $10 below Dated Brent in January, and in March Platts assessed Urals delivered to India above Dated Brent for the first time. As Gulf flows recovered and Chinese buyers competed for Russian oil, India&rsquo;s Russian intake fell to 2.08 million barrels a day in August and 1.82 million in September, about 35% of imports. Ship-tracking data reported by Reuters put Middle East arrivals at 2.8 million barrels a day in September, up 32% on August.</p>
{table(["Urals delivered to India against Dated Brent", "$ a barrel"], URALS)}
<p>Combining the two trackers, Russia and the Middle East supplied about {RUS_ME_SHARE:.0f}% of September&rsquo;s roughly {TOTAL_SEP:.1f} million barrels a day. US crude, the sweetest in the mix, went the other way: Kpler data show it falling from about 565,000 barrels a day in October 2025, when a wide Brent&ndash;WTI spread made it cheap, to about 75,000 in August 2026, a {US_DROP:.0f}% drop. Whatever the trade talks with Washington say about energy purchases, they had not shown up in tanker arrivals by August.</p>

<h2 class="gb-h2">What it costs</h2>
<p>PPAC&rsquo;s data show that the 2026 import bill is a price story. In September India imported {SEP_MT} million tonnes of crude, {VOL_CHG:.0f}% more than a year earlier, but paid ${SEP_BILL} billion, {SEP_BILL_CHG}% more, because the basket averaged ${BASKET_PRICE[2][1]:.2f} a barrel against ${BASKET_PRICE[0][1]:.2f} in September 2025, a rise of {PRICE_CHG:.0f}%. For April to September the bill was ${H1_BILL} billion against ${H1_BILL_PREV} billion, on almost the same volume ({H1_MT} against {H1_MT_PREV} million tonnes). Import dependence on a consumption basis was {DEP}%.</p>
<p>For refiners the margin case for Russian crude has narrowed from a $10 discount to roughly parity. Complex refineries can still gain from running heavier, sourer crude that sells at a discount to light sweet grades, but in 2026 that discount has come mostly from Gulf grades priced against Oman/Dubai rather than from Russia.</p>

<h2 class="gb-h2">What sour crude asks of a refinery</h2>
<p>Sulphur has to go somewhere. A barrel of Basrah Medium carries about {S_KG['Basrah Medium (Iraq)']:.1f} kg of sulphur, about {RATIO:.0f} times a barrel of Murban and far more than WTI Midland. Most of it ends up as hydrogen sulphide removed in hydrotreaters, as sulphur in heavy fuel and coke, or as recovered elemental sulphur. As this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/inside-refinery-how-hydrogen-cleans.html">piece on refinery hydrogen</a> explains, every litre of BS-VI diesel has to be brought down to 10 parts per million, using hydrogen made mostly from natural gas. Chemistry sets a floor: removing a tonne of sulphur as hydrogen sulphide consumes at least {H2_PER_T_S:.0f} kg of hydrogen, and real hydrotreaters use several times that because they also saturate other molecules.</p>
<p>That means a sourer slate raises hydrogen demand, sulphur-recovery load and catalyst wear, at the same time as India is asking refiners to replace part of their grey hydrogen with green hydrogen at about three times the cost. A slate that has stayed sour while being priced as if it were sweet carries a processing cost that the basket does not show.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>PPAC should publish, alongside the basket, the monthly physical slate of crude processed by Indian refineries: volume by origin, API gravity band and sulphur band.</li>
<li>The basket notes should state plainly that the weights reflect pricing benchmarks, so that a Brent-heavy formula is not read as a shift to sweet crude.</li>
<li>Refiners should report hydrogen consumption per tonne of crude processed and its sulphur content each year, so the cost of the slate shows up in the green-hydrogen debate.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>PPAC&rsquo;s own basket notes and India&rsquo;s customs data by grade could not be opened directly; the weights come from Business Standard&rsquo;s report of the March change and the October ratio from a secondary summary that did not label its sides. Russian and Middle East volumes come from different tanker trackers (Kpler and Reuters), so the combined share is approximate; one weekly tracker reported much lower Russian arrivals in late September, which this piece could not reconcile. The US series comes from a single report of Kpler data. No published figure for Indian refiners&rsquo; gross margins in the July&ndash;September quarter was found, so this piece does not estimate the margin effect. Assay figures vary by cargo, and no reliable sulphur figure for Urals was found.</p>
"""

sources = ("Indian Basket formula change: Business Standard (12 April 2026, &ldquo;Wars prompt India to change crude price basket formula&rdquo;), Angel One and Business Today (March 2026); October ratio per Drishti IAS (as indexed). "
           "Flows: Kpler data via Business Standard (17 October 2026), ETV Bharat (14 October 2026) and Hellenic Shipping News (September 2026); Middle East arrivals per Reuters ship tracking via EnergyNews (October 2026); US arrivals per Kpler via Indian Oil &amp; Gas (August 2026) and Outlook Business (October 2025). "
           "Urals pricing: Reuters via Baird Maritime (August 2026), Business Recorder, The Moscow Times (March 2026) and S&amp;P Global Platts (18 March 2026). "
           "Import bill and dependence: PPAC data via The Print, Free Press Journal and UNI (October 2026). Crude assays: Ceylon Petroleum Corporation crude properties annex (WTI Midland, Murban); Iraq SOMO specification via S&amp;P Global (2020); Urals per index summaries. "
           "Sulphur per barrel, the hydrogen floor and the combined share are this blog&rsquo;s arithmetic. Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/where-worlds-oil-sits-when-it-isnt.html", "Where the World&rsquo;s Oil Sits When It Isn&rsquo;t Moving: Storage, Floating Barrels, and the Hormuz Shock of 2026"),
    ("https://masaladeutsch.blogspot.com/2026/08/petroleum-trade-pairings-and-us-crude.html", "Petroleum trade pairings and the US crude storage picture"),
    ("https://masaladeutsch.blogspot.com/2026/08/inside-refinery-how-hydrogen-cleans.html", "Inside the Refinery: How Hydrogen Cleans Your Diesel"),
]

build("Energy · 27 October 2026",
      "India&rsquo;s Crude Basket Now Counts Russian Oil as &lsquo;Sweet&rsquo;. The Barrels Its Refineries Run Are Still Mostly Sour",
      "In March India changed its crude price formula so that Brent, the sweet benchmark, carries 61% of the weight. That reflects how its oil is priced, not what it is: in September about nine in ten imported barrels came from Russia and the Gulf, and sour crude costs refiners hydrogen.",
      body, sources, related, OUT)
print({g: round(v, 2) for g, v in S_KG.items()}, "ratio", round(RATIO, 1), "h2", round(H2_PER_T_S, 1), "total", round(TOTAL_SEP, 2), "rus+me", round(RUS_ME_SHARE, 1), "usdrop", round(US_DROP), "vol", round(VOL_CHG, 1), "price", round(PRICE_CHG))
