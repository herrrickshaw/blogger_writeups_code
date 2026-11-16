"""CORSIA second phase from 1 January 2027: India's entry, the supply of eligible emissions units, and the bill.
Build from the repo root:  python3 out/research/corsia-india-2027/build.py
Every figure is from the source named beside it (URL and date in the comment) or computed here with an assert."""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, line, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-corsia-india-2027-mandatory-offset-credit-supply.html"
B = "https://blog.vertistratsolution.com"

# ---------------------------------------------------------------- sources (URL, date read: 15-16 Nov 2026)
U = {
    # ICAO Assembly Resolution A42-22, para 9 e): second phase 2027-2035, 0.5% / 90% RTK rule, LDC/SIDS/LLDC exempt. Oct 2025
    "a42": "https://www.icao.int/sites/default/files/environmental-protection/Assembly42/Resolution-A42-22_CORSIA.pdf",
    # ICAO, 2018 International Total RTK ranking by State (published Aug 2019)
    "rtk": "https://www.icao.int/sites/default/files/environmental-protection/CORSIA/Documents/Background%20Information/International-RTK-rankings_2018_SIDS_LDC_LLDC.pdf",
    # ICAO, CORSIA States for Chapter 3 State Pairs, 7th edition, 16 July 2026: 134 States from 1 Jan 2027
    "states": "https://www.icao.int/sites/default/files/environmental-protection/CORSIA/Documents/CORSIA_States_for_Chapter_3_State-Pairs_7Ed_16_July.pdf",
    "states_page": "https://www.icao.int/CORSIA/corsia-states-chapter-3-state-pairs",
    # ICAO CORSIA Newsletter Aug-Sep 2026 (6 Oct 2026): ~44 million labelled; 700 million to 1 billion potential; 31 Jan 2028
    "nl_sep": "https://www.icao.int/sites/default/files/environmental-protection/CORSIA/Newsletter/CORSIA-Newsletter_August-September-2026_Final.pdf",
    # ICAO CORSIA Newsletter Oct 2026 (6 Nov 2026): 8 programmes for 2027-2029; LoA letter to States 27 Oct 2026
    "nl_oct": "https://www.icao.int/sites/default/files/environmental-protection/CORSIA/Newsletter/CORSIA-Newsletter_October-2026.pdf",
    # ICAO CAEP, Technical assessments for the 2025 CORSIA periodic review, Council 235th session, June 2025
    "caep": "https://www.icao.int/sites/default/files/environmental-protection/CORSIA/Documents/CAEP_Inputs-to-2025-CORSIA-periodic-review-C235.pdf",
    # ICAO TAB recommendations, Sept 2026: unit dates for 2027-2029
    "tab": "https://www.icao.int/sites/default/files/environmental-protection/CORSIA/TAB/2026/SECTION-4_TAB-RECOMMENDATIONS_SEPTEMBER-2026.pdf",
    # ICAO ESAF/WACAF workshop slides, 2026: 32.4 million labelled as of 9 March 2026
    "wacaf": "https://www.icao.int/sites/default/files/WACAF/MeetingDocs/2026/ENV/ESAF-WACAF%20and%20IATA%20Joint%20Virtual%20Workshop%20on%20CORSIA%20CEEUs%2C%20Letters%20of%20Authorisation/English/CORSIA_CEEUs_TAB_LoAs.pdf",
    # Annex 16 Vol IV, 2nd ed., Appendix 1 timeline (copy hosted by the Swiss FOCA): 31 Jan 2028 and 31 Jan 2031
    "annex": "https://www.bazl.admin.ch/dam/it/sd-web/UVhYwPu6Prla/icao_annex_16_environmentalprotectionvolumeiv-corsia.pdf",
    # European Parliament study PE 795.717, Oct 2026, section 7.1.2
    "ep": "https://www.europarl.europa.eu/RegData/etudes/STUD/2026/795717/ECTI_STU(2026)795717_EN.pdf",
    # Environmental Defense Fund blog, 27 July 2026: ~41 million; "up to four times"
    "edf": "https://blogs.edf.org/energyexchange/2026/07/27/corsia-at-a-crossroads-the-next-year-will-determine-its-course",
    # IATA Chart of the Week, 18 Sept 2026: 72 million under 42 LoAs (Aug 2026); 200-250 million needed
    "iata_sep": "https://www.iata.org/en/iata-repository/publications/economic-reports/corsia-eeu-supply-is-growing-but-not-fast-enough",
    # IATA Chart of the Week, 28 Oct 2026: first-phase demand 169.5 to 214.8 Mt; ~43 million tagged
    "iata_oct": "https://www.iata.org/en/iata-repository/publications/economic-reports/corsia-first-phase-in-numbers",
    # IATA press release, 6 June 2026: SAF 2.4 Mt in 2026, 0.8% of aviation fuel use
    "iata_saf": "https://www.iata.org/en/pressroom/2026-releases/06-06-saf-production-volumes-still-disappointing",
    # ICCT working paper, Sept 2026: India aviation emissions inventory and CORSIA implementation (Table 11)
    "icct": "https://theicct.org/wp-content/uploads/2026/08/ID-628-%E2%80%93-India-CORSIA_working-paper_final.pdf",
    # DGCA CAR Section 10, Series C, Part I, Issue 2, 8 Oct 2024
    "car": "https://www.dgca.gov.in/digigov-portal/Upload?attachId=BFA8%2BhtVyvlpuKGZg1dXOg%3D%3D&flag=iframeAttachView",
    # DGCA slides at ICAO APAC CORSIA seminar, May 2025: Indian operators
    "dgca_ppt": "https://www.icao.int/sites/default/files/APAC/Meetings/2025/2025%20CORSIASAP/Presentations/PPT-FOR-ICAO-CORSIA-SEMINAR_India.pdf",
    # PIB, 28 April 2023: India decided not to participate in the voluntary phases
    "pib23": "https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1920505&lang=2&reg=48",
    # PIB, 29 July 2026: minister's review of SAF and CORSIA preparedness
    "pib26": "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2291473&lang=1&n=cdcd&reg=48",
    # Rajya Sabha USQ 33, 20 July 2026: obligation from 2027; SAF targets 1% / 2% / 5%
    "rs33": "https://sansad.in/getFile/annex/271/AU33_JrIVUh.pdf?source=pqars",
    # Lok Sabha USQ 4012 (2019-20): India filed reservations in 2016 and 2019
    "ls4012": "https://sansad.in/getFile/loksabhaquestions/annex/172/AU4012.pdf?source=pqals",
    # ICAO A40 plenary minutes (Doc 10132 corr.): text of India's reservations to A40-18 and A40-19
    "a40": "https://www.icao.int/sites/default/files/Meetings/AMC/ArchivedAssembly/en/A40/10132_corr1_en.pdf",
    # ICAO summary listing of reservations to A41-21 and A41-22 (2022)
    "a41": "https://www.icao.int/sites/default/files/2025-02/a41_res_sum_en.pdf",
    # ICAO Doc 10227, Assembly Resolutions in Force as of 3 Oct 2025, Appendix A
    "a42res": "https://www.icao.int/sites/default/files/Meetings/a42/Documents/Resolutions/10227_en.pdf",
    # IATA CORSIA Handbook (Feb 2024), compliance-cycle table: notification by 30 Nov 2030, cancellation by 31 Jan 2031
    "iata_hb": "https://www.iata.org/contentassets/fb745460050c48089597a3ef1b9fe7a8/corsia-handbook.pdf",
    # Fastmarkets voluntary carbon report, 26 Aug 2026: CORSIA Phase 1 spot $12.40
    "fm": "https://a.storyblok.com/f/179543/x/82debc0b12/fastmarkets-report-26th-aug-2026.pdf",
    # General Index, October 2026 pricing analysis (5 Nov 2026): CEEU averaged $12.85/mt
    "gx": "https://www.general-index.com/analytics-posts/october-pricing-analysis-global-voluntary-carbon-markets",
    # Carbon Pulse, 6 Nov 2026: about 42 million labelled as of 30 Oct by its own registry count
    "cp": "https://carbon-pulse.com/568383?site=nzp",
}


