"""India's LNG imports after the 2026 closure of the Strait of Hormuz: volumes, sources, price, terminal use, demand.
Build from the repo root:  python3 out/research/india-lng-hormuz-2026/build.py
(writes out/post-india-lng-imports-2026-hormuz-shock.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 16 November 2026.
PPAC's LNG import workbook (ppac.gov.in/natural-gas/import) could not be opened from this environment; PPAC figures
are from its PDF reports. Source-country shares are Kpler ship-tracking data as printed by Indian newspapers."""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-lng-imports-2026-hormuz-shock.html"

# ---------------------------------------------------------------------------------------------------------------
# 1. IEA, Global Gas Security Review 2026 (PDF dated 2 Nov 2026, web page "published 3 November 2026"), India text
#    https://www.iea.org/files/42bb838f-d20d-4815-8554-32146033967d/GlobalGasSecurityReview2026.pdf
#    "LNG imports ... rising by over 10% (or 2.6 bcm) y-o-y over January-September. Imports from North America more
#    than doubled to 6.1 bcm, while African volumes also doubled to 9.4 bcm, together offsetting a sharp 35% decline
#    in Middle Eastern supplies ... Qatar's volumes declined by 72% y-o-y, while Oman became the main remaining Middle
#    Eastern source, with imports rising to 5.3 bcm." Demand Jan-Sep -3%; CGD +16%, industry -4%, power -9%;
#    full-year 2026 demand "around 2%" lower; domestic output down for a 27th consecutive month.
#    Jan-Oct: India's imports "grew by 10% (or nearly 3 bcm)".
IEA_IMPORT_UP, IEA_IMPORT_BCM, IEA_QATAR_DROP, IEA_ME_DROP = 10, 2.6, 72, 35
IEA_NAM_BCM, IEA_AFR_BCM, IEA_OMAN_BCM = 6.1, 9.4, 5.3
IEA_DEMAND, IEA_CGD, IEA_IND, IEA_POWER, IEA_FY_DEMAND, IEA_PROD_MONTHS = -3, 16, -4, -9, -2, 27

# 2. IEEJ, LNG Review October 2026 (4 Nov 2026)  https://eneken.ieej.or.jp/data/13639.pdf
#    Global LNG imports 303 Mt in Jan-Sep 2026, -1.8%; "Egypt, India and Southeast Asia notably increased imports";
#    Qatar's exports 22 Mt against 60 Mt a year earlier.
IEEJ_WORLD_MT, IEEJ_WORLD_PCT, IEEJ_QATAR_2026, IEEJ_QATAR_2025 = 303, -1.8, 22, 60

# 3. Kpler ship tracking, as printed (secondary). Monthly totals, million tonnes.
#    Reuters, 9 Jun 2026: "India's LNG imports dropping to a three-year low of 1.67 million tons in March"
#      https://www.reuters.com/commentary/reuters-open-interest/lng-demand-asia-recovers-iran-shock-china-buys-2026-06-09
#    Indian Express, 7 Jun 2026: May 2.2 Mt, 13.5% over April, 32% over March, 6% y/y, 6.4% above the 2025 monthly average
#      https://indianexpress.com/article/business/us-tops-indias-lng-basket-in-may-imports-recover-to-pre-war-levels-10727698
#    Indian Express, 4 Aug 2026: May-July 7.08 Mt (+15.4% y/y); March-April "declined by almost 13%"
#      https://indianexpress.com/article/business/india-lng-imports-rise-hormuz-crisis-us-iran-war-10816660/
#    Indian Express, 14 Oct 2026: September 2.24 Mt, -12.7% m/m, +7% y/y; May-September 11.87 Mt (+17.8%)
#      http://indianexpress.com/article/business/oman-replaces-us-india-lng-imports-hormuz-hit-10920946
#    Indian Express, 28 Oct 2026: 1-25 October 2.51 Mt (+9.8% y/y); Qatar 0.44, US 0.56, UAE 0.38, Oman 0.30, Nigeria 0.28;
#      Qatar averaged 0.07 Mt a month in March-September against 0.95 Mt in 2025
#      https://indianexpress.com/article/business/qatar-doha-lng-imports-india-strait-of-hormuz-ship-transfers-recovery-10939796
#    Times of India, 31 Oct 2026: "a record 2.7 million tonnes so far in Oct", +17.4%
#      https://timesofindia.indiatimes.com/business/india-business/power-fertiliser-fuel-lng-import-surge/articleshow/135379662.cms
K_MAR, K_MAY, K_MAY_JUL, K_SEP, K_MAY_SEP, K_OCT25, K_OCT = 1.67, 2.2, 7.08, 2.24, 11.87, 2.51, 2.7
K_MARAPR_YOY, K_MAYJUL_YOY, K_SEP_YOY, K_MAYSEP_YOY, K_OCT_YOY, K_OCT25_YOY = -13, 15.4, 7, 17.8, 17.4, 9.8
K_APR = K_MAY / 1.135                      # derived: May was 13.5% above April
K_AVG25 = K_MAY / 1.064                    # derived: May was 6.4% above the 2025 monthly average
K_JUNJUL = (K_MAY_JUL - K_MAY) / 2         # derived: average of June and July
K_AUG = K_SEP / (1 - 0.127)                # derived: September was 12.7% below August
assert round(K_MAY / 1.32, 2) == K_MAR                      # the Reuters and Indian Express March figures agree
assert round(K_APR, 2) == 1.94 and round(K_AVG25, 2) == 2.07 and round(K_JUNJUL, 2) == 2.44 and round(K_AUG, 2) == 2.57
assert abs((K_MAY_SEP - K_MAY_JUL - K_SEP) - K_AUG) < 0.03   # August from the period totals (2.55) matches within rounding
MAR_VS_AVG = 100 * (K_MAR / K_AVG25 - 1)
assert round(MAR_VS_AVG) == -19
Q_AVG25, Q_MARSEP, Q_SEP, Q_OCT25 = 0.95, 0.07, 0.1, 0.44

#    Supplier shares, March-September 2026 against a year earlier: Kpler via Economic Times, 22 Oct 2026
#      https://economictimes.indiatimes.com/industry/energy/oil-gas/indias-lng-imports-surge-9-amid-supply-gap-from-qatar-and-uae-with-us-oman-and-nigeria-leading-the-charge/articleshow/135125222.cms
#      total imports +9% y/y; US, Oman and Nigeria "about 68%" from 25%; spot "more than a third"; JKM about $20 against $12
SHARES = [("United States", 26, 11.5), ("Oman", 22, 6), ("Nigeria", 19, 7), ("Angola", 9.5, 7.5),
          ("United Arab Emirates", 8, 14), ("Qatar", 3, 45)]
