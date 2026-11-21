"""Karnataka Startup Policy 2025-2030: approval (Thursday 6 November 2025), Rs 518.27 crore outlay, the target of 25,000 new startups (10,000 outside Bengaluru),
the per-startup arithmetic, and dated progress data (Elevate, Elevate NxT, KITS registrations, DPIIT recognition, SISFS, venture commitments).
Build from the repo root:  python3 out/research/karnataka-startup-policy-2025-30/build.py            (writes out/post-karnataka-startup-policy-2025-30.html)
                           python3 out/research/karnataka-startup-policy-2025-30/build.py --check    (arithmetic and asserts only)
Every figure is from the source named beside it, or computed below with an assert. Analysed 21 November 2026.
The policy text was not found. Pages read in full: Entrepreneur India (8 Nov 2025), Dataquest (10 Nov 2025), YourStory (7 Nov 2025), NammaWard (26 Aug 2026, a report of
Legislative Council reply to starred question 530 of 20 Aug 2026). Others were read as search excerpts: PIB (17 Apr 2026), Lok Sabha reply 1446 (28 Jul 2026),
the Karnataka IT department document of July 2026, the Elevate 2025 and Elevate NxT 2026 pages of the Karnataka Startup Cell, and two Moneycontrol articles."""
import datetime as dt
import html as _h
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
OUT = ROOT / "out/post-karnataka-startup-policy-2025-30.html"
STEPS = 9


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. dates
step(1, "dates and weekday checks")
assert D(2025, 11, 6).strftime("%A") == "Thursday"        # YourStory, 7 Nov 2025: cabinet 'on Thursday'
assert D(2026, 1, 17).strftime("%A") == "Saturday"        # department document: policy 'unveiled on 17 January 2026' (launch, not approval)
assert (D(2026, 1, 17) - D(2025, 11, 6)).days == 72
assert D(2026, 8, 20).strftime("%A") == "Thursday"        # Legislative Council reply of 20 August 2026
assert D(2025, 11, 15).strftime("%A") == "Saturday"       # Elevate 2025 winners selected 15 Nov 2025 (nine days after approval)
assert D(2026, 6, 30) > D(2026, 3, 31)

# ---- 2. the per-startup figure
step(2, "per-startup arithmetic")
OUTLAY_CR, TARGET, YEARS, OUTSIDE = 518.27, 25_000, 5, 10_000
PER = OUTLAY_CR * 1e7 / TARGET                             # rupees per target startup
assert PER == 207_308.0 and f"{PER / 1e5:.2f}" == "2.07"
assert round(PER / YEARS) == 41_462 and f"{OUTLAY_CR / YEARS:.3f}" == "103.654"
assert OUTSIDE / TARGET == 0.4
CAP_PF, CAP_ELEV, CAP_NXT = 12, 50, 100                     # Rs lakh: PF and ESI reimbursement cap per startup; Elevate cap; Elevate NxT cap
assert CAP_ELEV * 1e5 / PER > 24 and f"{CAP_ELEV * 1e5 / PER:.1f}" == "24.1" and f"{CAP_NXT * 1e5 / PER:.1f}" == "48.2"
ALL_PF_CR = TARGET * CAP_PF * 1e5 / 1e7                      # if every target startup drew the full PF and ESI cap
assert ALL_PF_CR == 3_000.0 and f"{ALL_PF_CR / OUTLAY_CR:.1f}" == "5.8"
FOF = 500                                                    # Rs crore fund of funds 'proposed' (Dataquest, 10 Nov 2025)
assert f"{100 * FOF / OUTLAY_CR:.1f}" == "96.5" and round(OUTLAY_CR - FOF, 2) == 18.27
LEAP = 1000
assert f"{LEAP / OUTLAY_CR:.2f}" == "1.93"

