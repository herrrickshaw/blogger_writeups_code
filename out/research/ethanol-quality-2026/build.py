"""Ethanol 2026-27: blending history, feedstock rules for the 2026-27 tender, prices by feedstock, procurement cost.
Build from the repo root:  python3 out/research/ethanol-quality-2026/build.py   (writes out/post-india-ethanol-2026-27-tender-feedstock-blending.html). Analysed 18 November 2026."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-ethanol-2026-27-tender-feedstock-blending.html"
B = "https://blog.vertistratsolution.com"

# ---- Blending, ESY (Lok Sabha/Rajya Sabha replies, PIB 23 Jul 2026) ----
BLEND = [("2013-14", 1.53), ("2017-18", 4.22), ("2020-21", 8.10), ("2021-22", 10.02), ("2022-23", 12.06), ("2023-24", 14.60), ("2024-25", 19.24), ("2025-26 (to Jan 2026)", 20.0)]
assert 19.24 - 14.60 == 4.64 or round(19.24 - 14.60, 2) == 4.64
# ---- Procurement value, Rs crore (RS USQ 141, 20 Jul 2026) ----
PROC = [("2023-24", 48757), ("2024-25", 73996), ("2025-26 to June 2026", 49577)]
assert round(100 * (73996 / 48757 - 1)) == 52
# ---- 2026-27 tender (S&P Global, 22 Oct 2026): about 11 billion litres; FCI rice 7.2 MT = up to 3.24 billion litres; 1.08 bn litres cap in each of first 3 quarters ----
TENDER, RICE_BL, RICE_MT = 11.0, 3.24, 7.2
assert round(RICE_BL * 1000 / RICE_MT) == 450                    # litres per tonne
assert round(1.08 * 3, 2) == RICE_BL and round(100 * RICE_BL / TENDER) == 29
# ---- Ethanol price by feedstock, ESY 2025-26, Rs a litre (MoPNG via USDA GAIN, 23 Jul 2026) ----
PRICE = [("Maize", 71.86), ("Sugarcane juice, syrup, sugar", 65.61), ("Damaged food grains", 64.00), ("Surplus FCI rice", 60.32), ("B-heavy molasses", 60.73), ("C-heavy molasses", 57.97)]
spread = max(v for _, v in PRICE) - min(v for _, v in PRICE)
assert round(spread, 2) == 13.89
# ---- Suppliers and capacity ----
SUPPLIERS = 501
CAP_BL = 20                                                          # about 2,000 crore litres a year (RS USQ 940)
NEED_BL = (10, 11)                                                   # E20 needs about 10 to 11 billion litres a year (question text)
assert CAP_BL / NEED_BL[1] > 1.8

TITLE = "Ethanol 2026-27: 11 billion litres tendered, cane juice and B-heavy molasses excluded"
assert 55 <= len(TITLE) <= 90, len(TITLE)

top = top_line([
    ("20%", " was the average ethanol blend by January 2026, reached in December 2025; the government says no decision has been taken to go beyond 20%, while a US agriculture attache projects 23.4% for 2026."),
    ("11 billion litres", " are sought in the 16 October 2026 tender for 2026-27, which excludes sugarcane juice, sugar syrup and B-heavy molasses and allots 7.2 million tonnes of FCI rice, up to 3.24 billion litres."),
    ("Rs 73,996 crore", " was spent on ethanol in 2024-25, up 52% from Rs 48,757 crore; E20 petrol with a minimum RON of 95 became the national standard from 1 April 2026."),
])

s1 = insight(
    "Blending rose from 1.53% in 2013-14 to 20% in 2025-26",
    bars("Ethanol blending reached 20% in 2025-26, five years ahead of the 2030 target",
         BLEND, accent="2025-26 (to Jan 2026)", unit="%", ref=(20, "E20"),
         sub="Average ethanol blended in petrol by public sector oil marketing companies, % by volume, by ethanol supply year (November to October).",
         source="Rajya Sabha unstarred question 1898 (8 March 2026); Rajya Sabha unstarred question 143 (20 July 2026); PIB, 23 July 2026.")
    + numbers(["Item", "Value", "Source"],
              [["Target year for 20%", "advanced from 2030 to ESY 2025-26", "National Policy on Biofuels, as amended 2022"],
               ["Reached", "19.98% average to 31 December 2025; 19.99% in December 2025", "Rajya Sabha question 300, February 2026"],
               ["E20 standard", "mandatory from 1 April 2026 at a minimum RON of 95, after a 17 February directive", "Lok Sabha question 700; USDA GAIN"],
               ["Beyond 20%", "no decision; E85 only for certified flex-fuel vehicles", "PIB, 23 July 2026"],
               ["Registered suppliers", f"{SUPPLIERS}", "Rajya Sabha question 141"]]),
    "A rise of 4.64 points from 14.60% to 19.24% in 2024-25 was the last big step, and the 20% in 2025-26 is a plateau that the government says it will not leave without scientific and industry consultation.",
    "The Ministry of Petroleum should publish the monthly blend by oil company and state, so that the plateau can be checked against the 20% claimed.",
    "blend")

s2 = insight(
    "The 2026-27 tender wants 11 billion litres and bans cane juice and B-heavy molasses",
    bars("FCI rice is allotted up to 3.24 billion litres, 29% of the 11 billion litres tendered",
         [("Total tendered for ESY 2026-27", TENDER), ("FCI rice allotment, up to", RICE_BL), ("Rice cap in each of the first three quarters", 1.08), ("Left for maize, damaged grain, C-heavy molasses and others", round(TENDER - RICE_BL, 2))],
         accent="FCI rice allotment, up to", unit=" billion litres",
         sub="Billion litres of denatured anhydrous ethanol. The food department told sugar states on 22 October 2026 that sugar diversion to ethanol will not be permitted from 1 November.",
         source="S&amp;P Global Commodity Insights, 22 October 2026 (tender of 16 October; order of 22 October).")
    + numbers(["Feature", "Detail"],
              [["Excluded feedstocks", "sugarcane juice, sugar, sugar syrup, B-heavy molasses"], ["Eligible", "maize, damaged food grains, FCI surplus rice, C-heavy molasses, others permitted by the policy"],
               ["FCI rice", "7.2 million tonnes to 30 June 2027, up to 3.24 billion litres: 450 litres a tonne"], ["Rice offers", "none for August to October 2027"], ["Period", "1 November 2026 to 31 October 2027"]]),
    "Grain and rice now carry the blending target, which moves the ethanol programme closer to food supply, since rice that FCI would otherwise hold is allotted a quarter of the tender.",
    "The food and petroleum ministries should publish, before each quarter, how much FCI rice and maize the tender will use, so that grain markets and distilleries can plan together.",
    "tender")

s3 = insight(
    "Ethanol prices range from Rs 57.97 a litre for C-heavy molasses to Rs 71.86 for maize",
    bars("Maize ethanol is paid Rs 13.89 a litre more than C-heavy molasses ethanol",
         sorted(PRICE, key=lambda kv: -kv[1]), accent="Maize", unit="₹/litre",
         sub="Administered ethanol price by feedstock, ESY 2025-26, Rs a litre.",
         source="Ministry of Petroleum and Natural Gas, as published in USDA FAS GAIN Biofuels Annual, 23 July 2026.")
    + numbers(["Feedstock", "ESY 2023-24", "ESY 2024-25", "ESY 2025-26"],
              [["Maize", "66.00", "71.86", "71.86"], ["Sugarcane juice, syrup, sugar", "65.61", "65.61", "65.61"], ["Damaged food grains", "64.00", "64.00", "64.00"],
               ["Surplus FCI rice", "58.50", "58.50", "60.32"], ["B-heavy molasses", "60.73", "60.73", "60.73"], ["C-heavy molasses", "56.28", "57.97", "57.97"]]),
    "A price gap of Rs 13.89 a litre between maize and C-heavy molasses explains why distilleries lean on grain, and it is paid for by the procurement bill of Rs 73,996 crore in 2024-25.",
    "The oil marketing companies should publish the quantity bought from each feedstock at each price every quarter, so the cost of the grain shift can be separated from the cost of volume.",
    "price")

s4 = insight(
    "Ethanol procurement cost Rs 73,996 crore in 2024-25, up 52% in a year",
    bars("Oil companies' ethanol bill rose 52% in 2024-25 and Rs 49,577 crore was spent by June 2026",
         PROC, accent="2024-25", unit="₹ crore",
         sub="Ethanol procurement value by public sector oil marketing companies, Rs crore, including transport and GST. 2025-26 covers November 2025 to June 2026 only.",
         source="Rajya Sabha unstarred question 141, 20 July 2026.")
    + numbers(["Item", "Value"],
              [["Procurement 2023-24", "Rs 48,757 crore"], ["Procurement 2024-25", "Rs 73,996 crore, up 52%"], ["Procurement 2025-26 to June 2026", "Rs 49,577 crore"],
               ["Capacity", "about 2,000 crore litres a year against about 1,000 to 1,100 crore litres needed for E20 (question text)"],
               ["Parliamentary committee", "Food and Consumer Affairs committee took a briefing on quality assurance and standardisation of ethanol and biofuels on 17 November 2026; no report yet"]]),
    "Installed capacity of about 20 billion litres is nearly twice the 10 to 11 billion litres that E20 needs, so the tender volume is set by policy and not by what distilleries can make.",
    "The Ministry of Petroleum should publish capacity utilisation by feedstock and the share of the 501 suppliers that supplied nothing in the last supply year.",
    "cost")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Petroleum and Natural Gas:</b> publish monthly blend and ethanol bought by company, state and feedstock.</li>
<li><b>Department of Food and Public Distribution:</b> publish the quarterly FCI rice and maize plan so grain markets can plan.</li>
<li><b>Oil marketing companies:</b> publish capacity utilisation and the number of registered suppliers that delivered.</li>
<li><b>Standing Committee on Food, Consumer Affairs and Public Distribution:</b> publish its quality-assurance findings with the test data it received.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''
method = '''<details class="xv-n"><summary>Method and definitions</summary><ul>
<li>An ethanol supply year (ESY) runs from 1 November to 31 October. Blending is ethanol by volume in petrol sold by public sector oil marketing companies.</li>
<li>RON is research octane number; E20 is petrol with 20% ethanol; FCI is the Food Corporation of India.</li>
<li>Rice litres a tonne is the tender allotment of 3.24 billion litres divided by 7.2 million tonnes.</li></ul></details>
'''
gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary><ul>
<li>The quality-assurance findings of the committee: it heard a briefing on 17 November 2026 and has published nothing.</li>
<li>The tender result: the 16 October 2026 tender was reported, but offers and awards were not read.</li>
<li>A conflict on the blend: the government says 20% in 2025-26 with no decision beyond; USDA projects 23.4% for calendar 2026 and says industry sources call E30 attainable.</li>
<li>Price and price series for 2026-27, which the sources do not give.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps
SOURCES = ('<a href="https://sansad.in/getFile/annex/270/AU1898_HVBDeE.pdf?source=pqars">Rajya Sabha unstarred question 1898, 8 March 2026</a> (blend by supply year) and <a href="https://sansad.in/getFile/annex/270/AU300_xODNmF.pdf?source=pqars">question 300</a> (December 2025 blend); '
  '<a href="https://sansad.in/getFile/annex/271/AU143_G24m0X.pdf?source=pqars">Rajya Sabha unstarred question 143, 20 July 2026</a> and <a href="https://sansad.in/getFile/annex/271/AU141_uFVNuE.pdf?utm_campaign=fullarticle&amp;utm_medium=referral&amp;source=pqars&amp;utm_source=inshorts">question 141</a> (suppliers; procurement value); '
  '<a href="https://sansad.in/getFile/annex/271/AU940_UiBiGe.pdf?source=pqars">Rajya Sabha unstarred question 940, 27 July 2026</a> (capacity); '
  '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2288271&amp;lang=1&amp;reg=3">PIB, 23 July 2026</a>; '
  '<a href="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU700_CehVn4.pdf?source=lsapps">Lok Sabha unstarred question 700, 23 July 2026</a> (RON 95 from 1 April 2026); '
  '<a href="https://www.spglobal.com/energy/en/news-research/latest-news/agriculture/102226-india-orders-states-to-enforce-zero-sugar-diversion-for-ethanol-supply">S&amp;P Global, 22 October 2026</a> (2026-27 tender); '
  '<a href="https://www.fas.usda.gov/data/gain-report/2026/07/Biofuels%20Annual_New%20Delhi_India_IN2026-0039.pdf">USDA FAS GAIN, Biofuels Annual, 23 July 2026</a> (prices by feedstock; 23.4% projection); '
  '<a href="https://prsindia.org/parliament-committees">PRS, committee schedule</a>. Shares computed by this blog. Analysed 18 November 2026.')
RELATED = [(f"{B}/2026/08/india-hit-e20-on-maize-and-rice-not.html", "India's E20 ethanol target: reached mainly with maize and rice, not sugarcane"),
           (f"{B}/2026/08/from-cane-to-code-digital-layer.html", "Ethanol blending beyond E20: AI in mills and fields, no blockchain tracing yet"),
           (f"{B}/2026/09/the-diesel-truck-isnt-why-your-eggs.html", "Egg prices in India: maize demand for ethanol raises feed costs more than diesel"),
           (f"{B}/2026/09/ethanol-freed-up-refinery-capacity-for.html", "E20 blending: freed refinery capacity goes to polymers and LPG, not pharma")]
build("Energy &middot; Biofuels", TITLE, "The 2026-27 ethanol tender seeks 11 billion litres without cane juice or B-heavy molasses and leans on 3.24 billion litres of FCI rice, after blending reached 20%.", body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE))
