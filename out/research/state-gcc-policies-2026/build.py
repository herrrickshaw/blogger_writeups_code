"""State GCC (global capability centre) policies compared: targets, incentive ceilings, what the documents say against each other and against a national estimate.
Build from the repo root:  python3 out/research/state-gcc-policies-2026/build.py            (writes out/post-state-gcc-policies-india-2026.html)
                           python3 out/research/state-gcc-policies-2026/build.py --check    (arithmetic and asserts only)
Every figure is from the source named beside it, or computed below with an assert. Analysed 21 November 2026.
Primary documents read as search excerpts: Karnataka GCC Policy 2024-29 and its operational guidelines and incentive pages, Maharashtra GR of 3 Nov 2025 and press note,
Gujarat GCC Policy 2025-30 resolution, MP GCC Policy 2025, Rajasthan GCC Policy 2025 order, UP GCC Policy 2024 pages, rules and press releases, Odisha GCC Policy 2025 gazette,
Karnataka Budget 2026-27. Haryana from a PwC alert on the policy (secondary). Tamil Nadu, Andhra Pradesh and part of Maharashtra from secondary summaries (Scutiger, AIM Research).
The AIM Research comparison page was read in full. No policy was read in full; the post says so."""
import datetime as dt
import html as _h
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
OUT = ROOT / "out/post-state-gcc-policies-india-2026.html"
STEPS = 9


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. dates: policy to operating rules (document listing dates; the file listings, not the policies, give the later date)
step(1, "dates and lags to operating rules")
KA_POL, KA_OPG = D(2024, 12, 3), D(2025, 9, 8)          # G.O. of 3 Dec 2024 notifies the policy; operational guidelines file dated 8 Sep 2025
MH_CAB, MH_GR, MH_OPG = D(2025, 9, 30), D(2025, 11, 3), D(2026, 8, 19)      # press note 30 Sep 2025; GR 3 Nov 2025; operational guidelines listed 19 Aug 2026
UP_POL, UP_SOP = D(2025, 5, 7), D(2026, 3, 14)           # policy effective 7 May 2025 (Scutiger); rules file named 14 Mar 2026
assert (KA_OPG - KA_POL).days == 279 and (MH_OPG - MH_GR).days == 289 and (UP_SOP - UP_POL).days == 311
assert (MH_GR - MH_CAB).days == 34
assert KA_POL.replace(year=2029) > D(2029, 11, 1)        # five years from 3 Dec 2024 runs to December 2029
assert D(2026, 5, 27).strftime("%A") == "Wednesday"      # Haryana policy notified 27 May 2026 (PwC)
assert D(2026, 10, 26).strftime("%A") == "Monday"        # UP GCC Innovation Summit, 'Monday', 26 October 2026

# ---- 2. targets as stated: new GCCs, jobs; and ratios
step(2, "targets and jobs per GCC")
T = {  # state: (new GCCs, jobs, source tier)
    "Karnataka": (500, 350_000, "policy"), "Maharashtra": (400, 400_000, "policy"), "Gujarat": (250, 50_000, "policy"),
    "Madhya Pradesh": (50, 37_000, "policy"), "Rajasthan": (200, 150_000, "AIM"), "Haryana": (100, 30_000, "PwC"), "Uttar Pradesh": (500, 200_000, "mixed")}
JPG = {k: v[1] / v[0] for k, v in T.items()}
assert JPG == {"Karnataka": 700.0, "Maharashtra": 1_000.0, "Gujarat": 200.0, "Madhya Pradesh": 740.0, "Rajasthan": 750.0, "Haryana": 300.0, "Uttar Pradesh": 400.0}
assert max(JPG.values()) / min(JPG.values()) == 5.0
INV_PG = {"Maharashtra": 50_600 / 400, "Gujarat": 10_000 / 250}
assert INV_PG == {"Maharashtra": 126.5, "Gujarat": 40.0}
SIX = ["Karnataka", "Maharashtra", "Gujarat", "Madhya Pradesh", "Rajasthan", "Haryana"]
N6 = sum(T[k][0] for k in SIX)
J6 = sum(T[k][1] for k in SIX)
assert N6 == 1_500 and J6 == 1_017_000
N7, J7 = N6 + T["Uttar Pradesh"][0], J6 + T["Uttar Pradesh"][1]
assert N7 == 2_000 and J7 == 1_217_000
J8 = J7 + 50_000                                          # Odisha 50,000+ jobs (AIM)
assert J8 == 1_267_000
CB_N, CB_J = 1_380, 1_180_000                             # CBRE via IANS, August 2026 (as reported by AIM Research)
assert N6 - CB_N == 120 and f"{100 * (N6 - CB_N) / CB_N:.1f}" == "8.7" and f"{100 * (N7 - CB_N) / CB_N:.1f}" == "44.9"
assert f"{100 * (J7 - CB_J) / CB_J:.1f}" == "3.1" and f"{100 * (J8 - CB_J) / CB_J:.1f}" == "7.4"