def a(key, text):
    return f'<a href="{html.escape(U[key])}">{text}</a>'


# ---------------------------------------------------------------- 1. who is in, and why
THRESHOLD = 0.5                                            # per cent of 2018 international RTK (A42-22, para 9 e)
RTK_TOTAL = 735_574                                        # million RTK, "Total of above States" (ICAO ranking)
RTK = {"China": (1, 90_858.7, 12.35), "Russian Federation": (9, 21_396.7, 2.91),      # (rank, million RTK, share %)
       "India": (20, 9_949.0, 1.35), "Brazil": (26, 5_764.5, 0.78)}
for name, (_, mrtk, share) in RTK.items():
    assert round(100 * mrtk / RTK_TOTAL, 2) == share, name          # ICAO's printed share matches its own totals
    assert share > THRESHOLD
STATES_2021, STATES_2026, STATES_2027 = 88, 130, 134       # ICAO newsletters; 6th and 7th editions of the States list
ADDED_2027 = ["Brazil", "China", "India", "Russian Federation"]     # 7th edition amendment note, 16 July 2026
assert STATES_2026 + len(ADDED_2027) == STATES_2027
INDIA_X = RTK["India"][2] / THRESHOLD
assert round(INDIA_X, 1) == 2.7

# ---------------------------------------------------------------- 2. supply against first-phase demand (million units; 1 unit = 1 t CO2)
LABELLED = 44                    # "approximately 44 million" labelled, ICAO newsletter Aug-Sep 2026
LABELLED_MARCH = 32.4            # ICAO slides: as of 9 March 2026
EDF_UNITS = 41                   # EDF, 27 July 2026, reading ICAO's tracker
LOA_COVERED, LOAS = 72, 42       # IATA, as of August 2026 (includes verified but unissued units)
ICAO_DEMAND = (105, 150)         # ICAO CAEP, June 2025: first phase 2024-2026, Mt CO2
ICAO_ALL = (950, 1500)           # same source: 2024-2035
IATA_DEMAND = (169.5, 214.8)     # IATA, 28 Oct 2026
POOL = (700, 1000)               # ICAO newsletter: potential pool, million units, mitigation years 2021-2026
GUYANA = 24_963_214              # ICAO dashboard table, as of 29 Sep 2026 (newsletter Aug-Sep 2026)
HOSTS = [("Guyana", "ART", 24_963_214), ("Rwanda", "Gold Standard and VCS", 622_891 + 5_530_081),
         ("Cambodia", "VCS", 3_369_411), ("Madagascar", "VCS", 2_822_091), ("Nigeria", "Gold Standard and VCS", 1_624_017 + 40_188),
         ("Malawi", "Gold Standard", 1_524_196), ("Lao PDR", "VCS", 1_276_305), ("Gambia", "VCS", 196_652),
         ("Tanzania", "Gold Standard", 180_867), ("Sierra Leone", "VCS", 2_078)]
