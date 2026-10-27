import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-samudra-manthan-offshore.html'

# ---------------------------------------------------------------- data (Cabinet, 31 Jul 2026, as reported)
TOTAL = 84084
PARTS = [("Drilling 60 deepwater wells", 43200),
         ("Seismic and other data", 28534),
         ("Shared offshore hubs", 10000),
         ("Manufacturing and services zones", 2000)]
SEISMIC = [("Basin-wide 2D seismic", 12000), ("3D seismic and other geophysics", 12534), ("Reprocessing repository data, AI interpretation", 4000)]
assert sum(v for _, v in SEISMIC) == PARTS[1][1]
ITEMISED = sum(v for _, v in PARTS)
UNITEMISED = TOTAL - ITEMISED
WELLS, CAP, CAP_ALT, SHARE = 60, 675, 650, 0.5
PER_WELL_ALLOC = PARTS[0][1] / WELLS
AT_CAP = WELLS * CAP
CAP_GAP = PARTS[0][1] - AT_CAP
IMPLIED_WELL = CAP / SHARE                    # Rs crore: well cost at which the cap binds
INR_USD = 94.93                               # 23 Oct 2026 reference rate (this blog's green-debt update)
def usd_m(cr): return cr * 1e7 / INR_USD / 1e6
RESERVE_TARGET, POTENTIAL = 600, 5600         # MMTOE
CRUDE_MMT, GAS_BCM = 28.0, 34.326             # 2025-26 provisional (ministry reply)
DOMESTIC = CRUDE_MMT + GAS_BCM                # DGH oil-plus-oil-equivalent-gas convention: 1 bcm ~ 1 MMTOE
YEARS = RESERVE_TARGET / DOMESTIC
# Deepwater well cost estimates, $ million
COSTS = [("Minister, Sept 2026 (typical deep-sea well)", 100, 100),
         ("Swarajya, Samudra Manthan areas", 120, 145),
         ("Stratigraphic campaign, first estimate (Rs 800 cr)", usd_m(800), usd_m(800)),
         ("Stratigraphic campaign, revised (Rs 1,200 cr)", usd_m(1200), usd_m(1200)),
         ("Well cost at which the scheme&rsquo;s cap binds (Rs 1,350 cr)", usd_m(IMPLIED_WELL), usd_m(IMPLIED_WELL))]
# Past deepwater record
KG98_CAPEX = 5.07            # $ bn, 2018 estimate
KG98_OIL_2017, KG98_OIL_NOW_TGT, KG98_OIL_ACT = 78000, 45000, 20000
KG98_GAS_2017, KG98_GAS_TGT = 15.57, 10
OALP_BLOCKS, OALP_PLEDGE, OALP_DISC, OALP_PROD = 172, 4.36, 14, 1


