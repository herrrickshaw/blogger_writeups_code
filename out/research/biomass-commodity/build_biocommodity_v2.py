import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/update-2026-10-28-rice-and-maize-became-ethanol.html'

# ---------------------------------------------------------------- data
# Ethanol prices paid by oil companies, Rs a litre, ESY 2026-27 tender (BPCL e-tender 26985); basic + incentive, ex-GST/transport
ETH = [("C-heavy molasses and other feedstocks", 57.97), ("Surplus FCI rice", 60.32),
       ("Damaged food grains", 64.00), ("Maize", 68.86)]
MAIZE_2526 = 71.86
FCI_RICE_QTL = 2390            # OMSS(D) price for ethanol, Nov 2026 - Jun 2027
FCI_COST_QTL = 3889.46         # FCI economic cost 2025-26 RE (Rajya Sabha reply)
FCI_DISCOUNT = (1 - 2320 / FCI_COST_QTL) * 100   # at the Nov 2025 - Oct 2026 price of Rs 2,320
RICE_TO_ETH_T = 6.35           # million tonnes of FCI rice to distilleries, Jun 2025 - Jun 2026
RICE_VALUE_CR = 14596.78
DISTILLERIES_IS = 499
# Biomass
BENCH_PER_1000KCAL = 2.27      # Rs, northern region excl. NCR, non-torrefied pellets, from 8 Nov 2023
GCV_LO, GCV_HI = 2800, 4000    # kcal/kg, spec range
BENCH_T_LO = BENCH_PER_1000KCAL * GCV_LO       # Rs per tonne (kcal/kg x 1000 kg / 1000 kcal)
BENCH_T_HI = BENCH_PER_1000KCAL * GCV_HI
CEEW_PELLET_50KM = (4000, 5000)
COFIRED_CY25_LT = 24.76        # lakh tonnes, calendar 2025
WDRA_AGRI = 218
# Bamboo: Assam Bio Ethanol Pvt Ltd (ABEPL), Numaligarh
ABE_ETH_T, ABE_BAMBOO_T, ABE_HA, ABE_SAPLINGS = 49000, 500000, 12500, 60e5
ABE_FARMERS_REG, ABE_FARMERS_TGT, ABE_PAID_CR = 4200, 30000, 2.4
ABE_CHIP_ID, ABE_CHIP_SIGNED, ABE_CHIP_SUPPLY = 24, 8, 4
ABE_CHIPS_EOI_T = 375000
ETH_DENSITY = 0.789
L_PER_T_BAMBOO = ABE_ETH_T * 1000 / ETH_DENSITY / ABE_BAMBOO_T
YIELD_T_HA = ABE_BAMBOO_T / ABE_HA


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def chart_eth():
    W, L, top, bh, gap, lab = 400, 10, 24, 18, 8, 190
    H = top + len(ETH) * (bh + gap) + 30
    sc = (W - L - lab - 50) / 75
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Price oil companies pay for ethanol by feedstock in the 2026-27 tender: C-heavy molasses Rs 57.97, FCI rice Rs 60.32, damaged grain Rs 64.00, maize Rs 68.86 a litre.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Price paid for ethanol by feedstock, 2026-27, Rs a litre</text>']
    for i, (n, v) in enumerate(ETH):
        y = top + i * (bh + gap)
        col = "#1c5d99"
        s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 13}" font-size="10" fill="#212529">{v:.2f}</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">BPCL e-tender 26985 (16 Oct 2026); basic price plus incentive, before GST and transport.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def t_levers():
    return table(["What made a commodity", "Rice and maize for ethanol", "Biomass for co-firing today", "Abroad"], [
        ("A guaranteed buyer", "Oil companies must blend 20%; yearly tenders for about 1,100 crore litres", f"Coal plants must co-fire 5%; about {COFIRED_CY25_LT} lakh tonnes used in 2025", "UK and EU subsidy regimes; Japan&rsquo;s feed-in tariff for biomass power"),
        ("A price set in advance", "Administered ethanol price by feedstock; FCI rice sold to distilleries at a notified price", "A benchmark pellet price per 1,000 kcal set in November 2023, valid for a year", "Argus price index for pellets delivered around Rotterdam"),
        ("A traded or hedgeable market", "Maize sold in open markets, with a history of futures on Indian exchanges; FCI rice sold under the open-market sale scheme", "No exchange or published index", "Wood-pellet futures on EEX (since 2017) and Euronext"),
        ("A quality grade", "BIS standard for fuel ethanol; grain bought on FAQ norms", "A specification in the model contract (moisture, calorific value), not a graded standard", "ISO 17225 grades; ENplus A1/A2/B for pellets"),
        ("Storage and finance", "Grain in FCI and WDRA-registered warehouses; loans against warehouse receipts", "No warehouse-receipt category for pellets, briquettes or baled straw", "Pellets financed and stored as a standard bulk cargo"),
        ("A clear legal status and trade code", "Grain is a product with its own customs codes", "Straw is treated as farm waste; no customs line for agro-residue pellets", "EU by-product test; HS 4401.31 for wood pellets; Japan&rsquo;s certified palm kernel shells"),
        ("Cheap capital for plants", f"Interest subvention built {DISTILLERIES_IS} distilleries", "Capital grants per tonne an hour of pellet capacity (MNRE, CPCB in the NCR)", "&mdash;"),
    ])


