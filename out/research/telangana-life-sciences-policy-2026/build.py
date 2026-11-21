"""Telangana Next-Gen Life Sciences Policy 2026-30: approval date, incentives, baseline, and what the stated targets imply.
Build from the repo root:  python3 out/research/telangana-life-sciences-policy-2026/build.py   (writes out/post-telangana-life-sciences-policy-2026-30.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 21 November 2026.
Targets (stated goals) are kept apart from reported outcomes; growth rates, ratios and rupee conversions are computed here and labelled so.
Sources read in full: the policy text (Invest Telangana page, sections 6.5 and 7), search excerpts of the others; the post says which."""
import datetime as dt
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-telangana-life-sciences-policy-2026-30.html"
STEPS = 8


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


# ---- 1. dates
step(1, "dates and weekday checks")
D_UNVEIL, D_CABINET, D_TLSF = dt.date(2026, 1, 21), dt.date(2026, 5, 23), dt.date(2026, 5, 14)
assert D_UNVEIL.strftime("%A") == "Wednesday" and D_CABINET.strftime("%A") == "Saturday"   # reports say 'on Saturday' (BusinessLine, PTI, Deccan Chronicle)
GAP_DAYS = (D_CABINET - D_UNVEIL).days
assert GAP_DAYS == 122
assert D_TLSF.strftime("%A") == "Thursday"      # TNIE of 15 May: board meeting 'on Thursday'

# ---- 2. stated targets (policy; reports of 21-22 Jan and 23-24 May 2026) and what they imply
step(2, "target arithmetic")
INV_USD_BN, JOBS, YEARS = 25, 500_000, 5          # 'over the next five years' (Deccan Chronicle, PTI, All India Radio); policy period 2026-2030
assert INV_USD_BN / YEARS == 5.0 and JOBS / YEARS == 100_000
JOBS_PER_BN = JOBS / INV_USD_BN
USD_PER_JOB = INV_USD_BN * 1e9 / JOBS
assert JOBS_PER_BN == 20_000 and USD_PER_JOB == 50_000
# the policy's own rupee-dollar pair: overall exports INR 1.2 lakh crore = USD 14.4 billion; life sciences INR 36,893 crore = USD 4.43 billion
RATE_CR_PER_BN = 120_000 / 14.4
assert round(RATE_CR_PER_BN, 1) == 8333.3
assert abs(36_893 / 4.43 - RATE_CR_PER_BN) / RATE_CR_PER_BN < 0.002          # the two pairs in the policy agree to 0.2%
INV_INR_CR = INV_USD_BN * RATE_CR_PER_BN
assert round(INV_INR_CR) == 208_333
# reported investment pace (rupees converted at the policy's own pair; 'investments' is not defined in either source)
PACE_2Y = 84_000 / 2 / RATE_CR_PER_BN            # TNIE 15 May 2026: Rs 84,000 crore 'over the past two years'
PACE_20M = 63_000 / 20 * 12 / RATE_CR_PER_BN     # IT department 23 Oct 2025: Rs 63,000 crore in the past 20 months
assert f"{PACE_2Y:.2f}" == "5.04" and f"{PACE_20M:.2f}" == "4.54"
assert round(100 * (PACE_2Y - 5.0) / 5.0, 1) == 0.8
# life sciences economy: USD 80 billion (minister, Oct 2025; TLSF page) and USD 145 billion (TNIE, 15 May 2026); vision of USD 250 billion by 2030
ECON_LO, ECON_HI, ECON_TGT = 80, 145, 250
M_LO, M_HI = ECON_TGT / ECON_LO, ECON_TGT / ECON_HI
assert f"{M_LO:.2f}" == "3.12" and f"{M_HI:.2f}" == "1.72"
G_LO = (M_LO) ** (1 / 5) - 1       # from Oct 2025, five years to 2030
G_HI = (M_HI) ** (1 / 4) - 1       # from May 2026, four years to 2030
G_PAST = 3 ** (1 / 10) - 1         # 'nearly tripled since 2016' (TNIE): exactly tripled over ten years is the upper bound of the stated change
assert f"{100 * G_LO:.1f}" == "25.6" and f"{100 * G_HI:.1f}" == "14.6" and f"{100 * G_PAST:.1f}" == "11.6"
assert G_PAST < G_HI < G_LO
# jobs against the reported employment base (Invest Telangana sector page, undated: 200,000+ professionals)
EMP_BASE = 200_000
JOBS_MULT = JOBS / EMP_BASE
assert JOBS_MULT == 2.5

