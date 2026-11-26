"""Sodium-ion batteries: weight, energy delivered per charge, per kg and over life, and cost per kWh delivered.
Build from the repo root:  python3 out/research/sodium-ion-battery-2026/build.py   (writes out/post-sodium-ion-battery-weight-energy-delivered.html)
Arithmetic lives in calc.py beside this file and is asserted there; this file re-asserts every figure it prints. Analysed 26 November 2026.
Opened and read for this piece: Wood Mackenzie press release, The Driven (13 Nov 2026), Electrek, Best Magazine, pv magazine (2023, 2024, 2025, 2026), Business Standard (Jan 2026),
an arXiv preprint (secondary). Blocked by a bot challenge or by the network allowlist and so NOT opened (search excerpts only): IEA, RSC Publishing, Nature, CEEW, YourStory, energy-storage.news, Gizmochina."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402
import calc as c  # noqa: E402  (importing runs the asserts)

OUT = ROOT / "out/post-sodium-ion-battery-weight-energy-delivered.html"
B = "https://blog.vertistratsolution.com"
TITLE = "Sodium-ion batteries: 17% more mass per kWh than LFP at claimed densities"
assert 55 <= len(TITLE) <= 90, len(TITLE)
S = "40 kWh small car"

# ---- derived figures used in prose (each asserted again here so a change in calc.py cannot silently change the text)
PCT_MORE = round(100 * (205 / 175 - 1), 1)
assert PCT_MORE == 17.1
M = {k: c.MASS[(S, k, "mid")] for k in c.CELL}
EXTRA_CAR = round(M["Na_Naxtra"] - M["LFP_hi"], 1)
assert EXTRA_CAR == 46.5 and round(M["Na_Naxtra"], 1) == 317.5 and round(M["LFP_hi"], 1) == 271.0
BE6 = round(c.BE[(6000, 175)])
assert BE6 == 7029
OTHER0 = round(c.IMPL[0], 1)
assert OTHER0 == 89.9 and round(100 * c.IMPL[0] / c.PRICE["LFP"]) == 45
COST_GAP = round(100 * (c.COST_BE - 1), 1)
assert COST_GAP == 14.5

top = top_line([
    (f"{PCT_MORE}%", f" more mass for the same energy: a 175 Wh/kg sodium-ion cell (CATL&rsquo;s claim) against a 205 Wh/kg LFP cell, which is {EXTRA_CAR} kg more in a 40 kWh car pack under an assumed 80% cell-to-pack ratio and about {c.RANGE_LOSS_PCT:.1f}% less range under stated vehicle assumptions."),
    (f"{BE6:,}", f" cycles is what the 175 Wh/kg sodium-ion cell needs to deliver as much lifetime energy per kg as LFP lasting 6,000 cycles; the only cycle figures for sodium-ion found here are company claims of 4,000 to 10,000, none verified in the field."),
    (f"${OTHER0}", f" a kWh is the least that LFP&rsquo;s non-purchase costs would need to be for Wood Mackenzie&rsquo;s 21% lower sodium-ion ownership cost to hold at its $229 against $200 upfront prices, with sodium-ion&rsquo;s own costs at zero; the release gives no cost inputs to check it."),
])

# ---------------------------------------------------------------- section 1: per kg and weight penalty
rows1 = [("Lithium NMC, 280 Wh/kg cell (CATL Qilin 3, claim)", M["NMC"]),
         ("LFP, 205 Wh/kg cell", M["LFP_hi"]),
         ("Sodium-ion, 175 Wh/kg cell (CATL Naxtra, claim)", M["Na_Naxtra"]),
         ("Sodium-ion, 170 Wh/kg cell (KPIT top variant, claim)", M["Na_KPIT_top"]),
         ("LFP, 160 Wh/kg cell (BYD Blade class)", M["LFP_lo"]),
         ("Sodium-ion, 110 Wh/kg cell (KPIT current cell, claim)", M["Na_KPIT_now"])]
rows1 = [(a, round(b, 1)) for a, b in rows1]
assert [r[1] for r in rows1] == [198.4, 271.0, 317.5, 326.8, 347.2, 505.1]
chart1 = bars("A 40 kWh sodium-ion pack at 175 Wh/kg cells weighs 317.5 kg; LFP at 205 weighs 271 kg", rows1,
              accent="Sodium-ion, 175 Wh/kg cell (CATL Naxtra, claim)", unit=" kg", vmax=520,
              sub="Pack mass for 40 kWh of usable energy, kg. Assumptions: pack Wh/kg is 80% of the cell figure, 90% of the pack is usable. Cell figures are company claims or press reports, not tests.",
              source="Cell densities: Electrek and Best Magazine (Naxtra), pv magazine (KPIT), Best Magazine (Qilin), Electrek (Blade); the LFP 205 figure was seen only in a search excerpt of an IEA page. Mass computed by this blog.")
sens = []
for k, lab in [("NMC", "NMC 280"), ("LFP_hi", "LFP 205"), ("Na_Naxtra", "Sodium-ion 175"), ("Na_KPIT_top", "Sodium-ion 170"), ("LFP_lo", "LFP 160"), ("Na_KPIT_now", "Sodium-ion 110")]:
    sens.append([lab, c.CELL[k]] + [f"{c.pack_wh_kg(c.CELL[k], f):.0f}" for f in c.PACK_FRAC.values()]
                + [f"{c.MASS[('3 kWh e-scooter', k, 'mid')]:.1f}", f"{c.MASS[(S, k, 'mid')]:.1f}", f"{c.MASS[('2 MWh stationary container', k, 'mid')] / 1000:.2f}"]
                + [f"{c.MASS[(S, k, 'low')]:.0f}&ndash;{c.MASS[(S, k, 'high')]:.0f}"])
assert sens[2][5:8] == ["23.8", "317.5", "15.87"] and sens[1][5:8] == ["20.3", "271.0", "13.55"]
tbl1 = numbers(["Chemistry (cell Wh/kg)", "Cell Wh/kg", "Pack Wh/kg at 70%", "at 80%", "at 85%", "3 kWh scooter (kg)", "40 kWh car (kg)", "2 MWh container (t)", "Car pack at 85% to 70% (kg)"], sens,
               "Show cell-to-pack sensitivity and pack masses (assumed fractions)") + numbers(
    ["Input", "Value", "Status and source"],
    [["Naxtra cell", "175 Wh/kg (up to)", "Company claim; Electrek 23 Jan and 5 Feb 2026, Best Magazine 3 Feb 2026 (unit printed as Wh/kg on those pages)"],
     ["KPIT cells", "100 to 170 Wh/kg; 110 Wh/kg for the then-current cell; 135 and 170 variants", "Company claim; pv magazine, 19 Dec 2023 (secondary report of the chairman&rsquo;s statements)"],
     ["Hina sodium-ion packs", "&lsquo;around 165 Wh/kg&rsquo;", "Electrek, 22 Jun 2026, secondary; the cell and pack basis were not stated"],
     ["Commercial sodium-ion cells", "140 to 180 Wh/kg against 200 to 280 for premium lithium-ion", "Electrek, 20 Jul 2026 (secondary summary)"],
     ["BYD Blade LFP", "about 150 Wh/kg now; 160 and 210 for new versions", "Electrek, 9 Dec 2024, from an unnamed source (secondary); an arXiv preprint labels 160 as a pack figure; cell or pack level is not clear"],
     ["Qilin 3 NMC", "280 Wh/kg cell; pack 625 kg, 255 kg lighter than a comparable LFP pack", "Company claim; Best Magazine, 2026. The pack&rsquo;s kWh was not printed, so no pack Wh/kg can be derived"],
     ["Cell-to-pack fraction", "70%, 80%, 85%", "ASSUMPTION of this blog for every chemistry; no opened source measures it. A life-cycle study excerpt (not opened) assumes 80% for sodium-ion"],
     ["Vehicle", "1,000 kg without battery; 0.1125 kWh/km (the 45 kWh Naxtra pack&rsquo;s claimed 400 km on China&rsquo;s CLTC cycle); 40% of consumption scales with mass", "ASSUMPTIONS; anchor from Electrek, 5 Feb 2026"],
     ["Rider", "75 kg", "ASSUMPTION"]],
    "Show the inputs and their status")
means1 = (f"At equal pack fraction the mass ratio is the density ratio, so claimed sodium-ion is {PCT_MORE}% heavier than 205 Wh/kg LFP: {EXTRA_CAR} kg more in a 40 kWh car pack (about {c.RANGE_LOSS_PCT:.1f}% of range), "
          f"{c.EXTRA['3 kWh e-scooter']:.1f} kg in a 3 kWh scooter pack and {c.EXTRA['2 MWh stationary container'] / 1000:.2f} tonnes in a 2 MWh container, and none of it against LFP near 160 Wh/kg.")
todo1 = "Buyers should ask suppliers for pack mass and rated energy in kilograms and kilowatt-hours on a datasheet, because no opened source gives a measured pack figure for any of these chemistries."
s1 = insight("Weight: sodium-ion packs carry 17.1% more mass per kWh than 205 Wh/kg LFP, by claim", chart1 + tbl1, means1, todo1, "weight")

# ---------------------------------------------------------------- section 2: cycle life, claim against evidence
rows2 = [("LFP, DNV scorecard 2021, extrapolated by this blog (test)", (c.CYC["LFP_dnv_low"], c.CYC["LFP_dnv_high"]), "", "2,700&ndash;8,960"),
         ("LFP modules, Sonnen lab test (83% left at 10,000)", c.CYC["LFP_sonnen"], "", "10,000"),
         ("LFP, BYD Blade (&gt;3,000, via a preprint)", c.CYC["LFP_low"], "", "&gt;3,000"),
         ("Sodium-ion, KPIT (claim; 4,000 to 5,000 tested)", (c.CYC["KPIT_low"], c.CYC["KPIT_high"]), "", "4,000&ndash;6,000"),
         ("Sodium-ion, Naxtra (claim; via a preprint)", c.CYC["Naxtra"], "", "&gt;10,000")]
chart2 = bars("Sodium-ion cycle life: 4,000 to 10,000 cycles claimed; none verified in the field", rows2,
              accent=["Sodium-ion, KPIT (claim; 4,000 to 5,000 tested)", "Sodium-ion, Naxtra (claim; via a preprint)"], unit=" cycles", vmax=10000, from_zero=True,
              sub="Cycles to 80% of original capacity as reported; a range is drawn solid to the low end and lighter to the high end. LFP rows are lab tests or warranties, sodium-ion rows are company statements.",
              source="pv magazine (Sonnen, 15 Jul 2021; KPIT, 19 Dec 2023 and 22 Mar 2024), arXiv 2509.23837 (preprint, not peer-reviewed; it tells readers to verify Naxtra&rsquo;s 10,000 cycles), pv magazine opinion (1 Oct 2026).")
# DNV Battery Scorecard: cycles to lose 1% of capacity, 135 to 448 for LFP; linear extrapolation to 20% loss
assert c.CYC["LFP_dnv_low"] == 20 * 135 and c.CYC["LFP_dnv_high"] == 20 * 448
tbl2 = numbers(["Item", "Figure", "Status and source"],
               [["LFP cycles to lose 1% of capacity (DNV Battery Scorecard)", "135 to 448; nickel-manganese-cobalt 180 to 849", "Reported by pv magazine, 15 Jul 2021; times 20 gives 2,700 to 8,960 cycles to 80%, a straight-line extrapolation made here"],
                ["Sonnen LFP modules", "83% of capacity after 10,000 cycles; guarantee 80% at 10,000; one cell at 65% after 28,000 full cycles", "Manufacturer test, pv magazine, 15 Jul 2021; a residential product, 1C, 100% depth of discharge"],
                ["LFP field record", "ten-plus years of operation", "pv magazine opinion by an industry executive, 1 Oct 2026"],
                ["Sodium-ion field record", "none at scale; first peer-reviewed ageing studies on commercial cells in early 2026", "Same opinion piece (the underlying studies were not opened)"],
                ["Sodium-ion ageing study excerpt", "up to 5,000 equivalent full cycles tested; large cell-to-cell variability; sodium plating on some cells", "Seen only in a search excerpt (RSC Publishing page blocked); not used in any figure here"],
                ["KPIT", "80% retention at 6,000 cycles; 4,000 to 5,000 cycles tested at 3C; the 170 Wh/kg variant had not run 3,000 cycles", "Company statements, pv magazine 19 Dec 2023 and 22 Mar 2024"],
                ["Earlier general statement", "sodium-ion life of 100 to 1,000 cycles", "pv magazine background text, 22 Mar 2024; older than the Naxtra claims"],
                ["Wood Mackenzie", "&lsquo;SIB wins on supply chain security, cycle life and wide thermal threshold&rsquo;", "A quoted view in a press release; no cycle figure given"]],
               "Show the cycle-life evidence")
means2 = "Every sodium-ion cycle figure found is a manufacturer or developer statement while the LFP figures are lab tests, warranties and a decade of operation, so the two ranges overlap on paper but carry different weight as evidence."
todo2 = "Lenders and buyers should treat sodium-ion cycle life as unproven until independent pack-level tests and field degradation curves are published, as an opinion in pv magazine on 1 October 2026 also concluded."
s2 = insight("Cycle life: sodium-ion figures are claims, LFP figures are tests and field history", chart2 + tbl2, means2, todo2, "cycles")

# ---------------------------------------------------------------- section 3: lifetime energy per kg
rows3 = [("LFP 205, 3,000 cycles", c.LIFE[("LFP 205", 3000)]), ("Sodium-ion 175, 3,000 cycles", c.LIFE[("Na 175", 3000)]),
         ("LFP 205, 6,000 cycles", c.LIFE[("LFP 205", 6000)]), ("Sodium-ion 175, 6,000 cycles", c.LIFE[("Na 175", 6000)]),
         (f"Sodium-ion 175, {BE6:,} cycles (break-even)", c.life_kwh_per_kg(175, c.PACK_FRAC["mid"], c.BE[(6000, 175)])),
         ("Sodium-ion 175, 10,000 cycles (claim)", c.LIFE[("Na 175", 10000)])]
rows3 = [(a, round(b)) for a, b in rows3]
assert [r[1] for r in rows3] == [399, 340, 797, 680, 797, 1134]
chart3 = bars(f"Lifetime energy per kg of pack: sodium-ion matches 6,000-cycle LFP at {BE6:,} cycles", rows3,
              accent=f"Sodium-ion 175, {BE6:,} cycles (break-even)", unit=" kWh/kg", vmax=1400,
              sub="Energy delivered over life per kilogram of pack, kWh. Pack Wh/kg (80% of cell) x 90% depth of discharge x cycles to 80% capacity x 0.9 average capacity, before round-trip losses.",
              source="Computed by this blog from the cell densities and cycle figures above; every factor other than the densities and cycles is an assumption.")
sens3 = []
for n in (2000, 3000, 6000, 10000):
    sens3.append([f"{n:,}"] + [f"{c.breakeven_cycles(n, 205, d):,.0f}" for d in (110, 140, 160, 175, 190)])
assert sens3[2] == ["6,000", "11,182", "8,786", "7,688", "7,029", "6,474"]
lifetab = [[lab, f"{c.LIFE[(lab, 3000)]:.0f}", f"{c.LIFE[(lab, 6000)]:.0f}", f"{c.LIFE[(lab, 10000)]:.0f}"] for lab in ("LFP 205", "LFP 160", "Na 175", "Na 110")]
assert lifetab[2] == ["Na 175", "340", "680", "1134"]
tbl3 = numbers(["LFP cycles to 80%", "Sodium-ion 110 Wh/kg needs", "140", "160", "175", "190"], sens3,
               "Show break-even cycles for sodium-ion against 205 Wh/kg LFP") + numbers(
    ["Cell (Wh/kg)", "3,000 cycles (kWh/kg)", "6,000 cycles", "10,000 cycles"], lifetab, "Show lifetime kWh per kg of pack at three cycle counts")
tbl3 += numbers(["Per-charge, per-kg", "Value"],
                [["Usable energy per kg, 175 Wh/kg cell", f"{c.pack_wh_kg(175, .8) * c.DOD:.0f} Wh/kg (pack 140 Wh/kg x 0.9)"],
                 ["Usable energy per kg, 205 Wh/kg LFP", f"{c.pack_wh_kg(205, .8) * c.DOD:.0f} Wh/kg (pack 164 Wh/kg x 0.9)"],
                 ["Round-trip efficiency used for storage", "0.90 for both (ASSUMPTION); pv magazine opinion cites 90% to 95% for LFP and says sodium-ion has no proven project figure"]],
                "Show energy per charge")
assert round(c.pack_wh_kg(175, .8) * c.DOD) == 126 and round(c.pack_wh_kg(205, .8) * c.DOD) == 148
means3 = f"A lower-density chemistry can deliver more lifetime energy per kilogram only if it lasts longer, and sodium-ion at 175 Wh/kg needs {BE6:,} cycles to match LFP at 6,000 (17.1% more), so the claimed 10,000 cycles would beat it by 42% while a 110 Wh/kg cell would need {round(c.BE[(6000, 110)]):,}."
assert round(100 * (c.LIFE[("Na 175", 10000)] / c.LIFE[("LFP 205", 6000)] - 1)) == 42
todo3 = "Procurement documents should state the cycle count, depth of discharge, temperature and end-of-life threshold behind every cycle claim, so that the break-even can be tested against a measured figure."
s3 = insight(f"Energy over life: sodium-ion at 175 Wh/kg needs {BE6:,} cycles to match LFP at 6,000", chart3 + tbl3, means3, todo3, "lifetime")

# ---------------------------------------------------------------- section 4: cost per kWh delivered and the 21% claim
rows4 = [(f"Sodium-ion other costs of ${y}/kWh", round(v, 1)) for y, v in c.IMPL.items()]
assert [r[1] for r in rows4] == [89.9, 121.5, 153.2, 216.5]
chart4 = bars(f"Wood Mackenzie&rsquo;s 21% claim needs LFP to carry at least ${OTHER0} a kWh in other costs", rows4,
              accent="Sodium-ion other costs of $0/kWh", unit="$/kWh", vmax=230, ref=(200, "LFP upfront price, $200 a kWh"),
              sub="Back-solved: the 20-year non-purchase cost (operation plus augmentation) that LFP must have for sodium-ion at $229 upfront to be 21% cheaper to own, for four assumed sodium-ion non-purchase costs.",
              source="Wood Mackenzie press release (woodmac.com; also reported by The Driven, 13 Nov 2026) for $229, $200, 21% and 20 years; the back-solve is this blog&rsquo;s arithmetic.")
cpd = [[f"{n:,}", f"{100 * c.CPD[('LFP', n)]:.1f}", f"{100 * c.CPD[('Na', n)]:.1f}", f"{c.cost_per_kwh_delivered(c.PRICE['Na'], n) / c.cost_per_kwh_delivered(c.PRICE['LFP'], n):.3f}"] for n in (3000, 6000, 10000)]
assert cpd == [["3,000", "9.1", "10.5", "1.145"], ["6,000", "4.6", "5.2", "1.145"], ["10,000", "2.7", "3.1", "1.145"]]
tbl4 = numbers(["Cycles to 80%", "LFP at $200 (US cents per kWh delivered)", "Sodium-ion at $229 (cents)", "Ratio"], cpd,
               "Show upfront cost per kWh delivered (no augmentation, no operating cost)") + numbers(
    ["Item", "Value", "Status"],
    [["Upfront price", "$229 a kWh sodium-ion, $200 a kWh LFP, global averages", "Wood Mackenzie; the release does not say whether this is cell, module or system, and The Driven calls them systems"],
     ["Total cost of ownership", "21% lower for sodium-ion over 20 years, from no augmentation events and lower operating cost", "Wood Mackenzie; operating cost, augmentation cost and discount rate are not published, so it cannot be reproduced from its own inputs"],
     ["Cost per kWh delivered", "price / (90% depth x cycles x 0.9 fade x 0.90 round trip)", "This blog; upfront price only, one purchase, no augmentation"],
     ["Break-even upfront", f"sodium-ion needs {COST_GAP}% more cycles than LFP to equal its upfront cost per kWh delivered (229 / 200)", "Computed here"],
     ["20 years of daily cycling", "7,300 cycles, above the 3,000 low end and below the 10,000 high end of the LFP figures", "Computed here; an LFP system at the low end would need augmentation, which is the cost Wood Mackenzie says sodium-ion avoids"],
     ["Other price points", "cell prices of $52 (LFP) and $59 (sodium-ion) a kWh for 2025, parity around 2035", "Wood Mackenzie blog; older and on a different basis, not combined with the figures above"],
     ["Policy", "China taxes LFP at 2% from 1 Sep 2026 (4% from Sep 2027), sodium-ion exempt to end-2028", "Wood Mackenzie release, via The Driven"]],
    "Show the inputs and what is not published")
means4 = f"At the same cycles to 80% sodium-ion costs {COST_GAP}% more upfront per kWh delivered, and the 21% lower ownership cost means LFP&rsquo;s other costs must be at least ${OTHER0} a kWh (45% of its purchase price) even if sodium-ion&rsquo;s were zero, a gap that rests on augmentation and operating inputs the release does not publish."
todo4 = "Wood Mackenzie should publish the operating cost, augmentation schedule and discount rate behind the 21% figure, so that buyers can rerun it with their own cycling and prices."
s4 = insight(f"Cost per kWh delivered: sodium-ion is {COST_GAP}% dearer upfront; the 21% claim has no inputs", chart4 + tbl4, means4, todo4, "cost")

# ---------------------------------------------------------------- where each fits, India
fits = numbers(["Use", "What the sources support", "Status"],
               [["Stationary, 2 to 4 hours (India&rsquo;s 92 GWh programme)", "LFP is the bankable choice for projects built today; sodium-ion economics are said to hold across 2 to 4 hours; cell cost parity with LFP expected among leaders by end-2026, system parity after 2030", "Wood Mackenzie release (secondary analyst view); no India sodium-ion project data found"],
                ["Two- and three-wheelers", "Weight matters least on heavier motorcycles and delivery scooters; E-Went, a Kolkata scooter maker, plans sodium-ion trials from December", "Electrek 20 Jul 2026 (opinion); Best Magazine on E-Went (excerpt only: pack size not found)"],
                ["Light commercial vehicles and buses", "CATL&rsquo;s 45 kWh Tectrans II pack for vans and light trucks: charges at &minus;30&deg;C and keeps 90% of usable capacity at &minus;40&deg;C. Pack mass not published. No bus data found", "Company claim, Electrek and Best Magazine, Jan to Feb 2026"],
                ["Passenger cars", "Changan Nevo A06: 45 kWh Naxtra pack, 400 km CLTC claimed (8.89 km/kWh) against 63.18 kWh lithium-ion and 630 km (9.97 km/kWh), 10.9% fewer km per kWh", "Company claims (CLTC cycle), Electrek 5 Feb 2026; CATL expects only GWh-level output by end-2026"],
                ["Cold weather", "90% of usable capacity at &minus;40&deg;C against about 80% for lithium batteries on average", "CATL claim as reported by Electrek, 30 Jan 2026"],
                ["Hard carbon anode", "initial coulombic efficiency of 75% to 85%; no proven round-trip figure from projects", "Opinion by an industry executive, pv magazine, 1 Oct 2026"],
                ["India: who makes what", "Reliance owns Faradion (UK); Business Standard (12 Jan 2026) says Reliance is building a 30 GWh battery plant at Jamnagar and is &lsquo;advancing sodium-ion&rsquo;; Reliance&rsquo;s 2023 target was megawatt-scale sodium-ion cell output by 2025, and no production report was found. KPIT unveiled cells in 2023 and sought manufacturing partners. Wood Mackenzie puts India at early commercial validation, with an underdeveloped supply chain and a $1.25 billion incentive scheme",
                 "Announced, not commercial: no named Indian production volume was found for any of them"],
                ["India: smaller makers", "Naxion Energy (Coimbatore pack plant, 1.5 GWh a year claimed), Rechargion (Pune, own hard carbon), Indi Energy (biomass hard carbon) were reported by YourStory in August 2026", "Seen only in search excerpts (YourStory blocked); company claims, unverified"],
                ["Global supply deals", "more than 70 GWh of agreements; BYD 30 GWh planned; CATL at least 1 GWh of shipments by end-2026", "Wood Mackenzie, via The Driven, 13 Nov 2026"]],
               "Show where each chemistry fits and what is commercial in India")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Bureau of Indian Standards and the Automotive Research Association of India:</b> publish measured pack mass, rated energy, cycles to 80% and the test conditions for every battery type-approved in India, so that pack Wh/kg is a certified number and not a derived one.</li>
<li><b>Ministry of Heavy Industries:</b> name the chemistry and the quarterly commissioned GWh for each beneficiary of the cell manufacturing scheme, so that sodium-ion output in India can be told apart from announcements.</li>
<li><b>Ministry of Power and the Solar Energy Corporation of India:</b> require the projects in the 92 GWh programme to report annual capacity and round-trip efficiency, by chemistry, for the life of the project.</li>
<li><b>A national test laboratory named by the Ministry of Heavy Industries:</b> test commercial sodium-ion and LFP cells to the same protocol and publish pack-level energy density and cycles to 80%.</li>
<li><b>Wood Mackenzie:</b> publish the operating cost, augmentation and discount-rate inputs behind its 21% total-cost figure.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Pack Wh/kg is the cell Wh/kg times a cell-to-pack fraction of 70%, 80% or 85%, the same for every chemistry. This is an assumption: no source opened for this piece measured it, so every pack figure here is derived and is not a finding.</li>
<li>Pack mass for a stated usable energy is the energy divided by pack Wh/kg and by a 90% usable depth of discharge. At equal fractions the mass ratio between two chemistries is the inverse of their cell density ratio.</li>
<li>Range effect: a 1,000 kg vehicle body, consumption of 0.1125 kWh/km at the LFP 205 pack&rsquo;s mass, with 40% of consumption scaling with total mass. The scooter payload effect is the extra pack mass over an assumed 75 kg rider.</li>
<li>Lifetime energy per kg is pack Wh/kg x 0.9 depth of discharge x cycles to 80% x 0.9 (capacity fading in a straight line from 100% to 80%) and, for storage, x 0.90 round trip. Break-even cycles are the reference cycles times the ratio of cell densities.</li>
<li>Cost per kWh delivered divides the upfront price by lifetime throughput per kWh of capacity. It ignores operating cost, augmentation, replacement and discounting, which is why the 21% total-cost claim is only back-solved.</li>
<li>The LFP cycle range of 2,700 to 8,960 multiplies the DNV Battery Scorecard&rsquo;s 135 to 448 cycles per 1% of capacity by 20, assuming a straight-line fade. The scorecard figures were read in pv magazine&rsquo;s 2021 report of them.</li>
<li>Where the sources disagree (Blade at 150 or 160 Wh/kg, cell or pack; KPIT at 110 or 160), both figures are shown and neither is chosen as fact.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>A measured pack-level Wh/kg for any chemistry. CATL gave a Qilin pack mass (625 kg) without the pack&rsquo;s kWh; the 45 kWh Naxtra pack&rsquo;s mass was not published; Electrek&rsquo;s &lsquo;around 165 Wh/kg&rsquo; for Hina packs does not say how it was measured. The cell-to-pack fractions are assumptions.</li>
<li>Sources that could not be opened: the IEA (Global EV Outlook 2026, the sodium-ion commentary), RSC Publishing (a benchmarking paper, a 2026 ageing study, a life-cycle assessment), Nature, CEEW, YourStory, Energy-Storage.news and Gizmochina returned a bot challenge or were outside the allowed network, and were not bypassed. Anything from them appears only as a labelled excerpt: LFP at up to 205 Wh/kg, the excerpt of the RSC benchmarking paper (sodium cells 10% to 15% below LFP), the 80% pack assumption in a life-cycle study, the Naxion and Rechargion claims, and the CEEW report on sodium-ion in India. None of it feeds a computed figure other than the LFP 205 Wh/kg cell density, which is why the LFP 160 Wh/kg case is shown beside it.</li>
<li>Whether Electrek and Gizmochina printed Naxtra&rsquo;s density as kWh/kg: the Electrek and Best Magazine pages read Wh/kg, and the Gizmochina page could not be opened.</li>
<li>Energy per litre for sodium-ion or LFP. The only volumetric figures found are for NMC (a 760 Wh/L claim for CATL&rsquo;s Qilin Condensed cell) and a claimed 112-litre reduction in the Qilin 3 pack, so a stationary footprint comparison is not made.</li>
<li>Independent cycle-life data for commercial sodium-ion cells beyond a search-excerpt mention of a 2026 ageing study. Naxtra&rsquo;s 10,000 cycles was found only in an arXiv preprint that repeats it and asks readers to verify it; no CATL document was opened.</li>
<li>What Wood Mackenzie&rsquo;s $229 and $200 cover (cell, module or system), and its operating and augmentation inputs. The Moonwatt claim of cost parity in two to three years was not opened (Energy-Storage.news blocked) and is not used.</li>
<li>Sodium-ion shipping at low state of charge and the voltage differences from lithium-ion cells: no opened source covers them, so they are not discussed.</li>
<li>Named Indian production volumes. Reliance&rsquo;s sodium-ion status rests on one line in a Business Standard report; Reliance&rsquo;s 2025 megawatt-scale target was not confirmed as met. A Renewable Energy Secretary&rsquo;s expectation of commercial pilots in two to three years and Jitendra EV&rsquo;s plan for sodium-ion e-2Ws in two years were not found in any source opened.</li>
<li>The pv magazine piece of 1 October 2026 is an opinion by the head of energy storage at a developer, not a measurement; the same goes for the Electrek e-bike article.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + '<section class="xv-sec"><h2 class="gb-h2" id="fit">Where each fits, and what is commercial in India</h2>\n' + fits + "</section>\n" + fixes + method + gaps

SOURCES = (
    'Primary or near-primary (opened): <a href="https://www.woodmac.com/press-releases/sodium-ion-batteries-establish-a-foothold-as-a-lithium-alternative/">Wood Mackenzie press release on sodium-ion</a> (an analyst firm&rsquo;s estimates: $229 and $200 a kWh, 21% lower TCO, 70 GWh of agreements); '
    '<a href="https://www.woodmac.com/blogs/energy-pulse/sodium-ion-batteries-enter-energy-storage-market/">Wood Mackenzie blog</a> (2025 cell prices). '
    '</p><p class="gb-note" style="margin:.6rem 0 0">Secondary (opened), news: <a href="https://thedriven.io/2026/11/13/sodium-ion-batteries-gain-ground-with-more-than-70-gwh-in-supply-deals/">The Driven, 13 November 2026</a>; '
    '<a href="https://electrek.co/2026/01/23/ev-battery-leader-plans-first-sodium-ion-batteries-passenger-cars/">Electrek, 23 January 2026</a> and <a href="https://electrek.co/2026/01/30/catl-byd-betting-on-new-type-of-ev-battery/">30 January 2026</a> (CATL claims); '
    '<a href="https://electrek.co/2026/02/05/first-sodium-ion-battery-ev-debuts-game-changer/">Electrek, 5 February 2026</a> (Changan Nevo A06); <a href="https://electrek.co/2026/06/22/chinese-sodium-ion-battery-matches-tesla-build-quality/">Electrek, 22 June 2026</a> (RWTH Aachen teardown, Hina packs); '
    '<a href="https://electrek.co/2026/07/20/will-we-soon-see-sodium-ion-batteries-on-electric-bikes/">Electrek, 20 July 2026</a> (opinion); <a href="https://electrek.co/2024/12/09/byd-to-cut-ev-battery-costs-by-15-new-blade-battery/">Electrek, 9 December 2024</a> (BYD Blade); '
    '<a href="https://www.bestmag.co.uk/catl-sodium-ion-batteries-enter-ev-testing/">Best Magazine, 3 February 2026</a> and <a href="https://www.bestmag.co.uk/catl-4-minute-fast-charging/">CATL Qilin 3 report</a>; '
    '</p><p class="gb-note" style="margin:.6rem 0 0">Secondary (opened), pv magazine and others: <a href="https://www.pv-magazine.com/2023/12/19/kpit-unveils-sodium-ion-battery-with-energy-density-of-up-to-170-wh-kg/">pv magazine, 19 December 2023</a> (KPIT, company statements); '
    '<a href="https://www.pv-magazine.com/2024/03/22/sodium-ion-batteries-a-viable-alternative-to-lithium/">pv magazine, 22 March 2024</a> (Faradion, Reliance); '
    '<a href="https://www.pv-magazine.com/2021/07/15/sonnen-battery-still-running-after-28000-full-charge-cycles/">pv magazine, 15 July 2021</a> (Sonnen test, DNV Battery Scorecard); '
    '<a href="https://www.pv-magazine.com/2026/10/01/sodium-ion-batteries-the-next-frontier-or-the-next-risk/">pv magazine, 1 October 2026</a> (opinion); '
    '<a href="https://www.pv-magazine.com/2026/08/10/advanced-sodium-ion-battery-prototypes-now-approaching-200-wh-kg/">pv magazine, 10 August 2026</a> (review, density 100 to 160 Wh/kg); '
    '<a href="https://www.business-standard.com/companies/news/reliance-says-battery-manufacturing-plans-on-track-2026-target-unchanged-126011201033_1.html">Business Standard, 12 January 2026</a> (Reliance); '
    '<a href="https://arxiv.org/pdf/2509.23837">arXiv 2509.23837</a> (preprint, not peer-reviewed, a secondary source for the 10,000-cycle claim and the Blade 160 Wh/kg label). '
    '</p><p class="gb-note" style="margin:.6rem 0 0">Not opened, excerpts only: IEA, RSC Publishing, Nature, CEEW, YourStory, Energy-Storage.news (see the &lsquo;could not establish&rsquo; box). Every cell density and cycle figure for sodium-ion is a company claim. All masses, break-evens and costs per kWh delivered were computed by this blog, with assumptions stated. Analysed 26 November 2026.')

RELATED = [
    (f"{B}/2026/09/indias-battery-storage-boom-is.html", "Grid battery storage in India: about 9.3 GWh by mid-2026, up from 1.08 GWh"),
    (f"{B}/2026/11/14500-crore-for-92-gwh-indias-storage.html", "India's storage subsidy: &#8377;14,500 crore for 92 GWh, down to &#8377;1,576 a kWh"),
    (f"{B}/2026/09/indias-ev-localisation-deadline-just.html", "India's EV localisation deadline: split in two over the one input China controls"),
    (f"{B}/2026/08/the-battery-passport-was-built-for.html", "Battery passports: built for recycling, with a use in preventing battery fires"),
    (f"{B}/2026/10/how-to-use-ev-battery-management-sim.html", "How to use ev-battery-management-sim: simulate EV battery packs and test the model on battery datasets"),
    (f"{B}/2026/11/five-open-source-control-simulators-for.html", "Open-source control simulators: 5 for EV batteries, electrolysers and prosthetic hands"),
    (f"{B}/2026/08/indias-ev-market-single-digit.html", "India's EV sales: 12% of vehicles in April&ndash;September, cars in single digits"),
]

build("Energy &middot; Batteries", TITLE,
      "A 175 Wh/kg sodium-ion cell is claimed against up to 205 Wh/kg for LFP; four charts set out the weight penalty, the unproven cycle claims, the lifetime energy per kilogram and what the 21% cost claim requires.",
      body, SOURCES, RELATED, str(OUT))
assert "masaladeutsch" not in OUT.read_text().lower()
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