HOST_SUM = sum(h[2] for h in HOSTS)
assert HOST_SUM == 42_151_991 and HOST_SUM < LABELLED * 1e6          # the table is cut off in the text copy; rows read sum to 42.2 million
assert GUYANA / (LABELLED * 1e6) > 0.5                                 # "more than half"
GAP_LO, GAP_HI = ICAO_DEMAND[0] / LABELLED, IATA_DEMAND[1] / LABELLED
assert round(GAP_LO, 1) == 2.4 and round(GAP_HI, 1) == 4.9
assert 3.5 < ICAO_DEMAND[1] / EDF_UNITS < 4                            # EDF's "up to four times": 150 / 41 = 3.7
PHASE2_ICAO = (ICAO_ALL[0] - ICAO_DEMAND[0], ICAO_ALL[1] - ICAO_DEMAND[1])
assert PHASE2_ICAO == (845, 1350)

# ---------------------------------------------------------------- 3. India's requirement (ICCT working paper, Sept 2026, Table 11; Mt CO2)
YEARS = list(range(2027, 2036))
COVERED = [9.86, 10.25, 10.66, 11.09, 11.54, 12.00, 12.49, 13.00, 13.54]
OFFSET = [2.58, 2.77, 2.97, 3.14, 3.38, 3.62, 4.21, 4.47, 4.61]
ICCT_TOTAL, ICCT_BASELINE = 31.76, 5.9
assert abs(sum(OFFSET) - ICCT_TOTAL) < 0.02 and abs(sum(COVERED) - 104.43) < 0.02
FIRST_PERIOD = sum(OFFSET[:3])                                         # 2027-2029, cancellation due 31 January 2031
assert round(FIRST_PERIOD, 1) == 8.3
SHARE_27, SHARE_35 = OFFSET[0] / COVERED[0], OFFSET[-1] / COVERED[-1]
assert round(100 * SHARE_27) == 26 and round(100 * SHARE_35) == 34     # "about a quarter", "a third"
SAF_2027_KT = 26                                                       # ICCT: 1% SAF in 2027 cuts about 26 kt
assert round(100 * SAF_2027_KT / (OFFSET[0] * 1000)) == 1
CEF_SHARE = 9.2                                                        # ICCT: % of 2027-2035 requirement met by eligible fuels
SAF_MT, SAF_SHARE = 2.4, 0.8                                           # IATA, 6 June 2026

