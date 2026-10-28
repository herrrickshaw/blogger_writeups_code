import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-drug-margins.html'

# ---------------------------------------------------------------- data
IPM_CR = 240672                     # Indian pharma market 2025, Rs crore (Pharmarack, as reported)
NONSCHED_SHARE = 0.82               # non-scheduled share of market (Standing Committee, Aug 2026, PRS summary)
NONSCHED_CR = IPM_CR * NONSCHED_SHARE

# Overcharging demands vs recoveries, Rs crore
RECOVERY = [  # label, demanded, recovered, source
    ("2016", 4928.09, 386.07, "Lok Sabha reply"),
    ("2018", 6058.07, 829.88, "Government reply to Parliament"),
    ("Mar 2026", 10029.8, 1582.4, "Explainer citing official data"),
]
UNREC_2025 = 8526                   # unrecovered, Rs crore, per committee (85% of demand)
UNREC_SHARE_2025 = 0.85
LITIG_SHARE = 0.70                  # share of unrecovered under litigation (committee)
DEMAND_IMPLIED = UNREC_2025 / UNREC_SHARE_2025
LITIG_CR = UNREC_2025 * LITIG_SHARE

# Stockist price vs MRP cited by the committee (Dec 2025 report), Rs per pack
MARKUPS = [("Cetirizine", 2.00, 21.06), ("Pantoprazole", 10.00, 102.00)]
GST = 0.05                          # GST on most medicines after the Sept 2025 rate cut (assumption stated in text)
CAP_LO, CAP_HI = 1 / (1 - 0.30), 1.30   # 30% "of MRP" vs 30% "on price to stockist" readings
CAP_HI_MULT, CAP_LO_MULT = max(CAP_LO, CAP_HI), min(CAP_LO, CAP_HI)

# Illustrative branded chain (BioSpectrum): C&F 3%, wholesaler 10%, retailer 20%, MRP Rs 100
MRP_STD = 100.0
PTR_STD = MRP_STD / 1.20
PTS_STD = PTR_STD / 1.10
CF_STD = PTS_STD / 1.03
STD_MULT = MRP_STD / PTS_STD

# 2019 and 2021 trade-margin actions
TMR_2019 = dict(drugs=42, brands=526, max_cut=90, savings_cr=984)
EX_2019 = [("Pemetrexed 500 mg injection", 22000, 2800), ("Erlotinib 150 mg tablets", 8800, 2400)]
TMR_2021 = dict(devices=5, reported=684, cut=620, max_cut=88, margin_lo=3, margin_hi=709)
TMR_2026 = dict(drugs=137, proposed=110, savings_cr=2500, max_cut=70)

# Jan Aushadhi example (study, prices 2019-21)
JA_TELMI = (7.19, 1.10)             # private median per tablet vs Jan Aushadhi, Rs


