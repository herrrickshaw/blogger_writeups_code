"""Global LNG in 2026 after the Strait of Hormuz disruption, and QatarEnergy's October 2026 US LNG contracts.
Build from the repo root:  python3 out/research/lng-hormuz-2026/build.py
Every figure is from the source named beside it, or computed here with an assert. Written 15 Nov 2026."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, _fig, bars, flow, insight, numbers, sources_block, top_line  # noqa: E402

OUT = ROOT / "out/post-global-lng-2026-hormuz-supply-loss.html"
B = "https://blog.vertistratsolution.com"

# ---- IEA, Global Gas Security Review 2026 incl. Gas Market Report Q4-2026, 2 Nov 2026 ----
# https://www.iea.org/files/42bb838f-d20d-4815-8554-32146033967d/GlobalGasSecurityReview2026.pdf
IEA_FCST_2026 = -3                  # % global LNG supply 2026, "steepest yearly decline on record" (about -20 bcm)
GULF_LOSS_BCM = 60                  # "over 60 bcm" Qatar+UAE loadings y-o-y, March-October
NONGULF_GAIN_BCM, NONGULF_PCT = 40, 14   # "more than 40 bcm" / 14%, March-October, "two-thirds" of the Gulf decline
GLOBAL_PROD_FALL_BCM, GLOBAL_PROD_FALL_PCT = 20, 6   # "around 20 bcm" / 6%, March-October (the winter-outlook section says 5%)
DELIVERED_JAN_OCT_BCM, DELIVERED_JAN_OCT_PCT = 62, 63   # delivered Qatar+UAE LNG, Jan-Oct
JKM_Q3, JKM_Q3_UP = 25.60, 95       # USD/MBtu, Q3 2026 Asian spot (Platts JKM), % y-o-y
TTF_Q3, TTF_Q3_UP = 21.5, 90        # USD/MBtu, Q3 2026 TTF, "almost 90%" y-o-y
OIL_LO, OIL_HI = 12, 14             # USD/MBtu, estimated oil-indexed LNG, Q3 2026, "around 30% above Q3 2025"
TTF_MAR_OCT, JKM_MAR_OCT = 20, 21.5  # USD/MBtu, March-October averages ("close to 20", "21.5")
WINTER_CASE1, WINTER_CASE2 = -3, -7  # % y-o-y global LNG supply, winter 2026/27: reopening from Jan 2027 / closed to end-March 2027
PK_QATAR_SHARE_2025 = 98            # % of Pakistan's 2025 LNG imports from Qatar
PK_JAN_OCT = -56                    # % y-o-y Pakistan LNG imports, Jan-Oct (4.5 bcm)
CHINA_JAN_OCT_IEA = -10             # % y-o-y China, Jan-Oct (IEEJ has -5.8% for Jan-Sep)
EU_Q1Q3_IEA = -3.5                  # % y-o-y Europe, Q1-Q3
NFE_DELAY = "H1 2027 at the earliest, from end-2026"
RAS_LAFFAN_TRAINS_MTPA = 12.8       # two trains damaged 18-19 March (17.5 bcm/yr)
CUM_LOSS_2026_30_BCM, CUM_LOSS_SHARE = 150, 15   # cumulative 2026-2030 supply loss; 15% of new supply
FLEX_2016, FLEX_2025 = 29, 50       # % destination-flexible contracts ("more than 50% in 2025")
QATAR_CARGOES_MAR_SEP = 40          # about 40 cargoes shipped March-September, all to Asia
assert abs(GULF_LOSS_BCM - NONGULF_GAIN_BCM - GLOBAL_PROD_FALL_BCM) == 0     # 60 - 40 = 20: the three IEA figures are consistent
assert 0.6 < NONGULF_GAIN_BCM / GULF_LOSS_BCM < 0.7                           # "essentially offsetting two-thirds"

# ---- IEEJ, LNG Review October 2026 (published Nov 2026) ----
# https://eneken.ieej.or.jp/data/13639.pdf
GLOBAL_IMPORTS_MT, GLOBAL_IMPORTS_PCT = 303, -1.8   # Jan-Sep 2026
QATAR_9M_2026, QATAR_9M_2025 = 22, 60               # Mt exports, Jan-Sep
US_ADD, CA_ADD, RU_ADD = 16, 7, 2                   # Mt added, Jan-Sep, y-o-y
JP, KR, CN, TW = -4.7, -6.4, -5.8, 6.2              # % y-o-y imports, Jan-Sep 2026
NEA4_PCT = -4.2
LANDED = {"Japan": 11.98, "Korea": 12.09, "China": 11.72, "Taiwan": 13.95}   # USD/MBtu, 9-month weighted landed price
TTF_28OCT_USD = 32.86               # USD/MBtu, TTF November contract settlement 28 Oct 2026 (EUR 100.72/MWh; converted by IEEJ)
QATAR_DROP = QATAR_9M_2025 - QATAR_9M_2026
REPLACED = US_ADD + CA_ADD + RU_ADD
assert QATAR_DROP == 38 and REPLACED == 25

# ---- Cheniere, press release 22 Oct 2026 (https://lngir.cheniere.com/news-events/press-releases/detail/348/cheniere-signs-long-term-sale-and-purchase-agreements-to) ----
CHENIERE_MTPA, CHENIERE_SPL, CHENIERE_CCL, CHENIERE_FID_CONDITIONAL = 4, 2, 2, 1
# ---- Woodside, ASX announcement 29 Oct 2026 (https://www.woodside.com/docs/default-source/asx-announcements/2026/055-woodside-signs-20-year-lng-supply-agreement-with-qatarenergy.pdf) ----
WOODSIDE_MTPA = 3                   # "up to 3 Mtpa", 20 years; Louisiana LNG first LNG 2029, three trains 16.5 Mtpa
# ---- Reuters, 29 Oct 2026 (one page; deliveries: Cheniere 2031, Woodside 2030 per QatarEnergy; 7 mtpa together; "There's more to come") ----
# https://www.reuters.com/business/energy/qatarenergy-buys-us-other-lng-hedge-future-hormuz-disruptions-2026-10-29
QATAR_CAPACITY_MTPA = 77            # QatarEnergy LNG, 14 trains: https://www.qatarenergylng.qa/english/About-Us (also Reuters, 29 Oct 2026)
assert CHENIERE_SPL + CHENIERE_CCL == CHENIERE_MTPA
TOTAL_US = CHENIERE_MTPA + WOODSIDE_MTPA
assert TOTAL_US == 7
SHARE_OF_CAP = 100 * TOTAL_US / QATAR_CAPACITY_MTPA
assert round(SHARE_OF_CAP) == 9
DAMAGED_SHARE = 100 * RAS_LAFFAN_TRAINS_MTPA / QATAR_CAPACITY_MTPA
assert round(DAMAGED_SHARE) == 17

# ---- price ratios ----
RATIO_LO, RATIO_HI = JKM_Q3 / OIL_HI, JKM_Q3 / OIL_LO
assert round(RATIO_LO, 1) == 1.8 and round(RATIO_HI, 1) == 2.1

# ---- other importers ----
# Egypt: Energy Research Unit via bne IntelliNews, 3 Nov 2026 (single secondary page): 10.52 Mt vs 5.70 Mt, Jan-Sep
# https://www.intellinews.com/egypt-s-lng-imports-top-2025-record-as-cairo-pushes-east-mediterranean-gas-hub-ambitions-481337
EGYPT_2026, EGYPT_2025 = 10.52, 5.70
EGYPT_PCT = 100 * (EGYPT_2026 / EGYPT_2025 - 1)
assert round(EGYPT_PCT) == 85
# Europe (the source says Europe, not the EU): Attaqa energy research unit via Egypt Oil & Gas, 17 Oct 2026 (single secondary page): 87.37 Mt vs 89.96 Mt, Jan-Sep
# https://egyptoil-gas.com/news/europes-lng-imports-drop-13-to-21-52-mmt-in-q3-2026
EU_2026, EU_2025 = 87.37, 89.96
EU_PCT = 100 * (EU_2026 / EU_2025 - 1)
assert round(EU_PCT, 1) == -2.9
# India: PPAC data as reported by Financial Express, 27 Oct 2026: 18,189 vs 17,414 MMSCM, April-September; article says 4.4%
# https://www.financialexpress.com/policy/economy-india-spends-1-6-bn-extra-on-lng-imports-in-h1-as-global-prices-flare-up-4370672
IN_2026, IN_2025, IN_REPORTED = 18189, 17414, 4.4
IN_PCT = 100 * (IN_2026 / IN_2025 - 1)
assert abs(IN_PCT - IN_REPORTED) < 0.1
# India supplier shares: Kpler via Economic Times, 22 Oct 2026 (March-September): Qatar 45% -> 3%; US, Oman, Nigeria 25% -> 68%
# https://m.economictimes.com/industry/energy/oil-gas/indias-lng-imports-surge-9-amid-supply-gap-from-qatar-and-uae-with-us-oman-and-nigeria-leading-the-charge/articleshow/135125222.cms
IN_QATAR_BEFORE, IN_QATAR_NOW, IN_3SUP_BEFORE, IN_3SUP_NOW = 45, 3, 25, 68

# ======================================================================================================
top = top_line([
    (f"{IEA_FCST_2026}%", f" is the IEA&rsquo;s forecast for global LNG supply in 2026, the steepest yearly fall on record. "
     f"Qatar and UAE loadings fell by over {GULF_LOSS_BCM} bcm from March to October; output elsewhere rose {NONGULF_PCT}% and offset about two-thirds."),
    (f"${JKM_Q3:.2f}/MBtu", f" was the average Asian spot LNG price in Q3 2026, up {JKM_Q3_UP}% on a year earlier, "
     f"against an estimated ${OIL_LO}-{OIL_HI}/MBtu for oil-indexed LNG."),
    (f"{TOTAL_US} Mtpa", f" is the maximum volume of US LNG in QatarEnergy&rsquo;s October contracts with Cheniere (up to {CHENIERE_MTPA}, 22 October) and Woodside "
     f"(up to {WOODSIDE_MTPA}, 29 October), with deliveries due from 2030 and 2031."),
])

# ---- 1. supply lost and replaced ----
LQ, LUS, LCA, LRU = "Qatar <small>exports</small>", "United States", "Canada", "Russia"
s1 = insight(
    f"Global LNG supply: forecast to fall {-IEA_FCST_2026}% in 2026 as Qatar and UAE loadings drop over {GULF_LOSS_BCM} bcm",
    bars(f"Qatar&rsquo;s nine-month exports fell {QATAR_DROP} Mt; the US, Canada and Russia added {REPLACED} Mt",
         [(LQ, -QATAR_DROP, "", f"-{QATAR_DROP} Mt ({QATAR_9M_2025} to {QATAR_9M_2026})"), (LUS, US_ADD), (LCA, CA_ADD), (LRU, RU_ADD)],
         accent=LQ, unit=" Mt",
         sub="Change in LNG exports, January to September 2026 against the same months of 2025, million tonnes. "
             "Only the three exporters IEEJ names are shown.",
         source="IEEJ, LNG Review October 2026 (Nov 2026).")
    + numbers(["IEA measure (Global Gas Security Review, 2 Nov 2026)", "Value"],
              [["Qatar + UAE loadings, March to October, y-o-y", f"over {GULF_LOSS_BCM} bcm lower"],
               ["Non-Gulf LNG production, March to October, y-o-y", f"+{NONGULF_PCT}%, more than {NONGULF_GAIN_BCM} bcm"],
               ["Global LNG production, March to October, y-o-y", f"-{GLOBAL_PROD_FALL_PCT}%, around {GLOBAL_PROD_FALL_BCM} bcm"],
               ["Delivered Qatar + UAE LNG, January to October, y-o-y", f"about {DELIVERED_JAN_OCT_BCM} bcm lower ({DELIVERED_JAN_OCT_PCT}%)"],
               ["Global LNG supply, full year 2026, forecast", f"{IEA_FCST_2026}%, about 20 bcm"],
               ["Cumulative LNG supply lost 2026 to 2030, estimate", f"{CUM_LOSS_2026_30_BCM} bcm, {CUM_LOSS_SHARE}% of new supply due in the period"]],
              "Show the IEA volume figures (bcm)"),
    f"New US, Canadian and African capacity replaced about two-thirds of the Gulf loss, which left global LNG production around {GLOBAL_PROD_FALL_BCM} bcm lower from March to October.",
    "Importers should plan 2026/27 winter purchases on the IEA&rsquo;s two winter cases, a fall in global LNG supply of around {0}% or {1}%, rather than on a return to Gulf loadings.".format(-WINTER_CASE1, -WINTER_CASE2),
    "supply")

# ---- 2. prices ----
LJ, LT, LO = "Asian spot LNG <small>Platts JKM, up %d%%</small>" % JKM_Q3_UP, "European hub <small>TTF, up almost %d%%</small>" % TTF_Q3_UP, \
    "Oil-indexed LNG <small>estimate, about 30% above Q3 2025</small>"
s2 = insight(
    f"LNG prices in Q3 2026: Asian spot ${JKM_Q3:.2f}/MBtu, oil-indexed ${OIL_LO}-{OIL_HI}/MBtu",
    bars("Asian spot LNG averaged 1.8 to 2.1 times the estimated oil-indexed price in Q3 2026",
         [(LJ, JKM_Q3, "", f"${JKM_Q3:.2f}/MBtu"), (LT, TTF_Q3), (LO, (OIL_LO, OIL_HI))],
         accent=LJ, unit="$/MBtu",
         sub="Average price in the third quarter of 2026, USD per million British thermal units. Oil-indexed is an IEA estimate range.",
         source="IEA, Global Gas Security Review 2026 (2 Nov 2026), Gas Market Report Q4-2026.")
    + numbers(["Price measure", "USD/MBtu", "Source and period"],
              [["TTF, March to October average", f"close to {TTF_MAR_OCT}", "IEA; up almost 70% y-o-y"],
               ["Asian spot, March to October average", f"{JKM_MAR_OCT}", "IEA; up almost 80% y-o-y"],
               ["Landed price, Japan", f"{LANDED['Japan']}", "IEEJ; weighted average, January to September"],
               ["Landed price, Korea", f"{LANDED['Korea']}", "IEEJ; same basis"],
               ["Landed price, China", f"{LANDED['China']}", "IEEJ; same basis"],
               ["Landed price, Taiwan", f"{LANDED['Taiwan']}", "IEEJ; same basis"],
               ["TTF November contract, settlement 28 October", f"{TTF_28OCT_USD}", "IEEJ; EUR 100.72/MWh converted by IEEJ"]],
              "Show other price readings"),
    "Buyers on oil-indexed contracts paid well under the spot price in Q3, but the IEA expects oil-linked prices to rise in Q4 because oil prices reach contract formulas with a lag of five to six months.",
    "LNG buyers should budget winter contract costs on oil prices of five to six months earlier, not on the Q3 contract price.",
    "prices")

# ---- 3. importers ----
rows3 = [("Egypt <small>Jan-Sep, Energy Research Unit</small>", EGYPT_PCT, "", "+%d%%" % round(EGYPT_PCT)),
         ("Taiwan <small>Jan-Sep, IEEJ</small>", TW, "", "+%s%%" % TW),
         ("India <small>Apr-Sep, PPAC volume</small>", IN_REPORTED, "", "+%s%%" % IN_REPORTED),
         ("Europe <small>Jan-Sep, Attaqa, as reported</small>", round(EU_PCT, 1), "", "%s%%" % round(EU_PCT, 1)),
         ("Japan <small>Jan-Sep, IEEJ</small>", JP, "", "%s%%" % JP),
         ("China <small>Jan-Sep, IEEJ</small>", CN, "", "%s%%" % CN),
         ("Korea <small>Jan-Sep, IEEJ</small>", KR, "", "%s%%" % KR),
         ("Pakistan <small>Jan-Oct, IEA</small>", PK_JAN_OCT, "", "%s%%" % PK_JAN_OCT)]
s3 = insight(
    f"LNG imports in 2026: Pakistan down {-PK_JAN_OCT}%, Egypt up about 85%, China down {-CN}%",
    bars("Pakistan, 98% supplied by Qatar in 2025, imported 56% less; Egypt imported about 85% more",
         rows3, accent=["Pakistan <small>Jan-Oct, IEA</small>", "Egypt <small>Jan-Sep, Energy Research Unit</small>"], unit="%",
         sub="Change in LNG imports against the same months of 2025, per cent. Periods differ by row, as labelled.",
         source="IEEJ LNG Review October 2026; IEA Global Gas Security Review 2026; Energy Research Unit via bne IntelliNews (3 Nov 2026); "
                "Attaqa via Egypt Oil &amp; Gas (17 Oct 2026); PPAC via Financial Express (27 Oct 2026).")
    + numbers(["Importer", "Period", "Change", "Source"],
              [["Global imports", "Jan-Sep", f"{GLOBAL_IMPORTS_PCT}% ({GLOBAL_IMPORTS_MT} Mt)", "IEEJ"],
               ["Four Northeast Asian markets", "Jan-Sep", f"{NEA4_PCT}% (141.35 Mt)", "IEEJ"],
               ["Egypt", "Jan-Sep", f"{EGYPT_2025:.2f} to {EGYPT_2026} Mt", "Energy Research Unit via bne IntelliNews"],
               ["India", "Apr-Sep", f"{IN_2025:,} to {IN_2026:,} MMSCM", "PPAC via Financial Express"],
               ["India, share of imports from Qatar", "Mar-Sep", f"{IN_QATAR_BEFORE}% to {IN_QATAR_NOW}%", "Kpler via Economic Times"],
               ["India, share from US, Oman and Nigeria", "Mar-Sep", f"{IN_3SUP_BEFORE}% to {IN_3SUP_NOW}%", "Kpler via Economic Times"],
               ["Europe", "Q1-Q3", f"{EU_Q1Q3_IEA}%", "IEA"],
               ["Europe", "Jan-Sep", f"{EU_2025} to {EU_2026} Mt", "Attaqa via Egypt Oil &amp; Gas"],
               ["China", "Jan-Oct", f"{CHINA_JAN_OCT_IEA}% (7 bcm)", "IEA"],
               ["Pakistan, Qatar share of 2025 LNG imports", "2025", f"{PK_QATAR_SHARE_2025}%", "IEA"]],
              "Show the numbers and sources"),
    f"Pakistan took {PK_QATAR_SHARE_2025}% of its 2025 LNG from Qatar and cut imports most, while India replaced Qatari cargoes with US, Omani and Nigerian supply and imported {IN_REPORTED}% more.",
    "Importers that depend on one exporter should contract a second, destination-flexible source before the next outage.",
    "importers")

# ---- 4. Qatar's pivot ----
fl = flow([
    ("End of February to 2 March", "The Middle East conflict begins at the end of February. QatarEnergy stops LNG production on 2 March; force majeure is declared."),
    ("18-19 March", f"Missile attacks on Ras Laffan damage two liquefaction trains of {RAS_LAFFAN_TRAINS_MTPA} Mtpa combined, about {DAMAGED_SHARE:.0f}% of Qatar&rsquo;s {QATAR_CAPACITY_MTPA} Mtpa."),
    ("March to September", f"Qatar ships around {QATAR_CARGOES_MAR_SEP} LNG cargoes, all to Asia. January to September exports are {QATAR_9M_2026} Mt, against {QATAR_9M_2025} Mt a year earlier."),
    ("22 October", f"Cheniere signs two SPAs for up to {CHENIERE_MTPA} Mtpa through 2054: {CHENIERE_SPL} Mtpa each from Sabine Pass and Corpus Christi, "
                   f"free on board, priced at Henry Hub plus a fixed fee. {CHENIERE_FID_CONDITIONAL} Mtpa depends on a Sabine Pass expansion decision. Deliveries start in the early 2030s.", True),
    ("29 October", f"Woodside signs for up to {WOODSIDE_MTPA} Mtpa for 20 years from Louisiana LNG, free on board, starting at Train 2 and reaching {WOODSIDE_MTPA} Mtpa at Train 3. "
                   "First LNG at the plant is targeted for 2029. Reuters reports QatarEnergy&rsquo;s chief executive saying &ldquo;there&rsquo;s more to come&rdquo;.", True),
    ("2027 and after", f"The IEA expects North Field East, Qatar&rsquo;s 43.5 bcm/yr expansion, to start up in {NFE_DELAY}."),
])
s4 = insight(
    f"QatarEnergy&rsquo;s October purchases: up to {TOTAL_US} Mtpa of US LNG, delivered from 2030 and 2031",
    _fig(f"Qatar signed for up to {TOTAL_US} Mtpa of US LNG on 22 and 29 October, for delivery from 2030", "", fl,
         "IEA Global Gas Security Review 2026; IEEJ LNG Review October 2026; Cheniere press release, 22 Oct 2026; Woodside ASX announcement, 29 Oct 2026; Reuters, 29 Oct 2026."),
    f"The contracts place up to {TOTAL_US} Mtpa of Qatar&rsquo;s portfolio outside the Strait of Hormuz, about {SHARE_OF_CAP:.0f}% of its {QATAR_CAPACITY_MTPA} Mtpa capacity, from 2030, and add no LNG for this winter.",
    "Asian and European buyers of Qatari LNG should ask QatarEnergy which sources and delivery points will back their contracts during a Gulf outage.",
    "qatar")

fixes = """<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>International Energy Agency and member governments:</b> agree in advance the triggers for gas demand reduction and joint action in a Gulf LNG outage.</li>
<li><b>QatarEnergy:</b> publish monthly loadings and the scope of its force majeure by buyer, so importers can plan winter cargoes.</li>
<li><b>India&rsquo;s Ministry of Petroleum and Natural Gas, through PPAC:</b> publish monthly LNG imports by supplier country and contract type.</li>
<li><b>European Commission:</b> publish the gas demand reduction that applies if EU storage falls below a stated level in January; the IEA says storage could end the winter at record lows.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
"""

method = f'''<details class="xv-n"><summary>Method</summary>
<ul>
<li>Volumes and prices are from the IEA Global Gas Security Review 2026 (2 November 2026) and the IEEJ LNG Review October 2026. Contract terms are from Cheniere&rsquo;s press release and Woodside&rsquo;s ASX announcement.</li>
<li>Computed here: Qatar&rsquo;s nine-month fall ({QATAR_9M_2025} to {QATAR_9M_2026} Mt = {QATAR_DROP} Mt); the three named exporters&rsquo; gain ({US_ADD}+{CA_ADD}+{RU_ADD} = {REPLACED} Mt); the {TOTAL_US} Mtpa total ({CHENIERE_MTPA}+{WOODSIDE_MTPA}); {SHARE_OF_CAP:.1f}% of Qatar&rsquo;s capacity; the price ratio of {RATIO_LO:.1f} to {RATIO_HI:.1f} ({JKM_Q3} divided by {OIL_HI} and by {OIL_LO}); Egypt (+{EGYPT_PCT:.1f}%), Europe ({EU_PCT:.1f}%) and India (+{IN_PCT:.2f}% from the volumes, reported as {IN_REPORTED}%).</li>
<li>Where the IEA gives a threshold (&ldquo;over 60 bcm&rdquo;, &ldquo;more than 40 bcm&rdquo;), the post keeps the threshold.</li>
</ul></details>
'''

gaps = f'''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li><b>Source disagreements.</b> The IEA gives the fall in global LNG production from March to October as 6% in one section and 5% in another, both about 20 bcm.</li>
<li><b>China and Ras Laffan.</b> For China, IEEJ shows {CN}% for January to September and the IEA {CHINA_JAN_OCT_IEA}% for January to October. Reports date the Ras Laffan damage to 18-19 March (IEA) or to April (one Indian outlet); the post uses the IEA date.</li>
<li><b>Mixed periods.</b> The importer chart combines January-September, April-September and January-October changes, each labelled. Egypt and Europe each rest on one secondary page. For India, PPAC volumes show +4.4% for April-September, while Kpler data reported by the Economic Times show +9% for March-September.</li>
<li><b>Contract volumes.</b> The Cheniere and Woodside volumes are maximums: one million tonnes a year of the Cheniere total depends on a Sabine Pass expansion decision, and Woodside&rsquo;s volume reaches {WOODSIDE_MTPA} Mtpa only when Train 3 starts.</li>
<li><b>Dates and prices.</b> Delivery dates are QatarEnergy&rsquo;s (2030 and 2031) as reported by Reuters; Cheniere says &ldquo;early 2030s&rdquo;. Contract prices beyond Cheniere&rsquo;s Henry Hub formula were not published.</li>
<li><b>Qatar&rsquo;s other purchases.</b> Reuters reports QatarEnergy buying other non-Gulf LNG as well; no other contract was confirmed here.</li>
<li><b>Current flows.</b> Tracker data on October loadings and the status of the Strait change daily and were not used for any figure.</li>
</ul></details>
'''

SRC = [
    ("https://www.iea.org/files/42bb838f-d20d-4815-8554-32146033967d/GlobalGasSecurityReview2026.pdf", "IEA, Global Gas Security Review 2026 including Gas Market Report Q4-2026, 2 November 2026"),
    ("https://eneken.ieej.or.jp/data/13639.pdf", "IEEJ, LNG Review October 2026, November 2026"),
    ("https://lngir.cheniere.com/news-events/press-releases/detail/348/cheniere-signs-long-term-sale-and-purchase-agreements-to", "Cheniere, SPAs with QatarEnergy, 22 October 2026"),
    ("https://www.woodside.com/docs/default-source/asx-announcements/2026/055-woodside-signs-20-year-lng-supply-agreement-with-qatarenergy.pdf", "Woodside, ASX announcement, 29 October 2026"),
    ("https://www.reuters.com/business/energy/qatarenergy-buys-us-other-lng-hedge-future-hormuz-disruptions-2026-10-29", "Reuters, 29 October 2026 (QatarEnergy purchases; one page)"),
    ("https://www.qatarenergylng.qa/english/About-Us", "QatarEnergy LNG, About Us (77 Mtpa, 14 trains)"),
    ("https://www.intellinews.com/egypt-s-lng-imports-top-2025-record-as-cairo-pushes-east-mediterranean-gas-hub-ambitions-481337", "bne IntelliNews, Egypt LNG imports, 3 November 2026 (secondary)"),
    ("https://egyptoil-gas.com/news/europes-lng-imports-drop-13-to-21-52-mmt-in-q3-2026", "Egypt Oil &amp; Gas citing Attaqa, 17 October 2026 (secondary)"),
    ("https://www.financialexpress.com/policy/economy-india-spends-1-6-bn-extra-on-lng-imports-in-h1-as-global-prices-flare-up-4370672", "Financial Express citing PPAC, 27 October 2026 (secondary)"),
    ("https://m.economictimes.com/industry/energy/oil-gas/indias-lng-imports-surge-9-amid-supply-gap-from-qatar-and-uae-with-us-oman-and-nigeria-leading-the-charge/articleshow/135125222.cms", "Economic Times citing Kpler, 22 October 2026 (secondary)"),
]
src_links = sources_block(SRC)

body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps + src_links

REL = [
    (f"{B}/2026/09/global-lng-trade-hit-record-437-million.html", "Global LNG trade: record 437 million tonnes in 2025, nearly double a decade ago"),
    (f"{B}/2026/08/europe-bought-record-amount-of-lng-and.html", "EU LNG imports: a record 146 bcm in 2025, nearly three-fifths from the US"),
    (f"{B}/2026/10/indias-cheapest-lng-capacity-is-extra.html", "LNG terminals in India: Dahej ran at 92% in April–May 2026, newer ones at 24–37%"),
    (f"{B}/2026/10/india-wants-15-of-its-energy-from-gas.html", "Gas in India's energy mix: share down from 7.5% to 7.0%, against a 15% target"),
    (f"{B}/2026/08/thermal-parity-is-dead-what-85-oil-and.html", "Oil-gas decoupling: $85 oil, a $7 gas ceiling and India's crude-linked formula"),
]

sources_text = ("Primary: IEA Global Gas Security Review 2026 (2 Nov 2026); IEEJ LNG Review October 2026; Cheniere release (22 Oct 2026); "
                "Woodside ASX announcement (29 Oct 2026); QatarEnergy LNG company page. Reuters (29 Oct 2026) is one page. "
                "Egypt, Europe and India figures come from single secondary pages and are labelled so. Forecasts are the IEA&rsquo;s; "
                "source disagreements are listed above.")

TITLE = "Global LNG in 2026: supply forecast down 3%, with Qatar contracting US LNG"
assert 55 <= len(TITLE) <= 80, len(TITLE)
build("Energy &middot; LNG", TITLE,
      "The IEA expects global LNG supply to fall 3% in 2026 after the Hormuz disruption cut Qatar and UAE loadings, and QatarEnergy signed for up to 7 Mtpa of US LNG in October.",
      body, sources_text, REL, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