# ---------------------------------------------------------------- 4. the bill ($ million, 2027-2035, Indian carriers)
ICCT_COST, ICCT_TIGHT = 781, 2600                                      # ICCT: sufficient supply; tighter supply ("approximately $2.6 billion")
ICCT_PRICE, ICCT_TIGHT_PRICE = (21, 27), (61, 91)                      # $/t CO2, 2027-2035
ICCT_2027, ICCT_2035 = 53.6, 124.9                                     # $ million a year
assert abs(ICCT_2027 / OFFSET[0] - ICCT_PRICE[0]) < 0.5               # ICCT's 2027 bill is about its low-end price times 2.58 Mt
PRICE_OCT, PRICE_AUG = 12.85, 12.40                                    # General Index, Oct 2026 average; Fastmarkets, 26 Aug 2026
COST_SPOT = ICCT_TOTAL * PRICE_OCT
assert round(COST_SPOT) == 408
assert round(ICCT_TIGHT / ICCT_COST, 1) == 3.3

# ---------------------------------------------------------------- headline
TITLE = "CORSIA from 2027: India joins with about 44 million eligible units labelled"
assert 55 <= len(TITLE) <= 80 and str(LABELLED) in TITLE

top = top_line([
    (f"{STATES_2027} states", f" are in CORSIA offsetting from 1 January 2027, up from {STATES_2026}. ICAO&rsquo;s July 2026 list adds Brazil, China, India "
                              f"and Russia. India&rsquo;s 2018 traffic share was {RTK['India'][2]}%, above the {THRESHOLD}% threshold."),
    (f"About {LABELLED} million", f" units were labelled as eligible by late September 2026, ICAO says. Demand for 2024 to 2026 is estimated at "
                                  f"{ICAO_DEMAND[0]} to {ICAO_DEMAND[1]} million (ICAO) or {IATA_DEMAND[0]} to {IATA_DEMAND[1]} million (IATA), due by 31 January 2028."),
    (f"{OFFSET[0]} million tonnes", f" is the offset requirement ICCT projects for Indian carriers in 2027, rising to {OFFSET[-1]} million by 2035. "
                                    f"Their first cancellation deadline is 31 January 2031."),
])

intro = f'''<p>CORSIA is the offsetting scheme of the International Civil Aviation Organization (ICAO) for international flights. Airlines offset growth in emissions above 85% of the 2019 level by cancelling approved carbon credits, called eligible emissions units.</p>
<p>The {a("ep", "European Parliament&rsquo;s COP31 study")} of October 2026 says participation becomes mandatory from 1 January 2027 for states above a 0.5% traffic share. ICAO&rsquo;s own {a("a42", "Resolution A42-22")} confirms the rule, with exemptions for least developed, small island and landlocked developing states.</p>
'''

LBL = {"China": "China <small>rank 1</small>", "Russian Federation": "Russia <small>rank 9</small>",
       "India": "India <small>rank 20</small>", "Brazil": "Brazil <small>rank 26</small>"}
s1 = insight(
    f"India joins CORSIA offsetting in 2027: its 2018 traffic share was {RTK['India'][2]}%, above {THRESHOLD}%",
    bars("All four states added for 2027 were above ICAO&rsquo;s 0.5% traffic threshold in 2018",
         [(LBL[k], v[2]) for k, v in RTK.items()], accent=LBL["India"], unit="%",
         ref=(THRESHOLD, f"{THRESHOLD}% of international traffic, the threshold in ICAO Assembly Resolution A42-22"),
         sub="Share of 2018 international revenue tonne-kilometres (passengers and cargo carried, times distance), %.",
         source="ICAO, 2018 international RTK ranking by state; ICAO, CORSIA States for Chapter 3 State Pairs, 7th edition, 16 July 2026.")
    + numbers(["State", "Rank, 2018", "Million RTK", "Share"],
              [[k, v[0], f"{v[1]:,.1f}", f"{v[2]}%"] for k, v in RTK.items()] + [["All reporting states", "", f"{RTK_TOTAL:,}", "100%"]]),
    f"India did not volunteer for the 2021 to 2026 phases, and ICAO&rsquo;s 2027 list applies the Assembly&rsquo;s traffic rule, "
    f"so routes between India and the other {STATES_2027 - 1} listed states carry offsetting requirements from 2027.",
    f"Airlines flying to and from India should check their 2027 schedules against ICAO&rsquo;s list of {STATES_2027} states, "
    "because only routes between two listed states count.",
    "who")