# ---- 3. Karnataka baseline: do the numbers in the policy and the budget agree with the target?
step(3, "Karnataka baseline arithmetic")
assert 500 + 500 == 1_000                                 # the policy's own statement: 500 new, total 1,000, so a baseline of 500
assert 875 + 500 == 1_375                                 # if the statistics panel's 875+ is the baseline
assert f"{550 / 875:.3f}" == "0.629"                      # the 2026-27 budget's 550+ against the panel's 875+
assert f"{600_000 / 875:.0f}" == "686" and f"{600_000 / 500:.0f}" == "1200"       # talent pool of 0.6 million per GCC on each baseline
assert f"{100 * (JPG['Karnataka'] / (600_000 / 875) - 1):.1f}" == "2.1"           # target jobs per new GCC is within 2.1% of the average on the 875 baseline

# ---- 4. support ceilings
step(4, "support ceilings")
CAP = {"Gujarat": 200, "Haryana": 150, "Maharashtra": 100, "Madhya Pradesh": 30, "Uttar Pradesh": 25, "Rajasthan": 10}     # highest capital subsidy ceiling per GCC, Rs crore
assert [CAP[k] for k in ("Gujarat", "Haryana", "Maharashtra", "Madhya Pradesh", "Uttar Pradesh", "Rajasthan")] == sorted(CAP.values(), reverse=True)
assert CAP["Gujarat"] / CAP["Rajasthan"] == 20.0
assert 500e6 / 1e7 == 50 and 1_500e6 / 1e7 == 150 and 25e6 / 1e7 == 2.5 and 37.5e6 / 1e7 == 3.75 and 7.5e6 / 1e7 == 0.75 and 150e6 / 1e7 == 15
GJ_I_CAPEX, GJ_I_OPEX, GJ_II_CAPEX, GJ_II_OPEX, YRS = 50, 20, 200, 40, 5
assert GJ_I_CAPEX + GJ_I_OPEX * YRS == 150 and GJ_II_CAPEX + GJ_II_OPEX * YRS == 400
assert GJ_I_CAPEX / INV_PG["Gujarat"] == 1.25                     # Category I capex ceiling against the average investment per GCC implied by the target
assert f"{0.30 * INV_PG['Gujarat']:.0f}" == "12"                  # 30% of Rs 40 crore
assert 6_000 * 12 == 72_000 and round(20e7 / 72_000) == 2_778    # Odisha: Rs 6,000 a seat a month; ceiling Rs 20 crore a applicant is 2,778 seat-years
assert 10 / 0.25 == 40.0                        # UP Level-1: a 25% subsidy reaches its Rs 10 crore ceiling at Rs 40 crore of eligible investment
assert 10 / 0.30 > 33 and f"{10 / 0.30:.1f}" == "33.3"            # Rajasthan: 30% reaches Rs 10 crore at Rs 33.3 crore
assert 15 / 0.40 == 37.5                                          # MP Level I: 40% reaches Rs 15 crore at Rs 37.5 crore

TITLE = "State GCC policies in India: targeted jobs per new GCC range from 200 to 1,000"
plain = _h.unescape(TITLE)
assert 55 <= len(plain) <= 90, len(plain)
assert not any(w in plain.lower().split() for w in ("you", "your", "we", "our"))
print(f"consistency checks passed (dates, targets, Karnataka baseline, ceilings); title {len(plain)} characters", flush=True)
if "--check" in sys.argv:
    sys.exit(0)

from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402


def _rs(v, unit):
    s = f"{v:,.2f}".rstrip("0").rstrip(".")
    return f"Rs {s} {unit}"


