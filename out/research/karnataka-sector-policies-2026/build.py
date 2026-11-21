"""Karnataka's 2026 sector policies: the Sustainable Data Centre Policy 2026-2031 and the Marine Biotechnology Policy 2026-2031
(both approved by the cabinet at Mangaluru on Friday 18 September 2026) and the Aerospace Policy 2026-31 (approved Wednesday 9 September 2026).
Build from the repo root:  python3 out/research/karnataka-sector-policies-2026/build.py            (writes out/post-karnataka-sector-policies-2026.html)
                           python3 out/research/karnataka-sector-policies-2026/build.py --check    (arithmetic and asserts only)
Every figure is from the source named beside it, or computed below with an assert. Analysed 21 November 2026.
No policy text was found for any of the three. Pages read in full: ThePrint (19 Sep), Deccan Chronicle (19 Sep), MediaNama (21 Sep), Dataquest (20 Sep),
ThePrint/PTI (9 Sep), HR Katha (10 Sep), GKToday (19 Sep), IASPoint (17 Nov). Everything else was read as a search excerpt; the post says so.
The data-centre cooling analysis in out/research/dc-cooling is reused for one figure (25-26 million litres per MW-year, flagged there as a press and advocacy figure)."""
import datetime as dt
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
OUT = ROOT / "out/post-karnataka-sector-policies-2026.html"
STEPS = 9


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. dates
step(1, "dates and weekday checks")
D_DC_MAR, D_AERO = D(2026, 9, 18), D(2026, 9, 9)
assert D_DC_MAR.strftime("%A") == "Friday"            # Deccan Chronicle, ThePrint, BusinessLine: 'on Friday'; ThePrint dated 19 Sep
assert D_AERO.strftime("%A") == "Wednesday"           # PTI, 9 Sep: 'on Wednesday'
D_LAUNCH = D(2026, 11, 17)
assert D_LAUNCH.strftime("%A") == "Tuesday" and (D_LAUNCH - D_DC_MAR).days == 60      # IASPoint: marine policy 'formally announced' on 17 Nov at the Bengaluru Tech Summit
assert (D_DC_MAR - D_AERO).days == 9

# ---- 2. which rupee figure belongs to which decision (ThePrint headline joins two decisions)
step(2, "attributing Rs 1,300 crore and Rs 120 crore")
DC_OUT, MAR_OUT = 1300.45, 120
assert round(DC_OUT + MAR_OUT, 2) == 1420.45
assert round(DC_OUT) == 1300 and MAR_OUT != round(DC_OUT)      # the headline's 'Rs 1,300-cr' is the data centre policy only
assert round(100 * MAR_OUT / (DC_OUT + MAR_OUT), 1) == 8.4

# ---- 3. data centre: target against baselines
step(3, "data centre baselines and pace")
TARGET_MW = 1000
BASE = [("Anarock, H1 2026 (Bengaluru, text panel)", 137.0), ("Cushman &amp; Wakefield figure via NextMSC, GHAR and The Hindu, H1 2026 (Bengaluru)", 162.0),
        ("Knight Frank, 2025 (Bengaluru live capacity)", 169.5), ("Lok Sabha reply of 18 March 2026, industry sources (Bengaluru)", 182.0),
        ("State IT secretary, July 2026 (Karnataka installed)", 400.0)]
assert [b[1] for b in BASE] == sorted(b[1] for b in BASE)
assert f"{TARGET_MW / 400:.1f}" == "2.5" and f"{TARGET_MW / 137:.1f}" == "7.3" and f"{TARGET_MW / 162:.1f}" == "6.2"
KF20, KF25 = 106.3, 169.5
assert round(KF25 - KF20, 1) == 63.2 and round((KF25 - KF20) / 5, 2) == 12.64
assert f"{100 * ((KF25 / KF20) ** (1 / 5) - 1):.1f}" == "9.8"
NEED_YR = (TARGET_MW - KF25) / 6          # end-2025 to end-2031
assert f"{NEED_YR:.1f}" == "138.4" and f"{NEED_YR / ((KF25 - KF20) / 5):.1f}" == "11.0"
assert f"{100 * ((TARGET_MW / KF25) ** (1 / 6) - 1):.1f}" == "34.4"
assert (TARGET_MW - 400) / 6 == 100.0
PER_MW_OUTLAY = DC_OUT / TARGET_MW                         # Rs crore of policy budget per MW of target
assert f"{PER_MW_OUTLAY:.2f}" == "1.30"
CAPEX_PER_MW, INV_IMPLIED = 60, 60 * TARGET_MW             # state officials, DH 18 July 2026: about Rs 60 crore per MW
assert INV_IMPLIED == 60_000 and f"{100 * DC_OUT / INV_IMPLIED:.1f}" == "2.2"
WATER_ML_MW_YR = 25                                        # million litres per MW-year, traditional cooling (GHAR.tv; press and advocacy figure per out/research/dc-cooling)
WATER_MLD = WATER_ML_MW_YR * TARGET_MW / 365
assert f"{WATER_MLD:.1f}" == "68.5" and f"{100 * WATER_MLD / 400:.1f}" == "17.1"     # against 400 MLD of surplus treated water (state IT secretary)

