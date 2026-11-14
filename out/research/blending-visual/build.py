"""Visual-first edition of "Biofuel blends and mileage" (docs/VISUAL_STORY_STYLE.md).
Build from the repo root:  python3 out/research/blending-visual/build.py

Keeps the live post's frame exactly (title block, accessibility bar, translate widget, picture, the
"does not establish" card, related links, sources, disclaimer) and replaces only the body between them.
Every number below appears in the live post (posts/blending-on-budget-energy-density-and.html) or is
arithmetic on those numbers, checked by the asserts."""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from exec_viz import STYLE, bars, insight, line, numbers, top_line  # noqa: E402

SLUG = "blending-on-budget-energy-density-and"
SRC = (ROOT / f"posts/{SLUG}.html").read_text(encoding="utf-8")
OUT = ROOT / f"out/update-2026-11-15-{SLUG}.html"

# ---- figures from the live post ----
PETROL, ETHANOL, DIESEL, ISOBUTANOL = 32.4, 21.3, 35.8, 26.6        # MJ/L
E20_CEIL = 0.20 * (1 - ETHANOL / PETROL) * 100                      # % energy per litre lost at 20%
ISO_CEIL = 0.15 * (1 - ISOBUTANOL / DIESEL) * 100                   # at the proposed 15%
assert round(ETHANOL / PETROL * 100) == 66 and round(ISOBUTANOL / DIESEL * 100) == 74
assert round(E20_CEIL, 1) == 6.9 and round(ISO_CEIL, 1) == 3.9
for s in ("₹3,900–4,900 a year", "₹0.27–0.33 per kilometre", "2–6% efficiency reduction", "SIAM cites 2–4%",
          "1–2%", "₹650–1,300 a year", "$1.4 per litre", "$0.6–0.8/L", "about 1.05%", "about 0.93%",
          "3% in FY2026-27, 4% in FY2027-28 and 5% from FY2028-29", "1% blending from 2027, rising to 2% by 2028 and 5% by 2030"):
    assert s in re.sub(r"\s+", " ", html.unescape(SRC)), s

# ---- the live frame (tools/viz_frame.py): head and mid kept byte for byte, the hero chart replaced by the sections ----
sys.path.insert(0, str(ROOT / "tools"))
from viz_frame import split  # noqa: E402
FR = split(SRC)
head, mid, tail = FR.head, FR.mid, FR.tail
picture = FR.keep_front + FR.notes

top = top_line([
    ("66%", " of petrol&rsquo;s energy per litre is what ethanol carries, so E20 costs drivers 2&ndash;6% in mileage: "
            "about &#8377;3,900&ndash;4,900 a year at a 4% loss, on Delhi fuel prices."),
    ("3.9% vs 6.9%", " is the most mileage a 15% isobutanol-diesel blend could cost, against E20&rsquo;s ceiling. "
                     "The diesel mandate is proposed, not notified."),
    ("$1.4 a litre", " is a 2026 projection for India-made SAF, against $0.6&ndash;0.8 for conventional jet fuel. "
                     "SAF and CBG cost users money, not range."),
])

s1 = insight(
    "Energy per litre: ethanol 66% of petrol, isobutanol 74% of diesel, CBG and SAF near parity",
    bars("Only the two alcohols fall well short of the fuel they replace",
         [("Ethanol in petrol <small>E20, live nationwide</small>", 66), ("Isobutanol in diesel <small>proposed, 15%</small>", 74),
          ("CBG in CNG <small>1% obligation, rising to 5%</small>", (93, 95)), ("SAF in jet fuel <small>by mass; from 2027</small>", (99, 102))],
         accent="Ethanol in petrol <small>E20, live nationwide</small>", unit="%", vmax=104, from_zero=True, ref=(100, "100% means the same energy as the host fuel"),
         sub="Energy density of the blend component as a share of the fuel it replaces.",
         source="NITI Aayog ethanol roadmap; US DOE Alternative Fuels Data Center; IEA Advanced Motor Fuels; published aviation-fuel comparisons.")
    + numbers(["Pair", "Host fuel", "Blend component", "Share"],
              [["Ethanol in petrol", "32.4 MJ/L", "21.3 MJ/L", "66%"], ["Isobutanol in diesel", "35.8 MJ/L", "26.6 MJ/L", "74%"],
               ["CBG in CNG", "50&ndash;56 MJ/kg", "47&ndash;52 MJ/kg", "93&ndash;95%"], ["SAF in jet fuel", "43.3 MJ/kg", "44.0 MJ/kg", "99&ndash;102%"]]),
    "Ethanol and isobutanol cost drivers mileage because each litre carries less energy, while CBG and SAF match their host fuels "
    "and show up as a price premium instead.",
    "Judge a blending mandate by the energy gap of its blend component, not by its headline percentage.",
    "pairs")

s2 = insight(
    "E20 mileage: 2 to 6% lost in tests, under the 6.9% energy ceiling",
    bars("E20&rsquo;s measured mileage loss sits under its 6.9% energy ceiling",
         [("Energy ceiling <small>20% ethanol, less energy per litre</small>", round(E20_CEIL, 1)),
          ("ARAI controlled tests", (2, 6)), ("SIAM&rsquo;s figure", (2, 4)),
          ("Used for the cost estimate", 4)],
         accent="ARAI controlled tests", unit="%",
         sub="Mileage lost on E20 against pure petrol, %.",
         source="ARAI and SIAM, as cited in the post; ceiling computed from 32.4 and 21.3 MJ/L."),
    "E20 sells at the price of the petrol it replaced, so a 4% loss works out to &#8377;0.27&ndash;0.33 a kilometre, "
    "lightest for E20-compliant vehicles made since about 2023.",
    "The petroleum ministry should publish its own estimate of E20&rsquo;s mileage loss and yearly cost, split between compliant and older vehicles.",
    "e20")