# ---- 3. baseline (policy text, FY2023-24) and its internal consistency check
step(3, "baseline figures and consistency checks")
EXP_LS_CR, EXP_ALL_CR, EXP_LS_USD, EXP_ALL_USD, SHARE_STATED = 36_893, 120_000, 4.43, 14.4, 32
SHARE_CR, SHARE_USD = 100 * EXP_LS_CR / EXP_ALL_CR, 100 * EXP_LS_USD / EXP_ALL_USD
assert f"{SHARE_CR:.1f}" == "30.7" and f"{SHARE_USD:.1f}" == "30.8"
assert SHARE_STATED - SHARE_CR > 1.2                 # stated 32% is 1.3 points above both computed shares: flagged, not corrected
IMPLIED_TOTAL_CR = EXP_LS_CR / (SHARE_STATED / 100)
assert round(IMPLIED_TOTAL_CR) == 115_291
GV_ACRES, GV_EXPAND = 1000, 300                      # Invest Telangana: 'about 1,000 acres'; policy: 'another 300 acres'
assert 100 * GV_EXPAND / GV_ACRES == 30
MD_JOBS, MD_COMP, MD_ACRES = 7_000, 60, 302         # Medical Devices Park, policy text
assert round(MD_JOBS / MD_COMP) == 117

# ---- 4. incentives (policy section 7): large-unit investment subsidy caps and the plant spend at which each cap binds
step(4, "incentive caps")
CAPS = [("Pharma Villages: 15% of plant and machinery", 15, 20), ("Advanced manufacturing: 25% of plant and machinery", 25, 20),
        ("Advanced manufacturing beyond the Regional Ring Road: 30%", 30, 30)]
BIND = {n: cap / (pct / 100) for n, pct, cap in CAPS}
assert [round(v, 1) for v in BIND.values()] == [133.3, 80.0, 100.0]
MEGA_CR, MEGA_JOBS = 200, 1000                       # T-IDEA mega project: fixed capital investment of at least Rs 200 crore or more than 1,000 jobs
assert BIND["Advanced manufacturing: 25% of plant and machinery"] < BIND["Advanced manufacturing beyond the Regional Ring Road: 30%"] < MEGA_CR

TITLE = "Telangana Life Sciences Policy 2026-30: targets of USD 25 billion and 500,000 jobs"
assert 55 <= len(TITLE) <= 90, len(TITLE)
assert not any(w in TITLE.lower().split() for w in ("you", "your", "we", "our"))

step(5, "writing sections")
top = top_line([
    ("23 May 2026", f", a Saturday, is the date reports give for cabinet approval of the Next-Gen Life Sciences Policy 2026-30, {GAP_DAYS} days after its unveiling at Davos on 21 January; the USD 25 billion and 500,000 jobs are stated targets, and no result against them was found."),
    (f"{JOBS_PER_BN:,.0f} jobs", f" for each USD 1 billion is what the two targets imply together (computed), or USD {USD_PER_JOB:,.0f} of investment for each new job."),
    (f"{100 * G_HI:.1f}% to {100 * G_LO:.1f}%", f" a year is the growth a separate target of a USD {ECON_TGT} billion life sciences economy by 2030 implies, depending on whether the base is USD {ECON_HI} billion (May 2026 report) or USD {ECON_LO} billion (October 2025 statement)."),
])

