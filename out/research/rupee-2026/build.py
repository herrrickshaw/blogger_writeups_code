"""India's rupee in October-November 2026: the rebound from the early-October low, reserves, the RBI forward book and the forecasts.
Build from the repo root:  python3 out/research/rupee-2026/build.py   (writes out/post-india-rupee-rebound-reserves-forward-book-november-2026.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 16 November 2026."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-rupee-rebound-reserves-forward-book-november-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- Spot rupee, Rs per US dollar ----
# The Hindu BusinessLine, 11 Nov 2026: closed at 93.69 on Wednesday 11 Nov, up 24 paise on 93.93 (intraday 93.62-93.87); HDFC Securities cites "the absence of central bank intervention".
# ABC Live weekly forex report, 11 Nov 2026 (secondary; RBI and Reuters data): close 3 Nov 94.74; 9 Nov close 93.9275 after an intraday 93.69 and dollar buying by state-run banks that traders
#   linked to the RBI (no official figure); FBIL reference rates 5 Nov 94.3996, 6 Nov 94.1402, 9 Nov 93.8579.
# Financial Express, 9 Nov 2026 (Anand Rathi): early-October low of around 96.80 (a single source); the rupee "gained nearly 3.25%" from it.
# Reuters poll of 37 strategists, 2-4 Nov 2026: with spot near 94.70, median 96.00 at end-January and 96.33 at end-April.
LOW_OCT, C3NOV, C9NOV, C11NOV = 96.80, 94.74, 93.93, 93.69
GAIN_DOLLAR_COST = 100 * (LOW_OCT - C11NOV) / LOW_OCT          # fall in rupees needed to buy a dollar
GAIN_RUPEE = 100 * (LOW_OCT / C11NOV - 1)                       # rise in the rupee's dollar value
assert round(GAIN_DOLLAR_COST, 1) == 3.2 and round(GAIN_RUPEE, 1) == 3.3
assert round(C3NOV - C11NOV, 2) == 1.05

# ---- Reserves, US$ billion (RBI weekly statistical supplement) ----
# Mint 8 Nov 2026: record $785.71bn in the week to 4 Sep; $717.06bn on 30 Oct ($2.69bn lower on the week; $68.65bn below the peak; $25.95bn above end-March 2026).
# PTI / Business Standard, 13 Nov 2026: $719.547bn in the week to 6 Nov (+$2.49bn), gold +$2.205bn to $104.796bn.
PEAK, OCT30, OCT23, NOV6 = 785.706, 717.056, 719.75, 719.547
MAR26 = OCT30 - 25.95
assert round(PEAK - OCT30, 2) == 68.65 and round(OCT30 - OCT23, 2) == -2.69 and round(NOV6 - OCT30, 2) == 2.49
assert round(MAR26, 2) == 691.11
COMP = [("Foreign-currency assets", 591.118), ("Gold", 102.591), ("Special drawing rights", 18.558), ("IMF reserve position", 4.790)]
assert abs(sum(v for _, v in COMP) - OCT30) < 0.01
PEAK_TO_NOV6 = PEAK - NOV6
assert round(PEAK_TO_NOV6, 1) == 66.2

# ---- RBI forward book and swap windows (IDFC First Bank Economic Research, 9 Nov 2026, as reported by PTI / Business Standard) ----
# Net short forward dollar position $239bn at end-September 2026 (ABC Live: $239.2bn); about $40bn matures within a year, $56bn in 1-3 years, $143bn in 3-5 years, the
# longer maturities mostly tied to the FCNR(B) scheme. Swap windows (FCNR(B), external commercial borrowing, overseas foreign-currency borrowing) drew $150bn cumulatively;
# balance of payments tracking a $65bn surplus in H1 FY27, an underlying deficit of $85bn without the windows. Import cover of unencumbered reserves about 7 months in October 2026, 10 a year earlier.
LADDER = [("Within 1 year", 40), ("1 to 3 years", 56), ("3 to 5 years", 143)]
assert sum(v for _, v in LADDER) == 239
BOP, WINDOWS = 65, 150
assert BOP - WINDOWS == -85

# ---- Flows and outlook ----
# Financial Express, 9 Nov (Anand Rathi): about $30bn of foreign portfolio equity outflow in 2026 through 6 Nov, about $5bn net inflow in November so far; USD/INR range 93.50-95.50 in
#   December, 65-70% chance of a year-end close above 94. Elara Capital: 93.0-95.0. IDFC First: 92-94 by December, 94-95 by March 2027, 96 by June 2027.
# The Hindu BusinessLine, 11 Nov: Axis Bank keeps 100 by June 2027. Commerce Ministry via The Hindu BusinessLine, 13 Nov: October goods deficit $39.88bn, a one-year high.
FORECAST = [("Spot, 11 November 2026", C11NOV), ("IDFC First, March 2027 (94 to 95)", 94.5), ("Reuters poll median, end-April 2027", 96.33),
            ("IDFC First, June 2027", 96.0), ("Axis Bank, June 2027", 100.0)]

TITLE = "India's rupee: Rs 93.69 a dollar on 11 November, 3% above its early-October low"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    ("Rs 93.69", f" a dollar was the rupee&rsquo;s close on 11 November, about {GAIN_RUPEE:.0f}% stronger than the early-October low of around Rs 96.80 (one source); the 4 November Reuters poll expected Rs 96.00 by January."),
    ("$68.65 billion", f" is how far reserves fell from the 4 September record to $717.06 billion on 30 October; they were $719.55 billion on 6 November, and the fall mixes dollar sales, FCNR(B) deployment and valuation."),
    ("$239 billion", " is the RBI&rsquo;s net short forward dollar position at the end of September, $143 billion of it due in three to five years; it must buy dollars as inflows return, which limits how far the rupee can rise."),
])

s1 = insight(
    "The rupee rose from about 96.80 per dollar in early October to 93.69 on 11 November",
    bars("The rupee gained about 3% from its early-October low, helped by cheaper crude and inflows",
         [("Early October low (one source)", LOW_OCT), ("3 November, close", C3NOV), ("9 November, close", C9NOV), ("11 November, close", C11NOV)],
         accent="11 November, close", unit=" Rs/$", fmt=lambda v: f"Rs {v:.2f}",
         sub="Rupees needed to buy one US dollar; a lower value is a stronger rupee.",
         source="The Hindu BusinessLine, 11 November 2026; ABC Live, 11 November 2026; Financial Express, 9 November 2026 (Anand Rathi).")
    + numbers(["Measure", "Value", "Source"],
              [["Gain from the low", f"{GAIN_DOLLAR_COST:.1f}% fewer rupees per dollar; the rupee is {GAIN_RUPEE:.1f}% stronger in dollar terms", "Computed here; Financial Express says nearly 3.25%"],
               ["FBIL reference rate", "5 November 94.3996; 6 November 94.1402; 9 November 93.8579", "ABC Live (secondary), citing the RBI"],
               ["Drivers cited", "cheaper crude, foreign portfolio inflows, a risk-on mood; HDFC Securities: no central bank intervention", "The Hindu BusinessLine, 11 November"],
               ["Counter-view", "dollar buying by state-run banks on 9 November that traders linked to the RBI; no official amount", "ABC Live, citing Reuters"],
               ["Goods deficit, October", "$39.88 billion, a one-year high", "Commerce Ministry via The Hindu BusinessLine, 13 November"]]),
    "The rupee needed 1.05 fewer rupees per dollar between 3 and 11 November, and the sources disagree on whether the RBI bought dollars on the way, so how much of the move is flows and how much is central-bank management is not shown by the closing rates.",
    "The RBI should publish its spot and forward intervention weekly with a short lag, since market reports of dollar buying by state-run banks cannot be confirmed from reserves data.",
    "spot")

s2 = insight(
    "Reserves fell $68.65 billion from the 4 September record to $717.06 billion on 30 October",
    bars("Reserves fell $68.65 billion from the record, then rose $2.49 billion by 6 November",
         [("End-March 2026 (computed)", round(MAR26, 2)), ("4 September 2026, record", round(PEAK, 2)), ("30 October 2026", round(OCT30, 2)), ("6 November 2026", round(NOV6, 2))],
         accent="6 November 2026", unit=" $ billion",
         sub="Total foreign exchange reserves, US$ billion, weekly RBI data. The end-March value is the 30 October figure less the $25.95 billion rise the report gives.",
         source="RBI weekly statistical supplement, as reported by Mint (8 November 2026) and PTI (13 November 2026).")
    + numbers(["Component, 30 October", "US$ billion", "Weekly change"],
              [["Foreign-currency assets", "591.118", "&minus;2.088"], ["Gold", "102.591", "&minus;0.559 (6 November: +2.205 to 104.796)"],
               ["Special drawing rights", "18.558", "&minus;0.047"], ["IMF reserve position", "4.790", "+0.003"],
               ["Total", "717.056", "&minus;2.691"]]),
    f"Reserves are still $25.95 billion above end-March but ${PEAK_TO_NOV6:.1f} billion below the September record, and the weekly change mixes dollar sales, deployment of FCNR(B) funds and valuation, so it does not give an intervention amount.",
    "The RBI should split each weekly reserve change into transactions, valuation and income, so intervention and valuation effects can be read separately.",
    "reserves")

s3 = insight(
    "RBI's net forward dollar short position is $239 billion, $143 billion due in 3 to 5 years",
    bars("The RBI's forward dollar short is $239 billion; $143 billion falls due in 3 to 5 years",
         LADDER, accent="3 to 5 years", unit=" $ billion",
         sub="Net short forward dollar position at the end of September 2026 by time to maturity, US$ billion; the longer buckets are mostly linked to FCNR(B) swaps.",
         source="IDFC First Bank Economic Research, 9 November 2026, as reported by PTI and Business Standard (RBI data).")
    + numbers(["Measure", "Value", "Source"],
              [["Swap-window inflows", f"${WINDOWS} billion since the windows opened (FCNR(B), external commercial borrowing, overseas borrowing)", "IDFC First"],
               ["Balance of payments, H1 FY2026-27", f"tracking a ${BOP} billion surplus; an underlying ${WINDOWS - BOP} billion deficit without the windows", "IDFC First"],
               ["Import cover, unencumbered reserves", "about 7 months in October 2026, 10 a year earlier", "IDFC First"],
               ["Window for oil companies and a reserve for importers", "RBI measures to curb dollar demand, easing spot pressure", "Business Standard, 9 November"]]),
    "Of the $150 billion drawn through swap windows, the balance of payments surplus of $65 billion becomes an $85 billion deficit without it, and the forward short means the RBI must buy dollars as inflows come back, which caps the rupee&rsquo;s rise.",
    "The RBI should publish the forward book by maturity every month, with the FCNR(B)-linked share, so repayment years and reserves can be read together.",
    "forward")

s4 = insight(
    "Forecasts put the rupee at 96 to 100 per dollar by mid-2027; spot is 93.69",
    bars("Forecasts put the rupee at 96 to 100 per dollar by mid-2027; spot was 93.69",
         FORECAST, accent="Spot, 11 November 2026", unit=" Rs/$", fmt=lambda v: f"Rs {v:.2f}",
         sub="Rupees per dollar. IDFC First's March figure is the midpoint of its 94 to 95 range; forecasts are made on different dates and are not outcomes.",
         source="IDFC First Bank (9 November 2026); Reuters poll of 37 strategists (4 November 2026); Axis Bank (The Hindu BusinessLine, 11 November 2026).")
    + numbers(["Forecaster", "Forecast", "Date made"],
              [["IDFC First Bank", "92&ndash;94 by December 2026; 94&ndash;95 by March 2027; 96 by June 2027", "9 November"],
               ["Reuters poll, 37 strategists", "median 96.00 at end-January and 96.33 at end-April 2027", "2&ndash;4 November"],
               ["Axis Bank", "100 by June 2027, citing low forex adequacy and heavy 3&ndash;5 year maturities", "11 November"],
               ["Anand Rathi", "93.50&ndash;95.50 in December; 65&ndash;70% chance of a year-end close above 94", "9 November"],
               ["Elara Capital", "93.0&ndash;95.0 in the near term", "9 November"],
               ["Foreign portfolio equity flows", "about $30 billion of outflow in 2026 to 6 November; about $5 billion net inflow in November so far", "Financial Express (Anand Rathi), 9 November"]]),
    "The short-term range is 93 to 95.5 but every medium-term forecast read is weaker than spot, from 94 to 95 by March to 100 by June, so the rally rests on crude and inflows that the same forecasters expect to fade.",
    "Importers and borrowers should plan hedges on the 96 to 100 range for mid-2027 rather than the 11 November level, since the November rally is the one part of the path no forecaster extrapolates.",
    "forecast")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Reserve Bank of India:</b> publish spot and forward intervention by week, and split reserve changes into transactions, valuation and income.</li>
<li><b>Reserve Bank of India:</b> publish the forward book by maturity each month, with the share tied to FCNR(B) swaps and the repayment years.</li>
<li><b>Ministry of Finance and the RBI:</b> publish a joint table of swap-window inflows and the dates on which the dollars are due, so the repayment years are visible.</li>
<li><b>FBIL:</b> publish the reference-rate series with the time of fixing and the volume behind it, so market closes and official fixes can be compared.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The rupee is quoted in rupees per dollar, so a lower number is a stronger rupee. The gain from the October low is computed two ways: 3.2% fewer rupees per dollar, or 3.3% more dollars per rupee.</li>
<li>Reserves are the RBI&rsquo;s weekly statistical supplement totals; the end-March value is derived from the 30 October total and the reported $25.95 billion rise.</li>
<li>The forward book is the RBI&rsquo;s net short forward position in dollars, from RBI data as summarised by IDFC First Bank; it is a commitment to deliver dollars when buy-sell swaps mature.</li>
<li>Forecast values come from different dates and sources; the chart is not a forecast of this blog.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The early-October low: Rs 96.80 comes from a single analyst quoted by Financial Express; the FBIL series for October was not read.</li>
<li>RBI spot intervention: no official figure; ABC Live reports bank dollar demand that traders linked to the RBI, while HDFC Securities describes no central bank intervention. Both are reports, not data.</li>
<li>Weekly reserve declines: ABC Live calls the 30 October fall an eighth straight weekly decline while Mint calls it the second in a row; this piece does not use either count.</li>
<li>The forward-book and swap-window figures rest on one bank&rsquo;s report summarising RBI data; the RBI&rsquo;s own table was not read.</li>
<li>Portfolio flows: a data site reported large November equity inflows from NSDL, but the figure conflicts with the roughly $5 billion in Financial Express, and is not used.</li>
<li>Rupee levels after 11 November are not covered.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://www.thehindubusinessline.com/markets/forex/rupee-closes-at-seven-month-high-of-9369-as-fpi-inflows-lower-crude-prices-boost-sentiment/article71689839.ece">The Hindu BusinessLine, 11 November 2026</a> (11 November close; drivers; Axis Bank); '
    '<a href="https://abclive.in/2026/11/12/india-forex-reserves-fall">ABC Live weekly forex report, 11 November 2026</a> (closing and FBIL rates; reserves components; secondary); '
    '<a href="https://www.financialexpress.com/policy/economy/rupee-surges-to-6-month-highs-what-controls-its-next-move-experts-list-3-key-triggers/4380278">Financial Express, 9 November 2026</a> (October low; flows; analyst ranges); '
    '<a href="https://www.livemint.com/economy/indias-forex-reserves-fall-2-69-billion-to-717-billion-why-rbi-is-selling-dollars-and-what-it-means-for-the-rupee-11794125996170.html">Mint, 8 November 2026</a> (reserves to 30 October); '
    '<a href="https://www.business-standard.com/finance/news/india-s-forex-reserves-rise-by-2-49-billion-to-719-55-billion-rbi-data-126111301246_1.html">Business Standard (PTI), 13 November 2026</a> (reserves to 6 November); '
    '<a href="https://www.business-standard.com/finance/news/rbi-s-239-bn-forward-dollar-position-to-limit-rupee-gains-report-126110900571_1.html">Business Standard (PTI), 9 November 2026</a> and '
    '<a href="https://www.cnbctv18.com/economy/rbi-usd-239-billion-forward-dollar-position-to-limit-rupee-gains-despite-fpi-inflows-report-20030513.htm">CNBC TV18, 9 November 2026</a> (IDFC First Bank report: forward book, swap windows, forecasts); '
    '<a href="https://www.reuters.com/world/india/india-rupee-set-resume-slide-foreign-inflows-remain-weak-2026-11-04">Reuters, 4 November 2026</a> (strategist poll); '
    '<a href="https://www.thehindubusinessline.com/economy/indias-exports-hit-record-90-billion-in-october-but-merchandise-trade-deficit-widens/article71697780.ece">The Hindu BusinessLine, 13 November 2026</a> (October goods deficit). '
    'Gains, reserves differences and the end-March value computed by this blog. Analysed 16 November 2026.')

RELATED = [
    (f"{B}/2026/10/the-rbis-fcnrb-window-drew-133-billion.html", "RBI's FCNR(B) swap window: $133 billion drawn, reserves down $51 billion from peak"),
    (f"{B}/2026/08/rbi-foreign-exchange-reserves-20152026.html", "RBI foreign exchange reserves, 2015–2026: monthly and weekly data with the rupee"),
    (f"{B}/2026/08/where-rupee-actually-stands-ten-years.html", "The rupee over 10 years: against the dollar, yuan, rouble, riyal, dirham and yen"),
    (f"{B}/2026/08/effective-buying-power-china-comparison.html", "Rupee real exchange rate: nominal and inflation-adjusted, with a China comparison"),
    (f"{B}/2026/08/the-rupee-fell-10-and-exports-grew-09.html", "Rupee and exports in FY2025-26: the rupee fell 10%, merchandise exports grew 0.9%"),
]

build("Markets &middot; Currency", TITLE,
      "The rupee closed at Rs 93.69 on 11 November, about 3% above its early-October low, while reserves are $66 billion below their September record and the RBI&rsquo;s forward book is $239 billion short.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