s2 = insight(
    f"Eligible units: about {LABELLED} million labelled, against {ICAO_DEMAND[0]} to {IATA_DEMAND[1]:.0f} million needed by 2028",
    bars(f"Labelled supply is about {LABELLED} million units; the lowest demand estimate is {ICAO_DEMAND[0]} million",
         [("Labelled as eligible <small>ICAO, late September 2026</small>", LABELLED, "", f"about {LABELLED} million"),
          (f"Covered by {LOAS} host-country letters <small>IATA, August 2026; includes units not yet issued</small>", LOA_COVERED, "", f"about {LOA_COVERED} million"),
          ("Demand, 2024 to 2026 <small>ICAO technical committee, June 2025</small>", ICAO_DEMAND),
          ("Demand, 2024 to 2026 <small>IATA, October 2026</small>", IATA_DEMAND)],
         accent="Labelled as eligible <small>ICAO, late September 2026</small>", unit=" million",
         sub="Million emissions units; one unit is one tonne of CO2. Demand is the total airlines must cancel for 2024 to 2026 by 31 January 2028.",
         source="ICAO CORSIA Newsletter, August-September 2026; IATA Chart of the Week, 18 September and 28 October 2026; "
                "ICAO CAEP inputs to the 2025 CORSIA periodic review.")
    + numbers(["Host country", "Programme", "Units labelled"],
              [[h, p, f"{n:,}"] for h, p, n in HOSTS],
              "Show where the labelled units come from (ICAO dashboard, 29 September 2026)"),
    f"Demand is {GAP_LO:.1f} to {GAP_HI:.1f} times the labelled supply, Guyana alone issued more than half of it, and ICAO puts the potential pool at "
    f"{POOL[0]} million to {POOL[1] / 1000:.0f} billion units, of which IATA counts about {LOA_COVERED} million under host-country letters of authorisation.",
    "Host governments, India included, should publish how and when they will issue letters of authorisation, "
    "because that step decides how many units reach airlines.",
    "supply")

s3 = insight(
    f"Indian carriers: about {OFFSET[0]:.1f} million tonnes to offset in 2027, {OFFSET[-1]:.1f} million by 2035",
    line("Indian carriers must offset about a quarter of covered emissions in 2027, a third by 2035",
         {"Covered": list(zip(YEARS, COVERED)), "To offset": list(zip(YEARS, OFFSET))},
         accent="To offset", unit="Mt",
         sub="Million tonnes of CO2 a year, projected. Covered: Indian carriers&rsquo; emissions on international routes between CORSIA states. "
             "To offset: the part needing units.",
         source="ICCT working paper, India aviation emissions inventory and CORSIA implementation, September 2026, Table 11.")
    + numbers(["Year", "Covered emissions, Mt", "Offset requirement, Mt"],
              [[y, f"{c:.2f}", f"{o:.2f}"] for y, c, o in zip(YEARS, COVERED, OFFSET)] + [["2027 to 2035", "104.43", f"{ICCT_TOTAL}"]]),
    f"On ICCT&rsquo;s projection Indian carriers need about {FIRST_PERIOD:.1f} million units for 2027 to 2029, "
    "and ICAO&rsquo;s Annex 16 timeline sets cancellation for that period at 31 January 2031.",
    f"Indian airlines should plan purchases from their 2027 emissions onward, because supply for 2024 to 2026 had reached only about "
    f"{LABELLED} million labelled units in the third year of that period.",
    "india")