tvo = ('<table class="gb-table"><thead><tr><th>Kind</th><th>What this piece includes</th></tr></thead><tbody>'
       '<tr><td><b>Target</b></td><td>USD 25 billion of investment, 500,000 new jobs, a top-five hub by 2030 (the policy text says top three), a USD 250 billion sector.</td></tr>'
       '<tr><td><b>Reported outcome</b></td><td>Rs 84,000 crore of investment over two years and a USD 145 billion sector, as stated by officials in 2025-26 and not checked here.</td></tr>'
       '<tr><td><b>Computed here</b></td><td>Growth rates, jobs per USD billion, shares and rupee conversions, each marked as computed.</td></tr>'
       '</tbody></table>\n')

s1 = insight(
    f"Cabinet approved the policy on 23 May 2026, {GAP_DAYS} days after the Davos unveiling",
    flow([("21 Jan 2026 (Wednesday)", "Chief Minister A. Revanth Reddy unveils the Next-Gen Life Sciences Policy 2026-30 at the World Economic Forum meeting in Davos; the state press release says the aim is a top-three global cluster by 2030, while The Hindu and The New Indian Express say top five."),
          ("14 May 2026 (reported 15 May)", "Telangana Life Sciences Foundation board meeting; officials put the sector at USD 145 billion and investments at more than Rs 84,000 crore over two years (as reported)."),
          ("23 May 2026 (Saturday)", "State cabinet approves the policy, with R&D units recognised as industries; briefing by Minister Ponguleti Srinivas Reddy; the stated aim is one of the top five life sciences hubs by 2030.", True),
          ("2026 to 2030", "Policy period. Targets: USD 25 billion of investment and 500,000 new jobs, over five years as reported.")])
    + numbers(["Item", "Statement", "Source and status"],
              [["Approval date", "Saturday 23 May 2026", "BusinessLine, 23 May; Deccan Chronicle, 24 May; PTI via EdexLive, 24 May (all secondary)"],
               ["Unveiling", "Wednesday 21 January 2026, Davos", "Telangana state press release, 21 January (official); The Hindu, 21 January (secondary)"],
               ["Hub ranking aim", "Top three (state press release and policy text) or top five (reports of 22 January, 23 and 24 May)", "Conflict: not resolved here"],
               ["Nodal agency", "Telangana Life Sciences Foundation; overseen by the Industries and Commerce and the IT departments", "State press release, 21 January"],
               ["Days between", f"{GAP_DAYS}", "Computed here"]],
              "Show the dates and the conflict on the ranking aim"),
    "The policy was announced in January and approved in May, so incentives in the text apply to investments made after the launch, and the date that launch counts from is not stated in the sources read.",
    "The Industries and Commerce Department should state the date from which investments qualify, since the policy text says only that investments made after the policy launch are eligible.",
    "approval")

s2 = insight(
    "Reported investment pace of about USD 5 billion a year matches the target pace",
    bars("Reported investment pace is close to the USD 5 billion a year the target implies",
         [("Target: USD 25 billion over five years (stated goal)", 5.0),
          ("Reported: Rs 84,000 crore over two years, to May 2026", round(PACE_2Y, 2)),
          ("Reported: Rs 63,000 crore in 20 months, to October 2025", round(PACE_20M, 2))],
         accent="Reported: Rs 84,000 crore over two years, to May 2026", vmax=6, fmt=lambda v: f"USD {v:.2f} billion",
         sub="USD billion a year. Rupees converted at Rs 8,333 crore per USD billion, the rate implied by the policy&rsquo;s own export figures (computed). Neither source defines &lsquo;investments&rsquo;, so announcements and realised spending cannot be separated.",
         source="New Indian Express, 15 May 2026 (secondary, reporting the Telangana Life Sciences Foundation board); Telangana IT department, 23 October 2025 (official); policy text.")
    + numbers(["Item", "Value", "Basis"],
              [["Target per year", f"USD {INV_USD_BN / YEARS:.1f} billion and {JOBS // YEARS:,} jobs", "USD 25 billion and 500,000 jobs over five years (computed)"],
               ["Target in rupees", f"About Rs {INV_INR_CR / 1e5:.2f} lakh crore", "At the policy&rsquo;s own rate (computed)"],
               ["Jobs per USD 1 billion", f"{JOBS_PER_BN:,.0f}", "500,000 / 25 (computed)"],
               ["Investment per new job", f"USD {USD_PER_JOB:,.0f}", "Computed"],
               ["Investments reported, two years", "More than Rs 84,000 crore", "TNIE, 15 May 2026"],
               ["Investments reported, 20 months", "Rs 63,000 crore from life sciences, of Rs 3.2 lakh crore across all sectors", "IT department, 23 October 2025"],
               ["Investments reported, two years (other page)", "Over Rs 80,000 crore", "Invest Telangana pharma page, undated"],
               ["Green Pharma City MoUs", "Nearly Rs 20,000 crore signed; minister asked for them to be grounded", "TNIE, 15 May 2026"]],
              "Show the numbers behind the investment pace"),
    f"If the reported investment is counted in full, the recent pace is already {100 * (PACE_2Y - 5.0) / 5.0:.1f}% above the target pace of USD 5 billion a year, which suggests the target counts something narrower or that most of the reported sum is announced rather than spent.",
    "The Telangana Life Sciences Foundation should publish yearly figures for investments grounded, separate from MoUs signed, so that progress against USD 25 billion can be read directly.",
    "pace")

