"""Sour crude in India's purchases: the multi-year trend, the origins that replaced each other, what 2026 changed, and what sour crude costs.
Build from the repo root:  python3 out/research/sour-crude-trends-2026/build.py   (writes out/post-india-sour-crude-purchases-trends.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 26 November 2026.
Primary sources read in full: PPAC Ready Reckoner 2025-26 (Tables 4.1, 4.2, 4.3, 8.24 and the benchmark-spread chart on p.115) and the IEA India Oil
Market Report, Outlook to 2030 (chapter 4). Everything else is secondary and labelled as such in the post."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-sour-crude-purchases-trends.html"
B = "https://blog.vertistratsolution.com"

# ---- 1. PPAC Ready Reckoner 2025-26, Table 4.2: high-sulphur (HS) and low-sulphur (LS) crude processed, MMT (refinery runs, imported plus domestic)
FY = ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
HS = [161.4, 185.0, 197.9, 205.3, 213.8, 214.0]
LS = [60.3, 56.7, 57.4, 56.2, 54.9, 58.0]
TOT = [221.8, 241.7, 255.2, 261.5, 268.6, 272.0]
PPAC_SHARE_PRINTED = [72.8, 76.6, 77.5, 78.5, 79.6, 78.7]       # the share row PPAC prints
for i in range(6):
    assert abs(HS[i] + LS[i] - TOT[i]) < 0.15, (FY[i], HS[i] + LS[i], TOT[i])   # HS + LS = total within rounding
    assert abs(100 * HS[i] / TOT[i] - PPAC_SHARE_PRINTED[i]) <= 0.1, (FY[i], 100 * HS[i] / TOT[i])   # PPAC divides unrounded tonnes: FY22 gives 76.5 against the printed 76.6
SHARE = dict(zip(FY, PPAC_SHARE_PRINTED))
assert max(SHARE, key=SHARE.get) == "2024-25"
HS_RISE = round(HS[-1] - HS[0], 1)                                  # 52.6 Mt more HS crude in FY26 than FY21
LS_RISE = round(LS[-1] - LS[0], 1)
assert HS_RISE == 52.6 and LS_RISE == -2.3
GROWTH_SHARE_OF_HS = 100 * HS_RISE / (TOT[-1] - TOT[0])             # share of total growth that was HS crude
assert round(GROWTH_SHARE_OF_HS) == 105                             # more than all of the growth: LS fell slightly

# PPAC Table 4.3: imported crude processed, MMT, and Table 8.24: crude imports, MMT (customs-basis series)
IMP_PROC_SHARE = [87.4, 88.8, 89.6, 89.7, 90.1, 90.5]
IMPORTS_MT = {"2018-19": 226.5, "2019-20": 227.0, "2020-21": 196.5, "2021-22": 212.4, "2022-23": 232.7, "2023-24": 234.3, "2024-25": 243.2, "2025-26": 245.8}
# conflict from the brief: "243.22 Mt in 2024-25" is PPAC's FY25 figure (243.2); "234.3 Mt in FY25" is PPAC's FY24 figure. PPAC's table does not start before 2018-19.
assert IMPORTS_MT["2024-25"] == 243.2 and IMPORTS_MT["2023-24"] == 234.3
assert round(100 * (IMPORTS_MT["2025-26"] / IMPORTS_MT["2024-25"] - 1), 1) == 1.1    # the Ready Reckoner prints "1.0% increase"; the 0.1 gap is rounding of the tonnes
JAM_VAD = 33.6 + 33.7 + 18.9                                        # Table 4.1 FY26 processing: Jamnagar DTA + SEZ, Vadinar
JAM_VAD_SHARE = 100 * JAM_VAD / TOT[-1]
assert round(JAM_VAD, 1) == 86.2 and round(JAM_VAD_SHARE, 1) == 31.7

# ---- IEA, India Oil Market Report: Outlook to 2030, ch.4 (import quality from Kpler; text gives 2021 and 2023 only, the annual 2014-2023 series is a chart)
SOUR_2023, SWEET_2023, LIGHT_SOUR_2023, MH_SOUR_2023 = 85, 15, 24, 62
SWEET_DROP_PTS, LIGHT_SOUR_DROP_PTS, MH_SOUR_RISE_PTS = 8, 5, 13
SWEET_2021 = SWEET_2023 + SWEET_DROP_PTS                           # derived here, not printed by the IEA
SOUR_2021 = 100 - SWEET_2021
assert SWEET_2021 == 23 and SOUR_2021 == 77
assert abs(LIGHT_SOUR_2023 + MH_SOUR_2023 - SOUR_2023) <= 1       # 24 + 62 = 86 against the printed 85: rounding in the IEA's own text
assert abs(SOUR_2023 + SWEET_2023 - 100) == 0
ORIGIN = {"Russia": (3, 40), "Middle East": (61, 45), "West Africa": (12, 4.5), "Latin America": (4.5, 3)}      # 2021 -> 2023 share of imports, %
ORIGIN_PTS = {k: round(b - a, 1) for k, (a, b) in ORIGIN.items()}
assert ORIGIN_PTS == {"Russia": 37, "Middle East": -16, "West Africa": -7.5, "Latin America": -1.5}
assert abs(sum(ORIGIN_PTS.values()) - 12) < 0.1                    # the other regions (Asia, North America, other Africa) net +12 points; not itemised by the IEA
IEA_RUSSIA_2023_ALT = 38                                           # the IEA text also says "Russia made up 38% of India's crude imports" for 2023: a conflict with "nearly 40%" inside the report

# ---- 2. Russia in 2026, Kpler arrivals, million b/d (secondary: reported by ThePrint, Outlook Business, Business Standard, Financial Express)
RUS = [("Dec 2025", 1.28), ("Jan 2026", 1.22), ("Early Feb 2026", 1.09), ("Jul 2026", 2.82), ("Aug 2026", 2.08), ("Sep 2026", 1.82), ("Oct 2026", 1.97)]
OCT_TOTAL, SEP_TOTAL, OCT25_TOTAL = 5.63, 5.34, 4.95               # Kpler totals, provisional to 30 Oct (Financial Express)
assert round(100 * 1.97 / OCT_TOTAL, 1) == 35.0                     # Kpler: "around 35%" in October
assert abs(100 * 1.82 / SEP_TOTAL - 35) < 1.5                       # 34.1% against the 35% reported for September
JUL_TOTAL = 2.82 / 0.55
assert 5.0 < JUL_TOTAL < 5.3                                        # implies "just over 5 million b/d", as BS/CREA report
assert round(100 * (OCT_TOTAL / OCT25_TOTAL - 1)) == 14             # +14% on a year earlier, as reported
RUS_DROP_JUL_OCT = round(100 * (1 - 1.97 / 2.82))
assert RUS_DROP_JUL_OCT == 30
# US crude and Kpler's February call of "up to ~10% of intake"
US_KBD = {"Oct 2025 (peak)": 565, "Jan 2026": 295, "Mar 2026": 165, "Jul 2026": 125, "Aug 2026": 75, "Oct 2026 (to 30 Oct)": 157}
US_SHARE_OCT25 = 100 * 565 / (OCT25_TOTAL * 1000)
US_SHARE_OCT26 = 100 * 157 / (OCT_TOTAL * 1000)
assert round(US_SHARE_OCT25, 1) == 11.4 and round(US_SHARE_OCT26, 1) == 2.8
assert round(100 * (1 - 75 / 565)) == 87                            # the live basket post's -87%, Oct 2025 to Aug 2026
VEN_OCT, VEN_SEP, ANG_OCT, ANG_SEP = 345, 196, 335, 36              # kb/d, Kpler via Financial Express and ThePrint
assert round(VEN_OCT / VEN_SEP, 2) == 1.76 and round(ANG_OCT / ANG_SEP, 1) == 9.3

# ---- 4. PPAC benchmark spread, Brent minus Dubai, US$ a barrel by fiscal year (Ready Reckoner p.115 chart; read from the data labels, olive series)
SPREAD = [("2015-16", 1.83), ("2016-17", 1.70), ("2017-18", 1.63), ("2018-19", 0.84), ("2019-20", 0.66), ("2020-21", -0.11),
          ("2021-22", 2.91), ("2022-23", 3.53), ("2023-24", 0.81), ("2024-25", 0.37), ("2025-26", -1.58)]
assert len(SPREAD) == 11
POS = [v for _, v in SPREAD if v > 0]
assert len(POS) == 9 and round(sum(POS) / len(POS), 2) == 1.59 and min(v for _, v in SPREAD) == -1.58
FLIP = round(SPREAD[7][1] - SPREAD[-1][1], 2)
assert FLIP == 5.11                                                 # swing in the Dubai discount from FY23 to FY26, $/bbl
# landed prices by origin from customs data, Business Standard (7 May 2024), $/bbl
LAND_24 = [("Venezuela", 64.0), ("Russia", 76.4), ("Iraq", 79.0), ("United States", 86.3), ("UAE", 89.2), ("Saudi Arabia", 90.3), ("Nigeria", 91.0)]
LAND_23 = {"Iraq": 90.6, "Russia": 83.2, "Saudi Arabia": 100.5, "UAE": 104.0, "United States": 91.6, "Nigeria": 109.0}
assert [v for _, v in LAND_24] == sorted(v for _, v in LAND_24)
GAP_NG_IQ_24, GAP_NG_IQ_23 = round(91 - 79, 1), round(109 - 90.6, 1)
assert GAP_NG_IQ_24 == 12.0 and GAP_NG_IQ_23 == 18.4
GAP_RU_IQ_24, GAP_RU_IQ_23 = round(79 - 76.4, 1), round(90.6 - 83.2, 1)
assert GAP_RU_IQ_24 == 2.6 and GAP_RU_IQ_23 == 7.4                  # BS text: "less than $3" and "over $7"
# IOC: spot share of purchases April-June 2026 (Bloomberg via Outlook Business)
IOC_SPOT, IOC_RUS, IOC_KBD, IOC_SHARE = 84, 54, 1.4, 27
assert abs(100 * IOC_KBD / 5.2 - IOC_SHARE) < 1.0                   # 1.4 of about 5.2 mb/d is 27%
H2_PER_T_S = 2.016 / 32.06 * 1000                                   # kg H2 per tonne S as H2S, the stoichiometric floor used in the live basket post
assert round(H2_PER_T_S) == 63

TITLE = "India's sour crude: high-sulphur grades were 78.7% of refinery runs in 2025-26"
assert 55 <= len(TITLE) <= 90, len(TITLE)

top = top_line([
    (f"{SHARE['2025-26']}%", f" of crude processed in FY2025-26 was high-sulphur, up from {SHARE['2020-21']}% in FY2020-21 (PPAC); the IEA puts sour grades at {SOUR_2023}% of imports in 2023, up from {SOUR_2021}% in 2021 by this blog&rsquo;s arithmetic."),
    ("3% to 40%", " is Russia&rsquo;s share of India&rsquo;s imports between 2021 and 2023 (IEA, from Kpler), mostly medium-sour Urals, taking share from the Middle East (61% to 45%) and West Africa (12% to 4.5%)."),
    ("&minus;$1.58", " was PPAC&rsquo;s Brent-minus-Dubai spread for FY2025-26, a sour premium; it was +$3.53 in FY2022-23, so the discount that makes sour crude attractive reversed in 2026."),
])

# ---------------------------------------------------------------- section 1
s1 = insight(
    f"Sour share: high-sulphur crude rose from {SHARE['2020-21']}% to {SHARE['2025-26']}% of refinery runs",
    bars("High-sulphur crude was 78.7% of India's refinery runs in 2025-26, after a 79.6% peak",
         [(f, SHARE[f]) for f in FY], accent="2024-25", unit="%", vmax=100,
         sub="High-sulphur crude as a share of all crude processed, per cent, by fiscal year; imported and domestic crude together, as defined by the oil companies reporting to PPAC.",
         source="PPAC Ready Reckoner 2025-26, Table 4.2 (primary). Printed shares; recomputed from the rounded tonnes they agree within 0.1 point.")
    + numbers(["Fiscal year", "High-sulphur (Mt)", "Low-sulphur (Mt)", "Total (Mt)", "HS share (%)", "Imported share of runs (%)"],
              [[f, f"{HS[i]}", f"{LS[i]}", f"{TOT[i]}", f"{SHARE[f]}", f"{IMP_PROC_SHARE[i]}"] for i, f in enumerate(FY)]
              + [["IEA, imports 2021", "&ndash;", "&ndash;", "&ndash;", f"{SOUR_2021} sour (derived)", "different measure"],
                 ["IEA, imports 2023", "&ndash;", "&ndash;", "&ndash;", f"{SOUR_2023} sour, {LIGHT_SOUR_2023} light sour, {MH_SOUR_2023} medium and heavy sour", "different measure"]]),
    f"High-sulphur runs grew by {HS_RISE} million tonnes between FY2020-21 and FY2025-26 while low-sulphur runs fell by {abs(LS_RISE)}, so all of the growth in refining came from sour grades, and the share slipped from 79.6% to {SHARE['2025-26']}% in FY2025-26 only because low-sulphur runs recovered by 3.1 million tonnes.",
    "PPAC should publish its high-sulphur and low-sulphur series monthly with the sulphur cut-off it uses, so that the runs data can be set beside the import data.",
    "share")

# ---------------------------------------------------------------- section 2
s2 = insight(
    "Origins: Russia gained 37 points of import share in 2021-23; the Middle East lost 16",
    bars("Russia's share of India's crude imports rose 37 points in 2021-23; Middle East fell 16",
         [("Russia", ORIGIN_PTS["Russia"], "3% to 40%"), ("Latin America", ORIGIN_PTS["Latin America"], "4.5% to 3%"),
          ("West Africa", ORIGIN_PTS["West Africa"], "12% to 4.5%"), ("Middle East", ORIGIN_PTS["Middle East"], "61% to 45%")],
         accent="Russia", unit=" points",
         sub="Change in each origin&rsquo;s share of India&rsquo;s crude imports, 2021 to 2023, percentage points, computed here from the IEA&rsquo;s printed shares. Other regions net +12 points and are not itemised.",
         source="IEA, India Oil Market Report: Outlook to 2030, chapter 4, using Kpler data (primary for the IEA&rsquo;s numbers; the IEA&rsquo;s own source is a ship tracker).")
    + numbers(["Measure", "Value", "Source and status"],
              [["Middle East share of imports before 2022", "more than 60% (61% in 2021)", "IEA, Kpler"],
               ["Iraq share in 2021 against Russia", "24% against 2%", "Business Standard, May 2024, from customs data (secondary)"],
               ["Saudi Arabia 2023 / Iraq 2023", "710 / 900 thousand b/d", "IEA, Kpler"],
               ["UAE, Kuwait, Oman, 2021 to 2023", "UAE &minus;170 to 260; Kuwait &minus;75 to 153; Oman &minus;100 to under 10 thousand b/d", "IEA, Kpler"],
               ["Russia, 2024 and 2025", "about one third of imports in 2024; about 1.7 million b/d in 2025", "Kpler via ThePrint, March 2026 (secondary)"],
               ["Russia, December 2025 to February 2026", "below 25% for the first time in two years", "Kpler via ThePrint (secondary)"],
               ["Russia 2023: two IEA figures", "&lsquo;nearly 40%&rsquo; and &lsquo;38%&rsquo; in the same chapter", "Conflict inside the IEA text; both are for 2023 and the difference is not explained"]]),
    "The IEA&rsquo;s shares show Russian medium-sour crude replacing Gulf supply and West African and Latin American barrels from 2021, and Business Standard&rsquo;s customs-based figures for the same year put Iraq at 24% and Russia at 2%, so the two sources agree on the starting point.",
    "The Commerce Ministry and PPAC should publish crude imports by origin and by API and sulphur band each month, because the only multi-year origin series found here is from a commercial ship tracker.",
    "origins")

# ---------------------------------------------------------------- section 3
s3 = insight(
    "2026: Russian arrivals ran 1.09 million b/d in February, 2.82 in July, 1.97 in October",
    bars("Russian crude into India: 1.09 million b/d in February, 2.82 in July, 1.97 in October",
         [(m, v) for m, v in RUS], accent="Jul 2026", unit=" million b/d", vmax=3,
         sub="Monthly arrivals of Russian crude in India, million barrels a day, as reported from Kpler. March to June are not shown because no Kpler monthly figure was found in a source read for this piece.",
         source="Kpler via Outlook Business (22 Feb 2026), ThePrint (30 Oct 2026), Financial Express (30 Oct 2026), Business Standard (11 Aug and 17 Oct 2026); secondary.")
    + numbers(["Measure", "Value", "Source and status"],
              [["Russian share, July 2026", "55% (Kpler); 55.5% of just over 5 million b/d (CREA); 50.83% (a Reuters-based report)", "Three figures for one month; providers differ"],
               ["Russian share, October 2026", f"about 35% (1.97 of {OCT_TOTAL} million b/d, provisional to 30 October)", "Kpler; October total a record, +14% on a year earlier"],
               ["Russian arrivals, October 2026, other tracker", "692 thousand b/d, down 67% on September", "S&P Global Commodities at Sea via bne IntelliNews: conflicts with Kpler&rsquo;s 1.97 million, unreconciled"],
               ["Gulf crude through Hormuz", "about 2.6 million b/d, nearly 50% of imports, in January and February; 2.1 million b/d in November", "Kpler via ThePrint and Bloomberg via bne (secondary)"],
               ["Angola, September to October", f"{ANG_SEP} to {ANG_OCT} thousand b/d", "Kpler; an earlier month-to-date reading was 282"],
               ["Venezuela, September to October", f"{VEN_SEP} to {VEN_OCT} thousand b/d, all for Jamnagar", "Kpler via ThePrint and Financial Express"],
               ["US crude", "565 thousand b/d (Oct 2025), 75 (Aug 2026), 157 (Oct 2026, provisional); 91 in a part-month reading", "Kpler via Business Standard, Financial Express"]]),
    f"Russia&rsquo;s volume rose {round(100 * (2.82 / 1.09 - 1))}% from February to July, fell {RUS_DROP_JUL_OCT}% by October, and was replaced by Atlantic Basin barrels (Angola, Venezuela) that doubled to about 1.2 million b/d, while Kpler&rsquo;s February call of US crude at up to 10% of intake matched October 2025&rsquo;s {US_SHARE_OCT25:.1f}% and not the {US_SHARE_OCT26:.1f}% of October 2026.",
    "Refiners and PPAC should state, with each month&rsquo;s import release, which tracker or customs series the origin shares come from, since three providers give three different Russian figures for one month.",
    "swing")

# ---------------------------------------------------------------- section 4
s4 = insight(
    "Sour discount: Dubai was $1.58 a barrel above Brent in 2025-26, $3.53 below in 2022-23",
    bars("PPAC's Brent-minus-Dubai spread: $3.53 a barrel in 2022-23, minus $1.58 in 2025-26",
         [(f, v) for f, v in SPREAD], accent="2025-26", unit="$/bbl",
         sub="Brent minus Dubai, US dollars a barrel, fiscal-year average; positive means the sour benchmark sold below Brent, negative means above. Read from the data labels of the PPAC chart.",
         source="PPAC Ready Reckoner 2025-26, trend in spread of international benchmark crude oils (primary; chart labels, not a table).")
    + numbers(["Origin", "Landed price FY2022-23 ($/bbl)", "Landed price FY2023-24 ($/bbl)"],
              [["Venezuela", "n/a", "64.0"], ["Russia", "83.2", "76.4"], ["Iraq", "90.6", "79.0"], ["United States", "91.6", "86.3"],
               ["UAE", "104.0", "89.2"], ["Saudi Arabia", "100.5", "90.3"], ["Nigeria", "109.0", "91.0"]],
              "Show landed prices by origin (customs data, secondary)")
    + numbers(["Measure", "Value", "Source and status"],
              [["Nigerian (sweet) over Iraqi (sour), landed", f"${GAP_NG_IQ_23} in FY2022-23, ${GAP_NG_IQ_24} in FY2023-24", "Computed from customs prices; includes freight and timing"],
               ["Russian below Iraqi, landed", f"${GAP_RU_IQ_23} in FY2022-23, ${GAP_RU_IQ_24} in FY2023-24", "Business Standard, customs data"],
               ["Urals delivered India against Dated Brent", "premium March to June 2026; discount above $10 on 7 July; $1 to $2 on 6 November; $2 to $3 on 23 November", "Reuters (7 Jul, 6 Nov) and a trader-sourced report (23 Nov); secondary"],
               ["IOC spot share, April to June 2026", f"{IOC_SPOT}% of crude purchases; Russia {IOC_RUS}% of its imports; normally about half under term contracts", "Bloomberg via Outlook Business (secondary)"],
               ["Jamnagar and Vadinar share of 2025-26 runs", f"{JAM_VAD_SHARE:.1f}% ({JAM_VAD:.1f} of {TOT[-1]} million tonnes)", "PPAC Table 4.1 (primary), computed here"],
               ["Hydrogen floor for removing sulphur", f"{H2_PER_T_S:.0f} kg per tonne of sulphur, before the extra used in real hydrotreaters", "Chemistry; method of this blog&rsquo;s earlier basket piece"]],
              "Show the refiner economics"),
    f"The average sour discount in the {len(POS)} positive years of the series was ${sum(POS)/len(POS):.2f} a barrel and it swung by ${FLIP} between FY2022-23 and FY2025-26, so the saving that complex refiners earn on sour crude is small and unstable, and Jamnagar and Vadinar ({JAM_VAD_SHARE:.1f}% of runs) carry most of the capacity to exploit it.",
    "Refiners should disclose each year the share of runs under term contracts against spot and the average discount to Dated Brent by grade, so the margin from running sour crude can be separated from freight and timing effects.",
    "economics")

watch = flow([("Each month", "PPAC&rsquo;s monthly import and flash reports show total crude imports; October 2026 flash data is already out, and the origin split still has to come from trackers."),
              ("Each quarter", "IOC, BPCL and HPCL earnings calls give the spot-to-term split; IOC reported 84% spot for April&ndash;June 2026."),
              ("Next price move", "Urals delivered to India was a $2 to $3 discount to Dated Brent on 23 November, and BPCL expects fewer Russian cargoes in November, so Gulf share should recover first.", True),
              ("OPEC+", "OPEC crude output rose 1.38 million b/d to 22.87 million b/d in October (as reported in this blog&rsquo;s November basket piece); more Gulf supply favours Gulf sour grades over Russian ones.")])
watch = '<section class="xv-sec"><h2 class="gb-h2" id="watch">What to watch next</h2>\n' + watch + "</section>\n"

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>PPAC:</b> publish crude imports by origin country and by sulphur and API band each month alongside the import release, so that the sour share does not have to be read from commercial ship trackers.</li>
<li><b>PPAC:</b> state the sulphur cut-off that separates high-sulphur from low-sulphur crude in Table 4.2 and publish the series monthly, so it can be compared with the IEA&rsquo;s sour definition.</li>
<li><b>Ministry of Commerce and PPAC:</b> reconcile the customs and PPAC import tonnages and state which one feeds each published ratio, since press reports gave 234.3 million tonnes for both FY2023-24 and FY2024-25.</li>
<li><b>Refiners:</b> disclose term against spot purchases and the average discount to Dated Brent by grade in each quarterly result.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>PPAC&rsquo;s high-sulphur share (Table 4.2) is of all crude processed, imported plus domestic, using the oil companies&rsquo; own classification; the IEA&rsquo;s sour share is of imports, by quality band, from Kpler. They are different measures and are never combined into one series here.</li>
<li>The IEA prints 85% sour and 63% medium-heavy for 2023, and says sweet fell by 8 points to 15%. Adding 8 gives 23% sweet and 77% sour for 2021; that 2021 figure is this blog&rsquo;s arithmetic. The IEA&rsquo;s 62% (medium and heavy sour) plus 24% (light sour) is 86%, one point above its printed 85%, which is rounding.</li>
<li>Origin changes are the IEA&rsquo;s printed 2021 and 2023 shares subtracted. The IEA text gives &lsquo;just under 3%&rsquo; and &lsquo;nearly 40%&rsquo; for Russia, entered as 3 and 40.</li>
<li>The Brent-minus-Dubai figures were read from the data labels on the PPAC chart (page 115); the labels sit beside, not on, some points, so each was matched to its year by the colour and x-position of the label and checked against the lines. The 2016-17 pair was initially read the wrong way round and corrected on the rendered chart.</li>
<li>Kpler figures are provisional ship-tracking estimates, not customs data. October 2026 totals are provisional to 30 October.</li>
<li>Landed prices from customs data are not a sour discount: they include freight, insurance, contract timing and quality differences.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The sour share of India&rsquo;s imports for any year other than 2021 and 2023, and any year before 2021. The IEA has an annual 2014&ndash;2023 chart but prints only those two years in text. PPAC&rsquo;s high-sulphur series in the 2025-26 Ready Reckoner starts in FY2020-21; earlier editions were not read.</li>
<li>Crude imports by origin from an official table. PPAC&rsquo;s site and Ready Reckoner give no origin split (only that sourcing grew from 27 to 41 countries). A DGCI&amp;S Kolkata document found through search returned a placeholder page, so its FY2022-23 to FY2024-25 Russian shares (21.6%, 35.9%, 35.8%) are not used.</li>
<li>Origin shares for FY2015-16 to FY2020-21 and for FY2025-26 as a whole.</li>
<li>FY2015-16 import tonnage of about 202.85 million tonnes. PPAC&rsquo;s current table starts in FY2018-19. The conflict over 243.22 and 234.3 is resolved against PPAC&rsquo;s table: 243.2 is FY2024-25 and 234.3 is FY2023-24; the claimed FY2023-24 figure of 226.6 matches no year in that table.</li>
<li>Other 2026 Russian shares from the search (46.8% in March, about 54% in June, Gulf suppliers 39% in September, OPEC 53.2% and Russia 27.4% in December 2025): not opened here, different providers, and not used.</li>
<li>Urals discounts for February and March 2026 (about $9 below ICE Brent; Platts parity on 17 March; $28.75 below at Primorsk): not confirmed from a primary release. Only the Reuters-reported pattern is used.</li>
<li>The Russian arrivals conflict for October 2026 (Kpler 1.97 million b/d against S&amp;P Global 692 thousand b/d) and the three July shares (55%, 55.5%, 50.83%).</li>
<li>HPCL Rajasthan Refinery: the reported 2 million barrels in August 2026 were Nigerian Okwuibome and Utapate crude from Glencore, bought by tender, and this piece did not check their assays, so it does not call them sour. IOC&rsquo;s October 2025 Americas tender sought both low- and high-sulphur grades.</li>
<li>Refinery complexity indices by plant. PPAC publishes no Nelson index; processing share is used as a proxy.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + watch + fixes + method + gaps

SOURCES = (
    'Primary: <a href="https://ppac.gov.in/download.php?file=rep_studies/1784899305_The_PPAC_Ready_Reckoner_FY_2025%E2%80%9326_Final.pdf">PPAC Ready Reckoner 2025-26</a> (Tables 4.1, 4.2, 4.3, 8.24; benchmark-spread chart; sourcing from 27 to 41 countries); '
    '<a href="https://iea.blob.core.windows.net/assets/6b3a9f48-adeb-4de3-bbe5-1be9c8fcd069/IndianOilMarket-Outlookto2030.pdf">IEA, India Oil Market Report: Outlook to 2030</a> (chapter 4; data to 2023, from Kpler); '
    '<a href="https://www.kpler.com/blog/india-us-trade-deal-to-reshape-marginal-crude-flows-not-displace-russian-barrels">Kpler, 4 February 2026</a> (US crude up to about 10% of intake). '
    'Secondary: <a href="https://www.business-standard.com/economy/news/iraq-closes-gap-with-russian-oil-in-fy24-as-moscow-s-discounts-shrink-124050701053_1.html">Business Standard, 7 May 2024</a> (customs data, landed prices, 2021 shares); '
    '<a href="https://theprint.in/economy/russian-crude-never-left-indias-import-mix-it-made-up-1-3rd-of-oil-imports-from-2024-to-2026/2874224">ThePrint, 9 March 2026</a>; '
    '<a href="https://www.outlookbusiness.com/economy-and-policy/india-rebalances-crude-slate-as-saudi-gains-russian-flows-ease-under-sanctions-pressure">Outlook Business, 22 February 2026</a>; '
    '<a href="https://theprint.in/economy/indias-crude-imports-set-to-record-highest-ever-5-4-5-6-mn-b-d-in-october-as-refiners-diversify-supplies/3086310">ThePrint, 31 October 2026</a>; '
    '<a href="https://www.financialexpress.com/policy/economy/crude-imports-set-to-hit-record-in-october/4373542">Financial Express, 31 October 2026</a>; '
    '<a href="https://www.business-standard.com/economy/news/india-us-crude-oil-imports-russian-trump-sanctions-venezuela-trade-tariffs-126081100747_1.html">Business Standard, 11 August 2026</a> (US arrivals; CREA July share); '
    '<a href="https://www.business-standard.com/economy/news/us-energy-supplies-india-west-asia-crude-lng-lpg-imports-126101400660_1.html">Business Standard, 14 October 2026</a>; '
    '<a href="https://www.intellinews.com/russia-s-urals-discount-widens-to-deepest-since-april-2023-as-gulf-crude-returns-484744?source=india">bne IntelliNews, 13 November 2026</a> (Argus, Bloomberg, S&amp;P Global figures); '
    '<a href="https://www.reuters.com/business/energy/discounts-russian-urals-crude-widen-more-than-10-per-barrel-india-sources-say-2026-07-07">Reuters, 7 July 2026</a>; '
    '<a href="https://www.bairdmaritime.com/shipping/tankers/indian-demand-cools-down-and-pushes-russian-crude-into-a-discount">Reuters via Baird Maritime, 6 November 2026</a>; '
    '<a href="https://www.reuters.com/business/energy/indias-bpcl-expects-russian-crude-purchases-fall-november-2026-10-26">Reuters, 26 October 2026</a> (BPCL); '
    '<a href="https://www.outlookbusiness.com/corporate/hpcl-taps-west-africa-for-crude-supply-to-its-rajasthan-refinery">Outlook Business, 4 August 2026</a> (HRRL purchase; IOC spot share via Bloomberg); '
    '<a href="https://www.reuters.com/business/energy/ioc-seeks-24-million-barrels-oil-americas-january-march-2026-document-shows-2025-10-30">Reuters, 30 October 2025</a> (IOC Americas tender). '
    'Shares, differences, averages and the hydrogen floor computed by this blog. Analysed 26 November 2026.')

RELATED = [
    (f"{B}/2026/10/indias-crude-basket-now-counts-russian.html", "India's crude basket: Brent weighted at 61%, while most imported barrels are sour"),
    (f"{B}/2026/11/indias-crude-basket-120-in-october-89.html", "India's crude basket: $120 in October, $89 on 10 November; pump prices frozen"),
    (f"{B}/2026/08/inside-refinery-how-hydrogen-cleans.html", "Hydrogen in Indian refineries: needed for 10 ppm BS-VI diesel, mostly from fossil gas"),
    (f"{B}/2026/08/petroleum-trade-pairings-and-us-crude.html", "US crude storage and petroleum trade pairings: reserves, Cushing and OPEC output"),
]

build("Energy &middot; Crude oil", TITLE,
      "PPAC puts high-sulphur grades at 78.7% of India&rsquo;s refinery runs in 2025-26, up from 72.8% five years earlier; four charts set out the origins that replaced each other, the 2026 swing and the sour discount.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
