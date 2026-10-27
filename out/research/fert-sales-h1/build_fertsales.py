import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-fert-sales-h1.html'

# ---------------------------------------------------------------- data
# April-September (H1) sales, production, imports, million tonnes: Rural Voice and The Wire (citing
# industry/FAI data), 26 Oct 2026. Where only the 2026 value and % change were reported, the 2025 value
# is back-calculated here.
def base(now, pct):
    return now / (1 + pct / 100)

SALES = {  # product: (H1 2026, H1 2025)
    "Urea": (18.521, 19.307),
    "DAP": (4.364, base(4.364, -0.6)),
    "NPK complexes": (6.007, base(6.007, -22.2)),
    "MOP": (0.9658, base(0.9658, -11.7)),
    "SSP": (2.828, base(2.828, -1.4)),
}
PROD = {
    "Urea": (15.064, base(15.064, 4.3)),
    "DAP": (1.994, base(1.994, -0.3)),
    "NPK complexes": (3.822, 5.928),
    "MOP": (0.0, 0.0),            # India mines no potash
    "SSP": (2.631, base(2.631, -10.4)),
}
IMP = {
    "Urea": (5.589, 3.979),
    "DAP": (3.399, base(3.399, -11.2)),
    "NPK complexes": (1.386, base(1.386, -31.4)),
    "MOP": (1.679, base(1.679, 41.0)),
    "SSP": (0.0, 0.0),            # not imported in quantity
}
def pct(a, b): return (a / b - 1) * 100
CHG = {k: pct(*v) for k, v in SALES.items()}
SUPPLY = {k: (PROD[k][0] + IMP[k][0], PROD[k][1] + IMP[k][1]) for k in SALES}
GAP = {k: (SUPPLY[k][0] - SALES[k][0], SUPPLY[k][1] - SALES[k][1]) for k in SALES}   # + = stocks built

# September alone (same sources)
SEP = {"Urea": (2.705, 8.0), "DAP": (0.9836, 6.9), "NPK complexes": (0.6761, -39.3)}
SEP_NPK_PROD_CHG = -44.0
SEP_UREA_IMP, SEP_UREA_IMP_CHG = 0.843, -56.6

# Retail prices, Rs per 50 kg bag (urea: 45 kg bag)
BAG = {  # grade: (kharif 2025, kharif 2026, kg per bag, (N, P2O5, K2O) %)
    "DAP 18-46-0": (1350, 1350, 50, (18, 46, 0)),
    "NPK 12-32-16": (1720, 2450, 50, (12, 32, 16)),
    "NPK 10-26-26": (1720, 2450, 50, (10, 26, 26)),
    "NPK 16-16-16": (1475, 2050, 50, (16, 16, 16)),
    "Urea 46-0-0": (266.5, 266.5, 45, (46, 0, 0)),
}
def per_kg_nutrient(price, kg, grade):
    return price / (kg * sum(grade) / 100)
NUTP = {g: (per_kg_nutrient(b[0], b[2], b[3]), per_kg_nutrient(b[1], b[2], b[3])) for g, b in BAG.items()}

# NBS rates, Rs per kg of nutrient (kharif 2025, kharif 2026), from the P&K subsidy piece
NBS = {"N": (43.02, 47.32), "P": (43.60, 52.76), "K": (2.38, 2.38)}
def subsidy(grade, i):
    n, p, k = grade
    return 10 * (n * NBS["N"][i] + p * NBS["P"][i] + k * NBS["K"][i])
def revenue(g, i):
    b = BAG[g]
    return b[i] * 1000 / b[2] + subsidy(b[3], i)
assert round(subsidy((18, 46, 0), 1)) == 32787 and round(subsidy((18, 46, 0), 0)) == 27800
REV = {g: (revenue(g, 0), revenue(g, 1)) for g in ("DAP 18-46-0", "NPK 12-32-16", "NPK 10-26-26")}