def t_bamboo():
    return table(["Commodity lever", "Bamboo for the Numaligarh plant", "Straw for co-firing"], [
        ("Legal status", "Bamboo grown outside forests ceased to be a &ldquo;tree&rdquo; under the Indian Forest (Amendment) Act, 2017, so it needs no felling or transit permit", "Treated as farm waste; no product status"),
        ("Warehouse receipts", "Bamboo added to WDRA&rsquo;s list of farm commodities in September 2025 (Gazette CG-DL-E-04092025-265958)", "Not among the 2024 and 2025 additions"),
        ("Anchor buyer", f"One plant needing about {ABE_BAMBOO_T/1e5:.0f} lakh tonnes of green bamboo a year", "Coal plants under a 5% mandate"),
        ("First processing near the farm", f"Decentralised chipping units 30&ndash;40 km from farms cut poles to standard-size chips; {ABE_CHIP_ID} identified, {ABE_CHIP_SIGNED} signed, {ABE_CHIP_SUPPLY} supplying (February 2026)", "Balers and pellet plants, mostly in four northern states"),
        ("Direct payment and registration", f"About {ABE_FARMERS_REG:,} farmers registered on a digital platform; Rs {ABE_PAID_CR} crore paid straight to bank accounts", "Paid through aggregators, if at all"),
        ("Published price", "Not published", "A 2023 benchmark per 1,000 kcal"),
    ])


