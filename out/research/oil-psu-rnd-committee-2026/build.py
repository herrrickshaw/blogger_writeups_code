"""Oil PSU R&D: the Ninth Report of the Standing Committee on Petroleum and Natural Gas (presented 12 Aug 2026), its own spend and profit tables, and what a minimum-R&D benchmark would mean.
Build from the repo root:  python3 out/research/oil-psu-rnd-committee-2026/build.py   (writes out/post-oil-psu-rnd-committee-2026.html)
Every figure is from the report (Lok Sabha Secretariat PDF, 74 pages, read from the text layer: Part I paras 1.1-1.9, Part II Observations 1-5 and 13, start-up replies 1.38-1.39)
or the PRS summary, or is computed below with an assert. Analysed 25 November 2026.
"""
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-oil-psu-rnd-committee-2026.html"
STEPS = 8


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


# ---- 1. the report's own R&D spend table (para 1.2, Rs crore), transcribed row by row
step(1, "R&D spend table (para 1.2) and column totals")
YEARS = ["FY2021-22", "FY2022-23", "FY2023-24", "FY2024-25", "FY2025-26"]
SPEND = {
    "ONGC": [531.59, 569.85, 686.68, 667.31, 744.48],
    "IOCL": [576.55, 698.21, 946.14, 1067.03, 717.13],
    "HPCL": [363.67, 319.22, 352.50, 463.25, 579.41],
    "BPCL": [219.82, 168.60, 189.97, 220.99, 295.84],
    "GAIL": [243.70, 180.71, 250.20, 375.53, 262.67],
    "OIL": [100.96, 179.03, 149.22, 147.3, 173.22],
    "EIL": [28.55, 30.10, 29.12, 26.79, 23.25],
    "BLC": [7.91, 7.84, 8.36, 9.01, 10.24],
    "MRPL": [1.01, 0.57, 5.57, 40.18, 46.73],
    "NRL": [2.73, 2.09, 11.97, 27.69, 38.14],
    "CPCL": [7.15, 9.72, 10.72, 12.73, 17.84],
}
TOTALS_PRINTED = [2083.64, 2165.94, 2640.45, 3057.81, 2908.95]       # the TOTAL row printed in the report
assert len(SPEND) == 11                                              # '11 PSUs' (PRS summary; report table)
for j, tot in enumerate(TOTALS_PRINTED):
    assert abs(sum(v[j] for v in SPEND.values()) - tot) < 0.011, (YEARS[j], sum(v[j] for v in SPEND.values()), tot)   # every printed total equals the sum of its column
T = TOTALS_PRINTED
G_5Y = 100 * (T[4] / T[0] - 1)
G_PEAK_TO_LAST = 100 * (T[4] / T[3] - 1)
assert f"{G_5Y:.1f}" == "39.6" and f"{G_PEAK_TO_LAST:.1f}" == "-4.9"
assert T[3] == max(T) and T[4] < T[3]
# report text conflict: Observation 1 says spend rose 'to Rs.2098.95 crore in FY 2025-26'; the table total is 2908.95 (digits transposed)
OBS_TYPO = 2098.95
assert OBS_TYPO != T[4] and sorted(str(OBS_TYPO).replace(".", "")) == sorted(str(T[4]).replace(".", ""))
IOCL_FALL = 100 * (SPEND["IOCL"][4] / SPEND["IOCL"][3] - 1)
GAIL_FALL = 100 * (SPEND["GAIL"][4] / SPEND["GAIL"][3] - 1)
assert f"{IOCL_FALL:.1f}" == "-32.8" and f"{GAIL_FALL:.1f}" == "-30.1"
# without IOCL and GAIL the other nine PSUs rose in FY2025-26
OTHER9_24 = T[3] - SPEND["IOCL"][3] - SPEND["GAIL"][3]
OTHER9_25 = T[4] - SPEND["IOCL"][4] - SPEND["GAIL"][4]
assert OTHER9_25 > OTHER9_24
OTHER9_G = 100 * (OTHER9_25 / OTHER9_24 - 1)
assert f"{OTHER9_G:.1f}" == "19.4"
TOP2 = SPEND["ONGC"][4] + SPEND["IOCL"][4]
TOP2_SHARE = 100 * TOP2 / T[4]
assert f"{TOP2_SHARE:.1f}" == "50.2"
MRPL_X = SPEND["MRPL"][4] / SPEND["MRPL"][0]
assert round(MRPL_X) == 46

