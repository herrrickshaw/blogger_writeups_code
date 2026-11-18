"""India's push to indigenise 100 imports (DPIIT, Nov 2026): PVC capacity against demand, import sources, solar chain, import growth.
Build from the repo root:  python3 out/research/dpiit-100-2026/build.py   (writes out/post-india-100-item-import-push-pvc-china-nov-2026.html)
Analysed 18 November 2026."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-100-item-import-push-pvc-china-nov-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- PVC (Commerce Ministry statement, Indian Express 2 Aug 2026; GTRI via ET 29 Jul 2026; DGFT notification 24 Jul 2026) ----
CAP, DEMAND, NEW_CAP, RIL_PLAN = 1615, 4139, 3000, 1500           # kilotonnes a year
GAP = DEMAND - CAP
assert GAP == 2524 and round(100 * CAP / DEMAND) == 39
assert round(100 * RIL_PLAN / CAP) == 93
assert CAP + NEW_CAP == 4615 and CAP + NEW_CAP > DEMAND
IMPORTS = [("China", 735.4), ("Japan", 280.4), ("Taiwan", 152.7), ("South Korea", 123.6), ("Mexico", 92.9)]
TOTAL_IMP = 1630
top5 = sum(v for _, v in IMPORTS)
assert round(100 * 735.4 / TOTAL_IMP) == 45 and round(top5) == 1385 and round(100 * top5 / TOTAL_IMP) == 85
assert round(DEMAND - CAP) == round(GAP)
RIL_SHARE = 0.51
assert round(RIL_SHARE * CAP) == 824

# ---- Solar chain (Indian Express 8 Nov via NCA Academy and EcoNiti, secondary): module 233 GW, cell about 30 GW, ingot-wafer about 2 GW ----
CHAIN = [("Modules", 233), ("Cells", 30), ("Ingots and wafers", 2)]
assert round(233 / 30, 1) == 7.8 and round(30 / 2) == 15

# ---- Import growth (NCA Academy summary of PTI/Indian Express, secondary) ----
CHEM_26, CHEM_G = 16.1, 10.5
MACH_26, MACH_G = 34.1, 15.5
CHEM_PRIOR, MACH_PRIOR = CHEM_26 / (1 + CHEM_G / 100), MACH_26 / (1 + MACH_G / 100)
assert round(CHEM_PRIOR, 1) == 14.6 and round(MACH_PRIOR, 1) == 29.5
TOTAL_IMP_FY26, TOTAL_G = 775, 7.5

TITLE = "India's 100-item import push: PVC capacity meets 39% of demand"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    ("100 items", " is the list DPIIT has drawn up of heavily imported intermediates and capital goods, from PVC and ammonia to tunnel boring machines; proposals go to the Finance Ministry for Budget 2027-28."),
    ("39%", f" of PVC demand is met by domestic capacity, 1,615 of 4,139 kilotonnes a year; an import floor price of $0.766 a kg runs for six months from 24 July 2026."),
    ("45%", " of the $1.63 billion of PVC resin imported in 2025-26 came from China, $735.4 million; the China goods deficit is reported above $100 billion."),
])

s1 = insight(
    "India's PVC capacity is 1,615 kilotonnes a year against demand of 4,139",
    bars("Domestic PVC capacity meets 39% of demand; 3,000 kilotonnes more is expected in 2026-27",
         [("Demand", DEMAND), ("Domestic capacity", CAP), ("Shortfall", GAP), ("New capacity expected in 2026-27", NEW_CAP), ("Reliance planned capacity, 2026-27", RIL_PLAN)],
         accent="Domestic capacity", unit=" kilotonnes",
         sub="Kilotonnes a year. Commerce Ministry figures; Reliance is reported to hold 51% of domestic output and plans 1.5 million tonnes by 2026-27.",
         source="Commerce and Industry Ministry statement, Indian Express, 2 August 2026; Indian Express, 8 November 2026.")
    + numbers(["Item", "Value", "Source"],
              [["Minimum import price", "$0.766 a kg CIF on suspension PVC resin (HS 39041020); imports at or below it restricted for six months from 24 July 2026", "DGFT notification, 24 July 2026"],
               ["Exemptions", "100% export-oriented units, SEZ units and advance authorisation imports, if not sold in the domestic market", "DGFT notification"],
               ["Cost assessment", "$0.65 to $0.75 a kg is at or below the cost of production of the most efficient domestic producer", "Commerce Ministry"],
               ["Anti-dumping", "DGTR recommended duties of $22 to $284 a tonne in August 2025", "Commerce Ministry"],
               ["Quality control order", "revoked on 12 November 2025 to ease supply", "Commerce Ministry"],
               ["Reliance", f"51% of domestic manufacturing, about {round(RIL_SHARE * CAP)} kilotonnes on the 1,615 base; planned 1,500 kilotonnes is {round(100 * RIL_PLAN / CAP)}% of today&rsquo;s national capacity", "Indian Express; computed here"]]),
    "If the 3,000 kilotonnes arrive in 2026-27, capacity of 4,615 kilotonnes passes demand of 4,139 and the shortfall turns into a surplus, so the floor price protects a market that the ministry itself expects to flip within a year.",
    "The Commerce Ministry should state before the six-month floor lapses in January 2027 which new plants are under construction and when each commissions, so that the extension decision can be tested against capacity.",
    "pvc")

s2 = insight(
    "China supplied $735.4 million of $1.63 billion of PVC resin imports in 2025-26, 45%",
    bars("Five suppliers sent 85% of India's $1.63 billion of PVC resin; China sent 45%",
         IMPORTS + [("All other suppliers", round(TOTAL_IMP - top5, 1))], accent="China", unit="$ million",
         sub="Suspension PVC resin imports in 2025-26, US$ million. The total is the rounded $1.63 billion that GTRI reports.",
         source="GTRI, as reported by The Economic Times, 29 July 2026.")
    + numbers(["Supplier", "US$ million", "Share of $1.63 billion"],
              [[n, f"{v:,.1f}", f"{100 * v / TOTAL_IMP:.0f}%"] for n, v in IMPORTS]),
    "A floor price of $0.766 a kg touches virtually every major supplier, and GTRI expects it to raise domestic prices without reducing import dependence.",
    "The Commerce Ministry should publish the monthly import volume and landed price of PVC resin by supplier through the six-month period, so that the effect on prices and on imports can be read from data.",
    "sources")

s3 = insight(
    "India makes 233 GW of solar modules a year but about 30 GW of cells and 2 GW of wafers",
    bars("Solar capacity falls by factors of 8 and 15 at each step upstream of modules",
         CHAIN, accent="Ingots and wafers", unit=" GW a year",
         sub="Approximate annual capacity in GW, industry estimates quoted by The Indian Express; China plans export licences for solar manufacturing technology.",
         source="Indian Express, 8 November 2026, as summarised by NCA Academy and EcoNiti (secondary).")
    + numbers(["Step", "GW a year", "Ratio to the next step"],
              [["Modules", "233", f"{233 / 30:.1f} times cells"], ["Cells", "30", f"{30 / 2:.0f} times ingot and wafer"], ["Ingots and wafers", "2", "&ndash;"],
               ["Cost of switching machinery to Europe or Japan", "20% to 40% higher", "Industry executive, Indian Express"]]),
    "Module assembly depends on imported cells, and new cell and wafer plants depend on equipment that China proposes to license, so the 100-item list reaches into the solar chain at its thinnest point.",
    "DPIIT should publish the 100 items with their import value and country of origin, so that the strategic ones can be told apart from the ones that are only large.",
    "solar")

s4 = insight(
    "Chemical imports rose 10.5% and machinery imports 15.5% in April to September 2026",
    bars("Machinery imports reached $34.1 billion in April to September 2026, up 15.5%",
         [("Chemicals, April to September 2025 (implied)", round(CHEM_PRIOR, 1)), ("Chemicals, April to September 2026", CHEM_26),
          ("Machinery, April to September 2025 (implied)", round(MACH_PRIOR, 1)), ("Machinery, April to September 2026", MACH_26)],
         accent="Machinery, April to September 2026", unit="$ billion",
         sub="Imports in US$ billion. The 2025 values are back-calculated here from the reported 2026 values and growth rates.",
         source="PTI via NCA Academy, 13 November 2026 (secondary); total imports $775 billion in 2025-26, up 7.5%.")
    + numbers(["Measure", "Value", "Note"],
              [["Total merchandise imports, 2025-26", "$775 billion, up 7.5%", "NCA Academy summary of PTI"],
               ["Goods deficit with China", "above $100 billion", "Indian Express, 8 November, &ldquo;current fiscal year&rdquo;; Drishti IAS, 12 November, FY2025-26"],
               ["Working groups", "six, set up 4 June 2026, chaired by the DPIIT Secretary", "NCA Academy"],
               ["Possible support", "incentives, research help, tariff steps, testing facilities", "NCA Academy; BusinessLine, 9 November"]]),
    "Machinery imports are growing faster than the overall import bill of 7.5%, which means the push to localise capital goods is running against the direction of the data.",
    "The Finance Ministry should decide support for the list item by item against the import value and the time to build capacity, since a blanket incentive would reward items that need none.",
    "growth")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>DPIIT:</b> publish the 100 items with import value, source country and the date a domestic plant would commission.</li>
<li><b>Ministry of Commerce and Industry:</b> publish monthly PVC import volume and landed price by supplier during the minimum-price period, with the decision date on extension.</li>
<li><b>Ministry of Commerce and Industry:</b> state whether the China goods deficit above $100 billion refers to FY2025-26 or to the part of FY2026-27 so far, and publish the series.</li>
<li><b>Ministry of New and Renewable Energy:</b> publish solar cell and wafer capacity under construction by plant.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''
method = '''<details class="xv-n"><summary>Method and definitions</summary><ul>
<li>Capacity and demand are in kilotonnes a year as the Commerce Ministry gave them; the shortfall and shares are computed here.</li>
<li>The minimum import price is a CIF value floor: imports at or below $0.766 a kg are restricted, imports above it are free, for six months from the gazette date of 24 July 2026.</li>
<li>2025 import values in the last chart are implied by dividing the 2026 value by one plus the reported growth rate.</li></ul></details>
'''
gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary><ul>
<li>The list of 100 items: it has not been published; only sectors and examples are in press reports.</li>
<li>The period of the China deficit: one report says the current fiscal year, another says FY2025-26.</li>
<li>The date of the floor price: one Indian Express report gives 24 June and another 24 July; the gazette is dated 24 July 2026 and is used here.</li>
<li>The solar capacity figures and the import growth rates come from secondary summaries of the Indian Express and PTI, not from the originals.</li>
<li>Whether the 3,000 kilotonnes of new capacity is under construction; the ministry says it is &ldquo;expected&rdquo;.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps
SOURCES = ('<a href="https://indianexpress.com/article/explained/explained-economics/chemical-to-capital-goods-india-100-10954928">Indian Express, 8 November 2026</a> (100-item push; Reliance share; China deficit); '
  '<a href="https://www.thehindubusinessline.com/economy/dpiit-eyes-budget-fy28-push-to-localise-100-import-heavy-items-from-pharma-to-machinery/article71683165.ece">The Hindu BusinessLine, 9 November 2026</a> (working groups; Budget FY28); '
  '<a href="https://indianexpress.com/article/business/minimum-import-price-on-s-pvc-resin-to-reduce-import-dependency-commerce-ministry-10814803/">Indian Express, 2 August 2026</a> (ministry statement on capacity, demand and floor price); '
  '<a href="https://egazette.gov.in/WriteReadData/2026/274781.pdf">DGFT notification, Gazette of India, 24 July 2026</a>; '
  '<a href="https://m.economictimes.com/news/economy/foreign-trade/import-restriction-on-low-priced-pvc-resin-may-push-domestic-prices-gtri/articleshow/132707736.cms">Economic Times, 29 July 2026</a> (GTRI import values); '
  '<a href="https://ncaacademy.com/dpiit-indigenise-100-critical-items">NCA Academy, 13 November 2026</a> and <a href="https://www.econiti.org/daily-news/2026-11-09/2026-11-09-dpiit-indigenise-100-critical-items-china-export-curbs">EcoNiti, 9 November 2026</a> (secondary); '
  '<a href="https://www.drishtiias.com/current-affairs-news-analysis-editorials/news-analysis/12-11-2026">Drishti IAS, 12 November 2026</a>. Shares and ratios computed by this blog. Analysed 18 November 2026.')
RELATED = [(f"{B}/2026/07/indias-petrochemical-import-tree-from.html", "India's petrochemical imports: ethylene and propylene chains least import-dependent"),
           (f"{B}/2026/08/the-barrel-really-is-shifting-indias.html", "Indian refiners' petrochemical shift: measured by a Petrochemical Intensity Index"),
           (f"{B}/2026/09/five-years-and-25000-crore-later-china.html", "India's drug ingredient imports: 73.71% from China after Rs 25,000 crore of schemes"),
           (f"{B}/2026/10/indias-approved-solar-cell-makers-can.html", "India's approved solar-cell list: 37.8 GW a year, rooftop exemption ends 31 December")]
build("Trade &middot; Industry", TITLE, "DPIIT's list of 100 heavily imported items meets a PVC market where capacity covers 39% of demand, China supplies 45% of imports and a six-month price floor runs to January 2027.", body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE))
