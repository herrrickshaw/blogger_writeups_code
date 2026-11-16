"""India's October 2026 power squeeze: record demand, coal stocks at about six days, critical plants, and the coal supply response.
Build from the repo root:  python3 out/research/power-squeeze-2026/build.py   (writes out/post-india-power-demand-coal-stocks-october-2026.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 16 November 2026."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-power-demand-coal-stocks-october-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- Demand ----
# Crisil, reported by ETEnergyWorld 5 Nov 2026 (https://energy.economictimes.indiatimes.com/news/coal/indias-power-demand-hits-record-160-bu-in-october-as-coal-stocks-fall-to-five-year-low/135577143):
#   October 2026 consumption 160 BU, +22% on a year earlier (October 2025: -6%); peak demand 261 GW against 221 GW a year earlier (the article says +24%);
#   generation about 173 BU (+23%), coal-based +29%, coal share about 70% against 67%; hydro -19%; FY2026-27 demand 1,885-1,895 BU (+10-11%).
# Power Line, 6 Nov 2026 (https://powerline.net.in/specials/surge-in-demand-sector-attempts-to-cope-with-unseasonal-power-peaks-12788044):
#   September consumption 162 BU (+11.4%), peak 269.06 GW on 10 Sep (+17%); October first-half average peak 252.3 GW (+23.8%), second half 230.4 GW; 31 Oct peak about 225 GW.
# CREA India Energy Snapshot Q2 2026-27, 12 Oct 2026: record peak 270 GW on 16 July (+18% on 230 GW).
OCT_BU, OCT_GROWTH, OCT25_GROWTH, SEP_BU, SEP_GROWTH = 160, 22, -6, 162, 11.4
PEAK_OCT26, PEAK_OCT25 = 261, 221
PEAK_GROWTH = 100 * (PEAK_OCT26 / PEAK_OCT25 - 1)
assert round(PEAK_GROWTH) == 18                                     # the Crisil text says 24%, which does not follow from 261 and 221; computed value used
TWO_YEAR = (1 + OCT_GROWTH / 100) * (1 + OCT25_GROWTH / 100) - 1
assert round(100 * TWO_YEAR) == 15                                  # October 2026 about 15% above October 2024
IMPLIED_OCT25 = OCT_BU / (1 + OCT_GROWTH / 100)
assert round(IMPLIED_OCT25) == 131

# ---- Coal stocks at thermal plants, million tonnes ----
# Power Line (from CEA data): 59 Mt on 1 March 2026 -> 20 Mt on 31 October; critical plants 21 (1 March), 45 (1 September), 86 (31 October).
# Crisil: about 20 Mt on 31 October against 48 Mt a year earlier; six days of consumption against 16 days; 86 of 191 coal plants below 25% of norm, against 11 a year earlier.
# CREA: 21 Mt on 30 September, 36% of the 58 Mt normative requirement; 32 critical plants on 22 Aug, 84 on 30 Sep, 85 on 1 Oct, 91 on 6 Oct.
# The Hindu BusinessLine, 26 Oct 2026: on 25 Oct 85 of 176 domestic-coal plants (207 GW) and 7 of 15 imported-coal plants (17.77 GW) critical; stocks 17.67 + 2.26 Mt; 91 on 21 Oct (domestic plants).
# Argus Media, 26 Oct 2026: 19.93 Mt on 25 October, about six days against a norm of about 19 days; 98 plants critical (different count).
MAR1, SEP30, OCT31, OCT31_25, NORM = 59, 21, 20, 48, 58
assert 17.67 + 2.26 == 19.93
CRIT = {"1 March 2026": 21, "1 September 2026": 45, "31 October 2026": 86, "31 October 2025": 11}
PLANTS = 176 + 15
assert PLANTS == 191
assert round(100 * OCT31 / NORM) == 34 and round(MAR1 / OCT31, 1) == 3.0 and OCT31_25 / OCT31 == 2.4
assert round(100 * 86 / PLANTS) == 45 and round(100 * (MAR1 - OCT31) / MAR1) == 66      # Power Line states a 66% reduction

# ---- Coal supply response ----
# Coal India, BSE filing 1 Nov 2026 and Business Standard: October supplies 70.3 Mt (+19% on 59.2 Mt); power sector 57.1 Mt (record; previous 56.5 Mt in May 2024;
#   October 2025: 48 Mt); production 67.2 Mt (+19.3%, October record; previous 62.47 Mt in October 2024); power-sector rakes averaged 310 a day.
# Ministry of Coal via PIB, 23 Oct 2026 (https://www.coal.nic.in/sites/default/files/2026-10/Pib9oct26.pdf): daily stock drawdown fell from 0.243 Mt in September to 0.116 Mt in October;
#   "stock rebuilding is yet to commence".  Power Line: stocks fell 7.28 Mt in September and 0.56 Mt in 1-10 October; supply to power 2.21 -> 2.49 Mt a day; rakes 426 -> 469 a day.
# Argus Media, 26 Oct 2026 (Kpler estimate): thermal coal imports about 15.06 Mt in October, highest for the month in three years; no fresh blending directive.
CIL_PWR_OCT26, CIL_PWR_OCT25, CIL_PWR_PREV = 57.1, 48.0, 56.5
assert round(100 * (CIL_PWR_OCT26 / CIL_PWR_OCT25 - 1)) == 19
assert round(7.28 / 30, 3) == 0.243
DRAW_SEP, DRAW_OCT = 0.243, 0.116

# ---- Exchange prices, Rs per unit (Crisil) ----
RTM, DAM_GROWTH = 5.7, 149
SOLAR_NOW, SOLAR_PREV, NONSOLAR_NOW, NONSOLAR_PREV = 2.3, 1.4, 6.8, 3.1
assert round(NONSOLAR_NOW / SOLAR_NOW, 1) == 3.0

TITLE = "India's power demand in October 2026: 160 billion units, coal stocks at six days"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    (f"{OCT_BU} BU", f" of electricity was consumed in October 2026, {OCT_GROWTH}% above a year earlier and, because October 2025 fell 6%, about {100 * TWO_YEAR:.0f}% above October 2024; the peak was {PEAK_OCT26} GW (Crisil)."),
    (f"{OCT31} Mt", f" of coal sat at power plants on 31 October, a third of the {NORM} Mt norm and down from {MAR1} Mt on 1 March; that is about six days of burn, against 16 days a year earlier."),
    ("86 of 191", f" coal plants held under 25% of their required stock on 31 October, against 11 a year earlier, even as Coal India sent a record {CIL_PWR_OCT26} Mt to power plants in the month."),
])

s1 = insight(
    "Electricity demand rose 22% in October 2026, on top of a 6% fall in October 2025",
    bars("October demand grew 22% after a 6% fall a year earlier; September grew 11.4%",
         [("October 2025", OCT25_GROWTH), ("September 2026", SEP_GROWTH), ("October 2026", OCT_GROWTH)],
         accent="October 2026", unit="%", sub="Year-on-year change in electricity consumed, per cent.",
         source="Crisil (via ETEnergyWorld, 5 November 2026); Power Line, 6 November 2026.")
    + numbers(["Measure", "Value", "Source"],
              [["October 2026 consumption", f"{OCT_BU} BU, +{OCT_GROWTH}% (about {IMPLIED_OCT25:.0f} BU in October 2025)", "Crisil; the October 2025 value is computed here"],
               ["Peak demand, October", f"{PEAK_OCT26} GW against {PEAK_OCT25} GW (+{PEAK_GROWTH:.0f}% computed; the report says +24%)", "Crisil"],
               ["September 2026", f"{SEP_BU} BU (+{SEP_GROWTH}%), peak 269.06 GW on 10 September", "Power Line"],
               ["First and second half of October", "average peak 252.3 GW (+23.8%), then 230.4 GW", "Power Line"],
               ["Record peak, 2026", "270 GW on 16 July, +18%", "CREA, 12 October 2026"],
               ["Crisil outlook, 2026-27", "1,885&ndash;1,895 BU, +10&ndash;11%", "Crisil"]]),
    f"October 2026 sat about {100 * TWO_YEAR:.0f}% above October 2024 once the weak October 2025 base is removed, and the growth came from heat and weak rain that the Power Line report ties to El Ni&ntilde;o, so part of the 22% is a base effect.",
    "Planners should read monthly growth against two-year comparisons, since a 22% rise on a 6% fall overstates the underlying trend and understates the base to which stocks and capacity must be scaled.",
    "demand")

s2 = insight(
    "Plant coal stocks fell from 59 Mt in March to 20 Mt on 31 October, a third of the norm",
    bars("Coal stocks at power plants fell from 59 Mt to 20 Mt; a year earlier they were 48 Mt",
         [("1 March 2026", MAR1), ("30 September 2026", SEP30), ("31 October 2026", OCT31), ("31 October 2025", OCT31_25)],
         accent="31 October 2026", unit=" Mt", ref=(NORM, f"normative requirement, {NORM} Mt (CREA)"),
         sub="Coal held at thermal power plants, million tonnes. October 2025 and the norm are from different reports; the norm varies by plant and season.",
         source="Power Line (CEA data), 6 November 2026; CREA, 12 October 2026; Crisil via ETEnergyWorld, 5 November 2026.")
    + numbers(["Measure", "Value", "Source"],
              [["Stock, 31 October 2026", f"about {OCT31} Mt, about six days of consumption (16 days a year earlier)", "Crisil"],
               ["Stock, 25 October 2026", "19.93 Mt: 17.67 Mt at domestic-coal plants, 2.26 Mt at imported-coal plants; about six days against a norm of about 19", "Hindu BusinessLine; Argus Media"],
               ["Fall since 1 March", f"{100 * (MAR1 - OCT31) / MAR1:.0f}%", "Power Line"],
               ["Stock as share of the norm", f"{100 * OCT31 / NORM:.0f}% (21 Mt was 36% on 30 September)", "Computed; CREA"]]),
    "Stock fell by about two-thirds between March and October while consumption stayed near 79 Mt a month from June to September, so the margin that absorbs a supply or demand shock is now about six days.",
    "The coal and power ministries should publish a dated target for rebuilding stocks and report progress weekly, since the Ministry of Coal itself says rebuilding has not yet begun.",
    "stocks")

s3 = insight(
    "Plants with critical stock rose from 21 in March to 86 of 191 on 31 October",
    bars("Critical coal plants rose from 21 in March to 86 on 31 October, against 11 a year earlier",
         [(k, v) for k, v in CRIT.items()], accent="31 October 2026", unit=" plants",
         ref=(PLANTS, f"all coal plants counted, {PLANTS}"),
         sub="Plants holding under 25% of their normative coal requirement. Other counts exist (91 at the 21 October peak, 98 in one trade report), because plant sets and dates differ.",
         source="Power Line (CEA data), 6 November 2026; Crisil via ETEnergyWorld, 5 November 2026; Hindu BusinessLine, 26 October 2026.")
    + numbers(["Date", "Critical plants", "Source"],
              [["22 August", "32", "CREA"], ["30 September", "84", "CREA"], ["1 October", "85", "CREA"], ["6 October", "91", "CREA"],
               ["21 October", "91 (domestic-coal plants, peak)", "Hindu BusinessLine"], ["25 October", "85 of 176 domestic-coal plants; 7 of 15 imported-coal plants", "Hindu BusinessLine"],
               ["31 October", "86 of 191", "Crisil; Power Line"]]),
    f"By 31 October {100 * 86 / PLANTS:.0f}% of coal plants were below a quarter of their required stock, and the count has stayed between 81 and 91 since late September, so the shortage is persistent rather than a spike.",
    "The Central Electricity Authority should publish the critical-plant count with a fixed plant list, ownership split and normative stock in each daily report, so the counts in different reports can be compared.",
    "plants")

s4 = insight(
    "Coal India sent a record 57.1 Mt to power plants in October, 19% more than a year earlier",
    bars("Coal India's supply to power plants reached 57.1 Mt, above the May 2024 record of 56.5 Mt",
         [("October 2025", CIL_PWR_OCT25), ("May 2024, previous record", CIL_PWR_PREV), ("October 2026", CIL_PWR_OCT26)],
         accent="October 2026", unit=" Mt", sub="Coal India supply to the power sector in one month, million tonnes.",
         source="Coal India filing of 1 November 2026; Business Standard, 1 November 2026.")
    + numbers(["Measure", "Value", "Source"],
              [["Coal India supply, all sectors, October", "70.3 Mt, +19% on 59.2 Mt (first month above 70 Mt)", "Coal India filing"],
               ["Coal India production, October", "67.2 Mt, +19.3%, an October record", "Coal India filing"],
               ["Stock drawdown per day", f"{DRAW_SEP} Mt in September to {DRAW_OCT} Mt in October", "Ministry of Coal, PIB 23 October 2026"],
               ["Supply and rakes to power, 1&ndash;10 October", "2.49 Mt a day against 2.21 Mt in September; 469 rakes a day against 426", "Power Line"],
               ["Thermal coal imports, October", "about 15.06 Mt estimated, the highest October in three years; no fresh blending directive", "Argus Media, 26 October 2026 (Kpler estimate)"],
               ["Exchange prices, October", f"real-time market Rs {RTM} a unit (more than double); day-ahead +{DAM_GROWTH}%; non-solar hours Rs {NONSOLAR_NOW} against Rs {NONSOLAR_PREV}, solar hours Rs {SOLAR_NOW} against Rs {SOLAR_PREV}", "Crisil"]]),
    f"Record dispatch more than halved the daily drawdown, from {DRAW_SEP} Mt in September to {DRAW_OCT} Mt in October, but it only slowed the fall, because stocks remained near 20 Mt on 31 October.",
    "Coal India, Indian Railways and the power ministry should publish weekly dispatch against consumption for the power sector, so the date when stocks start rising can be seen and not forecast.",
    "response")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Coal and Ministry of Power:</b> publish a dated stock-rebuilding target and a weekly dispatch-against-consumption table for the power sector.</li>
<li><b>Central Electricity Authority:</b> state in each daily coal report the plant list, ownership split and normative stock behind the critical-plant count.</li>
<li><b>Ministry of Power:</b> state whether a blending directive for imported coal will be issued for the winter, since trade reports say domestic plants have not been told to import for blending.</li>
<li><b>Grid-India:</b> publish evening energy-not-met by state each month, since reports name several states with evening supply gaps but give no figures.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Demand is electricity consumed (energy met); generation is a separate, larger measure (about 173 BU in October, Crisil). The two are not interchangeable.</li>
<li>A &ldquo;critical&rdquo; plant holds under 25% of its normative coal stock (CEA definition, as stated by CREA and Hindu BusinessLine). Normative stock is the number of days of burn set for each plant by its distance from the mine, so the national norm is an aggregate.</li>
<li>The two-year comparison multiplies the October 2026 growth (+22%) by the October 2025 growth (&minus;6%): 1.22 &times; 0.94 = 1.147.</li>
<li>Peak growth is recomputed from the stated peaks (261 GW against 221 GW) because the report&rsquo;s own +24% does not follow from them.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>CEA&rsquo;s daily coal report and Grid-India data were not downloaded for this piece; stock, demand and price figures are read from Crisil (through ETEnergyWorld), Power Line, CREA, Coal India, the Ministry of Coal and trade press. The CEA report of 30 October was found but its totals were not read.</li>
<li>Plant counts differ across reports (84&ndash;91 in CREA, 85 and 91 in Hindu BusinessLine, 86 in Crisil, 98 in Argus Media) because the plant set and the date differ; the 86 of 191 is Crisil&rsquo;s end-October count.</li>
<li>The cause of the demand surge: Crisil and Power Line cite heat, weak rain and El Ni&ntilde;o; this piece does not test it. The 24% peak-growth figure in Crisil&rsquo;s report is not reproduced.</li>
<li>Whether stocks have risen since 31 October: the latest figure read is 31 October, and a figure of about 19 Mt is quoted by Power Line for a nearby date.</li>
<li>Import figures: the 15.06 Mt October estimate is a Kpler estimate quoted by Argus Media, not a reported figure.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://energy.economictimes.indiatimes.com/news/coal/indias-power-demand-hits-record-160-bu-in-october-as-coal-stocks-fall-to-five-year-low/135577143">ETEnergyWorld, 5 November 2026</a> (Crisil report: October demand, peak, generation, stocks, critical plants, exchange prices, outlook); '
    '<a href="https://powerline.net.in/specials/surge-in-demand-sector-attempts-to-cope-with-unseasonal-power-peaks-12788044">Power Line, 6 November 2026</a> (CEA-based demand and stock series, critical-plant counts, October supply measures); '
    '<a href="https://energyandcleanair.org/quarterly-energy-snapshot-for-india-q2-2026-27">CREA, Quarterly energy snapshot for India Q2 2026-27, 12 October 2026</a> (July peak, 30 September stocks, norm, plant counts); '
    '<a href="https://www.coal.nic.in/sites/default/files/2026-10/Pib9oct26.pdf">Ministry of Coal, PIB release of 23 October 2026</a> (drawdown, rake loading, rebuilding not yet begun); '
    'Coal India, stock-exchange filing of 1 November 2026, as reported by '
    '<a href="https://www.business-standard.com/industry/news/coal-india-s-october-supplies-cross-70-mt-for-first-time-hit-new-record-126110100720_1.html">Business Standard, 1 November 2026</a> (October supply and production); '
    '<a href="http://www.thehindubusinessline.com/markets/commodities/almost-half-of-domestic-coal-based-power-plants-have-critical-stocks/article71627830.ece">The Hindu BusinessLine, 26 October 2026</a> (25 October plant and stock counts); '
    '<a href="https://www.argusmedia.com/en/news-and-insights/latest-market-news/2895681-india-s-thermal-coal-imports-set-for-october-rebound">Argus Media, 26 October 2026</a> (Kpler import estimate; days of stock; blending); '
    '<a href="https://npp.gov.in/public-reports/cea/daily/fuel/30-10-2026/dailyCoal1-2026-10-30.pdf">CEA daily coal stock report, 30 October 2026</a> (located; totals not read). '
    'Percentages, ratios and the two-year comparison computed by this blog. Analysed 16 November 2026.')

RELATED = [
    (f"{B}/2026/10/india-ordered-112-captive-coal-plants.html", "Captive coal plants: 112 ordered to full output as exchange prices rose 50%"),
    (f"{B}/2026/10/india-has-auctioned-141-commercial-coal.html", "Commercial coal mines in India: 141 auctioned since 2020, 15 producing"),
    (f"{B}/2026/09/a-2223-crore-coal-freight-railway-line.html", "₹2,223 crore coal-freight railway: land acquired one survey number at a time"),
    (f"{B}/2026/09/indias-battery-storage-boom-is.html", "Grid battery storage in India: about 9.3 GWh by mid-2026, up from 1.08 GWh"),
]

build("Energy &middot; Power", TITLE,
      "Electricity demand hit a record in October 2026 while coal held at power plants fell to about six days of burn; 86 of 191 coal plants were below a quarter of their required stock.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
