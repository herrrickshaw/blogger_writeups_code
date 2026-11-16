"""Sustainable aviation fuel (SAF) blending targets: India's indicative 1% / 2% / 5% for international flights against the EU, the UK and Asia,
with India's requirement in tonnes and the supply behind each target.
Build from the repo root:  python3 out/research/saf-blend-india-eu-2026/build.py   (writes out/post-india-saf-blend-targets-compared-with-eu-uk.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 16 November 2026."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line, waterfall  # noqa: E402

OUT = ROOT / "out/post-india-saf-blend-targets-compared-with-eu-uk.html"
B = "https://blog.vertistratsolution.com"

# ---- India: the targets (share of SAF in ATF for international flights, %) ----
# Rajya Sabha USQ 828, Ministry of Civil Aviation, 27 Jul 2026: "approved indicative blending targets of 1% by 2027, 2% by 2028, and 5% by 2030
#   for SAF in conventional Aviation Turbine Fuel for international operations"  https://sansad.in/getFile/annex/271/AU828_tu5NZH.pdf?source=pqars
# Rajya Sabha USQ 1737, Ministry of Petroleum and Natural Gas, 15 Dec 2025 (same targets, "initially for international flights")
#   https://sansad.in/getFile/annex/269/AU1737_T6tK0c.pdf?source=pqars
# Rajya Sabha USQ 41, MoCA, 20 Jul 2026: "Policy for Sustainable Aviation Fuels (SAF) has not been finalised yet."
#   https://sansad.in/getFile/annex/271/AU41_uTds0S.pdf?source=pqars
# PIB, MoPNG, 23 Apr 2026 (ATF Control Order amended 17 Apr 2026; targets "1% in 2027, 2% in 2028, and 5% in 2030")
#   https://www.pib.gov.in/PressReleasePage.aspx?PRID=2255021&lang=1&reg=3
IN_T = {2027: 1, 2028: 2, 2030: 5}
# Draft National Policy on SAF (not published; press reports only): 1% 2027, 2% 2028, 3% 2029, 5% 2030; 10% in 2035 and 20% in 2040 indicative
#   (BusinessLine 4 Nov 2026; NDTV Profit 3 Nov 2026; Mint 5 Nov 2026; New Indian Express 5 Nov 2026). CNBC TV18 / PTI, 7 Nov 2026, says 40% by 2040.
DRAFT_2029, DRAFT_2035, DRAFT_2040, DRAFT_2040_PTI = 3, 10, 20, 40
# New Indian Express, 5 Nov 2026, quoting the draft: ATF "nearly 14.2 million tonnes" by 2030, "7.7 million tonnes" international.
DRAFT_ATF_2030_MT, DRAFT_INTL_2030_MT = 14.2, 7.7

# ---- India: jet fuel (ATF) sales, thousand tonnes (TMT), and the international share ----
# PPAC Ready Reckoner FY 2025-26 (Aug 2026): "International aviation contributed to 39% of the total ATF volumes of 9.16 MMT during FY 2025-26";
#   Table 6.8 ATF total 9,161 TMT (FY2025-26), 8,985 TMT (FY2024-25); sector chart FY2024-25 international 26%.
#   https://ppac.gov.in/download.php?file=rep_studies%2F1784899305_The_PPAC_Ready_Reckoner_FY_2025%E2%80%9326_Final.pdf
# PPAC Industry Consumption Report, September 2026 (21 Oct 2026): Apr-Sep 2026 ATF 4,443 TMT, "51% domestic aviation & 49% international aviation"
#   https://ppac.gov.in/download.php?file=menu%2F1792999364_ICR_September%2026.pdf
ATF_FY26, SH_FY26 = 9161, 0.39
ATF_FY25, SH_FY25 = 8985, 0.26
ATF_H1FY27, SH_H1FY27 = 4443, 0.49
INTL_FY26 = ATF_FY26 * SH_FY26                      # TMT
INTL_FY25 = ATF_FY25 * SH_FY25
INTL_H1FY27_ANN = ATF_H1FY27 * SH_H1FY27 * 2        # six months doubled: a rough annual rate, not a forecast
assert round(INTL_FY26) == 3573 and round(INTL_FY25) == 2336 and round(INTL_H1FY27_ANN) == 4354
NEED = {p: INTL_FY26 * 1000 * p / 100 for p in (1, 2, 5)}          # tonnes of SAF a year at FY2025-26 sales
assert round(NEED[1], -2) == 35700 and round(NEED[2], -2) == 71500 and round(NEED[5], -2) == 178600
NEED1_FY25 = INTL_FY25 * 10
NEED1_H1 = INTL_H1FY27_ANN * 10
assert round(NEED1_FY25, -2) == 23400 and round(NEED1_H1, -2) == 43500
SHARE_ROUNDING_T = 0.005 * ATF_FY26 * 1000 * 0.01                  # the 39% is a rounded share: half a point of all ATF, at 1%
assert round(SHARE_ROUNDING_T, -2) == 500
ALL_FUEL_EQUIV = IN_T[2030] * SH_FY26                              # India's 5% of international fuel as a share of all ATF sold
assert round(ALL_FUEL_EQUIV, 2) == 1.95
# S&P Global Energy and SAF Association report, 28 Sep 2026 (as reported by S&P Global): SAF demand "about 46,000 metric tons in 2027 to roughly
#   250,000 mt by 2030"; four ISCC-CORSIA certified co-processing units, 106,500 t: BPCL Mumbai 61,000; IOCL Panipat 30,000; HPCL Visakh 10,000; MRPL 5,500.
#   https://www.spglobal.com/energy/en/news-research/latest-news/agriculture/092826-india-positioned-to-meet-2027-saf-targets-by-coprocessing-2030-goals-need-urgent-finance-report
SP_2027, SP_2030 = 46000, 250000
CERT = {"BPCL Mumbai": 61000, "Indian Oil Panipat": 30000, "HPCL Visakh": 10000, "MRPL Mangaluru": 5500}
CERT_T = sum(CERT.values())
assert CERT_T == 106500
assert NEED[2] < CERT_T < NEED[5] and SP_2027 < CERT_T < SP_2030
DRAFT_NEED_2030 = DRAFT_INTL_2030_MT * 1e6 * 0.05
assert round(DRAFT_NEED_2030) == 385000
assert round(100 * DRAFT_INTL_2030_MT / DRAFT_ATF_2030_MT) == 54   # the draft's own 2030 international share, against PPAC's 39% for FY2025-26

# ---- India: named projects, tonnes a year ----
# Indian Oil Annual Report 2024-25: ATJ plant at Panipat "86.8 TMT per annum", "by 2027-28"; co-processing "targeting 30 KTPA of neat SAF"
#   https://iocl.com/download/SingleAnnualReport202425.pdf
# Indian Oil investor presentation FY2025-26 (Aug 2026): "JV with M11 Energy Transition Pvt. Ltd for setting up 100 KTPA SAF project at Paradip Refinery"
#   https://iocl.com/uploads/IOCL_Investor_Presentation_25-26.pdf
# Topsoe, 14 Oct 2026: BPCL Mumbai revamps a 4,000 t/day kerosene hydrotreater to co-process 5% used cooking oil; commissioning "by the end of 2026"
#   https://www.topsoe.com/news/topsoe-secures-technology-contract-for-bharat-petroleums-saf-project-in-india
# ICAO ACT-SAF feasibility study for India (undated): IOCL Panipat co-processing 35 kt/year, BPCL Mumbai 15 kt/year
#   https://www.icao.int/sites/default/files/environmental-protection/Documents/ACT-SAF/Feasibility_Study_India.pdf
# MRPL: ISCC CORSIA certificate 24 Apr 2026 (results press release, 15 Jul 2026); EOI for SAF supply, "2027: 5,000 Kilolitres"
# TruAlt Bioenergy, 18 Jun 2026: Rs 150 crore PM JI-VAN approval, SAF plant of "10 crore litres per annum" (litres; left out of the tonnes total)
# Rajya Sabha Starred Q 6, MoCA, 20 Jul 2026: PM JI-VAN aid approved in June 2026 "for three commercial-scale and two demonstration-scale SAF projects"
#   https://sansad.in/getFile/annex/271/AS6_36Hhd1.pdf?source=pqars
ATJ_PANIPAT, PARADIP = 86800, 100000
NAMED_T = CERT_T + ATJ_PANIPAT + PARADIP
assert NAMED_T == 293300 and NEED[5] < SP_2030 < NAMED_T < DRAFT_NEED_2030
BPCL_FEED_CEILING = 4000 * 0.05 * 365              # tonnes of used cooking oil a year if the unit ran every day at 5%
assert BPCL_FEED_CEILING == 73000 and CERT["BPCL Mumbai"] <= BPCL_FEED_CEILING
TRUALT_ML = 10 * 10                                 # 10 crore litres = 100 million litres

# ---- European Union: ReFuelEU Aviation ----
# Regulation (EU) 2023/2405, Annex I: SAF 2% 2025, 6% 2030, 20% 2035, 34% 2040, 42% 2045, 70% 2050; synthetic 1.2% average and 0.7% minimum
#   in 2030-31, 5% 2035, 10% 2040, 15% 2045, 35% 2050.  https://eur-lex.europa.eu/eli/reg/2023/2405/oj
EU_T = {2025: 2, 2030: 6, 2035: 20, 2040: 34, 2045: 42, 2050: 70}
EU_SYN = {2030: 0.7, 2035: 5, 2040: 10, 2045: 15, 2050: 35}
EU_SYN_AVG_2030 = 1.2
# EASA, ReFuelEU Aviation Annual Technical Report 2026 (17 Sep 2026, corrigendum 2 Nov 2026)  https://www.easa.europa.eu/en/downloads/144166/en
#   2025: 39.3 Mt aviation fuel supplied, 1.1 Mt SAF, 2.79%. 2030 jet demand assumed 44.385 Mt. Capacity in 2030: 1.5 Mt (scenario 1),
#   3.7 Mt (scenario 2), 5.5 Mt plus 0.6 Mt synthetic (scenario 3); "2.1 Mt required ... (excluding synthetic aviation fuels)"; 2026 announcements
#   would lift scenario 2 to 4.6 Mt. Prices 2025 (EASA report page): SAF EUR 1,925/t, conventional jet EUR 640/t.
EU_FUEL_2025, EU_SAF_2025, EU_SAF_SHARE = 39.3, 1.1, 2.79
EU_DEMAND_2030 = 44.385
EU_S1, EU_S2, EU_S3, EU_S3_SYN, EU_S2_WITH_2026 = 1.5, 3.7, 5.5, 0.6, 4.6
EU_NEED_EX_SYN = (EU_T[2030] - EU_SYN_AVG_2030) / 100 * EU_DEMAND_2030
EU_NEED_ALL = EU_T[2030] / 100 * EU_DEMAND_2030
EU_NEED_SYN = EU_SYN_AVG_2030 / 100 * EU_DEMAND_2030
assert round(EU_NEED_EX_SYN, 1) == 2.1 and round(EU_NEED_ALL, 2) == 2.66 and round(EU_NEED_SYN, 2) == 0.53
assert round(100 * EU_SAF_2025 / EU_FUEL_2025, 1) == 2.8          # EASA: 2.79%
assert EU_S1 < EU_NEED_EX_SYN < EU_S2 and round(EU_S2 / 2.1, 1) == 1.8
EU_VS_INDIA = EU_SAF_2025 * 1e6 / NEED[1]
assert 30 <= EU_VS_INDIA <= 31
P_SAF, P_JET = 1925, 640
assert round(P_SAF / P_JET, 1) == 3.0
# Neste, 10 Nov 2026: "realistic production capacity could reach 3.2 million tonnes by 2030 ... the 2.8 million tonnes required"; capacity
#   "already exceeds 1 million tonnes". The same three figures are in EASA's European Aviation Environmental Report 2025 (EU+EFTA, section 6.5).
#   https://www.neste.com/news-and-insights/aviation/saf-win-win-for-europe-competitiveness-and-resilience
#   https://www.easa.europa.eu/en/domains/environment/eaer/sustainable-aviation-fuels/saf-market
# IATA, The SAF Market in the EU (Oct 2026): 6% in 2030 "corresponding to 2.6 Mt of SAF according to EASA".
NESTE_CAP, NESTE_NEED, IATA_NEED = 3.2, 2.8, 2.6

# ---- United Kingdom: SAF Mandate ----
# DfT, SAF Mandate compliance guidance 2026, Table 6 (% of total fuel): 2025 2.00, 2026 3.60, 2027 5.20, 2028 6.80 (PtL 0.20), 2030 10.00 (PtL 0.50),
#   2035 15.00 (PtL 1.50).  https://assets.publishing.service.gov.uk/media/69a80cb5a2495f2d259f1425/dft-saf-mandate-compliance-guidance-26.pdf
# GOV.UK collection page: 22% in 2040; PtL 3.5% in 2040.  https://www.gov.uk/government/collections/sustainable-aviation-fuel-saf-mandate
UK_T = {2025: 2.0, 2027: 5.2, 2028: 6.8, 2030: 10.0, 2035: 15.0, 2040: 22}

# ---- Asia and Brazil ----
# Singapore: CAAS and Ministry of Transport pages (read Nov 2026): 1% uplift target for 2027, goal of 3-5% by 2030; levy on flights from 1 Jan 2027.
#   A CAAS release of 10 Nov 2025 gave 2026 as the start.  https://www.caas.gov.sg/sustainability/airline-domain-sustainability-initiatives
# South Korea: MOLIT / MOTIE, Sep 2025: 1% from 2027 on international departures, 3-5% in 2030, 7-10% in 2035 (ranges to be fixed in 2026 and 2029).
# Japan: METI subcommittee paper, 17 Aug 2026: 1% FY2030, 3% FY2031, 5% FY2032-34, international fuel at seven airports.
#   https://www.meti.go.jp/shingikai/enecho/shigen_nenryo/nenryo_seisaku/pdf/023_03_00.pdf  (committee approval 24 Aug 2026 per S&P Global)
# Indonesia: energy ministry Decree 113/2026 as tabulated by USDA FAS (GAIN ID2026-0033, Aug 2026): bio-avtur 1% 2027-28, 5% 2029-30, two airports.
# Malaysia: Bernama, 5 Nov 2026: 1% mandate "deferred to 2030" (one report).
# Brazil: Law 14.993/2024 and Decree 13.094 of 12 Aug 2026: emissions cut on domestic flights of 1% 2027, 1% 2028, 2% 2029, 3% 2030 ... 10% from 2037.
SG_2030, KR_2030, KR_2035 = (3, 5), (3, 5), (7, 10)
JP_FY2030, ID_2030, MY_2030 = 1, 5, 1
BR = {2027: 1, 2028: 1, 2029: 2, 2030: 3, 2035: 8, 2037: 10}
assert UK_T[2030] > EU_T[2030] > IN_T[2030] >= ID_2030 >= SG_2030[1] > JP_FY2030

TITLE = "Sustainable aviation fuel: India targets 5% by 2030, the EU 6% and the UK 10%"
assert 55 <= len(TITLE) <= 80, len(TITLE)


def t(v):
    """Tonnes rounded to the nearest hundred, for computed figures."""
    return f"{round(v, -2):,.0f}"


top = top_line([
    (f"{IN_T[2030]}% by 2030", f" is India&rsquo;s indicative target for sustainable aviation fuel (SAF) in jet fuel for international flights, after {IN_T[2027]}% in 2027 and "
                               f"{IN_T[2028]}% in 2028. The EU requires {EU_T[2030]}% and the UK {UK_T[2030]:.0f}% in 2030, on all flights and in law."),
    (f"About {round(NEED[1], -3):,.0f} tonnes", f" of SAF a year meets the 1% target at FY2025-26 sales: 1% of the {INTL_FY26 / 1000:.2f} million tonnes of jet fuel sold for international "
                                                f"flights (PPAC: 39% of 9.16 million tonnes). Certified refinery capacity is reported at {CERT_T:,} tonnes."),
    (f"{EU_SAF_2025} million tonnes", f" of SAF was supplied at EU airports in 2025, {EU_SAF_SHARE}% of fuel against a 2% minimum and about {round(EU_VS_INDIA, -1):.0f} times India&rsquo;s 1% need. "
                                      f"EASA counts {EU_S2} million tonnes of EU capacity by 2030 against {EU_NEED_EX_SYN:.1f} million needed."),
])

intro = (f'<p>This piece compares the targets, their scope and the tonnes behind them. The hydrogen each litre needs is in '
         f'<a href="{B}/2026/08/the-hydrogen-bill-hiding-inside-indias.html">Sustainable aviation fuel in India: hydrogen needed per litre, by pathway</a>; '
         f'eligibility is in <a href="{B}/2026/09/under-corsias-own-numbers-corn-ethanol.html">Corn ethanol jet fuel under CORSIA</a>; batch tracking is in '
         f'<a href="{B}/2026/10/how-to-use-saf-monitoring-system-track.html">How to use saf-monitoring-system</a>.</p>\n')

L_IN = "India <small>international flights; indicative</small>"
s1 = insight(
    "India's 2030 target of 5% is below the EU's 6% and the UK's 10%, and covers fewer flights",
    bars("India aims for 5% on international flights in 2030; the EU and UK require 6% and 10%",
         [("United Kingdom <small>all jet fuel; in law</small>", UK_T[2030]),
          ("European Union <small>all fuel at EU airports; in law</small>", EU_T[2030]),
          (L_IN, IN_T[2030]),
          ("Indonesia <small>two airports first; decree with conditions</small>", ID_2030),
          ("Singapore <small>departing flights; goal</small>", SG_2030),
          ("South Korea <small>international departures; range to be fixed</small>", KR_2030),
          ("Japan <small>international fuel at 7 airports; FY2030</small>", JP_FY2030),
          ("Malaysia <small>deferred from 2027; one report</small>", MY_2030)],
         accent=L_IN, unit="%",
         sub="SAF as a share of the jet fuel each scheme covers, 2030. The schemes cover different flights and differ in legal force.",
         source="Rajya Sabha USQ 828; Regulation (EU) 2023/2405; UK DfT guidance 2026; CAAS; MOLIT; METI, 17 August 2026; USDA FAS on Indonesia&rsquo;s Decree 113/2026; Bernama, 5 November 2026.")
    + numbers(["Scheme", "2027", "2030", "2035", "Covers", "Status"],
              [["United Kingdom", f"{UK_T[2027]}%", f"{UK_T[2030]:.0f}%", f"{UK_T[2035]:.0f}%", "all jet fuel supplied; power-to-liquid part 0.2% from 2028, 0.5% in 2030", f"in law since 1 January 2025; {UK_T[2040]}% in 2040"],
               ["European Union", f"{EU_T[2025]}%", f"{EU_T[2030]}%", f"{EU_T[2035]}%", f"fuel at EU airports; synthetic part {EU_SYN_AVG_2030}% average, {EU_SYN[2030]}% minimum in 2030", f"in law; {EU_T[2050]}% in 2050, {EU_SYN[2050]}% synthetic"],
               ["India", f"{IN_T[2027]}%", f"{IN_T[2030]}%", f"not set (draft, as reported: {DRAFT_2035}%)", "jet fuel for international flights", "indicative; policy not final on 20 July 2026"],
               ["Singapore", "1%", "3&ndash;5% goal", "&ndash;", "flights departing Singapore", "levy from 1 January 2027"],
               ["South Korea", "1%", "3&ndash;5%", "7&ndash;10%", "international departures", "roadmap of September 2025; ranges to be fixed"],
               ["Indonesia", "1%", "5%", "&ndash;", "two airports first", "Decree 113/2026, subject to readiness (USDA)"],
               ["Japan", "none", "1% (FY2030)", "not set (5% in FY2032 to FY2034)", "international fuel at seven airports", "METI proposal, August 2026"],
               ["Malaysia", "none", "1%", "&ndash;", "not stated", "deferred to 2030 (Bernama, one report)"],
               ["Brazil (emissions cut, not a blend)", f"{BR[2027]}%", f"{BR[2030]}%", f"{BR[2035]}%", "domestic flights", f"in law; {BR[2037]}% from 2037"]],
              "Show each scheme by year, scope and status"),
    f"India&rsquo;s 5% is close to the EU&rsquo;s 6% as a number, but it is an indicative target on international flights only, about {ALL_FUEL_EQUIV:.0f}% of all jet fuel "
    "sold in India at FY2025-26 shares, and the civil aviation ministry told Parliament on 20 July 2026 that the SAF policy was not final.",
    "Airlines and fuel suppliers should plan for 1% on international uplift from January 2027, as press reports of the draft policy describe, and treat the "
    "2035 and 2040 figures as unsettled until the policy is notified.",
    "targets")

L5 = "5% in 2030"
s2 = insight(
    f"India's 1% target for 2027 needs about {round(NEED[1], -3):,.0f} tonnes at FY2025-26 fuel sales",
    bars(f"Certified refinery capacity of {CERT_T:,} tonnes covers the 1% and 2% targets, not the 5%",
         [("1% in 2027", NEED[1]), ("2% in 2028", NEED[2]), (L5, NEED[5])],
         accent=L5, fmt=lambda v: f"{t(v)} t",
         ref=(CERT_T, f"{CERT_T:,} tonnes a year: four certified co-processing units, as reported by S&amp;P Global"),
         sub=f"Tonnes of SAF a year if each target is applied to FY2025-26 international jet fuel sales of {INTL_FY26 / 1000:.2f} million tonnes. "
             "Sales in 2027 to 2030 will differ.",
         source="Computed by this blog from PPAC Ready Reckoner FY 2025-26 (9,161 thousand tonnes of ATF, 39% international); capacity from S&amp;P Global, 28 September 2026.")
    + numbers(["Basis for the fuel sold to international flights", "1% target, tonnes a year", "Source"],
              [[f"FY2024-25: 26% of {ATF_FY25:,} thousand tonnes", t(NEED1_FY25), "PPAC; computed"],
               [f"FY2025-26: 39% of {ATF_FY26:,} thousand tonnes", t(NEED[1]), "PPAC; computed"],
               [f"April to September 2026, doubled: 49% of {ATF_H1FY27:,} thousand tonnes", t(NEED1_H1), "PPAC; computed"],
               ["Projection for 2027", f"about {SP_2027:,}", "S&amp;P Global Energy and SAF Association"],
               ["5% in 2030, projection", f"about {SP_2030:,}", "S&amp;P Global Energy and SAF Association"],
               [f"5% in 2030, on the draft policy&rsquo;s reported {DRAFT_INTL_2030_MT} million tonnes", f"{DRAFT_NEED_2030:,.0f}", "New Indian Express, 5 November 2026; computed"]],
              "Show the 1% requirement on four fuel bases, and two 2030 figures"),
    f"At FY2025-26 sales the 1% and 2% targets need about {t(NEED[1])} and {t(NEED[2])} tonnes, inside the {CERT_T:,} tonnes of certified co-processing capacity that "
    f"S&amp;P Global reports, while the 5% target needs about {t(NEED[5])} tonnes and depends on plants not yet built.",
    f"Oil marketing companies should publish contracted SAF volumes for 2027 against the {t(NEED1_FY25)} to {SP_2027:,} tonnes that the 1% target implies, "
    "and PPAC should define the international fuel base.",
    "tonnes")

s3 = insight(
    f"Named Indian refinery projects total about {round(NAMED_T, -3):,.0f} tonnes a year if all are built",
    waterfall(f"Two Indian Oil plants would add {ATJ_PANIPAT + PARADIP:,} tonnes to {CERT_T:,} of certified co-processing",
              ("Certified co-processing, four refineries <small>S&amp;P Global</small>", CERT_T),
              [("Indian Oil Panipat, ethanol-to-jet <small>planned for 2027-28</small>", ATJ_PANIPAT),
               ("Indian Oil and M11, Paradip <small>joint venture; no date in the source</small>", PARADIP)],
              "Named capacity if all are built", unit=" t",
              sub="SAF production capacity, tonnes a year. Certified means approved under ISCC CORSIA, not producing at that rate.",
              source="S&amp;P Global, 28 September 2026; Indian Oil Annual Report 2024-25; Indian Oil investor presentation, August 2026.")
    + numbers(["Plant", "Capacity", "Source and caveat"],
              [["BPCL Mumbai, co-processing", f"{CERT['BPCL Mumbai']:,} t", f"S&amp;P Global; an ICAO study lists 15,000 t; Topsoe says the 4,000 t/day unit will co-process 5% (at most {BPCL_FEED_CEILING:,.0f} t of feed a year), due by end-2026"],
               ["Indian Oil Panipat, co-processing", f"{CERT['Indian Oil Panipat']:,} t", "S&amp;P Global and Indian Oil (30 KTPA of neat SAF); 35,000 t in the ICAO study and Argus"],
               ["HPCL Visakh, co-processing", f"{CERT['HPCL Visakh']:,} t", "S&amp;P Global only"],
               ["MRPL Mangaluru, co-processing", f"{CERT['MRPL Mangaluru']:,} t", "S&amp;P Global; certified 24 April 2026 (MRPL); MRPL seeks 5,000 kilolitres of SAF for 2027"],
               ["Indian Oil Panipat, ethanol-to-jet", f"{ATJ_PANIPAT:,} t", "Indian Oil Annual Report 2024-25"],
               ["Indian Oil and M11, Paradip", f"{PARADIP:,} t", "Indian Oil investor presentation"],
               ["TruAlt Bioenergy, Bagalkot (not in the total)", f"{TRUALT_ML} million litres", "company release, 18 June 2026; Rs 150 crore PM JI-VAN aid"],
               ["PM JI-VAN approvals, June 2026", "3 commercial, 2 demonstration", "Rajya Sabha Starred Question 6; projects not named"]],
              "Show each plant, its capacity and its source"),
    f"Named refinery-linked capacity of {NAMED_T:,} tonnes exceeds the 5% need of {t(NEED[5])} tonnes at FY2025-26 sales and S&amp;P Global&rsquo;s projected {SP_2030:,} tonnes, "
    f"but not the {DRAFT_NEED_2030:,.0f} tonnes implied by the draft policy&rsquo;s reported 2030 fuel forecast, and {ATJ_PANIPAT + PARADIP:,} tonnes of it is not yet built.",
    "The petroleum ministry should publish commissioning dates and monthly SAF output for each plant, so buyers can tell certified capacity from fuel delivered.",
    "projects")

L_S2 = "Scenario 2 <small>plus plants under construction or with an investment decision</small>"
s4 = insight(
    f"EU supply: {EU_SAF_2025} Mt of SAF in 2025, and {EU_S2} Mt of capacity by 2030 against {EU_NEED_EX_SYN:.1f} Mt needed",
    bars(f"EU plants built, in construction or funded reach {EU_S2} Mt by 2030; {EU_NEED_EX_SYN:.1f} Mt is needed",
         [("Scenario 1 <small>plants able to make SAF at end-2025</small>", EU_S1),
          (L_S2, EU_S2),
          ("Scenario 3 <small>plus high-credibility announcements</small>", EU_S3)],
         accent=L_S2, unit=" Mt",
         ref=(round(EU_NEED_EX_SYN, 1), f"{EU_NEED_EX_SYN:.1f} Mt: SAF needed in 2030 for the 6% share, excluding the synthetic part (EASA)"),
         sub="EU SAF production capacity in 2030, million tonnes a year, excluding synthetic fuel. Capacity is maximum output, not a production forecast.",
         source="EASA, ReFuelEU Aviation Annual Technical Report 2026, as corrected 2 November 2026.")
    + numbers(["Item", "Value", "Source"],
              [["Aviation fuel supplied at EU airports, 2025", f"{EU_FUEL_2025} Mt", "EASA report 2026"],
               ["SAF supplied, 2025", f"{EU_SAF_2025} Mt, {EU_SAF_SHARE}%", "EASA report 2026"],
               ["Jet fuel demand assumed for 2030", f"{EU_DEMAND_2030} Mt", "EASA, from Eurocontrol"],
               ["6% of that demand", f"{EU_NEED_ALL:.2f} Mt", "computed"],
               [f"Synthetic part, {EU_SYN_AVG_2030}% average", f"{EU_NEED_SYN:.2f} Mt, against {EU_S3_SYN} Mt in scenario 3 only", "computed; EASA"],
               ["Scenario 2 with 2026 announcements", f"{EU_S2_WITH_2026} Mt", "EASA report 2026"],
               ["Neste, 10 November 2026", f"{NESTE_CAP} Mt capacity against {NESTE_NEED} Mt required", "matches EASA&rsquo;s 2025 environmental report"],
               ["IATA, October 2026", f"{IATA_NEED} Mt required", "citing EASA"],
               ["Average price, 2025", f"SAF €{P_SAF:,} a tonne; conventional jet €{P_JET} a tonne", "EASA"]]),
    f"On EASA&rsquo;s count the EU can meet the 6% share in 2030 from plants built, under construction or funded, while the synthetic part of about {EU_NEED_SYN:.1f} Mt "
    f"has no large plant past an investment decision, and Neste&rsquo;s {NESTE_CAP} Mt against {NESTE_NEED} Mt repeats EASA&rsquo;s older 2025 figures.",
    f"Indian producers planning exports should size EU demand on EASA&rsquo;s {EU_NEED_EX_SYN:.1f} Mt and {EU_S2} Mt figures, and treat the synthetic sub-target "
    "as the part of the EU market still short of supply.",
    "eu")

trail = f'''<details class="xv-n"><summary>India&rsquo;s document trail: what is official and what is press-reported</summary>
<ul>
<li><b>Official:</b> the targets appear in Parliament answers from the petroleum ministry (15 December 2025) and the civil aviation ministry (20, 27 and 30 July 2026), and in a PIB release of 23 April 2026. All call them &ldquo;indicative&rdquo;.</li>
<li><b>Official:</b> on 17 April 2026 the ATF Control Order was amended to bring SAF-blended jet fuel within it.</li>
<li><b>Official:</b> on 20 July 2026 the civil aviation ministry said the SAF policy &ldquo;has not been finalised yet&rdquo;.</li>
<li><b>Press-reported:</b> a draft national SAF policy, seen by four newspapers in early November 2026, makes 1% mandatory from 2027, adds {DRAFT_2029}% in 2029, penalties, and indicative {DRAFT_2035}% in 2035 and {DRAFT_2040}% in 2040. A PTI report carried by CNBC TV18 gives {DRAFT_2040_PTI}% by 2040.</li>
<li><b>Not found:</b> the order or minutes that approved the indicative targets, and the draft policy text itself.</li>
</ul></details>
'''

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Civil Aviation:</b> notify the SAF policy before 1 January 2027, stating who is obliged, the fuel base, the compliance year and the penalty.</li>
<li><b>PPAC:</b> publish how jet fuel is classed as international, with monthly tonnes, since the reported share moved from 26% in FY2024-25 to 49% in April to September 2026.</li>
<li><b>Ministry of Petroleum and Natural Gas:</b> publish SAF produced, blended and sold by refinery each month, as EASA reports for the EU each year.</li>
<li><b>DGCA:</b> open the SAF registry described in the draft policy, with batch-level records, so each tonne is claimed once.</li>
<li><b>Both ministries:</b> state whether imported SAF counts toward the targets; press accounts of the draft differ on this.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = f'''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>India&rsquo;s tonnes are PPAC jet fuel (ATF) sales, times PPAC&rsquo;s international share, times the target. The 39% share is rounded, so the 1% figure carries about {t(SHARE_ROUNDING_T)} tonnes of rounding either way.</li>
<li>The April to September 2026 basis doubles six months of sales. It is a rate, not a forecast.</li>
<li>India&rsquo;s 5% as a share of all jet fuel is 5% times 39%, {ALL_FUEL_EQUIV:.2f}%.</li>
<li>The EU&rsquo;s {EU_NEED_EX_SYN:.1f} Mt is EASA&rsquo;s figure; it equals (6% minus {EU_SYN_AVG_2030}%) of {EU_DEMAND_2030} Mt. The full 6% is {EU_NEED_ALL:.2f} Mt.</li>
<li>Shares are as each scheme states them. The UK awards certificates by energy and emissions saving; Brazil sets an emissions cut, so it is left off the chart.</li>
<li>Capacity figures are nameplate tonnes a year. Co-processing units and HEFA plants can switch between SAF and other fuels.</li>
</ul></details>
'''

gaps = f'''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The text of India&rsquo;s draft SAF policy, and the instrument that approved the indicative targets. The 2040 figure is {DRAFT_2040}% in four reports and {DRAFT_2040_PTI}% in one.</li>
<li>Why PPAC&rsquo;s international share of jet fuel rose from 26% (FY2024-25) to 39% (FY2025-26) and 49% (April to September 2026). PPAC says the split comes from oil companies and is not based on tax treatment.</li>
<li>India&rsquo;s 2030 requirement: {t(NEED[5])} tonnes at FY2025-26 sales, about {SP_2030:,} (S&amp;P Global) or {DRAFT_NEED_2030:,.0f} (the draft&rsquo;s reported forecast).</li>
<li>Whether any Indian refinery has sold SAF commercially. Sources disagree on BPCL Mumbai (61,000 or 15,000 tonnes) and Indian Oil Panipat (30,000 or 35,000).</li>
<li>The EU&rsquo;s 2030 requirement appears as {NESTE_NEED} Mt, {EU_NEED_ALL:.2f} Mt and {IATA_NEED} Mt, and realistic capacity as {NESTE_CAP} Mt or {EU_S2} Mt, depending on the EASA edition used.</li>
<li>Singapore&rsquo;s start year: 2026 in a CAAS release of November 2025 and in PIB&rsquo;s April 2026 release, 2027 on current CAAS and transport ministry pages.</li>
<li>Japan: PIB cites 10% by 2030, an earlier airline-use goal; METI&rsquo;s supply obligation starts at 1% in FY2030.</li>
<li>Indonesia and Malaysia rest on one secondary source each. Thailand, Vietnam, China and the United States are not covered, and CORSIA offsets are left to a separate piece.</li>
</ul></details>
'''

body = STYLE + top + intro + s1 + s2 + s3 + s4 + trail + fixes + method + gaps

SOURCES = (
    '<a href="https://sansad.in/getFile/annex/271/AU828_tu5NZH.pdf?source=pqars">Rajya Sabha USQ 828, Ministry of Civil Aviation, 27 July 2026</a> (indicative targets); '
    '<a href="https://sansad.in/getFile/annex/269/AU1737_T6tK0c.pdf?source=pqars">Rajya Sabha USQ 1737, Ministry of Petroleum and Natural Gas, 15 December 2025</a>; '
    '<a href="https://sansad.in/getFile/annex/271/AU41_uTds0S.pdf?source=pqars">Rajya Sabha USQ 41, 20 July 2026</a> (policy not finalised); '
    '<a href="https://sansad.in/getFile/annex/271/AS6_36Hhd1.pdf?source=pqars">Rajya Sabha Starred Question 6, 20 July 2026</a> (certifications, PM JI-VAN approvals); '
    '<a href="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU1978_e8NuiA.pdf?source=lsapps">Lok Sabha USQ 1978, 30 July 2026</a>; '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2255021&amp;lang=1&amp;reg=3">PIB, Ministry of Petroleum and Natural Gas, 23 April 2026</a> (ATF Control Order); '
    'draft SAF policy, press reports only: <a href="http://www.thehindubusinessline.com/economy/logistics/draft-saf-policy-proposes-90-per-cent-local-fuel-uplift-for-international-airlines/article71665373.ece">BusinessLine, 4 November 2026</a>, '
    '<a href="https://www.ndtvprofit.com/business/govt-proposes-mandatory-saf-blending-for-airlines-from-jan-2027-in-draft-policy-target-20-by-2040-12278793">NDTV Profit, 3 November 2026</a>, '
    '<a href="https://www.livemint.com/industry/indias-green-aviation-push-comes-with-a-fuel-bill-saf-mandate-to-hit-airlines-11793795774046.html">Mint, 5 November 2026</a>, '
    '<a href="https://www.newindianexpress.com/story/india/2026/nov/05/dgca-green-aviation-fuel-norms-ready">New Indian Express, 5 November 2026</a> (2030 fuel forecast), '
    '<a href="https://www.cnbctv18.com/business/aviation/india-may-mandate-sustainable-aviation-fuel-from-2027-what-it-means-airlines-airfares-20028776.htm">CNBC TV18 with PTI, 7 November 2026</a> (40% by 2040); '
    '<a href="https://ppac.gov.in/download.php?file=rep_studies%2F1784899305_The_PPAC_Ready_Reckoner_FY_2025%E2%80%9326_Final.pdf">PPAC Ready Reckoner FY 2025-26</a> (ATF 9,161 thousand tonnes, 39% international; FY2024-25 8,985 and 26%); '
    '<a href="https://ppac.gov.in/download.php?file=menu%2F1792999364_ICR_September%2026.pdf">PPAC Industry Consumption Report, September 2026</a> (4,443 thousand tonnes, 49% international); '
    '<a href="https://ppac.gov.in/download.php?file=menu/1779264620_ICR_April_2026.pdf">PPAC Industry Consumption Report, April 2026</a> (note that the sector split is supplied by oil companies); '
    '<a href="https://www.spglobal.com/energy/en/news-research/latest-news/agriculture/092826-india-positioned-to-meet-2027-saf-targets-by-coprocessing-2030-goals-need-urgent-finance-report">S&amp;P Global, 28 September 2026</a> '
    '(report with the SAF Association: 46,000 and 250,000 tonnes; 106,500 tonnes certified; a secondary source for plant capacities); '
    '<a href="https://iocl.com/download/SingleAnnualReport202425.pdf">Indian Oil Annual Report 2024-25</a>; '
    '<a href="https://iocl.com/uploads/IOCL_Investor_Presentation_25-26.pdf">Indian Oil investor presentation FY2025-26</a>; '
    '<a href="https://www.topsoe.com/news/topsoe-secures-technology-contract-for-bharat-petroleums-saf-project-in-india">Topsoe, 14 October 2026</a> (BPCL Mumbai); '
    '<a href="https://www.icao.int/sites/default/files/environmental-protection/Documents/ACT-SAF/Feasibility_Study_India.pdf">ICAO ACT-SAF feasibility study for India</a>; '
    '<a href="https://nsearchives.nseindia.com/corporate/MRPL_15072026194248_PressreleaseSD.pdf">MRPL release, 15 July 2026</a> and '
    '<a href="https://admin.mrpl.co.in/img/UploadedFiles/ExpressionofInterest/Files/Hindi/4305df9009094e129b6b978a2828555c.pdf">MRPL expression of interest for SAF</a>; '
    '<a href="https://trualtbioenergy.com/public/assets/fronted/governance-investor/Press%20Release_18062026.pdf">TruAlt Bioenergy, 18 June 2026</a>; '
    '<a href="https://www.argusmedia.com/en/news-and-insights/latest-market-news/2723366-india-s-ioc-gets-iscc-certification-for-saf-at-panipat">Argus, 21 August 2025</a>; '
    '<a href="https://eur-lex.europa.eu/eli/reg/2023/2405/oj">Regulation (EU) 2023/2405, Annex I</a>; '
    '<a href="https://www.easa.europa.eu/en/downloads/144166/en">EASA, ReFuelEU Aviation Annual Technical Report 2026, corrected 2 November 2026</a> and its '
    '<a href="https://www.easa.europa.eu/en/document-library/general-publications/refueleu-aviation-annual-technical-report-2026">report page</a> (prices); '
    '<a href="https://www.easa.europa.eu/en/domains/environment/eaer/sustainable-aviation-fuels/saf-market">EASA, European Aviation Environmental Report 2025, SAF market</a>; '
    '<a href="https://www.neste.com/news-and-insights/aviation/saf-win-win-for-europe-competitiveness-and-resilience">Neste, 10 November 2026</a>; '
    '<a href="https://www.iata.org/contentassets/0bf212bfcb0548f2b6ad4c1e229f7e94/the-saf-market-in-the-eu.pdf">IATA, The SAF Market in the European Union, October 2026</a>; '
    '<a href="https://assets.publishing.service.gov.uk/media/69a80cb5a2495f2d259f1425/dft-saf-mandate-compliance-guidance-26.pdf">UK Department for Transport, SAF Mandate compliance guidance 2026, Table 6</a>; '
    '<a href="https://www.gov.uk/government/collections/sustainable-aviation-fuel-saf-mandate">GOV.UK, SAF Mandate</a>; '
    '<a href="https://www.caas.gov.sg/sustainability/airline-domain-sustainability-initiatives">Civil Aviation Authority of Singapore</a> and its '
    '<a href="https://www.caas.gov.sg/resources/media-and-publication/newsroom/new-sustainable-aviation-fuel-levy-to-apply-from-1-april-2026-for-flights-departing-from-1-october-2026">release of 10 November 2025</a>; '
    '<a href="https://www.molit.go.kr/LCMS/DWN.jsp?fileName=SAF%20Blending%20Becomes%20Mandatory%20for%20International%20Flights%20Departing%20Korea%20in%202027.pdf&amp;fold=%2Feng0301%2F">South Korea, MOLIT, September 2025</a>; '
    '<a href="https://www.meti.go.jp/shingikai/enecho/shigen_nenryo/nenryo_seisaku/pdf/023_03_00.pdf">Japan, METI subcommittee paper, 17 August 2026</a> and '
    '<a href="https://www.spglobal.com/energy/en/news-research/latest-news/crude-oil/082426-japan-to-proceed-with-oil-shipping-aid-restore-national-crude-reserves-to-90-days-of-net-imports">S&amp;P Global, 24 August 2026</a>; '
    '<a href="https://www.fas.usda.gov/data/gain-report/2026/08/Biofuels%20Annual_Jakarta_Indonesia_ID2026-0033.pdf">USDA FAS, Indonesia Biofuels Annual, August 2026</a> (Decree 113/2026, secondary); '
    '<a href="https://bernamabiz.com/news.php?id=2630516">Bernama, 5 November 2026</a> (Malaysia, one report); '
    '<a href="https://www.gov.br/anp/pt-br/assuntos/saf">Brazil, ANP</a> and '
    '<a href="https://www.gov.br/portos-e-aeroportos/pt-br/assuntos/noticias/2026/08/programa-de-combustivel-sustentavel-de-aviacao-e-regulamentado">Ministry of Ports and Airports, 12 August 2026</a>. '
    'Tonnes for India and the EU checks are computed by this blog. Capacity is not production, and targets marked indicative, goal or reported are not obligations. Analysed 16 November 2026.')

RELATED = [
    (f"{B}/2026/08/the-hydrogen-bill-hiding-inside-indias.html", "Sustainable aviation fuel in India: hydrogen needed per litre, by pathway"),
    (f"{B}/2026/09/under-corsias-own-numbers-corn-ethanol.html", "Corn ethanol jet fuel under CORSIA: worse than the fossil fuel it replaces"),
    (f"{B}/2026/10/how-to-use-saf-monitoring-system-track.html", "How to use saf-monitoring-system: track SAF batches against blending and carbon-credit rules"),
    (f"{B}/2026/10/the-hydrogen-behind-biofuel-mandate.html", "Biofuel mandates by country: EU, UK and some member states set hydrogen quotas"),
    (f"{B}/2026/09/india-wants-isobutanol-in-both-diesel.html", "Isobutanol in India: planned for diesel and jet fuel, with almost no dedicated production"),
]

build("Aviation fuel &middot; Policy",
      TITLE,
      "India&rsquo;s indicative target for sustainable aviation fuel reaches 5% of jet fuel for international flights in 2030; the EU and the UK require 6% and 10% of all "
      f"jet fuel by law. India&rsquo;s first step, 1% in 2027, is about {round(NEED[1], -3):,.0f} tonnes at FY2025-26 sales. The policy that would make it binding was still a draft in November 2026.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars title")