# ---- 4. aerospace
step(4, "aerospace targets")
A_INV_NEW, A_INV_OLD, A_JOBS_NEW, A_JOBS_OLD = 60_000, 45_000, 60_000, 60_000
assert f"{100 * (A_INV_NEW / A_INV_OLD - 1):.1f}" == "33.3" and A_JOBS_NEW == A_JOBS_OLD
assert A_INV_NEW / A_JOBS_NEW == 1.0 and A_INV_OLD / A_JOBS_OLD == 0.75        # Rs crore of investment per job targeted
assert D(2022, 8, 26).replace(year=2027) == D(2027, 8, 26)                        # 2022-27 policy valid five years from 26 Aug 2022, or until a new policy

# ---- 5. marine biotechnology
step(5, "marine biotechnology targets and baselines")
M_BASE, M_LO, M_HI = 2, 6, 8
assert M_LO / M_BASE == 3 and M_HI / M_BASE == 4
assert f"{100 * ((M_LO / M_BASE) ** (1 / 5) - 1):.1f}" == "24.6" and f"{100 * ((M_HI / M_BASE) ** (1 / 5) - 1):.1f}" == "32.0"
J_TECH, J_COAST, J_TOTAL = 2_500, 7_500, 10_000
assert J_TECH + J_COAST == J_TOTAL                         # GKToday's two categories sum to ThePrint's 'approximately 10,000'
assert MAR_OUT * 1e7 / J_TOTAL == 120_000                  # Rs per job targeted
FISH_NOW, FISH_OLD, FISH_2020 = 9.63, 5.81, 8.0            # lakh tonnes: 2024-25, 2015-16 (ThePrint, Economic Survey 2025-26); 2020 report 'nearly 800,000 tons'
assert f"{100 * (FISH_NOW / FISH_OLD - 1):.1f}" == "65.7" and f"{100 * (FISH_NOW / FISH_2020 - 1):.1f}" == "20.4"
SW_UNITS, SW_T = 21_000, 9_450
assert SW_T / SW_UNITS == 0.45
SW_AREA, SW_POT = 0.04, 1280.05
assert f"{100 * SW_AREA / SW_POT:.4f}" == "0.0031"
assert 10_000 + 21_000 == 31_000

TITLE = "Karnataka&rsquo;s 2026 policies: data centre, aerospace and marine biotechnology targets"
import html as _h
plain = _h.unescape(TITLE)
assert 55 <= len(plain) <= 90, len(plain)
assert not any(w in plain.lower().split() for w in ("you", "your", "we", "our"))
print(f"consistency checks passed (data centre, aerospace, marine); title {len(plain)} characters", flush=True)
if "--check" in sys.argv:
    sys.exit(0)

from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

def _rs(v, unit):
    s = f"{v:,.2f}".rstrip("0").rstrip(".")
    return f"Rs {s} {unit}"


step(6, "writing sections")
top = top_line([
    (f"Rs {DC_OUT:,.2f} crore", f" is the five-year budget framework of the Sustainable Data Centre Policy 2026&ndash;2031, approved at Mangaluru on 18 September 2026; the marine biotechnology policy approved the same day carries Rs {MAR_OUT} crore, and the aerospace policy of 9 September states no outlay in the reports read."),
    ("1,000 MW", f" is the data centre target for 2031, {TARGET_MW / 400:.1f} to {TARGET_MW / 137:.1f} times the capacity reported today depending on the baseline; a target, not an outcome."),
    ("$6&ndash;8 billion", f" is the marine target for 2031 against about $2 billion, {M_LO // M_BASE} to {M_HI // M_BASE} times, while the aerospace policy targets Rs {A_INV_NEW:,} crore of investment and {A_JOBS_NEW:,} jobs; no source gives results for any of the three."),
])

