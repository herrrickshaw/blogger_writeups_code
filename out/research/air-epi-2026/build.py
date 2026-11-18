"""India's air: EPI 2026 rank, Delhi's 15 Nov PM2.5 sources, solar output lost to aerosols, NCAP progress.
Build from the repo root:  python3 out/research/air-epi-2026/build.py   (writes out/post-india-epi-2026-air-quality-solar-output-nov-2026.html). Analysed 18 November 2026."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-epi-2026-air-quality-solar-output-nov-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- EPI 2026 (Yale/Columbia, epi.yale.edu) ----
EPI = [("Estonia (rank 1)", 74.79), ("South Asia average", 31.81), ("Bangladesh (175)", 23.46), ("India (176)", 22.46), ("Laos (177)", 21.78)]
assert round(74.79 - 22.46, 2) == 52.33 and round(31.81 - 22.46, 2) == 9.35
IN = {"Overall EPI": (176, 22.46), "Environmental health": (174, 15.13), "Air quality": (175, 7.89), "Ecosystem vitality": (171, None), "Climate change": (130, None), "Air pollution (emissions)": (88, 51.99)}
# ---- Delhi, 15 Nov 2026, PM2.5 source apportionment (TNIE: AQEWS and IDSS) ----
SRC = [("Biomass burning", 37.1), ("Secondary organic aerosols", 22.0), ("Vehicles", 17.2), ("Secondary inorganic aerosols", 9.6), ("Waste burning", 5.5), ("Mixed combustion", 4.3),
       ("Mineral dust and ash", 2.0), ("Firecrackers", 1.6), ("Industry", 0.6)]
assert abs(sum(v for _, v in SRC) - 99.9) < 0.05
assert round(37.1 + 5.5 + 4.3, 1) == 46.9
AQI_15NOV, STATIONS, POOR, VPOOR = 290, 58, 34, 23
assert POOR + VPOOR + 1 == STATIONS
# ---- Solar (The Hindu, 28 May 2026): aerosols cut solar output 9.6% in 2023, about 15 TWh ----
LOSS_PCT, LOSS_TWH = 9.6, 15
IMPLIED_UNAFFECTED = LOSS_TWH / (LOSS_PCT / 100)
assert round(IMPLIED_UNAFFECTED) == 156 and round(IMPLIED_UNAFFECTED - LOSS_TWH) == 141
# ---- Costs and exposure ----
COST_BN, COST_PCT = 260, 6                                          # Dalberg-Clean Air Fund, 2024
DEATHS_LAKH = 20                                                    # State of Global Air 2025, 2023 (more than)
CITIES, OVER_WHO, OVER_NAT = 267, 261, 38                           # CREA October 2026
assert round(100 * OVER_WHO / CITIES) == 98 and round(100 * OVER_NAT / CITIES) == 14
NCAP, LOWER, BIG = 130, 108, 26
assert NCAP - LOWER == 22 and round(100 * LOWER / NCAP) == 83 and round(100 * BIG / NCAP) == 20

TITLE = "India's air: EPI rank 176 of 177, 9.6% of solar output lost, Delhi AQI 290"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    ("176 of 177", " is India's rank in the 2026 Environmental Performance Index, with 175th in air quality; Laos is last and Bangladesh is 175th."),
    ("37.1%", " of Delhi's PM2.5 on 15 November came from biomass burning (stubble, dung cakes, wood), with the AQI at 290; firecrackers contributed 1.6%."),
    ("9.6%", " of India's solar output, about 15 terawatt-hours, was lost to aerosols in 2023; CREA found 261 of 267 cities above the WHO daily guideline in October 2026."),
])

s1 = insight(
    "India scores 22.46 of 100 in the 2026 EPI, 9.35 below the South Asia average",
    bars("India ranks 176th of 177 at 22.46, ahead of only Laos at 21.78",
         EPI, accent="India (176)", unit=" points", fmt=lambda v: f"{v:.2f}",
         sub="Environmental Performance Index 2026 score, 0 to 100; 177 countries, 47 indicators. India was 176th of 180 in 2024 and last in 2022.",
         source="Yale Center for Environmental Law and Policy and Columbia CIESIN, EPI 2026 (epi.yale.edu), country page for India.")
    + numbers(["Category", "India rank", "India score"],
              [[k, str(r), f"{sc:.2f}" if sc is not None else "&ndash;"] for k, (r, sc) in IN.items()] + [["Improvement over ten years", "&ndash;", "+7.47"]]),
    "India ranks 175th on air quality, which measures health burden, but 88th on air pollution, which tracks emission trends, so the index penalises exposure and illness more than emissions.",
    "The Ministry of Environment should publish the exposure data behind its objection to the index, since it rejected the 2022 ranking as based on unscientific methods and has not supplied a rival measure.",
    "epi")

s2 = insight(
    "On 15 November biomass burning was 37.1% of Delhi's PM2.5; firecrackers 1.6%",
    bars("Delhi's PM2.5 on 15 November: biomass burning 37.1%, vehicles 17.2%, industry 0.6%",
         SRC, accent="Biomass burning", unit="%",
         sub="Real-time source apportionment of PM2.5 at an AQI of 290 ('poor'); of 58 stations, 34 were poor, 23 very poor and one moderate.",
         source="New Indian Express, 16 November 2026, citing the Air Quality Early Warning System and the Integrated Decision Support System.")
    + numbers(["Fact", "Value"],
              [["AQI, 4 pm 15 November", "290; very poor from 11 November, near severe at times"], ["Worst station", "NSIT Dwarka, 364"], ["Biomass, waste and mixed combustion together", "46.9%"],
               ["Cloud seeding", "proposed again as an emergency measure (Drishti IAS, 12 November)"], ["Pusa decomposer", "ICAR microbial spray for stubble, 15 to 20 days (Drishti IAS)"]]),
    "A single day&rsquo;s apportionment is a snapshot, but burning of biomass, waste and mixed fuels adds to 46.9% against 17.2% for vehicles and 1.6% for firecrackers, which points the measures at fields and households.",
    "The Commission for Air Quality Management should publish the daily apportionment for Delhi and its neighbours on a standing page, so a day&rsquo;s figure can be read against the season.",
    "delhi")

s3 = insight(
    "Aerosols cut India's solar output by 9.6% in 2023, about 15 terawatt-hours",
    bars("About 141 of 156 terawatt-hours that clean air would have given reached the grid in 2023",
         [("Implied output without the aerosol loss", round(IMPLIED_UNAFFECTED)), ("Implied actual output", round(IMPLIED_UNAFFECTED - LOSS_TWH)), ("Loss to aerosols", LOSS_TWH)],
         accent="Loss to aerosols", unit=" TWh",
         sub="Terawatt-hours. The 15 TWh and 9.6% are reported; the totals are back-calculated here from them and are not figures in the study.",
         source="The Hindu, 28 May 2026, on a Nature Sustainability analysis; calculation by this blog.")
    + numbers(["Estimate", "Value", "Source"],
              [["Solar output lost to aerosols, 2023", "9.6%, about 15 TWh", "Nature Sustainability via The Hindu"], ["Cost of air pollution, 2024", "about $260 billion, about 6% of GDP", "Dalberg Advisors and Clean Air Fund via Drishti IAS"],
               ["Deaths attributed, 2023", "more than 20 lakh", "State of Global Air 2025 via Drishti IAS"]]),
    "A 9.6% loss of solar output is about 15 TWh, so the study treats polluted air as a cost to the power system as well as to health.",
    "The Ministry of New and Renewable Energy should publish the soiling and aerosol loss for its large solar parks each month, so that cleaning costs and output losses can be set against the cost of cleaner air.",
    "solar")

s4 = insight(
    "In October 2026, 261 of 267 cities broke the WHO guideline and 38 the national limit",
    bars("261 of 267 cities topped the WHO daily PM2.5 guideline in October 2026; 38 topped India's",
         [("Cities monitored", CITIES), ("Above the WHO daily guideline of 15 micrograms", OVER_WHO), ("Above India's daily standard of 60 micrograms", OVER_NAT)],
         accent="Above India's daily standard of 60 micrograms", unit=" cities",
         sub="Number of cities with a monthly PM2.5 above each level, October 2026. In 2025-26, 108 of 130 NCAP cities had lower annual PM10 than in 2017-18.",
         source="CREA, October 2026 report, via Drishti IAS, 14 November 2026.")
    + numbers(["Measure", "Value"],
              [["NCAP cities with lower PM10 than 2017-18", "108 of 130 (83%)"], ["NCAP cities with reductions above 40%", "26 (20%)"], ["NCAP cities without a fall", "22 by subtraction"],
               ["PM10 against PM2.5", "falling dust does not mean falling fine particles; PM2.5 forms from SO2 and NOx"]]),
    "A city can meet the national standard of 60 micrograms and still exceed the WHO guideline of 15 by a factor of four, which is why 38 cities breaching India&rsquo;s limit understates how many breathe air above the health guideline.",
    "The Central Pollution Control Board should publish city-wise PM2.5 against both the national standard and the WHO guideline each month on one page.",
    "cities")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Commission for Air Quality Management:</b> publish daily source apportionment for Delhi and neighbouring districts on a standing page.</li>
<li><b>Central Pollution Control Board:</b> publish monthly city PM2.5 against the national standard and the WHO guideline.</li>
<li><b>Ministry of New and Renewable Energy:</b> publish monthly aerosol and soiling losses for large solar parks.</li>
<li><b>Ministry of Environment:</b> publish the data behind any objection to the EPI.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''
method = '''<details class="xv-n"><summary>Method and definitions</summary><ul>
<li>The EPI scores each country from 0 to 100 on 47 indicators in three objectives: environmental health (25% of the score), ecosystem vitality (45%) and climate change (30%).</li>
<li>PM2.5 is fine particulate matter under 2.5 micrometres; AQI bands: 201 to 300 poor, 301 to 400 very poor, 401 to 500 severe.</li>
<li>Implied solar output is 15 TWh divided by 9.6%; it is not a figure in the study.</li></ul></details>
'''
gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary><ul>
<li>The 2023 solar output total used in the study; the totals here are back-calculated.</li>
<li>How representative 15 November is: the apportionment is a single day at an AQI of 290.</li>
<li>The CREA, Dalberg and State of Global Air figures were read through Drishti IAS, not from the reports.</li>
<li>Ecosystem vitality and climate-change scores for India; only ranks were read.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps
SOURCES = ('<a href="https://epi.yale.edu/2026/results/country/IND">EPI 2026, India country page</a>; <a href="https://epi.yale.edu/indicator/2026/EPI">EPI 2026 ranking table</a>; '
  '<a href="https://thewire.in/environment/india-second-from-lowest-in-environment-performance-index">The Wire, 11 July 2026</a> (category ranks); '
  '<a href="https://www.newindianexpress.com/cities/delhi/2026/Nov/16/air-quality-improves-in-delhi-iit-chokes-at-428">New Indian Express, 16 November 2026</a> (Delhi apportionment); '
  '<a href="https://www.thehindu.com/sci-tech/science/air-pollution-cut-india-solar-power-output-one-tenth-2023-study/article71028944.ece">The Hindu, 28 May 2026</a> (solar); '
  '<a href="https://www.drishtiias.com/daily-updates/daily-news-analysis/balancing-economic-growth-and-air-quality-in-india">Drishti IAS, 14 November 2026</a> (CREA, Dalberg, NCAP, State of Global Air); '
  '<a href="https://www.drishtiias.com/current-affairs-news-analysis-editorials/news-analysis/12-11-2026">Drishti IAS, 12 November 2026</a>. Shares computed by this blog. Analysed 18 November 2026.')
RELATED = [(f"{B}/2026/09/delhis-smog-towers-failed-test-44-year.html", "Delhi's smog towers and purifiers: almost no measured effect at city scale"),
           (f"{B}/2026/08/rooftop-solar-is-working-household.html", "Rooftop solar in India: over 12 GW by May 2026, household batteries unsubsidised"),
           (f"{B}/2026/09/the-solar-panel-recycling-opportunity.html", "Solar panel recycling in India: both recycling pathways lose money per tonne")]
build("Environment &middot; Energy", TITLE, "India ranks 176th of 177 in the 2026 EPI, aerosols cost 9.6% of solar output in 2023, and biomass burning was 37.1% of Delhi's PM2.5 on 15 November.", body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE))