# ---- 2. the Ministry's profit table (para 1.5, FY2025-26): R&D as a share of profit AFTER tax
step(2, "share of profit after tax (para 1.5) and recomputation")
PAT = {"ONGC": 32894, "OIL": 4455.34, "IOCL": 43677.32, "BPCL": 23303, "HPCL": 17175.23, "EIL": 691.59, "GAIL": 6968}
PCT_PRINTED = {"ONGC": 2.26, "OIL": 3.89, "IOCL": 1.64, "BPCL": 1.27, "HPCL": 3.0, "EIL": 3.36, "GAIL": 3.77}
PCT_OTHERS = {"BLC": 4.17, "MRPL": 2.42, "NRL": 1.25, "CPCL": 0.58}      # printed as percentages only; their PAT is not in the report
COMP = {k: 100 * SPEND[k][4] / PAT[k] for k in PAT}
for k in PAT:
    if k != "HPCL":
        assert abs(COMP[k] - PCT_PRINTED[k]) < 0.011, (k, COMP[k], PCT_PRINTED[k])      # six of seven printed percentages reproduce
assert f"{COMP['HPCL']:.2f}" == "3.37" and COMP["HPCL"] - PCT_PRINTED["HPCL"] > 0.36     # HPCL printed as 3%; the printed R&D and PAT give 3.37%
RD7 = sum(SPEND[k][4] for k in PAT)
PAT7 = sum(PAT.values())
assert round(RD7, 2) == 2796.00 and round(PAT7, 2) == 129164.48                         # the report's combined row: 2796 and 1,29,164.5
COMB = 100 * RD7 / PAT7
assert f"{COMB:.2f}" == "2.16"                                                          # the report's '2.16 %'
REST4 = sum(SPEND[k][4] for k in PCT_OTHERS)
assert round(REST4, 2) == 112.95 and round(RD7 + REST4, 2) == T[4]
ALL_PCT = sorted(list(COMP.values()) + list(PCT_OTHERS.values()))
assert (round(ALL_PCT[0], 2), round(ALL_PCT[-1], 2)) == (0.58, 4.17)                    # range over all 11 PSUs
assert (round(min(COMP.values()), 2), round(max(COMP.values()), 2)) == (1.27, 3.89)      # range over the seven with printed PAT
assert max(COMP.values()) / min(COMP.values()) > 3          # 'more than three times' in section 3
# PRS says the PSU-wise range is 1.3% to 3.8%: that is the seven-PSU range with 3.89 cut to 3.8
assert round(max(COMP.values()), 1) == 3.9

# ---- 3. illustrative benchmark: lift the two PSUs below the combined share to it (computed; the report names no percentage)
step(3, "illustrative benchmark arithmetic")
GAP = {k: COMB / 100 * PAT[k] - SPEND[k][4] for k in PAT if COMP[k] < COMB}
assert sorted(GAP) == ["BPCL", "IOCL"]
GAP_SUM = sum(GAP.values())
assert f"{GAP['IOCL']:.1f}" == "228.3" and f"{GAP['BPCL']:.1f}" == "208.6" and f"{GAP_SUM:.0f}" == "437"
GAP_PCT_OF_TOTAL = 100 * GAP_SUM / T[4]
assert f"{GAP_PCT_OF_TOTAL:.1f}" == "15.0"
# ONGC lies above it by construction; HPCL, EIL, GAIL, OIL are above
assert all(COMP[k] > COMB for k in ("ONGC", "HPCL", "EIL", "GAIL", "OIL"))

