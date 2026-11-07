"""Hyaluronic acid and other cosmetic ingredients from India's maize crop (7 Nov 2026).

Run: PYTHONPATH=tools/postbuild python3 out/research/maize-cosmetics/build_maizecosmetics.py
Every derived figure in the post is computed here. Conversion yields marked ASSUMPTION are this
blog's round-number process assumptions from published literature, not plant data.
"""
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-maize-cosmetics.html'
FX = 88.0          # Rs per US$, ASSUMPTION, in line with rates used elsewhere on this blog

# --- maize: how much, and at what price ---------------------------------------------------------
MAIZE_26, MAIZE_25 = 55.093, 43.409     # Mt; 3rd Advance Estimate 2025-26 vs 2024-25 (PIB, 27 May 2026)
MSP = 2410                               # Rs/quintal, 2026-27
SPOT_LO, SPOT_HI = 17950, 21000          # Rs/t, May 2026 spot range (USDA Post, via BusinessLine)
ETH_DIVERT = 12.8                        # Mt maize to ethanol, 2025-26 (P) (APEDA market dashboard)
EXPORTS = 2.4                            # Mt, MY2025-26 forecast (USDA Post)
OFFERED, REQUIRED = 1776, 1050           # crore litres offered vs needed, ESY 2025-26 (earlier posts)
ETH_PRICE = 68.86                        # Rs/L, maize ethanol, ESY 2026-27 tender
ETH_YIELD = 380                          # litres per tonne of maize (used across this blog)
GLUCOSE = 0.65                           # t glucose per t maize by wet milling, ASSUMPTION

rise = MAIZE_26 - MAIZE_25
rise_pct = rise / MAIZE_25 * 100
spot_mid = (SPOT_LO + SPOT_HI) / 2
below_msp = (1 - spot_mid / (MSP * 10)) * 100
eth_rev = ETH_YIELD * ETH_PRICE                  # Rs of ethanol revenue per tonne of maize
grain_share = spot_mid / eth_rev * 100           # grain cost as % of that revenue
unsold = OFFERED - REQUIRED

# --- hyaluronic acid ----------------------------------------------------------------------------
HA_LAB_YIELD = (0.19, 0.22)      # g HA per g glucose (Zhang 2023, S. zooepidemicus; Cheng 2016, C. glutamicum)
HA_YIELD = 0.15                  # recovered after purification losses, ASSUMPTION
HA_WORLD = 1285                  # t, forecast global sales of HA raw material in 2026 (Frost & Sullivan)
HA_CHINA_SHARE = 82              # % of world output, 2021 (Bloomage, citing Frost & Sullivan)
HA_IMPORT_PRICE = 86.75          # US$/kg, cosmetic HA shipment from China, March 2024 (customs record)
HA_COS_LO, HA_COS_HI = 65, 200   # US$/kg, Chinese cosmetic-grade export range (2025 market report)
HA_PHARMA = 1100                 # US$/kg and up, pharmaceutical grade (same report)

ha_per_t = GLUCOSE * HA_YIELD * 1000              # kg HA per tonne of maize
maize_for_world = HA_WORLD / (ha_per_t / 1000)    # t maize to make the world's HA
share_of_crop = maize_for_world / (MAIZE_26 * 1e6) * 100
maize_100t = 100 / (ha_per_t / 1000)              # t maize for a 100 t/yr HA plant
glucose_per_kg_ha = 1 / HA_YIELD                  # kg glucose per kg HA
GLUCOSE_PRICE = 40                                # Rs/kg of glucose, ASSUMPTION (bulk liquid glucose, dry basis)
feed_cost_ha = glucose_per_kg_ha * GLUCOSE_PRICE  # Rs of sugar per kg of HA
ha_price_rs = HA_IMPORT_PRICE * FX
feed_share_ha = feed_cost_ha / ha_price_rs * 100

