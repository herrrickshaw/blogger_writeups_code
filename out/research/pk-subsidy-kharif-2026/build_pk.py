import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-pk-subsidy-kharif-2026.html'

# ---------------------------------------------------------------- NBS rates, Rs per kg of nutrient (Cabinet decisions)
SEASONS = ["Kharif 2025", "Rabi 2025-26", "Kharif 2026"]
RATES = {  # N, P, K, S
    "Kharif 2025": (43.02, 43.60, 2.38, 1.77),
    "Rabi 2025-26": (43.02, 47.96, 2.38, 2.87),
    "Kharif 2026": (47.32, 52.76, 2.38, 3.16),
}
BUDGET = {"Kharif 2025": 37216.15, "Rabi 2025-26": 37952.29, "Kharif 2026": 41533.81}   # Rs crore
GRADES = {  # kg of N, P2O5, K2O, S per tonne
    "DAP 18-46-0": (180, 460, 0, 0),
    "MOP 0-0-60": (0, 0, 600, 0),
    "NPK 10-26-26": (100, 260, 260, 0),
    "NPKS 20-20-0-13": (200, 200, 0, 130),
}
def sub(grade, season): return sum(a * b for a, b in zip(GRADES[grade], RATES[season]))
DAP = {s: sub("DAP 18-46-0", s) for s in SEASONS}
assert round(DAP["Kharif 2025"]) == 27800 and round(DAP["Rabi 2025-26"]) == 29805   # match the published per-tonne figures
DAP_RISE = (DAP["Kharif 2026"] / DAP["Kharif 2025"] - 1) * 100

# ---------------------------------------------------------------- DAP economics per tonne
MRP = 1350 * 20                           # Rs 1,350 per 50 kg bag, unchanged
CFR = {"Kharif 2025": 800, "Rabi 2025-26": 704, "Kharif 2026": 932.5}   # $/t CFR India
CFR_NOTE = {"Kharif 2025": "about $800 (Jul 2025)", "Rabi 2025-26": "$699&ndash;709 (mid-Nov 2025)", "Kharif 2026": "$930&ndash;935 (IPL tender, May 2026)"}
FX = {"Kharif 2025": 86.0, "Rabi 2025-26": 88.7, "Kharif 2026": 96.0}  # Rs per $ around those dates (approximate)
COST = {s: CFR[s] * FX[s] for s in SEASONS}
REAL = {s: MRP + DAP[s] for s in SEASONS}
GAP = {s: COST[s] - REAL[s] for s in SEASONS}
BE = {s: REAL[s] / FX[s] for s in SEASONS}
K26 = "Kharif 2026"
FARMER_SHARE = MRP / COST[K26] * 100
SUB_SHARE = DAP[K26] / COST[K26] * 100
GAP_SHARE = GAP[K26] / COST[K26] * 100

# ---------------------------------------------------------------- MOP
MOP_CFR_26, MOP_CFR_25 = 383, 349          # $/t CFR, BPC-IPL May 2026; previous contract Jun 2025
MOP_MRP = 1534 * 20                        # Rs/t, reported MRP (Rajya Sabha answer, Dec 2024)
MOP_SUB = sub("MOP 0-0-60", K26)
MOP_COST_26 = MOP_CFR_26 * FX[K26]
MOP_GAP_26 = MOP_COST_26 - (MOP_MRP + MOP_SUB)

# ---------------------------------------------------------------- budget
NBS_FY27 = 54000                           # Rs crore, FY2026-27 provisional NBS allocation (Argus)
KH_SHARE = BUDGET[K26] / NBS_FY27 * 100
BUDGET_RISE = (BUDGET[K26] / BUDGET["Kharif 2025"] - 1) * 100


