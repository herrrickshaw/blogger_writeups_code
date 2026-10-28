import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-biomass-aggregation.html'

# ---------------------------------------------------------------- data
MACHINES_LO, MACHINES_HI = 3.00e5, 3.24e5        # CRM machines to Punjab, Haryana, UP, Delhi since 2018 (PIB reply; explainer)
FUNDS_LO, FUNDS_HI = 3623, 3926.16               # Rs crore released (CEEW to 2024-25; explainer to 2025-26)
BALERS_RAKES = 4500                              # "more than 4,500 balers and rakes" (PIB parliament reply)
CHCS = 40000
BAL_SHARE_HI = BALERS_RAKES / MACHINES_LO * 100
BAL_SHARE_LO = BALERS_RAKES / MACHINES_HI * 100
# 2023-24 ex-situ supply-chain window
EXSITU_MT, EXSITU_CENTRES, EXSITU_CR, CENTRE_T = 1.5, 333, 600, 4500
PROJ_COST_CR, PROJ_SUBSIDY_CR = 1.8, 1.5         # project for 4,500 t a season; subsidy rounded
SUB_PER_T = EXSITU_CR * 1e7 / (EXSITU_MT * 1e6)
assert abs(EXSITU_CENTRES * CENTRE_T / 1e6 - 1.4985) < 1e-6
# scale comparisons, million tonnes
PUNJAB_EXSITU_2025 = 6.0
NW_RICE_BURNT = 23.0
HARYANA_STRAW = 7.3
COFIRED_FY25, COFIRED_2025_10M = 1.62, 3.42
COAL_POWER_FY24 = 859.25
COFIRE_7PC = COAL_POWER_FY24 * 0.07
COFIRED_SHARE = COFIRED_FY25 / COAL_POWER_FY24 * 100
# National Biomass Atlas of India (SSS-NIBE for MNRE; ASCI study, TE 2015-18): surplus Mt/yr (None = not read cleanly) and power potential MW
ATLAS = [  # state, surplus Mt, MW, in CRM's four states, main surplus crop
    ("Punjab", 22.25, 3022.1, True, "rice straw (about 18.8 Mt)"),
    ("Uttar Pradesh", 21.60, 2800.3, True, "wheat straw (about 13.0 Mt)"),
    ("Gujarat", 21.74, 2637.8, False, "see atlas"),
    ("Maharashtra", 21.49, 2629.5, False, "sugarcane, wheat"),
    ("Madhya Pradesh", None, 2516.4, False, "wheat (about 6.3 Mt), maize, rice"),
    ("Andhra Pradesh", 17.09, 1999.5, False, "see atlas"),
    ("Haryana", None, 1353.3, True, "rice (about 3.0 Mt), wheat (about 2.0 Mt)"),
]
ATLAS_NATIONAL_MT, ATLAS_NATIONAL_GW = 230, 28
MW_OUT = sum(mw for _, _, mw, crm, _ in ATLAS if not crm)
MW_IN = sum(mw for _, _, mw, crm, _ in ATLAS if crm)
# CEEW (2025, Punjab): delivered cost of paddy straw, Rs per tonne
AGG_15KM = 1330
DEL_50_LO, DEL_50_HI = 2500, 3000
PEL_50_LO, PEL_50_HI = 4000, 5000


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def chart_scale():
    rows = [("2023-24 supply-chain window, target", EXSITU_MT, "#1c5d99"),
            ("Biomass co-fired in coal plants, FY25", COFIRED_FY25, "#1c5d99"),
            ("Punjab ex-situ target, 2025", PUNJAB_EXSITU_2025, "#868e96"),
            ("Rice stubble burnt in NW India, Oct-Nov", NW_RICE_BURNT, "#a5402c"),
            ("7% co-firing on FY24 power-sector coal*", COFIRE_7PC, "#495057")]
    W, L, top, bh, gap, lab = 400, 10, 24, 16, 8, 196
    H = top + len(rows) * (bh + gap) + 34
    sc = (W - L - lab - 40) / 62
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Million tonnes of straw: the 2023-24 supply-chain window targets 1.5, coal plants co-fired 1.62 in FY25, Punjab targeted 6 ex-situ, about 23 is burnt in north-west India, and 7% co-firing would need about 60.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Biomass volumes, million tonnes a year</text>']
    for i, (n, v, col) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 12}" font-size="9.5" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 12}" font-size="9.5" fill="#212529">{v:.1f}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">*Illustrative: 7% of the power sector&rsquo;s 859 Mt of coal in 2023-24, by weight.</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Sources in the note at the end; arithmetic by this blog.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_mix():
    W, L, top, bh = 400, 10, 34, 26
    H = top + bh + 52
    other = MACHINES_LO - BALERS_RAKES
    sc = (W - 2 * L) / MACHINES_LO
    wb = max(BALERS_RAKES * sc, 3)
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Of about 3 lakh crop-residue machines funded since 2018, about 4,500 are balers and rakes.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Crop-residue machines funded since 2018, about 3 lakh</text>',
         f'<rect x="{L}" y="20" width="9" height="9" fill="#868e96"/><text x="{L + 13}" y="28" font-size="9.5" fill="#212529">Mulch, sow or incorporate straw in the field</text>',
         f'<rect x="{L + 250}" y="20" width="9" height="9" fill="#a5402c"/><text x="{L + 263}" y="28" font-size="9.5" fill="#212529">Balers and rakes</text>',
         f'<rect x="{L}" y="{top}" width="{other * sc:.1f}" height="{bh}" fill="#868e96"/>',
         f'<rect x="{L + other * sc:.1f}" y="{top}" width="{wb:.1f}" height="{bh}" fill="#a5402c"/>',
         f'<text x="{L + other * sc - 6:.1f}" y="{top + bh + 14}" font-size="9.5" fill="#a5402c" text-anchor="end">about {BALERS_RAKES:,} balers and rakes, {BAL_SHARE_LO:.1f}&ndash;{BAL_SHARE_HI:.1f}%</text>',
         f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Punjab, Haryana, Uttar Pradesh and Delhi; Lok Sabha replies as published by PIB.</text>',
         '</svg>']
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def t_costs():
    return table(["Step or form", "Cost, Rs a tonne", "Note"], [
        ("Collect, bale and haul to a straw bank 15 km away", f"{AGG_15KM:,}", "Cutting and baling are about half of procurement cost"),
        ("Bales delivered 50 km away", f"{DEL_50_LO:,}&ndash;{DEL_50_HI:,}", "Beyond about 50 km, hauling is likely uneconomic"),
        ("Briquettes or pellets delivered 50 km away", f"{PEL_50_LO:,}&ndash;{PEL_50_HI:,}", "Densified fuel is what coal plants and kilns can use"),
        ("Storage", "20&ndash;30% of delivered cost", "Straw is collected in weeks and used all year; stored below about 20% moisture"),
    ])