def pct_cut(old, new):
    return (1 - new / old) * 100


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def chart_recovery():
    W, L, top, bh, gap, lab = 400, 10, 40, 14, 14, 66
    H = top + len(RECOVERY) * (2 * bh + gap) + 24
    sc = (W - L - lab - 70) / 10500
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Overcharging demanded by NPPA against amounts recovered, Rs crore: 2016, 4,928 vs 386; 2018, 6,058 vs 830; March 2026, 10,030 vs 1,582.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Overcharging demanded vs recovered, Rs crore</text>',
         f'<rect x="{L}" y="20" width="9" height="9" fill="#868e96"/><text x="{L + 13}" y="28" font-size="9.5" fill="#212529">Demanded (cumulative)</text>',
         f'<rect x="{L + 150}" y="20" width="9" height="9" fill="#a5402c"/><text x="{L + 163}" y="28" font-size="9.5" fill="#212529">Recovered</text>']
    for i, (n, d, r, _) in enumerate(RECOVERY):
        y = top + i * (2 * bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + bh + 4}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{d * sc:.1f}" height="{bh}" fill="#868e96"/>')
        s.append(f'<text x="{L + lab + d * sc + 4:.1f}" y="{y + 11}" font-size="9.5" fill="#212529">{d:,.0f}</text>')
        s.append(f'<rect x="{L + lab}" y="{y + bh}" width="{r * sc:.1f}" height="{bh}" fill="#a5402c"/>')
        s.append(f'<text x="{L + lab + r * sc + 4:.1f}" y="{y + bh + 11}" font-size="9.5" fill="#212529">{r:,.0f} ({r / d * 100:.0f}%)</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Parliamentary replies (2016, 2018); March 2026 figure from an explainer of official data.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_markup():
    rows = [("Usual branded chain", STD_MULT, "#1c5d99"), ("30% cap, upper reading", CAP_HI_MULT, "#1c5d99")]
    rows += [(f"{n}, as sold", mrp / st, "#a5402c") for n, st, mrp in MARKUPS]
    W, L, top, bh, gap, lab = 400, 10, 30, 16, 8, 140
    H = top + len(rows) * (bh + gap) + 34
    sc = (W - L - lab - 50) / 11
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Retail price as a multiple of the price to stockist: about 1.3 in a usual branded chain and under a 30% cap, against about 10.5 for cetirizine and 10.2 for pantoprazole as cited by the parliamentary committee.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Retail price (MRP) as a multiple of the price to stockist</text>']
    for i, (n, v, col) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 12}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 12}" font-size="9.5" fill="#212529">{v:.1f}&times;</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Branded chain: illustrative 10% wholesale and 20% retail margins (BioSpectrum).</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Cetirizine, pantoprazole: committee report, Dec 2025. Excludes GST.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def t_rules():
    return table(["Rule", "Covers", "How the price is set", "Limit on increases"], [
        ("Ceiling price (DPCO 2013, scheduled drugs)", "Medicines on the National List of Essential Medicines; ceiling prices for about 530 medicines", "Simple average price to retailer of all brands with at least 1% market share, plus a 16% retailer margin", "Annual change by the wholesale price index"),
        ("Non-scheduled drugs (DPCO 2013, para 20)", f"About {NONSCHED_SHARE * 100:.0f}% of the market by value", "The company sets the launch price; no check on margins", "Up to 10% a year; breaches are recovered as overcharging"),
        ("Trade-margin cap (DPCO 2013, para 19, extraordinary powers)", f"42 cancer drugs (2019); five medical devices (2021); {TMR_2026['drugs']} cancer drugs (from 9 Nov 2026)", "Retail price limited to a set margin over the price to stockist or distributor", "Notified case by case; no standing framework"),
    ])


def t_actions():
    return table(["Action", "What was capped", "Reported effect"], [
        ("Feb 2019", f"{TMR_2019['drugs']} non-scheduled cancer drugs, 30% trade margin", f"{TMR_2019['brands']} brands cut MRP, by up to {TMR_2019['max_cut']}%; savings put at about Rs {TMR_2019['savings_cr']:,} crore a year"),
        ("July 2021", f"{TMR_2021['devices']} devices (oximeters, BP monitors, nebulisers, thermometers, glucometers), 70% margin on price to distributor", f"Pre-cap margins {TMR_2021['margin_lo']}% to {TMR_2021['margin_hi']}%; {TMR_2021['cut']} of {TMR_2021['reported']} reported brands ({TMR_2021['cut'] / TMR_2021['reported'] * 100:.0f}%) cut MRP, by up to {TMR_2021['max_cut']}%"),
        ("Oct 2026 (S.O. 5690(E), from 9 Nov)", f"{TMR_2026['drugs']} non-scheduled cancer drugs, all strengths and combinations, 30% margin plus GST", f"Prices to fall by up to {TMR_2026['max_cut']}%, varying by drug; savings put at about Rs {TMR_2026['savings_cr']:,} crore a year"),
    ])


def t_examples():
    rows = []
    for n, old, new in EX_2019:
        rows.append((n, f"{old:,}", f"{new:,}", f"{pct_cut(old, new):.0f}%"))
    return table(["2019 example", "MRP before (Rs)", "MRP after (Rs)", "Cut"], rows)