s3 = insight(
    f"The USD 250 billion sector target implies {100 * G_HI:.1f}% to {100 * G_LO:.1f}% a year, depending on the base",
    bars(f"USD 250 billion by 2030 needs {100 * G_HI:.1f}% a year from USD 145 billion, {100 * G_LO:.1f}% from USD 80 billion",
         [("From USD 80 billion (October 2025 statement), five years", round(100 * G_LO, 1)),
          ("From USD 145 billion (May 2026 report), four years", round(100 * G_HI, 1)),
          ("Past decade, if exactly tripled since 2016, ten years", round(100 * G_PAST, 1))],
         accent="From USD 145 billion (May 2026 report), four years", unit="%", vmax=30,
         sub=f"Compound yearly growth in dollar value, computed here. Multiples of the base: {M_LO:.2f} times USD 80 billion and {M_HI:.2f} times USD 145 billion. The report says the sector &lsquo;nearly tripled&rsquo; since 2016, so the third bar is an upper bound on that change.",
         source="Minister D. Sridhar Babu, 23 October 2025 (Telangana IT department); New Indian Express, 15 May 2026; Invest Telangana pharma page (USD 250 billion by 2030); growth computed here.")
    + numbers(["Item", "Value", "Source and status"],
              [["Sector value, October 2025", "USD 80 billion (target USD 250 billion by 2030)", "Telangana IT department release (official)"],
               ["Sector value, May 2026", "USD 145 billion", "New Indian Express, TLSF board meeting (secondary)"],
               ["Gap between the two values", "USD 65 billion in about seven months; definitions not given", "Computed; the sources do not reconcile it"],
               ["New jobs target against reported employment", f"500,000 against 200,000+ professionals, {JOBS_MULT:.1f} times at most", "Invest Telangana sector page, undated (official); computed"],
               ["Life sciences exports, FY2023-24", f"Rs {EXP_LS_CR:,} crore (USD {EXP_LS_USD} billion)", "Policy text (official)"],
               ["Share of state exports, FY2023-24", f"Stated 32%; computed {SHARE_CR:.1f}% from Rs {EXP_LS_CR:,} crore of Rs {EXP_ALL_CR:,} crore and {SHARE_USD:.1f}% in dollars", "Policy text; the stated share is 1.3 points above the computed ones"],
               ["Exports, April to December 2024", "More than Rs 26,000 crore", "Telangana IT department, 23 October 2025"],
               ["Genome Valley organisations", "250+ (policy), 200+ (Invest Telangana, TLSF), around 500 (TLSF cluster page)", "Three official counts for one cluster"],
               ["Genome Valley workforce", "15,000+ (Invest Telangana), 18,000 (TLSF cluster page), 20,000 (TLSF Genome Valley page)", "Three official counts, undated"],
               ["Genome Valley expansion", f"Another {GV_EXPAND} acres on about {GV_ACRES:,} acres, {100 * GV_EXPAND / GV_ACRES:.0f}% more", "Policy text; Invest Telangana (computed)"],
               ["Medical Devices Park", f"{MD_ACRES} acres, about {MD_COMP} companies, over {MD_JOBS:,} jobs", "Policy text"],
               ["Companies and FDA sites", "2,000+ life sciences companies; 250+ USFDA-approved sites (269 on another page)", "Policy text; Invest Telangana"]],
              "Show the baseline and the conflicts between sources"),
    f"The state quotes two sector values seven months apart, so the target is {M_LO:.1f} times one and {M_HI:.1f} times the other, and a jobs target of 500,000 is at most {JOBS_MULT:.1f} times the 200,000 professionals the state counts today.",
    "The Planning Department should publish one dated definition of the life sciences economy, with the base year and the value, so every target can be measured against the same figure.",
    "baseline")