tvo = ('<table class="gb-table"><thead><tr><th>Kind</th><th>What this piece includes</th></tr></thead><tbody>'
       '<tr><td><b>Decided</b></td><td>Cabinet approval of three policies: aerospace on 9 September 2026; data centres and marine biotechnology on 18 September 2026.</td></tr>'
       '<tr><td><b>Targets</b></td><td>1,000 MW of data centre load and a 10&ndash;12% share of AI-ready capacity; Rs 60,000 crore and 60,000 jobs in aerospace; $2 billion to $6&ndash;8 billion and about 10,000 jobs in marine biotechnology. All are goals for 2031.</td></tr>'
       '<tr><td><b>Outcomes</b></td><td>None found for these policies. Baselines that exist (data centre capacity, the 2022&ndash;27 aerospace targets, fish production) pre-date them.</td></tr>'
       '<tr><td><b>Not found</b></td><td>The text of any of the three policies, incentive rates for data centres and marine biotechnology, any amount for the seaweed production-linked incentive, and any aerospace outlay.</td></tr>'
       '</tbody></table>\n')

s1 = insight(
    "Rs 1,300.45 crore belongs to the data centre policy; the marine policy has Rs 120 crore",
    bars("Rs 1,300.45 crore is the data centre budget; the marine policy has Rs 120 crore",
         [("Sustainable Data Centre Policy 2026&ndash;2031", DC_OUT), ("Marine Biotechnology Policy 2026&ndash;2031", MAR_OUT)],
         accent="Sustainable Data Centre Policy 2026&ndash;2031", unit=" crore", fmt=lambda v: _rs(v, "crore"), vmax=1400,
         sub=f"Five-year budget frameworks, Rs crore. Together Rs {DC_OUT + MAR_OUT:,.2f} crore (computed); the marine share is {100 * MAR_OUT / (DC_OUT + MAR_OUT):.1f}%. The Deccan Chronicle calls the data centre figure a &lsquo;revised budget framework&rsquo; and Dataquest a &lsquo;proposed outlay&rsquo;; what it was revised from is not stated.",
         source="Deccan Chronicle, 19 September 2026; ThePrint, 19 September 2026; Dataquest, 20 September 2026; The Hindu BusinessLine, 18 September 2026 (all secondary).")
    + flow([("9 Sep 2026 (Wednesday)", "Cabinet approves the Karnataka Aerospace Policy 2026&ndash;31, reported by PTI from Bengaluru; no outlay or target figure appears in the PTI text."),
            ("18 Sep 2026 (Friday)", "Cabinet meeting in Mangaluru, chaired by Chief Minister D.K. Shivakumar, approves the Sustainable Data Centre Policy 2026&ndash;2031 and the Marine Biotechnology Policy 2026&ndash;2031 (Deccan Chronicle, ThePrint, BusinessLine, Dataquest).", True),
            ("19 Sep 2026", "ThePrint headline: &lsquo;Rs 1,300-cr data centre policy, PLI-centred Blue Bioeconomy roadmap&rsquo;; the text gives Rs 1,300.45 crore to the data centre policy and Rs 120 crore to the marine policy."),
            ("17 Nov 2026 (Tuesday)", "Marine policy &lsquo;formally announced&rsquo; at the 29th Bengaluru Tech Summit, 60 days after approval (IASPoint, a study-notes site; secondary).")])
    + numbers(["Item", "Statement", "Source and status"],
              [["Data centre policy", "Revised budget framework of Rs 1,300.45 crore for five years; 1 GW cumulative IT load and 10&ndash;12% of India&rsquo;s AI-ready capacity by 2031", "Deccan Chronicle, ThePrint, MediaNama, Dataquest (page text read)"],
               ["Marine policy", "Rs 120 crore over five years for the Karnataka Institute of Marine Biotechnology and Blue Economy (KIMBE), marine biotechnology zones, the seaweed incentive and a blue carbon pilot", "ThePrint; BusinessLine; GKToday"],
               ["Combined", f"Rs {DC_OUT + MAR_OUT:,.2f} crore (computed here); no source gives a combined figure", "Computed"],
               ["Venue", "Mangaluru; ThePrint&rsquo;s dateline reads Bengaluru, but its text and the others place the meeting in Mangaluru", "ThePrint; Deccan Chronicle; BusinessLine; Dataquest"],
               ["Aerospace outlay", "Not stated in the PTI or HR Katha text; a search excerpt mentions a Rs 4,000 crore support figure, from a page not read and not used", "Not established"]],
              "Show the figures and which decision each belongs to"),
    "The Rs 1,300 crore figure in the headline belongs to the data centre policy alone, while the roadmap built around a production-linked incentive is the marine policy, whose budget is Rs 120 crore.",
    "The Department of Electronics, IT, BT and Science and Technology should publish each approved policy with its budget by component, so that a headline cannot join two budgets.",
    "budget")