s4 = insight(
    f"Cost to Indian carriers: ${ICCT_COST} million over nine years, $2.6 billion if units are scarce",
    bars(f"Scarce units would lift Indian carriers&rsquo; bill from ${ICCT_COST} million to about $2.6 billion",
         [(f"At ${PRICE_OCT} a unit throughout <small>October 2026 average for first-phase units; computed by this blog</small>", round(COST_SPOT)),
          (f"At ${ICCT_PRICE[0]} to ${ICCT_PRICE[1]} a unit <small>ICCT, sufficient supply</small>", ICCT_COST),
          (f"At ${ICCT_TIGHT_PRICE[0]} to ${ICCT_TIGHT_PRICE[1]} a unit <small>ICCT, tighter supply</small>", ICCT_TIGHT, "", "about $2.6 billion")],
         accent=f"At ${ICCT_TIGHT_PRICE[0]} to ${ICCT_TIGHT_PRICE[1]} a unit <small>ICCT, tighter supply</small>", unit="$ million",
         sub=f"Cumulative cost of {ICCT_TOTAL} million units, 2027 to 2035, US$ million.",
         source=f"ICCT working paper, September 2026; General Index, 5 November 2026 (CEEU average ${PRICE_OCT}); "
                f"first bar = {ICCT_TOTAL} million units &times; ${PRICE_OCT}."),
    f"The bill depends more on the unit price than on traffic, and first-phase units were assessed at ${PRICE_AUG:.2f} a tonne in late August 2026 (Fastmarkets) "
    f"and averaged ${PRICE_OCT} in October (General Index), below the ${ICCT_PRICE[0]} to ${ICCT_PRICE[1]} that ICCT assumed.",
    "The DGCA should add a penalty provision to its CORSIA requirements, which this blog did not find in the October 2024 text, "
    "so that airlines that buy units are not undercut by those that do not.",
    "cost")

rules = f'''<h2 class="gb-h2" id="rules">What India has put in place</h2>
<p><b>Rules.</b> The DGCA&rsquo;s {a("car", "Civil Aviation Requirement, Section 10, Series C, Part I")} was first issued on 24 December 2018 and reissued on 8 October 2024. It covers monitoring, reporting, verification and the cancelling of units. The DGCA is to tell each operator its requirement by 30 November each year.</p>
<p><b>Airlines.</b> A {a("dgca_ppt", "DGCA presentation to an ICAO seminar")} in May 2025 lists IndiGo, SpiceJet, Air India (with Vistara merged into it), Air India Express and Akasa Air as the Indian operators under CORSIA.</p>
<p><b>Preparation.</b> The civil aviation minister {a("pib26", "reviewed readiness on 29 July 2026")}. The meeting discussed letters of authorisation and a CORSIA-compliant carbon market framework. This blog found no published outcome of either.</p>
<p><b>Reservations.</b> India {a("ls4012", "filed reservations")} to the CORSIA resolutions in 2016 and 2019. Its {a("a40", "2019 text")} asked for a baseline &ldquo;closer to 2027&rdquo; for developing states. ICAO&rsquo;s lists for {a("a41", "2022")} and {a("a42res", "2025")} record no reservation by India.</p>

<h2 class="gb-h2" id="saf">Sustainable aviation fuel covers little of the requirement</h2>
<p>Airlines can also reduce their requirement with CORSIA-eligible fuels. {a("iata_saf", "IATA estimated in June 2026")} that sustainable aviation fuel output will be about {SAF_MT} million tonnes in 2026, {SAF_SHARE}% of aviation fuel use.</p>
<p>India&rsquo;s indicative targets are 1% by 2027, 2% by 2028 and 5% by 2030 for international flights. ICCT estimates the 1% blend cuts the 2027 requirement by about {SAF_2027_KT} thousand tonnes, roughly 1%, and that eligible fuels meet {CEF_SHARE}% of the 2027 to 2035 total.</p>
<p>Two earlier posts cover the fuel side: <a href="{B}/2026/09/under-corsias-own-numbers-corn-ethanol.html">corn ethanol jet fuel under CORSIA</a> and <a href="{B}/2026/08/the-hydrogen-bill-hiding-inside-indias.html">hydrogen needed per litre of sustainable aviation fuel in India</a>.</p>
'''

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>DGCA:</b> publish the enforcement and penalty provisions for airlines that do not cancel units, and the cancellation-report template, before the first 2027 emissions report.</li>
<li><b>Ministry of Civil Aviation, with the environment ministry:</b> publish the outcome of the July 2026 review on letters of authorisation, including whether Indian projects may supply units to airlines.</li>
<li><b>Indian airlines:</b> disclose projected CORSIA requirements and unit purchases in annual reports, starting with 2027.</li>
<li><b>ICAO:</b> report labelled units for the 2027 to 2029 period separately on its dashboard, next to an updated demand estimate.</li>
<li><b>Host governments of approved projects:</b> issue pending letters of authorisation before the 31 January 2028 deadline for 2024 to 2026.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