step(5, "writing sections")
top = top_line([
    ("200 to 1,000", " jobs per new GCC is the range implied by seven states&rsquo; own targets, from Gujarat (50,000 jobs, 250 GCCs) to Maharashtra (4 lakh jobs, 400 GCCs); the targets are goals, and no count of GCCs opened under any policy was found."),
    ("1,375", " would be Karnataka&rsquo;s total after 500 new GCCs if the policy&rsquo;s own statistics panel of 875 existing GCCs is right; the target of 1,000 fits a baseline of 500, and the March 2026 budget says more than 550 are operating."),
    ("1,500 to 2,000", " new GCCs is the sum of the state targets in the primary documents (six states, then with Uttar Pradesh), against 1,380 in the national estimate that a comparison site attributes to CBRE; the job targets sum to 12.2 lakh against 11.8 lakh."),
])

tvo = ('<table class="gb-table"><thead><tr><th>Kind</th><th>What this piece includes</th></tr></thead><tbody>'
       '<tr><td><b>Decided</b></td><td>Ten states have a GCC policy or scheme in force: Karnataka (3 Dec 2024), Gujarat (10 Feb 2025), Madhya Pradesh (Feb 2025), Uttar Pradesh (effective 7 May 2025), Maharashtra (GR of 3 Nov 2025), Rajasthan (Dec 2025), Odisha (gazette 31 Dec 2025), Haryana (27 May 2026), Tamil Nadu (scheme, 2024), Andhra Pradesh (policy 4.0, 2024).</td></tr>'
       '<tr><td><b>Targets</b></td><td>New GCCs, jobs and investment for 2029 to 2031, as each state states them; Tamil Nadu and Andhra Pradesh state none in the sources read.</td></tr>'
       '<tr><td><b>Outcomes</b></td><td>None found: no count of GCCs opened or jobs created under any state policy was found. Karnataka&rsquo;s budget gives a count of operating GCCs (more than 550) but not a count since the policy.</td></tr>'
       '<tr><td><b>Not found</b></td><td>A policy read in full for any state; Andhra Pradesh&rsquo;s targets; a common definition of a GCC; the basis of the national estimate.</td></tr>'
       '</tbody></table>\n')

s1 = insight(
    "Targeted jobs per new GCC range from 200 in Gujarat to 1,000 in Maharashtra",
    bars("Targeted jobs per new GCC range from 200 in Gujarat to 1,000 in Maharashtra",
         [(k, v) for k, v in sorted(JPG.items(), key=lambda kv: kv[1])], accent="Gujarat", unit=" jobs", fmt=lambda v: f"{v:,.0f}", vmax=1_100,
         sub="Jobs targeted divided by new GCCs targeted, computed here: five-fold between the lowest and the highest. Karnataka, Maharashtra, Gujarat and Madhya Pradesh are from the policy documents; Rajasthan (AIM Research) and Haryana (PwC) are secondary; Uttar Pradesh divides 2 lakh jobs (AIM, five years) by 500 GCCs (Chief Minister, by 2031), two different horizons.",
         source="Policy documents of Karnataka, Maharashtra, Gujarat, Madhya Pradesh; Uttar Pradesh press release of 26 October 2026; AIM Research, 13 November 2026; PwC, 3 June 2026 (excerpts).")
    + numbers(["State", "Policy and date", "Targets as stated", "Source and status"],
              [["Karnataka", "GCC Policy 2024-29, notified 3 December 2024, in force five years", "500 new GCCs (1,000 in total), 3.5 lakh jobs, US$50 billion of output by 2029", "Policy PDF (primary, excerpt)"],
               ["Maharashtra", "GCC Policy 2025, cabinet note 30 September, GR 3 November 2025; eligible investment from 1 April 2025", "About 400 new GCCs, 4 lakh jobs; expected investment Rs 50,600 crore (Rs 126.5 crore a GCC, computed)", "GR and press note (primary, excerpts)"],
               ["Gujarat", "GCC Policy 2025-30, resolution 10 February 2025, launched 11 February", "At least 250 new GCCs, more than 50,000 jobs, Rs 10,000 crore (Rs 40 crore a GCC, computed)", "Resolution, DST page, CM release (primary, excerpts)"],
               ["Madhya Pradesh", "GCC Policy 2025, February 2025", "More than 50 GCCs and 37,000 direct jobs", "Policy PDF (primary, excerpt)"],
               ["Rajasthan", "GCC Policy 2025 under the RIPS 2024; order of December 2025; valid to 31 March 2029", "200+ GCCs and 1.5 lakh jobs by 2030", "AIM Research (secondary); the order excerpt carries no target"],
               ["Haryana", "GCC Policy 2026, notified 27 May 2026, five years", "100+ new GCCs and 30,000+ jobs", "PwC (secondary summary of the policy)"],
               ["Uttar Pradesh", "GCC Policy 2024, effective 7 May 2025; rules published March 2026", "500 GCCs by 2031 (Chief Minister, 26 October 2026); 2 lakh+ jobs in five years (AIM Research)", "Invest UP press release (primary); AIM (secondary)"],
               ["Odisha", "GCC Policy 2025, cabinet November 2025, gazette 31 December 2025", "Rs 1,000+ crore, 5+ hubs, 50,000+ jobs (AIM Research); no GCC count", "AIM (secondary); gazette excerpt has no target"],
               ["Andhra Pradesh; Tamil Nadu", "IT and GCC Policy 4.0 (2024-29); Special Scheme to promote GCCs (G.O. of 12 March 2024, to 31 March 2027)", "None found for Andhra Pradesh; Tamil Nadu&rsquo;s scheme covers up to 50 GCCs, and a 2030 goal of 460+ is reported", "AIM; Scutiger (secondary)"]],
              "Show the targets and their sources"),
    "A five-fold gap in jobs per targeted GCC means the targets do not describe the same kind of centre, so a state&rsquo;s count of GCCs cannot be compared with another&rsquo;s without a common definition of size and function.",
    "The Union Ministry of Electronics and Information Technology, with the states, should publish one definition of a GCC and a yearly count of GCCs and jobs by state against each policy target.",
    "targets")

