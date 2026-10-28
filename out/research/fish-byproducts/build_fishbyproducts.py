import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-fish-byproducts.html'

# ---------------------------------------------------------------- data (sources in the sources paragraph)
USD_INR = 94.93                     # rate used across this blog in late Oct 2026
FISH_PROD_LT = 197.75               # all fish, lakh tonnes, 2024-25 (Department of Fisheries)
MARINE_2025_LT = 35.7               # marine landings 2025, lakh tonnes (CMFRI)
KERALA_SARDINE_2024_LT = 1.49       # Kerala oil sardine 2024, lakh tonnes (CMFRI)
WASTE_MT = (4, 6)                   # ICAR-CIFT press note, million tonnes a year
WASTE_ALT_MT = 0.3                  # ICAR-CIFT by-products information system
LOSS_CR = {"Inland": 46000, "Marine": 15000}   # annual post-harvest loss, Rs crore (standing committee; Lok Sabha reply)
LOSS_PCT = {"Inland": 5.23, "Marine": 10.52}   # NABCONS evaluation (Lok Sabha, Mar 2022)
LOSS_TOTAL = sum(LOSS_CR.values())
assert LOSS_TOTAL == 61000

# yields per tonne of raw fish (sardine by-products, Morocco study; Peru anchoveta plant benchmark)
MEAL_YIELD, OIL_YIELD = 0.22, 0.07
# prices
MEAL_RS_KG = (42, 105)              # IndiaMART asking prices: sun-dried 45% protein, flame-dried 60% protein
OIL_USD_T = (2600, 6800)            # Peruvian crude fish oil: early 2025 CFR China; June 2026 spot
OIL_RS_KG = tuple(round(u * USD_INR / 1000) for u in OIL_USD_T)
CAPS_RS = (7.55, 13.32)             # retail Rs per 1,000 mg capsule, 180 EPA/120 DHA, 60-count packs (HK Vitals, Inlife)
CAPS_RS_KG = tuple(round(c * 1000) for c in CAPS_RS)   # 1,000 capsules hold 1 kg of oil
REFINE_YIELD = 0.70                 # ASSUMPTION: share of crude oil that ends up as capsule-grade oil

meal_val = tuple(MEAL_YIELD * 1000 * p for p in MEAL_RS_KG)            # Rs per tonne of raw fish
oil_val = tuple(OIL_YIELD * 1000 * p for p in OIL_RS_KG)
caps_val = tuple(OIL_YIELD * 1000 * REFINE_YIELD * p for p in CAPS_RS_KG)
mo_low, mo_high = meal_val[0] + oil_val[0], meal_val[1] + oil_val[1]

# trade, HS 1504, 2024-25, Rs crore (TradeStat via busy.in)
TRADE = [("Fish body oil (15042010), exports", 354.0, "x"),
         ("Fish lipid oil (15042020), imports", 127.82, "m"),
         ("Fish body oil (15042010), imports", 65.66, "m"),
         ("Cod liver oil (15041010), imports", 10.56, "m")]

# fishmeal plants (CIBA study) and the largest listed company
PLANTS = {"Karnataka": 23, "Maharashtra": 4, "Gujarat": 3, "Tamil Nadu": 3, "Kerala": 2}
PLANTS_TOTAL = sum(PLANTS.values())
CIBA_MEAL_T, CIBA_OIL_T = 65000, 34000
MUKKA_MEAL_T, MUKKA_OIL_T = 115050, 16950

# PMMSY
PMMSY_CR, PMMSY_EXT_CR = 20050, 700
COLDCHAIN_CR, COLD_PLANTS, TRANSPORT_UNITS = 2797, 775, 28489
HARBOUR_CR = 3741.89
PMMSY_BE_2627 = 2500