s2 = insight(
    "Karnataka&rsquo;s 1,000 MW data centre target is 2.5 to 7.3 times reported capacity",
    bars("Karnataka&rsquo;s 1,000 MW data centre target is 2.5 to 7.3 times reported capacity",
         [(b[0], b[1]) for b in BASE] + [("Policy target, cumulative IT load by 2031", TARGET_MW)],
         accent="Policy target, cumulative IT load by 2031", unit=" MW", vmax=1000,
         sub=f"MW of IT load. The baselines differ in scope and date: five sources give 137 to 182 MW for Bengaluru and about 400 MW for the state. Against 400 MW the target is {TARGET_MW / 400:.1f} times; against 162 MW it is {TARGET_MW / 162:.1f} times; against 137 MW it is {TARGET_MW / 137:.1f} times (computed).",
         source="Sources as listed in the table below; secondary except the Lok Sabha reply (official, read as an excerpt).")
    + numbers(["Item", "Value", "Source and status"],
              [["Target", "1 GW cumulative IT load by 2031 and 10&ndash;12% of India&rsquo;s AI-ready data centre capacity; the 10&ndash;12% is called an &lsquo;ambition&rsquo;", "Deccan Chronicle, 19 September 2026"],
               ["Capacity, state", "About 400 MW installed; official data pegs 18 of 32 centres at 292.27 MW and has none for the other 14", "Deccan Herald, 18 July 2026 (IT secretary); The Hindu, 2 October 2026 (excerpts)"],
               ["Capacity, Bengaluru", "162 MW operational (H1 2026), 9.1% of India&rsquo;s 1,789 MW; 169.5 MW in 2025; 182 MW in a March 2026 reply; 137 MW in one Anarock panel", "NextMSC (secondary, Cushman &amp; Wakefield); Knight Frank; PIB, 18 March 2026; Anarock"],
               ["Pace, Bengaluru", f"Live capacity rose from {KF20} MW in 2020 to {KF25} MW in 2025, {KF25 - KF20:.1f} MW or {(KF25 - KF20) / 5:.2f} MW a year ({100 * ((KF25 / KF20) ** (1 / 5) - 1):.1f}% a year, computed)", "Knight Frank, India Data Centre Market Update 2025 (excerpt)"],
               ["Pace needed", f"From 169.5 MW at end-2025 to 1,000 MW at end-2031 is {NEED_YR:.1f} MW a year, {NEED_YR / ((KF25 - KF20) / 5):.1f} times the 2020&ndash;25 pace in Bengaluru; from 400 MW it is 100 MW a year (computed; the 400 MW has no earlier series)", "Computed here"],
               ["Pipeline", "About 8 MW under construction and 92 MW planned in Bengaluru, near 100 MW; the Hindu of 18 November repeats &lsquo;162 MW with a pipeline exceeding 100 MW&rsquo;", "GHAR.tv (secondary); The Hindu, 18 November 2026 (excerpt)"],
               ["Budget per MW", f"Rs {PER_MW_OUTLAY:.2f} crore of policy budget per MW of target; officials put investment at about Rs {CAPEX_PER_MW} crore per MW, or Rs {INV_IMPLIED:,} crore for 1,000 MW, so the budget is {100 * DC_OUT / INV_IMPLIED:.1f}% of that (computed)", "Deccan Herald, 18 July 2026; computed"],
               ["Water", f"Traditional cooling is quoted at about {WATER_ML_MW_YR} million litres per MW a year; for 1,000 MW that is {WATER_MLD:.1f} million litres a day, {100 * WATER_MLD / 400:.1f}% of the 400 million litres a day of surplus treated water the IT secretary cites (computed upper bound)", "GHAR.tv; this blog&rsquo;s data-centre cooling analysis flags 25&ndash;26 million litres as a press and advocacy figure above the physical range"],
               ["Incentive rates", "Not found: the policy covers capital investment, land, electricity, connectivity, green energy, R&amp;D, skilling and MSMEs without rates in any report read", "Not established"]],
              "Show the data centre baselines, pace and checks"),
    f"The target is {TARGET_MW / 400:.1f} to {TARGET_MW / 137:.1f} times the capacity reported today and needs about {NEED_YR:.0f} MW a year against the 13 MW a year Bengaluru added in 2020&ndash;25, and it equals the 1,000 MW already planned in April 2026, so it is a goal rather than a result.",
    "The Electronics, IT and BT Department should publish a single dated series of installed and operational data centre capacity for the state, so that progress to 1,000 MW can be read against one baseline.",
    "datacentre")