def chart_atlas():
    rows = sorted(ATLAS, key=lambda r: -r[2])
    W, L, top, bh, gap, lab = 400, 10, 36, 15, 7, 104
    H = top + len(rows) * (bh + gap) + 34
    sc = (W - L - lab - 60) / 3100
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Biomass power potential from surplus crop residue by state, in MW, from the National Biomass Atlas; four of the seven largest states are outside the crop residue management scheme.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Power potential of surplus crop residue, MW</text>',
         f'<rect x="{L}" y="20" width="9" height="9" fill="#1c5d99"/><text x="{L + 13}" y="28" font-size="9.5" fill="#212529">Covered by the CRM scheme</text>',
         f'<rect x="{L + 170}" y="20" width="9" height="9" fill="#a5402c"/><text x="{L + 183}" y="28" font-size="9.5" fill="#212529">Outside it</text>']
    for i, (n, mt, mw, crm, _) in enumerate(rows):
        y = top + i * (bh + gap)
        col = "#1c5d99" if crm else "#a5402c"
        s.append(f'<text x="{L + lab - 6}" y="{y + 11}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{mw * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + mw * sc + 4:.1f}" y="{y + 11}" font-size="9.5" fill="#212529">{mw:,.0f}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">National Biomass Atlas of India (SSS-NIBE, for MNRE), triennium ending 2017-18.</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Delhi, also covered by the scheme, is not shown.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def t_atlas():
    return table(["State", "Surplus crop residue, Mt a year", "Power potential, MW", "Main surplus", "In CRM scheme?"], [
        (n, f"{mt:.2f}" if mt else "not read cleanly", f"{mw:,.0f}", crop, "Yes" if crm else "No")
        for n, mt, mw, crm, crop in sorted(ATLAS, key=lambda r: -r[2])])


def t_schemes():
    return table(["Scheme", "Where", "What it pays for", "Support"], [
        ("Crop Residue Management (CRM), in-situ, since 2018", "Punjab, Haryana, UP, Delhi", "Machines that leave straw in the field: super seeders, Happy Seeders, mulchers, zero-till drills", "50% of machine cost for farmers; 80% for custom hiring centres up to Rs 30 lakh"),
        ("CRM ex-situ supply chain, revised 2023-24", "Same four states", "Balers, rakes, tedders, cutters, high-HP tractors, loaders, telehandlers for aggregators tied to a buyer", "65% of capital cost from Centre and state, 25% from the buying industry, 10% from the aggregator; about Rs 1.5 crore per 4,500-tonne project"),
        ("Sub-Mission on Agricultural Mechanisation (SMAM)", "All states", "Farm machinery and custom hiring centres in general", "40% for general farmers; 50% for SC/ST, small, marginal and north-eastern farmers"),
        ("CPCB pellet and torrefaction grant (2022)", "Delhi, Punjab, Haryana, NCR districts of Rajasthan and UP", "New plants turning paddy straw into pellets", "Rs 14 lakh per tonne an hour (non-torrefied, cap Rs 70 lakh); Rs 28 lakh (torrefied, cap Rs 1.4 crore); Rs 50 crore corpus"),
        ("MNRE National Bioenergy Programme", "All states", "Pellet and briquette plants", "Reported at about Rs 21 lakh per tonne an hour for pellets (cap Rs 1.05 crore) and Rs 9 lakh for briquettes; phase I to March 2026"),
        ("Biomass co-firing policy (SAMARTH)", "All coal plants", "Demand: 5% biomass from 2024-25, 7% from 2025-26", "A mandate, not a subsidy; NCR plants told to use at least 50% paddy residue from Punjab, Haryana or NCR"),
        ("GOBARdhan and SATAT", "All states", "Compressed-biogas plants, which can use straw", "Capital assistance and an administered gas price (see this blog&rsquo;s GOBARdhan piece)"),
    ])


def t_makers():
    return table(["Maker", "Based in", "Straw-handling machines (as listed)", "Indicative listed price"], [
        ("Shaktiman (Tirth Agro Technology)", "Rajkot, Gujarat", "Round balers SRB 45C and SRB 60+ (15&ndash;25 kg bales that can be lifted by hand); Big Round Baler SRB 120; square baler SBM 165 Plus; PTO and wheel-type hay rakes; super seeder", "SBM 165 Plus about Rs 9.7 lakh"),
        ("Dasmesh", "Punjab", "512 square baler; 631 round straw baler", "About Rs 11.5&ndash;15 lakh (square); about Rs 3.3 lakh (round)"),
        ("Swaraj (Mahindra group)", "Punjab", "SQ 180 square baler", "About Rs 11.3 lakh"),
        ("New Holland (CNH)", "Multinational, made and sold in India", "BC5060 square baler", "About Rs 12.9 lakh"),
        ("Claas", "German brand", "Markant and Quadrant square balers", "Markant about Rs 11 lakh"),
        ("Fieldking (Beri Udyog)", "Haryana", "Square baler", "One listing shows about Rs 23 lakh, which may be an error"),
        ("John Deere", "Multinational", "Compact round baler", "About Rs 3.5 lakh"),
        ("Farmpower", "Punjab", "Small baler for paddy and wheat straw", "About Rs 2.8 lakh"),
    ])


def t_extend():
    return table(["Step", "What it would change", "Where to start"], [
        ("Open the 65:25:10 supply-chain window to every state with a buyer", "Aggregators outside the four northern states could buy balers, rakes and loaders against a contract with a power plant, pellet maker, CBG plant or 2G ethanol plant", "Gujarat, Maharashtra, Andhra Pradesh and Madhya Pradesh, which the National Biomass Atlas shows have surpluses close to Punjab&rsquo;s, starting with districts within 50 km of coal plants under the co-firing mandate and of commissioned CBG plants"),
        ("Fund aggregation sets, not single machines", "A baler is useless without a rake, a loader and a trailer; projects should be priced as sets, as the 2023-24 window does", "Custom hiring centres that already own high-HP tractors"),
        ("Pay part of the subsidy per tonne delivered", "Ties public money to straw actually collected rather than machines bought; CEEW and others have reported idle CRM machines", "New projects from the next season"),
        ("Working capital and storage", "Straw is collected in four to six weeks and used all year; depots and credit decide whether the chain survives", "Agriculture Infrastructure Fund and NABARD lines already named in the guidelines"),
        ("Extend the pellet grants beyond the NCR", "CPCB&rsquo;s grant covers only plants using straw from the NCR states; pellets are the form coal plants can use", "Rice and cotton belts in Madhya Pradesh, Bihar, eastern UP, Andhra Pradesh, Telangana and Maharashtra"),
        ("Back Indian machine makers to localise large balers", "Square balers sell for about Rs 10&ndash;15 lakh; a domestic baler and knotter supply chain lowers the 35% the aggregator and industry must find", "Makers such as Shaktiman, Dasmesh, Swaraj and Fieldking already build balers"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>~3 lakh</b><span>crop-residue machines funded in four northern states since 2018, for Rs {FUNDS_LO:,.0f}&ndash;{FUNDS_HI:,.0f} crore</span></div>
<div class="gb-stat"><b>~4,500</b><span>of them are balers and rakes, the machines that collect straw, about {BAL_SHARE_HI:.1f}%</span></div>
<div class="gb-stat"><b>1.5 Mt</b><span>of straw a year targeted by the 2023-24 supply-chain window, against about 23 Mt burnt in north-west India</span></div>
<div class="gb-stat"><b>{COFIRED_SHARE:.1f}%</b><span>biomass actually co-fired in coal plants in FY25 (1.62 Mt), against a 5&ndash;7% mandate</span></div>
</div>'''

body = f"""
{stats}

<p>India has spent about seven years and Rs 3,600&ndash;3,900 crore on machines to stop farmers in Punjab, Haryana, Uttar Pradesh and Delhi burning paddy straw. Almost all of that money bought machines that deal with the straw in the field: super seeders, Happy Seeders, mulchers and zero-till drills. Only about 4,500 of some 3 lakh machines are balers and rakes, the equipment that gathers straw so that someone else can use it. Meanwhile coal plants are under a mandate to burn 5&ndash;7% biomass and used only a fraction of that.</p>
<p>The <a href="https://gobardhan.sbm.gov.in/assets/guidelines/Crop_Residue_Management_Guidelines_2023-24.pdf">Crop Residue Management guidelines for 2023-24</a>, now hosted on the GOBARdhan portal, were the government&rsquo;s first attempt to fund that collection chain. This piece sets out what the guidelines do, how they fit with the other biomass schemes, which Indian companies make the machines, and what it would take to extend aggregation machinery to farmers across India.</p>

<h2 class="gb-h2">What the 2023-24 guidelines changed</h2>
<p>The guidelines add an &ldquo;ex-situ&rdquo; window to the Crop Residue Management scheme. An aggregator, which can be a farmer, a rural entrepreneur, a cooperative, a farmer-producer organisation or a panchayat, signs a contract with an industry that uses paddy straw. The Centre and the state pay 65% of the capital cost of the machinery, the industry pays 25% and the aggregator 10%. Eligible equipment includes higher-HP tractors, cutters, tedders, medium and large balers, rakes, loaders, grabbers and telehandlers. A project sized for 3,000 tonnes a season was costed at about Rs 1 crore and one for 4,500 tonnes at about Rs 1.8 crore, with the subsidy rounded to Rs 1.5 crore. Working capital is left to the industry and aggregator, or to the Agriculture Infrastructure Fund, NABARD and banks.</p>
<p>The target was 1.5 million tonnes of straw through {EXSITU_CENTRES} collection centres of 4,500 tonnes each, with Rs {EXSITU_CR} crore of assistance: about Rs {SUB_PER_T:,.0f} of capital subsidy for each tonne of yearly collection capacity. Reports differ on whether the industry&rsquo;s 25% is for machinery or for operating costs. No count of projects sanctioned or tonnes collected under the window was found.</p>

<h2 class="gb-h2">The machines bought so far mostly keep straw in the field</h2>
{chart_mix()}
<p>Since 2018 the four states have distributed about 3 lakh machines to individual farmers and more than {CHCS:,} custom hiring centres, according to Lok Sabha replies published by PIB. Of these, &ldquo;more than 4,500&rdquo; are balers and rakes. In-situ machines have a real case: they avoid moving straw at all. But they do nothing for the industries that need straw, and they leave the straw-using economy with almost no collection fleet. Punjab alone targeted about 6 million tonnes of straw for ex-situ use in 2025, and Haryana produces about 7.3 million tonnes of paddy straw a year.</p>

<h2 class="gb-h2">Demand is far larger than the collection chain</h2>
{chart_scale()}
<p>Coal plants co-fired about 1.62 million tonnes of biomass in 2024-25, up from 0.38 million tonnes a year earlier, and about 3.42 million tonnes in January to October 2025, according to the power ministry as reported by Argus. The power sector burnt about 859 million tonnes of coal in 2023-24, so the 2024-25 volume was about {COFIRED_SHARE:.1f}% of that coal. If the 7% mandate were met by weight, it would need about {COFIRE_7PC:.0f} million tonnes of biomass a year, more than twice the rice stubble burnt in north-west India each autumn. Straw for plants near Delhi must be at least half paddy residue from Punjab, Haryana or the NCR under the power ministry&rsquo;s model contract. Brick kilns outside the NCR in Punjab and Haryana have been told to use paddy-straw pellets or briquettes.</p>
<p>The binding constraint is collection, not demand. A baler and rake combination cost about Rs 15 lakh in 2020, biomass plants in Punjab were reported paying about Rs 169 a quintal (about Rs 1,690 a tonne) for straw, and listing sites put baled straw at Rs 800&ndash;1,500 a tonne to paper mills and power plants. At those prices, the margin for an aggregator depends on running the machines for as many tonnes as possible in a short window, which is what the ex-situ design tries to guarantee by tying each project to a buyer.</p>

<h2 class="gb-h2">Where the surplus is: the National Biomass Atlas</h2>
{chart_atlas()}
<p>SSS-NIBE&rsquo;s <a href="https://nibe.res.in/english/biomass-atlas.php">National Biomass Atlas of India</a>, built on a study by the Administrative Staff College of India for the Ministry of New and Renewable Energy, puts India&rsquo;s surplus agricultural residue at about {ATLAS_NATIONAL_MT} million tonnes a year, enough for about {ATLAS_NATIONAL_GW} GW of biomass power, on 2015&ndash;18 data. &ldquo;Surplus&rdquo; is what is left after fodder, fuel and other existing uses. Its state table shows that the residue is not concentrated where the crop-residue scheme spends. Gujarat, Maharashtra and Andhra Pradesh each have a surplus of about 17&ndash;22 million tonnes, close to Punjab&rsquo;s 22 million, and Madhya Pradesh&rsquo;s residue supports about as much power as theirs. None of them is covered by the crop-residue machinery scheme. Of the seven states in the table, those outside the scheme account for about {MW_OUT:,.0f} MW of potential against {MW_IN:,.0f} MW inside it.</p>
{t_atlas()}
<p class="gb-note">Figures as shown on the atlas page and in the power ministry&rsquo;s SAMARTH copy of the same table; parts of the published table are garbled, so the Maharashtra total and the missing totals should be checked against the atlas download. Older estimates (for example, 234 million tonnes of surplus in a 2014 study, or 178 million tonnes in a CSE report) differ in years and assumptions.</p>
<p>The atlas also shows that the surplus is not all rice straw. Uttar Pradesh&rsquo;s and Madhya Pradesh&rsquo;s largest surplus is wheat straw, Maharashtra&rsquo;s is sugarcane and wheat residue, and in the cotton belt it is cotton stalk. A national aggregation programme would need different machines for each: balers and rakes for loose straw, shredders and stalk pullers for cotton and pigeon-pea stalks, and trash balers for sugarcane.</p>

<h2 class="gb-h2">What collection actually costs</h2>
{t_costs()}
<p>The Sardar Swaran Singh National Institute of Bio-Energy (SSS-NIBE) in Kapurthala, the Ministry of New and Renewable Energy&rsquo;s research institute, has been the main official voice on this. Its director general has described the core problem as a feedstock that is seasonal, voluminous and low in energy, and paddy straw as harder than wheat, cotton, mustard or maize residue because of its high ash and low calorific value. A 2025 review by SSS-NIBE researchers with US national-laboratory co-authors notes that the economics of biomass supply chains in India are under-studied. The institute ran a national seminar on biomass supply-chain management in Chandigarh in 2024, where Punjab&rsquo;s science council set out the state&rsquo;s paddy-straw problems.</p>
<p>The clearest cost figures come from CEEW&rsquo;s 2025 work in Punjab. Collecting, baling and hauling straw to a straw bank 15 km away costs about Rs {AGG_15KM:,} a tonne of bales, and cutting and baling make up about half of the procurement cost. Delivered to a buyer 50 km away, bales cost about Rs {DEL_50_LO:,}&ndash;{DEL_50_HI:,} a tonne, and briquettes or pellets Rs {PEL_50_LO:,}&ndash;{PEL_50_HI:,}. Storage is 20&ndash;30% of the delivered cost, and hauling beyond about 50 km is likely to be uneconomic. Against straw prices of roughly Rs 1,700 a tonne at the plant gate, that leaves little margin unless machines run at full use and buyers sit close to the fields. That is why aggregation machinery has to be sited around buyers, not spread evenly across districts.</p>

<h2 class="gb-h2">The schemes that touch biomass aggregation</h2>
{t_schemes()}
<p class="gb-note">Rates are as reported in official releases and summaries; the MNRE and CPCB rates differ between sources and should be checked against the current office memoranda.</p>
<p>The pieces exist, but they do not join up. The machinery subsidy that funds collection is confined to four states; the pellet grant is confined to the NCR; the general mechanisation scheme pays only 40&ndash;50% and is not tied to a buyer; and the co-firing mandate creates demand everywhere without paying for the machines that would meet it.</p>

<h2 class="gb-h2">Who makes the machines</h2>
{t_makers()}
<p class="gb-note">Prices are indicative figures from Indian tractor-listing sites (2025&ndash;26), not dealer quotes; they vary by state, dealer and accessories. Inclusion is not an endorsement.</p>
<p>India already has a domestic industry for these machines. Shaktiman, founded in Rajkot in 1997 as a spare-parts maker and now with dealers in many countries by its own account, lists a range that runs from small round balers producing 15&ndash;25 kg bales that a person can lift, through a big round baler, to a square baler and hay rakes, alongside the super seeders that the in-situ scheme has favoured. Punjab makers such as Dasmesh and Swaraj, Haryana&rsquo;s Fieldking and multinationals assembling in India (New Holland, Claas, John Deere) sell square and round balers. Small square balers need 35&ndash;45 HP tractors, which most custom hiring centres already have. Small round balers suit smallholdings and manual handling; square balers suit trucking to plants. A national programme would need both.</p>

<h2 class="gb-h2">How to extend aggregation machinery across India</h2>
{t_extend()}

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Ministry of Agriculture should publish, for every ex-situ project, the aggregator, the buying industry, the machines funded and the tonnes delivered each season.</li>
<li>The ex-situ window should be opened to all states, with eligibility tied to a signed offtake contract with a co-firing plant, pellet plant, CBG plant or 2G ethanol plant rather than to geography.</li>
<li>Part of the subsidy should be paid per tonne delivered, so that public money follows straw collected, not machines bought.</li>
<li>The Ministry of Power should publish biomass co-fired by plant and by source state each month, so that collection projects can be sited where demand is.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The 2023-24 guidelines could not be opened from this blog&rsquo;s research environment; their terms come from the PIB release of July 2023 and consistent secondary summaries. The number of ex-situ projects sanctioned and tonnes collected under them was not found. Machine totals differ between sources (3.0 lakh in a PIB reply, 3.24 lakh in an explainer) and so do fund totals (Rs 3,623 crore and Rs 3,926 crore), probably because of different cut-off years. Straw prices are older reported figures. Machine prices are listing-site figures, and Shaktiman&rsquo;s product range is from its own site and trade-fair listing. The co-firing requirement in tonnes is an illustration on a weight basis, not an official estimate. The National Biomass Atlas page could not be opened from this blog&rsquo;s research environment; its state figures were read from the page&rsquo;s indexed text and the SAMARTH copy, and two state totals could not be read cleanly. No standalone SSS-NIBE report on biomass collection and use was found; this piece draws on the institute&rsquo;s published review, its director general&rsquo;s statements and its 2024 seminar, and on CEEW&rsquo;s cost estimates for Punjab.</p>
"""

sources = ("CRM 2023-24 guidelines: PIB release of 1 July 2023 (PRID 1936626) and summaries by Down To Earth, Deccan Herald, PMF IAS and Agro Spectrum; guideline PDF on the GOBARdhan portal (gobardhan.sbm.gov.in). Machines, CHCs, balers and rakes, subsidy rates: PIB parliament replies (PRIDs 2112397, 2198748, 2240644); CEEW on CRM machines and custom hiring centres; Eminent IAS explainer for the Rs 3,926 crore total. Punjab ex-situ target and Rs 500 crore: CEEW; Haryana straw: Vision IAS summary. "
           "SMAM rates: scheme summaries (Sanskriti IAS, newskart). CPCB pellet and torrefaction grant: PIB (PRID 1867506), S.S. Rana. MNRE bioenergy programme rates: industry summaries citing the MNRE office memorandum of 16 July 2024. Co-firing mandate and volumes: Ministry of Power policy as summarised by IMPRI and Power Line; Argus Media (December 2025) citing the power ministry; power-sector coal use 2023-24: CSE citing NITI Aayog. Rice stubble burnt in north-west India: published review cited in this blog&rsquo;s cotton-stalk piece. "
           "National Biomass Atlas of India (SSS-NIBE for MNRE, ASCI study, TE 2015-18), nibe.res.in, and the SAMARTH &lsquo;All India&rsquo; state table (samarth.powermin.gov.in). SSS-NIBE: its director general as quoted by the Energy Institute (New Energy World); Ahmed et al. (2025), &ldquo;Biomass to bio-energy supply chain: economic viability, case studies, challenges and policy implications in India&rdquo; (PNNL record); SSS-NIBE national seminar on biomass supply-chain management (2024, iamrenew). Collection costs: CEEW, ex-situ crop residue management and paddy-straw storage reports and annexure (2025). Straw and machine prices: The Tribune; Hindustan Times (2020); TractorJunction, TractorGyan and Tractor For Everyone listings. Shaktiman: shaktimanagro.com and its EIMA exhibitor listing. Shares, per-tonne subsidy and the co-firing illustration are this blog&rsquo;s arithmetic. Not investment advice; machine mentions are not endorsements.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/ethanols-coal-boilers-briquette-gap-and.html", "Ethanol&rsquo;s Coal Boilers, the Briquette Gap, and What US Carbon Capture Actually Delivers"),
    ("https://masaladeutsch.blogspot.com/2026/10/cotton-stalk-is-one-of-hardest-crop.html", "Cotton Stalk Is One of the Hardest Crop Wastes to Turn Into Gas"),
    ("https://masaladeutsch.blogspot.com/2026/10/bagasse-is-one-crop-residue-already.html", "Bagasse Is the One Crop Residue Already Sitting at a Factory Gate"),
    ("https://masaladeutsch.blogspot.com/2026/10/gobardhan-aims-for-12-times-todays.html", "GOBARdhan Aims for 12 Times Today&rsquo;s Biogas Output"),
    ("https://masaladeutsch.blogspot.com/2026/08/biomass-power-at-night-dispatchable.html", "Biomass Power at Night: The Dispatchable Renewable India&rsquo;s Growth Numbers Left Behind"),
]

build("Agriculture · 28 October 2026",
      "India Has Funded 3 Lakh Machines to Stop Stubble Burning. About 4,500 of Them Collect Straw",
      "The 2023-24 crop residue guidelines added a 65:25:10 window to fund balers, rakes and loaders for straw aggregators tied to a buyer, but only in four northern states. Coal plants, pellet makers and biogas plants across India need far more straw than that chain can collect.",
      body, sources, related, OUT)
print("bal share", round(BAL_SHARE_LO, 2), round(BAL_SHARE_HI, 2), "sub/t", round(SUB_PER_T), "cofire share", round(COFIRED_SHARE, 2), "7pc", round(COFIRE_7PC, 1))