# --- the menu of glucose-derived ingredients ----------------------------------------------------
# name, g product per g glucose (ASSUMPTION from literature), US$/kg, India's trade position, note
MENU = [
    ("Sorbitol (70% solution)", 1.00, 0.52,
     "net exporter: $61.0m in 2024", "humectant in toothpaste, creams"),
    ("Citric acid", 0.75, 0.70,
     "imported 141,747 t in 2024, 95% from China", "chelator, pH control"),
    ("Lactic acid", 0.85, 1.61,
     "imported 6,217 t in 2024", "exfoliant, pH control"),
    ("Erythritol", 0.45, 1.60,
     "no separate code; China has ~380,000 t capacity", "cooling agent, oral care"),
    ("1,3-propanediol", 0.51, 1.80,
     "no Indian plant found", "glycol replacement, solvent"),
    ("Xanthan gum", 0.65, 2.50,
     "imported mostly from China at about $2.50/kg", "thickener"),
    ("Alkyl polyglucosides", 0.50, 2.50,
     "no Indian plant found", "mild surfactant"),
    ("Hyaluronic acid (cosmetic)", HA_YIELD, HA_IMPORT_PRICE,
     "imported, chiefly from China", "humectant"),
]

def per_t_maize(y, price):
    """Rupees of product revenue from one tonne of maize."""
    return GLUCOSE * y * 1000 * price * FX

def maize_for_10k(y):
    """Tonnes of maize behind 10,000 t of product."""
    return 10000 / y / GLUCOSE

VAL = {n: per_t_maize(y, p) for n, y, p, _, _ in MENU}
VAL["As grain, at the May 2026 spot price"] = spot_mid
VAL["As ethanol, at the 2026-27 tender price"] = eth_rev
ha_vs_eth = VAL["Hyaluronic acid (cosmetic)"] / eth_rev

# --- sanity checks ------------------------------------------------------------------------------
assert round(rise_pct) == 27 and round(below_msp) == 19
assert 90 < ha_per_t < 105                       # ~97 kg HA per tonne of maize
assert 12000 < maize_for_world < 14000           # world HA fits inside ~13,000 t of maize
assert share_of_crop < 0.03
assert 70 < grain_share < 80                     # grain is three-quarters of ethanol revenue
assert feed_share_ha < 5                         # sugar is a few per cent of HA's price
assert 25 < ha_vs_eth < 32

L = lambda x: f"{x:,.0f}"

def table(head, rows, note=None):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    t = f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'
    if note:
        t += f'<p class="gb-note">{note}</p>'
    return t