s3 = insight(
    "Aerospace investment target rises 33.3% to Rs 60,000 crore; jobs target stays at 60,000",
    bars("Aerospace investment target: Rs 45,000 crore in 2022&ndash;27, Rs 60,000 crore in 2026&ndash;31",
         [("Aerospace and Defence Policy 2022&ndash;27 target", A_INV_OLD), ("Aerospace Policy 2026&ndash;31 target", A_INV_NEW)],
         accent="Aerospace Policy 2026&ndash;31 target", unit=" crore", fmt=lambda v: _rs(v, "crore"), vmax=65_000,
         sub=f"Investment targets over five years, Rs crore; the increase is {100 * (A_INV_NEW / A_INV_OLD - 1):.1f}% (computed). Both policies target 60,000 jobs, so investment per targeted job rises from Rs {A_INV_OLD / A_JOBS_OLD:.2f} crore to Rs {A_INV_NEW / A_JOBS_NEW:.2f} crore (computed). The 2022&ndash;27 figures are the state&rsquo;s own objectives; the 2026&ndash;31 figures come from one trade outlet.",
         source="Government of Karnataka, Aerospace and Defence Policy 2022&ndash;27 (policy document, excerpt); Lok Sabha reply 566, 3 February 2026 (official); HR Katha, 10 September 2026 (secondary).")
    + numbers(["Item", "Value", "Source and status"],
              [["Approval", "Cabinet, Wednesday 9 September 2026; announced by Deputy Chief Minister G. Parameshwara; PTI dateline Bengaluru", "PTI via ThePrint, 9 September 2026 (page text read)"],
               ["Targets", "Rs 60,000 crore of investment and 60,000 jobs over five years", "HR Katha, 10 September 2026 (page text read; the other outlets in the search listing were not read)"],
               ["Incentives", "Zone 1 projects: 30% capital subsidy; other zones vary; non-focus areas up to 35%. The text does not explain why non-focus areas exceed Zone 1; space manufacturing is a focus sector with 25&ndash;30% investment incentives", "HR Katha; BusinessLine, 8 September 2026 (excerpt, IT secretary)"],
               ["Named projects", "Tata Advanced Systems to make 40 aircraft; Hindustan Aeronautics to make 97 Light Combat Aircraft (PTI); HR Katha describes a Tata aircraft-manufacturing facility", "PTI; HR Katha: the two differ in wording"],
               ["Prior policy", "2022&ndash;27: Rs 45,000 crore (USD 6 billion) and 60,000 jobs, in force from 26 August 2022 for five years or until a new policy", "Policy document; Lok Sabha reply 566"],
               ["Baseline", "Karnataka makes 67% of defence aircraft and helicopters and 25% of India&rsquo;s aircraft and spacecraft industry, per the state&rsquo;s own statements; the IT secretary says 65% of India&rsquo;s aerospace exports", "Industrial Policy 2025&ndash;30 (gazette, excerpt); BusinessLine, 8 September 2026 (excerpt)"],
               ["Same-day decisions", "A Rs 300 crore employment fund for 10 districts (Rs 2,500 per employee for two years) and the Shramika Nivasa housing scheme were approved the same day; they are not part of the aerospace policy", "HR Katha; PTI"],
               ["Name", "PTI: Karnataka Aerospace Policy 2026&ndash;31; BusinessLine: Aerospace &amp; Defence Policy 2026&ndash;31", "Not reconciled"]],
              "Show the aerospace figures and sources"),
    "The new policy raises the investment target by a third while keeping the jobs target of 2022&ndash;27, and no source gives the investment or jobs actually achieved under the earlier policy, so the new target has no measured base.",
    "The Commerce and Industries Department should publish the investment made and jobs created under the 2022&ndash;27 policy, alongside the 2026&ndash;31 targets.",
    "aerospace")

