"""India's 14 PLI schemes at March 2026: NITI Aayog impact assessment (published 12 Nov 2026).
Build from the repo root:  python3 out/research/pli-2026/build.py   (writes out/post-india-pli-schemes-scorecard-march-2026.html)
Figures are from NITI Aayog's report (niti.gov.in, Impact-Assessment-of-PLI-Schemes.pdf) unless a source is named. Analysed 18 November 2026."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-pli-schemes-scorecard-march-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- Aggregate, March 2026 (Rs crore) ----
INV, PROD, JOBS, PAID, OUTLAY = 240138, 2266412, 849069, 35354, 191049
INV_T, PROD_T, JOBS_T = 315000, 3537000, 3019000          # full-tenure targets (Drishti/ET: Rs 3.15 lakh crore, Rs 35.37 lakh crore, 30.19 lakh jobs)
assert round(100 * PAID / OUTLAY, 2) == 18.51
assert round(100 * INV / INV_T) == 76 and round(100 * PROD / PROD_T) == 64 and round(100 * JOBS / JOBS_T) == 28
ELAPSED = 100 * 578 / 996                                     # months completed of 996 (BusinessLine, 13 Nov)
assert round(ELAPSED) == 58
assert INV > OUTLAY                                           # firms have put in more than the government's total outlay

# ---- Incentive paid by scheme, Rs crore and % of scheme outlay (NITI Table) ----
SECT = [("Drones and drone components", 93, 77.50), ("Large-scale electronics", 19091, 55.83), ("Pharmaceutical drugs", 6659, 44.39),
        ("Food products", 2714, 24.89), ("Telecom and networking", 2756, 22.59), ("Automobiles and components", 2386, 9.20),
        ("White goods", 580, 9.29), ("Medical devices", 267, 7.79), ("Speciality steel", 236, 3.73), ("Technical textiles and MMF", 386, 3.61),
        ("Bulk drugs", 88, 1.27), ("IT hardware 2.0", 98, 0.57), ("ACC batteries", 0, 0.0), ("Solar PV modules", 0, 0.0)]
assert sum(a for _, a, _ in SECT) == PAID
OUTLAYS = {"Pharmaceutical drugs": 15000, "IT hardware 2.0": 17000, "Telecom and networking": 12195, "Automobiles and components": 25938, "ACC batteries": 18100,
           "Drones and drone components": 120, "Technical textiles and MMF": 10683, "White goods": 6238, "Solar PV modules": 24000, "Food products": 10900, "Speciality steel": 6322}
assert sum(OUTLAYS.values()) == 146496 and OUTLAY - sum(OUTLAYS.values()) == 44553
for k, v in OUTLAYS.items():
    paid = dict((n, a) for n, a, _ in SECT)[k]; pct = dict((n, p) for n, _, p in SECT)[k]
    assert abs(100 * paid / v - pct) < 0.1, (k, 100 * paid / v, pct)

# ---- Annual jobs achievement against annual targets (ET, 13 Nov) and incentive paid against plan (BusinessLine, 13 Nov) ----
JOBS_YR = [("Up to FY23", 86), ("FY24", 85), ("FY25", 156), ("FY26", 31)]
FY26_PAID, FY26_PLAN = 15519, 15472
assert FY26_PAID > FY26_PLAN and round(100 * FY26_PAID / FY26_PLAN) == 100

# ---- Slow schemes (NDTV Profit, secondary) ----
ACC_TARGET, ACC_BUILT = 50, 1.4
SOLAR_BEFORE, SOLAR_NOW = 8, 116
assert round(100 * ACC_BUILT / ACC_TARGET, 1) == 2.8 and round(SOLAR_NOW / SOLAR_BEFORE, 1) == 14.5
# Autos (Indian Express 15 Nov, Dataful 18 Nov): investment 44,326 vs 42,500 projected; incremental sales 52,414 vs 231,500; jobs 67,820 vs 148,147
assert round(100 * 52414 / 231500) == 23 and round(100 * 67820 / 148147) == 46

TITLE = "India's PLI schemes: Rs 35,354 crore paid, 18.5% of outlay, jobs at 28% of target"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    ("Rs 35,354 crore", " of the Rs 1.91 lakh crore PLI outlay, 18.5%, had been paid by March 2026, with 58% of the combined scheme period gone; the report says payouts follow production."),
    ("76% and 64%", " of the investment and production targets were met, against 28% of the jobs target: 8.49 lakh jobs of 30.19 lakh."),
    ("Rs 0", " had been paid under the battery and solar module schemes; the battery scheme had built 1.4 GWh of a 50 GWh target and no commercial production."),
])

s1 = insight(
    "Investment is at 76% of target and production 64%, but jobs are at 28% and payouts 18.5%",
    bars("Firms have invested more than the government's whole outlay; jobs and payouts lag",
         [("Investment against full-tenure target", round(100 * INV / INV_T)), ("Production against full-tenure target", round(100 * PROD / PROD_T)),
          ("Share of scheme period elapsed", round(ELAPSED)), ("Jobs against full-tenure target", round(100 * JOBS / JOBS_T)), ("Incentive paid against outlay", 18.51)],
         accent="Jobs against full-tenure target", unit="%", sub="Cumulative to March 2026; 14 schemes. Investment Rs 2.40 lakh crore, production Rs 22.66 lakh crore, 8.49 lakh jobs.",
         source="NITI Aayog, Impact Assessment of PLI Schemes, 12 November 2026; The Hindu BusinessLine, 13 November 2026.")
    + numbers(["Measure", "Achieved", "Full-tenure target"],
              [["Investment", "Rs 2,40,138 crore", "Rs 3.15 lakh crore"], ["Production and sales", "Rs 22,66,412 crore", "Rs 35.37 lakh crore"],
               ["Employment", "8,49,069", "30.19 lakh"], ["Incentive paid", "Rs 35,354 crore", "Outlay Rs 1,91,049 crore"],
               ["Scheme period", "578 of 996 combined months", "58% elapsed"]]),
    "Investment of Rs 2.40 lakh crore already exceeds the Rs 1.91 lakh crore outlay, which fits the report&rsquo;s point that PLI pays only after firms invest and sell above a baseline, so a low payout share does not by itself mean weak uptake.",
    "NITI Aayog should publish scheme-wise payout against the plan for each year with the reason for each gap, so that the 18.5% can be read against what was due.",
    "scorecard")

s2 = insight(
    "Drones and electronics have been paid 78% and 56% of outlay; batteries and solar nothing",
    bars("Share of each scheme's outlay paid by March 2026 runs from 78% to zero",
         [(n, p, f"Rs {a:,} crore") for n, a, p in SECT], accent="Large-scale electronics", unit="%",
         sub="Incentive paid as a percentage of the scheme outlay. The 14 schemes' outlays total Rs 1,91,049 crore.",
         source="NITI Aayog, Impact Assessment of PLI Schemes, Table of disbursement till March 2026.")
    + numbers(["Scheme", "Outlay, Rs crore", "Paid, Rs crore", "Paid, %"],
              [[n, f"{OUTLAYS[n]:,}" if n in OUTLAYS else "see report", f"{a:,}", f"{p:.2f}"] for n, a, p in SECT]),
    "Large-scale electronics alone accounts for Rs 19,091 crore of the Rs 35,354 crore paid, which is 54% of all money paid, so the portfolio average hides one scheme doing most of the work.",
    "The report should state, for each scheme below 10% paid, the date by which the first payout is expected, since two schemes were still at nil in March 2026.",
    "sectors")

s3 = insight(
    "Annual jobs achievement fell from 156% of target in FY25 to 31% in FY26",
    bars("Employment ran above its annual target in FY25 and fell to 31% of it in FY26",
         JOBS_YR, accent="FY26", unit="%", ref=(100, "annual target"),
         sub="Employment generated as a percentage of the annual employment target, all 14 schemes.",
         source="Economic Times, 13 November 2026, reporting NITI Aayog's assessment.")
    + numbers(["Scheme", "Jobs by March 2026", "Note"],
              [["Food products", "3.29 lakh", "Indian Express, 15 November"], ["Large-scale electronics", "1.69 lakh", "Dataful, 18 November"],
               ["Pharmaceutical drugs", "1.15 lakh", "Dataful, 18 November"],
               ["Automobiles and components", "67,820", "Against 1,48,147 projected: 46%"],
               ["White goods", "52,703", "Indian Express"], ["Telecom and networking", "33,610", "Indian Express"],
               ["Textiles", "33,427", "Indian Express"], ["Every other scheme", "under 15,000 each", "Indian Express"]]),
    "The cumulative 28% of the jobs target conceals a yearly swing, and the report itself warns that a low cumulative figure during implementation cannot be read as failure to reach the final target.",
    "NITI Aayog should publish jobs by scheme and by year with the definition of a PLI job, so that the swing between FY25 and FY26 can be traced to specific schemes.",
    "jobs")

s4 = insight(
    "Solar module capacity grew from 8 GW to 116 GW, while batteries built 1.4 of 50 GWh",
    bars("Two schemes without payouts: modules reached 116 GW, batteries only 1.4 GWh of 50",
         [("Solar modules before the scheme, GW", SOLAR_BEFORE), ("Solar modules now, GW", SOLAR_NOW), ("Battery target, GWh", ACC_TARGET), ("Battery capacity built, GWh", ACC_BUILT)],
         accent="Battery capacity built, GWh", unit="", fmt=lambda v: f"{v:g}",
         sub="Capacity in GW (modules) or GWh (batteries). The modules scheme is in its gestation period; the battery scheme has not begun commercial production.",
         source="NDTV Profit, 12 November 2026, reporting the NITI Aayog assessment (secondary; the report PDF was read only in part).")
    + numbers(["Scheme", "Measure", "Value"],
              [["Solar modules", "Domestic manufacturing capacity", "8 GW to nearly 116 GW; 21% of capacity creation attributed to the scheme (Drishti)"],
               ["ACC batteries", "Capacity built against target", "1.4 GWh against 50 GWh; no incentive paid"],
               ["White goods", "Domestic value addition", "20% to 55%; compressor capacity 1 million to 10 million units (NDTV Profit, Drishti)"],
               ["Automobiles", "Incremental sales against projection", "Rs 52,414 crore against Rs 2,31,500 crore (23%)"]]),
    "Capacity can be built well ahead of payouts, as in solar modules, while the battery scheme shows the opposite case of capacity that is mostly unbuilt after technology gaps, imported machinery and project delays.",
    "The ministries running the battery and solar schemes should publish a project-wise table of capacity commissioned against capacity committed, so that the 116 GW and the 1.4 GWh can be matched to named plants.",
    "capacity")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>NITI Aayog and the implementing ministries:</b> publish payout against plan by scheme and year, with the reason for each gap.</li>
<li><b>Ministry of Heavy Industries and the Ministry of New and Renewable Energy:</b> publish capacity committed and commissioned by named plant for the battery and solar module schemes.</li>
<li><b>NITI Aayog:</b> define a PLI job and publish employment by scheme and year, so the FY25 and FY26 swing can be explained.</li>
<li><b>Department of Expenditure:</b> report the sunset date of each scheme next to its unspent outlay.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''
method = '''<details class="xv-n"><summary>Method and definitions</summary><ul>
<li>PLI pays a firm only after it invests and sells above a baseline, so payout share trails investment and production by design.</li>
<li>&ldquo;Share of scheme period elapsed&rdquo; is 578 of the 996 combined months in the 14 schemes, as reported.</li>
<li>Jobs, investment and production are as reported by participating firms to the implementing ministries; NITI Aayog and IIM Ahmedabad assessed them.</li>
<li>Full-tenure targets (Rs 3.15 lakh crore, Rs 35.37 lakh crore, 30.19 lakh jobs) are from press reports of the assessment; the percentages were recomputed here.</li></ul></details>
'''
gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary><ul>
<li>Outlays of the three schemes at the top of the report&rsquo;s table (large-scale electronics, bulk drugs, medical devices): the extract read does not print them; their combined outlay is Rs 44,553 crore by subtraction.</li>
<li>Whether the reported jobs are additional to what industry would have created anyway; the report says additionality is visible in several sectors, not all.</li>
<li>Export figures by scheme, which the assessment covers but this piece does not.</li>
<li>Battery and module capacity numbers come from a news report on the assessment, not from the PDF.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps
SOURCES = ('<a href="https://www.niti.gov.in/sites/default/files/2026-11/Impact-Assessment-of-PLI-Schemes.pdf">NITI Aayog, Impact Assessment of PLI Schemes, November 2026</a>; '
  '<a href="http://www.thehindubusinessline.com/news/national/pli-schemes-disburse-185-of-191-lakh-crore-outlay-by-march-2026-niti-aayog-report/article71694448.ece">The Hindu BusinessLine, 13 November 2026</a> (payout against plan; months elapsed); '
  '<a href="https://m.economictimes.com/news/economy/policy/pli-schemes-achieve-76-of-investment-target-64-of-production-goal-niti-aayog/amp_articleshow/135781420.cms">Economic Times, 13 November 2026</a> (annual jobs achievement); '
  '<a href="http://indianexpress.com/article/explained/explained-economics/pli-schemes-india-employment-generation-jobs-10963325">Indian Express, 15 November 2026</a> (jobs by scheme); '
  '<a href="https://insights.dataful.in/articles/investment-outpaces-jobs-a-mid-course-assessment-of-indias-pli-schemes">Dataful, 18 November 2026</a>; '
  '<a href="https://www.ndtvprofit.com/india/indias-pli-schemes-get-a-report-card-which-sectors-passed-and-which-didnt-12317420">NDTV Profit, 12 November 2026</a> (secondary); '
  '<a href="https://www.drishtiias.com/daily-updates/daily-news-analysis/niti-aayog-report-on-impact-assessment-of-pli-schemes">Drishti IAS, 13 November 2026</a>. Shares computed by this blog. Analysed 18 November 2026.')
RELATED = [(f"{B}/2026/08/pli-medical-devices-coverage-and-gaps.html", "PLI for medical devices: 28 projects, no new application rounds before March 2027"),
           (f"{B}/2026/08/indias-mobile-phone-pli-beat-every.html", "India's electronics schemes: phone PLI beat targets, 5 of 12 chip plants produce"),
           (f"{B}/2026/10/the-phone-plis-successor-pays-up-to-5.html", "Smartphone PLI successor: up to 5% above 15% yearly growth, 0.20% for battery cells"),
           (f"{B}/2026/10/indias-approved-solar-cell-makers-can.html", "India's approved solar-cell list: 37.8 GW a year, rooftop exemption ends 31 December")]
build("Industry &middot; Policy", TITLE, "NITI Aayog's mid-course review shows Rs 35,354 crore paid of Rs 1.91 lakh crore, investment at 76% of target and jobs at 28%, with the battery and solar schemes still unpaid.", body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE))
