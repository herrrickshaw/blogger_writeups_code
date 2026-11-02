import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-spark-plugs-ethanol.html'

# ---- Trade: HS 851110 (spark plugs), India, calendar 2023, UN Comtrade via WITS -------------
# (partner, value US$ thousand, pieces)
IMP = [
    ("Japan",         10763.19,  5_929_360),
    ("China",          6269.27, 63_125_900),
    ("Thailand",       3833.93,  3_271_080),
    ("South Korea",    3283.00,  1_326_650),
    ("United States",  2858.93,    272_527),
]
IMP_TOTAL = (32219.38, 74_929_800)
EXP = [
    ("Germany",       15982.81, 20_672_800),
    ("Bangladesh",     4217.13,  6_305_510),
    ("South Korea",    1515.00,    693_445),
    ("United States",  1202.12,  1_468_620),
    ("UAE",            1052.77,    643_789),
]
EXP_TOTAL = (37255.76, 43_619_300)
USD_INR = 83.0          # rounded 2023 average, for rupee conversions only


def unit_usd(v, q):
    return v * 1000 / q


IMP_U = [(n, v, q, unit_usd(v, q)) for n, v, q in IMP]
EXP_U = [(n, v, q, unit_usd(v, q)) for n, v, q in EXP]
IMP_TOTAL_U = unit_usd(*IMP_TOTAL)
EXP_TOTAL_U = unit_usd(*EXP_TOTAL)
CHINA_SHARE_PCS = 63_125_900 / IMP_TOTAL[1] * 100
CHINA_SHARE_VAL = 6269.27 / IMP_TOTAL[0] * 100
JAPAN_SHARE_VAL = 10763.19 / IMP_TOTAL[0] * 100
JAPAN_SHARE_PCS = 5_929_360 / IMP_TOTAL[1] * 100

# ---- Air-fuel chemistry: how much leaner E20 runs in an engine set up for E10 ---------------
# Stoichiometric air-fuel ratios by mass (textbook values) and densities (kg/l)
AFR_PETROL, AFR_ETHANOL = 14.7, 9.0
RHO_PETROL, RHO_ETHANOL = 0.745, 0.789


def blend(vol_eth):
    m_e = vol_eth * RHO_ETHANOL
    m_p = (1 - vol_eth) * RHO_PETROL
    w = m_e / (m_e + m_p)                     # ethanol mass fraction
    afr = w * AFR_ETHANOL + (1 - w) * AFR_PETROL
    return w, afr


W10, AFR10 = blend(0.10)
W20, AFR20 = blend(0.20)
# Oxygen mass share: ethanol is 34.7% oxygen by mass
O10, O20 = W10 * 34.7, W20 * 34.7
LEAN_PCT = (AFR10 / AFR20 - 1) * 100          # % more air than the fuel needs, first-order, fixed fuel mass

# ---- Owner cost scenario (all assumptions labelled in the text) ---------------------------
KM_YEAR = 8000           # assumption: km a year for a commuter two-wheeler
INTERVAL_OLD = 12000     # Honda Activa manual: replace every 12,000 km
INTERVAL_NEW = 9000      # assumption: 25% shorter life on E20 in an old carburetted engine
PLUG_RS = 170            # NGK standard two-wheeler plug, online retail (MR7C9N)
LABOUR_RS = 100          # assumption: workshop fitting charge if done outside a service
KMPL = 50                # assumption: commuter two-wheeler mileage
PETROL_RS = 94.77        # Delhi petrol price quoted by MoPNG, Rajya Sabha, 3 Aug 2026
NITI_LOSS = (0.03, 0.04)  # NITI Aayog 2021: 3-4% for 2W designed for E0, calibrated for E10

plugs_old = KM_YEAR / INTERVAL_OLD
plugs_new = KM_YEAR / INTERVAL_NEW
extra_plugs = plugs_new - plugs_old
extra_plug_cost = extra_plugs * (PLUG_RS + LABOUR_RS)
fuel_bill = KM_YEAR / KMPL * PETROL_RS
mileage_cost = (fuel_bill * NITI_LOSS[0], fuel_bill * NITI_LOSS[1])
per_crore = extra_plug_cost * 1e7 / 1e7      # Rs crore a year per crore vehicles
IRIDIUM_RS = 865