s4 = insight(
    "Advanced manufacturing subsidy caps: Rs 20 crore, or Rs 30 crore beyond the Ring Road",
    bars("Large-unit capital subsidy is capped at Rs 20 crore, or Rs 30 crore beyond the Ring Road",
         [(n, cap) for n, pct, cap in CAPS], accent="Advanced manufacturing beyond the Regional Ring Road: 30%", unit=" crore",
         fmt=lambda v: f"Rs {v:g} crore", vmax=35,
         sub="Maximum investment subsidy for large units, Rs crore, on plant and machinery (land and building excluded). The cap binds at plant spending of Rs 80 crore, Rs 100 crore and Rs 133.3 crore respectively (computed). A mega project is defined in the T-IDEA policy as Rs 200 crore of fixed capital or more than 1,000 jobs.",
         source="Telangana Next-Gen Life Sciences Policy 2026-2030, section 7.3 (official policy text).")
    + numbers(["Incentive", "Entitlement in the policy text", "Applies to"],
              [["Registration", "100% reimbursement of stamp duty and transfer duty", "Life sciences units, common list"],
               ["Power, general", "Fixed power charges reimbursed at Rs 1.00 a unit for 5 years", "Common list"],
               ["Power, advanced manufacturing", "Rs 2.00 a unit for 5 years", "Advanced manufacturing"],
               ["Net SGST", "100% for 5 years (micro and small), 75% for 7 years (medium), 50% for 7 years (large), up to 100% of eligible fixed capital", "Common list, as under T-IDEA"],
               ["Capital subsidy, micro and small", "25% up to Rs 30 lakh; extra 20% up to Rs 20 lakh for women-owned", "Common list"],
               ["Capital subsidy, advanced manufacturing", "25% of plant and machinery up to Rs 20 crore (large); 50% up to Rs 10 crore (MSME)", "Advanced manufacturing"],
               ["Beyond the Regional Ring Road", "30% up to Rs 30 crore (large); 50% up to Rs 20 crore (MSME)", "Advanced manufacturing"],
               ["Pharma Villages", "15% up to Rs 20 crore (large); 25% up to Rs 5 crore (MSME); five anchor investors of more than Rs 500 crore each in three years", "Pharma Villages"],
               ["R&D units", "Treated as industrial units under clause 6 of T-IDEA, so the common list applies; no separate rupee rate for R&D was found in the text read", "Pharmaceutical R&D"],
               ["Innovation fund", "Rs 100 crore at the start, scalable to Rs 1,000 crore, public-private structure, co-investing with venture and private equity funds", "Startups and translational research"],
               ["Employment", "Rs 2,000 for each domiciled employee&rsquo;s EPF contribution, up to 500 employees, twice in the policy term", "Common list"],
               ["Talent", "India Reimagined Fellowship of up to USD 300,000 over three years is a national programme the state will work with", "Researchers relocating to India"]],
              "Show the incentive list"),
    "The policy&rsquo;s own text treats pharmaceutical R&D as an industrial unit under T-IDEA, so R&D draws on the common list and the larger caps apply to advanced manufacturing, not to R&D as such.",
    "The Industries and Commerce Department should publish an expected fiscal cost for the incentive list at the USD 25 billion target, since none was found in the sources read.",
    "incentives")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Telangana Industries and Commerce Department:</b> state the date from which investments qualify under the policy and publish the expected fiscal cost of the incentive list at the USD 25 billion target.</li>