# ---- 3. KITS registrations, Legislative Council reply of 20 August 2026 (via NammaWard)
step(3, "KITS registrations and consistency of the district table")
YRS = ["2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
ALL_DIST = [230, 415, 537, 699, 703]
BLR_URBAN = [168, 290, 334, 510, 511]
assert sum(ALL_DIST) == 2_584 and sum(BLR_URBAN) == 1_813
ROWS = {"Bengaluru Rural": [0, 12, 30, 27, 13, 82], "Mysuru": [10, 19, 18, 31, 33, 111], "Dharwad": [13, 15, 22, 15, 20, 85],
        "Dakshina Kannada": [8, 17, 21, 20, 16, 82], "Udupi": [5, 6, 11, 26, 6, 54], "Belagavi": [2, 17, 12, 12, 9, 52],
        "Kalaburagi": [5, 6, 21, 10, 7, 49], "Uttara Kannada": [0, 4, 4, 2, 11, 21], "Bidar": [2, 2, 5, 3, 9, 21]}
for k, r in ROWS.items():
    assert sum(r[:5]) == r[5], k                             # each printed district row sums to its total
assert all(ALL_DIST[i] >= BLR_URBAN[i] + sum(r[i] for r in ROWS.values()) for i in range(5))      # the nine named districts never exceed the all-district row
OUTSIDE_N = 2_584 - 1_813
assert OUTSIDE_N == 771 and f"{100 * OUTSIDE_N / 2_584:.1f}" == "29.8" and f"{100 * 1_813 / 2_584:.1f}" == "70.2"
OUT_25 = 703 - 511
assert OUT_25 == 192 and f"{100 * OUT_25 / 703:.1f}" == "27.3"
PACE = TARGET / YEARS
assert PACE == 5_000 and f"{100 * 703 / PACE:.1f}" == "14.1"

# ---- 4. DPIIT recognition and jobs (PIB 17 Apr 2026: Karnataka 22,600+ at 31 Mar 2026; Lok Sabha reply 1446: 24,026 at 30 Jun 2026)
step(4, "DPIIT recognition")
DP_MAR, DP_JUN = 22_600, 24_026                              # the March figure is printed as '22,600+', so the true value lies in 22,600 to 22,699
assert DP_JUN - DP_MAR == 1_426 and DP_JUN - 22_699 == 1_327
assert (DP_JUN - 22_699) * 4 == 5_308 and (DP_JUN - DP_MAR) * 4 == 5_704      # annualised pace of one quarter: 5,308 to 5,704 recognitions a year
JOBS_DPIIT = 246_000                                          # direct jobs, Karnataka startups recognised by DPIIT, 31 Mar 2026 ('2,46,000+')
assert f"{JOBS_DPIIT / DP_MAR:.1f}" == "10.9"
assert DP_JUN < TARGET and TARGET - DP_JUN == 974

# ---- 5. Elevate
step(5, "Elevate programmes")
APP25, ELIG25, FINAL25, WIN25 = 1_474, 1_398, 350, 103
assert f"{100 * WIN25 / APP25:.1f}" == "7.0" and APP25 > ELIG25 > FINAL25 > WIN25
NXT_APP, NXT_ELIG, NXT_PITCH, NXT_SEL, NXT_CR = 983, 824, 661, 33, 30
assert 524 + 165 + 135 == NXT_ELIG                            # Elevate NxT stage 2: Bengaluru district + beyond Bengaluru + beyond Karnataka
assert f"{100 * 165 / NXT_ELIG:.1f}" == "20.0" and f"{100 * NXT_SEL / NXT_APP:.1f}" == "3.4"
assert f"{NXT_CR * 100 / NXT_SEL:.1f}" == "90.9" and NXT_CR * 100 / NXT_SEL < CAP_NXT      # Rs lakh per startup, under the Rs 1 crore cap
assert f"{100 * 12 / NXT_SEL:.1f}" == "36.4"
E_N_2017, E_CR_2017 = 1_250, 292.57                           # since 2017 (IT department document, July 2026; Moneycontrol 2 Nov: Rs 293 crore)
E_N_2021, E_CR_2021 = 762, 175.94                             # since 2021, Idea2PoC (Council reply)
assert f"{E_CR_2017 * 100 / E_N_2017:.1f}" == "23.4" and f"{E_CR_2021 * 100 / E_N_2021:.1f}" == "23.1"      # Rs lakh per startup on both bases: consistent
E_MC = 1_084                                                  # Moneycontrol, 19 Nov 2026: 'supported 1,084 startups, including 390 beyond Bengaluru'
assert E_MC < E_N_2017 and E_N_2017 - E_MC == 166 and f"{100 * 390 / E_MC:.1f}" == "36.0"
assert WIN25 != 143                                           # Moneycontrol, 19 Nov 2026: 143 startups announced at the 2025 conclave; the portal lists 103 winners: not reconciled

# ---- 6. central scheme and venture commitments
step(6, "SISFS and venture commitments")
SIS_N, SIS_APP, SIS_DIS = 542, 104.87, 79.08
assert f"{100 * SIS_DIS / SIS_APP:.1f}" == "75.4"
VC_CR, VC_N = 1_050, 24
assert VC_CR / VC_N == 43.75

TITLE = "Karnataka Startup Policy 2025&ndash;30: Rs 518.27 crore for 25,000 startups, Rs 2.07 lakh each"
plain = _h.unescape(TITLE)
assert 55 <= len(plain) <= 90, len(plain)
assert not any(w in plain.lower().split() for w in ("you", "your", "we", "our"))
print(f"consistency checks passed (per-startup, KITS table, DPIIT, Elevate, SISFS); title {len(plain)} characters", flush=True)
if "--check" in sys.argv:
    sys.exit(0)

from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

def _rs(v, unit):
    s = f"{v:,.2f}".rstrip("0").rstrip(".")
    return f"Rs {s} {unit}"


step(7, "writing sections")
top = top_line([
    (f"Rs {PER / 1e5:.2f} lakh", f" is the policy outlay of Rs {OUTLAY_CR} crore divided by the target of {TARGET:,} new startups (Rs {PER:,.0f} each, about Rs {PER / YEARS:,.0f} a year); the grant caps per startup are Rs 12 lakh, Rs 50 lakh and Rs 1 crore, so the outlay cannot fund every target startup at a cap."),
    (f"{100 * OUTSIDE_N / 2_584:.1f}%", f" of the {2_584:,} startups registered with the state&rsquo;s Karnataka Innovation and Technology Society since 2021 are outside Bengaluru Urban, against a policy target of {100 * OUTSIDE / TARGET:.0f}% outside Bengaluru; the series ends in March 2026, four months after approval."),
    (f"{DP_JUN:,}", " is the number of Karnataka entities recognised as startups by the Union government on 30 June 2026; it counts every startup recognised since 2016, so it is not progress against a target of new startups, and no count of startups created under the policy was found."),
])

tvo = ('<table class="gb-table"><thead><tr><th>Kind</th><th>What this piece includes</th></tr></thead><tbody>'
       '<tr><td><b>Decided</b></td><td>Cabinet approval of the Karnataka Startup Policy 2025&ndash;2030 on Thursday 6 November 2025, with an outlay of Rs 518.27 crore; the policy was unveiled on 17 January 2026.</td></tr>'
       '<tr><td><b>Targets</b></td><td>25,000 new startups in five years, 10,000 of them outside Bengaluru; a proposed Rs 500 crore fund of funds.</td></tr>'
       '<tr><td><b>Outcomes found</b></td><td>Programme counts from before and after approval: Elevate selections, KITS registrations to March 2026, central recognition counts to June 2026. None is a count of startups created under the policy.</td></tr>'
       '<tr><td><b>Not found</b></td><td>The policy text, a spending figure against the Rs 518.27 crore, and a yearly count of new startups since approval.</td></tr>'
       '</tbody></table>\n')

s1 = insight(
    "Rs 518.27 crore across 25,000 startups is Rs 2.07 lakh each, or Rs 41,462 a year",
    bars("The outlay is Rs 2.07 lakh per target startup; the grant caps are 6 to 48 times that",
         [("Outlay per target startup (Rs 518.27 crore &divide; 25,000)", PER / 1e5), ("PF and ESI reimbursement cap per startup", CAP_PF),
          ("Elevate grant cap", CAP_ELEV), ("Elevate NxT grant cap", CAP_NXT)],
         accent="Outlay per target startup (Rs 518.27 crore &divide; 25,000)", unit=" lakh", fmt=lambda v: _rs(v, "lakh"), vmax=105,
         sub=f"Rs lakh per startup. The outlay per startup is computed here; the caps are those reported for the policy (PF and ESI Rs 3,000 per employee a month for two years, capped at Rs 12 lakh) and for the programmes. If every target startup drew the PF and ESI cap alone, the cost would be Rs {ALL_PF_CR:,.0f} crore, {ALL_PF_CR / OUTLAY_CR:.1f} times the outlay (computed).",
         source="Entrepreneur India, 8 November 2025; Dataquest, 10 November 2025; YourStory, 7 November 2025; Lok Sabha reply 1446, 28 July 2026 (official, excerpt). All outlay and cap figures are secondary reports of the policy.")
    + numbers(["Item", "Value", "Source and status"],
              [["Approval", "Cabinet, Thursday 6 November 2025; Minister Priyank Kharge; unveiled 17 January 2026", "YourStory, 7 November 2025; Karnataka IT department document, July 2026"],
               ["Outlay", f"Rs {OUTLAY_CR} crore over five years, Rs {OUTLAY_CR / YEARS:.2f} crore a year (computed)", "Entrepreneur India; Dataquest; YourStory"],
               ["Per startup", f"Rs {PER:,.0f} each, Rs {PER / YEARS:,.0f} a year (computed from 25,000 startups in five years)", "Computed; assert in builder"],
               ["Fund of funds", f"A Rs {FOF} crore fund of funds is &lsquo;proposed&rsquo;; it is {100 * FOF / OUTLAY_CR:.1f}% of the outlay. Whether it is inside the Rs {OUTLAY_CR} crore is not stated; if it were, Rs {OUTLAY_CR - FOF:.2f} crore would remain for every other measure. On 20 August 2026 the government said a Rs 200 crore fund of funds under the Local Economy Accelerator Programme (LEAP) is not yet established", "Dataquest, 10 November 2025; Council reply via NammaWard, 26 August 2026: the two amounts conflict"],
               ["Other measures", "Capital grant up to Rs 50 lakh (up to 50% of fixed cost) for private incubators; support for cloud costs and research; Beyond Bengaluru Cluster Seed Fund; Elevate NxT for deeptech", "Dataquest; Entrepreneur India"],
               ["LEAP", f"Rs {LEAP:,} crore over five years, {LEAP / OUTLAY_CR:.2f} times the policy outlay (computed); 5 lakh jobs; the relationship to the Rs {OUTLAY_CR} crore is not stated; the reply names eight cities, the Startup Cell page six clusters", "Council reply via NammaWard; Startup Cell page (excerpt)"]],
              "Show the policy figures and sources"),
    f"The outlay is Rs {PER / 1e5:.2f} lakh per target startup, and the caps on individual support are many times that, so the policy can fund only a share of the 25,000 startups at the stated rates.",
    "The IT and BT Department should publish how the Rs 518.27 crore is divided between the fund of funds, grants, reimbursements and infrastructure, and what is spent each year.",
    "perstartup")

s2 = insight(
    "Outside Bengaluru: 40% target against 29.8% of state registrations since 2021",
    bars("Outside Bengaluru: 40% target, 29.8% of KITS registrations, 43% of Elevate 2025 winners",
         [("Policy target: startups outside Bengaluru", 100 * OUTSIDE / TARGET), ("KITS registrations outside Bengaluru Urban, 2021-22 to 2025-26", round(100 * OUTSIDE_N / 2_584, 1)),
          ("KITS registrations outside Bengaluru Urban, 2025-26 alone", round(100 * OUT_25 / 703, 1)), ("Elevate supported since 2017, beyond Bengaluru (Moneycontrol, 2 Nov 2026)", 37),
          ("Elevate 2025 winners beyond Bengaluru (Startup Cell page)", 43)],
         accent="KITS registrations outside Bengaluru Urban, 2021-22 to 2025-26", unit="%", vmax=50,
         sub=f"Per cent. The registration shares are computed from the district table of a Legislative Council reply of 20 August 2026: {OUTSIDE_N} of 2,584, and {OUT_25} of 703 in 2025-26 (the financial year that ended four months after approval). Registration with the state society is not the policy&rsquo;s own count of new startups.",
         source="Karnataka Legislative Council starred question 530, answered 20 August 2026, via NammaWard, 26 August 2026 (secondary); Karnataka Startup Cell, Elevate 2025 page (excerpt); Moneycontrol, 2 November 2026 (excerpt).")
    + numbers(["Item", "Value", "Source and status"],
              [["KITS registrations by year", f"{ALL_DIST[0]}, {ALL_DIST[1]}, {ALL_DIST[2]}, {ALL_DIST[3]}, {ALL_DIST[4]} from 2021-22 to 2025-26; total {sum(ALL_DIST):,} (sum checked)", "Council reply via NammaWard (secondary; the annexure was not read)"],
               ["Bengaluru Urban", f"{sum(BLR_URBAN):,} of 2,584, {100 * 1_813 / 2_584:.1f}%; {BLR_URBAN[4]} of {ALL_DIST[4]} in 2025-26", "Same; computed shares"],
               ["Named districts", "Mysuru 111; Dharwad 85; Bengaluru Rural 82; Dakshina Kannada 82; Udupi 54; Belagavi 52; Kalaburagi 49; Uttara Kannada 21; Bidar 21; each row sums to its total (checked)", "Same"],
               ["Jobs", "More than 7,000 jobs estimated for the 2,584 registered startups", "Council reply via NammaWard (the government&rsquo;s own estimate)"],
               ["Elevate, beyond Bengaluru", f"Moneycontrol of 2 November: more than 37% of 1,250 supported; Moneycontrol of 19 November: 390 of {E_MC:,} supported, {100 * 390 / E_MC:.1f}% (computed); the two totals differ by {E_N_2017 - E_MC}", "Moneycontrol (excerpts): not reconciled"],
               ["Elevate NxT 2026 applicants", f"Of {NXT_ELIG} applicants that qualified at stage 2, 524 were from Bengaluru district, 165 from beyond Bengaluru ({100 * 165 / NXT_ELIG:.1f}%) and 135 from beyond Karnataka (sum checked)", "Startup Cell, Elevate NxT 2026 page (excerpt)"],
               ["Beyond Bengaluru programmes", "LEAP of Rs 1,000 crore; four of six centres of excellence outside Bengaluru reported set up; the reply does not name which four; Rs 200 crore fund of funds not yet established; bootcamp institutions still being selected (20 August 2026)", "Council reply via NammaWard"]],
              "Show the Beyond Bengaluru figures and checks"),
    "The state&rsquo;s own registration series puts about 30% of startups outside Bengaluru Urban against a 40% target, and the series ends in March 2026, so it measures the base the policy started from rather than its results.",
    "The Karnataka Startup Cell should publish yearly registrations by district from April 2026 on the same basis as the 2021&ndash;26 table, with the share outside Bengaluru, so that the 10,000 target can be tracked.",
    "beyond")

s3 = insight(
    "KITS registrations reached 703 in 2025-26; the policy pace is 5,000 new startups a year",
    bars("Yearly KITS registrations rose to 703 in 2025-26; 25,000 over five years is 5,000 a year",
         [(y, v) for y, v in zip(YRS, ALL_DIST)] + [("Policy pace: 25,000 &divide; 5 years", PACE)],
         accent="Policy pace: 25,000 &divide; 5 years", unit="", vmax=5_200,
         sub=f"Startups registered a year with the Karnataka Innovation and Technology Society, all 31 districts. 703 is {100 * 703 / PACE:.1f}% of the policy pace (computed). The measures differ: the pace counts new startups of any kind, the series counts registrations with one state society, so the comparison shows scale, not shortfall.",
         source="Karnataka Legislative Council starred question 530, answered 20 August 2026, via NammaWard, 26 August 2026 (secondary).")
    + numbers(["Item", "Value", "Source and status"],
              [["DPIIT recognition, Karnataka", f"22,600+ at 31 March 2026 and {DP_JUN:,} at 30 June 2026; the difference is {DP_JUN - DP_MAR:,} at most and {DP_JUN - 22_699:,} at least because the March figure is rounded down (computed)", "PIB, 17 April 2026; Lok Sabha reply 1446, 28 July 2026 (official, excerpts)"],
               ["Annualised pace", f"One quarter&rsquo;s change multiplied by four is {(DP_JUN - 22_699) * 4:,} to {(DP_JUN - DP_MAR) * 4:,} recognitions a year (computed), near the 5,000 a year pace; recognition is not creation, since older startups can register at any time", "Computed; one quarter only"],
               ["Gap to the target", f"{TARGET - DP_JUN} below 25,000, but 25,000 is a target of new startups and {DP_JUN:,} is a cumulative total since 2016", "Computed"],
               ["Direct jobs", f"2,46,000+ direct jobs in Karnataka&rsquo;s recognised startups at 31 March 2026, about {JOBS_DPIIT / DP_MAR:.1f} a startup (computed from two rounded figures)", "PIB, 17 April 2026"],
               ["Baseline before the policy", "Reports give over 18,000 registered startups (Dataquest, November 2025), over 14,000 (Startup Cell page, undated) and over 15,000 nurtured under the 2015 and 2022 frameworks (Entrepreneur India); none matches the March 2026 recognition count, so no growth since approval is computed", "Reports differ in measure and date"],
               ["Central seed fund, Karnataka", f"{SIS_N} startups selected under the Startup India Seed Fund Scheme, Rs {SIS_APP} crore approved and Rs {SIS_DIS} crore disbursed to 30 June 2026, {100 * SIS_DIS / SIS_APP:.1f}% (computed); this is a central scheme, not the state policy", "Lok Sabha reply 1446 (excerpt)"]],
              "Show the registration and recognition figures"),
    "The state series and the central count do not share a definition with the target of 25,000 new startups, so neither shows how many startups the policy has produced since November 2025.",
    "The IT and BT Department should define a startup for the target, state which registry counts it, and publish the count at approval and each quarter since.",
    "counts")

s4 = insight(
    "Elevate 2025 selected 103 startups from 1,474 applications; Elevate NxT 2026 selected 33",
    bars("Elevate 2025 narrowed 1,474 applications to 103 winners, a selection rate of 7.0%",
         [("Applications", APP25), ("Qualified after eligibility checks", ELIG25), ("Pitched at the grand finale", FINAL25), ("Winners selected on 15 November 2025", WIN25)],
         accent="Winners selected on 15 November 2025", unit="", vmax=1_500,
         sub=f"Startups at each stage of the Elevate 2025 call (grant up to Rs 50 lakh); 43% of winners were from beyond Bengaluru and 43% were women-led, as published. The 2026 deeptech call, Elevate NxT, drew {NXT_APP} applications, and {NXT_SEL} startups were selected with Rs {NXT_CR} crore sanctioned, Rs {NXT_CR * 100 / NXT_SEL:.1f} lakh each on average (computed), {100 * NXT_SEL / NXT_APP:.1f}% of applications.",
         source="Karnataka Startup Cell, Elevate 2025 page (excerpt); Karnataka Startup Cell, Elevate NxT 2026 page (excerpt); Council reply via NammaWard, 26 August 2026 (secondary).")
    + numbers(["Item", "Value", "Source and status"],
              [["Elevate since 2017", f"{E_N_2017:,} startups and about Rs {E_CR_2017} crore committed, Rs {E_CR_2017 * 100 / E_N_2017:.1f} lakh a startup (computed); Moneycontrol of 2 November gives Rs 293 crore and more than 37% beyond Bengaluru, nearly 20% women-led", "Karnataka IT department document, July 2026; Moneycontrol, 2 November 2026 (excerpts)"],
               ["Elevate since 2021", f"{E_N_2021} startups selected and Rs {E_CR_2021} crore allocated, Rs {E_CR_2021 * 100 / E_N_2021:.1f} lakh a startup (computed), consistent with the since-2017 average", "Council reply via NammaWard"],
               ["Conflict: totals", f"Moneycontrol of 19 November says Elevate had supported {E_MC:,} startups, {E_N_2017 - E_MC} fewer than {E_N_2017:,}; the dates and scope behind each total are not given", "Moneycontrol, 19 November 2026 (excerpt): not reconciled"],
               ["Conflict: 2025 cohort", "The Startup Cell page lists 103 winners; Moneycontrol of 19 November says 143 startups were announced at the 2025 conclave; the 143 may include other tracks, which the excerpt does not say", "Startup Cell page; Moneycontrol: not reconciled"],
               ["Elevate NxT 2026 funnel", f"{NXT_APP} applications, {NXT_ELIG} qualified, {NXT_PITCH} pitched in person, {NXT_SEL} selected with Rs {NXT_CR} crore (12 women-led, {100 * 12 / NXT_SEL:.1f}%, computed); up to Rs 1 crore each", "Startup Cell page; Moneycontrol, 2 November 2026; Council reply"],
               ["Venture commitments", f"24 venture capital firms announced Rs {VC_CR:,} crore of investment commitments for Karnataka deeptech startups at the Future Makers Conclave on 19 November 2026; commitments, not disbursements, and the period is not stated", "Moneycontrol, 19 November 2026 (excerpt)"],
               ["Other state funds", "KITVEN Fund-5 began with Rs 100 crore for deeptech; Rs 225 crore sanctioned since 2021 for 13 centres of excellence; Rs 170 crore and more of support to startups on the Startup Cell page (undated)", "Council reply via NammaWard; Startup Cell page"]],
              "Show the Elevate figures and conflicts"),
    "Elevate funds about 7% of applicants in a call and Elevate NxT about 3%, at an average near Rs 23 lakh for the older programme and Rs 91 lakh for the new one, and the two cohort counts reported for 2025 differ.",
    "The Startup Cell should publish each Elevate call&rsquo;s winners, grant amounts and amounts actually released, with the cohort count agreed across all its announcements.",
    "elevate")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Department of Electronics, IT and BT:</b> publish the policy text and the split of the Rs 518.27 crore by measure, stating whether the Rs 500 crore fund of funds is inside it.</li>
<li><b>Karnataka Startup Cell:</b> define a startup for the 25,000 target, name the registry that counts it, and publish the count at approval and each quarter since.</li>
<li><b>Karnataka Startup Cell:</b> publish yearly district-wise registrations from April 2026 on the 2021&ndash;26 basis, with the share outside Bengaluru against the 40% target.</li>
<li><b>Karnataka Startup Cell:</b> publish for each Elevate call the winners, grant sanctioned and amount released, and reconcile the cohort counts given in different announcements.</li>
<li><b>Department of Electronics, IT and BT:</b> state how the Rs 1,000 crore LEAP, the Rs 200 crore and Rs 500 crore funds of funds and the Rs 518.27 crore outlay relate to one another.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The approval date is the Thursday before YourStory&rsquo;s report of Friday 7 November 2025; the policy was unveiled on 17 January 2026, 72 days later, according to a department document.</li>
<li>The per-startup figure divides Rs 518.27 crore by 25,000 and is checked by an assertion; it is an average of an outlay, not a grant any startup receives.</li>
<li>Percentages, ratios and sums are computed here from the figures shown; each is checked by an assertion in the builder, and the district table was checked for row and column sums.</li>
<li>A target is a goal for 2030; a registration or recognition count is an outcome of a registry, not of the policy. The 22,600+ and 2,46,000+ figures are printed with a plus sign and are treated as lower bounds.</li>
<li>Page text was read for Entrepreneur India, Dataquest, YourStory and NammaWard. The NammaWard article reports a written Legislative Council reply; the reply itself and its annexure were not read. Official pages, the Lok Sabha reply, PIB and Moneycontrol were read as search excerpts. News sites are secondary.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The text of the policy, and with it the split of the Rs 518.27 crore by measure and any spending against it. Whether the proposed Rs 500 crore fund of funds is inside the outlay is not stated, and the government told the Council on 20 August 2026 that a Rs 200 crore fund of funds under LEAP had not been set up.</li>
<li>How many startups the policy has created since approval. No count by the policy&rsquo;s own definition was found; the KITS series ends in March 2026 and the central series counts recognitions since 2016.</li>
<li>Whether the target of 25,000 new startups counts registrations, recognitions or something else, and whether the 10,000 outside Bengaluru is a cap, a floor or a share.</li>
<li>A baseline at approval. Reports give over 18,000, over 14,000 and over 15,000 startups on different bases, and the central count was 22,600+ in March 2026.</li>
<li>Why Elevate totals differ (1,250 and 1,084) and why the 2025 cohort is 103 on the Startup Cell page and 143 in a news report.</li>
<li>Jobs created by policy beneficiaries. The 7,000-plus estimate covers the 2,584 registered startups and the 2,46,000-plus covers all recognised startups; neither is limited to policy support.</li>
<li>Funds actually released: the Rs 1,050 crore of venture commitments of 19 November 2026 are commitments, and grant releases against sanctions were not found.</li>
<li>How LEAP&rsquo;s Rs 1,000 crore relates to the policy outlay, and which cities it covers: the reply lists eight, the Startup Cell page six clusters.</li>
</ul></details>
'''

step(8, "assembling body and page")
body = STYLE + top + tvo + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://www.entrepreneur.com/en-in/news-and-trends/karnataka-cabinet-approves-startup-policy-2025-2030-with/499357">Entrepreneur India, 8 November 2025</a>, '
    '<a href="https://www.dqindia.com/news/karnataka-targets-25000-startups-with-rs-518-crore-policy-10642944">Dataquest, 10 November 2025</a> and '
    '<a href="https://yourstory.com/2025/11/karnataka-new-startup-policy-targets-10-000-ventures-outside-bengaluru">YourStory, 7 November 2025</a> (secondary; page text read: the policy); '
    '<a href="https://nammaward.in/wardpulse/government-says-bengaluru-urban-has-1-813-of-2-584-startups">NammaWard, 26 August 2026</a> (secondary; a report of Karnataka Legislative Council starred question 530, answered 20 August 2026; the reply was not read); '
    '<a href="https://eitbt.karnataka.gov.in/startup/public/141/elevate-2025-winners/en">Karnataka Startup Cell, Elevate 2025 winners</a>, '
    '<a href="https://eitbt.karnataka.gov.in/startup/public/157/elevate-nxt-2026-winners/en">Karnataka Startup Cell, Elevate NxT 2026</a> and '
    '<a href="https://eitbt.karnataka.gov.in/uploads/media_to_upload1785224806.pdf">Karnataka IT, BT and S&amp;T department document, July 2026</a> (official, excerpts); '
    '<a href="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU1446_N4i3CT.pdf">Lok Sabha unstarred question 1446, 28 July 2026</a> and '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2253019&amp;lang=2&amp;reg=48">PIB, 17 April 2026</a> (official, excerpts); '
    '<a href="https://www.moneycontrol.com/news/business/rs-1-000-cr-leap-25-000-startups-karnataka-s-big-push-to-build-innovation-hubs-beyond-bengaluru-14066148.html">Moneycontrol, 2 November 2026</a> and '
    '<a href="https://www.moneycontrol.com/news/business/startup/karnataka-s-deeptech-startups-attract-rs-1-050-crore-investment-commitments-from-24-vcs-14084909.html">Moneycontrol, 19 November 2026</a> (secondary, excerpts). '
    'Percentages, ratios and sums computed by this blog. Analysed 21 November 2026.')
RELATED = []

build("Policy &middot; Karnataka", TITLE,
      "Karnataka&rsquo;s Startup Policy 2025&ndash;2030 has an outlay of Rs 518.27 crore and a target of 25,000 new startups; this piece computes the per-startup figure, sets out the dated progress data, and lists what the sources do not show.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(plain), "chars in title")
step(9, "complete")
