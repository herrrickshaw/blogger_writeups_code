"""India's 2026 monsoon and El Nino: rainfall, reservoirs, hydropower and the rabi season ahead.
Build from the repo root:  python3 out/research/el-nino-2026/build.py   (writes out/post-india-monsoon-2026-el-nino-reservoirs-rabi.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 16 November 2026."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-monsoon-2026-el-nino-reservoirs-rabi.html"
B = "https://blog.vertistratsolution.com"

# ---- IMD, Salient Features of the 2026 Southwest Monsoon Season (30 Sep 2026) and end-of-season report (5 Oct 2026) ----
# https://mausam.imd.gov.in/Forecast/marquee_data/Salient_Features_SW_MONSOON%20_2026_30_sep.pdf ; https://imdpune.gov.in/seasons_previous/swmonsoon/swmonsoon26/end_of_season_report.pdf
# Table 1 (mm): region: (LPA, actual).  Highlights give East and Northeast India as 1017.1 mm in one line and 1016.3 mm in the table; the table is used.
RAIN = {"All India": (868.6, 759.4), "Northwest India": (587.6, 553.0), "Central India": (978.0, 952.8), "East and Northeast India": (1367.3, 1016.3), "South Peninsula": (716.2, 542.0)}
pct = {k: 100 * a / l for k, (l, a) in RAIN.items()}
assert round(pct["All India"]) == 87 and round(pct["East and Northeast India"]) == 74 and round(pct["South Peninsula"]) == 76
assert round(pct["Northwest India"]) == 94 and round(pct["Central India"]) == 97
assert round(RAIN["All India"][0] - RAIN["All India"][1], 1) == 109.2
MONTHLY = [("June", 65), ("July", 101), ("August", 84), ("September", 92)]
SUBDIV_DEFICIENT, SUBDIV_NORMAL, SUBDIV_EXCESS = 17, 18, 1
assert SUBDIV_DEFICIENT + SUBDIV_NORMAL + SUBDIV_EXCESS == 36

# ---- IMD press release of 31 Oct 2026 (November outlook): very strong El Nino prevailing; very strong likely in Nov-Dec; November rainfall below normal (<77% of LPA)
#   for the country (LPA 29.7 mm) and for the South Peninsula (LPA 118.7 mm); above-normal temperatures over most of the country; neutral Indian Ocean Dipole.
# https://mausam.imd.gov.in/Forecast/marquee_data/Press_Release_NOV_31oct_2026.pdf
# NIAS working paper "Super El Nino" (3 Nov 2026; secondary): record daily Nino 3.4 anomaly of +3.11 C on 21 Sep 2026; US CPC (8 Oct) 83% chance of exceeding +2.5 C in Oct-Dec; not checked here.

# ---- Reservoirs: Central Water Commission bulletin of 15 Oct 2026 as quoted by Forbes India, 16 Nov 2026 ----
# 178 reservoirs at 68.58% of capacity: 24.53% lower than a year earlier and 16.44% below the 10-year average (read as relative differences).
RES, RES_LY_GAP, RES_AVG_GAP = 68.58, 24.53, 16.44
RES_LY = RES / (1 - RES_LY_GAP / 100)
RES_AVG = RES / (1 - RES_AVG_GAP / 100)
assert round(RES_LY, 1) == 90.9 and round(RES_AVG, 1) == 82.1
# Outlook Business, 4 Nov 2026 (24 September): about 70% of capacity, against 79% last year and a 10-year average of 76.62%.

# ---- Power system (see the power-squeeze post): CREA Q2 FY27 large hydro -20% (60 BU), Crisil October hydro -19%, consumption +22%, coal-based generation +29% ----
POWER = [("Large hydro generation, July to September", -20), ("Hydro generation, October", -19), ("Electricity consumption, October", 22), ("Coal-based generation, October", 29)]

# ---- Grain buffer ----
# Department of Food and Public Distribution Foodgrains Bulletin, central pool on 1 Oct 2026 as shown by Tipsheet (6 Nov 2026; https://tipsheet.markets/economy/rural/food):
#   840.8 lakh tonnes of wheat and rice, 2.7 times the 307.7 lakh tonne norm. Hindu BusinessLine, 30 Oct: wheat about 463 lakh tonnes; Mint, 30 Oct: rice 377.6 lakh tonnes (37.76 Mt).
STOCK, NORM, WHEAT, RICE = 840.8, 307.7, 463.0, 377.6
assert round(STOCK / NORM, 1) == 2.7 and abs(WHEAT + RICE - STOCK) < 0.5
# Agriculture ministry, 29 Sep 2026 (via Forbes India): foodgrain target 373.93 Mt for 2026-27 against the record 376.56 Mt of 2025-26.
TARGET, RECORD = 373.93, 376.56
assert round(100 * (TARGET / RECORD - 1), 1) == -0.7

TITLE = "India's 2026 monsoon: 87% of normal rain, reservoirs low, a very strong El Niño"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    ("87%", " of the long-period average fell in the June&ndash;September 2026 monsoon, 109 mm short; east and northeast India received 74%, its lowest since 1901, and the south 76%, according to the India Meteorological Department (IMD)."),
    (f"{RES}%", f" of capacity was held by 178 monitored reservoirs on 15 October, which the Central Water Commission figures put 24.53% below a year earlier and 16.44% below the 10-year average."),
    ("2.7 times", f" the buffer norm was the central pool&rsquo;s {STOCK} lakh tonnes of wheat and rice on 1 October, while IMD says very strong El Ni&ntilde;o conditions are likely in November and December and November rain below 77% of normal."),
])

s1 = insight(
    "Monsoon 2026 ended at 87% of normal, with east and northeast India driest since 1901",
    bars("East and northeast India got 74% of normal rain and the south 76%; all India 87%",
         [("East and Northeast India", round(pct["East and Northeast India"])), ("South Peninsula", round(pct["South Peninsula"])), ("All India", round(pct["All India"])),
          ("Northwest India", round(pct["Northwest India"])), ("Central India", round(pct["Central India"]))],
         accent=["East and Northeast India", "South Peninsula"], unit="%", ref=(100, "long-period average = 100%"),
         sub="Rainfall from 1 June to 30 September 2026 as a percentage of the long-period average, by IMD region.",
         source="IMD, Salient Features of the 2026 Southwest Monsoon Season, 30 September 2026 (Table 1).")
    + numbers(["Region", "Long-period average (mm)", "Rain in 2026 (mm)", "% of average"],
              [[k, f"{l}", f"{a}", f"{100 * a / l:.1f}"] for k, (l, a) in RAIN.items()] +
              [["Month, all India", "June / July / August / September", "&ndash;", "65 / 101 / 84 / 92"],
               ["Sub-divisions", f"{SUBDIV_DEFICIENT} deficient (42% of area), {SUBDIV_NORMAL} normal (53%), {SUBDIV_EXCESS} excess (Odisha, 5%)", "&ndash;", "&ndash;"]]),
    "June reached only 65% of normal and August 84%, and 17 of 36 sub-divisions covering 42% of the country&rsquo;s area were deficient, so the national 87% hides a much drier east and south.",
    "State governments in the dry regions should publish drought declarations at taluk or block level on one date-stamped list, since the national average cannot tell a farmer whether the year counts as a drought.",
    "rain")

s2 = insight(
    f"Reservoirs held {RES}% of capacity on 15 October, about 82% on a 10-year average",
    bars("Reservoirs held 68.6% of capacity on 15 October; the 10-year average is about 82%",
         [("15 October 2026", RES), ("10-year average (computed)", round(RES_AVG, 1)), ("15 October 2025 (computed)", round(RES_LY, 1))],
         accent="15 October 2026", unit="%",
         sub="Live storage as a share of capacity in the 178 reservoirs the Central Water Commission monitors. The two comparison values are computed from the reported percentage gaps, read as relative differences.",
         source="Central Water Commission bulletin of 15 October 2026, as reported by Forbes India, 16 November 2026.")
    + numbers(["Measure", "Value", "Source"],
              [["Storage, 15 October", f"{RES}% of capacity; {RES_LY_GAP}% below last year and {RES_AVG_GAP}% below the 10-year average", "CWC via Forbes India"],
               ["Implied last year and average", f"about {RES_LY:.1f}% and {RES_AVG:.1f}% (if the gaps are relative)", "Computed here"],
               ["Storage, 24 September", "about 70%, against 79% last year and a 10-year average of 76.62%", "Outlook Business, 4 November 2026"],
               ["Kharif sowing", "130.25 million hectares, about 1% below last year (1.2% by end-September)", "USDA FAS, 30 October; ICRA, 1 October"],
               ["Drought declarations", "Karnataka 217 of 240 taluks; Maharashtra 265 of 358 talukas; Andhra Pradesh 388 mandals in 21 of 28 districts", "NIAS working paper, 3 November 2026 (secondary)"]]),
    "Water held in reservoirs is the link from this year&rsquo;s deficit to the rabi crop, and with storage about 13 points below the average on 15 October the winter season starts with less irrigation water than usual.",
    "The Central Water Commission should publish reservoir storage by basin against the 10-year average each week through the rabi season, so irrigation releases can be matched to what is held.",
    "reservoirs")

s3 = insight(
    "Hydropower fell 19% to 20% while consumption rose 22% and coal generation 29%",
    bars("Hydro output fell 19% to 20% while October use rose 22% and coal generation 29%",
         POWER, accent="Hydro generation, October", unit="%", sub="Year-on-year change, per cent; July to September for the first row, October for the others.",
         source="CREA, India Energy Snapshot Q2 2026-27, 12 October 2026; Crisil via ETEnergyWorld, 5 November 2026.")
    + numbers(["Measure", "Value", "Source"],
              [["Large hydro generation, July to September", "60 BU, &minus;20%; plant load factor 50% against 61%", "CREA"],
               ["Hydro generation, October", "&minus;19%", "Crisil"],
               ["Consumption and coal-based generation, October", "+22% and +29%; coal share about 70% of generation", "Crisil"],
               ["Cause cited", "heat and below-normal rain linked to El Ni&ntilde;o", "Crisil; Power Line, 6 November 2026"]]),
    "A dry year cut the supply of hydropower as heat raised demand, and coal-based generation rose 29% in October to cover the gap, which links the monsoon to the coal stock position in a single month.",
    "The Central Electricity Authority should publish a monthly table of the hydro shortfall against the coal and gas generation that replaced it, so the cost of a dry year to the power system can be read directly.",
    "power")

s4 = insight(
    f"Central wheat and rice stocks were {STOCK} lakh tonnes on 1 October, 2.7 times the norm",
    bars(f"The central pool held {STOCK} lakh tonnes on 1 October against a norm of {NORM}",
         [("Central pool, wheat and rice", STOCK), ("of which wheat", WHEAT), ("of which rice", RICE), ("Buffer norm for 1 October", NORM)],
         accent="Central pool, wheat and rice", unit=" lakh tonnes", sub="Stock on 1 October 2026, lakh tonnes. Wheat and rice come from different reports, so the parts are approximate.",
         source="Department of Food and Public Distribution bulletin as shown by Tipsheet; Hindu BusinessLine and Mint, 30 October 2026.")
    + numbers(["Measure", "Value", "Source"],
              [["Foodgrain target, 2026-27", f"{TARGET} Mt against a record {RECORD} Mt in 2025-26 ({100 * (TARGET / RECORD - 1):.1f}%)", "Agriculture ministry, 29 September, via Forbes India"],
               ["IMD, November outlook", "rain below 77% of normal for India and for the South Peninsula; above-normal maximum and minimum temperatures over most of the country", "IMD, 31 October 2026"],
               ["El Ni&ntilde;o", "very strong conditions prevailing; very strong likely in November&ndash;December", "IMD, 31 October 2026"],
               ["Duration", "INCOIS puts the chance of El Ni&ntilde;o dominating through March 2027 at 85&ndash;98% (secondary)", "Outlook Business, 4 November 2026"],
               ["Wheat and heat", "heat in February&ndash;March during grain filling cut yields in 2022 (secondary)", "NIAS working paper, 3 November 2026"]]),
    f"The central pool can supply rationing and market sales for months at {STOCK / NORM:.1f} times its norm, so the exposure this winter is the rabi crop, vegetable prices and water rather than the grain in store.",
    "The Agriculture Ministry should release the first advance estimates for kharif 2026-27 with the rainfall and reservoir overlay by district, and add a February&ndash;March heat-risk advisory for wheat.",
    "buffer")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Agriculture:</b> release the first advance estimates for kharif 2026-27, which have not yet appeared, and publish them with district rainfall and reservoir data.</li>
<li><b>Central Water Commission:</b> publish storage by basin against the 10-year average weekly through the rabi season, with the drawdown plan for irrigation.</li>
<li><b>IMD and the Agriculture Ministry:</b> issue a February&ndash;March heat advisory for wheat with dated triggers for irrigation and sowing-time guidance.</li>
<li><b>State governments:</b> publish drought declarations by taluk or block on one dated list, and the relief tied to each.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Rainfall shares are IMD&rsquo;s figures for the four months June to September against the 1971&ndash;2020 long-period average; percentages are recomputed from the millimetre values in the IMD tables.</li>
<li>The reservoir comparison values (about 90.9% a year earlier and 82.1% on average) are computed from the 68.58% reading and the reported gaps of 24.53% and 16.44%, read as relative differences; if the gaps are in percentage points the values would be 93.1% and 85.0%.</li>
<li>The buffer norm is the quarterly minimum the Cabinet Committee on Economic Affairs sets for 1 October; the stock is wheat and rice together.</li>
<li>Hydro and demand changes are year-on-year, from CREA for the July&ndash;September quarter and from Crisil for October.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>Crop output: the first advance estimates of kharif 2026-27 had not been released when this was written, so no production figure is given; sowing area (about 1% lower) is not yield.</li>
<li>The El Ni&ntilde;o record and its probabilities (a +3.11&deg;C daily anomaly on 21 September; an 83% chance above +2.5&deg;C in October&ndash;December; 85&ndash;98% to March) come from a working paper and a magazine, not from NOAA or INCOIS directly; IMD&rsquo;s own statement is &ldquo;very strong El Ni&ntilde;o conditions are prevailing&rdquo;.</li>
<li>The reservoir figures are from a magazine report of the 15 October bulletin; the latest CWC bulletin was not read, and a figure of 71.84% on a later date appears in a USDA report without a date.</li>
<li>Drought declarations and the 70% share of land under dry or drought conditions come from a working paper citing IIT Gandhinagar&rsquo;s monitor and state notices, and were not checked against the originals.</li>
<li>Effects on rabi yields, wheat and food prices are expectations in the sources, not outcomes; the October food-inflation figure (8.94%) is in this blog&rsquo;s separate CPI post.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://mausam.imd.gov.in/Forecast/marquee_data/Salient_Features_SW_MONSOON%20_2026_30_sep.pdf">IMD, Salient Features of the 2026 Southwest Monsoon Season, 30 September 2026</a> and '
    '<a href="https://imdpune.gov.in/seasons_previous/swmonsoon/swmonsoon26/end_of_season_report.pdf">IMD end-of-season report, October 2026</a> (rainfall by region and month; sub-divisions); '
    '<a href="https://mausam.imd.gov.in/Forecast/marquee_data/Press_Release_NOV_31oct_2026.pdf">IMD press release, 31 October 2026</a> (El Ni&ntilde;o status; November outlook); '
    '<a href="http://www.forbesindia.com/business/economy/rural-economy-resilient-but-uneven-next-few-quarters-key-article/3000568">Forbes India, 16 November 2026</a> (Central Water Commission bulletin of 15 October; agriculture ministry target); '
    '<a href="http://www.outlookbusiness.com/planet/future-of-food/the-el-ni%C3%B1o-effect-why-indias-kharif-recovery-may-not-tell-the-full-story">Outlook Business, 4 November 2026</a> (24 September reservoir storage; INCOIS probability; secondary); '
    '<a href="https://www.fas.usda.gov/data/gain/2026/10/india-weak-southwest-monsoon-and-el-nino-threaten-winter-sowing">USDA Foreign Agricultural Service, 30 October 2026</a> (kharif sowing); '
    '<a href="https://www.icra.in/Rating/DownloadResearchSpecialCommentReport?id=7156">ICRA, Southwest Monsoon Wrapup 2026, October 2026</a>; '
    '<a href="http://eprints.nias.res.in/3500/1/Super%20El%20Nino.pdf">NIAS working paper on the 2026 El Ni&ntilde;o, 3 November 2026</a> (secondary: Nino 3.4 record, drought declarations); '
    '<a href="https://energyandcleanair.org/quarterly-energy-snapshot-for-india-q2-2026-27">CREA, 12 October 2026</a> and '
    '<a href="https://energy.economictimes.indiatimes.com/news/coal/indias-power-demand-hits-record-160-bu-in-october-as-coal-stocks-fall-to-five-year-low/135577143">ETEnergyWorld (Crisil), 5 November 2026</a> (hydro and demand); '
    '<a href="https://tipsheet.markets/economy/rural/food">Tipsheet, grain stocks, 6 November 2026</a> (Department of Food and Public Distribution data); '
    '<a href="https://www.thehindubusinessline.com/economy/agri-business/indian-millers-bid-higher-rates-to-get-fcis-wheat-offtake-100-in-many-states/article71645756.ece">Hindu BusinessLine, 30 October 2026</a> and '
    '<a href="https://www.livemint.com/news/governments-paddy-procurement-hit-by-weather-woes-storage-constraints/amp-11793357180974.html">Mint, 30 October 2026</a> (wheat and rice stocks); '
    '<a href="https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24516">RBI Bulletin</a> (monsoon and El Ni&ntilde;o in the inflation outlook). '
    'Percentages, implied reservoir values and ratios computed by this blog. Analysed 16 November 2026.')

RELATED = [
    (f"{B}/2026/11/the-chessboard-and-indias-granaries.html", "India's grain storage: 918 lakh tonnes, compared with a record harvest"),
    (f"{B}/2026/10/indias-winter-harvest-now-outgrows-its.html", "India's rabi and summer crops: 53% of foodgrains, up from 36% in 1966-67"),
    (f"{B}/2026/10/indias-biggest-mandi-crops-have.html", "Mandi prices in India: vegetables swing 2 to 8 times as much as paddy and wheat"),
    (f"{B}/2026/10/wheats-support-price-rose-by-25.html", "Wheat MSP for 2027-28: up ₹25 or 1.0%, with 480 lakh tonnes in the central pool"),
    ("https://blog.vertistratsolution.com/2026/10/how-to-use-kalkiflooding-125-years-of.html", "How to use kalki_flooding: 125 years of Indian city rainfall extremes from IMD data"),
]

build("Climate &middot; Agriculture", TITLE,
      "The 2026 southwest monsoon ended 13% below normal under a very strong El Ni&ntilde;o that IMD expects to continue through December; reservoirs, hydropower and the rabi crop carry the effects forward.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