# ---- 4. other counts in the report
step(4, "start-up, publication, centre and sector counts")
STARTUPS = {"IOCL": 42, "BPCL": 30, "HPCL": 28, "EIL": 29, "GAIL": 38}           # Observation 13
assert sum(STARTUPS.values()) == 167 and sum(STARTUPS.values()) > 150             # PRS: 'more than 150'
STARTUPS_OIL = 25                                                                  # para 1.38: 'currently 25 (startups) are being funded by OIL'
assert sum(STARTUPS.values()) + STARTUPS_OIL == 192
PAPERS = {"IOCL": 127, "BPCL": 71, "HPCL": 144, "EIL": 21}                         # Observation 4
assert sum(PAPERS.values()) == 363                                                 # the report's 'total output of 363 papers between 2022 and 2025'
MANPOWER = {"IOCL": 457, "BPCL": 60, "HPCL": 140, "EIL": 53, "GAIL": 9, "ONGC": 842, "OIL": 58}      # oral evidence, 24 Feb 2025 (para 1.15)
assert sum(MANPOWER.values()) == 1619                                              # the witness also said 'nearly 2,000' in para 1.16
GERD_PET, GERD_ALL = 1634.45, 127380.96
assert f"{100 * GERD_PET / GERD_ALL:.1f}" == "1.3"                                 # 1.3% in 2020-21 (para 1.6)
assert 16 + 5 == 21                                                                # 16 R&D centres and five regional labs (Annexure I)

TITLE = "Oil PSU R&D: Rs 2,909 crore in FY2025-26, 2.16% of profit after tax at seven majors"
assert 55 <= len(TITLE) <= 90, len(TITLE)
assert not any(w in TITLE.lower().split() for w in ("you", "your", "we", "our"))

step(5, "writing sections")
top = top_line([
    (f"Rs {T[4]:,.0f} crore", f" is the R&D spend of 11 oil PSUs in FY2025-26, {abs(G_PEAK_TO_LAST):.1f}% below the Rs {T[3]:,.0f} crore peak of FY2024-25 and {G_5Y:.1f}% above Rs {T[0]:,.0f} crore in FY2021-22 (the report&rsquo;s own table; computed changes)."),
    (f"{COMB:.2f}%", f" of seven major PSUs&rsquo; profit after tax went on R&amp;D in FY2025-26, from {min(COMP.values()):.2f}% at BPCL to {max(COMP.values()):.2f}% at OIL; the committee asked for a floor tied to profit before tax, a figure the report does not give."),
    ("No number", " is what the committee recommends: a minimum &lsquo;preferably&rsquo; set as a percentage of profit before tax, and the Ministry told it there is no such guideline today."),
])

s1 = insight(
    f"Oil PSU R&D spend peaked at Rs {T[3]:,.0f} crore in FY2024-25 and fell {abs(G_PEAK_TO_LAST):.1f}% in FY2025-26",
    bars("R&D spend of 11 oil PSUs, Rs crore: up 39.6% in four years, down in the latest year",
         [(y, round(v, 2)) for y, v in zip(YEARS, T)], accent=YEARS[4], vmax=3600, fmt=lambda v: f"Rs {v:,.2f} crore",
         sub="Total of the 11 PSUs in the report&rsquo;s table (para 1.2); every printed total reproduces as the sum of its column (checked). The report&rsquo;s Observation 1 prints the FY2025-26 figure as Rs 2,098.95 crore, which is the table&rsquo;s Rs 2,908.95 crore with digits transposed.",
         source="Standing Committee on Petroleum and Natural Gas, Ninth Report, para 1.2 (primary); changes computed here.")
    + numbers(["PSU"] + YEARS, [[k] + [f"{x:,.2f}" for x in v] for k, v in SPEND.items()] + [["Total"] + [f"{x:,.2f}" for x in T]]),
    f"The fall in FY2025-26 comes from two companies, IOCL ({IOCL_FALL:.1f}%) and GAIL ({GAIL_FALL:.1f}%), while the other nine together rose {OTHER9_G:.1f}% (computed).",
    "The Ministry should state why IOCL and GAIL spent less, because the report gives no reason and the Ministry told the committee spending is rising year on year.",
    anchor="spend")

