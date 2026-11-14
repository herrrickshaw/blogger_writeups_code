"""Visual-first edition of the chloride post (docs/VISUAL_STORY_STYLE.md).
Build from the repo root:  python3 out/research/chloride-ethanol/build_visual.py
Same facts and sources as build_post.py, which stays as the record of the first edition; every number
here is imported from it or computed from those numbers, so the two cannot drift apart."""
import pathlib
import runpy
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from viz_frame import split  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

# reuse the first edition's data (running it also rewrites out/post-chloride-in-fuel-ethanol-india.html, unchanged)
D = runpy.run_path(str(pathlib.Path(__file__).with_name("build_post.py")))
LIMITS, EMAIL, R = D["LIMITS"], D["EMAIL"], D["R"]
TANK_L, TANK_KG = D["TANK_L"], D["TANK_KG"]
ACC, PERM = D["IS10500_ACC"], D["IS10500_PERM"]
OUT = ROOT / "out/update-2026-11-15-chloride-in-fuel-ethanol-is-15464-sets.html"

assert R[500][0] > TANK_L > R[100][0]          # the chart's claim: 500 mg/kg needs more water than the tank holds
assert round(EMAIL[0][2] / 3) == 190            # "up to 190 times the 3 ppm limit"

top = top_line([
    ("No limit", " on chloride in 1G ethanol, made from molasses and grain, which is almost all the ethanol India blends. "
                 "IS 15464:2022 caps only 2G ethanol, at 3 mg/kg."),
    (f"{EMAIL[0][2]} ppm vs under 3", " is the gap in the 2026 E20 dispute: the highest reading in automakers&rsquo; internal emails "
                                      "(Rajasthan) against oil-company tests of distillery, terminal and pump samples."),
    (f"{R[1][0]:.0f} litres", f" of tap water ({ACC} mg/L chloride) left in a {TANK_L:,}-litre E20 tank can breach a 1 mg/kg limit. "
                              f"A 500 mg/kg reading would need {R[500][0]:,.0f} litres, more than the tank holds."),
])

LBL = {"Brazil": "Brazil <small>ANP Resolution 907/2022</small>", "Europe": "Europe <small>EN 15376:2014</small>",
       "2G": "India, 2G ethanol <small>IS 15464:2022</small>", "United States": "United States <small>ASTM D4806, RFA 2018 summary</small>",
       "1G": "India, 1G ethanol <small>IS 15464:2022</small>"}
key = lambda lab: next(k for k in LBL if k in lab)
s1 = insight(
    "India&rsquo;s chloride limit: 3 mg/kg for 2G ethanol, none for the 1G ethanol it blends",
    bars("Brazil and Europe cap all blending ethanol at 1 to 1.5 mg/kg; India caps only 2G",
         [(LBL[key(lab)], v) for lab, v in LIMITS], accent=LBL["1G"], unit=" mg/kg",
         sub="Inorganic chloride allowed in ethanol for blending, mg/kg. Lower is stricter; dashed means no limit.",
         source="ANP 907/2022; EN 15376:2014; IS 15464:2022, Table 1; Renewable Fuels Association summary of ASTM D4806 (2018).")
    + numbers(["IS 15464:2022, Table 1", "1G ethanol", "2G / OGF ethanol"],
              [["Inorganic chloride, mg/kg, max", "not specified", "3.0"], ["Sulphate, mg/kg, max", "not specified", "4"],
               ["Water, % v/v, max", "to report", "0.3"]], "Show the three rows of IS 15464 that differ"),
    "Almost all of India&rsquo;s blending ethanol is 1G, so the 3 ppm limit that officials cited in August 2026 has no published basis "
    "in the standard, and this blog found no amendment, notification or contract clause that applies it.",
    "BIS should extend the 3 mg/kg chloride limit, with the sulphate and water limits, to 1G ethanol, or publish the instrument that already does.",
    "standard")