# --- figure: value per tonne of maize, log scale -------------------------------------------------
def chart():
    import math
    rows = [("As grain (May 2026 spot)", VAL["As grain, at the May 2026 spot price"]),
            ("As ethanol (2026-27 price)", VAL["As ethanol, at the 2026-27 tender price"]),
            ("As citric acid", VAL["Citric acid"]),
            ("As sorbitol", VAL["Sorbitol (70% solution)"]),
            ("As 1,3-propanediol", VAL["1,3-propanediol"]),
            ("As lactic acid", VAL["Lactic acid"]),
            ("As xanthan gum", VAL["Xanthan gum"]),
            ("As hyaluronic acid", VAL["Hyaluronic acid (cosmetic)"])]
    W, LAB, top, bot = 360, 128, 54, 42
    rh, gap = 20, 7
    H = top + len(rows) * (rh + gap) + bot
    lo, hi = 4.0, 6.0                              # log10 bounds: Rs 10,000 to Rs 1,000,000
    plot_w = W - LAB - 10
    x_of = lambda v: LAB + (math.log10(v) - lo) / (hi - lo) * plot_w
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Revenue from one tonne of maize by end use, on a logarithmic scale: about Rs 19,000 as grain, Rs 26,000 as ethanol and Rs 744,000 as cosmetic-grade hyaluronic acid.">',
         '<text x="8" y="13" font-size="12" fill="#495057">What one tonne of maize is worth, by end use</text>',
         '<text x="8" y="26" font-size="9.5" fill="#6c757d">Rupees of product, at 0.65 t glucose per tonne. Log scale.</text>']
    for g, lab in ((1e4, "10k"), (1e5, "1 lakh"), (1e6, "10 lakh")):
        x = x_of(g)
        s.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{top - 6}" y2="{top + len(rows) * (rh + gap) - gap + 2}" stroke="#dee2e6"/>')
        anc = "end" if x > W - 30 else "middle"
        s.append(f'<text x="{min(x, W - 3):.1f}" y="{top - 10}" font-size="9" fill="#6c757d" text-anchor="{anc}">{lab}</text>')
    for i, (lab, v) in enumerate(rows):
        y = top + i * (rh + gap)
        w = max(2.0, x_of(v) - LAB)
        s.append(f'<text x="{LAB - 6}" y="{y + rh - 6:.0f}" font-size="10" fill="#212529" text-anchor="end">{lab}</text>')
        s.append(f'<rect x="{LAB}" y="{y}" width="{w:.1f}" height="{rh}" fill="#1c5d99"/>')
        txt = f"Rs {L(v)}"
        if LAB + w + 6 * len(txt) > W - 4:        # label would run off the edge: set it inside the bar
            s.append(f'<text x="{LAB + w - 5:.1f}" y="{y + rh - 6:.0f}" font-size="9.5" fill="#fff" text-anchor="end">{txt}</text>')
        else:
            s.append(f'<text x="{LAB + w + 5:.1f}" y="{y + rh - 6:.0f}" font-size="9.5" fill="#212529">{txt}</text>')
    s.append(f'<text x="8" y="{H - 24}" font-size="9" fill="#6c757d">Product prices: India import or export unit values, 2024&ndash;26.</text>')
    s.append(f'<text x="8" y="{H - 12}" font-size="9" fill="#6c757d">Revenue, not margin: it buys none of the plant, power or purification.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'

stats = f"""<div class="gb-stats">
<div class="gb-stat"><b>{MAIZE_26} Mt</b><span>India&rsquo;s record maize crop in 2025-26, {rise_pct:.0f}% above the year before, with spot prices about {below_msp:.0f}% under the support price</span></div>
<div class="gb-stat"><b>{L(maize_for_world)} t</b><span>of maize would carry the world&rsquo;s whole year of hyaluronic acid: {share_of_crop:.3f}% of India&rsquo;s crop</span></div>
<div class="gb-stat"><b>{feed_share_ha:.0f}%</b><span>of cosmetic hyaluronic acid&rsquo;s import price is the sugar it is made from; in ethanol, grain is about {grain_share:.0f}%</span></div>
<div class="gb-stat"><b>{HA_CHINA_SHARE}%</b><span>of the world&rsquo;s hyaluronic acid came from China in 2021, with one firm supplying 44%</span></div>
</div>"""

body = f"""
{stats}

<p>India has just harvested a record {MAIZE_26} million tonnes of maize, {rise_pct:.0f}% more than the year before, and spot prices have spent months below the support price of Rs {L(MSP)} a quintal. The obvious question is what else the crop could become. Ethanol already takes about {ETH_DIVERT} million tonnes of it. The fashionable answer is cosmetics: hyaluronic acid, the humectant in half the serums on a chemist&rsquo;s shelf, is made by fermenting glucose, and glucose comes from maize starch.</p>

<p>This piece works through the arithmetic of that idea, for hyaluronic acid and for the other ingredients a maize wet mill could feed. The short version: the chemistry works, the volumes do not. Cosmetic ingredients are worth a great deal per tonne and consume almost no grain. Treating them as an outlet for a maize surplus is a category error &mdash; but treating them as an import-substitution target is not.</p>

<h2 class="gb-h2">Is there a surplus, and of what?</h2>

<p>The crop is genuinely large. The Agriculture Ministry&rsquo;s third advance estimate for 2025-26 puts maize at {MAIZE_26} million tonnes against {MAIZE_25} million the previous year, a rise of {rise:.1f} million tonnes. Average spot prices in the major producing states in May 2026 ran between Rs {L(SPOT_LO)} and Rs {L(SPOT_HI)} a tonne, by the United States Department of Agriculture&rsquo;s India office, roughly {below_msp:.0f}% below the minimum support price. The USDA office raised its estimate of India&rsquo;s maize exports for the year to {EXPORTS} million tonnes and cut imports to 50,000 tonnes. Cheap maize, moving out of the country: that is what a surplus looks like.</p>

<p>But the surplus that matters for a fermentation business is not grain. India&rsquo;s distilleries offered oil marketing companies {L(OFFERED)} crore litres of ethanol for the 2025-26 supply year against a requirement of about {L(REQUIRED)} crore litres, so roughly {L(unsold)} crore litres of capacity had no buyer. The spare asset is fermenter volume and the starch-to-glucose plant in front of it, not the maize. A tonne of grain can be bought by anyone; a sterile, instrumented fermenter with a trained crew cannot.</p>

<p>Maize&rsquo;s existing industrial uses show the same thing. An ANGRAU market outlook puts the split at about 54% poultry and animal feed, 25% ethanol, 14% starch and 7% food. Starch is the entry point for everything in this piece.</p>

<h2 class="gb-h2">Hyaluronic acid: the chemistry is easy, the scale is tiny</h2>

<p>Hyaluronic acid (HA) is a long sugar chain &mdash; a polysaccharide &mdash; that holds water, which is why it turns up in serums, eye drops and joint injections. It used to be extracted from rooster combs. Since the 1980s it has been made by fermentation: a bacterium is fed glucose and secretes HA, which is then precipitated, filtered and dried.</p>

<p>Published yields are consistent. A 2023 study of <i>Streptococcus zooepidemicus</i>, the industrial workhorse, reported {HA_LAB_YIELD[0]} grams of HA per gram of glucose in batch fermentation. A 2016 paper on an engineered <i>Corynebacterium glutamicum</i>, a safer organism with no toxins, reported {HA_LAB_YIELD[1]} g/g. Allowing for purification losses, this piece assumes {HA_YIELD} grams of saleable HA per gram of glucose, and {GLUCOSE} tonnes of glucose from a tonne of maize. Both are this blog&rsquo;s assumptions, not plant figures.</p>

<p>That gives about <b>{ha_per_t:.0f} kg of hyaluronic acid per tonne of maize</b>. Now set it against demand. Frost &amp; Sullivan forecasts global sales of HA raw material at about {L(HA_WORLD)} tonnes in 2026. At {ha_per_t:.0f} kg a tonne, the entire world&rsquo;s supply would come out of <b>{L(maize_for_world)} tonnes of maize</b> &mdash; {share_of_crop:.3f}% of India&rsquo;s crop, or about {maize_100t:.0f} tonnes for a respectable 100-tonne-a-year plant. A single mid-sized distillery eats more grain in a week.</p>

<p>The value runs the other way. A customs record from March 2024 shows cosmetic-grade HA powder landing from China at about ${HA_IMPORT_PRICE}/kg; a 2025 market report puts Chinese cosmetic-grade export prices at ${HA_COS_LO}&ndash;{HA_COS_HI}/kg and pharmaceutical grade above ${L(HA_PHARMA)}/kg. At the import price, the HA from one tonne of maize is worth about Rs {L(VAL["Hyaluronic acid (cosmetic)"])}, against Rs {L(eth_rev)} as ethanol &mdash; roughly {ha_vs_eth:.0f} times more.</p>

<p>That multiple is seductive and mostly meaningless, because the grain is not the cost. Making a kilogram of HA needs about {glucose_per_kg_ha:.1f} kg of glucose; at Rs {GLUCOSE_PRICE} a kilo that is Rs {L(feed_cost_ha)}, or about {feed_share_ha:.0f}% of what the kilogram sells for. Everything else &mdash; the fermenter, the sterile air, the precipitation solvent, the drying, the testing &mdash; is the business. In ethanol it is the other way round: maize at the May spot price is about {grain_share:.0f}% of the revenue from the ethanol it yields. Ethanol is a grain business with a factory attached. Hyaluronic acid is a factory business with a little grain attached.</p>

<p>Which is why a cheap maize crop is close to irrelevant to whether India makes its own HA, and why China&rsquo;s dominance is not about corn. China supplied {HA_CHINA_SHARE}% of world output in 2021, with Bloomage Biotech alone at 44%; the top four suppliers by volume were all Chinese. Bloomage says its fermentation yield went from under 3 g/L when it started in 2000 to 12&ndash;14 g/L. That is two decades of strain and process work, not a feedstock advantage.</p>

<h2 class="gb-h2">What India buys, and who in India makes it</h2>

<p>India&rsquo;s HA imports are hard to size because they share a customs line with everything else in the natural-polymer basket. India imported $71.9 million of goods under HS 391390 in 2024, 11,338 tonnes in all, half of it by value from China. Most of that tonnage is xanthan gum at about $2.50/kg; HA arrives in 50- and 100-kilogram lots at eighty-odd dollars a kilo. A separate eight-digit code for hyaluronic acid would make the number knowable; there is not one.</p>

<p>There is Indian activity, all of it small and recent:</p>

<ul>
<li>Cosmos Bio, incubated at C-CAMP in Bengaluru, makes recombinant ectoine and hyaluronic acid and has taken BIRAC and Karnataka state grants.</li>
<li>Cellarim Labs markets a cell-free HA, made with enzymes rather than live cells, which it describes as India&rsquo;s first.</li>
<li>Stelis Biopharma holds an Indian patent, granted in 2020, on producing sodium hyaluronate by fermenting a <i>Streptococcus</i> strain free of hyaluronidase activity.</li>
<li>A northern-region science and technology cluster reports scaling a non-pathogenic <i>Bacillus</i>-based HA process from laboratory proof to pilot readiness.</li>
</ul>

<p>Several Indian websites advertise themselves as HA &ldquo;manufacturers&rdquo;; the listings carry the HS code for imported polymer and prices from Rs 200 to Rs 10,000 a kilogram, which is the spread of a trading business, not a plant. A market study of the Asia-Pacific region describes India as structurally import-dependent for all but the lowest cosmetic grades, importing bulk powder and doing the formulation locally. This piece found no evidence of commercial-scale Indian HA fermentation.</p>

<h2 class="gb-h2">The rest of the menu, ranked by what it would actually absorb</h2>

<p>Hyaluronic acid is the glamorous end of a long list. The same glucose stream feeds a dozen ingredients that go into cosmetics and personal care, and the cheaper ones consume real tonnage.</p>

{table(["Product", "Maize, t", "$/kg", "Rs/t maize"],
       [(n, f"{maize_for_10k(y) / 1000:.0f},000 t" if maize_for_10k(y) >= 1000 else f"{maize_for_10k(y):,.0f} t",
         f"{p:,.2f}" if p < 10 else f"{p:,.0f}", L(per_t_maize(y, p))) for n, y, p, _, _ in MENU],
       "The maize column is the tonnage behind 10,000 t of product, and the last column the revenue from one tonne of maize. Both use this blog&rsquo;s assumed 0.65 t of glucose per tonne of maize and the literature yields in the builder; they are indicative. Prices are India import or export unit values for 2024, except hyaluronic acid (a March 2024 shipment) and erythritol (Chinese market price).")}

{chart()}

<p>Read the table from the bottom up. Hyaluronic acid pays Rs {L(VAL["Hyaluronic acid (cosmetic)"])} a tonne of maize and will never take more than a few thousand tonnes of grain. Xanthan gum and lactic acid pay far less per tonne but could absorb tens of thousands. Citric acid is the volume story: India imported {L(141747)} tonnes in 2024, worth $105.2 million, and 95% of it came from China. Replacing that import alone would take roughly {L(141747 / 0.75 / GLUCOSE)} tonnes of maize &mdash; still under half a per cent of the crop, but twenty times what the world&rsquo;s hyaluronic acid needs, and against a competitor whose capacity the European Commission says grew by 780,000 tonnes between 2019 and 2025.</p>

<p>Sorbitol shows what India can already do. Gulshan Polyols runs 72,000 tonnes a year of it at Jhagadia, integrated from maize through starch and dextrose, and India exported $61.0 million of sorbitol in 2024. It is a humectant in toothpaste and creams, it is made from maize glucose, and nobody calls it a cosmetics breakthrough.</p>

<h2 class="gb-h2">What stands in the way</h2>

<p><b>Purity, not yield.</b> Cosmetic grade is a powder specification. Injectable grade is a sterile, endotoxin-controlled, pharmacopoeia-compliant product, and that is where the price is: Chinese pharmaceutical-grade HA sells above ${L(HA_PHARMA)}/kg against ${HA_COS_LO}&ndash;{HA_COS_HI} for cosmetic. The organism choice follows from this. <i>Streptococcus zooepidemicus</i> is an animal pathogen that makes toxins; engineered <i>Bacillus subtilis</i> and <i>Corynebacterium glutamicum</i> are endotoxin-free and are what the newer processes use, including India&rsquo;s pilot work.</p>

<p><b>The price has already fallen.</b> The oversupply is on the other side. Bloomage&rsquo;s revenue fell 11.6% in 2024 and its net profit by about 72%, its worst year since listing. Chinese cosmetic-grade HA at ${HA_COS_LO}/kg is a fraction of the Rmb 2,226 a kilogram that Huaxi Biotech&rsquo;s 2019 prospectus recorded. An Indian entrant arrives into a market where the incumbent has spare capacity and nothing to lose by cutting price &mdash; the pattern this blog found in lysine, and again in erythritol, where Chinese capacity reached 380,000 tonnes and the price fell from about Rmb 40,000 a tonne to under Rmb 10,000.</p>

<p><b>The rules are thin.</b> Cosmetics are regulated under the Cosmetics Rules, 2020, administered by the Central Drugs Standard Control Organisation. An ingredient sold for injection is a drug and faces a different regime entirely. A market study notes that CDSCO has no specific monograph for hyaluronic acid, so importers work to the general Drugs and Cosmetics Act requirements.</p>

<p><b>There is a policy hook, and it is not about maize.</b> The BioE3 policy, approved in August 2024, names bio-based chemicals, biopolymers and enzymes as one of six priority areas, and the department has set up biofoundries and pilot-scale biomanufacturing hubs for exactly this gap between a laboratory result and a plant. The shortlist of bio-based chemicals it is funding as import substitutes &mdash; itaconic acid, succinic acid, squalene, rhamnolipids &mdash; is a cosmetics-ingredient list in all but name. Squalene and rhamnolipids go straight into skincare and mild cleansers. Hyaluronic acid is not on the published shortlist.</p>

<h2 class="gb-h2">What would fix this</h2>

<p>Give hyaluronic acid its own eight-digit customs code. It currently shares HS 391390 with xanthan gum, alginates and laboratory reagents, so neither the volume nor the average price India pays can be read from the trade data. A separate code costs nothing and would tell a prospective investor the size of the market.</p>

<p>Target the fermenter, not the feedstock. Every incentive aimed at &ldquo;value addition to maize&rdquo; will be captured by ethanol, which is where the tonnage is. If the aim is cosmetic ingredients, the binding constraint is sterile fermentation capacity, downstream purification and endotoxin-grade quality systems &mdash; which is what the BioE3 biomanufacturing hubs are for, and what they should be measured on.</p>

<p>Add hyaluronic acid, and the cosmetic polysaccharides generally, to the published bio-based chemicals shortlist, or say why they were left off. The policy already funds squalene and rhamnolipids for the same end market.</p>

<p>Put the idle distillery capacity to the test before building anything new. About {L(unsold)} crore litres of ethanol capacity had no buyer this year. Some of that plant is glucose-ready and could run contract fermentation for lactic acid, xanthan or citric acid, where India imports at known volumes and prices. That is a smaller claim than &ldquo;cosmetics from the maize surplus&rdquo;, and a testable one.</p>

<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>

<p>The conversion yields are from published laboratory and process literature, not from any operating Indian plant, and the recovered hyaluronic acid yield of {HA_YIELD} g per g of glucose, the {GLUCOSE} tonnes of glucose per tonne of maize, and the Rs {GLUCOSE_PRICE} a kilogram glucose price are this blog&rsquo;s assumptions. Change them and the rupee-per-tonne figures move, though not by enough to alter the ranking. India&rsquo;s hyaluronic acid imports could not be separated from the rest of HS 391390, so the $86.75/kg price comes from two individual shipment records in March 2024 rather than an annual average, and the quantity imported is unknown. The global HA tonnage is a consultancy forecast, not a measured figure, and the grade split behind it dates from 2021. No Indian commercial HA fermentation plant was found, but absence of evidence here is not proof; the companies named are at pilot or early commercial stage and their capacities were not published. Prices for alkyl polyglucosides and 1,3-propanediol are international reference levels, not Indian landed costs. The 2025-26 maize production figure is an advance estimate, not a final one, and the ethanol diversion figure is a projection.</p>
"""

sources = (
    "Maize: Ministry of Agriculture third advance estimates for 2025-26 (PIB, 27 May 2026); spot prices, export and import forecasts "
    "from the USDA India office as reported by The Hindu BusinessLine (23 June 2026); use split from the ANGRAU maize outlook report 2025-26; "
    "ethanol diversion from APEDA&rsquo;s market intelligence dashboard. Ethanol offer, allocation and tender prices from this blog&rsquo;s earlier pieces. "
    "Hyaluronic acid fermentation yields: Zhang et al., <i>Bioresource Technology</i> 377 (2023) and Cheng et al., <i>Biotechnology Journal</i> 11 (2016). "
    "Global tonnage, China&rsquo;s share and the grade split: Frost &amp; Sullivan figures as reported by Bloomage Biotech and by securities research on it; "
    "Bloomage&rsquo;s 2024 results from Yicai Global. Cosmetic and pharmaceutical grade price ranges from a 2025 China market report; the $86.75/kg landed price "
    "is a March 2024 shipment record under HS 39139090. Trade figures for citric acid, lactic acid, sorbitol and HS 391390 are from WITS/UN Comtrade for 2024. "
    "Chinese citric-acid capacity growth from a European Commission anti-dumping notice (September 2026); erythritol capacity and prices from trade press. "
    "1,3-propanediol yield and price from a 2024 review of production costs in microbial biotechnology. Indian producers: the ABLE India Biotech Handbook 2024 (Cosmos Bio), "
    "a Yale green-chemistry technology listing (Cellarim Labs), an Indian patent filing (Stelis Biopharma) and the Office of the Principal Scientific Adviser&rsquo;s "
    "S&amp;T clusters annual report 2025-26. BioE3: Cabinet approval release of 24 August 2024 and the Parliament answer of 23 July 2026. "
    "Arithmetic and all conversion assumptions are in the builder at out/research/maize-cosmetics/. Nothing here is investment advice."
)

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/indias-lysine-deficit-is-102-million.html",
     "India&rsquo;s Lysine Deficit Is $102 Million and China Holds About Three-Quarters of World Capacity. Molasses Is the Cheap Part. The Fermenter Is the Hard Part"),
    ("https://masaladeutsch.blogspot.com/2026/08/7186-litre-why-maize-is-indias-priciest.html",
     "&#8377;71.86 a Litre: Why Maize Is India&rsquo;s Priciest Ethanol Feedstock, Even as This Season&rsquo;s Acreage Falls"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-2026-27-ethanol-tender-drops.html",
     "India&rsquo;s 2026-27 Ethanol Tender Drops Cane Juice, Cuts Maize by Rs 3 a Litre and Flips From Sugar-First to Cheapest-First"),
    ("https://masaladeutsch.blogspot.com/2026/10/india-imported-28-million-of-sucralose.html",
     "India Imported $28 Million of Sucralose in FY26, Up 49%"),
    ("https://masaladeutsch.blogspot.com/2026/07/top-15-chemicals-for-import.html",
     "The Top 15 Import-Substitution Chemicals, Code by Code"),
]

build("Chemicals &middot; Agriculture &middot; 7 November 2026",
      "A Record Maize Crop Will Not Make India a Hyaluronic Acid Producer. The World&rsquo;s Entire Supply Fits Inside 13,000 Tonnes of Grain",
      f"Cosmetic-grade hyaluronic acid is fermented from glucose, and India has a {MAIZE_26} million tonne maize crop trading below its support price. "
      f"But the sugar is about {feed_share_ha:.0f}% of what the ingredient sells for, against {grain_share:.0f}% for ethanol. "
      "The constraint is sterile fermentation and purification, not grain.",
      body, sources, related, OUT)

print("maize/t:", L(spot_mid), "ethanol Rs/t:", L(eth_rev), "grain share %:", round(grain_share, 1))
print("HA kg/t maize:", round(ha_per_t, 1), "| world needs t maize:", L(maize_for_world),
      f"({share_of_crop:.4f}% of crop) | feed share {feed_share_ha:.1f}% | HA vs ethanol x{ha_vs_eth:.1f}")
print("citric maize t:", L(141747 / 0.75 / GLUCOSE))