def chart_parts():
    W, L, top, bh, gap, lab = 400, 10, 24, 18, 8, 170
    rows = PARTS + [("Not itemised in reports", UNITEMISED)]
    H = top + len(rows) * (bh + gap) + 22
    sc = (W - L - lab - 60) / 45000
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Samudra Manthan outlay by component, Rs crore: drilling 43,200; seismic 28,534; hubs 10,000; zones 2,000; not itemised 350.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Samudra Manthan, Rs {TOTAL:,} crore to 2030-31: where it goes</text>']
    for i, (n, v) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="9.5" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{max(v * sc, 1.5):.1f}" height="{bh}" fill="{"#868e96" if i == len(rows) - 1 else "#1c5d99"}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 13}" font-size="9.5" fill="#212529">{v:,}</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Rs crore. Components as reported from the Cabinet decision of 31 July 2026.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_costs():
    W, L, top, bh, gap, lab = 400, 10, 24, 16, 8, 210
    H = top + len(COSTS) * (bh + gap) + 22
    sc = (W - L - lab - 50) / 160
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Estimates of the cost of one Indian deepwater well, in US dollars million, from 84 to 145.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Cost of one deepwater well, $ million</text>']
    for i, (n, lo, hi) in enumerate(COSTS):
        y = top + i * (bh + gap)
        col = "#a5402c" if i == len(COSTS) - 1 else "#1c5d99"
        s.append(f'<text x="{L + lab - 6}" y="{y + 12}" font-size="9" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{lo * sc:.1f}" height="{bh}" fill="{col}"/>')
        if hi > lo:
            s.append(f'<rect x="{L + lab + lo * sc:.1f}" y="{y}" width="{(hi - lo) * sc:.1f}" height="{bh}" fill="{col}" opacity=".45"/>')
        lbl = f"{lo:.0f}" if hi == lo else f"{lo:.0f}&ndash;{hi:.0f}"
        s.append(f'<text x="{L + lab + hi * sc + 4:.1f}" y="{y + 12}" font-size="9.5" fill="#212529">{lbl}</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Rupee figures at Rs {INR_USD} a dollar (23 Oct 2026). This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_record():
    return table(["Earlier deepwater effort", "What was expected", "What happened"], [
        ("ONGC KG-DWN-98/2 (Krishna-Godavari, east coast)", f"${KG98_CAPEX} bn capex (2018); peak {KG98_OIL_2017:,} b/d oil and {KG98_GAS_2017} mmscmd gas in 2017 plans, cut to {KG98_OIL_NOW_TGT:,} b/d and {KG98_GAS_TGT} mmscmd", f"First oil January 2024, after a 2021 target; crude about {KG98_OIL_ACT:,} b/d and gas reported at 1.5&ndash;3 mmscmd in late 2025 and 2026, with geology blamed"),
        ("Reliance&ndash;BP KG-D6 (east coast)", "Once described as India&rsquo;s largest gas discovery; D1 and D3 fields producing from April 2009", "Output fell steeply within a few years of starting; newer R-Cluster (2020), Satellite (2021) and MJ fields (peak about 12 mmscmd) restored part of it"),
        ("OALP exploration blocks (since 2017)", f"{OALP_BLOCKS} blocks awarded, ${OALP_PLEDGE} bn of committed work", f"{OALP_DISC} discoveries reported and {OALP_PROD} marginal field producing"),
        ("Andaman ultra-deepwater (2025&ndash;26)", "Four exploratory wells in 2025-26; a stratigraphic well spudded 27 January 2026", "No commercial discovery announced; the minister has cited 46 earlier dry wells in the region"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>Rs {TOTAL:,} cr</b><span>of public money for offshore exploration, surveys and shared infrastructure to 2030-31</span></div>
<div class="gb-stat"><b>Rs {CAP} cr</b><span>maximum support per deepwater well, half of a well costing about ${usd_m(IMPLIED_WELL):.0f} million</span></div>
<div class="gb-stat"><b>{RESERVE_TARGET} MMTOE</b><span>of new reserves targeted, about {YEARS:.0f} years of India&rsquo;s current oil and gas output</span></div>
<div class="gb-stat"><b>{OALP_DISC} &rarr; {OALP_PROD}</b><span>OALP discoveries to producing fields since 2017, the record the scheme has to beat</span></div>
</div>'''

body = f"""
{stats}

<p>This blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/09/dgh-has-awarded-172-oalp-blocks-and-436_0369361351.html">piece on India&rsquo;s exploration licensing</a> found that the Open Acreage Licensing Programme had awarded about {OALP_BLOCKS} blocks and ${OALP_PLEDGE} billion of committed work since 2017, for {OALP_DISC} discoveries and one marginal producing field. On 31 July 2026 the Cabinet approved a different approach for the hardest acreage. Samudra Manthan, the National Offshore Exploration Scheme, puts Rs {TOTAL:,} crore of public money into surveying the seabed, sharing the cost of deepwater wells and building shared offshore infrastructure, up to 2030-31.</p>
<p>This piece sets out what the money buys, what a deepwater well costs, what the reserve target means against India&rsquo;s output, and what the country&rsquo;s last deepwater bets suggest about the step after a discovery.</p>

<h2 class="gb-h2">What the money buys</h2>
{chart_parts()}
<p>About half the outlay pays for drilling, a third for data. The seismic share of Rs {PARTS[1][1]:,} crore splits into Rs {SEISMIC[0][1]:,} crore of basin-wide 2D surveys, Rs {SEISMIC[1][1]:,} crore of 3D and other geophysics, and Rs {SEISMIC[2][1]:,} crore to reprocess data already in the National Data Repository. The four components reported sum to Rs {ITEMISED:,} crore, Rs {UNITEMISED} crore short of the total; the reports do not say what the rest is for.</p>
<p>The drilling arithmetic has a gap too. The government will pay up to half the eligible cost of each deepwater well, capped at Rs {CAP} crore (some reports say Rs {CAP_ALT} crore). Sixty wells at the cap is Rs {AT_CAP:,} crore, but the drilling line is Rs {PARTS[0][1]:,} crore, or Rs {PER_WELL_ALLOC:.0f} crore a well. The Rs {CAP_GAP:,} crore difference could pay for about {CAP_GAP / CAP:.0f} more wells at the cap, or may cover drilling costs outside the per-well support; the release as reported does not explain it.</p>

<h2 class="gb-h2">What a deepwater well costs</h2>
{chart_costs()}
<p>The cap binds on any well costing more than Rs {IMPLIED_WELL:,.0f} crore, about ${usd_m(IMPLIED_WELL):.0f} million. That is at the top of the range now quoted for Indian deepwater wells. The petroleum minister put a typical deep-sea well at about $100 million in September, with rigs leasing at around $250,000 a day; Swarajya put wells in the scheme&rsquo;s target areas at $120&ndash;145 million; and the cost of each well in the earlier stratigraphic drilling campaign was reported to have risen from Rs 800 crore to about Rs 1,200 crore. At those costs the scheme pays close to half, which is the intention: it turns a $100&ndash;145 million bet into a $50&ndash;75 million one for the company drilling.</p>

<h2 class="gb-h2">What 600 MMTOE means</h2>
<p>The scheme aims to add more than {RESERVE_TARGET} million tonnes of oil equivalent (MMTOE) of reserves. The government puts the hydrocarbon potential of the eastern and western offshore basins at over {POTENTIAL:,} MMTOE, so the target is about {RESERVE_TARGET / POTENTIAL * 100:.0f}% of that potential turned into proved reserves. India produced about {CRUDE_MMT} million tonnes of crude and {GAS_BCM:.1f} billion cubic metres of gas in 2025-26, provisionally, or about {DOMESTIC:.0f} MMTOE on the oil-plus-gas convention the Directorate General of Hydrocarbons uses. {RESERVE_TARGET} MMTOE is therefore about {YEARS:.0f} years of current domestic output, a meaningful addition but well short of replacing the 88% of crude that India imports.</p>

<h2 class="gb-h2">The step after a discovery</h2>
{t_record()}
<p>India&rsquo;s deepwater record is not short of discoveries. KG-D6 and ONGC&rsquo;s neighbouring KG-DWN-98/2 were both large finds. The trouble came after: complex reservoirs that produced well below plan, development that ran years late, and output that peaked early. ONGC&rsquo;s block, approved at ${KG98_CAPEX} billion of capital spending in 2018, began producing oil in January 2024 instead of 2021, and was reported in 2026 to be producing well under half of its cut-down oil target. The OALP record points the same way: {OALP_DISC} discoveries, one producing field.</p>
<p>Samudra Manthan addresses the first step well. Better seismic data and shared drilling costs should mean more and cheaper wells, and the common hubs could make small finds worth developing. But the scheme&rsquo;s published targets are counted in wells drilled and reserves added. Neither guarantees production, and the deepwater-and-ultra-deepwater part of OALP Round X, the acreage the scheme is meant to help, had its bid deadline extended for a sixth time, to 15 November 2026.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Ministry of Petroleum and Natural Gas should publish the full component-wise outlay, including the unitemised Rs {UNITEMISED} crore and how the drilling line relates to the per-well cap.</li>
<li>Each supported well should be reported on completion with its cost, the support paid and the result, so the cost-sharing can be judged well by well.</li>
<li>The scheme should add a production milestone, such as discoveries reaching a development plan within a set number of years, alongside its targets for wells drilled and reserves added.</li>
<li>DGH should publish the time from discovery to first production for every offshore discovery since 2000, so delays like KG-DWN-98/2&rsquo;s can be compared.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The Cabinet release and the PIB background note could not be opened directly; figures come from their text as indexed by search engines and from news reports, which disagree on the per-well cap (Rs {CAP} crore or Rs {CAP_ALT} crore) and in one case describe about 150 wells rather than 60. The current output of KG-DWN-98/2 differs between reports, and no audited cost overrun was found. KG-D6&rsquo;s production history is described qualitatively because no consistent annual series was found. Converting gas to oil equivalent at one billion cubic metres per MMTOE follows DGH&rsquo;s convention and is approximate. Dollar figures use one exchange rate and ignore cost escalation to 2031.</p>
"""

sources = ("Samudra Manthan: Cabinet decision of 31 July 2026 as reported by Outlook Business, Deccan Herald, Deccan Chronicle, Free Press Journal, Angel One and Offshore Technology; component details per Drishti IAS, NEXT IAS and Vision IAS summaries, the PIB background document as indexed, and First Break (seismic split). "
           "Well costs: the petroleum minister via Republic World (29 September 2026); Swarajya; the stratigraphic campaign via Chem In Digest. Andaman wells: Drilling Contractor and PSU Watch (2026). "
           "KG-DWN-98/2: Business Standard (13 November 2025) and 2026 press reports; 2018 cost estimate per Business Standard. KG-D6: Business Standard (2019), Offshore Technology and Indian Infrastructure (MJ field). "
           "Domestic production 2025-26: Ministry of Petroleum and Natural Gas reply to Parliament via The Print. OALP figures and Round X dates: this blog&rsquo;s OALP piece and its 27 September 2026 update. "
           "Per-well arithmetic, dollar conversions and the years-of-output comparison are this blog&rsquo;s. Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/09/dgh-has-awarded-172-oalp-blocks-and-436_0369361351.html", "DGH Has Awarded 172 OALP Blocks and $4.36 Billion in Pledges. One Has Reached Production"),
    ("https://masaladeutsch.blogspot.com/2026/08/where-worlds-oil-sits-when-it-isnt.html", "Where the World&rsquo;s Oil Sits When It Isn&rsquo;t Moving: Storage, Floating Barrels, and the Hormuz Shock of 2026"),
]

build("Energy · 27 October 2026",
      "Samudra Manthan Pays Up to Rs 675 Crore a Well. India&rsquo;s Last Deepwater Bets Show Discovery Is the Easy Part",
      "The new Rs 84,084 crore offshore scheme shares the cost of 60 deepwater wells and pays for new seismic surveys. Its 600 MMTOE reserve target is about ten years of India&rsquo;s output; the harder test, on India&rsquo;s record, is turning finds into production.",
      body, sources, related, OUT)
print("itemised", ITEMISED, "unitemised", UNITEMISED, "per well", PER_WELL_ALLOC, "gap", CAP_GAP, "implied $m", round(usd_m(IMPLIED_WELL)), "domestic", round(DOMESTIC, 1), "years", round(YEARS, 1), [round(c[1]) for c in COSTS])