def chart_dap():
    W, L, top, gw, bw = 400, 44, 30, 118, 40
    ch = 150
    vmax = 95000
    H = top + ch + 50
    base = top + ch
    sc = ch / vmax
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Per tonne of imported DAP: what the seller receives (retail price plus subsidy) against the import cost, for kharif 2025, rabi 2025-26 and kharif 2026.">',
         f'<text x="10" y="12" font-size="12" fill="#495057">Imported DAP per tonne: what it earns vs what it costs, Rs</text>',
         f'<rect x="10" y="18" width="9" height="9" fill="#868e96"/><text x="23" y="26" font-size="9.5" fill="#212529">Farmer pays</text>',
         f'<rect x="90" y="18" width="9" height="9" fill="#1c5d99"/><text x="103" y="26" font-size="9.5" fill="#212529">Subsidy</text>',
         f'<rect x="160" y="18" width="9" height="9" fill="#a5402c"/><text x="173" y="26" font-size="9.5" fill="#212529">Import cost (CFR)</text>']
    for v in (0, 30000, 60000, 90000):
        y = base - v * sc
        s.append(f'<line x1="{L}" x2="{W - 8}" y1="{y:.1f}" y2="{y:.1f}" stroke="#dee2e6"/>')
        s.append(f'<text x="{L - 4}" y="{y + 3:.1f}" font-size="9" fill="#6c757d" text-anchor="end">{v // 1000}k</text>')
    for i, sname in enumerate(SEASONS):
        x = L + 12 + i * gw
        hm, hs, hc = MRP * sc, DAP[sname] * sc, COST[sname] * sc
        s.append(f'<rect x="{x}" y="{base - hm:.1f}" width="{bw}" height="{hm:.1f}" fill="#868e96"/>')
        s.append(f'<rect x="{x}" y="{base - hm - hs:.1f}" width="{bw}" height="{hs:.1f}" fill="#1c5d99"/>')
        s.append(f'<text x="{x + bw / 2}" y="{base - hm - hs - 4:.1f}" font-size="9" fill="#212529" text-anchor="middle">{REAL[sname] / 1000:.1f}k</text>')
        s.append(f'<rect x="{x + bw + 4}" y="{base - hc:.1f}" width="{bw}" height="{hc:.1f}" fill="#a5402c"/>')
        s.append(f'<text x="{x + bw * 1.5 + 4}" y="{base - hc - 4:.1f}" font-size="9" fill="#212529" text-anchor="middle">{COST[sname] / 1000:.1f}k</text>')
        s.append(f'<text x="{x + bw + 2}" y="{base + 13}" font-size="9.5" fill="#212529" text-anchor="middle">{sname}</text>')
    s.append(f'<text x="10" y="{H - 16}" font-size="9" fill="#6c757d">Retail price Rs 1,350 a bag; NBS subsidy; CFR price &times; approximate rupee rate.</text>')
    s.append(f'<text x="10" y="{H - 4}" font-size="9" fill="#6c757d">Before port, bagging, freight and interest costs. This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_rates():
    rows = []
    for lab, idx in (("Nitrogen (N), Rs/kg", 0), ("Phosphate (P), Rs/kg", 1), ("Potash (K), Rs/kg", 2), ("Sulphur (S), Rs/kg", 3)):
        rows.append([lab] + [f"{RATES[sn][idx]:.2f}" for sn in SEASONS])
    for g in GRADES:
        rows.append([f"{g}, Rs/tonne"] + [f"{sub(g, sn):,.0f}" for sn in SEASONS])
    rows.append(["Season budget, Rs crore"] + [f"{BUDGET[sn]:,.0f}" for sn in SEASONS])
    return table(["Nutrient-based subsidy"] + SEASONS, rows)


def t_dap():
    rows = [
        ["DAP import price, $/t CFR"] + [CFR_NOTE[sn] for sn in SEASONS],
        ["Rupees per dollar (approx.)"] + [f"{FX[sn]:.1f}" for sn in SEASONS],
        ["Import cost, Rs/t"] + [f"{COST[sn]:,.0f}" for sn in SEASONS],
        ["Farmer pays (Rs 1,350 a bag), Rs/t"] + [f"{MRP:,}" for sn in SEASONS],
        ["Subsidy, Rs/t"] + [f"{DAP[sn]:,.0f}" for sn in SEASONS],
        ["Shortfall before handling costs, Rs/t"] + [f"<b>{GAP[sn]:,.0f}</b>" for sn in SEASONS],
        ["Import price that would break even, $/t"] + [f"{BE[sn]:,.0f}" for sn in SEASONS],
    ]
    return table(["Per tonne of imported DAP"] + SEASONS, rows)


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>Rs {DAP[K26]:,.0f}</b><span>subsidy per tonne of DAP in kharif 2026, up {DAP_RISE:.0f}% on kharif 2025</span></div>
<div class="gb-stat"><b>Rs {GAP[K26]:,.0f}</b><span>by which a tonne of DAP imported at May&rsquo;s price costs more than retail price plus subsidy</span></div>
<div class="gb-stat"><b>${BE[K26]:,.0f}</b><span>a tonne is the import price the kharif 2026 subsidy can carry; India paid $930&ndash;935</span></div>
<div class="gb-stat"><b>{KH_SHARE:.0f}%</b><span>of the full year&rsquo;s budgeted NBS subsidy is committed by the kharif season alone</span></div>
</div>'''

body = f"""
{stats}

<p>In April the Union Cabinet approved Rs {BUDGET[K26]:,.0f} crore of nutrient-based subsidy (NBS) for phosphatic and potassic (P&amp;K) fertilisers for kharif 2026, the April&ndash;September season, {BUDGET_RISE:.0f}% more than a year earlier. The subsidy per kilogram of phosphate rose to Rs 52.76 and of nitrogen to Rs 47.32, so a tonne of di-ammonium phosphate (DAP), India&rsquo;s most used phosphate fertiliser, now carries Rs {DAP[K26]:,.0f} of subsidy. The retail price of DAP has stayed at Rs 1,350 a 50 kg bag.</p>
<p>This blog has covered <a href="https://masaladeutsch.blogspot.com/2026/08/indias-fertiliser-import-bill-hits-18.html">India&rsquo;s $18 billion fertiliser import bill</a> and <a href="https://masaladeutsch.blogspot.com/2026/08/imported-fertiliser-fuel-prices-diesel.html">why fertiliser prices barely reach wholesale inflation</a>. This piece works out what the new rates mean per tonne: how much of the cost of imported DAP the farmer, the subsidy and the importer each bear, and how that has changed over three seasons.</p>

<h2 class="gb-h2">The rates, season by season</h2>
{t_rates()}
<p>The government pays a fixed amount for each kilogram of nitrogen, phosphate, potash and sulphur in a fertiliser, so a grade&rsquo;s subsidy follows from its nutrient content. DAP is 18% nitrogen and 46% phosphate; at kharif 2026 rates that is Rs {DAP[K26]:,.0f} a tonne. The same formula gives the published Rs 27,800 for kharif 2025 and Rs 29,805 for rabi 2025-26. Potash has been held at Rs 2.38 a kilogram throughout, so muriate of potash (MOP) gets only Rs {MOP_SUB:,.0f} a tonne.</p>

<h2 class="gb-h2">Imported DAP earns less than it costs</h2>
{chart_dap()}
{t_dap()}
<p>An importer of DAP receives two things for a tonne: Rs {MRP:,} from the farmer at the fixed retail price, and the subsidy. In kharif 2026 that is Rs {REAL[K26]:,.0f}. Indian Potash Limited bought about 1.35 million tonnes in May at $930&ndash;935 a tonne, when the rupee was around {FX[K26]:.0f} to the dollar: about Rs {COST[K26]:,.0f} a tonne, before port charges, bagging, inland freight and interest. The shortfall is about Rs {GAP[K26]:,.0f} a tonne. Of the import cost, the farmer pays about {FARMER_SHARE:.0f}%, the subsidy covers {SUB_SHARE:.0f}%, and about {GAP_SHARE:.0f}% is not covered.</p>
<p>The subsidy rose, but the import price and the rupee rose faster. Subsidy plus retail price covers imported DAP only up to about ${BE[K26]:,.0f} a tonne, and that break-even has barely moved across the three seasons (${BE['Kharif 2025']:,.0f}, ${BE['Rabi 2025-26']:,.0f}, ${BE[K26]:,.0f}), while the market moved from about $700 to more than $930. In rabi 2025-26, when DAP fell to around $700, the shortfall was about Rs {GAP['Rabi 2025-26']:,.0f}; by kharif 2026 it was more than five times that. The Fertiliser Association of India asked for the kharif rates to be revised, citing raw-material prices up 100&ndash;200% after the West Asia conflict.</p>
<p>Who bears the shortfall is not published. Importers and domestic makers who use imported phosphoric acid and rock can carry cheaper earlier stock, run down margins, cut imports, or wait for a special package like the Rs 3,500 a tonne the government paid on DAP in 2024-25. Any of these shows up somewhere: in company results, in a later supplementary subsidy, or in supply. DAP imports in April&ndash;December 2025 were 5.95 million tonnes, up from 4.13 million a year earlier, and stocks in March 2026 were well above the pro-rata requirement.</p>

<h2 class="gb-h2">Potash and the budget</h2>
<p>MOP is the other large import. India&rsquo;s new contract with Belarusian Potash Company in May was $383 a tonne, up from $349 a year earlier. At about Rs {FX[K26]:.0f} to the dollar that is Rs {MOP_COST_26:,.0f} a tonne. MOP&rsquo;s retail price is formally decontrolled; at the Rs 1,534 a bag reported in a December 2024 parliamentary answer, retail price plus subsidy falls about Rs {MOP_GAP_26:,.0f} a tonne short, a much smaller gap than DAP&rsquo;s.</p>
<p>The budget is the other pressure point. The provisional NBS allocation for 2026-27 was about Rs {NBS_FY27:,} crore; the kharif season alone has committed Rs {BUDGET[K26]:,.0f} crore of it, about {KH_SHARE:.0f}%. In 2025-26 the NBS allocation was raised 22.5% above its provisional figure during the year; at current import prices a similar revision looks likely.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Department of Fertilizers should publish, each season, the import price and exchange rate it assumed when setting NBS rates, so the gap between assumed and actual cost is visible.</li>
<li>NBS rates should be revised automatically within a season when the landed price of DAP moves by more than a set margin, instead of through ad hoc special packages.</li>
<li>The government should publish quarterly import volumes, landed prices and subsidy paid per tonne for DAP and MOP, as this blog proposed earlier, so the shortfall and who bears it can be measured.</li>
<li>If the retail price of DAP is to stay fixed, the budget should say so and provide for the subsidy that implies at current prices, rather than revising the allocation mid-year.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The Cabinet&rsquo;s kharif 2026 rates were read from press reports, not the notification; the per-tonne DAP figure is this blog&rsquo;s arithmetic from those rates, checked against the published figures for the two previous seasons. Import prices are single reference points per season and the exchange rates are approximate, so the shortfalls are indicative. The comparison treats the full Rs 1,350 retail price as the importer&rsquo;s revenue, although it includes GST and the dealer&rsquo;s margin, and it leaves out port, bagging, freight and interest costs; both make the real shortfall larger. Whether a special package was paid on DAP in 2026 was not found. The MOP retail price is from 2024 and may have changed.</p>
"""

sources = ("NBS rates and budgets: Union Cabinet decisions for kharif 2026 (ANI, ETV Bharat, PSU Watch, Free Press Journal, April 2026), rabi 2025-26 (PIB document; Business Standard, October 2025) and kharif 2025 (Business Standard, March 2025). DAP retail price: Ministry of Chemicals and Fertilizers statements (March 2026). "
           "Import prices: Indian Potash Limited DAP tender, May 2026 (Fertilizer Daily, Profercy); September 2026 DAP range (Fertilizer Daily); 2025 DAP prices (PTI via The Week; Argus; CRU). MOP contract: Argus and Fertilizer Daily (May 2026). MOP retail price: data.gov.in mirror of a Rajya Sabha answer (December 2024). Rupee: press reports of the rate in May 2026 (5paisa, Angel One). "
           "Budget and imports: Argus on the 2026-27 NBS allocation and 2025 imports; FAI request for revision (PSU Watch); 2024-25 special package and losses (Down To Earth); ICRA on loss-making DAP imports (September 2025). "
           "Per-tonne subsidies, import costs, shortfalls and break-even prices are this blog&rsquo;s arithmetic. Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/indias-fertiliser-import-bill-hits-18.html", "India&rsquo;s Fertiliser Import Bill Hits $18 Billion, and Parliament&rsquo;s Own Committee Explains Why"),
    ("https://masaladeutsch.blogspot.com/2026/07/indias-subsidised-imports-fertilisers.html", "India&rsquo;s Subsidised Imports &mdash; Fertilisers Explode +76% (FY25 vs FY26)"),
    ("https://masaladeutsch.blogspot.com/2026/08/nature-versus-nurture-indias-fertiliser.html", "Nature Versus Nurture: India&rsquo;s Fertiliser-Fed Food Security"),
    ("https://masaladeutsch.blogspot.com/2026/08/imported-fertiliser-fuel-prices-diesel.html", "Diesel passes straight through to WPI. Fertiliser mostly doesn&rsquo;t &mdash; because subsidy absorbs it."),
]

build("Agriculture &amp; Fertilisers · 27 October 2026",
      f"India Raised the DAP Subsidy {DAP_RISE:.0f}% This Kharif. Imported DAP Still Costs About Rs {round(GAP[K26], -3) / 1000:.0f},000 a Tonne More Than It Earns",
      f"Kharif 2026 rates put Rs {DAP[K26]:,.0f} of subsidy on a tonne of DAP, whose retail price stays at Rs 1,350 a bag. At May&rsquo;s import price and rupee, that covers only DAP bought below about ${BE[K26]:,.0f} a tonne; India paid more than $930.",
      body, sources, related, OUT)
print({s: (round(DAP[s]), round(COST[s]), round(REAL[s]), round(GAP[s]), round(BE[s])) for s in SEASONS}, "rise", round(DAP_RISE, 1), "shares", round(FARMER_SHARE), round(SUB_SHARE), round(GAP_SHARE), "MOP", round(MOP_SUB), round(MOP_COST_26), round(MOP_GAP_26), "kh share", round(KH_SHARE, 1), "budget rise", round(BUDGET_RISE, 1))