<li><b>Telangana Life Sciences Foundation:</b> publish yearly investments grounded and jobs created against the two targets, separate from MoUs signed, with a stated definition of each.</li>
<li><b>Telangana Planning Department:</b> publish one dated definition of the life sciences economy, with base year and value, to replace the USD 80 billion and USD 145 billion figures.</li>
<li><b>Telangana Information Technology and Industries departments:</b> state whether the aim is a top-three or a top-five global cluster, and name the ranking used to measure it.</li>
<li><b>Telangana Life Sciences Foundation:</b> reconcile the three Genome Valley company counts and workforce counts on the state portals into one dated figure.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Implied growth is (target / base) raised to 1 over the years, in dollars. The five years run from October 2025 for the USD 80 billion base and the four years from May 2026 for the USD 145 billion base; both are assumptions, as the sources do not state the base year of each value.</li>
<li>Rupee figures are converted at Rs 8,333 crore per USD billion, which is the rate in the policy&rsquo;s own pair (Rs 1.2 lakh crore equals USD 14.4 billion); its second pair (Rs 36,893 crore equals USD 4.43 billion) gives a rate within 0.2% of it.</li>
<li>The state press release and the policy text were read in full; the policy text was read through its Invest Telangana page, sections 6.5 and 7. News reports were read as search excerpts only and are labelled secondary.</li>
<li>Target means a goal stated by the state. Outcome means a figure the state or a report gives as already achieved. Neither has been audited here.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>Whether the target is a top-three or a top-five cluster: the state press release of 21 January and the policy text say top three, while The Hindu, The New Indian Express and the reports of the 23 May cabinet decision say top five. No ranking method was found.</li>
<li>The cabinet resolution itself: the approval date rests on three news reports (BusinessLine, Deccan Chronicle, PTI), and no cabinet note or government order was read.</li>
<li>What counts as investment and a job: no source defines whether the Rs 84,000 crore, Rs 63,000 crore or Rs 80,000 crore figures are realised spending or announced commitments, or whether the 500,000 jobs are direct or indirect.</li>
<li>The base year and definition of the sector value: USD 80 billion (October 2025) and USD 145 billion (May 2026) differ by USD 65 billion in about seven months with no reconciliation, and the USD 250 billion target for 2030 appears on the Invest Telangana pharma page and in the minister&rsquo;s October 2025 speech, not in the policy text excerpts read.</li>
<li>The 32% export share: the policy text states 32%, but its own rupee and dollar figures give 30.7% and 30.8%; the total of Rs 1.2 lakh crore may be rounded, and which figure is right was not established. Exports after FY2023-24 were not found beyond April to December 2024 (more than Rs 26,000 crore, a nine-month figure).</li>
<li>The ranking of Genome Valley: Invest Telangana says it is ranked seventh among global life sciences hubs in CBRE&rsquo;s Global Life Sciences Atlas 2025, but the CBRE profile read does not show a rank.</li>
<li>Genome Valley counts: organisations (200+, 250+, around 500) and workforce (15,000+, 18,000, 20,000) differ across official pages; none is dated.</li>
<li>The incentive terms for R&amp;D units beyond their treatment as industrial units, any fiscal cost estimate, and whether the common-list items reproduce T-IDEA exactly; T-IDEA itself was not read.</li>
<li>Any outcome since 23 May 2026: no post-approval progress report on the policy was found.</li>
</ul></details>
'''

step(6, "assembling body")
body = STYLE + top + tvo + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://invest.telangana.gov.in/wp-content/themes/investtelangana-theme/assets/docs/policies/telangana-life-sciences-policy-2026-2030.pdf">Telangana Next-Gen Life Sciences Policy 2026-2030</a> and '
    '<a href="https://invest.telangana.gov.in/policy-life-sciences">Invest Telangana policy page</a> (official policy text; sections 6.5 and 7 read in full); '
    '<a href="https://www.telangana.gov.in/news/press-releases/2026/01/%E0%B0%A6%E0%B0%BE%E0%B0%B5%E0%B1%8B%E0%B0%B8%E0%B1%8D-%E0%B0%B5%E0%B1%87%E0%B0%A6%E0%B0%BF%E0%B0%95%E0%B0%97%E0%B0%BE-%E0%B0%A4%E0%B1%86%E0%B0%B2%E0%B0%82%E0%B0%97%E0%B0%BE%E0%B0%A3-%E0%B0%AA/">Telangana state press release, 21 January 2026</a> (official); '
    '<a href="https://www.thehindubusinessline.com/economy/policy/telangana-cabinet-clears-new-life-sciences-policy-2026-30/article71015456.ece">BusinessLine, 23 May 2026</a>, '
    '<a href="https://www.deccanchronicle.com/southern-states/telangana/nod-for-nextgen-life-sciences-policy-1958757">Deccan Chronicle, 24 May 2026</a> and '
    '<a href="https://www.edexlive.com/news/telangana-cabinet-approves-mid-day-meal-scheme-in-junior-colleges-2?utm_source=website&amp;utm_medium=related-stories">PTI via EdexLive, 24 May 2026</a> (secondary: cabinet approval); '
    '<a href="https://www.thehindu.com/news/national/telangana/telangana-unveils-next-gen-life-sciences-policy-202630-in-davos-eyes-25-billion-investments-5-lakh-jobs/article70532622.ece">The Hindu, 21 January 2026</a> and '
    '<a href="https://www.newindianexpress.com/states/telangana/2026/Jan/22/telangana-life-sciences-policy-targets-usd-25-billion-investments-5-lakh-jobs">New Indian Express, 22 January 2026</a> (secondary: unveiling); '
    '<a href="https://www.newindianexpress.com/states/telangana/2026/May/15/telangana-life-sciences-ecosystem-reaches-145-billion">New Indian Express, 15 May 2026</a> (secondary: USD 145 billion, Rs 84,000 crore); '
    '<a href="https://it.telangana.gov.in/telangana-targets-%E2%82%B91-lakh-crore-investment-in-life-sciences-by-2030-minister-sridhar-babu/">Telangana IT department, 23 October 2025</a> (official release: USD 80 billion, Rs 63,000 crore, exports); '
    '<a href="https://invest.telangana.gov.in/pharma">Invest Telangana pharma page</a> and '
    '<a href="https://invest.telangana.gov.in/sectors/life-sciences">sector page</a> (official, undated); '
    '<a href="https://lifesciences.telangana.gov.in/genome-valley">TLSF Genome Valley page</a> and '
    '<a href="https://lifesciences.telangana.gov.in/life-sciences-grid/clusters/genome-valley">TLSF cluster page</a> (official, undated); '
    '<a href="https://www.cbre.com/insights/local-response/global-life-sciences-atlas-market-profiles-hyderabad-india">CBRE, Hyderabad market profile, 11 April 2025</a> (secondary); '
    '<a href="https://www.biospectrumindia.com/news/109/27208/telangana-sets-global-ambition-with-life-sciences-policy-202630-targeting-25-b-investments.html">BioSpectrum, 21 January 2026</a> (secondary). '
    'Growth rates, ratios, shares and rupee conversions computed by this blog. Analysed 21 November 2026.')
RELATED = []

step(7, "writing page")
build("Policy &middot; Telangana", TITLE,
      "Telangana&rsquo;s cabinet approved the Life Sciences Policy 2026-30 on 23 May 2026; this piece sets out its incentives, the baseline it starts from, and what its stated targets imply.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
step(8, "complete")