K_MARSEP_YOY, THREE_NOW, THREE_BEFORE = 9, 68, 25
assert sum(s[1] for s in SHARES[:3]) == 67 and sum(s[2] for s in SHARES[:3]) == 24.5      # rounded shares add to 67 and 24.5; ET prints "about 68%" and 25%
#    Kpler via ET EnergyWorld, 10 Nov 2026: portfolio deliveries up about 3.6 Mt (about 161%), spot purchases up 35%, March-September
#      https://energy.economictimes.indiatimes.com/news/oil-and-gas/indias-lng-buyers-eye-flexi-deals-to-cut-risks-after-iran-war-hit-qatar-supply/135697041
PORTFOLIO_UP, SPOT_UP = 161, 35

# 4. PPAC, Snapshot of India's Oil & Gas data (Monthly Ready Reckoner) for September 2026, published 16 Oct 2026
#    https://ppac.gov.in/download.php?file=rep_studies%2F1792155544_Snapshot_of_India_Oil_and_Gas_Sept_2026_V3.pdf
#    April-September: LNG imports 18,189 MMSCM (17,414 a year earlier), $8.5 bn ($6.9 bn); net production 16,580 (17,359);
#    consumption 34,769 (34,773); import dependency 52.3% (50.1%). "LNG data source is DGCIS except for Aug'26 & Sep'26
#    for which data is as per prorated DGCIS (Last 12 months Average Data)". September, prorated: 2,957 (3,233), -8.55%.
P_LNG26, P_LNG25, P_USD26, P_USD25 = 18_189, 17_414, 8.5, 6.9
P_PROD26, P_PROD25, P_CONS26, P_CONS25, P_DEP26, P_DEP25 = 16_580, 17_359, 34_769, 34_773, 52.3, 50.1
P_SEP26, P_SEP25 = 2_957, 3_233
LNG_UP = 100 * (P_LNG26 / P_LNG25 - 1)
BILL_UP = 100 * (P_USD26 / P_USD25 - 1)
assert 4.4 < LNG_UP < 4.5 and round(BILL_UP) == 23
# PPAC's growth figure as printed (Moneycontrol via Free Press Journal, 26 Oct 2026:
#   https://www.freepressjournal.in/business/indias-natural-gas-import-bill-jumps-23-to-85-billion-in-h1) is 4.4%; the rounded volumes
#   compute to 4.45%. The post prints the reported 4.4% so it agrees with the global LNG post, which uses the same source figure.
LNG_UP_REPORTED = 4.4
assert P_LNG26 - P_LNG25 == 775 and P_PROD25 - P_PROD26 == 779 and abs(P_LNG26 + P_PROD26 - P_CONS26) <= 1
assert round(100 * (P_SEP26 / P_SEP25 - 1), 1) == -8.5
#    PPAC Ready Reckoner FY 2025-26, Table 3.10 (14 Aug 2026): 2025-26 (P) 34,427 MMSCM = 1,36,61,38,186 MMBtu, $13,356 mn, 9.8 $/MMBtu;
#    2024-25: 10.6; 2022-23: 16.4.   https://ppac.gov.in/download.php?file=rep_studies%2F1784899305_The_PPAC_Ready_Reckoner_FY_2025%E2%80%9326_Final.pdf
RR_MMSCM, RR_MMBTU, RR_USD_MN, RR_PRICE, RR_PRICE_2223 = 34_427, 1_366_138_186, 13_356, 9.8, 16.4
MMBTU_PER_MMSCM = RR_MMBTU / RR_MMSCM
assert round(RR_USD_MN * 1e6 / RR_MMBTU, 1) == RR_PRICE          # PPAC's own unit value reproduces
AVG26 = P_USD26 * 1e9 / (P_LNG26 * MMBTU_PER_MMSCM)               # implied average import value, $/MMBtu
AVG25 = P_USD25 * 1e9 / (P_LNG25 * MMBTU_PER_MMSCM)
assert round(AVG26, 1) == 11.8 and round(AVG25, 1) == 10.0
AVG_UP = 100 * (AVG26 / AVG25 - 1)
assert round(AVG_UP) == 18
#    Prices as reported: Economic Times, 22 Oct 2026 (JKM about $20 in March-September against $12; "currently around $30";
#    oil-linked LNG "around $14" at $110 Brent). GAIL Q2 FY27 earnings call, 30 Oct 2026: spot "$30 to $32"; Henry Hub-linked
#    LNG "around $9", "around $10" delivered; 18 spot cargoes in Q2 against 8 in Q1.
#      https://gailebank.gail.co.in/InvestorsZone/GAIL-Earnings-Call-Q2-FY27.pdf
#    ET EnergyWorld, 15 Sep 2026: "about 35-40 per cent of its imports from the spot market"; Times of India, 30 Sep 2026: September 2.1 Mt
#      https://energy.economictimes.indiatimes.com/news/oil-and-gas/natural-gas-imports-rise-despite-price-surge/134250092
#      https://timesofindia.indiatimes.com/business/india-business/energy-imports-from-west-asia-at-highest-level-since-onset-of-conflict/articleshow/134598948.cms
JKM26, JKM25, OIL_LINKED, SPOT_LO, SPOT_HI, HH_LO, HH_HI, GAIL_SPOT_Q2, GAIL_SPOT_Q1 = 20, 12, 14, 30, 32, 9, 10, 18, 8
JKM_UP = 100 * (JKM26 / JKM25 - 1)
assert round(JKM_UP) == 67
#    ICIS webinar deck, 5-6 Nov 2026 (secondary, one deck): South Asia Q4 2026 LNG imports 8.2 Mt, -18% y/y; India's spot demand
#    "likely to strengthen below $12/MMBtu"; spot "$12/MMBtu above oil-indexed term price"
#      https://cjp-rbi-icis.s3.eu-west-1.amazonaws.com/wp-content/uploads/sites/7/2026/11/10124733/ICIS-Webinar-LNG-supply-and-Asian-demand-this-winter-%E2%80%93-where-does-Europe-stand-%E2%80%93-56-Nov-2026.pdf
ICIS_SA_Q4, ICIS_SA_PCT, ICIS_INDIA_TRIGGER = 8.2, -18, 12