dates = f'''<details class="xv-n"><summary>Phase 1 and phase 2: the dates that apply to Indian airlines</summary>
<ul>
<li><b>2021 to 2023 (pilot) and 2024 to 2026 (first phase):</b> voluntary for states. India stayed out; its airlines have reported emissions to the DGCA since 2019.</li>
<li><b>31 January 2028:</b> airlines of the {STATES_2026} states in the first phase cancel units for 2024 to 2026. This deadline does not cover routes brought in by India&rsquo;s entry.</li>
<li><b>1 January 2027:</b> the second phase starts ({STATES_2027} states). It runs to 2035 in three-year compliance periods.</li>
<li><b>30 November 2030:</b> states notify airlines of final requirements for 2027 to 2029.</li>
<li><b>31 January 2031:</b> cancellation deadline for 2027 to 2029, or 60 days after the state&rsquo;s notification if that is later.</li>
<li><b>Units:</b> eight programmes are approved for 2027 to 2029 after the ICAO Council&rsquo;s November 2026 session. Units must come from emission reductions between 1 January 2021 and 31 December 2029.</li>
</ul></details>
'''

method = f'''<details class="xv-n"><summary>Method</summary>
<ul>
<li>Traffic shares are ICAO&rsquo;s 2018 figures; each was recomputed from ICAO&rsquo;s million-RTK column and its total of {RTK_TOTAL:,} million.</li>
<li>Supply uses ICAO&rsquo;s &ldquo;approximately 44 million&rdquo; labelled units. The multiples {GAP_LO:.1f} and {GAP_HI:.1f} are {ICAO_DEMAND[0]} &divide; {LABELLED} and {IATA_DEMAND[1]} &divide; {LABELLED}.</li>
<li>The Environmental Defense Fund&rsquo;s &ldquo;up to four times&rdquo;, quoted by the European Parliament study, is {ICAO_DEMAND[1]} &divide; {EDF_UNITS} million, which is {ICAO_DEMAND[1] / EDF_UNITS:.1f}.</li>
<li>The host-country table lists the rows legible in ICAO&rsquo;s newsletter. They sum to {HOST_SUM / 1e6:.1f} million; the rest of the table was cut off in the copy read.</li>
<li>India&rsquo;s requirement and costs are ICCT projections. The {FIRST_PERIOD:.1f} million for 2027 to 2029 is the sum of ICCT&rsquo;s three yearly figures.</li>
<li>The ${round(COST_SPOT)} million bar is {ICCT_TOTAL} million units at ${PRICE_OCT}, held flat. It is an illustration, not a forecast.</li>
</ul></details>
'''

gaps = f'''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>Whether India has notified penalties for non-compliance. The October 2024 DGCA text read here has none, and ICCT says no national penalty policy had been adopted when it published.</li>
<li>Each Indian airline&rsquo;s share of the requirement. ICCT publishes a national total only.</li>
<li>Whether India has issued any letter of authorisation for CORSIA units.</li>
<li>A price for units eligible for 2027 to 2029. The prices quoted are for first-phase units.</li>
<li>How many units are labelled for 2027 to 2029. ICAO&rsquo;s dashboard figure covers the first phase.</li>
<li>ICAO&rsquo;s live dashboard itself. The figure used is from ICAO&rsquo;s newsletter.</li>
</ul></details>
'''

body = STYLE + top + intro + s1 + s2 + s3 + s4 + rules + fixes + dates + method + gaps