# ---- Chart: average import value per plug, by source ------------------------------------


def chart_unit():
    rows = sorted(IMP_U, key=lambda r: -r[3])
    W, L, top, bh, gap, lab = 340, 4, 46, 20, 9, 92
    H = top + len(rows) * (bh + gap) + 46
    mx = max(r[3] for r in rows)
    sc = (W - L - lab - 92) / mx
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Average declared value per spark plug imported into India in 2023, by source country.">',
         f'<text x="{L}" y="15" font-size="14" fill="#495057">Value per imported spark plug, 2023</text>',
         f'<text x="{L}" y="33" font-size="11.5" fill="#6c757d">US$ (rupees), top five sources by value</text>']
    for i, (n, v, q, u) in enumerate(rows):
        y = top + i * (bh + gap)
        w = max(u * sc, 2)
        s.append(f'<text x="{L + lab - 6}" y="{y + 15}" font-size="12.5" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{w:.1f}" height="{bh}" fill="#1c5d99"/>')
        s.append(f'<text x="{L + lab + w + 5:.1f}" y="{y + 15}" font-size="12.5" fill="#212529">${u:.2f} (&#8377;{u * USD_INR:,.0f})</text>')
    s.append(f'<text x="{L}" y="{H - 24}" font-size="10.5" fill="#6c757d">UN Comtrade via WITS, HS 851110; &#8377;83 = US$1.</text>')
    s.append(f'<text x="{L}" y="{H - 8}" font-size="10.5" fill="#6c757d">US figure likely includes aircraft igniter plugs.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def lakh(n):
    return f"{n / 1e5:,.1f} lakh" if n < 1e7 else f"{n / 1e7:,.2f} crore"


def t_trade():
    rows = [(f"Import: {n}", f"{v / 1000:.1f}", lakh(q), f"{u:.2f}") for n, v, q, u in IMP_U]
    rows.append(("<b>All imports</b>", f"<b>{IMP_TOTAL[0] / 1000:.1f}</b>", f"<b>{lakh(IMP_TOTAL[1])}</b>", f"<b>{IMP_TOTAL_U:.2f}</b>"))
    rows += [(f"Export: {n}", f"{v / 1000:.1f}", lakh(q), f"{u:.2f}") for n, v, q, u in EXP_U]
    rows.append(("<b>All exports</b>", f"<b>{EXP_TOTAL[0] / 1000:.1f}</b>", f"<b>{lakh(EXP_TOTAL[1])}</b>", f"<b>{EXP_TOTAL_U:.2f}</b>"))
    return table(["2023, HS 851110", "US$ million", "Pieces", "US$ per plug"], rows)


def t_life():
    return table(["Plug and vehicle", "Replace every", "Price"], [
        ("Standard, Honda Activa (current)", "12,000 km", "&#8377;170"),
        ("Standard, older Activa (SCV110)", "9,000 km", "&mdash;"),
        ("Conventional, motorcycle (Denso, Japan)", "3,000&ndash;5,000 km", "&mdash;"),
        ("Conventional, car (Denso, Japan)", "15,000&ndash;20,000 km", "&mdash;"),
        ("Iridium, two-wheeler (NGK Iridium IX)", "longer; no fixed interval found", "&#8377;816&ndash;940"),
        ("Platinum or iridium, car", "up to 100,000 km", "&#8377;1,548 a set (Honda City)"),
    ]) + ('<p class="gb-note">Intervals: Honda Activa owner&rsquo;s and service manuals; Denso spark plug catalogue. '
          'Prices: standard NGK two-wheeler plug and NGK Iridium IX at Indian online retailers, 2026; Honda City set from V3Cars&rsquo; service schedule.</p>')


def t_mech():
    rows = [
        ("Carries oxygen, so needs less air", "Engine set up for E10 runs leaner: hotter combustion, hotter plug tip, faster electrode wear", "carburetted and other open-loop engines"),
        ("Absorbs more heat as it evaporates", "Cooler, wetter mixture at a cold start: harder lighting, possible fouling", "carburetted engines on cold mornings"),
        ("Higher octane (resists knock)", "Less knock heating; tuned engines can advance timing, which can call for a colder plug", "engines calibrated for E20 or higher"),
        ("Burns with less soot", "Fewer carbon deposits on the insulator", "all engines"),
        ("Attracts water; can carry acids", "Corrosion risk, mostly in the fuel system rather than the plug", "vehicles left standing; poor-quality fuel"),
    ]
    return table(["What ethanol changes", "What it can do at the plug, and where"],
                 [(a, f"{b}. <i>Mainly: {c}.</i>") for a, b, c in rows])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>20 crore+</b><span>two-wheelers, plus over 3 crore petrol cars, now run on E19&ndash;E20 petrol, by the Petroleum Ministry&rsquo;s count</span></div>
<div class="gb-stat"><b>~{LEAN_PCT:.0f}% leaner</b><span>is how an engine set up for E10 runs on E20 if nothing adjusts the fuel: this blog&rsquo;s arithmetic from standard fuel properties</span></div>
<div class="gb-stat"><b>20&ndash;70&deg;C</b><span>rise in exhaust temperature from E0 to E20 in small open-loop engines tested by the US Department of Energy (2009)</span></div>
<div class="gb-stat"><b>{CHINA_SHARE_PCS:.0f}%</b><span>of the spark plugs India imported in 2023 came from China, at about 10 cents each; Japan sent {JAPAN_SHARE_PCS:.0f}% of the pieces but {JAPAN_SHARE_VAL:.0f}% of the value</span></div>
</div>'''

body = f"""
{stats}

<p>India&rsquo;s oil companies have blended about 20% ethanol into petrol since late 2025, and the argument about E20 has been mostly about mileage and rubber seals. The spark plug has barely come up, though it is the engine part an owner replaces most often and the one that sits in the flame. This piece looks at what ethanol does to a spark plug, which vehicles that matters for, what the official tests and manufacturers have said, what it might cost an owner, and who makes and imports the plugs India uses.</p>

<p>The short answer: in a modern fuel-injected engine with an oxygen sensor, E20 makes little difference to the plug. The exposure is in older carburetted two-wheelers, which cannot adjust their fuel to ethanol&rsquo;s oxygen and so run leaner and hotter. Even there the likely cost of extra plugs is small next to the mileage loss. But no Indian test of plug wear on E20 has been published, so &ldquo;small&rdquo; is an estimate, not a measurement.</p>

<h2 class="gb-h2">What ethanol changes inside the cylinder</h2>

<p>A spark plug has one job: deliver a spark across a gap of about a millimetre, at the right moment, thousands of times a minute, while sitting in combustion gases at well over 2,000&deg;C. It works only within a temperature window. NGK, the largest plug maker, says that below about 450&deg;C the insulator tip collects carbon and the spark leaks away (&ldquo;fouling&rdquo;), and that if the tip overheats &ldquo;the electrodes wear quickly&rdquo; and it can ignite the mixture early (&ldquo;pre-ignition&rdquo;). How hot a plug runs depends on its design, its &ldquo;heat range&rdquo;, and on the engine and fuel.</p>

{t_mech()}

<p>The first row matters most. Ethanol is about 35% oxygen by mass. Burning a kilogram of petrol needs about {AFR_PETROL} kg of air; a kilogram of ethanol needs about {AFR_ETHANOL}. By this blog&rsquo;s arithmetic, E10 needs about {AFR10:.1f} kg of air per kg of fuel and E20 about {AFR20:.1f}. An engine that meters fuel for E10 and is then given E20, with nothing to correct it, is getting roughly {LEAN_PCT:.0f}% more air than the fuel needs. This is a first-order estimate that ignores small density differences.</p>

<p>Fuel-injected engines with an oxygen sensor in the exhaust measure this and add fuel. Bharat Stage VI emission rules from April 2020 moved most new Indian two-wheelers to fuel injection. Carburetted engines, which include most two-wheelers sold before then, have no such sensor: they run leaner on E20 for as long as they run. Leaner mixtures burn hotter. In 2009 the US Department of Energy tested small open-loop engines (lawn mowers, generators, trimmers) on blends up to E20. As ethanol rose, exhaust, cylinder-head and cylinder temperatures generally rose too, with exhaust temperatures 20&ndash;70&deg;C higher on E20 than on ethanol-free petrol. Those engines are not Indian motorcycles, but they work on the same principle as a carburetted commuter bike.</p>

<p>A hotter plug tip wears its electrodes faster, and the gap widens. A wider gap needs more voltage to spark, and a lean mixture is itself harder to light, so the two effects stack: the end of a plug&rsquo;s life shows up as misfires and hard starting sooner than it would on E10. Ethanol&rsquo;s other effects pull the other way. It cools the mixture as it evaporates, burns with less soot, and resists knock. Brazil, which has run engines on pure ethanol since 1979, fitted those cars with colder plugs to shed the extra heat, and Bosch&rsquo;s Brazilian engineers later designed plugs for multi-fuel engines with better cold starts, less sooting and better corrosion protection.</p>

<h2 class="gb-h2">What the official tests say, and do not say</h2>

<p>The government&rsquo;s position, repeated in answers to Parliament through 2026, is that tests by the Automotive Research Association of India (ARAI), Indian Oil, the Indian Institute of Petroleum and the carmakers&rsquo; body SIAM found no abnormal wear in older vehicles on E20. It says only some rubber parts and gaskets in certain older vehicles may need replacing earlier, once in a vehicle&rsquo;s life, and that insurance and warranties are unaffected. Maruti Suzuki says that of 2.84 crore cars it serviced in 2025-26, more than 1.5 crore were over three years old and so not certified for E20, and none showed E20-related corrosion, abnormal wear or shorter component life. Hero MotoCorp says its service data show no higher damage on E20.</p>

<p>None of these statements, as published, mentions spark plugs. Nor are the tests themselves public: The Hindu reported in July 2026 that the IOCL&ndash;IIP&ndash;SIAM&ndash;ARAI study on older vehicles &ldquo;has not yet been made public&rdquo;. The Ministry of Heavy Industries told Parliament that it compiles no data on complaints and has issued no directions to manufacturers on replacement schedules for parts exposed to higher blends. The government&rsquo;s own 2021 roadmap, drawn up by a NITI Aayog committee, did quantify mileage: a 3&ndash;4% loss for two-wheelers designed for E0 and calibrated for E10, and 6&ndash;7% for comparable cars.</p>

<p>The two-wheeler makers&rsquo; comfort is also not quite the same as the evidence a carburetted-bike owner would want. A carmaker&rsquo;s serviced fleet that is over three years old is largely fuel-injected; India&rsquo;s cars moved to injection long before its motorcycles did. Hero&rsquo;s statement covers its whole fleet, not carburetted models separately.</p>

<h2 class="gb-h2">What a shorter plug life would cost</h2>

<p>A spark plug is cheap. Honda&rsquo;s current Activa manual says to replace the plug every 12,000 km; an older Activa manual said 9,000 km. Japanese guidance from Denso is far shorter for motorcycles, 3,000&ndash;5,000 km for conventional plugs. Most car engines now use iridium or platinum plugs that last up to 100,000 km.</p>

{t_life()}

<p>To size the risk, take a carburetted commuter scooter ridden {KM_YEAR:,} km a year. These are assumptions, not measurements. Suppose E20 cut plug life from {INTERVAL_OLD:,} km to {INTERVAL_NEW:,} km, a quarter shorter. The owner would buy {extra_plugs:.2f} extra plugs a year, at about &#8377;{PLUG_RS} each plus &#8377;{LABOUR_RS} for fitting outside a scheduled service: about <b>&#8377;{extra_plug_cost:.0f} a year</b>. Across a crore such vehicles, that is about &#8377;{per_crore:.0f} crore a year.</p>

<p>The mileage loss on the same scooter is far larger. At {KMPL} km a litre and Delhi&rsquo;s &#8377;{PETROL_RS} a litre, the fuel bill is about &#8377;{fuel_bill:,.0f} a year; NITI Aayog&rsquo;s 3&ndash;4% loss is &#8377;{mileage_cost[0]:,.0f}&ndash;{mileage_cost[1]:,.0f} a year. Fitting an iridium plug at about &#8377;{IRIDIUM_RS} is an option for a worried owner, but it is a hedge against an unmeasured risk, and a carburettor re-set for E20 at a workshop addresses the cause (the lean mixture) rather than the symptom.</p>

<h2 class="gb-h2">Who makes and imports India&rsquo;s spark plugs</h2>

<p>India&rsquo;s market is dominated by the global names: Bosch, Niterra (the Japanese company formerly called NGK Spark Plug, whose Indian arm was renamed Niterra India in 2023), Denso and Champion (part of Federal-Mogul, now Tenneco), alongside Indian ignition-system suppliers named in market reports, such as Lucas TVS, India Nippon Electricals and Minda group firms. Consultancy estimates of the market&rsquo;s size, such as IMARC&rsquo;s US$155 million for 2025, cannot be checked against any official series. Niterra builds plugs at Bawal in Haryana and in 2017 announced a &yen;1.7 billion (about &#8377;100 crore at 2017 rates) expansion to double capacity. Its Indian media kit says the plant made nickel plugs and that iridium and platinum plugs were imported from Japan; it is not dated, and may be out of date.</p>

<p>Trade data show the same split. In 2023 India exported more spark plugs by value than it imported, about US${EXP_TOTAL[0] / 1000:.1f} million against US${IMP_TOTAL[0] / 1000:.1f} million. Germany took {15982.81 / EXP_TOTAL[0] * 100:.0f}% of exports, at about 77 US cents a plug. Imports came in two kinds. China sent {lakh(63_125_900)} plugs, {CHINA_SHARE_PCS:.0f}% of all pieces but {CHINA_SHARE_VAL:.0f}% of the value, at about 10 US cents (&#8377;8) each. Japan sent {lakh(5_929_360)} plugs worth {JAPAN_SHARE_VAL:.0f}% of the import bill, at about US$1.82 (&#8377;150) each, consistent with the premium plugs that iridium and platinum tips require.</p>

{chart_unit()}

{t_trade()}

<p>If E20, and the E27 and E30 blends now being discussed, push owners and manufacturers towards long-life iridium plugs, the money will flow mostly to the plants that put the precious-metal tips on, which for India&rsquo;s imports today are mainly in Japan, Thailand and South Korea. India has no commercial platinum-group metal mining. The volume opportunity is in cheaper plugs; the margin is in the tips.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The oil and heavy industries ministries should publish the IOCL&ndash;IIP&ndash;SIAM&ndash;ARAI legacy-vehicle study in full, including the condition of spark plugs and their electrode gaps at the end of each durability run, broken out by carburetted and fuel-injected vehicles.</li>
<li>ARAI or the Indian Institute of Petroleum should run a short, public fleet test on the most common pre-2020 carburetted motorcycles and scooters: plug gap growth per 1,000 km on E10 and E20, before and after re-setting the carburettor.</li>
<li>Two-wheeler makers should publish model-by-model advice for their carburetted models: whether the plug interval or type should change on E20, and what a workshop should adjust in the carburettor. The government says owners can ask authorised workshops for tuning; a published list would tell them what to ask for.</li>
<li>Before E27 or E30, the standards body should ask whether plugs need ethanol-specific designs or labelling, as Brazil&rsquo;s makers developed plugs for multi-fuel engines, and the industry ministry should look at whether tipping iridium plugs in India can be made viable under existing component incentives.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>No published measurement of spark plug wear on E20 in an Indian vehicle was found, from government, manufacturers or academic work; the effect described here is reasoned from fuel chemistry, plug makers&rsquo; guidance and US tests on small engines, not observed in Indian bikes. The air-fuel arithmetic is first-order and ignores the small difference in fuel density and how each carburettor actually meters fuel. The number of carburetted two-wheelers still on the road is not published, so the cost is given per vehicle and per crore of vehicles rather than as a national total. The 25% shorter plug life, annual distance, fitting charge and scooter mileage in the cost example are this blog&rsquo;s assumptions. India&rsquo;s spark plug market size and its split between factory fitment and replacement come only from consultancy estimates. HS code 851110 also covers igniter plugs for aircraft and industrial engines, so average values per plug mix very different products; 2024 and 2025 trade data were not checked. Whether Niterra India now makes iridium plugs locally could not be confirmed.</p>
"""

sources = ("Ministry of Petroleum and Natural Gas: Rajya Sabha unstarred questions 131, 136 and 924 (20 and 27 July 2026) and 1723 (3 August 2026); Lok Sabha unstarred question 6315 (2 April 2026); PIB releases of 12 August 2025 and 4 and 30 July 2026, and the PIB E20 factsheet. "
           "Ministry of Heavy Industries: Lok Sabha unstarred question 1478 (28 July 2026) and Rajya Sabha unstarred question 2328 (7 August 2026). The Hindu, 29 July 2026, on the unpublished legacy-vehicle study. "
           "NITI Aayog and MoPNG, Roadmap for Ethanol Blending in India 2020-25 (June 2021). "
           "US Department of Energy (NREL/ORNL), Effects of Intermediate Ethanol Blends on Legacy Vehicles and Small Non-Road Engines, Report 1 &ndash; Updated (February 2009); NREL, Global Ethanol-Blended-Fuel Vehicle Compatibility Study (2021); ORNL, Technical Issues Associated with the Use of Intermediate Ethanol Blends (2008); Orbital Engine Company, E10/E20 FMEA for non-automotive engines (2002). "
           "NGK Spark Plugs, Spark Plug Basics; Denso spark plug catalogue; Bisetto, Toniolo and Menezes (Robert Bosch Ltda.), Spark Plugs for Multi-fuel Vehicles, SAE 2006-01-2630. "
           "Honda Activa owner&rsquo;s manual maintenance schedule as summarised by BikeFixUp (October 2026) and Activa SCV110 service manual; V3Cars Honda City service schedule; NGK plug prices from Indian online retailers (Riders Junction, Riders Arena, Rawtorque, 2026). "
           "Trade: UN Comtrade via World Bank WITS, India HS 851110 imports and exports by partner, 2023. Niterra India media kit; Niterra Co. press release, 19 October 2017; IMARC Group, India Automotive Spark Plug Market (2025). "
           "Air-fuel ratios, oxygen share, unit values and the cost example are this blog&rsquo;s arithmetic (builder in the repository at out/research/spark-plugs-ethanol/). Nothing here is advice on servicing a particular vehicle; follow the manufacturer&rsquo;s schedule.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/india-has-legalised-e100-for-flex-fuel.html", "India Has Legalised E100 for Flex-Fuel Cars. Its E85 Still Costs More per Kilometre Than Petrol"),
    ("https://masaladeutsch.blogspot.com/2026/09/brazil-pumps-e30-at-every-station.html", "Brazil Pumps E30 at Every Station. The Equipment Behind It Is the Part Indias E20 Story Skips"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-ethanol-surplus-buys-about-five.html", "India&rsquo;s Ethanol Surplus Buys About Five Blend Points. E30, Diesel and Jet Fuel Need Twice the Supply."),
    ("https://masaladeutsch.blogspot.com/2026/09/e20-doesnt-cut-tailpipe-co2-by-30-run.html", "E20 Doesn&rsquo;t Cut Tailpipe CO2 by 30%. Run the Chemistry and the Real Number Is Close to Zero"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-biofuel-rules-are-being-written.html", "India&rsquo;s Biofuel Rules Are Being Written in Court: E20 Survives, States Gain Alcohol Powers"),
    ("https://masaladeutsch.blogspot.com/2026/08/vehicles-out-motors-in-indias-chapter.html", "Vehicles Out, Motors In: India&rsquo;s Chapter 87 Surplus and Its Chapter 85 Problem"),
]

build("Ethanol &amp; Autos · 2 November 2026",
      "E20 and the Spark Plug: What Ethanol Does to the Cheapest Part in India&rsquo;s 20 Crore Two-Wheelers",
      "Fuel-injected engines barely notice. Carburetted bikes run about 4% leaner on E20 and hotter at the plug tip, yet no Indian test of plug wear has been published. Even if plugs wore a quarter faster, the extra cost is about &#8377;60 a year, a tenth to an eighth of the mileage loss.",
      body, sources, related, OUT)
print("lean", round(LEAN_PCT, 2), "afr", round(AFR10, 2), round(AFR20, 2), "O", round(O10, 1), round(O20, 1),
      "extra", round(extra_plugs, 3), round(extra_plug_cost), "fuel", round(fuel_bill), [round(x) for x in mileage_cost],
      "china", round(CHINA_SHARE_PCS, 1), round(CHINA_SHARE_VAL, 1), "japan", round(JAPAN_SHARE_PCS, 1), round(JAPAN_SHARE_VAL, 1),
      "units", [(n, round(u, 2)) for n, v, q, u in IMP_U], round(IMP_TOTAL_U, 3), round(EXP_TOTAL_U, 3))