s2 = insight(
    "Capital subsidy ceilings per GCC: Rs 10 crore in Rajasthan, Rs 200 crore in Gujarat",
    bars("Capital subsidy ceilings per GCC: Rs 10 crore in Rajasthan, Rs 200 crore in Gujarat",
         [(k, v) for k, v in CAP.items()], accent="Gujarat", unit=" crore", fmt=lambda v: _rs(v, "crore"), vmax=210,
         sub="Highest capital subsidy ceiling a single GCC can reach under each policy, Rs crore: Gujarat for a project above Rs 250 crore or 500 jobs, Haryana for the top zone (Rs 500 to 1,500 million in the PwC summary), Maharashtra by size band (secondary), Madhya Pradesh and Uttar Pradesh for their advanced category, Rajasthan under the state industrial scheme. The ceilings apply to different bases and are not directly comparable.",
         source="Gujarat policy resolution; Madhya Pradesh policy PDF; Invest UP policy page; Rajasthan GCC order (primary, excerpts); PwC, 3 June 2026; Scutiger, 7 October 2026 (secondary).")
    + numbers(["State", "Capital and operating support as stated", "Source and status"],
              [["Gujarat", "Category I (fixed capital under Rs 250 crore): up to 20% on buildings and 30% on computers, software and networks, ceiling Rs 50 crore, in 20 quarterly instalments; operating support up to 15% of eligible spend, ceiling Rs 20 crore a year for five years. Category II (Rs 250 crore or 500 jobs): ceilings Rs 200 crore and Rs 40 crore a year. Five-year maxima Rs 150 crore and Rs 400 crore (computed)", "Resolution of 10 February 2025 (primary)"],
               ["Haryana", "Capex support 50 to 75% of eligible capex, ceiling Rs 2.5 to 3.75 crore per 100 eligible employees or Rs 50 to 150 crore, in 10 annual instalments; opex support 50 to 65% for 5 to 9 years, ceiling Rs 0.75 crore per 100 employees or Rs 15 crore a year; operations from 1 January 2026 qualify", "PwC alert (secondary)"],
               ["Maharashtra", "20% capital subsidy (ceiling Rs 10 to 100 crore by size) or rental assistance, not both; payroll support for three years on salaries above Rs 1 lakh a month", "Scutiger (secondary); the GR lists the heads without rates in the excerpt"],
               ["Madhya Pradesh", "Capex subsidy 40% of eligible investment up to Rs 15 crore (Level I) and Rs 30 crore (Advanced) in five annual instalments; land rebate up to 75%; interest assistance 6% up to Rs 5 crore; stamp duty 100%. AIM Research says the rates are not stated, and the policy states them", "Policy PDF (primary, excerpt); AIM (secondary, incomplete)"],
               ["Uttar Pradesh", "Level 1 (Rs 15 crore or 100 jobs; Rs 20 crore or 200 jobs in Gautam Buddh Nagar and Ghaziabad): 25% capital subsidy to Rs 10 crore over seven years; 20% opex subsidy to Rs 40 crore a year for five years; payroll support up to Rs 1.8 lakh a UP-domiciled employee; 30 to 50% land subsidy. Advanced: Rs 25 crore and Rs 80 crore a year", "Invest UP policy page, rules and press release (primary, excerpts)"],
               ["Rajasthan", "30% of project cost excluding land and buildings, ceiling Rs 10 crore over 10 years; minimum investment Rs 5 crore; 50% of land or floor space cost up to Rs 1 crore; electricity duty exempt for 7 years; stamp duty 75% exempt and 25% reimbursed", "Order of December 2025 (primary, excerpt); notified 2 December per Scutiger, order file dated 12 December: not reconciled"],
               ["Karnataka", "Incentives for infrastructure apply only beyond Bengaluru: 50% of rent, ceiling Rs 50 lakh (first 10 GCCs a year) for 100+ jobs and Rs 2 crore (first 6 a year) for 500+ jobs; 50% of internship stipends up to Rs 5,000 a month for three months; innovation labs 40% of capex with a ceiling of Rs 4 crore (policy summary) or Rs 5 crore (2026 call) in Bengaluru and 75% or Rs 3 crore beyond", "Operational guidelines; incentive page; call for proposals (primary, excerpts): the two Bengaluru ceilings conflict"],
               ["Odisha", "Capital subsidy and other support under the Odisha IT Policy; rent reimbursement Rs 6,000 a seat a month with a ceiling of Rs 20 crore an applicant, which is 2,778 seat-years (computed); up to 100 interns a year", "Gazette of 31 December 2025 (primary, excerpt)"],
               ["Tamil Nadu", "Payroll subsidy 30%, 20% and 10% over three years for up to 50 GCCs with Forbes Global 2000 or Fortune 1000 parents and 200+ direct jobs; to 31 March 2027", "Scutiger (secondary)"],
               ["Against average investment", f"Gujarat&rsquo;s Category I capex ceiling of Rs 50 crore is {GJ_I_CAPEX / INV_PG['Gujarat']:.2f} times the Rs 40 crore average investment per GCC implied by its own target, and 30% of Rs 40 crore is Rs 12 crore; a 25% subsidy reaches Uttar Pradesh&rsquo;s Rs 10 crore ceiling at Rs 40 crore of eligible investment, Rajasthan&rsquo;s at Rs {10 / 0.30:.1f} crore and Madhya Pradesh&rsquo;s Level I at Rs 37.5 crore (computed)", "Computed here"]],
              "Show the support terms by state and the checks"),
    "The ceilings differ by a factor of 20, and Gujarat&rsquo;s lowest-tier ceiling is above the average investment per GCC implied by its own target, so the ceiling binds only for large centres while the rate decides the cost to the state.",
    "Each state&rsquo;s IT department should publish, for each GCC supported, the investment, jobs and incentive sanctioned and paid, so that the cost per job under each policy can be computed.",
    "ceilings")