s4 = insight(
    "Marine biotechnology target is $6&ndash;8 billion by 2031, 3 to 4 times the $2 billion base",
    bars("Marine target: from about $2 billion to $6&ndash;8 billion by 2031, 3 to 4 times",
         [("Stated baseline, date not given", M_BASE), ("Target 2031, low end", M_LO), ("Target 2031, high end", M_HI)],
         accent="Target 2031, high end", unit="$ billion", vmax=9,
         sub=f"Blue bioeconomy value, USD billion. From a 2026 base the targets imply growth of {100 * ((M_LO / M_BASE) ** (1 / 5) - 1):.1f}% to {100 * ((M_HI / M_BASE) ** (1 / 5) - 1):.1f}% a year over five years (computed; the base year is not stated). The $2 billion also appears in Karnataka&rsquo;s 2020 bioeconomy report as the value of marine production.",
         source="ThePrint, 19 September 2026; The Hindu BusinessLine, 18 September 2026; Karnataka BioEconomy Report 2020 (Association of Biotechnology Led Enterprises, excerpt).")
    + numbers(["Item", "Value", "Source and status"],
              [["Approval", "Cabinet meeting in Mangaluru, Friday 18 September 2026; announced at the Bengaluru Tech Summit on 17 November 2026", "BusinessLine; GKToday; IASPoint (secondary)"],
               ["Budget", f"Rs {MAR_OUT} crore for five years, including KIMBE, marine biotechnology zones, the Seaweed Value Addition production-linked incentive and a blue carbon pilot; no amount for the incentive", "BusinessLine; ThePrint"],
               ["Jobs", f"About {J_TOTAL:,} direct and indirect (ThePrint); {J_TECH:,} technical and {J_COAST:,} coastal enterprise and livelihood opportunities (GKToday), which sum to the same total; Rs {MAR_OUT * 1e7 / J_TOTAL:,.0f} of budget per job targeted (computed)", "ThePrint; GKToday"],
               ["Fish production", f"{FISH_NOW} lakh tonnes in 2024-25 against {FISH_OLD} lakh tonnes in 2015-16, {100 * (FISH_NOW / FISH_OLD - 1):.1f}% higher (computed); fisheries are 0.48% of state GDP; about 1 million fishers in three coastal districts", "ThePrint, citing the Economic Survey 2025-26"],
               ["The $2 billion base", f"The 2020 report gives marine production of nearly 800,000 tonnes worth nearly $2 billion; 2024-25 production is {100 * (FISH_NOW / FISH_2020 - 1):.1f}% above that tonnage (computed). The base therefore looks like the value of marine production, and the policy documents read do not define it", "ABLE report 2020 (excerpt); inference by this blog"],
               ["Seaweed, recorded", f"Karnataka area under cultivation 0.04 hectares in 2020-21 to 2022-23 and nil in 2023-24 and 2024-25, which is {100 * SW_AREA / SW_POT:.4f}% of the {SW_POT:,} hectares identified as potential (computed)", "PIB, 10 February 2026; Takshashila, April 2026 (excerpts)"],
               ["Seaweed, approved", f"2020&ndash;25 approvals for Karnataka: 10,000 rafts and {SW_UNITS:,} monoline units with expected production of {SW_T:,} tonnes, {SW_T / SW_UNITS} tonne a unit (computed); the first trial of Kappaphycus at Uppunda in 2025 gave 180 kg from 20 net tubes in 72 days", "PIB, 10 February 2026; Indian Journal of Fisheries, 2025 (excerpts)"],
               ["Education", "Fisheries College at Mangaluru to be upgraded to a university with intake raised from 40 to 200; a search listing gives 60 to 200 (page not read)", "BusinessLine; listing title not reconciled"]],
              "Show the marine figures and baselines"),
    "The marine target is a tripling to quadrupling of a base that the policy does not date or define, and recorded seaweed cultivation in Karnataka is close to nil, so the target rests on activity the state does not yet measure.",
    "The Fisheries and Biotechnology Departments should define the $2 billion base, name its year and publish yearly seaweed area and production, so that the 2031 target can be tested.",
    "marine")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Department of Electronics, IT, BT and Science and Technology:</b> publish the approved data centre and marine policies with budget by component and the incentive rates, including the seaweed production-linked incentive amount.</li>