def t_whatif():
    rows = []
    for n, st, mrp in MARKUPS:
        lo = st * CAP_LO_MULT * (1 + GST)
        hi = st * CAP_HI_MULT * (1 + GST)
        rows.append((n, f"{st:.2f}", f"{mrp:.2f}", f"{(mrp / st - 1) * 100:,.0f}%", f"{lo:.2f}&ndash;{hi:.2f}", f"{pct_cut(mrp, hi):.0f}&ndash;{pct_cut(mrp, lo):.0f}%"))
    return table(["Pack cited by the committee", "Stockist price (Rs)", "MRP (Rs)", "Markup", "MRP under a 30% cap, with 5% GST (Rs)", "Implied cut"], rows)


TOT_SAVE = TMR_2019['savings_cr'] + TMR_2026['savings_cr']

stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{TMR_2026['drugs']}</b><span>cancer drugs whose trade margins are capped at 30% from 9 November 2026</span></div>
<div class="gb-stat"><b>{NONSCHED_SHARE * 100:.0f}%</b><span>of India&rsquo;s medicine sales by value are non-scheduled: no ceiling price, no margin limit</span></div>
<div class="gb-stat"><b>{RECOVERY[-1][2] / RECOVERY[-1][1] * 100:.0f}%</b><span>of the Rs {RECOVERY[-1][1]:,.0f} crore NPPA has demanded for overcharging had been recovered by March 2026</span></div>
<div class="gb-stat"><b>{MARKUPS[0][2] / MARKUPS[0][1]:.1f}&times;</b><span>a cetirizine pack&rsquo;s MRP over its stockist price, as cited by a parliamentary committee</span></div>
</div>'''

body = f"""
{stats}

<p>On 17 October 2026 the National Pharmaceutical Pricing Authority (NPPA) capped the trade margin on {TMR_2026['drugs']} cancer medicines at 30%, from 9 November. Prices are expected to fall by up to {TMR_2026['max_cut']}%, and the government puts the saving at about Rs {TMR_2026['savings_cr']:,} crore a year. The list grew from the {TMR_2026['proposed']} drugs first proposed. Two months earlier, the Lok Sabha&rsquo;s Standing Committee on Chemicals and Fertilizers reported that hospitals and pharmacies routinely sell medicines at 20&ndash;60% below their printed maximum retail price (MRP), which it read as evidence of large margins built into the price, and asked for a permanent trade-margin framework.</p>
<p>This piece explains how India controls medicine prices, why most medicines fall outside those controls, what earlier margin caps did, and why the regulator recovers so little of what it says companies overcharged.</p>

<h2 class="gb-h2">Two kinds of medicine, two kinds of control</h2>
{t_rules()}
<p>Most of the market is untouched by price control. India&rsquo;s medicine sales were about Rs {IPM_CR / 1e5:.2f} lakh crore in 2025, and the committee puts the non-scheduled share at {NONSCHED_SHARE * 100:.0f}%, about Rs {NONSCHED_CR / 1e5:.2f} lakh crore. For these, the only rule is that the MRP cannot rise by more than 10% a year. The launch price, and the margin in it, are left to the company. A 2023 Delhi High Court ruling (Bharat Serums) narrowed even that rule: the regulator can monitor non-scheduled prices and recover overcharges, but a breach does not take away a company&rsquo;s right to raise prices later.</p>
<p>The committee&rsquo;s December 2025 report showed what this allows. It cited a cetirizine pack with an MRP of Rs {MARKUPS[0][2]} against a stockist price of Rs {MARKUPS[0][1]:.0f}, a markup of {(MARKUPS[0][2] / MARKUPS[0][1] - 1) * 100:,.0f}%, and pantoprazole at Rs {MARKUPS[1][2]:.0f} against Rs {MARKUPS[1][1]:.0f}, a markup of {(MARKUPS[1][2] / MARKUPS[1][1] - 1) * 100:,.0f}%. Other common medicines were marked up by 600% to 1,800%. The public cannot see stockist prices, so it cannot see these margins.</p>

<h2 class="gb-h2">How big a margin is normal</h2>
{chart_markup()}
<p>In a usual branded-medicine chain, a wholesaler takes about 10% and a pharmacy about 20%, so the MRP ends up about {STD_MULT:.2f} times the price to stockist. A 30% cap allows about {CAP_LO_MULT:.2f} to {CAP_HI_MULT:.2f} times, depending on whether the 30% is read as a margin on the stockist price or a share of the MRP; reports describe it both ways, and the notification ties it to the March 2026 price to stockist. Either way, a 30% cap is close to what an ordinary branded chain already earns. It bites only where margins are far above normal: on &ldquo;trade generics&rdquo;, sold to pharmacies with very high margins so that they push them, and on expensive specialty drugs like cancer medicines. The Competition Commission&rsquo;s 2021 market study found that companies compete for pharmacy shelf space mainly by offering higher margins, especially on trade generics.</p>
{t_whatif()}
<p class="gb-note">An illustration of what a 30% cap would mean if it applied to these two packs; it does not. GST is assumed at 5%, the rate on most medicines after September 2025. The committee did not name the brands.</p>

<h2 class="gb-h2">What earlier caps did</h2>
{t_actions()}
{t_examples()}
<p>Every margin cap so far has cut prices sharply because the margins it removed were large. In 2019, {TMR_2019['brands']} cancer-drug brands lowered their MRPs, by up to {TMR_2019['max_cut']}%. In 2021, {TMR_2021['cut'] / TMR_2021['reported'] * 100:.0f}% of reported brands of five home medical devices cut prices after the regulator found margins of up to {TMR_2021['margin_hi']}%. But each cap was issued under the order&rsquo;s emergency powers for a named list. The committee noted that there is still no timeline for turning trade-margin rationalisation into a standing part of the price-control order, and the 2026 list covers only cancer drugs.</p>

<h2 class="gb-h2">Why overcharging is rarely repaid</h2>
{chart_recovery()}
<p>When a company charges more than a ceiling price or raises a non-scheduled price by more than 10%, the regulator demands the excess back with interest. The demands have grown and the recoveries have not kept up. By March 2026 the regulator had demanded about Rs {RECOVERY[-1][1]:,.0f} crore and recovered about Rs {RECOVERY[-1][2]:,.0f} crore, {RECOVERY[-1][2] / RECOVERY[-1][1] * 100:.0f}%. The committee put the unrecovered sum at Rs {UNREC_2025:,} crore, and found {LITIG_SHARE * 100:.0f}% of it, about Rs {LITIG_CR:,.0f} crore, tied up in court, some cases for more than 20 years. It recommended a fast-track mechanism for cases not in court and a legal cell inside the regulator for the rest.</p>

<h2 class="gb-h2">The cheaper alternative already on sale</h2>
<p>Jan Aushadhi Kendras, the government&rsquo;s generic-medicine pharmacies, price each medicine at no more than half the average of the top three brands, and often much less. One study found telmisartan 40 mg at a median Rs {JA_TELMI[0]} a tablet in private pharmacies against Rs {JA_TELMI[1]} at Jan Aushadhi, {pct_cut(*JA_TELMI):.0f}% less. That gap is roughly the size of the margins the committee found, which suggests the margin, more than the cost of making the medicine, is what separates the two prices. This blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/09/jan-aushadhi-sells-2439-products-heres.html">piece on Jan Aushadhi&rsquo;s 2,439 products</a> looks at where their ingredients come from.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Department of Pharmaceuticals should add a standing trade-margin rule to the Drugs (Prices Control) Order, as the committee asked: a cap on the markup from stockist price to MRP for all non-scheduled formulations above a set level, starting with trade generics, rather than lists notified one at a time.</li>
<li>The price to stockist should be published alongside the MRP for every pack, from the data companies already file on the regulator&rsquo;s IPDMS system, so that buyers and hospitals can see the margin.</li>
<li>The regulator should publish its overcharging cases with the company, the amount demanded, the amount recovered and the age of each case, every quarter.</li>
<li>Pharmacies should be required to show the Jan Aushadhi price of the same molecule where one exists.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The October 2026 notification (S.O. 5690(E)) and the committee&rsquo;s report could not be opened directly; their contents come from news reports and PRS Legislative Research&rsquo;s summary. Reports describe the 2026 cap both as 30% over the price to stockist and as 30% of the MRP; the piece shows both. The March 2026 recovery figures come from an explainer of official data and differ slightly from the committee&rsquo;s (Rs {RECOVERY[-1][1] - RECOVERY[-1][2]:,.0f} crore unrecovered against Rs {UNREC_2025:,} crore). The savings estimates (Rs {TMR_2019['savings_cr']:,} crore for 2019, Rs {TMR_2026['savings_cr']:,} crore for 2026) are official claims, not measured outcomes. No systematic data on margins across molecules was found; the cetirizine and pantoprazole figures are the committee&rsquo;s examples, and the branded-chain margins are an industry illustration. The Jan Aushadhi telmisartan comparison uses 2019&ndash;21 prices. Nothing here is medical advice; patients should not change medicines without a doctor.</p>
"""

sources = ("Standing Committee on Chemicals and Fertilizers, review of the role of the National Pharmaceutical Pricing Authority (presented 6 August 2026), via PRS Legislative Research&rsquo;s report summary; the committee&rsquo;s December 2025 report on non-scheduled drug prices, via Vision IAS, Outlook and The Tribune. "
           "2026 trade-margin cap: S.O. 5690(E) of 17 October 2026 and NPPA&rsquo;s 151st meeting, as reported by All India Radio, ThePrint, Moneylife, Upstox, Deccan Chronicle, Morung Express and TeamLease RegTech. "
           "2019 cap on 42 cancer drugs: NPPA via Business Insider, Medical Dialogues, Indian Pharma Post and BioSpectrum; ESMO 2021 abstract on savings. 2021 device caps: PIB (July 2021), ThePrint, Indian Pharma Post. "
           "DPCO 2013 ceiling-price method and para 20: Lok Sabha replies, Vikaspedia FAQ, Department of Pharmaceuticals review orders; Bharat Serums judgment via SCC Online and ELP. "
           "Overcharging recoveries: Lok Sabha replies (2016, 2018) via Medical Dialogues; March 2026 figures via Civilsdaily. "
           "Market size: Pharmarack via The Tribune (2025). Trade margins in branded and trade generics: BioSpectrum; Competition Commission of India market study (2021) via Khaitan &amp; Co. Jan Aushadhi pricing rule: Ministry of Health; telmisartan prices from a peer-reviewed study (PMC10471490). "
           "Markups, capped-price illustrations and recovery shares are this blog&rsquo;s arithmetic.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/09/jan-aushadhi-sells-2439-products-heres.html", "Jan Aushadhi Sells 2,439 Products. Here&rsquo;s What We Actually Know About Where Their APIs Come From."),
    ("https://masaladeutsch.blogspot.com/2026/08/indias-two-tracks-of-health-cover-and.html", "India&rsquo;s Two Tracks of Health Cover, and Where They Actually Meet"),
    ("https://masaladeutsch.blogspot.com/2026/09/indias-60000-crore-api-push-traced-to.html", "India&rsquo;s Rs 60,000 Crore API Push, Traced to Its Six Actual Schemes"),
]

build("Healthcare · 28 October 2026",
      "India Capped Margins on 137 Cancer Drugs. Common Medicines Outside Price Control Carry Markups of Up to 1,800%",
      "From 9 November, trade margins on 137 cancer medicines are capped at 30%. A parliamentary committee found pharmacies discounting 20&ndash;60% off printed prices and markups of 600% to 1,800% on common drugs that sit outside price control, and the regulator has recovered about a sixth of what it says companies overcharged.",
      body, sources, related, OUT)
print("nonsched cr", round(NONSCHED_CR), "std mult", round(STD_MULT, 3), "cap", round(CAP_LO_MULT, 3), round(CAP_HI_MULT, 3), "litig", round(LITIG_CR), "implied demand", round(DEMAND_IMPLIED))
