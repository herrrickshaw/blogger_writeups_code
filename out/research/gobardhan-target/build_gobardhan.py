import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-gobardhan-target.html'

# ---------------------------------------------------------------- data
OUTLAY_CR = 23731                 # Cabinet, 6 Aug 2026, FY2026-27 to FY2035-36
TARGET_MMSCMD = 5.0               # domestic CBG output goal by FY2035-36 (launch coverage, PSU Watch / Swarajya)
NOW_MMSCMD = 0.4                  # 217 commissioned plants, GOBARdhan portal, 6 Aug 2026 (PIB)
REGISTERED, UNDER_CONSTR, COMMISSIONED = 1908, 339, 217   # GOBARdhan portal, 6 Aug 2026
FUNCTIONAL, CGD_LINKED, CGD_WIP = 207, 24, 15              # PNGRB, Aug 2026 (this blog's earlier piece)
PRICE_MMBTU, OLD_PRICE_MMBTU = 2110, 1478
PRICE_KG, OLD_PRICE_KG = 98, 69   # this blog's earlier piece, lower calorific basis (PIB factsheet says Rs 105)
AFFORD_CAP = 10                   # Rs/kg cap on affordability support to the pooling operator (guidelines)
CAPEX_CAB, CAPEX_GUIDE = 2.0, 1.25   # Rs crore per TPD: Cabinet stage vs guidelines (capped Rs 30 cr a project)
CGD_SALES_MMSCM_YR = 17061        # all CGD gas sales in a year, PNGRB statistical booklet (Sep 2026)
CBO_MAX = 0.05                    # obligation from FY2028-29, on CNG (transport) and PNG (domestic) only
KG_PER_SCM = 0.72                 # assumption: density of CBG at standard conditions
JAN_PLANTS, JAN_TPD = 132, 920    # commissioned plants and tonnes a day reported for January 2026 (this blog's earlier piece)

MULTIPLE = TARGET_MMSCMD / NOW_MMSCMD
PER_PLANT_SCM = NOW_MMSCMD * 1e6 / COMMISSIONED
PER_PLANT_T = PER_PLANT_SCM * KG_PER_SCM / 1000
CGD_MMSCMD = CGD_SALES_MMSCM_YR / 365
CBO_CEIL = CGD_MMSCMD * CBO_MAX            # upper bound: 5% of ALL city-gas sales
ADD_MMSCMD = TARGET_MMSCMD - NOW_MMSCMD
ADD_TPD = ADD_MMSCMD * 1e6 * KG_PER_SCM / 1000
CAPEX_LOW, CAPEX_HIGH = ADD_TPD * CAPEX_GUIDE, ADD_TPD * CAPEX_CAB      # Rs crore, if capacity = output
PLANTS_AT_NOW_AVG = ADD_MMSCMD * 1e6 / PER_PLANT_SCM
TARGET_TPD = TARGET_MMSCMD * 1e6 * KG_PER_SCM / 1000
AFFORD_YR_AT_TARGET = TARGET_TPD * 1000 * AFFORD_CAP * 365 / 1e7        # Rs crore a year
REV_PLANT_NOW = PER_PLANT_T * 1000 * PRICE_KG * 365 / 1e7               # Rs crore a year
REV_PLANT_OLD = PER_PLANT_T * 1000 * OLD_PRICE_KG * 365 / 1e7
REV_10TPD = 10 * 1000 * PRICE_KG * 365 / 1e7
JAN_AVG_TPD = JAN_TPD / JAN_PLANTS
UTIL = PER_PLANT_T / JAN_AVG_TPD * 100
AUG_TPD = NOW_MMSCMD * 1e6 * KG_PER_SCM / 1000
assert round(MULTIPLE, 1) == 12.5 and round(CGD_MMSCMD, 1) == 46.7