rows2 = sorted(((k, v[4]) for k, v in SPEND.items()), key=lambda x: -x[1])
s2 = insight(
    f"ONGC and IOCL account for {TOP2_SHARE:.1f}% of the Rs {T[4]:,.0f} crore spent in FY2025-26",
    bars("ONGC spent Rs 744 crore and IOCL Rs 717 crore of the Rs 2,909 crore in FY2025-26",
         [(k, round(v, 2)) for k, v in rows2], accent=["ONGC", "IOCL"], vmax=900, fmt=lambda v: f"Rs {v:,.2f} crore",
         sub=f"FY2025-26 R&amp;D spend by company, Rs crore. BLC is Balmer Lawrie, EIL is Engineers India, MRPL is Mangalore Refinery, NRL is Numaligarh Refinery, CPCL is Chennai Petroleum. MRPL&rsquo;s spend is {MRPL_X:.0f} times its FY2021-22 level (computed), from a base of Rs 1.01 crore.",
         source="Ninth Report, para 1.2 (primary); shares computed here.")
    + numbers(["PSU", "FY2025-26 spend (Rs crore)", "Share of total (%)"],
              [[k, f"{v:,.2f}", f"{100 * v / T[4]:.1f}"] for k, v in rows2]),
    "Two upstream and refining majors carry half the sector&rsquo;s reported research budget, so a benchmark for the group is mostly a benchmark for them.",
    "The Ministry should publish the spend of each PSU in the same table as its R&amp;D headcount, because the headcounts in the oral evidence (1,619 across seven PSUs) sit apart from the money.",
    anchor="split")

pct_rows = sorted(list(((k, round(v, 2)) for k, v in COMP.items())) + list(PCT_OTHERS.items()), key=lambda x: -x[1])
s3 = insight(
    f"R&D took {COMB:.2f}% of seven oil PSUs&rsquo; profit after tax in FY2025-26, from {min(COMP.values()):.2f}% to {max(COMP.values()):.2f}%",
    bars("R&D as a share of profit after tax, FY2025-26: 0.58% to 4.17% across 11 PSUs",
         pct_rows, accent=["BPCL", "IOCL"], unit="%", vmax=5, ref=(round(COMB, 2), f"seven-PSU combined share, {COMB:.2f}%"),
         sub="Per cent of profit after tax (PAT). Seven PSUs are recomputed from the Ministry&rsquo;s R&amp;D and PAT figures; BLC, MRPL, NRL and CPCL appear in the report only as printed percentages, so their PAT is not shown. HPCL is printed as 3% in the report; its own figures give 3.37%.",
         source="Ninth Report, para 1.5 (Ministry reply, primary data, not audited); recomputed here. PRS summary quotes 1.3% to 3.8% for the seven.")
    + numbers(["PSU", "R&D (Rs crore)", "PAT (Rs crore)", "Share printed in report", "Share recomputed"],
              [[k, f"{SPEND[k][4]:,.2f}", f"{PAT[k]:,.2f}", ("3%" if k == "HPCL" else f"{PCT_PRINTED[k]:.2f}%"), f"{COMP[k]:.2f}%"] for k in PAT]
              + [["Combined, seven PSUs", "2,796.00", "1,29,164.50", "2.16%", f"{COMB:.2f}%"]]
              + [[k, f"{SPEND[k][4]:,.2f}", "not in report", f"{v:.2f}%", "n/a"] for k, v in PCT_OTHERS.items()]),
    "The spread is more than three times between the lowest and highest of the seven, and the committee&rsquo;s benchmark is tied to profit before tax, which is higher than profit after tax for any company paying tax.",
    "The Ministry should give the committee profit before tax for each PSU for FY2025-26, because without it the proposed benchmark cannot be tested against any company&rsquo;s actual spend.",
    anchor="profit")