<li><b>Department of Electronics, IT and BT:</b> publish one dated series of installed and operational data centre capacity for the state, with the definition used.</li>
<li><b>Department of Commerce and Industries:</b> publish investment and jobs achieved under the Aerospace and Defence Policy 2022&ndash;27, and state whether the 2026&ndash;31 policy replaces it.</li>
<li><b>Department of Fisheries:</b> define the $2 billion marine base, give its year, and publish yearly seaweed area and production.</li>
<li><b>Karnataka Information and Public Relations Department:</b> release each cabinet decision with its budget in one dated note, so that headlines do not join separate budgets.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Approval dates come from reports of 9, 18 and 19 September 2026; weekdays were checked against the calendar (Wednesday 9 September, Friday 18 September).</li>
<li>A target is a goal stated for 2031 or for the policy period; an outcome is a measured result. No outcome for any of the three policies was found, and the baselines shown pre-date them.</li>
<li>Ratios, percentages, growth rates and per-job figures are computed here from the figures shown, and each is checked by an assertion in the builder.</li>
<li>The page text was read for ThePrint, the Deccan Chronicle, MediaNama, Dataquest, PTI, HR Katha, GKToday and IASPoint. Other sources, including the Hindu, Deccan Herald, PIB, Lok Sabha replies, the policy documents and the market reports, were read as search excerpts and are labelled. News and study-notes sites are secondary.</li>
<li>The cooling-water figure reuses this blog&rsquo;s data-centre cooling analysis, which treats 25&ndash;26 million litres per MW a year as a press and advocacy figure above the physical range, so the result is an upper bound.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The text of any of the three policies. Incentive rates for data centres and for marine biotechnology, the amount of the seaweed production-linked incentive, and any aerospace outlay were not found; a search excerpt mentioned a Rs 4,000 crore aerospace support figure from a page not read.</li>
<li>What the data centre budget of Rs 1,300.45 crore was &lsquo;revised&rsquo; from, and whether it is spending or a ceiling: the Deccan Chronicle says revised budget framework and Dataquest says proposed outlay.</li>
<li>One baseline for data centre capacity. Bengaluru figures run from 137 to 182 MW and the state figure is about 400 MW; an Anarock excerpt shows 137 MW in its text and 179 in an exhibit whose labels were unclear. The Deccan Herald of 18 July speaks of adding 1,000 MW over five years, while the approved text speaks of 1 GW cumulative; these differ by the existing capacity.</li>
<li>Whether 162 MW is a city or a state figure: The Hindu of 18 November calls it Karnataka&rsquo;s operational capacity, while the market reports give it for Bengaluru and the IT secretary put the state at about 400 MW in July.</li>
<li>Whether the 10&ndash;12% share of India&rsquo;s AI-ready capacity can be tracked: no source defines AI-ready capacity or gives the national total.</li>
<li>The investment and jobs achieved under the 2022&ndash;27 aerospace policy, and whether the 2026&ndash;31 policy replaces it before August 2027. The Economic Survey 2025-26 has an aerospace export row, but the year headings were not in the excerpt read, so it is not used.</li>
<li>Why the reports give 30% for Zone 1 and up to 35% for non-focus areas, and whether the 25&ndash;30% quoted for space manufacturing is inside or additional to it.</li>
<li>The year and definition of the $2 billion marine base; whether the seaweed incentive has been notified; whether the Fisheries College intake rises from 40 or from 60.</li>
<li>Whether any investment, application or job has followed from any of the three policies since approval.</li>
</ul></details>
'''

step(7, "assembling body")
body = STYLE + top + tvo + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://theprint.in/india/governance/karnataka-cabinet-approves-rs-1300-cr-data-centre-policy-pli-centred-blue-bioeconomy-roadmap/3047214/">ThePrint, 19 September 2026</a>, '
    '<a href="https://www.deccanchronicle.com/southern-states/karnataka/karnataka-approves-sustainable-data-centre-policy-20262031-1988661">Deccan Chronicle, 19 September 2026</a>, '
    '<a href="https://www.medianama.com/2026/09/223-karnataka-sustainable-data-centre-policy/">MediaNama, 21 September 2026</a> and '
    '<a href="https://www.dqindia.com/government-policy/karnataka-sustainable-compute-push-targets-1-gw-by-2031-12553738">Dataquest, 20 September 2026</a> (secondary; page text read: data centre policy); '
    '<a href="https://www.thehindubusinessline.com/economy/agri-business/karnataka-approves-marine-biotechnology-policy/article71481076.ece">The Hindu BusinessLine, 18 September 2026</a>, '
    '<a href="https://www.gktoday.in/karnataka-approves-marine-biotechnology-policy/">GKToday, 19 September 2026</a>, '
    '<a href="https://iaspoint.com/karnatakas-blueprint-for-blue-bioeconomy-growth/">IASPoint, 17 November 2026</a> and '
    '<a href="https://www.moneycontrol.com/news/business/karnataka-approves-marine-biotech-policy-targets-6-8-billion-blue-bioeconomy-by-2031-14033166.html">Moneycontrol, 18 September 2026</a> (secondary: marine policy); '
    '<a href="https://theprint.in/india/karnataka-cabinet-approves-aerospace-policy-shramika-nivas-housing-scheme/3038294/">PTI via ThePrint, 9 September 2026</a>, '
    '<a href="https://www.hrkatha.com/news/karnataka-approves-aerospace-policy-targeting-rs-60000-crore-investment-60000-jobs/">HR Katha, 10 September 2026</a> and '
    '<a href="https://www.thehindubusinessline.com/news/national/karnataka-targets-50-share-of-indias-22-billion-space-market-by-2034/article71442718.ece">The Hindu BusinessLine, 8 September 2026</a> (secondary: aerospace policy); '
    '<a href="https://investkarnataka.co.in/wp-content/uploads/2025/02/Karnataka-Aerospace-Defence-Policy-22-27_compressed.pdf">Karnataka Aerospace and Defence Policy 2022&ndash;27</a>, '
    '<a href="https://sansad.in/getFile/loksabhaquestions/annex/187/AU566_Qbd3Re.pdf?source=pqals">Lok Sabha reply 566, 3 February 2026</a>, '
    '<a href="https://industries.karnataka.gov.in/storage/pdf-files/IndustrialPolicy2025-2030Gazette.pdf">Karnataka Industrial Policy 2025&ndash;30</a> and '
    '<a href="https://des.karnataka.gov.in/uploads/Economic_Survey_2025-26_English_FinalMpdf_1772796504.pdf">Karnataka Economic Survey 2025-26</a> (official, excerpts); '
    '<a href="https://www.deccanherald.com/story/business/karnataka-eyes-rs-60k-crore-investment-under-new-data-centre-policy-4077831">Deccan Herald, 18 July 2026</a>, '
    '<a href="https://www.thehindu.com/news/national/karnataka/karnatakas-drive-to-green-data-centres/article71531272.ece">The Hindu, 2 October 2026</a> and '
    '<a href="https://www.thehindu.com/news/national/karnataka/karnataka-charts-1000-mw-roadmap-in-consultation-with-industry-stakeholders/article71716752.ece">The Hindu, 18 November 2026</a> (secondary, excerpts: data centre baselines); '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2241783&amp;reg=3&amp;lang=2">PIB, 18 March 2026</a> (official, excerpt); '
    '<a href="https://content.knightfrank.com/research/3111/documents/en/india-data-centre-market-update-2025-12895.pdf">Knight Frank, India Data Centre Market Update 2025</a>, '
    '<a href="https://www.nextmsc.com/industry-deep-dive/data-centre-capacity-by-indian-state">NextMSC, 10 October 2026</a>, '
    '<a href="https://www.ghar.tv/intelligence/bengaluru-data-centre-market-report-2026-capacity-land-water-ai-compute/artgi2436">GHAR.tv, October 2026</a> and '
    '<a href="https://websitemedia.anarock.com/media/Data_centre_The_blueprint_of_the_digital_fortress_in_India_2026_b36407b0b2.pdf">Anarock, August 2026</a> (market reports, excerpts); '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2225765&amp;lang=1&amp;reg=1">PIB, 10 February 2026</a>, '
    '<a href="https://takshashila.org.in/content/publications/assets/20260401-India-seaweed-opportunity.pdf">Takshashila, April 2026</a>, '
    '<a href="https://epubs.icar.org.in/index.php/IJF/article/download/169990/64401/507557">Indian Journal of Fisheries, 2025</a> and '
    '<a href="https://ableindia.in/manage/images/resourceuploads/_Karnataka%20BioEconomy%20Report%202020.pdf">Karnataka BioEconomy Report 2020</a> (seaweed and marine baselines, excerpts). '
    'Percentages, ratios and sums computed by this blog. Analysed 21 November 2026.')
RELATED = []

step(8, "writing page")
build("Policy &middot; Karnataka", TITLE,
      "Karnataka&rsquo;s cabinet approved aerospace, data centre and marine biotechnology policies in September 2026; this piece sets out each one&rsquo;s date, budget and targets, which rupee figure belongs to which decision, and what can be checked against a baseline.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(plain), "chars in title")
step(9, "complete")