def chart_gas():
    W, L, top, bh, gap, lab = 400, 10, 26, 20, 10, 200
    rows = [("Made today by 217 commissioned plants", NOW_MMSCMD, "#868e96"),
            ("Most the 5% mandate could absorb*", CBO_CEIL, "#d9a441"),
            ("Scheme target, 2035-36", TARGET_MMSCMD, "#1c5d99")]
    H = top + len(rows) * (bh + gap) + 30
    sc = (W - L - lab - 40) / 5.2
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Compressed biogas, million standard cubic metres a day: {NOW_MMSCMD} made today, at most {CBO_CEIL:.1f} absorbed by the 5% blending mandate, and a target of {TARGET_MMSCMD:.0f}.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Compressed biogas, million standard cubic metres a day</text>']
    for i, (n, v, col) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 14}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 14}" font-size="10" fill="#212529">{v:.1f}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">*5% of all city-gas sales ({CGD_SALES_MMSCM_YR:,} MMSCM a year, PNGRB); the mandate covers only</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">CNG for vehicles and piped gas for homes, so the real figure is lower.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_funnel():
    W, L, top, bh, gap, lab = 400, 10, 24, 18, 8, 168
    rows = [("Registered on the portal", REGISTERED, "#868e96"), ("Under construction", UNDER_CONSTR, "#868e96"),
            ("Commissioned", COMMISSIONED, "#1c5d99"), ("Functional (PNGRB)", FUNCTIONAL, "#1c5d99"),
            ("Linked to a city-gas pipeline", CGD_LINKED, "#a5402c")]
    H = top + len(rows) * (bh + gap) + 20
    sc = (W - L - lab - 50) / REGISTERED
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Compressed biogas plants: {REGISTERED} registered, {UNDER_CONSTR} under construction, {COMMISSIONED} commissioned, {FUNCTIONAL} functional, {CGD_LINKED} linked to a city-gas pipeline.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Compressed biogas plants, August 2026</text>']
    for i, (n, v, col) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{max(v * sc, 2):.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + max(v * sc, 2) + 4:.1f}" y="{y + 13}" font-size="10" fill="#212529">{v:,}</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">GOBARdhan portal, 6 Aug 2026 (via PIB); functional and pipeline-linked: PNGRB, Aug 2026.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_scheme():
    return table(["Pillar", "What the scheme offers", "What it was before"], [
        ("Assured offtake", "City-gas companies must blend CBG at 3% of CNG for vehicles and piped gas for homes in 2026-27, 4% in 2027-28 and 5% from 2028-29; GAIL pools and buys the gas", "1% obligation in 2025-26; offtake letters from oil companies under SATAT"),
        ("Price", f"Rs {PRICE_MMBTU:,} per MMBtu, before tax and compression, held to 31 March 2036 with a yearly review", f"Rs {OLD_PRICE_MMBTU:,} per MMBtu from June 2025"),
        ("Capital assistance", f"Up to Rs {CAPEX_CAB:.0f} crore per tonne a day of capacity at Cabinet stage; the September guidelines are reported at Rs {CAPEX_GUIDE} crore, capped at Rs 30 crore a project", "Separate schemes run by MNRE and the Agriculture Ministry"),
        ("Pipelines", "Up to 80% of eligible cost for pipelines joining CBG clusters to trunk lines; up to 50% for a single plant&rsquo;s link to a city-gas network (launch release)", "A separate pipeline scheme"),
        ("Credit guarantee", "Up to 85% cover on eligible loans to MSME projects", "None specific to CBG"),
        ("Challenge fund", "For technology and ecosystem projects; amount not published", "&mdash;"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{NOW_MMSCMD} &rarr; {TARGET_MMSCMD:.0f}</b><span>million cubic metres of CBG a day, today and the 2035-36 target: {MULTIPLE:.1f} times, which the government calls &ldquo;nearly ten-fold&rdquo;</span></div>
<div class="gb-stat"><b>{PER_PLANT_T:.1f} t</b><span>a day: what the average commissioned plant makes, about a fifth of the average capacity reported in January</span></div>
<div class="gb-stat"><b>&le; {CBO_CEIL:.1f}</b><span>million cubic metres a day: the most the 5% city-gas blending mandate could take, under half the target</span></div>
<div class="gb-stat"><b>{CGD_LINKED} of {FUNCTIONAL}</b><span>working plants piped into a city-gas network</span></div>
</div>'''

body = f"""
{stats}

<p>This blog has followed compressed biogas (CBG) through its <a href="https://masaladeutsch.blogspot.com/2026/07/the-cbg-incentive-stack-every-leg-of.html">stack of incentives</a>, the <a href="https://masaladeutsch.blogspot.com/2026/09/india-has-132-compressed-biogas-plants.html">gap between plants and pipelines</a> and the <a href="https://masaladeutsch.blogspot.com/2026/10/biogas-is-priority-sector-loan-43.html">43% rise in the price it fetches</a>. In August the Cabinet put most of those pieces into one scheme. GOBARdhan, the National Circular Bioenergy Scheme, has Rs {OUTLAY_CR:,} crore for 2026-27 to 2035-36, an administered price of Rs {PRICE_MMBTU:,} per MMBtu, and a goal of about {TARGET_MMSCMD:.0f} million standard cubic metres of CBG a day (MMSCMD) by 2035-36.</p>
<p>This piece does not repeat the earlier ones. It asks whether the target adds up: how far today&rsquo;s plants are from it, who is obliged to buy the gas, what the money covers, and what the new price means for a plant of the size India actually has.</p>

<h2 class="gb-h2">What the scheme offers</h2>
{t_scheme()}
<p class="gb-note">The Cabinet release, the launch release of 1 October and the September guidelines are reported differently on capital assistance; this blog could not open any of them. The rupee split of the outlay between pillars has not been published.</p>

<h2 class="gb-h2">The target is more than ten-fold</h2>
<p>The government&rsquo;s own release gives the baseline. On 6 August 2026 the GOBARdhan registration portal counted {COMMISSIONED} commissioned plants producing {NOW_MMSCMD} MMSCMD, with {UNDER_CONSTR} under construction and {REGISTERED:,} registered. Going from {NOW_MMSCMD} to {TARGET_MMSCMD:.0f} MMSCMD is a multiple of {MULTIPLE:.1f}, more than the &ldquo;nearly ten-fold&rdquo; in the launch coverage.</p>
{chart_funnel()}
<p>The more telling number is output per plant. {NOW_MMSCMD} MMSCMD across {COMMISSIONED} plants is about {PER_PLANT_SCM:,.0f} cubic metres a day each, or about {PER_PLANT_T:.1f} tonnes at {KG_PER_SCM} kg per cubic metre. In January 2026, {JAN_PLANTS} commissioned plants were reported at {JAN_TPD} tonnes a day, about {JAN_AVG_TPD:.0f} tonnes each. That can only have been capacity: {NOW_MMSCMD} MMSCMD is about {AUG_TPD:,.0f} tonnes a day from {COMMISSIONED} plants. On those two figures, the average commissioned plant is producing about {UTIL:.0f}% of what it was built for. Neither source states its basis clearly and the portal does not publish capacity, so this is an inference, not a measured utilisation rate. But it says the first problem is not the number of plants. If the remaining {ADD_MMSCMD:.1f} MMSCMD came from plants that perform like today&rsquo;s average, it would take about {PLANTS_AT_NOW_AVG:,.0f} more of them.</p>

<h2 class="gb-h2">Who has to buy the gas</h2>
{chart_gas()}
<p>The scheme&rsquo;s demand guarantee is the CBG blending obligation on city-gas companies, rising to 5% from 2028-29. It applies only to CNG for vehicles and piped gas for homes. PNGRB&rsquo;s statistical booklet puts all city-gas sales at {CGD_SALES_MMSCM_YR:,} million cubic metres a year, about {CGD_MMSCMD:.1f} MMSCMD, and that total also includes industrial and commercial customers. Even 5% of all of it would be about {CBO_CEIL:.1f} MMSCMD, under half the {TARGET_MMSCMD:.0f} MMSCMD target. City-gas volumes will grow by 2035-36, but on today&rsquo;s base the mandate cannot absorb the target on its own. The rest has to go to GAIL&rsquo;s pool, to industry, or into pipelines, and only {CGD_LINKED} of {FUNCTIONAL} functional plants were piped into a city-gas network in August, with {CGD_WIP} more in progress.</p>

<h2 class="gb-h2">What the money covers, and what the price is worth</h2>
<p>The published pillars allow a rough check on the Rs {OUTLAY_CR:,} crore. Adding {ADD_MMSCMD:.1f} MMSCMD means about {ADD_TPD:,.0f} tonnes a day of output. Even if every new plant ran at full capacity, capital assistance would cost about Rs {CAPEX_LOW:,.0f} crore at the guideline rate and Rs {CAPEX_HIGH:,.0f} crore at the Cabinet-stage rate; real plants need more capacity than output, so the true figure is higher. The affordability support to the pooling operator, capped at Rs {AFFORD_CAP} a kilogram, would cost up to about Rs {AFFORD_YR_AT_TARGET:,.0f} crore a year once the target is reached. Pipelines, guarantees and the challenge fund come on top. The outlay is not obviously short, but it has little room for the target to be reached early or for capital assistance to run at the higher rate.</p>
<p>For a plant, the new price matters a great deal. At about Rs {PRICE_KG} a kilogram instead of Rs {OLD_PRICE_KG}, a plant making the current average of {PER_PLANT_T:.1f} tonnes a day would earn about Rs {REV_PLANT_NOW:.1f} crore a year instead of Rs {REV_PLANT_OLD:.1f} crore. A 10-tonne plant running full would earn about Rs {REV_10TPD:.0f} crore. The difference between those two figures, more than the price itself, is what decides whether a plant pays back, which is why feedstock supply and offtake matter more than the headline price.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The GOBARdhan portal should publish, for every commissioned plant, its design capacity and monthly output, so that utilisation can be tracked rather than inferred from a national average.</li>
<li>The Ministry of Petroleum and Natural Gas should publish the rupee allocation to each of the six pillars and the year-by-year spending plan.</li>
<li>The scheme should publish a demand plan that shows how much of the {TARGET_MMSCMD:.0f} MMSCMD will go to the city-gas mandate, GAIL&rsquo;s pool, industry and pipelines.</li>
<li>Capital assistance should be paid partly on measured output, not only on installed capacity, so the scheme pays for gas made rather than plants built.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The Cabinet and launch releases, the guidelines and the PNGRB booklet could not be opened directly; figures come from their text as indexed by search engines and from news reports. The PNGRB booklet&rsquo;s year was not stated in the text found. The January figure of 920 tonnes a day is read here as capacity; if it was output, the two official figures contradict each other. The per-plant output assumes a density of {KG_PER_SCM} kg per cubic metre and the per-kilogram price uses the lower of two reported conversions (Rs {PRICE_KG} rather than Rs 105). The split of city-gas sales between vehicles, homes and industry was not found, so the mandate&rsquo;s ceiling is an upper bound. Capital-assistance estimates assume new capacity equals new output and are a floor.</p>
"""

sources = ("GOBARdhan: Cabinet release of 6 August 2026 (PIB; PM India) and the GOBARdhan portal figures in it (1,908 registered, 217 commissioned producing 0.4 MMSCMD, 339 under construction); launch release of 1 October 2026 (PIB) for pipeline and credit-guarantee support; 5 MMSCMD target and &ldquo;nearly ten-fold&rdquo; per PSU Watch, Swarajya and Enerdata; operational guidelines of 15 September 2026 (capital assistance of Rs 1.25 crore per TPD capped at Rs 30 crore, GAIL as pooling operator, affordability support capped at Rs 10/kg) per Argus, Mondaq and Agrospectrum; Vision IAS and NEXT IAS summaries. "
           "Blending obligation schedule: MoPNG (via Vikaspedia, Tribune). City-gas sales: PNGRB Statistical Booklet (September 2026). Functional and pipeline-linked plants: PNGRB, August 2026, as in this blog&rsquo;s earlier piece. Price per kilogram: this blog&rsquo;s earlier piece on the price rise. "
           "Per-plant output, the mandate ceiling, capital-assistance and affordability-support estimates and plant revenues are this blog&rsquo;s arithmetic (builder in the repository at out/research/gobardhan-target/). Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/09/india-has-132-compressed-biogas-plants.html", "India Has 207 Compressed Biogas Plants Running. The Pipeline to Actually Use That Gas Reaches 24 of Them."),
    ("https://masaladeutsch.blogspot.com/2026/10/biogas-is-priority-sector-loan-43.html", "Biogas Is a Priority-Sector Loan. The 43% Higher CBG Price Is Worth About 50 Times the Cost of the Repo Hike"),
    ("https://masaladeutsch.blogspot.com/2026/07/the-cbg-incentive-stack-every-leg-of.html", "The CBG Incentive Stack &mdash; Every Leg of a Biogas Plant De-risked"),
]

build("Biogas · 27 October 2026",
      "GOBARdhan Aims for 12 Times Today&rsquo;s Biogas Output. The Mandate Meant to Buy It Covers Less Than Half",
      f"The new Rs {OUTLAY_CR:,} crore scheme wants 5 million cubic metres of compressed biogas a day by 2035-36. India&rsquo;s 217 commissioned plants make 0.4, about 1.3 tonnes a day each, and the city-gas blending mandate could absorb at most about 2.3.",
      body, sources, related, OUT)
print(dict(mult=round(MULTIPLE, 2), per_plant_scm=round(PER_PLANT_SCM), per_plant_t=round(PER_PLANT_T, 2), cgd=round(CGD_MMSCMD, 1), ceil=round(CBO_CEIL, 2), add_tpd=round(ADD_TPD), capex=(round(CAPEX_LOW), round(CAPEX_HIGH)), plants=round(PLANTS_AT_NOW_AVG), afford=round(AFFORD_YR_AT_TARGET), rev=(round(REV_PLANT_NOW, 2), round(REV_PLANT_OLD, 2), round(REV_10TPD, 1)), util=round(UTIL), jan=round(JAN_AVG_TPD,1), aug=round(AUG_TPD)))