s4 = insight(
    f"A floor at the {COMB:.2f}% average would add about Rs {GAP_SUM:,.0f} crore at IOCL and BPCL (illustrative)",
    bars("Lifting IOCL and BPCL to 2.16% of profit after tax adds Rs 228 crore and Rs 209 crore",
         [("IOCL", round(GAP["IOCL"], 1)), ("BPCL", round(GAP["BPCL"], 1))], accent=["IOCL", "BPCL"], vmax=300, fmt=lambda v: f"Rs {v:,.1f} crore",
         sub=f"Computed, not from the report: extra R&amp;D needed in FY2025-26 for each of the two PSUs below the seven-PSU combined share to reach {COMB:.2f}% of its profit after tax. The sum is {GAP_PCT_OF_TOTAL:.1f}% of the Rs {T[4]:,.0f} crore total. The committee names no percentage, and its benchmark is on profit before tax.",
         source="Ninth Report, paras 1.2 and 1.5 and Observation 1 (primary); scenario computed here.")
    + numbers(["PSU", "Actual (Rs crore)", "At 2.16% of PAT (Rs crore)", "Gap (Rs crore)"],
              [[k, f"{SPEND[k][4]:,.2f}", f"{COMB / 100 * PAT[k]:,.2f}", f"{GAP[k]:,.2f}"] for k in ("IOCL", "BPCL")]),
    "Setting the floor at today&rsquo;s group average would cost the two lowest spenders about 15% of the sector&rsquo;s total R&amp;D budget, and would leave the other five unaffected.",
    "The Ministry should publish the percentage it will test before it sets a benchmark, with profit before tax as the base the committee asked for.",
    anchor="benchmark")

