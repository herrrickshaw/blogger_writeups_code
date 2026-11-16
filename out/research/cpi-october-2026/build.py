"""India's CPI for October 2026 (base 2024=100): the 6.09% reading, what is inside it, and the RBI's next meeting.
Build from the repo root:  python3 out/research/cpi-october-2026/build.py   (writes out/post-india-retail-inflation-october-2026.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 16 November 2026."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-retail-inflation-october-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- MoSPI / NSO press release of CPI (base 2024=100) for October 2026, dated 12 November 2026 (provisional) ----
# https://www.mospi.gov.in/uploads/latestreleasesfiles/1794480048335-Press%20Release%20of%20CPI%20for%20October%202026%20.pdf  (read 16 Nov 2026)
# Annexure IV, all-India combined CPI inflation, per cent. The series starts in January 2026 (2025 indices are published without inflation rates).
CPI = [("January", 2.74), ("February", 3.21), ("March", 3.40), ("April", 3.48), ("May", 3.93), ("June", 4.38),
       ("July", 4.45), ("August", 4.83), ("September", 5.54), ("October", 6.09)]
CPI_RURAL_OCT, CPI_URBAN_OCT, CPI_RURAL_SEP, CPI_URBAN_SEP = 6.63, 5.41, 6.08, 4.88
CFPI_OCT, CFPI_SEP = 8.94, 7.74                                    # consumer food price index, combined
assert [v for _, v in CPI] == sorted(v for _, v in CPI)           # a rise in every month
assert round(CPI[-1][1] - CPI[0][1], 2) == 3.35
assert round(CFPI_OCT - CFPI_SEP, 2) == 1.20 and round(CPI_RURAL_OCT - CPI_URBAN_OCT, 2) == 1.22
RBI_CEILING = 6.0

# Annexure I, division-wise combined inflation, October 2026 (weight in per cent of the basket)
DIV = [("Personal care and miscellaneous", 5.04, 10.14), ("Restaurants and accommodation", 3.35, 10.06), ("Food and beverages", 36.75, 8.51),
       ("Transport", 8.80, 5.84), ("Clothing and footwear", 6.38, 4.96), ("Paan, tobacco and intoxicants", 2.99, 4.93),
       ("Education services", 3.33, 4.02), ("Furnishings and household equipment", 4.47, 3.94), ("Information and communication", 3.61, 3.16),
       ("Housing, water, electricity, gas and fuels", 17.66, 2.90), ("Recreation, sport and culture", 1.52, 2.52), ("Health", 6.10, 2.05)]
assert round(sum(w for _, w, _ in DIV), 2) == 100.00 - 0.0 or round(sum(w for _, w, _ in DIV), 2) == 100.0   # all twelve divisions listed

assert sum(1 for n,w,i in DIV if n!='Food and beverages' and i>=3.9)==7
# Page 3-4, key items (weight, September inflation, October inflation)
HIGH = [("Onion", 0.7006, 108.13, 116.22), ("Garlic", 0.3738, 54.62, 60.74), ("Silver jewellery", 0.3127, 87.82, 52.39),
        ("Ginger", 0.2556, 62.85, 48.32), ("Lemon", 0.1367, 36.41, 47.30)]
LOW = [("Potato", 0.7549, -11.52, -14.24), ("Cauliflower", 0.2330, -2.88, -10.57), ("Coconut", 0.1931, -3.99, -5.60),
       ("Brinjal", 0.2912, 2.21, -3.34), ("Cabbage", 0.1518, 5.58, -1.92)]
W_HIGH = sum(w for _, w, _, _ in HIGH)
assert round(W_HIGH, 4) == 1.7794
CONTRIB = sum(w * i / 100 for _, w, _, i in HIGH)                   # weight x inflation, a rough points contribution (see method note)
assert round(CONTRIB, 2) == 1.39
ONION_CONTRIB = HIGH[0][1] * HIGH[0][3] / 100
assert round(ONION_CONTRIB, 2) == 0.81

# Annexure III, state combined inflation and weights; the release's own chart lists the five highest among states above 50 lakh people
ST = {"Tamil Nadu": (8.00, 7.29), "Telangana": (4.14, 7.26), "Andhra Pradesh": (4.32, 7.25), "Madhya Pradesh": (4.70, 7.19), "Odisha": (2.55, 7.17),
      "Karnataka": (6.29, 7.07), "Uttar Pradesh": (12.53, 6.47), "Kerala": (4.37, 6.22), "Rajasthan": (5.84, 5.89), "Maharashtra": (10.59, 5.85),
      "Gujarat": (5.31, 5.71), "Bihar": (6.37, 5.71), "Punjab": (2.87, 5.60), "West Bengal": (6.50, 4.66), "Assam": (2.07, 4.59),
      "Haryana": (3.12, 4.38), "NCT of Delhi": (2.29, 3.80)}
TOP5 = ["Tamil Nadu", "Telangana", "Andhra Pradesh", "Madhya Pradesh", "Odisha"]
assert [ST[s][1] for s in TOP5] == [7.29, 7.26, 7.25, 7.19, 7.17]                  # the release's five values, in its order
assert all(ST[s][1] < 7.17 for s in ST if s not in TOP5)
assert min(v for _, v in ST.values()) == 3.80                                       # Delhi is the lowest of these larger states
W_TOP5 = sum(ST[s][0] for s in TOP5)
assert round(W_TOP5, 2) == 23.71

# ---- RBI ----
# RBI Bulletin (https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24516) and The Economic Times, 13 Nov 2026: MPC of 5-7 Oct 2026 raised the repo rate
# by 25 bp to 5.50%, stance changed from neutral to calibrated tightening, FY2026-27 CPI projection 5.2%, real GDP 7.1%.
# MLQ.ai and Business Standard poll, 12 Nov 2026: next MPC 2-4 December; DBS and CareEdge expect a second 25 bp rise (forecasts, not decisions).
# MoSPI release: November CPI due 14 December 2026.
REPO, RBI_PROJ = 5.50, 5.2
FYTD = [v for m, v in CPI if m in ("April", "May", "June", "July", "August", "September", "October")]
assert len(FYTD) == 7
IMPLIED = (RBI_PROJ * 12 - sum(FYTD)) / 5                                          # simple average of monthly rates needed for November to March
assert round(IMPLIED, 1) == 5.9

TITLE = "India's retail inflation: 6.09% in October 2026, above the RBI's 6% upper limit"
assert 55 <= len(TITLE) <= 80, len(TITLE)

top = top_line([
    ("6.09%", f" was India&rsquo;s retail inflation in October 2026, up from 5.54% in September and 0.09 points above the RBI&rsquo;s 6% upper limit; it has risen in every month since January&rsquo;s 2.74%."),
    ("116.22%", f" was onion inflation, with garlic at 60.74% and ginger at 48.32%; the five fastest-rising items weigh {W_HIGH:.2f}% of the basket and add roughly {CONTRIB:.1f} points on a weight-times-inflation estimate."),
    ("5.94%", f" would be the average monthly rate for November to March if the RBI&rsquo;s October projection of {RBI_PROJ}% for 2026-27 holds (a simple average, computed here); the next MPC meets on 2&ndash;4 December."),
])
assert round(IMPLIED, 2) == 5.94

s1 = insight(
    "Retail inflation rose in each month of 2026: 2.74% in January, 6.09% in October",
    bars("Retail inflation rose each month in 2026 and passed the RBI&rsquo;s 6% limit in October",
         [(m, v) for m, v in CPI], accent="October", unit="%", ref=(RBI_CEILING, "RBI upper tolerance limit, 6%"),
         sub="Year-on-year change in the all-India combined CPI, per cent, base 2024=100. October is provisional.",
         source="MoSPI, press release of 12 November 2026, Annexure IV.")
    + numbers(["Item", "Value", "Source"],
              [["October against September", f"+{CPI[-1][1] - CPI[-2][1]:.2f} points (5.54% to 6.09%)", "Computed from MoSPI Annexure IV"],
               ["Rural and urban, October", f"{CPI_RURAL_OCT}% and {CPI_URBAN_OCT}% (September {CPI_RURAL_SEP}% and {CPI_URBAN_SEP}%)", "MoSPI, key statistics"],
               ["Repo rate", f"{REPO}% after a 25 basis point rise at the 5&ndash;7 October meeting", "RBI Bulletin; Economic Times, 13 November 2026"],
               ["RBI projection, 2026-27", f"CPI {RBI_PROJ}%, real GDP 7.1%", "RBI MPC, October 2026"],
               ["Implied November&ndash;March average", f"about {IMPLIED:.2f}% (({RBI_PROJ} x 12 &minus; {sum(FYTD):.2f}) / 5)", "Computed here; a simple average of monthly rates, so approximate"]]),
    "October is the highest of the ten monthly readings published on the 2024-based series, and the RBI&rsquo;s own projection of 5.2% for the year implies about 5.9% a month for the remaining five months, so the path from here depends on whether October is the peak.",
    "Readers tracking rates should watch the 2&ndash;4 December MPC decision and the 14 December release of November CPI, the two dates that show whether the October reading is a peak.",
    "trend")

s2 = insight(
    "Onion inflation is 116%: five items weigh 1.78% of the basket, and five are falling",
    bars("Onion prices rose 116% in a year; potato and cauliflower prices fell",
         [(n, i, f"weight {w:.2f}%") for n, w, _, i in HIGH] + [(n, i, f"weight {w:.2f}%") for n, w, _, i in LOW[:3]],
         accent="Onion", unit="%",
         sub="Year-on-year change in the item index, October 2026, per cent. Items are the MoSPI release&rsquo;s own five highest and lowest; brinjal and cabbage (also falling) are in the table.",
         source="MoSPI, press release of 12 November 2026, key items.")
    + numbers(["Item", "Weight in basket (%)", "September inflation (%)", "October inflation (%)"],
              [[n, f"{w:.4f}", f"{s:.2f}", f"{i:.2f}"] for n, w, s, i in HIGH + LOW]),
    f"Onion, garlic, silver jewellery, ginger and lemon together weigh {W_HIGH:.2f}% of the basket, and weight times inflation puts their contribution at roughly {CONTRIB:.1f} of the 6.09 points (onion alone about {ONION_CONTRIB:.1f}), a rough estimate that ignores differences in base prices.",
    "The Department of Consumer Affairs should publish onion buffer stock and release dates alongside its price bulletin, because depleted stored stock and uneven rain, which press reports cite for the largest single item, are supply questions that stock data can answer.",
    "items")

s3 = insight(
    "Restaurants and personal care are above 10%, so prices rose beyond raw food",
    bars("Restaurants and personal care ran above 10%; housing and health stayed under 3%",
         [(n, i, f"weight {w:.2f}%") for n, w, i in DIV], accent="Food and beverages", unit="%",
         ref=(6.09, "all-India CPI inflation, 6.09%"),
         sub="Year-on-year inflation by CPI division, October 2026, combined rural and urban, per cent; weight is the share of the basket.",
         source="MoSPI, press release of 12 November 2026, Annexure I.")
    + numbers(["Division", "Weight (%)", "Inflation, October (%)"], [[n, f"{w:.2f}", f"{i:.2f}"] for n, w, i in DIV]),
    "Food and beverages carry 36.75% of the basket at 8.51%, while seven of the other eleven divisions are also at or above 3.9%, which fits the RBI&rsquo;s October note of early signs of inflation generalisation.",
    "MoSPI should add a contribution-to-inflation table by division and item to each monthly release, so the share of food, services and fuel in the headline can be read directly instead of estimated.",
    "divisions")

s4 = insight(
    "Five states are above 7.1%, led by Tamil Nadu at 7.29% and Telangana at 7.26%",
    bars("Five states are at 7.17% to 7.29% and Delhi at 3.80%, against 6.09% for India",
         [(s, ST[s][1], f"weight {ST[s][0]:.2f}%") for s in TOP5] + [("Uttar Pradesh", ST["Uttar Pradesh"][1], "weight 12.53%"),
          ("Maharashtra", ST["Maharashtra"][1], "weight 10.59%"), ("West Bengal", ST["West Bengal"][1], "weight 6.50%"), ("NCT of Delhi", ST["NCT of Delhi"][1], "weight 2.29%")],
         accent=TOP5, unit="%", ref=(6.09, "all-India CPI inflation, 6.09%"),
         sub="Combined rural and urban CPI inflation, October 2026, per cent. The five states are those the release lists as highest among states above 50 lakh people; the others shown are the two largest by weight and the two lowest.",
         source="MoSPI, press release of 12 November 2026, Annexure III; the order of the five follows the release&rsquo;s chart values.")
    + numbers(["Measure", "Value"],
              [["Rural and urban inflation, October", f"{CPI_RURAL_OCT}% and {CPI_URBAN_OCT}%"],
               ["Combined weight of the five states", f"{W_TOP5:.2f}% of the all-India basket"],
               ["Delhi, lowest of the larger states in Annexure III", "3.80%"]]),
    f"The five states above 7.1% carry {W_TOP5:.2f}% of the all-India weight, and rural inflation of {CPI_RURAL_OCT}% exceeds urban {CPI_URBAN_OCT}% by 1.22 points, so the pressure is strongest in rural areas and in five southern, central and eastern states.",
    "State governments with the highest readings should publish their own onion and vegetable procurement and release plans before the November data on 14 December.",
    "states")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>MoSPI:</b> publish each item&rsquo;s and division&rsquo;s contribution to headline inflation with every monthly release, with the method and the base-price adjustment stated.</li>
<li><b>Department of Consumer Affairs:</b> publish onion buffer-stock quantities, release dates and prices with its daily price bulletin during the lean months.</li>
<li><b>Reserve Bank of India:</b> publish the monthly path behind its 2026-27 projection in the December policy statement, so the 5.2% can be compared with the readings after October.</li>
<li><b>MoSPI:</b> state in each release which items have thin price quotations in the state-level tables, since the release itself warns that some state item indices use thin samples.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>All CPI figures are from MoSPI&rsquo;s press release of 12 November 2026 (base 2024=100, provisional for October). Inflation is the year-on-year change in the index.</li>
<li>The contribution estimates use weight times October inflation divided by 100. They treat each weight as the item&rsquo;s share a year ago, which is only approximately true when relative prices have moved, so they are rough points, not MoSPI figures.</li>
<li>The implied November-to-March average is the RBI&rsquo;s 5.2% projection times 12, less the sum of the seven April-to-October readings, divided by five. It treats the projection as a simple average of monthly rates; the RBI made the projection before the October reading.</li>
<li>Press reports compare October&rsquo;s 6.09% with 6.21% in October 2024. That earlier figure is from the old 2012-based series and is not on the same base; the 2024-based series publishes inflation rates only from January 2026.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The causes. The RBI Bulletin lists a deficient monsoon, El Ni&ntilde;o conditions and high energy prices; the release gives item and division rates, not a decomposition. Trade-press reports of depleted onion stocks and uneven rain are not tested here.</li>
<li>Item contributions in MoSPI&rsquo;s own terms: the release does not publish them, so the 1.4 points and 0.8 points are this blog&rsquo;s approximations.</li>
<li>Whether October is the peak. November data is due on 14 December; the repo-rate decision is due after the 2&ndash;4 December meeting. Economists&rsquo; expectations of a second rise (DBS, CareEdge) are forecasts, not decisions.</li>
<li>State rankings below the top five and above the lowest: Annexure III is listed in full in the release, but only the chart values for the top five are given by the release itself.</li>
<li>October values are provisional and are revised the following month.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://www.mospi.gov.in/uploads/latestreleasesfiles/1794480048335-Press%20Release%20of%20CPI%20for%20October%202026%20.pdf">MoSPI, Press release of Consumer Price Index (base 2024=100) for October 2026, 12 November 2026</a> (all CPI figures; Annexures I to IV); '
    '<a href="https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24516">RBI Bulletin</a> (October 2026 MPC resolution: repo rate, stance, growth and inflation projections, drivers); '
    '<a href="https://economictimes.indiatimes.com/news/economy/foreign-trade/indias-october-merchandise-trade-deficit-rises-to-one-year-high-of-39-88-billion-as-imports-surge/articleshow/135792320.cms">The Economic Times, 13 November 2026</a> (RBI projections as restated); '
    '<a href="https://www.thehindu.com/business/Economy/retail-inflation-crosses-rbis-upper-limit-for-first-time-in-two-years-comes-in-at-61-in-october-2026/article71693503.ece">The Hindu, 12 November 2026</a> and '
    '<a href="https://www.thehindubusinessline.com/economy/indias-retail-inflation-rises-to-609-in-october-breaches-rbis-upper-tolerance-limit/article71693402.ece">The Hindu BusinessLine, 12 November 2026</a> (comparison with October 2024 on the old series); '
    '<a href="https://www.cnbctv18.com/economy/india-october-cpi-inflation-breaches-rbi-upper-limit-rises-to-6-09-pc-food-inflation-20032597.htm">CNBC TV18, 12 November 2026</a> (poll estimate; next MPC); '
    '<a href="https://mlq.ai/news/indias-retail-inflation-breaks-the-rbis-6-ceiling-in-october-as-food-inflation-nears-9">MLQ.ai, 12 November 2026</a> (secondary: Business Standard poll; MPC dates 2&ndash;4 December; economists&rsquo; expectations). '
    'Percentages, contributions and the implied average computed by this blog. Analysed 16 November 2026.')

RELATED = [
    (f"{B}/2026/08/cpi-inflation-heatmap-india-june-2026.html", "CPI inflation heatmap for India, June 2026: 13 of 28 states, a 3.4-point spread"),
    (f"{B}/2026/08/the-price-and-tap-two-levers-behind.html", "RBI's rate lever: a corridor around the repo rate, targeting the call rate"),
    (f"{B}/2026/08/inflation-trends-globally-what-five.html", "G20 prices since 2020: 100 became 103.5 in China and about 1,900 in Argentina"),
    (f"{B}/2026/08/imported-fertiliser-fuel-prices-diesel.html", "Imported fertiliser and fuel prices in India: diesel, CPI and WPI, FY2012–FY2026"),
]

build("Prices &middot; Inflation", TITLE,
      "MoSPI&rsquo;s October release puts retail inflation at 6.09%, the first reading above the RBI&rsquo;s 6% limit in the 2024-based series; onions, restaurants and five states lead, and the RBI meets on 2&ndash;4 December.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