SOURCES = (
    "<b>ICAO:</b> " + a("a42", "Assembly Resolution A42-22") + " (paragraph 9 e); "
    + a("rtk", "2018 international RTK ranking") + "; "
    + a("states", "CORSIA States for Chapter 3 State Pairs, 7th edition, 16 July 2026") + " and its " + a("states_page", "index page") + "; "
    + a("nl_sep", "CORSIA Newsletter, August-September 2026") + "; " + a("nl_oct", "CORSIA Newsletter, October 2026") + "; "
    + a("caep", "CAEP inputs to the 2025 periodic review, June 2025") + "; " + a("tab", "Technical Advisory Body recommendations, September 2026") + "; "
    + a("wacaf", "workshop slides on eligible units, 2026") + "; " + a("annex", "Annex 16, Volume IV, Appendix 1") + " (copy hosted by the Swiss aviation office); "
    + a("a40", "40th Assembly plenary minutes") + "; " + a("a41", "reservations to A41-21 and A41-22") + "; " + a("a42res", "Assembly Resolutions in Force, October 2025") + ".<br>"
    "<b>India:</b> " + a("car", "DGCA CAR Section 10, Series C, Part I, Issue 2, 8 October 2024") + "; " + a("dgca_ppt", "DGCA slides, ICAO seminar, May 2025") + "; "
    + a("pib23", "PIB, 28 April 2023") + "; " + a("pib26", "PIB, 29 July 2026") + "; " + a("rs33", "Rajya Sabha unstarred question 33, 20 July 2026") + "; "
    + a("ls4012", "Lok Sabha unstarred question 4012") + ".<br>"
    "<b>Others:</b> " + a("ep", "European Parliament, COP31 Climate Change Conference, Part I (PE 795.717), October 2026") + "; "
    + a("edf", "Environmental Defense Fund, 27 July 2026") + "; " + a("iata_sep", "IATA, 18 September 2026") + "; " + a("iata_oct", "IATA, 28 October 2026") + "; "
    + a("iata_saf", "IATA, 6 June 2026") + "; " + a("iata_hb", "IATA CORSIA Handbook") + "; " + a("icct", "ICCT working paper, September 2026") + "; " + a("fm", "Fastmarkets, 26 August 2026") + "; "
    + a("gx", "General Index, 5 November 2026") + "; " + a("cp", "Carbon Pulse, 6 November 2026") + ".<br>"
    f"<b>Caveats:</b> Counts of labelled units differ by date and method: ICAO counted {LABELLED_MARCH} million on 9 March 2026, "
    f"the Environmental Defense Fund read about {EDF_UNITS} million in late July, "
    f"ICAO about {LABELLED} million in late September, IATA about 43 million in October, and Carbon Pulse counted about 42 million on 30 October. "
    f"Demand estimates differ more: ICAO&rsquo;s committee gives {ICAO_DEMAND[0]} to {ICAO_DEMAND[1]} million tonnes for 2024 to 2026 "
    f"(the Environmental Defense Fund quotes 100 to 150), IATA gave 200 to 250 million in September and {IATA_DEMAND[0]} to {IATA_DEMAND[1]} million in October. "
    "The European Parliament study describes the 0.5% rule as a share of traffic; ICAO&rsquo;s text specifies 2018 revenue tonne-kilometres and adds a second test, "
    "the states that together make up 90% of traffic. Unit prices are from price-reporting agencies, not ICAO. "
    "India&rsquo;s requirement and cost figures are projections by one research group."
)

RELATED = [
    (f"{B}/2026/09/under-corsias-own-numbers-corn-ethanol.html", "Corn ethanol jet fuel under CORSIA: worse than the fossil fuel it replaces"),
    (f"{B}/2026/08/the-hydrogen-bill-hiding-inside-indias.html", "Sustainable aviation fuel in India: hydrogen needed per litre, by pathway"),
    (f"{B}/2026/08/indias-carbon-credit-market-domestic.html", "India's carbon credit market: the domestic compliance scheme and Article 6.2"),
    (f"{B}/2026/09/india-solved-carbon-credit-banking-with.html", "Carbon credits in India: banking has no limit or expiry, trading not yet live"),
    (f"{B}/2026/09/india-wants-isobutanol-in-both-diesel.html", "Isobutanol in India: planned for diesel and jet fuel, with almost no dedicated production"),
]

STANDFIRST = (f"ICAO&rsquo;s offsetting scheme for international flights covers India, China, Brazil and Russia from 1 January 2027. "
              f"Airlines already in the scheme need {ICAO_DEMAND[0]} to {IATA_DEMAND[1]:.0f} million units by January 2028, and about {LABELLED} million are labelled. "
              f"Indian carriers&rsquo; first deadline is January 2031.")

build("Aviation &middot; Carbon markets", TITLE, STANDFIRST, body, SOURCES, RELATED, str(OUT))

# ---------------------------------------------------------------- house checks on the written text
text = OUT.read_text(encoding="utf-8")
vis = re.sub(r"<(style|script)[\s\S]*?</\1>", " ", text)
for m in re.finditer(r"<p(?:\s[^>]*)?>([\s\S]*?)</p>", body):
    words = len(html.unescape(re.sub(r"<[^>]+>", " ", m.group(1))).split())
    assert words <= 60, (words, m.group(1)[:80])
plain = html.unescape(re.sub(r"<[^>]+>", " ", vis))
assert not re.search(r"\b(you|your|we|our)\b", plain, re.I), re.search(r"\b(you|your|we|our)\b", plain, re.I)
assert "masaladeutsch.blogspot" not in body and "Masala" not in body
print("wrote", OUT.relative_to(ROOT), "|", len(TITLE), "chars title |", len(plain.split()), "words")