s3 = insight(
    "Karnataka&rsquo;s 1,000 GCC target fits a baseline of 500, not the 875 in its policy panel",
    bars("Karnataka&rsquo;s 1,000 GCC target fits a baseline of 500, not the 875 in its policy panel",
         [("Policy statistics panel, 2024 (extraction unclear)", 875), ("Policy introduction and state portal: 'over 500'", 500), ("Budget 2026-27, March 2026: 'more than 550' operating", 550),
          ("Target: total GCCs by 2029", 1_000), ("500 new on a baseline of 875 (computed)", 1_375)],
         accent="Target: total GCCs by 2029", unit="", fmt=lambda v: f"{v:,.0f}", vmax=1_450,
         sub="Number of GCCs in Karnataka as each document gives it. The policy says 500 new GCCs will bring the total to 1,000 by 2029, which implies 500 now. The statistics panel of the policy PDF, as extracted, reads 875+ units for the state, and the budget of March 2026 says more than 550 operate; counting units, centres or companies may explain the gap, and the documents do not say.",
         source="Karnataka GCC Policy 2024-29 (PDF excerpt, garbled statistics panel); Karnataka Startup Cell and IT department pages; Karnataka Budget 2026-27, paragraph 370 (excerpts).")
    + numbers(["Item", "Value", "Source and status"],
              [["Target", "500 new GCCs, total 1,000 by 2029; 3.5 lakh new jobs; US$50 billion of output from the new GCCs", "Policy PDF; Budget 2026-27 repeats the 500, 3.5 lakh and US$50 billion"],
               ["Statistics panel", "Karnataka 875+ GCC units, 0.6 million+ talent pool and US$22.2 billion market; India 1,975+ (printed '2975+'), 1.9 million+ and US$64.6 billion; the extraction is jumbled, so the assignment is inferred", "Policy PDF (excerpt)"],
               ["Check on the 875", "Talent per GCC is 686 on 875 and 1,200 on 500 (computed); the target of 700 jobs per new GCC is within 2.1% of the first, which suggests the panel is a real average", "Computed here; inference"],
               ["Other counts", "'Over 500' GCCs and 35% of India&rsquo;s GCC workforce on the policy page; 'over 40%' of India&rsquo;s GCCs in an August 2025 department document; 'more than 550' in the March 2026 budget, which is 0.63 of 875 (computed)", "Policy page; department document; Budget 2026-27"],
               ["Operational status", "Operational guidelines dated 8 September 2025, 279 days after the policy of 3 December 2024; applications open via KITS; calls for proposals for innovation labs run from 1 April to 30 September 2026", "Guidelines PDF; call for proposals (excerpts)"],
               ["Beyond Bengaluru", "All infrastructure incentives apply only outside Bengaluru; a new IT park at Mangaluru and Mysuru as a second IT city are announced in the budget", "Policy PDF; Budget 2026-27"]],
              "Show the Karnataka figures and checks"),
    "Karnataka&rsquo;s own documents give three baselines for the number of GCCs, 500, 550 and 875, and the target of 1,000 matches only the first, so progress cannot be read until the state says which count the target uses.",
    "The Karnataka IT, BT and Science and Technology Department should state which unit the target counts, give the number at 3 December 2024, and publish the number registered with the Karnataka Innovation and Technology Society each quarter.",
    "karnataka")