def t_steps():
    return table(["Step", "Ethanol precedent", "What it would do for biomass"], [
        ("Notify a benchmark price per tonne every year before the kharif harvest", "Ethanol prices are fixed per feedstock before each supply year", "Gives farmers and aggregators a known floor, as a Rajya Sabha committee recommended in February 2025"),
        ("Publish grades for agro-residue pellets and briquettes", "BIS standard for fuel ethanol", "Lets a pellet from Punjab and one from Maharashtra be priced against the same grade, as ISO 17225 does in Europe"),
        ("Notify pellets, briquettes and baled straw for warehouse receipts", "Rice bran, maize bran and oil cakes are already notified", "Lets collectors borrow against stored stock and sell through the year instead of in the six-week harvest window"),
        ("Publish a price index, then list a contract", "Maize futures on Indian exchanges", "Turns the benchmark into a market price that buyers and banks can use"),
        ("Long-term offtake contracts with coal plants", "Oil companies&rsquo; long-term ethanol contracts with dedicated plants", "Bankable demand for pellet plants and the aggregation machinery that feeds them"),
        ("Give agro-residue pellets their own customs and statistical codes", "Grain and ethanol are tracked by code", "Makes production, trade and prices visible"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>Rs {ETH[-1][1]:.2f}</b><span>a litre that oil companies pay for maize ethanol in 2026-27, fixed before the year begins</span></div>
<div class="gb-stat"><b>Rs {FCI_RICE_QTL:,}</b><span>a quintal: the notified price of FCI rice for distilleries from November 2026, below FCI&rsquo;s cost</span></div>
<div class="gb-stat"><b>Rs {BENCH_T_LO:,.0f}&ndash;{BENCH_T_HI:,.0f}</b><span>a tonne: the 2023 benchmark pellet price, converted at the specification&rsquo;s calorific range</span></div>
<div class="gb-stat"><b>{WDRA_AGRI}</b><span>farm commodities can be stored against negotiable warehouse receipts; pellets and baled straw are not among the recent additions</span></div>
</div>'''

body = f"""
{stats}

<p>India turned rice and maize into fuel by treating them as commodities with a guaranteed buyer, a price fixed in advance, a market where they trade, and warehouses that banks lend against. Oil companies must blend ethanol; they publish what they will pay for it by feedstock before each year begins; maize trades and is stored like any other grain; and the Food Corporation of India sells surplus rice to distilleries at a notified price. The result was hundreds of new distilleries and 20% blending reached ahead of schedule.</p>
<p>Biomass for power has the first of those four things and part of the second. Coal plants must co-fire biomass, and there is a benchmark price. It has none of the others. This piece sets out what made grain work as an ethanol commodity, how other countries made biomass a commodity, and what India would need to do the same for straw. It follows this blog&rsquo;s pieces on <a href="https://masaladeutsch.blogspot.com/2026/10/india-has-funded-3-lakh-machines-to.html">straw-collection machinery</a> and the <a href="https://masaladeutsch.blogspot.com/2026/10/indias-2026-27-ethanol-tender-drops.html">2026-27 ethanol tender</a>.</p>

<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px"><b>Updated 28 October 2026.</b> Added a section on bamboo for the Numaligarh 2G ethanol plant of Assam Bio Ethanol Pvt Ltd: the 2017 change that took bamboo grown outside forests out of the definition of a tree, bamboo&rsquo;s addition to WDRA&rsquo;s warehouse-receipt list in 2025, and the plant&rsquo;s chipping-unit and direct-payment collection model.</div>\n<h2 class="gb-h2">How rice and maize became ethanol commodities</h2>
{chart_eth()}
<p>For the supply year from November 2026, the oil companies are buying about 1,100 crore litres of ethanol at prices set per feedstock in the tender: Rs 57.97 a litre from C-heavy molasses, Rs 60.32 from surplus FCI rice, Rs 64.00 from damaged grain and Rs {ETH[-1][1]:.2f} from maize, down from Rs {MAIZE_2526:.2f} last year after the maize incentive was cut. A distiller knows before the year starts what each feedstock will earn.</p>
<p>The grain itself is priced too. FCI sold {RICE_TO_ETH_T} million tonnes of rice worth about Rs {RICE_VALUE_CR:,.0f} crore to distilleries between June 2025 and June 2026 at a notified price of Rs 2,250 and then Rs 2,320 a quintal, about {FCI_DISCOUNT:.0f}% below its own cost of about Rs {FCI_COST_QTL:,.0f}; from November 2026 the price is Rs {FCI_RICE_QTL:,}. Maize is bought in open markets, has a history of futures trading on Indian commodity exchanges, and is stored in registered warehouses. And interest subvention on loans built {DISTILLERIES_IS} distilleries, as this blog has <a href="https://masaladeutsch.blogspot.com/2026/08/interest-subvention-built-499-ethanol.html">reported</a>. Each of these is a lever the government chose to pull.</p>

<h2 class="gb-h2">How biomass became a commodity elsewhere</h2>
<p>Wood pellets are the clearest case. Europe first standardised them: the ISO 17225 series sets one set of grades and tests for solid biofuels, and the ENplus scheme adds stricter A1, A2 and B classes. Once a tonne of pellets meant the same thing from any supplier, a price could be published: Argus assesses pellets delivered into north-west Europe, and the European Energy Exchange launched wood-pellet futures in 2017, settled on that index, with the first trade in January 2018. Euronext lists a contract on ENplus A1 pellets. Trade in solid biofuels grew from about 56 to 300 petajoules between 2000 and 2010, with pellets from 8.5 to 120, according to research from Utrecht University.</p>
<p>Japan made a farm residue into a commodity through certification. Since April 2024, palm kernel shells burnt in power plants that receive its feed-in tariff must be certified sustainable under recognised schemes, which has turned a palm-oil by-product from Indonesia and Malaysia into a graded, documented import. The European Union&rsquo;s waste law excludes straw used for energy from the definition of waste and sets a test for when a residue is a by-product, which matters because waste needs permits to move and cannot easily be traded.</p>

<h2 class="gb-h2">What India has, and what it lacks</h2>
{t_levers()}
<p>The benchmark pellet price the power ministry set in November 2023, Rs {BENCH_PER_1000KCAL} per 1,000 kcal for non-torrefied pellets in the northern region outside the NCR, works out to about Rs {BENCH_T_LO:,.0f}&ndash;{BENCH_T_HI:,.0f} a tonne across the specification&rsquo;s calorific range of {GCV_LO:,}&ndash;{GCV_HI:,} kcal per kg, before GST and transport. CEEW estimates that pellets delivered 50 km cost about Rs {CEEW_PELLET_50KM[0]:,}&ndash;{CEEW_PELLET_50KM[1]:,} a tonne to make and move. So the price is not obviously too low. What is missing is everything that lets a price become a market: grades, an index, storage and finance.</p>
<p>The warehouse gap is the most telling. The Warehousing Development and Regulatory Authority has notified {WDRA_AGRI} farm commodities for negotiable warehouse receipts, against which banks lend. Its 2025 notification, read in the Gazette of India (CG-DL-E-04092025-265958), added rice bran, maize bran, several oil cakes, bamboo, raw jute and coconut with husk, and even urea and potash among non-farm goods. Biomass pellets, briquettes and baled straw are not among the 2024 and 2025 additions. A collector who bales straw in October cannot store it in a registered warehouse and borrow against it until a power plant needs it in March.</p>

<h2 class="gb-h2">Bamboo is the nearest case: the Numaligarh 2G ethanol plant</h2>
<p>One biomass in India already has most of the pieces. Assam Bio Ethanol Pvt Ltd (ABEPL), a joint venture of Numaligarh Refinery Limited with Finland&rsquo;s Fortum and Chempolis, has built a plant at Numaligarh in Golaghat that turns bamboo into second-generation ethanol, along with furfural and acetic acid. It produced fuel-grade ethanol in trials in September 2025 and was dedicated to the nation that month; in September 2026 it was reported to be in a stabilisation phase before commercial production. At full capacity it needs about {ABE_BAMBOO_T/1e5:.0f} lakh tonnes of green bamboo a year to make about {ABE_ETH_T:,} tonnes of ethanol, roughly {L_PER_T_BAMBOO:.0f} litres per tonne of green bamboo, and the bamboo would come from about {ABE_HA:,} hectares, implying about {YIELD_T_HA:.0f} tonnes per hectare a year.</p>
{t_bamboo()}
<p>The collection model is the interesting part. Rather than buying poles at the plant gate, ABEPL has set up a network of decentralised chipping units, run by local entrepreneurs within 30&ndash;40 km of the farms, which cut bamboo into chips of a standard size; it issued an expression of interest in October 2025 for trucking about {ABE_CHIPS_EOI_T/1e5:.2f} lakh tonnes of chips a year from those units. Farmers register on a digital platform and are paid directly, with no middleman, the company says: about {ABE_FARMERS_REG:,} had registered across 16 districts of Assam and parts of Arunachal Pradesh, Nagaland and Meghalaya by February 2026, against a target of {ABE_FARMERS_TGT:,} within a 300 km radius over three years. With the Assam forest department it has set up three high-tech nurseries for tissue-cultured saplings and plans to distribute about {ABE_SAPLINGS/1e5:.0f} lakh saplings free; Assam&rsquo;s rule allowing tea estates to use up to 5% of their land for other crops has led some to plant bamboo.</p>
<p>That is the ethanol model applied to a biomass: a guaranteed buyer, a first processing step close to the farm that turns a bulky residue into a standard product, registered suppliers paid directly, and a legal status and warehouse category that let the product be stored and moved. What it still lacks is a published price per tonne, and supply: the company said in February 2026 that the plant was in start-up because raw material was short. Straw could follow the same route, with chipping units replaced by baling and pelleting centres.</p>

<h2 class="gb-h2">What would make straw a commodity</h2>
{t_steps()}
<p>None of these steps needs a new subsidy. Most are notifications: a price before each kharif season, a BIS grade, a WDRA entry, a customs line. The ethanol programme shows that once a farm product has a buyer, a price, a grade and a warehouse, private capital follows. Straw already has the buyer. The Rajya Sabha&rsquo;s Committee on Subordinate Legislation recommended in February 2025 that a benchmark price for paddy residue, modelled on the minimum support price, be set with the Commission for Air Quality Management and notified before each kharif season. That would be the first step; warehouse receipts would be the one that lets the market last beyond the harvest.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Ministry of Power should notify a per-tonne benchmark price for agro-residue pellets and briquettes each year before the kharif harvest, by region and grade, and publish what plants actually paid.</li>
<li>BIS should publish grades for agro-residue pellets and briquettes aligned with ISO 17225, and the model co-firing contract should reference them.</li>
<li>WDRA should notify biomass pellets, briquettes and baled straw as commodities for negotiable warehouse receipts, with storage norms for moisture and fire safety.</li>
<li>DGFT and CBIC should create separate tariff lines for agro-residue pellets and briquettes, so that production and trade can be tracked.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The benchmark pellet price is the November 2023 figure, valid for a year; no later revision was found, and the per-tonne range is this blog&rsquo;s conversion at the specification&rsquo;s calorific range. Only WDRA&rsquo;s 2024 and 2025 additions were read in the gazette; its full list of notified commodities was not, so this piece does not claim no biomass item has ever been notified. Exchange trading volumes for wood-pellet futures were not found. Maize&rsquo;s exchange trading in 2026 was not checked. Ethanol prices are tender prices, not what was actually allocated by feedstock this year, and every award in the 2026-27 tender is provisional pending Supreme Court cases. ABEPL&rsquo;s sourcing figures are from February 2026 and its price per tonne of bamboo was not found; capacity is reported as 49,000 tonnes or 50,000 tonnes of ethanol a year, and feedstock as 5 lakh tonnes of green bamboo or about 3 lakh tonnes of dry bamboo. The public support found for its sourcing came from the Assam forest department&rsquo;s nurseries; no announcement of a separate state bamboo board role was found.</p>
"""

sources = ("Ethanol prices and tender terms: BPCL e-tender 26985 (16 October 2026) and tender 22376 (23 September 2025), as read in this blog&rsquo;s 2026-27 tender piece; ESY 2025-26 prices per Lok Sabha reply (Bioenergy Times). FCI rice to distilleries: Rajya Sabha reply, July 2026 (Business Standard, Outlook, Moneylife); OMSS(D) 2026-27 policy (Rural Voice). "
           "Benchmark pellet price: Ministry of Power/CEA, effective 8 November 2023 (K&amp;S Partners, PelletIndia, Argus). Co-firing volume: Ministry of Power Annual Report 2025-26. Pellet delivered cost: CEEW (2025). "
           "WDRA: notification of 2 September 2025, Gazette of India Extraordinary CG-DL-E-04092025-265958, and of 5 June 2024, CG-DL-E-02072024-255098, read via the SansadSaar index of the archive.org Gazette of India collection; WDRA FAQ for the 218 count. "
           "Abroad: EEX and ECC circulars, Argus methodology, Euronext (wood-pellet futures); ISO 17225 and ENplus (COFORD review; European Pellet Council); Lamers, Junginger et al. (2012), Utrecht University; Japan PKS certification (Argus; RSB); EU Waste Framework Directive 2008/98/EC as summarised (Frontiers, 2022). "
           "Bamboo and ABEPL: Assam Tribune, The Tribune, Deccan Herald and Northeast Today (February&ndash;March 2026), Bioenergy Times (12 September 2026), The Pamphlet, Sentinel Assam; ABEPL transport EOI (October 2025) as reported; Indian Forest (Amendment) Act 2017 (PRS bill track; Deccan Herald; The Tribune); WDRA notification of 2 September 2025 as above. Committee recommendation: Rajya Sabha Committee on Subordinate Legislation, February 2025 (Deccan Herald/PTI; Vision IAS). Per-tonne conversion and the FCI discount are this blog&rsquo;s arithmetic. Not investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/india-has-funded-3-lakh-machines-to.html", "India Has Funded 3 Lakh Machines to Stop Stubble Burning. About 4,500 of Them Collect Straw"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-2026-27-ethanol-tender-drops.html", "India&rsquo;s 2026-27 Ethanol Tender Drops Cane Juice, Cuts Maize by Rs 3 a Litre and Flips From Sugar-First to Cheapest-First"),
    ("https://masaladeutsch.blogspot.com/2026/08/interest-subvention-built-499-ethanol.html", "Interest Subvention Built 499 Ethanol Distilleries. Viability Gap Funding Built One Working 2G Plant."),
    ("https://masaladeutsch.blogspot.com/2026/08/ethanols-coal-boilers-briquette-gap-and.html", "Ethanol&rsquo;s Coal Boilers, the Briquette Gap, and What US Carbon Capture Actually Delivers"),
]

build("Agriculture · 28 October 2026",
      "Rice and Maize Became Ethanol Commodities With a Price, a Buyer and a Warehouse. Straw Has Only the Buyer",
      "India built its ethanol programme by giving grain a guaranteed buyer, a price fixed in advance, a market and warehouse finance. Biomass for power has a mandate and a 2023 benchmark price, but no grades, no index and no warehouse receipts. Europe and Japan show how residues become tradeable.",
      body, sources, related, OUT)
print("L/t", round(L_PER_T_BAMBOO), "t/ha", YIELD_T_HA)