s3 = insight(
    "Isobutanol in diesel: a 3.9% ceiling at 15%, just over half of E20&rsquo;s",
    bars("A 15% isobutanol blend would cost diesel just over half E20&rsquo;s mileage ceiling",
         [("E20 petrol <small>ceiling, 20% ethanol</small>", round(E20_CEIL, 1)),
          ("Isobutanol diesel <small>ceiling, 15% proposed</small>", round(ISO_CEIL, 1)),
          ("Isobutanol diesel <small>pilot trials at 2&ndash;5%</small>", (1, 2))],
         accent="Isobutanol diesel <small>ceiling, 15% proposed</small>", unit="%",
         sub="Most mileage the blend can cost (energy ceiling), and the loss reported in pilot trials, %.",
         source="Ceilings computed from 35.8 and 26.6 MJ/L (IEA-AMF) and 32.4 and 21.3 MJ/L; pilot trials as reported in the trade press."),
    "Isobutanol holds more energy per litre than ethanol, so even a deeper blend caps the loss near 3.9%, "
    "though that is a projection for a mandate that has not been notified.",
    "BIS should publish an isobutanol-diesel specification, and the ministry ARAI results at 15%, before any mandate is notified.",
    "isobutanol")

s4 = insight(
    "Gas and aviation mandates: 1% today, 5% by 2028-29 for CBG and 2030 for SAF",
    line("CBG&rsquo;s obligation rises fivefold by 2028-29; SAF reaches the same 5% in 2030",
         {"CBG": [(2026, 1), (2027, 3), (2028, 4), (2029, 5)],
          "SAF": [(2027, 1), (2028, 2), (2030, 5)]},
         accent="CBG", unit="%", yfmt=lambda v: f"{v:g}",
         sub="Required blend share, %. CBG by fiscal year ending March; SAF by calendar year. E20 is already at 20%.",
         source="PIB, mandatory CBG blending in city gas; India&rsquo;s SAF timeline, aligned with ICAO CORSIA Phase II.")
    + numbers(["Year", "CBG obligation", "SAF mandate"],
              [["2025-26", "1% (about 0.93&ndash;1.05% achieved)", "&ndash;"], ["2026-27", "3%", "&ndash;"], ["2027-28", "4%", "1% (2027)"],
               ["2028-29", "5%", "2% (2028)"], ["2030", "5%", "5%"]]),
    "Both mandates are small today, and CBG&rsquo;s first year landed at about 0.93 to 1.05% against a 1% target, "
    "so their cost to users comes through input prices rather than lost range.",
    "PNGRB should publish each city-gas company&rsquo;s monthly CBG share, and the civil aviation ministry the SAF price paid each year from 2027.",
    "mandates")

standards = '''<details class="xv-n"><summary>Which standards govern each fuel</summary>
<ul>
<li><b>Ethanol in petrol:</b> IS 17021 (E20 fuel), IS 2796 (petrol), IS 15464 (ethanol for blending). US comparators: ASTM D4806, ASTM D5798.</li>
<li><b>CBG in CNG:</b> IS 15958:2023 (CNG and LNG fuel), IS 16087:2016 (CBG, at least 90% methane). Europe: EN 16723-2.</li>
<li><b>Isobutanol in diesel:</b> IS 1460:2017 covers diesel only. No specification for the blend was found, in India or elsewhere.</li>
<li><b>SAF in jet fuel:</b> ASTM D1655 (Jet A-1) and ASTM D7566 (synthetic blends; Annex A5 for alcohol-to-jet). API 1543 and 1595 cover handling, not composition.</li>
</ul></details>
'''

supply = '''<details class="xv-n"><summary>Who is building isobutanol supply</summary>
<p>MC&sup2; Foundation, backed by seven public-sector energy companies, launched the Grand Butanol Challenge on 17 July 2026 with up to &#8377;12.5 crore for bio-based butanol routes; applications closed on 15 August 2026. BPCL already makes isobutanol, but from propylene, a fossil route.</p>
</details>
'''

fixes = '''<h2 class="gb-h2" id="fix">Five fixes</h2>
<ol>
<li><b>BIS:</b> publish a draft isobutanol-diesel specification before any mandate is notified.</li>
<li><b>Petroleum ministry:</b> publish ARAI results for isobutanol-diesel at 15%, by vehicle type.</li>
<li><b>Petroleum ministry:</b> publish an official estimate of E20&rsquo;s mileage loss and yearly cost to drivers.</li>
<li><b>PNGRB:</b> require each city-gas company to report its monthly CBG share against the 1% to 5% obligation.</li>
<li><b>Civil aviation ministry:</b> publish the SAF price paid and the jet-fuel benchmark each year from 2027.</li>
</ol>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

updated = ('<p class="gb-note"><b>Updated 15 November 2026:</b> rewritten as four charts; figures unchanged from the '
           '7 November update (CBG first-year blending, Q2 2026 SAF prices, isobutanol still not notified).</p>\n')

body = head + mid + STYLE + top + picture + "\n" + updated + s1 + s2 + s3 + s4 + standards + supply + fixes + "\n" + tail
OUT.write_text(body, encoding="utf-8")
words = lambda h: len(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", "", h, flags=re.S)).split())
print(f"wrote {OUT.relative_to(ROOT)}: {words(SRC):,} words -> {words(body):,}")