s2 = insight(
    "E20 chloride readings: automakers up to 570 ppm, oil companies 0 to 3 ppm",
    bars("Automakers reported up to 190 times the 3 ppm limit; oil-company pump tests met it",
         [(f"Rajasthan <small>automakers&rsquo; emails</small>", (EMAIL[0][1], EMAIL[0][2])),
          (f"Delhi <small>automakers&rsquo; emails</small>", (EMAIL[1][1], EMAIL[1][2])),
          (f"Maharashtra <small>automakers&rsquo; emails</small>", (EMAIL[2][1], EMAIL[2][2])),
          ("Fuel from vehicle tanks <small>SIAM letter, highest</small>", 500),
          ("Fuel-station samples <small>SIAM letter, highest</small>", 350),
          ("Fuel-station samples <small>oil companies, 160 reports</small>", (0, 3))],
         accent="Rajasthan <small>automakers&rsquo; emails</small>", unit=" ppm", ref=(3, "3 ppm, the limit the ministry and oil companies cited"),
         sub="Chloride in fuel, ppm (mg/kg), as reported. Each source sampled different points.",
         source="Reuters, 13 August 2026 (automakers&rsquo; emails); Business Today, 4 August 2026 (SIAM letter); PIB, 8 August 2026 (oil-company tests)."),
    "The two sides sampled different things, fuel from failed vehicles against ethanol and petrol at distilleries, terminals and pumps, "
    "so the numbers do not contradict each other as directly as the headlines suggested.",
    "Both sides should publish their laboratory reports with sampling points and methods, and test the same pumps and vehicles under one agreed method.",
    "dispute")

s3 = insight(
    "The 2026 dispute: a letter, a withdrawal and two sets of tests in three weeks",
    flow([("Before July", "Mercedes-Benz India raises fuel-contamination concerns. SIAM says automakers had raised chloride at the BIS fuel committee for over two years."),
          ("26 July", "Automakers discuss their findings privately with the petroleum ministry, a Maruti Suzuki executive later tells Reuters."),
          ("Late July", "SIAM writes to the ministry: up to 500 mg/kg chloride in fuel from vehicle tanks, 350 mg/kg at stations, and moisture above 10,000 mg/kg against a 3,000 limit.", True),
          ("4 and 5 August", "SIAM withdraws the letter, saying some numbers need authentication and there is &ldquo;no cause for concern&rdquo;."),
          ("7 and 8 August", f"Oil companies publish tests: refinery petrol at or below 1 ppm, ethanol from {D['DISTILLERIES']} distilleries under 3 ppm, "
                             f"{D['RO_REPORTS']} station reports at 0 to 3 ppm. Two or four outlets are suspended, depending on the statement."),
          ("13 August", "Reuters publishes the automakers&rsquo; internal emails with state-wise readings of 1.4 to 570 ppm.")]),
    "The dispute ended with a withdrawn letter and two sets of numbers, neither published with its sampling method, so the evidence leaves it unresolved.",
    "Fleet owners and fuel buyers should treat chloride as an open quality risk until a joint test with a published method settles it.",
    "timeline")