s4 = insight(
    "State targets sum to 1,500 to 2,000 new GCCs against 1,380 in the national estimate",
    bars("State targets sum to 1,500 to 2,000 new GCCs against 1,380 in the national estimate",
         [("Six state targets in policy documents and secondary summaries", N6), ("Plus Uttar Pradesh&rsquo;s 500 by 2031", N7), ("National estimate, CBRE via IANS (through AIM Research)", CB_N)],
         accent="National estimate, CBRE via IANS (through AIM Research)", unit="", fmt=lambda v: f"{v:,.0f}", vmax=2_100,
         sub=f"New GCCs targeted. The six are Karnataka 500, Maharashtra 400, Gujarat 250, Rajasthan 200, Haryana 100 and Madhya Pradesh 50. Adding Uttar Pradesh gives {N7:,}. The sums are {100 * (N6 - CB_N) / CB_N:.1f}% and {100 * (N7 - CB_N) / CB_N:.1f}% above the estimate (computed). Job targets sum to {J7 / 1e5:.1f} lakh with Uttar Pradesh against 11.8 lakh, {100 * (J7 - CB_J) / CB_J:.1f}% above.",
         source="Policy documents and press releases as in the first section; AIM Research, 13 November 2026, citing CBRE via IANS, August 2026 (secondary; the CBRE release was not read).")
    + numbers(["Item", "Value", "Source and status"],
              [["Sum of GCC targets", f"{N6:,} for six states and {N7:,} with Uttar Pradesh; Tamil Nadu&rsquo;s 460+ and Telangana&rsquo;s draft goal of 100 in 2026 are not added; horizons differ (2029 to 2031)", "Computed here"],
               ["Sum of job targets", f"{J6:,} for six states, {J7:,} with Uttar Pradesh and {J8:,} with Odisha&rsquo;s 50,000+ (computed)", "Computed here"],
               ["National estimate", "About 1,380 new GCCs and 1.18 million jobs by 2031 across states with GCC policies; the states counted and the method are not given", "AIM Research citing CBRE via IANS (secondary; not read at source)"],
               ["Reading", "The job sum with Uttar Pradesh is within 3.1% of the estimate while the GCC sum is 8.7% to 44.9% above it, so the estimate may count GCCs differently or use different states and horizons", "Computed; inference"],
               ["Policy to operating rules", f"Karnataka {(KA_OPG - KA_POL).days} days; Maharashtra {(MH_OPG - MH_GR).days} days from the GR (and {(MH_GR - MH_CAB).days} days from cabinet note to GR); Uttar Pradesh {(UP_SOP - UP_POL).days} days; dates are from file listings, not from the rules themselves", "Computed from listing dates"],
               ["In preparation", "Telangana: a draft policy reported in September 2026 aiming at 100 GCCs this year; Kerala: a roadmap from 45 to 150 GCCs by 2031; a national framework for tier-2 cities announced in the Union Budget 2025-26 was still being drafted in August 2026", "AIM Research citing Siasat, GKToday, Outlook Business (secondary)"]],
              "Show the sums, the national estimate and the lags"),
    "The state targets cannot be reconciled with the national estimate of 1,380, which suggests that the estimate and the states count different things or different years, and neither gives the basis.",
    "The Union IT Ministry should publish the states, horizons and definitions behind the national estimate, and each state should publish its target and baseline on one common basis.",
    "sums")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Union Ministry of Electronics and Information Technology:</b> publish one definition of a GCC and a yearly count of GCCs and jobs by state, against each state target.</li>