# 5. Petronet LNG, press release, Q2 2026-27 results, 2 Nov 2026
#    https://www.petronetlng.in/w/press-release-q2-2026-27-financial-results-1
#    Dahej 216 TBtu (211 a year earlier, 192 in April-June); utilisation 73% on 22.5 MMTPA (92% on 17.5 MMTPA; 66% in April-June);
#    company 231 TBtu (228), 64% (78%).
D_Q2, D_Q2_PY, D_Q1, D_UTIL, D_UTIL_PY, D_UTIL_Q1, D_CAP, D_CAP_OLD = 216, 211, 192, 73, 92, 66, 22.5, 17.5
#    Split of Dahej volume, brokerage summaries of the results (secondary): Prabhudas Lilladher, 3 Nov 2026 (long-term 21 TBtu
#    against 95; third-party 188 against 116; Kochi 23.7% against 26.9%); Emkay, 3 Nov 2026 (service 188, long-term 21, spot 7)
#      https://www.plindia.com/ResReport/PLNG-3-11-26-PL.pdf
#      https://images.moneycontrol.com/static-mcnews/2026/11/20261104094416_Petronet-LNG-0411026-emkay.pdf
D_LT, D_LT_PY, D_TP, D_TP_PY, D_SPOT, KOCHI, KOCHI_PY = 21, 95, 188, 116, 7, 23.7, 26.9
assert D_LT + D_TP + D_SPOT == D_Q2 and D_LT_PY + D_TP_PY == D_Q2_PY
#    Business Standard, 2 Nov 2026, and Reuters, 2 Nov 2026 (Petronet chief executive): about 6 of 75-80 Qatari cargoes due in
#    March-October arrived; QatarEnergy's force majeure extended to the end of 2026; contract 7.5 Mt a year.
#      https://www.business-standard.com/companies/news/petronet-lng-seeks-early-delivery-of-qatar-cargoes-amid-hormuz-disruptions-126110201588_1.html
#      https://www.reuters.com/business/india-petronet-talks-with-qatar-delivery-delayed-lng-cargoes-2026-11-02
CARGO_ARRIVED, CARGO_LO, CARGO_HI = 6, 75, 80
#    Petronet Q2 FY27 earnings call, 3 Nov 2026: India imported 20.15 Mt in January-September 2026; 25.3 Mt in calendar 2025
#      https://files.tijorifinance.com/insight/india/4487/Conference%20Call/CC-Nov26.pdf
PLL_9M, PLL_2025 = 20.15, 25.3
assert round(PLL_2025 * 9 / 12) == 19

# 6. Government orders and Parliament
#    Natural Gas (Supply Regulation) Order, 2026, S.O. 1232(E), 9 Mar 2026: 100% for domestic PNG, CNG, LPG production and pipeline
#    fuel; fertiliser 70%; grid industry 80%; CGD industrial and commercial 80%; cuts first to petrochemicals, then power.
#      https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/mar/doc2026310819601.pdf
#    PIB, Department of Fertilizers, 10 Mar 2026:  https://pib.gov.in/PressReleasePage.aspx?PRID=2237803
#    Lok Sabha USQ 1863 (29 Jul 2026): paragraphs 2 to 6 omitted by notification of 4 Jul 2026
#      https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU1863_MSyn5e.pdf?source=lsapps
#    Lok Sabha USQ 2087 (31 Jul 2026): gas used by fertiliser plants, MMSCM (domestic, RLNG, total)
#      https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU2087_dC1nuS.pdf?source=lsapps
FERT = [("January 2026", 234, 1532, 1766), ("February 2026", 217, 1380, 1598), ("March 2026", 211, 1028, 1239),
        ("April 2026", 205, 1195, 1400), ("May 2026", 223, 1367, 1590)]
assert all(abs(d + r - t) <= 1 for _, d, r, t in FERT)
FERT_RLNG_DROP = 100 * (FERT[2][2] / FERT[0][2] - 1)
assert round(FERT_RLNG_DROP) == -33
#    APERC Gas Report 2026 (Nov 2026, secondary for the 95% figure): fertiliser plants "around 95%", other industry "around 80%"
#    Industry report in Torrent Gas offer documents (19 Aug 2026, secondary): about 80%, then about 95% "with effect from 9 April 2026"
#      https://www.torrentgas.com/Users/images/investors/IPO%20Kit/Market%20Assessment%20&%20Industry%20Report%20on%20Natural%20Gas%20Industry.pdf
#    BusinessLine, 30 Oct 2026 (GAIL results filing): Petronet declared force majeure on 3 Mar 2026; RLNG allocation zero from 4 Mar; about 190 MMSCM supplied in H1
#      https://www.thehindubusinessline.com/companies/gail-india-to-list-cgd-arm-profit-surges-to-4724-cr-in-q2-fy27/article71645078.ece
#    PSU Watch, 2 Nov 2026: Petronet's Qatar contract from May 2028 is delivered ex-ship; ET EnergyWorld, 10 Nov 2026: US-sourced LNG under negotiation
#      https://psuwatch.com/newsupdates/petronet-seeks-early-delivery-of-qatar-lng-cargoes-amid-hormuz-disruption-md-akshay-kumar-singh
#    Indian Express, 4 Aug 2026: initial US-Iran pact on 17 June, partial recovery in transits for about three weeks; about 60% of India's LNG via Hormuz before the war
#      https://aperc.or.jp/file/2026/11/12/APERC_Gas_Report_2026_Edition.pdf