recs = '''<details class="xv-n"><summary>What the committee recommended, by theme</summary>
<ul>
<li><b>Minimum spend (Observation 1):</b> a benchmark of minimum R&amp;D expenditure for all oil PSUs, &lsquo;preferably a minimum percentage of their Profit Before Tax&rsquo;, reviewed periodically; a dedicated fund to co-finance cross-sector R&amp;D (green hydrogen, carbon capture, biofuels, waste-to-energy); measures for private co-investment.</li>
<li><b>People (Observation 2):</b> a dedicated R&amp;D career track, incentives for deployed patents and royalty-earning technologies, a common HR framework with a three-year manpower projection.</li>
<li><b>Centres and benchmarking (Observation 3):</b> a standard benchmarking system for the 16 R&amp;D centres and five regional laboratories (innovation productivity, technology transfer success rate, external collaboration, commercial adoption, clean-energy fit); board-level R&amp;D representation (only IOCL has it today); funding for fundamental science.</li>
<li><b>Output and review (Observations 4 and 5):</b> standard annual R&amp;D reporting, since the four centres named published 363 papers in 2022 to 2025 (IOCL 127, BPCL 71, HPCL 144, EIL 21); a unified review body with the Centre for High Technology; a cross-PSU review of projects near technology readiness level 6; a public list of projects on the Centre for High Technology website.</li>
<li><b>Start-ups (Observation 13):</b> IOCL, BPCL, HPCL, EIL and GAIL have funded 42, 30, 28, 29 and 38 start-ups, 167 in all (computed), consistent with the PRS summary&rsquo;s &lsquo;more than 150&rsquo;; OIL reports 25 currently funded. The committee asks for a fund for full-scale trials of proven start-up technology.</li>
<li><b>Also covered:</b> enhanced oil recovery and deep-water support, shale oil and gas hydrates, refining efficiency, an umbrella research organisation, patents and monetisation, net-zero research. These are in the report and are not examined here.</li>
</ul></details>
'''

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Petroleum and Natural Gas:</b> publish one annual table with each PSU&rsquo;s R&amp;D spend, profit before tax and profit after tax, so that a benchmark on profit before tax can be checked.</li>
<li><b>Ministry of Petroleum and Natural Gas:</b> define what counts as R&amp;D expenditure, including whether campus construction such as IOCL&rsquo;s Rs 3,199 crore second campus is counted, before any floor is set.</li>
<li><b>Lok Sabha Secretariat and the committee:</b> issue a correction for the Rs 2,098.95 crore figure in Observation 1 and for the 3% printed for HPCL in para 1.5.</li>
<li><b>Oil PSUs:</b> report start-ups on one definition (funded, engaged or currently funded), since the counts in the report mix the three.</li>
<li><b>Centre for High Technology:</b> publish the list of ongoing and completed projects the committee asked for, with spend per project.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The report was read from the Lok Sabha Secretariat PDF (74 pages, text layer): Part I paras 1.1 to 1.9 (spend, profit, GERD), 1.10 to 1.22 (people, centres), the start-up replies 1.38 and 1.39, and Part II Observations and Recommendations 1 to 5, 6, 7 and 13. Other sections (refining efficiency, umbrella organisation, patents, net zero) and the annexures and minutes were not analysed. The PRS summary was read in full.</li>
<li>R&amp;D spend is the Ministry&rsquo;s figure for each company as printed; the report does not define what is counted. Profit is profit after tax (PAT) as printed by the Ministry; the committee&rsquo;s recommendation refers to profit before tax (PBT), which the report does not give.</li>
<li>Shares are R&amp;D divided by PAT, computed here and checked against the printed percentages. The illustrative floor in the fourth section lifts the two PSUs below the seven-PSU combined share to that share; it is a computation, not a proposal in the report.</li>
<li>Seven PSUs have PAT in the report; BLC, MRPL, NRL and CPCL appear as printed percentages only, so no PAT-based combined share for all 11 is computed.</li>
<li>BLC is Balmer Lawrie, EIL is Engineers India, MRPL is Mangalore Refinery and Petrochemicals, NRL is Numaligarh Refinery, CPCL is Chennai Petroleum, OIL is Oil India.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>Profit before tax for any PSU: the report gives only profit after tax, and company annual reports were not reachable from the research environment, so the committee&rsquo;s own benchmark base cannot be computed here.</li>
<li>Profit for FY2021-22 to FY2024-25: the report gives profit for FY2025-26 only, so the share of profit over time is not shown, and whether FY2025-26 profit figures are final or provisional is not stated.</li>
<li>What the R&amp;D spend includes: no definition is given, and it is not stated whether capital spending on campuses or grants such as MRPL&rsquo;s Rs 6.7 crore from the Oil Industry Development Board are counted.</li>
<li>Why IOCL and GAIL spent less in FY2025-26 than in FY2024-25: the report does not say.</li>
<li>Source conflicts, not resolved: Observation 1 prints Rs 2,098.95 crore for FY2025-26 against Rs 2,908.95 crore in the table (the table matches its column sum); HPCL is printed as 3% against 3.37% from its own figures; the PRS summary says &lsquo;around 2%&rsquo; and a range of 1.3% to 3.8% for the PSUs, while the report prints 2.16% for seven PSUs and 0.58% to 4.17% across all 11.</li>
<li>Comparability of the 1.3% share: the figure is the petroleum sector&rsquo;s share of India&rsquo;s gross R&amp;D spend in 2020-21 (Rs 1,634.45 crore of Rs 1,27,380.96 crore), a different measure and year from the PSU spend table, so the two are not compared.</li>
<li>R&amp;D headcount: the oral evidence of 24 February 2025 gives 1,619 across seven PSUs and also says &lsquo;nearly 2,000&rsquo;; the gap is unexplained, and the GAIL figure of 9 looks low.</li>
<li>Whether the Ministry has acted: no action-taken report was found, and the Ministry told the committee it &lsquo;would explore&rsquo; a norm.</li>
</ul></details>
'''

step(6, "assembling body")
body = STYLE + top + s1 + s2 + s3 + s4 + recs + fixes + method + gaps

SOURCES = (
    'Standing Committee on Petroleum and Natural Gas (Chair: Sunil Tatkare), '
    '<a href="https://sansad.in/getFile/app/lsscommittee/Petroleum%20&amp;%20Natural%20Gas/18_Petroleum_And_Natural_Gas_9.pdf?source=app">Ninth Report, Examination of R&amp;D activities of Oil PSUs</a>, presented to Lok Sabha and laid in Rajya Sabha on 12 August 2026 (primary; Ministry replies and committee text); '
    '<a href="https://prsindia.org/policy/report-summaries/examination-of-r-d-activities-of-oil-psus">PRS Legislative Research summary</a> (secondary). '
    'Shares, changes and the illustrative floor computed by this blog. Analysed 25 November 2026.')
RELATED = []

step(7, "writing page")
build("Policy &middot; Energy", TITLE,
      "A parliamentary committee asked on 12 August 2026 for a minimum R&amp;D spend by oil PSUs, set as a share of profit before tax; this piece sets out the spend, profit and start-up figures in the report itself and what they show.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in html.lower().replace("accordion.js", ""), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
step(8, "complete")