def chart_value():
    rows = [("Crude fish oil, early 2025", OIL_RS_KG[0], "#868e96"),
            ("Crude fish oil, June 2026", OIL_RS_KG[1], "#1c5d99"),
            ("Same oil in capsules, low retail", CAPS_RS_KG[0], "#d9a441"),
            ("Same oil in capsules, high retail", CAPS_RS_KG[1], "#a5402c")]
    W, L, top, bh, gap, lab = 400, 10, 24, 18, 9, 178
    H = top + len(rows) * (bh + gap) + 34
    sc = (W - L - lab - 54) / max(r[1] for r in rows)
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Rupees per kilogram of fish oil: crude oil about {OIL_RS_KG[0]} to {OIL_RS_KG[1]}; the same oil sold as 1,000 mg retail capsules about {CAPS_RS_KG[0]:,} to {CAPS_RS_KG[1]:,}.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Rs per kg of fish oil, crude vs retail capsules</text>']
    for i, (n, v, col) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{max(v * sc, 2):.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + max(v * sc, 2) + 4:.1f}" y="{y + 13}" font-size="10" fill="#212529">{v:,}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Crude: Peruvian prices at Rs {USD_INR}/$. Capsules: 1,000 mg retail packs, 1,000</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">capsules per kg of oil; price includes refining, packing, GST and retail margin.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_trade():
    W, L, top, bh, gap, lab = 400, 10, 36, 18, 9, 196
    H = top + len(TRADE) * (bh + gap) + 22
    sc = (W - L - lab - 50) / max(v for _, v, _ in TRADE)
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="India fish-oil trade in 2024-25: fish body oil exports Rs 354 crore; imports of fish lipid oil Rs 128 crore, fish body oil Rs 66 crore and cod liver oil Rs 11 crore.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">India&rsquo;s fish-oil trade, 2024-25, Rs crore</text>',
         f'<rect x="{L}" y="20" width="9" height="9" fill="#1c5d99"/><text x="{L + 13}" y="28" font-size="9.5" fill="#212529">Exports</text>',
         f'<rect x="{L + 70}" y="20" width="9" height="9" fill="#a5402c"/><text x="{L + 83}" y="28" font-size="9.5" fill="#212529">Imports</text>']
    for i, (n, v, k) in enumerate(TRADE):
        y = top + i * (bh + gap)
        col = "#1c5d99" if k == "x" else "#a5402c"
        s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="9.5" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{max(v * sc, 2):.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + max(v * sc, 2) + 4:.1f}" y="{y + 13}" font-size="10" fill="#212529">{v:,.0f}</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Commerce ministry TradeStat figures as tabulated by busy.in; ITC-HS codes in brackets.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_chain():
    f = lambda a: f"{a[0]:,.0f}&ndash;{a[1]:,.0f}"
    return table(["Step (per tonne of raw oily fish)", "Output", "Value, Rs", "Basis"], [
        ("Fishmeal", f"about {MEAL_YIELD * 1000:.0f} kg", f(meal_val), f"Rs {MEAL_RS_KG[0]}&ndash;{MEAL_RS_KG[1]}/kg asking prices (45&ndash;60% protein)"),
        ("Crude fish oil", f"about {OIL_YIELD * 1000:.0f} kg", f(oil_val), f"Rs {OIL_RS_KG[0]}&ndash;{OIL_RS_KG[1]}/kg (Peruvian prices, early 2025 to June 2026)"),
        ("<b>Meal plus crude oil</b>", "", f"<b>{mo_low:,.0f}&ndash;{mo_high:,.0f}</b>", "What a fishmeal plant earns"),
        ("Oil refined and sold as 1,000 mg capsules", f"about {OIL_YIELD * 1000 * REFINE_YIELD:,.0f} kg, about {OIL_YIELD * 1000 * REFINE_YIELD * 1000:,.0f} capsules", f(caps_val), f"Retail Rs {CAPS_RS[0]}&ndash;{CAPS_RS[1]} a capsule; {REFINE_YIELD:.0%} of crude oil assumed capsule-grade"),
    ])


def t_shelf():
    return table(["Method", "Typical storage life", "Source and note"], [
        ("Fresh, iced immediately", "5&ndash;16 days by species; oil sardine about 6 days", "ICAR-CIFT study of 14 Indian species"),
        ("Fresh, iced after 3 hours in the sun", "Under 1 to 2 days for scads and anchovies", "Same study: delay matters more than ice"),
        ("Frozen at &minus;18&deg;C", "About 12 months", "ICAR-CIFT product note (coated trout fillets)"),
        ("Smoke-cured mackerel", "105 days chilled; 6 days at room temperature", "Mangaluru fisheries college study"),
        ("Smoke-dried freshwater fish", "4&ndash;165 days; up to 11 months with hygienic handling", "Odisha study"),
        ("Dry-, pickle- or smoke-cured oil sardine", "About 5&ndash;7 weeks, falling with fat content", "ICAR-CIFT Calicut, 1977"),
        ("Fish silage / fish amino acid", "About 60 days for jaggery-fermented carp waste", "ICAR study on fermented silage"),
    ])