# 7. PPAC Monthly Report on natural gas production, availability and consumption: sector table, MMSCM
#    (month of 2025, same month of 2026). March: March 2026 report; April: May 2026 report; May: June 2026 report (revised May
#    figures); June: July 2026 report; July: August 2026 report; August and September: September 2026 report.
#      Mar  https://ppac.gov.in/download.php?file=menu%2F1777261935_Monthly_Gas_Report_Mar%2026_Web%20V.pdf
#      Apr  https://ppac.gov.in/download.php?file=rep_studies%2F1780479565_Monthly_Gas%20_Report_April_26_WebV.pdf
#      May  https://ppac.gov.in/download.php?file=rep_studies/1783489036_Monthly_Gas_Report_May_26.pdf
#      Jun  https://ppac.gov.in/download.php?file=rep_studies%2F1785850302_Monthly%20Gas%20Report%20Jun%2026%20-%20WebV.pdf
#      Jul  https://ppac.gov.in/download.php?file=rep_studies%2F1787820194_Monthly_Gas_Report_Jul_26-WebV.pdf
#      Aug  https://ppac.gov.in/download.php?file=rep_studies/1792052546_Monthly_Gas_Report_Aug_26-WebV.pdf
#      Sep  https://ppac.gov.in/download.php?file=rep_studies%2F1793182058_Monthly_Gas_Report_Sep_26-WebV.pdf
MONTHS = ["Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
SECT = {  # sector: ([2025 months], [2026 months])
    "Fertiliser":      ([1660, 1443, 1498, 1663, 1739, 1766, 1644], [1239, 1400, 1648, 1655, 1774, 1714, 1683]),
    "City gas":        ([1294, 1281, 1336, 1312, 1396, 1386, 1360], [1443, 1482, 1734, 1748, 1780, 1667, 1573]),
    "Power":           ([586, 824, 805, 775, 745, 647, 725],        [511, 624, 642, 641, 609, 570, 919]),
    "Refineries":      ([431, 391, 464, 388, 428, 450, 448],        [317, 296, 372, 439, 482, 339, 219]),
    "Petrochemicals":  ([305, 297, 379, 384, 309, 337, 328],        [149, 174, 175, 200, 287, 287, 282]),
    "Other users":     ([1387, 1274, 1370, 1296, 1389, 1315, 1278], [1152, 1136, 1143, 1225, 1088, 1280, 1166]),
}
TOTAL = ([5663, 5510, 5851, 5818, 6005, 5900, 5782], [4810, 5112, 5714, 5907, 6019, 5857, 5842])
for i in range(7):                                                   # every month's sectors add up to PPAC's total
    assert abs(sum(v[0][i] for v in SECT.values()) - TOTAL[0][i]) <= 2
    assert abs(sum(v[1][i] for v in SECT.values()) - TOTAL[1][i]) <= 2
MARCH = {k: 100 * (v[1][0] / v[0][0] - 1) for k, v in SECT.items()}
MARCH_TOTAL = 100 * (TOTAL[1][0] / TOTAL[0][0] - 1)
# PPAC's printed March changes: fertiliser -25.4%, power -12.8%, CGD +11.5%, refinery -26.5%, petrochem -51.2%, others -16.9%, total -15.1%
assert [round(MARCH[k], 1) for k in SECT] == [-25.4, 11.5, -12.8, -26.5, -51.1, -16.9]      # petrochemicals: PPAC prints -51.2
assert round(MARCH_TOTAL, 1) == -15.1
SUM = {k: (sum(v[0]), sum(v[1])) for k, v in SECT.items()}
SUM_TOTAL = (sum(TOTAL[0]), sum(TOTAL[1]))
assert SUM["City gas"] == (9365, 11427) and SUM["Petrochemicals"] == (2339, 1554) and SUM_TOTAL == (40529, 39261)
CGD_GAIN = SUM["City gas"][1] - SUM["City gas"][0]
FERT_LOSS = SUM["Fertiliser"][0] - SUM["Fertiliser"][1]
OTHERS_LOSS = sum(SUM[k][0] - SUM[k][1] for k in ("Power", "Refineries", "Petrochemicals", "Other users"))
assert CGD_GAIN == 2062 and FERT_LOSS == 300 and OTHERS_LOSS == 3031
pct = lambda k: 100 * (SUM[k][1] / SUM[k][0] - 1)
assert [round(pct(k)) for k in SECT] == [-3, 22, -12, -18, -34, -12]
TOTAL_PCT = 100 * (SUM_TOTAL[1] / SUM_TOTAL[0] - 1)
assert round(TOTAL_PCT, 1) == -3.1
SEP_POWER = 100 * (SECT["Power"][1][6] / SECT["Power"][0][6] - 1)
assert round(SEP_POWER, 1) == 26.8                                    # PPAC prints 26.8%; the IEA text says 27%

# ---------------------------------------------------------------------------------------------------------------
top = top_line([
    (f"{IEA_QATAR_DROP}%", f" fall in Qatar&rsquo;s LNG deliveries to India in January&ndash;September 2026, according to the IEA. "
     f"Total imports still rose by over {IEA_IMPORT_UP}%, or {IEA_IMPORT_BCM} bcm, as supply from North America and Africa doubled."),
    (f"${P_USD26} billion", f" was the LNG import bill for April&ndash;September 2026, {BILL_UP:.0f}% higher for about {LNG_UP_REPORTED}% more gas "
     f"(PPAC, provisional). That is about ${AVG26:.1f}/MMBtu, against an Asian spot benchmark averaging about ${JKM26} in March&ndash;September."),
    (f"{-MARCH['Petrochemicals']:.0f}%", f" less gas reached petrochemical plants in March 2026 than a year earlier, and "
     f"{-MARCH['Fertiliser']:.0f}% less reached fertiliser plants. City gas use rose {MARCH['City gas']:.1f}% under the government&rsquo;s priority order."),
])

intro = f'''<p>Before the war that began on 28 February 2026, about 60% of India&rsquo;s LNG came through the Strait of Hormuz, mainly from Qatar, on Kpler data printed by the Indian Express.
This piece sets out what happened next, using PPAC reports, the IEA&rsquo;s November review, company results and ship-tracking data printed in the press.</p>
'''

# ---- 1. monthly volumes ----
L_MAR = "March <small>first month of the closure</small>"
s1 = insight(
    "Monthly imports: 1.67 million tonnes in March 2026, above the 2025 average from May",
    bars("India&rsquo;s LNG imports fell to 1.67 Mt in March 2026, then exceeded the 2025 monthly average",
         [(L_MAR, K_MAR),
          ("April <small>derived</small>", round(K_APR, 2)),
          ("May", K_MAY),
          ("June and July <small>average of the two, derived</small>", round(K_JUNJUL, 2)),
          ("August <small>derived</small>", round(K_AUG, 2)),
          ("September", K_SEP),
          ("October <small>part month, reported 31 October</small>", K_OCT)],
         accent=L_MAR, unit=" Mt", ref=(round(K_AVG25, 2), f"{K_AVG25:.2f} Mt, the 2025 monthly average (derived)"),
         sub="LNG delivered to India each month, million tonnes (Mt), from Kpler ship tracking as printed in the press.",
         source="Kpler data via Reuters (9 June 2026), Indian Express (7 June, 4 August, 14 and 28 October 2026) and Times of India (31 October 2026). "
                "Secondary sources. Derived months are computed from the percentage changes those reports give.")
    + numbers(["Period, 2026", "Kpler, as printed", "Change on a year earlier"],
              [["March", f"{K_MAR} Mt", "three-year low (Reuters)"],
               ["March&ndash;April", "not given", f"almost {-K_MARAPR_YOY}% lower"],
               ["May", f"{K_MAY} Mt", "+6%"],
               ["May&ndash;July", f"{K_MAY_JUL} Mt", f"+{K_MAYJUL_YOY}%"],
               ["September", f"{K_SEP} Mt", f"+{K_SEP_YOY}%"],
               ["May&ndash;September", f"{K_MAY_SEP} Mt", f"+{K_MAYSEP_YOY}%"],
               ["March&ndash;September", "not given", f"+{K_MARSEP_YOY}%"],
               ["1&ndash;25 October", f"{K_OCT25} Mt", f"+{K_OCT25_YOY}%"],
               ["October, part month", f"{K_OCT} Mt", f"+{K_OCT_YOY}%"],
               ["April&ndash;September, PPAC (provisional)", f"{P_LNG26:,} MMSCM", f"+{LNG_UP_REPORTED}% ({P_LNG25:,})"],
               ["January&ndash;September, IEA", f"+{IEA_IMPORT_BCM} bcm", f"over +{IEA_IMPORT_UP}%"],
               ["January&ndash;September, Petronet", f"{PLL_9M} Mt", f"{PLL_2025} Mt in all of 2025"]]),
    f"The shortfall lasted two months, and from April to September the extra LNG ({P_LNG26 - P_LNG25} MMSCM on PPAC&rsquo;s provisional count) "
    f"almost exactly matched a {P_PROD25 - P_PROD26} MMSCM fall in domestic gas output, while total gas use stayed flat.",
    f"Gas buyers and planners should treat March as the stress case, about {-MAR_VS_AVG:.0f}% below the 2025 monthly average, "
    "and size storage or swap arrangements to cover two months of it.",
    "volumes")

# ---- 2. sources ----
s2 = insight(
    "Supply sources: Qatar&rsquo;s share fell from 45% to 3% in March&ndash;September 2026",
    bars("Qatar supplied 3% of India&rsquo;s LNG in March&ndash;September 2026, down from 45% a year earlier",
         [(n, now, f"{before}% a year earlier") for n, now, before in SHARES],
         accent="Qatar", unit="%",
         sub="Share of India&rsquo;s LNG imports by supplier, March&ndash;September 2026, per cent.",
         source="Kpler ship-tracking data as printed by the Economic Times, 22 October 2026 (secondary). No official country-wise series was available.")
    + numbers(["Measure", "Figure", "Source"],
              [["Qatar, January&ndash;September 2026", f"&minus;{IEA_QATAR_DROP}% on a year earlier", "IEA"],
               ["Middle East, January&ndash;September 2026", f"&minus;{IEA_ME_DROP}%", "IEA"],
               ["North America", f"more than doubled to {IEA_NAM_BCM} bcm", "IEA"],
               ["Africa", f"doubled to {IEA_AFR_BCM} bcm", "IEA"],
               ["Oman", f"rose to {IEA_OMAN_BCM} bcm", "IEA"],
               ["Qatar, monthly average in 2025", f"{Q_AVG25} Mt", "Kpler via Indian Express"],
               ["Qatar, monthly average, March&ndash;September 2026", f"{Q_MARSEP} Mt", "Kpler via Indian Express"],
               ["Qatar, 1&ndash;25 October 2026", f"{Q_OCT25} Mt", "Kpler via Indian Express"],
               ["Qatari cargoes received by Petronet, March&ndash;October", f"about {CARGO_ARRIVED} of {CARGO_LO}&ndash;{CARGO_HI} due", "Petronet chief executive, 2 November"],
               ["US, Oman and Nigeria together", f"about {THREE_NOW}%, from {THREE_BEFORE}%", "Kpler via Economic Times"]],
              "Show the IEA and Qatar figures"),
    f"India replaced a supplier that depends on the strait with three that do not, and Kpler estimates that portfolio deliveries rose about "
    f"{PORTFOLIO_UP}% and spot purchases {SPOT_UP}% to do it.",
    "Petronet LNG, GAIL and other importers should write origin flexibility and delivery-at-port terms into renewed contracts, "
    "as Petronet has done on delivery terms and is negotiating on origin for its Qatar contract from 2028.",
    "sources")

# ---- 3. price ----
L_AVG26 = "Average import value, April&ndash;September 2026 <small>PPAC, computed</small>"
s3 = insight(
    "Price: about $11.8/MMBtu on average, with spot cargoes at $20 to $32",
    bars("India&rsquo;s average LNG import value was about $11.8/MMBtu; spot cargoes cost $20 to $32",
         [("Henry Hub-linked LNG <small>GAIL, October 2026</small>", (HH_LO, HH_HI)),
          ("Average import value, April&ndash;September 2025 <small>PPAC, computed</small>", round(AVG25, 1), "", f"${AVG25:.1f}/MMBtu"),
          (L_AVG26, round(AVG26, 1)),
          ("Oil-indexed LNG at $110 Brent <small>press estimate</small>", OIL_LINKED),
          ("Asian spot benchmark, March&ndash;September 2026 average", JKM26),
          ("Spot cargoes, late October 2026 <small>GAIL</small>", (SPOT_LO, SPOT_HI))],
         accent=L_AVG26, unit="$/MMBtu",
         sub="US dollars per million British thermal units (MMBtu). Averages are import value divided by import volume.",
         source="PPAC Snapshot for September 2026 and Ready Reckoner 2025-26 (this blog&rsquo;s division); GAIL earnings call, 30 October 2026; "
                "Economic Times, 22 October 2026 (secondary: benchmark average and oil-indexed estimate).")
    + numbers(["April&ndash;September", "2025", "2026", "Change"],
              [["LNG imports, MMSCM", f"{P_LNG25:,}", f"{P_LNG26:,}", f"+{LNG_UP_REPORTED}%"],
               ["Import bill, $ billion", f"{P_USD25}", f"{P_USD26}", f"+{BILL_UP:.0f}%"],
               ["Implied value, $/MMBtu", f"{AVG25:.1f}", f"{AVG26:.1f}", f"+{AVG_UP:.0f}%"],
               ["Asian spot benchmark, March&ndash;September, $/MMBtu", f"{JKM25}", f"{JKM26}", f"+{JKM_UP:.0f}%"],
               ["Import dependency, %", f"{P_DEP25}", f"{P_DEP26}", ""]]),
    f"Most LNG still arrived on contracts linked to oil or to the US gas price, so the average import value rose about {AVG_UP:.0f}% "
    f"while the Asian spot benchmark rose about {JKM_UP:.0f}%, and the spot price applied to the third or more of supply bought at short notice.",
    "Importers should hold enough oil-indexed and Henry Hub-linked contracts to cover priority demand, and PPAC should publish the term and spot split each month.",
    "price")

# ---- terminal use (no chart: three figures) ----
terminals = f'''<h2 class="gb-h2" id="terminals">Terminal use: Dahej handled {D_Q2} TBtu in July&ndash;September 2026, at {D_UTIL}% of capacity</h2>
<p>Petronet&rsquo;s Dahej terminal processed {D_Q2} trillion Btu in July&ndash;September 2026, against {D_Q2_PY} a year earlier. Utilisation reads {D_UTIL}% against {D_UTIL_PY}%
because capacity grew from {D_CAP_OLD} to {D_CAP} million tonnes a year in March 2026.</p>
<p>The cargo mix changed. Brokerage summaries of the results put long-term volume at {D_LT} TBtu, down from {D_LT_PY}, and third-party cargoes at {D_TP} TBtu, up from {D_TP_PY}.
About {CARGO_ARRIVED} of the {CARGO_LO}&ndash;{CARGO_HI} Qatari cargoes due in March&ndash;October arrived.</p>
<p>Kochi ran at {KOCHI}%, against {KOCHI_PY}% a year earlier. PPAC&rsquo;s terminal-by-terminal table for April&ndash;September 2026 could not be read for this piece,
so the other six terminals are not covered here.</p>
'''

# ---- 4. demand ----
order = ["Petrochemicals", "Refineries", "Fertiliser", "Other users", "Power", "City gas"]
LBL = {"Petrochemicals": "Petrochemicals", "Refineries": "Refineries", "Fertiliser": "Fertiliser plants",
       "Other users": "Other users <small>industry, pipeline fuel and more</small>", "Power": "Power stations",
       "City gas": "City gas <small>CNG and piped gas</small>"}
s4 = insight(
    "Demand: petrochemicals, refineries and power gave up gas, and city gas use rose",
    bars("March 2026: petrochemicals used 51% less gas, fertiliser 25% less, city gas 11.5% more",
         [(LBL[k], round(MARCH[k], 1)) for k in order],
         accent=LBL["Petrochemicals"], fmt=lambda v: f"{v:+.1f}%".replace("-", "&minus;"),
         sub="Natural gas consumption by sector, March 2026 against March 2025, per cent change. All sectors together: "
             f"&minus;{-MARCH_TOTAL:.1f}%.",
         source="PPAC, Monthly Report on natural gas production, availability and consumption, March 2026 (provisional). Changes recomputed from PPAC&rsquo;s volumes.")
    + numbers(["March&ndash;September, MMSCM", "2025", "2026", "Change"],
              [[k, f"{SUM[k][0]:,}", f"{SUM[k][1]:,}", f"{pct(k):+.0f}%".replace("-", "&minus;")] for k in order]
              + [["All sectors", f"{SUM_TOTAL[0]:,}", f"{SUM_TOTAL[1]:,}", f"&minus;{-TOTAL_PCT:.1f}%"]],
              "Show March&ndash;September by sector")
    + numbers(["Gas used by fertiliser plants, MMSCM", "Domestic", "Imported (RLNG)", "Total"],
              [[m, f"{d:,}", f"{r:,}", f"{t:,}"] for m, d, r, t in FERT],
              "Show fertiliser plants&rsquo; gas by month"),
    f"The March order kept household and vehicle gas whole and fertiliser at 70% of past use, so over March&ndash;September power, refineries, "
    f"petrochemicals and other users took {OTHERS_LOSS:,} MMSCM less gas than a year earlier while city gas took {CGD_GAIN:,} more.",
    "The petroleum ministry should keep the priority schedule as a standing plan with published triggers, so that plants able to switch fuel know they are first in line for cuts.",
    "demand")

outlook = f'''<h2 class="gb-h2" id="outlook">Outlook: the IEA expects India&rsquo;s gas demand to end 2026 about {-IEA_FY_DEMAND}% lower</h2>
<p>The IEA puts India&rsquo;s gas demand {-IEA_DEMAND}% lower in January&ndash;September and expects about {-IEA_FY_DEMAND}% lower for the year. Domestic output fell for a {IEA_PROD_MONTHS}th month in a row,
which is why imports rose while demand did not.</p>
<p>An ICIS webinar deck of early November 2026, a single secondary source, expects South Asian LNG imports of {ICIS_SA_Q4} Mt in October&ndash;December, {-ICIS_SA_PCT}% lower than a year earlier,
and India&rsquo;s spot buying to strengthen below ${ICIS_INDIA_TRIGGER}/MMBtu. Kpler&rsquo;s October count for India points the other way so far.</p>
'''

timeline = '<details class="xv-n"><summary>Timeline: March to November 2026</summary>\n' + flow([
    ("28 February", "War begins in West Asia; tanker movement through the Strait of Hormuz largely stops."),
    ("3&ndash;4 March", "Petronet declares force majeure to its buyers; GAIL&rsquo;s allocation of Qatari gas falls to zero from 4 March.", True),
    ("9 March", "The Natural Gas (Supply Regulation) Order sets priorities: household and vehicle gas 100%, fertiliser 70%, industry 80%."),
    ("9 April", "Fertiliser plants&rsquo; allocation reaches about 95% of past use (industry report in a Torrent Gas filing and APERC; secondary)."),
    ("17 June", "An initial US&ndash;Iran pact allows a partial recovery in transits for about three weeks."),
    ("4 July", "The government withdraws the allocation paragraphs of the order."),
    ("October", f"Qatari deliveries reach {Q_OCT25} Mt by 25 October, an eight-month high."),
    ("2 November", "Petronet says QatarEnergy has extended force majeure to the end of 2026."),
]) + '</details>\n'

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>PPAC</b> should publish LNG imports each month by source country and by contract type (term, portfolio, spot), and mark prorated months in every table.</li>
<li><b>The Ministry of Petroleum and Natural Gas</b> should keep the March 2026 priority schedule as a standing contingency plan, with published triggers for switching it on and off.</li>
<li><b>Petronet LNG, GAIL and other importers</b> should write origin flexibility and delivery-at-port terms into contract renewals, so a closed route does not stop supply.</li>
<li><b>PNGRB</b> should require every LNG terminal to publish monthly throughput split into long-term, third-party and spot cargoes.</li>
<li><b>The Department of Fertilizers</b> should publish each month the gas cost passed into the urea subsidy, so that the fiscal cost of spot LNG is visible.</li>
</ol>
<p><em>These are proposals from this blog, not recommendations any agency has adopted.</em></p>
'''

method = f'''<details class="xv-n"><summary>Method and units</summary>
<ul>
<li><b>Average import value.</b> PPAC&rsquo;s import bill divided by its import volume, using PPAC&rsquo;s own 2025-26 conversion of {RR_MMSCM:,} MMSCM to {RR_MMBTU:,} MMBtu.
The same division gives PPAC&rsquo;s printed ${RR_PRICE}/MMBtu for 2025-26. The bill is printed to one decimal of a billion dollars, so the result is approximate.</li>
<li><b>Derived months.</b> April, August, the June&ndash;July average and the 2025 monthly average are computed from percentage changes in the Indian Express reports of Kpler data, and are marked &ldquo;derived&rdquo;.</li>
<li><b>Sector figures.</b> PPAC monthly reports, provisional. May 2026 uses the revised figures in the June report. March&ndash;September sums and changes are this blog&rsquo;s arithmetic.</li>
<li><b>Units.</b> Mt is million tonnes of LNG; PPAC converts 1 Mt to 1,325 MMSCM (million standard cubic metres). bcm is billion cubic metres. TBtu is trillion British thermal units.</li>
<li><b>Global frame.</b> IEEJ counts world LNG imports at {IEEJ_WORLD_MT} Mt in January&ndash;September 2026, {-IEEJ_WORLD_PCT}% lower, with Qatar&rsquo;s exports at {IEEJ_QATAR_2026} Mt against {IEEJ_QATAR_2025} Mt.</li>
</ul></details>
'''

gaps = f'''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li><b>PPAC&rsquo;s month-by-month LNG import table.</b> The workbook on PPAC&rsquo;s LNG import page could not be opened. Monthly volumes here are Kpler figures printed in the press.</li>
<li><b>An official country-wise series.</b> None was found. Supplier shares rest on Kpler data printed by the Economic Times and the Indian Express.</li>
<li><b>The term and spot split.</b> &ldquo;More than a third&rdquo; spot is attributed by the Economic Times to industry executives; an earlier report said 35&ndash;40%. No official split exists.</li>
<li><b>Final April&ndash;September figures.</b> PPAC&rsquo;s August and September 2026 imports are prorated from the last 12 months, not counted, so the ${P_USD26} billion bill and the ${AVG26:.1f} average are provisional and will change when customs data arrive.</li>
<li><b>Terminals other than Dahej and Kochi.</b> PPAC&rsquo;s utilisation table for April&ndash;September 2026 could not be read.</li>
<li><b>The subsidy cost.</b> No government estimate of the extra urea subsidy caused by costlier LNG was found.</li>
</ul>
<p><b>Where sources disagree.</b> PPAC&rsquo;s prorated September import figure is {P_SEP26:,} MMSCM, 8.5% lower than a year earlier; Kpler&rsquo;s ship count shows September {K_SEP_YOY}% higher.
For September, Kpler via the Indian Express gives {K_SEP} Mt and the Times of India 2.1 Mt. For April&ndash;September PPAC shows +{LNG_UP_REPORTED}%; Kpler shows +{K_MARSEP_YOY}% for March&ndash;September and the IEA over +{IEA_IMPORT_UP}% for January&ndash;September.</p>
<p>City gas growth also differs by period and source: +{pct("City gas"):.0f}% in PPAC&rsquo;s March&ndash;September sector tables, +{IEA_CGD}% in the IEA&rsquo;s January&ndash;September text.
Qatar&rsquo;s 2025 monthly average is printed as {Q_AVG25} Mt and as 1 Mt in different Indian Express reports.</p>
</details>
'''

body = STYLE + top + intro + s1 + s2 + s3 + terminals + s4 + outlook + timeline + fixes + method + gaps

A = lambda url, text: f'<a href="{html.escape(url, quote=True)}">{text}</a>'
SOURCES = "; ".join([
    A("https://www.iea.org/files/42bb838f-d20d-4815-8554-32146033967d/GlobalGasSecurityReview2026.pdf", "IEA, Global Gas Security Review 2026, published 3 November 2026"),
    A("https://eneken.ieej.or.jp/data/13639.pdf", "IEEJ, LNG Review October 2026, 4 November 2026"),
    A("https://ppac.gov.in/download.php?file=rep_studies%2F1792155544_Snapshot_of_India_Oil_and_Gas_Sept_2026_V3.pdf", "PPAC, Snapshot of India&rsquo;s Oil &amp; Gas data for September 2026, 16 October 2026"),
    A("https://ppac.gov.in/download.php?file=rep_studies%2F1784899305_The_PPAC_Ready_Reckoner_FY_2025%E2%80%9326_Final.pdf", "PPAC Ready Reckoner 2025-26, Table 3.10"),
    "PPAC monthly gas reports for "
    + ", ".join([
        A("https://ppac.gov.in/download.php?file=menu%2F1777261935_Monthly_Gas_Report_Mar%2026_Web%20V.pdf", "March"),
        A("https://ppac.gov.in/download.php?file=rep_studies%2F1780479565_Monthly_Gas%20_Report_April_26_WebV.pdf", "April"),
        A("https://ppac.gov.in/download.php?file=rep_studies/1783489036_Monthly_Gas_Report_May_26.pdf", "May"),
        A("https://ppac.gov.in/download.php?file=rep_studies%2F1785850302_Monthly%20Gas%20Report%20Jun%2026%20-%20WebV.pdf", "June"),
        A("https://ppac.gov.in/download.php?file=rep_studies%2F1787820194_Monthly_Gas_Report_Jul_26-WebV.pdf", "July"),
        A("https://ppac.gov.in/download.php?file=rep_studies/1792052546_Monthly_Gas_Report_Aug_26-WebV.pdf", "August"),
        A("https://ppac.gov.in/download.php?file=rep_studies%2F1793182058_Monthly_Gas_Report_Sep_26-WebV.pdf", "September 2026"),
    ]),
    A("https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/mar/doc2026310819601.pdf", "Natural Gas (Supply Regulation) Order, 2026, S.O. 1232(E), 9 March 2026"),
    A("https://pib.gov.in/PressReleasePage.aspx?PRID=2237803", "PIB, Department of Fertilizers, 10 March 2026"),
    A("https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU2087_dC1nuS.pdf?source=lsapps", "Lok Sabha unstarred question 2087, 31 July 2026"),
    A("https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU1863_MSyn5e.pdf?source=lsapps", "Lok Sabha unstarred question 1863, July 2026"),
    A("https://www.petronetlng.in/w/press-release-q2-2026-27-financial-results-1", "Petronet LNG, results press release, 2 November 2026"),
    A("https://files.tijorifinance.com/insight/india/4487/Conference%20Call/CC-Nov26.pdf", "Petronet LNG earnings call, 3 November 2026"),
    A("https://gailebank.gail.co.in/InvestorsZone/GAIL-Earnings-Call-Q2-FY27.pdf", "GAIL earnings call, 30 October 2026"),
    A("https://www.plindia.com/ResReport/PLNG-3-11-26-PL.pdf", "Prabhudas Lilladher on Petronet, 3 November 2026") + " and "
    + A("https://images.moneycontrol.com/static-mcnews/2026/11/20261104094416_Petronet-LNG-0411026-emkay.pdf", "Emkay, 3 November 2026") + " (secondary: Dahej cargo mix)",
    A("https://www.business-standard.com/companies/news/petronet-lng-seeks-early-delivery-of-qatar-cargoes-amid-hormuz-disruptions-126110201588_1.html", "Business Standard, 2 November 2026") + " and "
    + A("https://www.reuters.com/business/india-petronet-talks-with-qatar-delivery-delayed-lng-cargoes-2026-11-02", "Reuters, 2 November 2026") + " (Qatari cargoes)",
    "Kpler ship-tracking data, secondary, via "
    + A("https://economictimes.indiatimes.com/industry/energy/oil-gas/indias-lng-imports-surge-9-amid-supply-gap-from-qatar-and-uae-with-us-oman-and-nigeria-leading-the-charge/articleshow/135125222.cms", "Economic Times, 22 October 2026") + ", "
    + A("https://energy.economictimes.indiatimes.com/news/oil-and-gas/indias-lng-buyers-eye-flexi-deals-to-cut-risks-after-iran-war-hit-qatar-supply/135697041", "ET EnergyWorld, 10 November 2026") + ", Indian Express ("
    + A("https://indianexpress.com/article/business/us-tops-indias-lng-basket-in-may-imports-recover-to-pre-war-levels-10727698", "7 June") + ", "
    + A("https://indianexpress.com/article/business/india-lng-imports-rise-hormuz-crisis-us-iran-war-10816660/", "4 August") + ", "
    + A("http://indianexpress.com/article/business/oman-replaces-us-india-lng-imports-hormuz-hit-10920946", "14 October") + ", "
    + A("https://indianexpress.com/article/business/qatar-doha-lng-imports-india-strait-of-hormuz-ship-transfers-recovery-10939796", "28 October 2026") + "), "
    + A("https://www.reuters.com/commentary/reuters-open-interest/lng-demand-asia-recovers-iran-shock-china-buys-2026-06-09", "Reuters, 9 June 2026") + " and "
    + A("https://timesofindia.indiatimes.com/business/india-business/power-fertiliser-fuel-lng-import-surge/articleshow/135379662.cms", "Times of India, 31 October 2026"),
    A("https://timesofindia.indiatimes.com/business/india-business/energy-imports-from-west-asia-at-highest-level-since-onset-of-conflict/articleshow/134598948.cms", "Times of India, 30 September 2026") + " (September at 2.1 Mt)",
    A("https://energy.economictimes.indiatimes.com/news/oil-and-gas/natural-gas-imports-rise-despite-price-surge/134250092", "ET EnergyWorld, 15 September 2026") + " (spot share of 35&ndash;40%)",
    A("https://cjp-rbi-icis.s3.eu-west-1.amazonaws.com/wp-content/uploads/sites/7/2026/11/10124733/ICIS-Webinar-LNG-supply-and-Asian-demand-this-winter-%E2%80%93-where-does-Europe-stand-%E2%80%93-56-Nov-2026.pdf", "ICIS webinar deck, November 2026") + " (secondary, single deck)",
    A("https://aperc.or.jp/file/2026/11/12/APERC_Gas_Report_2026_Edition.pdf", "APERC Gas Report 2026") + " and "
    + A("https://www.torrentgas.com/Users/images/investors/IPO%20Kit/Market%20Assessment%20&%20Industry%20Report%20on%20Natural%20Gas%20Industry.pdf", "industry report in Torrent Gas&rsquo;s offer documents, August 2026") + " (secondary: fertiliser allocation of about 95% from 9 April)",
    A("https://www.thehindubusinessline.com/companies/gail-india-to-list-cgd-arm-profit-surges-to-4724-cr-in-q2-fy27/article71645078.ece", "BusinessLine, 30 October 2026") + " (GAIL filing: force majeure of 3 March)",
    A("https://psuwatch.com/newsupdates/petronet-seeks-early-delivery-of-qatar-lng-cargoes-amid-hormuz-disruption-md-akshay-kumar-singh", "PSU Watch, 2 November 2026") + " (delivery terms of Petronet&rsquo;s contract from 2028)",
]) + (". PPAC figures for 2026-27 are provisional, and its August and September LNG imports are prorated estimates. Ship-tracking figures are secondary and may be revised. "
      "Averages, sums, derived months and percentage changes are computed by this blog. Analysed 16 November 2026.")

# ---- related posts: live titles and URLs from the manifest; none on the removal or merge lists ----
MAN = json.loads((ROOT / "meta/manifest.json").read_text(encoding="utf-8"))["posts"]
GONE = set(json.loads((ROOT / "out/gsc_index/phase1_remove.json").read_text())) | set(json.loads((ROOT / "out/gsc_index/phase3_map.json").read_text()))
BY_SLUG = {p["slug"]: p for p in (MAN.values() if isinstance(MAN, dict) else MAN)}
REL_SLUGS = ["indias-cheapest-lng-capacity-is-extra", "city-gas-just-became-indias-largest-gas", "india-wants-15-of-its-energy-from-gas",
             "global-lng-trade-hit-record-437-million", "india-imports-60-of-its-cooking-gas"]
assert not GONE & set(REL_SLUGS)
RELATED = [(BY_SLUG[s]["url"], BY_SLUG[s]["title"]) for s in REL_SLUGS]
assert all(u.startswith("https://blog.vertistratsolution.com/") for u, _ in RELATED)

TITLE = "India's LNG imports in 2026: up over 10% to September, Qatar's supply down 72%"
assert 55 <= len(TITLE) <= 80, len(TITLE)
STANDFIRST = ("Qatar supplied 45% of India&rsquo;s LNG before the Strait of Hormuz closed and 3% in the seven months after. "
              "Imports fell for two months, then ran above 2025 levels at a higher price, while petrochemical plants, refineries and power stations gave up gas.")

# ---- house checks: paragraph length, person, old name ----
plain = lambda s: html.unescape(re.sub(r"<[^>]+>", " ", s))
for para in re.findall(r"<p[^>]*>(.*?)</p>", body + f"<p>{STANDFIRST}</p>", flags=re.S):
    n = len(plain(para).split())
    assert n <= 60, (n, plain(para)[:80])
text = plain(re.sub(r"<style.*?</style>", " ", body, flags=re.S) + " " + STANDFIRST + " " + TITLE)
assert not re.search(r"\b(you|your|we|our|us)\b", text), re.search(r"\b(you|your|we|our|us)\b", text)
assert "masala" not in (body + SOURCES).lower()

build("Energy &middot; LNG", TITLE, STANDFIRST, body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