s4 = insight(
    "Tank-cleaning water: enough to breach 1 to 3 mg/kg, far too little for hundreds",
    bars("A 500 mg/kg reading would need more tap water than a 20,000-litre tank holds",
         [("1 mg/kg <small>SIAM&rsquo;s proposed limit for E20</small>", R[1][0]),
          ("3 mg/kg <small>the 2G ethanol limit</small>", R[3][0]),
          ("100 mg/kg", R[100][0]),
          ("500 mg/kg <small>SIAM letter, vehicle tanks</small>", R[500][0])],
         accent="500 mg/kg <small>SIAM letter, vehicle tanks</small>", unit=" L", ref=(TANK_L, f"{TANK_L:,} litres, the whole tank"),
         sub=f"Litres of water at {ACC} mg/L chloride (the IS 10500 drinking-water limit) needed to bring {TANK_KG / 1000:.0f} tonnes of E20 "
             "to each level, if all of it dissolves into the fuel.",
         source=f"Computed by this blog: level &times; {TANK_KG:,.0f} kg of fuel &divide; {ACC} mg/L. E20 taken as about 0.75 kg a litre.")
    + numbers(["Chloride in the fuel", f"Water at {ACC} mg/L", f"Water at {PERM:,} mg/L"],
              [[f"{t} mg/kg", f"{R[t][0]:,.0f} L", f"{R[t][1]:,.0f} L"] for t in (1, 3, 100, 500)]),
    "A few dozen litres of tap water left after cleaning can push E20 past a 1 to 3 mg/kg limit, but readings in the hundreds point to a saltier "
    "source, to separated water sampled on its own, or to a measurement problem.",
    "Rinse ethanol and E20 tanks with low-chloride water, drain and dry them completely, and test the first receipt after cleaning for chloride.",
    "water")

rules = f'''<details class="xv-n"><summary>What the rules say about cleaning water</summary>
<ul>
<li><b>IS 10500, drinking water:</b> up to {ACC} mg/L chloride, or {PERM:,} mg/L where there is no other source, and at least 0.2 mg/L free chlorine. Safe to drink; not chloride-free.</li>
<li><b>Oil-company depots:</b> ethanol tanks must be water-free and cleaned every two years or as needed, and the first receipt after cleaning is tested. The ministry does not say what water is used.</li>
<li><b>API 650, Annex S (stainless tanks):</b> test water under 50 ppm chloride, standing no more than 21 days, then drained and dried completely.</li>
<li><b>Water UK guidance:</b> strongly chlorinated water is acceptable for disinfection only if it is &ldquo;well flushed through the system immediately afterwards or pitting can occur&rdquo;.</li>
</ul></details>
'''

harm = '''<h2 class="gb-h2" id="harm">Why a few mg/kg of chloride matters</h2>
<p>With water and dissolved oxygen, chloride drives pitting and stress corrosion cracking in steel tanks and pipes. One study in a 2021 review found cracking with chloride below 1 mg/L in ethanol.</p>
<p>ASTM&rsquo;s chloride test method gives the reason for testing plainly: chlorides &ldquo;may be found in filter plugging deposits and fuel injector deposits&rdquo;.</p>
'''

fixes = '''<h2 class="gb-h2" id="s1">Five fixes, in order of effort</h2>
<ol>
<li><b>Put chloride on every tank truck&rsquo;s certificate</b>, next to purity, water, density and sulphur.</li>
<li><b>Specify tank-cleaning water</b>: low-chloride rinse, full draining and drying, a chloride test on the first receipt.</li>
<li><b>Make sure BIS-recognised laboratories can run the test</b> (ASTM D7319 or EN 15492).</li>
<li><b>Amend IS 15464</b> to apply the chloride, sulphate and water limits to 1G ethanol.</li>
<li><b>Add a chloride limit for finished E20</b>, so fuel can be tested at the pump against a published number.</li>
</ol>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The legal basis of the 3 ppm limit for 1G ethanol: no amendment, notification or contract clause was found.</li>
<li>The oil companies&rsquo; outlet-level tables at the Centre for High Technology, which could not be opened.</li>
<li>The automakers&rsquo; sampling method, known only through press coverage.</li>
<li>Current editions of foreign standards: the US figure is from a 2018 summary of ASTM D4806; China&rsquo;s GB 18350 was not checked.</li>
<li>What water oil companies and dealers use to clean tanks.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + rules + harm + fixes + gaps
SLUG = "chloride-in-fuel-ethanol-is-15464-sets"
FR = split((ROOT / f"posts/{SLUG}.html").read_text(encoding="utf-8"))
assert FR, "live post does not have the standard frame"
OUT.write_text(FR.head + FR.mid + body + "\n" + FR.tail, encoding="utf-8")
print("wrote", OUT.relative_to(ROOT))