<li><b>Karnataka IT, BT and Science and Technology Department:</b> state the unit the 1,000 target counts, the number at 3 December 2024 and a quarterly count of registered GCCs.</li>
<li><b>Each state IT department:</b> publish, for each GCC supported, the investment, jobs and incentive sanctioned and paid, so that cost per job can be computed.</li>
<li><b>Andhra Pradesh and Tamil Nadu:</b> publish targets and a baseline for their GCC policy and scheme, as the other eight states do.</li>
<li><b>Authors of national estimates:</b> publish the states, horizons and method behind the 1,380 GCCs and 1.18 million jobs, so that they can be reconciled with the state targets.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>A target is a goal stated for 2029 to 2031; an outcome is a measured result. No state publishes an outcome under its GCC policy in the sources read.</li>
<li>Jobs per GCC, investment per GCC, sums, differences and ceilings are computed here from the figures shown, and each is checked by an assertion in the builder. Dates to operating rules use the dates of file listings and are approximate.</li>
<li>Primary documents (policies, resolutions, gazettes, press releases, operational guidelines, the Karnataka budget) were read as search excerpts; none was read in full. Haryana comes from a PwC alert on the policy, and Maharashtra&rsquo;s rates, Tamil Nadu and Andhra Pradesh from secondary summaries. The comparison page of AIM Research, a commercial data provider, was read in full and used for items no primary excerpt gave; it is labelled secondary.</li>
<li>Targets differ in horizon (2029 for Karnataka, 2030 for Rajasthan, 2031 for the national estimate and Uttar Pradesh) and in what they count, so sums are indicative.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>Any GCC policy in full. The incentive rates for Maharashtra and the targets for Rajasthan, Haryana and Odisha come from secondary summaries.</li>
<li>Targets for Andhra Pradesh, and any target in Tamil Nadu&rsquo;s scheme beyond the 50-GCC limit and a reported 2030 goal of 460+.</li>
<li>Which count of GCCs in Karnataka is right (500, 550 or 875), whether the policy&rsquo;s statistics panel was read correctly from a jumbled extraction, and why the March 2026 budget gives a lower number than the panel.</li>
<li>The basis of the national estimate of 1,380 GCCs and 1.18 million jobs, which was read only through AIM Research.</li>
<li>How many GCCs have opened, and how many jobs have been created, under any state policy, and how much incentive has been paid.</li>
<li>The notification date of Rajasthan&rsquo;s policy (2 December 2025 in one secondary source and an order file dated 12 December), and the Bengaluru ceiling for Karnataka&rsquo;s innovation labs (Rs 4 crore or Rs 5 crore).</li>
<li>Whether incentives such as Maharashtra&rsquo;s payroll subsidy limited to salaries above Rs 1 lakh a month, or Uttar Pradesh&rsquo;s domicile conditions, change the cost per job materially.</li>
</ul></details>
'''

step(6, "assembling body")
body = STYLE + top + tvo + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://eitbt.karnataka.gov.in/uploads/media_to_upload1732030878.pdf">Karnataka GCC Policy 2024-29</a>, '
    '<a href="https://eitbt.karnataka.gov.in/uploads/media_to_upload1757327531.pdf">Karnataka GCC Policy operational guidelines</a>, '
    '<a href="https://eitbt.karnataka.gov.in/it/public/policy5/en">Karnataka GCC Policy page</a>, '
    '<a href="https://eitbt.karnataka.gov.in/it/public/139/click-on-%27read-more%27-to-know-more-about-the-policy-incentives./en">Karnataka incentive summary</a>, '
    '<a href="https://eitbt.karnataka.gov.in/uploads/media_to_upload1774351295.pdf">Karnataka call for innovation labs and centres of excellence</a> and '
    '<a href="https://finance.karnataka.gov.in/uploads/Eng%20Final%20BS%202026-27_1772786310.pdf">Karnataka Budget 2026-27</a> (official, excerpts); '
    '<a href="https://maitri.maharashtra.gov.in/wp-content/themes/maitri/PDF/GCC%20Policy%20GR%2003112025.pdf">Maharashtra GCC Policy GR, 3 November 2025</a>, '
    '<a href="https://industry.maharashtra.gov.in/sites/default/files/2025-09/gcc-policy-paraesa-naota-english.pdf">Maharashtra press note, 30 September 2025</a> and '
    '<a href="https://industry.maharashtra.gov.in/sites/default/files/2026-08/operational-guidelines-for-maharashtra-gcc-policy-2025.pdf">Maharashtra operational guidelines</a> (official, excerpts); '
    '<a href="https://dstpolicy.gujarat.gov.in/public/assets/gccpolicy/GCC_Policy_2025-30_Booklet.pdf">Gujarat GCC Policy 2025-30 booklet</a>, '
    '<a href="https://dst.gujarat.gov.in/dst/Home/GujaratGlobalCapabilityCenter">Gujarat DST page</a> and '
    '<a href="https://cmogujarat.gov.in/en/latest-news/gujarat-gcc-policy-2025-30-launch">Gujarat Chief Minister&rsquo;s release</a> (official, excerpts); '
    '<a href="https://invest.up.gov.in/up-gcc-policy-2024">UP GCC Policy 2024</a>, '
    '<a href="https://invest.up.gov.in/wp-content/uploads/2026/03/GCC-SOP_140326.pdf">UP GCC rules</a>, '
    '<a href="https://invest.up.gov.in/wp-content/uploads/2025/05/ENGLISH_Press-Release_GCC-Policy_May-06-2025.pdf">Invest UP press release, May 2025</a> and '
    '<a href="https://invest.up.gov.in/wp-content/uploads/2026/10/1-Eng_PressRelease_GCC_Summit_26Oct_2026_301026.pdf">Invest UP press release, 26 October 2026</a> (official, excerpts); '
    '<a href="https://invest.mp.gov.in/wp-content/uploads/2025/02/GCC-Policy-2025.pdf">Madhya Pradesh GCC Policy 2025</a>, '
    '<a href="https://jankalyanfile.rajasthan.gov.in/Content/UploadFolder/OrderEntry/ICOM/2025/Notification/O_121225_f3b5af28-722e-4b67-bd87-fd08ac56a9ed.pdf">Rajasthan GCC Policy 2025 order</a> and '
    '<a href="https://it.odisha.gov.in/sites/default/files/2026-01/6018-E%26IT%20Deptt.pdf">Odisha GCC Policy 2025 gazette</a> (official, excerpts); '
    '<a href="https://www.pwc.in/assets/pdfs/news-alert/tax-insights/2026/pwc_india_indirect_tax_insights_3_june_2026_government_of_haryana_notifies_the_haryana_global_capability_centres_policy_2026.pdf">PwC, 3 June 2026</a> (secondary: Haryana); '
    '<a href="https://www.scutiger.com/handbooks/gcc-playbook/india-state-gcc-incentives">Scutiger Technologies, 7 October 2026</a> and '
    '<a href="https://gccexplorer.com/guides/state-gcc-policies-india">AIM Research, 13 November 2026</a> (secondary, commercial data providers; the second read in full). '
    'Percentages, ratios and sums computed by this blog. Analysed 21 November 2026.')
RELATED = []

step(7, "writing page")
build("Policy &middot; States", TITLE,
      "Ten Indian states have GCC policies; this piece compares their targets, the support ceilings, Karnataka&rsquo;s inconsistent baseline and the sum of state targets against a national estimate, and says what no source shows.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(plain), "chars in title")
step(8, "page checks")
step(9, "complete")