MONSOON_DEF = 13           # % below long-period average, Jun-Sep 2026 (IMD, as reported)
KHARIF_AREA, KHARIF_AREA_CHG = 110.7, -1.2   # million ha, to 25 Sep 2026
NPK_PRICE_CHG = pct(2450, 1720)


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def chart_sales():
    order = sorted(CHG, key=lambda k: CHG[k])
    W, L, top, bh, gap, lab = 400, 10, 26, 18, 9, 108
    H = top + len(order) * (bh + gap) + 22
    zero = L + lab + 200
    sc = 200 / 25
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Change in fertiliser sales, April to September 2026 against a year earlier: NPK complexes {CHG["NPK complexes"]:.1f}%, MOP {CHG["MOP"]:.1f}%, urea {CHG["Urea"]:.1f}%, SSP {CHG["SSP"]:.1f}%, DAP {CHG["DAP"]:.1f}%.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Fertiliser sales, Apr&ndash;Sep 2026 vs a year earlier, %</text>',
         f'<line x1="{zero}" x2="{zero}" y1="{top - 4}" y2="{H - 20}" stroke="#adb5bd"/>']
    for i, k in enumerate(order):
        v = CHG[k]
        y = top + i * (bh + gap)
        w = abs(v) * sc
        col = "#a5402c" if v < -10 else "#1c5d99"
        s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="10" fill="#212529" text-anchor="end">{k}</text>')
        s.append(f'<rect x="{zero - w:.1f}" y="{y}" width="{max(w, 1.5):.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{zero + 5}" y="{y + 13}" font-size="10" fill="#212529">{v:+.1f}% &middot; {SALES[k][0]:.2f} Mt</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Industry data via Rural Voice and The Wire (26 Oct 2026). Mt = million tonnes sold in Apr&ndash;Sep 2026.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_price():
    grades = list(NUTP)
    W, L, top, bh, gap, lab = 400, 10, 40, 11, 12, 92
    H = top + len(grades) * (2 * bh + gap) + 22
    sc = (W - L - lab - 40) / 90
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Farm-gate price per kilogram of nutrient, kharif 2025 and kharif 2026: NPK grades rose by about two-fifths while DAP and urea were unchanged.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">What a farmer pays per kg of nutrient (N+P+K), Rs</text>',
         f'<rect x="{L}" y="20" width="9" height="9" fill="#adb5bd"/><text x="{L + 13}" y="28" font-size="9.5" fill="#212529">Kharif 2025</text>',
         f'<rect x="{L + 90}" y="20" width="9" height="9" fill="#a5402c"/><text x="{L + 103}" y="28" font-size="9.5" fill="#212529">Kharif 2026</text>']
    for i, g in enumerate(grades):
        y = top + i * (2 * bh + gap)
        a, b = NUTP[g]
        s.append(f'<text x="{L + lab - 6}" y="{y + bh + 4}" font-size="10" fill="#212529" text-anchor="end">{g}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{a * sc:.1f}" height="{bh}" fill="#adb5bd"/>')
        s.append(f'<text x="{L + lab + a * sc + 4:.1f}" y="{y + 9}" font-size="9" fill="#212529">{a:.0f}</text>')
        s.append(f'<rect x="{L + lab}" y="{y + bh}" width="{b * sc:.1f}" height="{bh}" fill="#a5402c"/>')
        s.append(f'<text x="{L + lab + b * sc + 4:.1f}" y="{y + bh + 9}" font-size="9" fill="#212529">{b:.0f}</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Bag prices per Rural Voice (Madhya Pradesh federation and company quotes); this blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def t_balance():
    rows = []
    for k in SALES:
        s, p, m, g = SALES[k], PROD[k], IMP[k], GAP[k]
        prod = "&mdash;" if p[0] == 0 else f"{p[0]:.2f} ({pct(*p):+.1f}%)"
        imp = "&mdash;" if m[0] == 0 else f"{m[0]:.2f} ({pct(*m):+.1f}%)"
        rows.append((k, f"{s[0]:.2f} ({CHG[k]:+.1f}%)", prod, imp, f"{g[1]:+.2f}", f"{g[0]:+.2f}"))
    return table(["Product", "Sales, Mt", "Production, Mt", "Imports, Mt", "Supply minus sales, 2025", "Supply minus sales, 2026"], rows)


def t_revenue():
    rows = []
    for g, (a, b) in REV.items():
        bg = BAG[g]
        rows.append((g, f"{bg[0]:,} &rarr; {bg[1]:,}", f"{subsidy(bg[3], 0):,.0f} &rarr; {subsidy(bg[3], 1):,.0f}", f"{a:,.0f} &rarr; {b:,.0f} ({pct(b, a):+.0f}%)"))
    return table(["Grade", "Bag price, Rs (kharif 2025 &rarr; 2026)", "Subsidy, Rs a tonne", "Seller&rsquo;s revenue, Rs a tonne"], rows)


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{CHG["NPK complexes"]:.1f}%</b><span>fall in sales of NPK complex fertilisers, April&ndash;September 2026</span></div>
<div class="gb-stat"><b>+{NPK_PRICE_CHG:.0f}%</b><span>rise in the price of a bag of NPK 12-32-16 or 10-26-26, to Rs 2,450</span></div>
<div class="gb-stat"><b>{CHG["DAP"]:.1f}%</b><span>change in DAP sales, its price held at Rs 1,350 a bag</span></div>
<div class="gb-stat"><b>{MONSOON_DEF}%</b><span>monsoon shortfall, the worst since 2015; kharif area fell only {abs(KHARIF_AREA_CHG):.1f}%</span></div>
</div>'''

body = f"""
{stats}

<p>Indian farmers bought less of every major fertiliser between April and September 2026 than a year earlier, according to industry figures reported by Rural Voice and The Wire. The falls were not even. Sales of NPK complex fertilisers dropped {abs(CHG["NPK complexes"]):.1f}% and potash (MOP) {abs(CHG["MOP"]):.1f}%, while urea fell {abs(CHG["Urea"]):.1f}% and DAP, the phosphate fertiliser most exposed to import prices, barely moved ({CHG["DAP"]:+.1f}%). In September&rsquo;s core-industries index, fertiliser output was down 11.7%.</p>
<p>The obvious explanation is the weather: the monsoon ended 13% short, the weakest since 2015. This blog&rsquo;s piece on the kharif subsidy, &ldquo;India Raised the DAP Subsidy 18% This Kharif. Imported DAP Still Costs About Rs 30,000 a Tonne More Than It Earns&rdquo;, suggested another: a subsidy that does not cover import costs. This piece tests both against the product-by-product figures. The answer is that sales fell most where prices rose, and least where the price was held.</p>

<h2 class="gb-h2">Sales fell most where the price moved</h2>
{chart_sales()}
<p>DAP and urea both have retail prices that did not change. Urea&rsquo;s is fixed by the government at Rs 266.50 for a 45 kg bag; DAP&rsquo;s is formally set by companies but has been held at Rs 1,350 a bag, which industry sources describe as an indirect cap. NPK complexes, which carry nitrogen, phosphate and potash in one granule, had no such restraint. In Madhya Pradesh the cooperative federation&rsquo;s price for a bag of 12-32-16 or 10-26-26 went from Rs 1,720 last kharif to Rs 2,450, and 16-16-16 from Rs 1,475 to Rs 2,050; companies quoted similar prices elsewhere.</p>
{chart_price()}
<p>Per kilogram of nutrient, a farmer now pays about Rs {NUTP["NPK 12-32-16"][1]:.0f} for 12-32-16 against Rs {NUTP["DAP 18-46-0"][1]:.0f} for DAP and Rs {NUTP["Urea 46-0-0"][1]:.0f} for urea. A farmer who switches from a complex fertiliser to DAP and urea pays less and gets no potash, which is what the sales show: NPK and MOP down sharply, DAP flat. Sales of single super phosphate (SSP), a cheap phosphate fertiliser, also held up ({CHG["SSP"]:+.1f}%).</p>

<h2 class="gb-h2">Why NPK prices rose and DAP&rsquo;s did not</h2>
{t_revenue()}
<p class="gb-note">Seller&rsquo;s revenue = bag price per tonne plus the nutrient-based subsidy at the season&rsquo;s per-kg rates (nitrogen Rs 43.02 &rarr; 47.32, phosphate Rs 43.60 &rarr; 52.76, potash Rs 2.38). Sulphur is ignored for these grades. This blog&rsquo;s arithmetic.</p>
<p>A company selling a tonne of DAP received about Rs {REV["DAP 18-46-0"][1]:,.0f} this kharif, {pct(*REV["DAP 18-46-0"][::-1]):.0f}% more than last year, entirely from the higher subsidy. Imported DAP cost about Rs 89,500 a tonne at May&rsquo;s tender price, so every imported tonne lost money, and DAP imports fell {abs(pct(*IMP["DAP"])):.1f}%. A tonne of 12-32-16 now earns about Rs {REV["NPK 12-32-16"][1]:,.0f}, {pct(*REV["NPK 12-32-16"][::-1]):.0f}% more, because the companies passed most of their higher costs to farmers. The shortfall on DAP was absorbed by companies and, through lower imports, by stocks; the shortfall on NPK was passed on, and farmers bought less.</p>
<p>Costs rose for a reason beyond phosphate prices. The closure of the Strait of Hormuz from 28 February cut global sulphur exports by about 45%, and China and Russia restricted exports of sulphuric acid and sulphur, according to Kpler. Sulphur and sulphuric acid go into phosphoric acid and into sulphur-bearing grades such as 20-20-0-13. Domestic NPK production fell {abs(pct(*PROD["NPK complexes"])):.1f}% in the half-year and 44% in September alone, and NPK imports fell {abs(pct(*IMP["NPK complexes"])):.1f}%.</p>

<h2 class="gb-h2">Demand or supply? The stock arithmetic</h2>
{t_balance()}
<p class="gb-note">Mt = million tonnes, April&ndash;September. 2025 values are back-calculated from the reported 2026 values and percentage changes where only those were given. Supply minus sales ignores opening stocks, so it shows direction, not the stock level. India produces no potash and imports little SSP.</p>
<p>Comparing what came into the country with what was sold separates the two explanations. For urea, production and imports exceeded sales by about {GAP["Urea"][0]:.1f} million tonnes, after falling {abs(GAP["Urea"][1]):.1f} million tonnes short a year earlier: urea was available and farmers bought less of it, which points to the weak monsoon. MOP looks the same: imports rose {pct(*IMP["MOP"]):.0f}% while sales fell. NPK is the opposite: about {SUPPLY["NPK complexes"][0]:.1f} million tonnes came in against {SALES["NPK complexes"][0]:.1f} million tonnes sold, so sales ran ahead of new supply and were met from stocks. NPK sales were limited by price and supply, not only by the rain.</p>
<p>September, when the monsoon was retreating, sharpens the contrast. Urea sales rose {SEP["Urea"][1]:.0f}% and DAP {SEP["DAP"][1]:.1f}% on the month a year earlier, but NPK fell {abs(SEP["NPK complexes"][1]):.1f}%. Rain alone would have moved them together.</p>

<h2 class="gb-h2">What it means for soils and for rabi</h2>
<p>The government has tried for years to move farmers away from urea and DAP towards balanced nutrition; in Punjab, Haryana and Uttar Pradesh the ratio of nitrogen to phosphate to potash applied is about 20:5:1, against a commonly cited ideal of 4:2:1. A season in which complex fertilisers became much dearer relative to DAP and urea pushes the ratio the wrong way. The kharif area sown was {KHARIF_AREA:.1f} million hectares, only {abs(KHARIF_AREA_CHG):.1f}% below last year, so less fertiliser went on almost the same land.</p>
<p>The rabi season, which uses more DAP, starts with DAP stocks built up and NPK stocks run down. Whether DAP stays at Rs 1,350 depends on rabi subsidy rates that had not been announced when this was written, and on whether phosphate and sulphur prices ease.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Department of Fertilizers should publish monthly sales, production, imports and closing stocks by product and state, as the Fertiliser Association of India&rsquo;s members already report them, so the effect of each season&rsquo;s subsidy rates can be measured within weeks.</li>
<li>Subsidy rates for complex fertilisers should be reviewed with DAP&rsquo;s, so that a policy that holds DAP&rsquo;s price does not make balanced grades relatively dearer.</li>
<li>The potash subsidy, unchanged at Rs 2.38 a kilogram, should be reviewed against the potash ratio the government wants farmers to use.</li>
<li>The government should publish the cost of the informal DAP price cap to companies each season, so that it is visible as policy rather than absorbed in balance sheets.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The April&ndash;September figures come from news reports citing industry sources and the Fertiliser Association of India; no official Department of Fertilizers release for the half-year could be opened. Several 2025 values are back-calculated from reported percentage changes. The NPK bag prices are mainly Madhya Pradesh cooperative prices and company quotes from May 2026, and prices of individual grades vary by company and state. Closing stocks were not available, so the supply-minus-sales figures ignore opening stocks. The relative weight of rain, price and supply cannot be separated precisely without state-level sales, which were not found.</p>
"""

sources = ("Sales, production and imports, April&ndash;September 2026 and September 2026: Rural Voice, &ldquo;Fertiliser Sales Decline Across All Categories in H1 FY27&rdquo; (26 October 2026) and The Wire (October 2026), both citing industry and FAI data; The Federal (26 October 2026). Fertiliser output in the core-industries index, September 2026: The Federal. "
           "NPK and DAP prices: Rural Voice on Madhya Pradesh&rsquo;s revised prices and company quotes (May 2026); urea price per PIB statements (Rs 266.50 a 45 kg bag). Subsidy rates: Cabinet decisions as summarised in this blog&rsquo;s piece on the kharif 2026 subsidy. Sulphur supply: Kpler (4 June 2026); CRU. "
           "Monsoon: IMD season-end data as reported by Business Standard (30 September 2026); kharif area to 25 September 2026: Ministry of Agriculture figures as reported. Nutrient ratio: Department of Fertilisers figures as reported by Rural Voice (March 2026). "
           "Per-kg nutrient prices, revenue per tonne, back-calculated 2025 values and supply-minus-sales are this blog&rsquo;s arithmetic (builder in the repository at out/research/fert-sales-h1/). Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/indias-fertiliser-import-bill-hits-18.html", "India&rsquo;s Fertiliser Import Bill Hits $18 Billion, and Parliament&rsquo;s Own Committee Explains Why"),
    ("https://masaladeutsch.blogspot.com/2026/08/nano-urea-works-as-supplement-and-fails.html", "Nano Urea Works as a Supplement and Fails as a Substitute. The Rulebook Now Agrees."),
    ("https://masaladeutsch.blogspot.com/2026/08/nature-versus-nurture-indias-fertiliser.html", "Nature Versus Nurture: India&rsquo;s Fertiliser-Fed Food Security"),
]

build("Agriculture · 27 October 2026",
      "India&rsquo;s Fertiliser Sales Fell Where Prices Rose. NPK Is Down 22% at Rs 2,450 a Bag; DAP, Held at Rs 1,350, Barely Moved",
      "Farmers bought less of every fertiliser this kharif, and the weak monsoon is part of it. But the steepest falls were in complex fertilisers whose price rose about 42%, while DAP, held at its old price despite a large import loss, was almost flat.",
      body, sources, related, OUT)
print({k: round(v, 1) for k, v in CHG.items()})
print("gap", {k: tuple(round(x, 2) for x in v) for k, v in GAP.items()})
print("nutp", {k: tuple(round(x, 1) for x in v) for k, v in NUTP.items()})
print("rev", {k: tuple(round(x) for x in v) for k, v in REV.items()})