def t_plants():
    rows = [(st, str(n)) for st, n in PLANTS.items()]
    rows.append(("<b>Total in study</b>", f"<b>{PLANTS_TOTAL}</b>"))
    return table(["State", "Fishmeal plants (CIBA study)"], rows)


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>Rs {LOSS_TOTAL:,} cr</b><span>a year of fish lost after harvest, by a parliamentary committee&rsquo;s estimate ({LOSS_CR["Inland"]:,} inland, {LOSS_CR["Marine"]:,} marine)</span></div>
<div class="gb-stat"><b>{WASTE_MT[0]}&ndash;{WASTE_MT[1]} Mt</b><span>of fish waste a year, by ICAR-CIFT&rsquo;s estimate, from about {FISH_PROD_LT / 10:.1f} Mt of fish</span></div>
<div class="gb-stat"><b>Rs {mo_low / 1000:,.0f}k&ndash;{mo_high / 1000:,.0f}k</b><span>of fishmeal and crude oil from a tonne of oily fish; the same oil in retail capsules sells for Rs {caps_val[0] / 1e5:.1f}&ndash;{caps_val[1] / 1e5:.1f} lakh</span></div>
<div class="gb-stat"><b>Rs {TRADE[0][1]:,.0f} cr</b><span>of fish body oil exported in 2024-25, while Rs {sum(v for _, v, k in TRADE if k == "m"):,.0f} crore of fish lipid, fish body and cod liver oil was imported</span></div>
</div>'''

body = f"""
{stats}

<p>India landed {MARINE_2025_LT} lakh tonnes of marine fish in 2025 and produced about {FISH_PROD_LT:.0f} lakh tonnes of fish in all in 2024-25. A large share never reaches a plate in good condition. A parliamentary committee put the value of fish lost after harvest at about Rs {LOSS_TOTAL:,} crore a year, and ICAR-CIFT, the government&rsquo;s fish-technology institute in Kochi, says processing alone leaves 4 to 6 million tonnes of heads, guts, frames, skin and scales. Much of the rest of the low-value catch goes, cheaply, to fishmeal plants.</p>
<p>That waste and that cheap catch can become products that keep for months or years: fish oil, refined into omega-3 capsules; fish amino acid fertiliser for natural farming; fishmeal; and properly cured, dried or frozen fish. This piece looks at what each is worth, how long it lasts, who captures the value, and what would move more of it to the people who catch the fish. It follows this blog&rsquo;s pieces on <a href="https://masaladeutsch.blogspot.com/2026/08/indias-animal-protein-export-complex.html">India&rsquo;s animal-protein exports</a> and <a href="https://masaladeutsch.blogspot.com/2026/08/indias-6000-crore-fisheries-scheme.html">the fisheries scheme that has barely paid out</a>, and takes the same approach as the piece on <a href="https://masaladeutsch.blogspot.com/2026/10/india-imports-whey-protein-its-cheese.html">the whey that cheese makers pour away</a>.</p>

<h2 class="gb-h2">How much is lost, and where</h2>
<p>The estimates differ widely, which is itself part of the problem. The Rs {LOSS_TOTAL:,} crore figure, repeated in a Lok Sabha reply, splits into Rs {LOSS_CR["Inland"]:,} crore inland and Rs {LOSS_CR["Marine"]:,} crore marine. A 2022 evaluation by NABARD&rsquo;s consultancy arm put physical wastage at {LOSS_PCT["Marine"]}% of marine fish and {LOSS_PCT["Inland"]}% of inland fish. On processing waste, ICAR-CIFT&rsquo;s recent press material says {WASTE_MT[0]}&ndash;{WASTE_MT[1]} million tonnes a year, while its own by-products database gives about {WASTE_ALT_MT} million tonnes of seafood waste; the first counts all trimmings, the second only what is collected. Filleting can leave as much as three-quarters of a fish as waste, and skin and bone alone are about 30%.</p>
<p>Losses start on the boat. ICAR-CIFT&rsquo;s study of 14 species found that fish iced immediately keep for 5 to 16 days, oil sardine about 6, but scads and anchovies left in the sun for three hours before icing keep for less than one to two days. Ice and insulated boxes at the point of landing are worth more than most processing.</p>

<h2 class="gb-h2">Fish oil: exported crude, bought back refined</h2>
{chart_trade()}
<p>India exported Rs {TRADE[0][1]:,.0f} crore of fish body oil in 2024-25, much of it probably crude oil from the fishmeal plants of the west coast, and imported Rs {sum(v for _, v, k in TRADE if k == "m"):,.0f} crore of fish lipid oil, fish body oil and cod liver oil. Omega-3 capsules themselves cannot be separated in the trade data, because they are classed with food preparations or medicines rather than under fish oil. But the pattern is visible: the country sells the bulk raw material and buys some of the refined material back.</p>
{chart_value()}
<p>The gap between crude oil and capsules is large. Peruvian crude fish oil, the world benchmark, sold for about ${OIL_USD_T[0]:,} a tonne in early 2025 and about ${OIL_USD_T[1]:,} in June 2026, when world fish-oil output was running about a fifth below a year earlier, or about Rs {OIL_RS_KG[0]}&ndash;{OIL_RS_KG[1]} a kg. A 60-capsule pack of 1,000 mg fish-oil capsules with 180 mg EPA and 120 mg DHA retails for about Rs 450&ndash;800 on Indian pharmacy sites, which is Rs {CAPS_RS_KG[0]:,}&ndash;{CAPS_RS_KG[1]:,} for the kilogram of oil inside. That retail price pays for refining (deodorising, molecular distillation to remove contaminants), gelatin capsules, testing, packing, GST, marketing and the retailer&rsquo;s margin, so it is not profit. It does show where most of the money in the chain sits.</p>
<p>Refined fish oil sold as a supplement is regulated under FSSAI&rsquo;s Health Supplements and Nutraceuticals Regulations, 2022, in force since April 2022, and fish oil itself now has a quality standard modelled on the Codex standard for fish oils. A small plant has to meet those standards, which means oxidation and contaminant testing it cannot do alone. This piece makes no claim about the health effects of omega-3 supplements.</p>

<h2 class="gb-h2">What a tonne of fish is worth at each step</h2>
{t_chain()}
<p class="gb-note">Illustrative arithmetic, not a plant&rsquo;s accounts. Yields are about 22% meal and 7% oil, from a study of sardine by-products and a Peruvian fishmeal plant&rsquo;s reported yields; Indian oil sardine is fattier in some seasons. The {REFINE_YIELD:.0%} capsule-grade share is this blog&rsquo;s assumption, and capsule prices are retail, before the costs listed above.</p>
<p>A fishmeal plant turns a tonne of oily fish into roughly Rs {mo_low:,.0f}&ndash;{mo_high:,.0f} of meal and oil. The fishers who supplied it are paid the price of low-grade fish. Studies by the Central Marine Fisheries Research Institute (CMFRI) put fishers&rsquo; share of what consumers pay for fresh fish at about 30&ndash;68% depending on the species, and at about 64% in 2013-14. For fish that goes to fishmeal, they get only the raw-material price, and none of the value added afterwards.</p>

<h2 class="gb-h2">Fishmeal plants and juvenile fish</h2>
{t_plants()}
<p>A study by the Central Institute of Brackishwater Aquaculture counted {PLANTS_TOTAL} fishmeal plants, {PLANTS["Karnataka"]} of them in Karnataka, and estimated about {CIBA_MEAL_T:,} tonnes of fishmeal and {CIBA_OIL_T:,} tonnes of fish oil a year from Karnataka, Kerala and Tamil Nadu; there are no official national figures. Mukka Proteins, the largest listed producer, reports capacity of {MUKKA_MEAL_T:,} tonnes of meal and {MUKKA_OIL_T:,} tonnes of oil a year across plants in Karnataka, Maharashtra, Gujarat and Oman. Oil sardine is the main raw material; Kerala alone landed {KERALA_SARDINE_2024_LT} lakh tonnes of it in 2024.</p>
<p>The conflict is with food and with the fishery itself. Fishmeal plants pay for volume, not size, so they create a market for juvenile fish that would be worth more if left to grow. Kerala set minimum legal sizes for 14 species in 2015 and 44 more in 2017, after reports that juveniles were being sold to plants in Mangaluru and Thoothukudi. A CMFRI study estimated that catching juvenile threadfin bream alone cost Kerala&rsquo;s fisheries about Rs 221 crore. The plants also have local costs: the National Green Tribunal fined a fishmeal plant near Udyavara in Udupi district in July 2022 for pollution affecting nearby villages. Processing waste, not whole fish, is the better raw material for meal and oil.</p>

<h2 class="gb-h2">Fish amino acid: a fertiliser from waste</h2>
<p>Fish amino acid, a liquid fertiliser used in natural farming, is made by fermenting fish waste with jaggery for two to three weeks. One natural-farming guide uses about 200 grams of jaggery for each kilogram of fish waste; a research protocol uses equal weights. Farmers dilute it heavily, typically 2&ndash;5 ml a litre of water for a foliar spray. An ICAR study found jaggery-fermented carp waste stayed usable for about 60 days, and that more than 20% jaggery made it spoil faster. A natural-farming account puts the production cost at about Rs 30 a litre and the farm-gate selling price at about Rs 50; branded products sell for much more, but no reliable retail benchmark was found.</p>
<p>The appeal for fishing villages is that it needs no plant: drums, jaggery and the guts and heads already at the landing centre. Fish protein hydrolysates and fish emulsions, the industrial versions, need enzymes and drying and are mostly made by larger firms.</p>

<h2 class="gb-h2">Curing and cold storage: making fish last</h2>
{t_shelf()}
<p>Traditional curing is where most fishing households, and particularly women, already add value. Salting and sun-drying on open beaches, however, give a product that keeps for weeks rather than months and fails food-safety tests. Hygienic drying on racks or in solar dryers, smoking kilns and proper packing extend storage life to several months, as the Odisha and Mangaluru studies show, and fetch higher prices; WorldFish and CMFRI projects in Odisha have trained women&rsquo;s groups to make hygienic dried fish and fish pickles, papads and cutlets.</p>
<p>The government&rsquo;s main fisheries scheme, Pradhan Mantri Matsya Sampada Yojana (PMMSY), approved in 2020 at Rs {PMMSY_CR:,} crore and extended into 2025-26 with about Rs {PMMSY_EXT_CR} crore more, has approved about Rs {COLDCHAIN_CR:,} crore for cold-chain and marketing infrastructure: {COLD_PLANTS} cold storages and ice plants, {TRANSPORT_UNITS:,} fish transport units, kiosks and markets. It has also approved Rs {HARBOUR_CR:,.0f} crore for 28 fishing harbours and 25 landing centres in five years, and has Rs {PMMSY_BE_2627:,} crore in the 2026-27 budget. By-product processing at landing centres is not a separate line in what has been reported.</p>

<h2 class="gb-h2">Who could capture the value</h2>
<p>Kerala&rsquo;s fishermen&rsquo;s cooperative federation, Matsyafed, shows that collective processing is possible. It federates more than 650 primary societies, 118 of them women&rsquo;s cooperatives, and runs ice and freezing plants, two fish manure plants and a plant that makes chitosan from shellfish waste. Those are the right kinds of assets: they turn what would be dumped into something that keeps and sells. The step most cooperatives have not taken is fish oil, because a refinery that meets FSSAI and export standards costs far more than a manure plant.</p>
<p>A practical split would be for cooperatives and women&rsquo;s groups to own the first, low-cost stage at the landing centre (collecting and chilling waste, making fish amino acid and silage, hygienic drying) and to sell crude oil and graded waste under contract to licensed refiners and fishmeal plants, rather than selling juvenile fish to them.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Department of Fisheries should publish annual statistics on fishmeal and fish-oil production, plant by plant, with the share of raw material that is processing waste rather than whole fish.</li>
<li>PMMSY should fund waste-collection, chilling and by-product units at landing centres as a named component, owned by fishermen&rsquo;s cooperatives or women&rsquo;s groups, and report them separately.</li>
<li>Coastal states should require fishmeal plants to record the species and size of the fish they buy, so that minimum-legal-size rules can be enforced at the plant gate, not only at sea.</li>
<li>ICAR-CIFT and FSSAI should publish a simple standard and testing route for small producers of fish amino acid and crude fish oil, so that cooperative products can be sold to refiners and farmers with known quality.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>There are no official national figures for fishmeal and fish-oil production or for the domestic omega-3 capsule market, and capsule imports cannot be separated in the trade data. The fishmeal plant count and output come from a single older study covering a few states. Indian fishmeal and sardine landing prices were found only as sellers&rsquo; asking prices, so the value chain uses world fish-oil prices and is illustrative. Sources disagree on the 2025 oil sardine catch (1.68 or 2.53 lakh tonnes) and on the volume of fish waste (0.3 or 4&ndash;6 million tonnes). The shelf-life figures come from separate studies of different species and products, some decades old. No current figures were found for Matsyafed&rsquo;s by-product output or for incomes of women&rsquo;s dry-fish groups.</p>
"""

sources = ("Production and landings: Department of Fisheries (fish production 2024-25, via PMMSY six-year coverage, September 2026); ICAR-CMFRI, Marine Fish Landings in India 2025 and 2024 (CMFRI releases; The Week, Outlook Business). "
           "Losses: Parliamentary Standing Committee estimate and Lok Sabha reply (Rs 61,000 crore; inland Rs 46,000 crore, marine Rs 15,000 crore); NABCONS evaluation cited in a Lok Sabha reply of March 2022; ICAR-CIFT press note on fish waste and its by-products information system; ICAR-CIFT papers on fish waste utilisation. "
           "Shelf life: ICAR-CIFT, effect of delay in icing on 14 Indian fishes; ICAR-CIFT product notes (Vikaspedia); smoke-cured mackerel (Mangaluru fisheries college) and smoke-dried fish (Odisha) studies; ICAR-CIFT Calicut 1977 study of cured oil sardine; ICAR study of fermented carp-waste silage (Indian Journal of Fisheries). "
           "Fish oil and meal: CIBA study, Production and marketing of fish meal in India (Indian Journal of Fisheries); Mukka Proteins IPO documents (IPO Central, Arihant Capital); NGT order on a Udupi plant (Outlaw Ocean Project database); yields from a sardine by-product study (Journal of Food Engineering, Thailand) and a Peruvian producer; fish oil prices from Undercurrent News (January 2025) and SalmonBusiness (15 June 2026); Indian fishmeal asking prices from IndiaMART listings; HS 1504 trade for 2024-25 from busy.in tabulations of TradeStat; capsule prices from BigBasket and PharmEasy listings (October 2026). "
           "Fish amino acid: LEISA India; Tropical Journal of Natural Product Research. Regulation: FSSAI Health Supplements and Nutraceuticals Regulations 2022 (FoodNavigator); GOED letters to FSSAI on fish oil standards. "
           "Juvenile fishing: CMFRI studies reported by The News Minute and SeafoodSource; Kerala minimum legal size rules. Fishers&rsquo; share: CMFRI price-spread studies. PMMSY: Vikaspedia and PIB (outlay and extension); PMMSY six-year coverage (Organiser, September 2026) for cold-chain and harbour approvals; Matsyafed: NFDB World Fisheries Day 2021 citation. "
           "Rupee values at Rs 94.93 to the dollar; value-chain figures are this blog&rsquo;s illustrative arithmetic. Nothing here is investment, medical or agronomic advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/indias-animal-protein-export-complex.html", "India&rsquo;s Animal-Protein Export Complex"),
    ("https://masaladeutsch.blogspot.com/2026/08/indias-6000-crore-fisheries-scheme.html", "India Allocated &#8377;6,000 Crore for Fisheries Under PM-MKSSY. It Has Paid Out &#8377;4.73 Crore So Far."),
    ("https://masaladeutsch.blogspot.com/2026/08/indias-shrimp-exports-did-not-collapse.html", "India&rsquo;s Shrimp Exports Did Not Collapse. The Code Did."),
    ("https://masaladeutsch.blogspot.com/2026/10/india-imports-whey-protein-its-cheese.html", "India Imports the Whey Protein Its Cheese Makers Pour Away"),
]

build("Fisheries · 28 October 2026",
      "A Kilo of Crude Fish Oil Sells for About Rs 650. In Capsules It Retails for Rs 7,500 or More. India&rsquo;s Fishers Sell Only the Fish",
      "India loses tens of thousands of crore of fish after harvest and sends cheap catch and juveniles to fishmeal plants. Oil, fish amino fertiliser and better curing could turn that waste into products that keep for months, if fishers&rsquo; cooperatives own the first steps.",
      body, sources, related, OUT)
print("oil Rs/kg", OIL_RS_KG, "caps Rs/kg", CAPS_RS_KG, "meal", meal_val, "oil", oil_val, "m+o", mo_low, mo_high, "caps", caps_val)
