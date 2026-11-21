"""Andhra Pradesh cabinet of Tuesday 10 November 2026: the AVGC-XR Policy 2026-31, the Robotics and Physical AI Policy 2026-36 and the amendment to the
Semiconductor and Display Fab Policy 4.0, with the investment items cleared the same day, the 512 MW AI data centre and its peers per MW.
Build from the repo root:  python3 out/research/andhra-pradesh-cabinet-2026-11-10/build.py            (writes out/post-andhra-pradesh-cabinet-10-november-2026.html)
                           python3 out/research/andhra-pradesh-cabinet-2026-11-10/build.py --check    (arithmetic and asserts only)
Every figure is from the source named beside it, or computed below with an assert. Analysed 21 November 2026.
Pages read in full: The New Indian Express (11 Nov), Deccan Chronicle (10 Nov), Telugu360 (10 Nov), GKToday (11 Nov), BusinessLine (18 Nov), tele.net (19 Nov).
Search excerpts only: The Hindu (10 and 16 Nov), Times of India (10 and 17 Nov), ETV Bharat (17 Nov), Hans India (17 Nov), Elets (11 Nov), Peepals (10 Nov),
MediaNama (24 Aug), The New Indian Express (24 Aug), Economic Times Manufacturing (28 Apr), and the text of G.O.Ms.No.59 of 22 Aug 2026 as hosted by a third party.
None of the three policy documents or G.O.Ms.No.87 itself was found; the post says so."""
import datetime as dt
import html as _h
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
OUT = ROOT / "out/post-andhra-pradesh-cabinet-10-november-2026.html"
STEPS = 9


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. dates
step(1, "dates and weekday checks")
for d, wd in [(D(2026, 11, 10), "Tuesday"), (D(2026, 11, 16), "Monday"), (D(2026, 11, 17), "Tuesday"), (D(2026, 11, 18), "Wednesday"), (D(2026, 11, 12), "Thursday")]:
    assert d.strftime("%A") == wd, d
assert (D(2026, 11, 16) - D(2026, 11, 10)).days == 6          # G.O.Ms.No.87 and the robotics order are dated 16 Nov, six days after the cabinet
assert (D(2026, 11, 10) - D(2026, 8, 22)).days == 80          # G.O.Ms.No.59 (AM AI Factory, 512 MW) is dated 22 Aug 2026, 80 days before the cabinet item
assert (D(2026, 8, 12) - D(2026, 7, 28)).days == 15           # consultative committee 28 Jul to investment board 12 Aug

# ---- 2. investment items cleared on 10 November (TNIE 11 Nov; Deccan Chronicle 10 Nov; TOI headline Rs 37,000 crore)
step(2, "investment items and the Rs 37,000 crore headline")
ITEMS = [("AM Intelligence: 512 MW AI data centre, Bheemunipatnam", 31_387.00, 1_000), ("Carbon Cosmo: LFP cathode complex, Naidupeta", 4_000.20, 700),
         ("Dixon Technologies: land allotment, Tirupati", 700.00, 2_300), ("Epack: AI data centre equipment unit, Rambilli", 570.20, 2_565),
         ("Ravali Spinners: expansion, West Godavari", 236.92, 1_569)]
TOTAL = round(sum(i[1] for i in ITEMS), 2)
assert TOTAL == 36_894.32
assert f"{100 * (37_000 - TOTAL) / 37_000:.2f}" == "0.29"                       # within 0.3% of the Times of India's Rs 37,000 crore
assert f"{100 * ITEMS[0][1] / TOTAL:.1f}" == "85.1"
JOBS_ALL = sum(i[2] for i in ITEMS)
assert JOBS_ALL == 8_134
REST_INV, REST_JOBS = round(TOTAL - ITEMS[0][1], 2), JOBS_ALL - ITEMS[0][2]
assert REST_INV == 5_507.32 and REST_JOBS == 7_134
assert f"{REST_INV / REST_JOBS:.2f}" == "0.77" and f"{ITEMS[0][1] / ITEMS[0][2]:.1f}" == "31.4"     # Rs crore per job: other four against the data centre
PER_JOB = [round(i[1] / i[2], 2) for i in ITEMS]
assert PER_JOB == [31.39, 5.71, 0.30, 0.22, 0.15]

# ---- 3. semiconductor amendment (BusinessLine 18 Nov; tele.net 19 Nov): the stack of percentages must be internally consistent
step(3, "semiconductor incentive stack")
assert 40 + 40 == 80 and 80 <= 90                                    # silicon fab: Centre 40% + State 40% = 80%, under the all-source cap of 90%
assert 40 <= 50                                                      # State's 40% is under the State cap of 50% of eligible fixed capital
assert 9 + 4.5 == 13.5 and 4.5 / 9 == 0.5                            # deployment-linked incentive: State adds half of the Centre's 9%
assert 30 + 18 == 48 and 18 / 30 == 0.6                              # machines and materials: State adds 60% of the Centre's 30%
assert 15 + 7.5 == 22.5 and 7.5 / 15 == 0.5                          # design seed: State Rs 7.5 crore is half of the Centre's Rs 15 crore, total Rs 22.5 crore
assert 450e6 / 1e7 == 45 and 1.8e9 / 1e7 == 180                      # tele.net prints Rs 450 million and Rs 1.8 billion: the same caps as Rs 45 crore and Rs 180 crore
assert 225e6 / 1e7 == 22.5 and 75e6 / 1e7 == 7.5
assert 10_000 * 6 == 60_000                                          # training subsidy Rs 10,000 a trainee a month for six months
# tele.net's Rs 10 billion to Rs 50 billion mega band is Rs 1,000 crore to Rs 5,000 crore
assert 10e9 / 1e7 == 1_000 and 50e9 / 1e7 == 5_000
STATES = [("Andhra Pradesh", 80), ("Odisha", 65), ("Tamil Nadu", 65), ("Uttar Pradesh", 60), ("Madhya Pradesh", 60), ("Gujarat", 56)]
assert [s[1] for s in STATES] == sorted((s[1] for s in STATES), reverse=True)
assert 80 - 65 == 15 and f"{80 / 56:.2f}" == "1.43"
PARK_ACRES_BL, PARK_ACRES_HANS = 5_000, 495                           # BusinessLine 'about 5,000 acres' against Hans India 'proposed 495-acre' park: a conflict
assert PARK_ACRES_BL / PARK_ACRES_HANS > 10
SP_INV, SP_JOBS = 20_000, 12_500                                      # Hans India: Reddipalle park Rs 20,000 crore, 12,500 jobs by 2029
assert SP_INV / SP_JOBS == 1.6

# ---- 4. AVGC-XR, robotics: targets and per-job ratios
step(4, "AVGC-XR and robotics")
AV_INV, AV_JOBS = 5_000, 100_000                                      # Rs crore, jobs: ETV Bharat and Times of India, 17 Nov
assert AV_INV * 1e7 / AV_JOBS == 500_000                              # Rs 5 lakh a job
assert 5 + 100 == 105 and f"{AV_INV / 105:.1f}" == "47.6"             # five anchor units and 100 companies
assert AV_JOBS / 2_000_000 == 0.05                                    # one lakh against Hans India's 20 lakh professionals needed by 2030
RB_INV, RB_JOBS = 3_536, 18_750                                       # Gudipalli robotics park (Hans India)
assert f"{RB_INV * 100 / RB_JOBS:.2f}" == "18.86"                     # Rs lakh a job
assert 132 / 6 == 22.0                                                # world average robot density against India's, per 10,000 manufacturing workers
DCP_INV, DCP_JOBS = 215_000, 6_240                                    # Anakapalli AI data centre park (Hans India)
assert f"{DCP_INV * 1e7 / DCP_JOBS / 1e5:.1f}" == "3445.5"            # Rs lakh a job
assert f"{ITEMS[0][1] * 1e7 / ITEMS[0][2] / 1e5:.1f}" == "3138.7"
LAKH_PER_JOB = {"AVGC-XR policy target": AV_INV * 1e7 / AV_JOBS / 1e5, "Robotics park, Gudipalli": RB_INV * 1e7 / RB_JOBS / 1e5,
                "Semiconductor park, Tirupati": SP_INV * 1e7 / SP_JOBS / 1e5, "AM Intelligence data centre": ITEMS[0][1] * 1e7 / ITEMS[0][2] / 1e5,
                "AI data centre park, Anakapalli": DCP_INV * 1e7 / DCP_JOBS / 1e5}
assert [round(v, 1) for v in LAKH_PER_JOB.values()] == [5.0, 18.9, 160.0, 3138.7, 3445.5]

# ---- 5. data centre approvals per MW (G.O.Ms.No.59; MediaNama 24 Aug; TNIE 24 Aug; ET 28 Apr)
step(5, "data centre cost per MW")
DC = [("AM AI Factory (Vizag), 512 MW", 31_387, 512, 1_000), ("Reliance, giga-scale (1,500 MW per ET)", 108_010, 1_500, None),
      ("Renew AP Green Data Center, Anakapalli (1,000 MW)", 85_200, 1_000, None), ("Data Centre Holdings India, 486 MW", 58_743, 486, 1_250)]
assert 58_743 + 31_387 + 108_010 + 85_200 == 283_340                  # the sum MediaNama prints for the four approvals
assert 486 + 512 + 1_000 + 1_500 == 3_498                             # the capacity MediaNama prints; the 85,200 and 1,000 are inferred from this and the TNIE total
assert abs((58_743 + 85_200) - 144_000) / 144_000 < 0.002              # TNIE: two August orders together Rs 1.44 lakh crore and 1,486 MW
assert 486 + 1_000 == 1_486
PER_MW = [round(c / m, 1) for _, c, m, _ in DC]
assert PER_MW == [61.3, 72.0, 85.2, 120.9]
assert f"{58_743 / 486 / (31_387 / 512):.2f}" == "1.97"
assert f"{100 * 3_498 / 15_016:.1f}" == "23.3"       # of the state's record peak load, as MediaNama says
assert f"{100 * 3_498 / 6_000:.1f}" == "58.3"                        # against the 6 GW hosting target the IT minister gave in September 2025 (ET)
assert 5_600 < 6_000                                                  # MoUs totalling 5.6 GW (ET, April 2026) are below the 6 GW target
KA_PER_MW = 60                                                       # Karnataka officials, about Rs 60 crore a MW (Deccan Herald, 18 Jul 2026)
assert f"{61.3 / KA_PER_MW:.2f}" == "1.02"
assert f"{1_000 / 512:.2f}" == "1.95" and f"{1_250 / 486:.2f}" == "2.57"
CAPS_RENEW = [3_700, 5_000, 2_500, 3_000, 200, 5]
assert sum(CAPS_RENEW) == 14_405 and f"{100 * 14_405 / 85_200:.1f}" == "16.9"
assert 1_800 / 0.10 == 18_000

TITLE = "Andhra Pradesh cabinet 10 Nov 2026: three technology policies, Rs 36,894 crore of projects"
plain = _h.unescape(TITLE)
assert 55 <= len(plain) <= 90, len(plain)
assert not any(w in plain.lower().split() for w in ("you", "your", "we", "our"))
print(f"consistency checks passed (items, semiconductor stack, per-job, per-MW); title {len(plain)} characters", flush=True)
if "--check" in sys.argv:
    sys.exit(0)

from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402


def _rs(v, unit, dec=None):
    """Rs figure; dec=2 keeps the source's two decimals (4,000.20), otherwise trailing zeros are dropped."""
    s = f"{v:,.2f}"
    if dec is None:
        s = s.rstrip("0").rstrip(".")
    elif float(v).is_integer():
        s = f"{v:,.0f}"
    return f"Rs {s} {unit}"


step(6, "writing sections")
top = top_line([
    (f"{100 * ITEMS[0][1] / TOTAL:.1f}%", f" of the Rs {TOTAL:,.2f} crore of investment items cleared on 10 November 2026 is one 512 MW AI data centre (Rs 31,387 crore, 1,000 jobs); the other four items carry {REST_JOBS:,} of the {JOBS_ALL:,} jobs."),
    ("80%", f" is the combined Centre and State capital support for a silicon fab under the amended semiconductor policy, against 65% in Odisha and Tamil Nadu and 56% in Gujarat on the State&rsquo;s own comparison; no project approved under it was found."),
    (f"Rs {PER_MW[0]} crore", f" per MW is the cost of the 512 MW data centre, the lowest of four approved Andhra Pradesh projects, which run to Rs {PER_MW[3]} crore a MW."),
])

tvo = ('<table class="gb-table"><thead><tr><th>Kind</th><th>What this piece includes</th></tr></thead><tbody>'
       '<tr><td><b>Decided</b></td><td>On Tuesday 10 November 2026 the cabinet approved the AVGC-XR Policy 2026&ndash;31, the Robotics and Physical AI Policy 2026&ndash;36 and amendments to the Semiconductor and Display Fab Policy 4.0, plus five investment items; government orders followed on 16 and 17 November.</td></tr>'
       '<tr><td><b>Targets</b></td><td>AVGC-XR: Rs 5,000 crore and one lakh jobs in five years. Robotics park: Rs 3,536 crore and 18,750 jobs. Semiconductor park: Rs 20,000 crore and 12,500 jobs by 2029. Projections from reports and a feature article, not from policy text.</td></tr>'
       '<tr><td><b>Outcomes</b></td><td>None found. No fab, robotics unit or AVGC-XR studio has been reported as approved under the new rules.</td></tr>'
       '<tr><td><b>Not found</b></td><td>The text of the three policies and of G.O.Ms.No.87, a robotics policy investment or jobs target, and the incentive terms for the 512 MW project beyond press summaries.</td></tr>'
       '</tbody></table>\n')

s1 = insight(
    "One data centre is 85.1% of the Rs 36,894 crore of projects cleared on 10 November",
    bars("One data centre is 85.1% of the Rs 36,894 crore of projects cleared on 10 November",
         [(i[0], i[1]) for i in ITEMS], accent=ITEMS[0][0], unit=" crore", fmt=lambda v: _rs(v, "crore", 2), vmax=33_000,
         sub=f"Rs crore of proposed investment. The five items sum to Rs {TOTAL:,.2f} crore (computed), within 0.3% of the Rs 37,000 crore in the Times of India headline. Investment per job targeted is Rs {PER_JOB[0]} crore at the data centre and Rs {REST_INV / REST_JOBS:.2f} crore across the other four (computed).",
         source="The New Indian Express, 11 November 2026; Deccan Chronicle, 10 November 2026; Times of India, 10 November 2026 (headline only, excerpt). Secondary.")
    + flow([("22 Aug 2026", "G.O.Ms.No.59 approves the 512 MW AI data centre for AM AI Factory (Vizag) Private Limited with tailor-made incentives, after committee stages on 28 July, 29 July and 12 August (text of the order, third-party copy)."),
            ("10 Nov 2026 (Tuesday)", "Cabinet approves the AVGC-XR Policy 2026&ndash;31, the Robotics and Physical AI Policy 2026&ndash;36, amendments to the semiconductor policy and five investment items, 80 days after the data centre order (Hindu, TNIE, Deccan Chronicle).", True),
            ("11 Nov 2026", "Reports say the incentives and budgets of the robotics policy have not been published and will follow in the government order (Elets, Peepals)."),
            ("16 Nov 2026 (Monday)", "Government order approving the robotics policy (The Hindu); G.O.Ms.No.87 amending the semiconductor policy is dated the same day (BusinessLine)."),
            ("17 Nov 2026 (Tuesday)", "AVGC-XR terms reported as finalised by government order: Rs 5,000 crore and one lakh jobs (ETV Bharat, Times of India, excerpts)."),
            ("18 Nov 2026 (Wednesday)", "Minister Nara Lokesh&rsquo;s release on the semiconductor amendment, reported by BusinessLine; its dateline reads 12 November, which is a Thursday and precedes the order it describes.")])
    + numbers(["Item", "Statement", "Source and status"],
              [["Cabinet date and scope", "Tuesday 10 November 2026; more than 30 agenda items; chaired by Chief Minister N. Chandrababu Naidu", "Deccan Chronicle; TNIE; GKToday (page text read)"],
               ["Investment items", f"AM Intelligence Rs 31,387 crore and 1,000 jobs; Carbon Cosmo Rs 4,000.20 crore and 700 jobs; Dixon Rs 700 crore and 2,300 jobs; Epack Rs 570.20 crore and 2,565 jobs; Ravali Spinners Rs 236.92 crore and 1,569 jobs; sum Rs {TOTAL:,.2f} crore and {JOBS_ALL:,} jobs (computed). The Dixon job figure is from the Deccan Chronicle alone", "TNIE; Deccan Chronicle"],
               ["Not in the sum", "Greenko solar capacity raised from 500 MW to 1,500 MW; a 119 MW wind project at Tadipatri; compressed biogas plants; land for a Reliance giga-scale AI data centre (about 25 acres); 173.82 acres for Hetero; a feasibility study of small modular reactors, which is not approval to build", "Telugu360; Deccan Chronicle; GKToday"],
               ["Reliance land", "About 25 acres approved on 10 November; a July order covers up to 854.97 acres and Rs 1,08,010 crore, and a report says 935 acres were sought; the three are not reconciled", "TNIE; MediaNama (excerpt); Economic Times (excerpt)"],
               ["Name of the data centre company", "AM Intelligence Labs (cabinet reports) and AM AI Factory (Vizag) Private Limited (the order; benefits apply only while the parent holds 51%)", "G.O.Ms.No.59 (third-party copy, excerpt)"]],
              "Show the cabinet items, dates and sources"),
    "The cabinet total is dominated by a single data centre that was approved by government order 80 days earlier, so most of the Rs 36,894 crore follows an approval already issued by government order.",
    "The IT, Electronics and Communications Department should list, for each cabinet investment item, the earlier order or board decision it follows, so that new and repeated approvals can be told apart.",
    "cabinet")

s2 = insight(
    "Silicon fab support is 80% in Andhra Pradesh, 15 points above the next state named",
    bars("Silicon fab capital support: 80% in Andhra Pradesh, 56% to 65% in five other states",
         [(s[0], s[1]) for s in STATES], accent="Andhra Pradesh", unit="%", vmax=100,
         sub="Combined Centre and State capital support for a silicon fab, per cent of eligible capital cost. The comparison is the Andhra Pradesh government&rsquo;s own, in a release by Minister Nara Lokesh; the other states&rsquo; figures were not checked against their policies. In Andhra Pradesh the 80% is 40% from the Centre under Semicon 2.0 and 40% from the State.",
         source="The Hindu BusinessLine, 18 November 2026 (page text read); tele.net, 19 November 2026 (page text read). Secondary; the order G.O.Ms.No.87 was not found.")
    + numbers(["Category", "Centre", "State", "Combined and limits"],
              [["Silicon fabs", "40%", "40% (matches Centre)", "80% of eligible capital cost"],
               ["Compound semiconductor, photonics, sensor, discrete and display fabs, advanced packaging", "Not printed", "Matches Centre", "70% combined (so 35% each, implied)"],
               ["Legacy packaging", "Not printed", "Matches Centre", "50% combined (25% each, implied)"],
               ["ATMP and OSAT units", "Centre capital support", "100% of the Centre&rsquo;s", "Matched rupee for rupee"],
               ["Machines and materials", "30% of capital cost", "18% (60% of the Centre&rsquo;s)", "48% combined, plus the Centre&rsquo;s production-linked incentive"],
               ["Chip design", "Rs 15 crore seed (implied)", "50% of the Centre&rsquo;s, up to Rs 7.5 crore", "Up to Rs 22.5 crore combined"],
               ["Deployment-linked incentive", "9% of net sales", "4.5% of net sales", "13.5% combined; Rs 45 crore a project, Rs 180 crore a company"],
               ["R&amp;D and talent", "Not printed", "25% of eligible project cost", "Combined cap 75%"],
               ["Overall caps", "", "State incentives 50% of eligible fixed capital", "All sources 90%"],
               ["Outside Semicon 2.0", "", "Rs 3 a unit power subsidy for five years from commercial production", "Plus incentives under the industrial or electronics policies"],
               ["Tailor-made packages", "", "Projects of Rs 1,000 crore to Rs 5,000 crore (mega) and above Rs 5,000 crore (ultra-mega), decided by the State Investment Promotion Board", "Case by case"],
               ["Talent", "", "Rs 10,000 a trainee a month for six months, Rs 60,000 a trainee (computed)", "At the AP Semiconductor Training and Capacity Building Centre"],
               ["Park", "", "BusinessLine and tele.net: about 5,000 acres at Tirupati; Hans India: a proposed 495-acre park at Reddipalle, Rs 20,000 crore, 12,500 jobs by 2029", "Acreage conflicts by a factor of 10; not reconciled"],
               ["Validity", "", "Five years or until replaced, from the amendment; the policy period is 2024&ndash;29", "Whether the five years run from 2026 is not stated"]],
              "Show the semiconductor incentive stack and the checks"),
    "The stack is internally consistent, with the State matching the Centre rupee for rupee and staying under its own caps of 50% and 90%, but no project has been reported under it and the park size is given as both about 5,000 and 495 acres.",
    "The IT, Electronics and Communications Department should publish G.O.Ms.No.87 with the eligibility guidelines it says will follow, and state the park area and the validity date in one table.",
    "semiconductor")

s3 = insight(
    "Investment per projected job: Rs 5 lakh in AVGC-XR, Rs 34.5 crore in AI data centres",
    bars("Investment per projected job: Rs 5 lakh in AVGC-XR, Rs 34.5 crore in AI data centres",
         [(k, v) for k, v in LAKH_PER_JOB.items()], accent="AVGC-XR policy target", unit=" lakh", fmt=lambda v: _rs(round(v, 1), "lakh"), vmax=3_600,
         sub="Rs lakh of projected investment per projected job, computed here from reported totals; 1 crore is 100 lakh. These are projections by the state or by a feature article, and they mix a policy target (AVGC-XR) with site-level estimates for parks and one company.",
         source="ETV Bharat and Times of India, 17 November 2026; Hans India, 17 November 2026 (feature article, excerpt); TNIE, 11 November 2026. Secondary.")
    + numbers(["Item", "Value", "Source and status"],
              [["AVGC-XR Policy 2026&ndash;31", f"Rs 5,000 crore from five anchor units and 100 companies (Rs {AV_INV / 105:.1f} crore each on average, computed) and one lakh jobs in five years; a 200-acre park in the planned Amaravati Media City", "ETV Bharat; Times of India (excerpts)"],
               ["AVGC-XR incentives", "50% of capital cost up to Rs 2 crore for infrastructure; 25% up to Rs 50 crore for a park; 25% up to Rs 25 crore for a centre of excellence; full SGST reimbursement for five years; stamp duty exemption; Rs 200 crore and 200 jobs qualify as a mega project", "ETV Bharat (excerpt)"],
               ["AVGC-XR baseline", f"The industry is said to need about 20 lakh more professionals by 2030, so one lakh jobs is {100 * AV_JOBS / 2_000_000:.0f}% of that; no figure for Andhra Pradesh&rsquo;s present AVGC-XR employment or output was found", "Hans India (feature; its source for the 20 lakh is not named)"],
               ["Robotics and Physical AI Policy 2026&ndash;36", "Approved on 10 November and by government order on 16 November; manufacturing-led, covering components, robot platforms, integration, R&amp;D, skills and adoption; no investment or jobs target for the policy was found", "The Hindu, 16 November (excerpt); Elets"],
               ["Robotics park", f"300 acres at Gudipalli, Sri Sathya Sai district; about Rs {RB_INV:,} crore and {RB_JOBS:,} jobs; phase I targeted for 2027; named participants include Kia and BEL", "Hans India (feature)"],
               ["Robotics baseline", f"India installed 9,123 industrial robots in 2024, sixth in the world; density six per 10,000 manufacturing workers against a world average of 132, which is {132 / 6:.0f} times; servo motors, encoders and reducers are about 45% of the value of an imported robot", "Hans India (feature; the underlying source is not named)"],
               ["Semiconductor park", f"Rs {SP_INV:,} crore and {SP_JOBS:,} jobs by 2029; named investors Dixon, Foxconn and TCL; Rs {SP_INV / SP_JOBS} crore a job (computed)", "Hans India (feature)"],
               ["AI data centre park", f"Anakapalli, 1,150 acres, about Rs 2.15 lakh crore and {DCP_JOBS:,} jobs by 2027", "Hans India (feature)"]],
              "Show the policy targets, baselines and checks"),
    "The three policies project very different employment per rupee, from Rs 5 lakh a job in animation and gaming to over Rs 30 crore a job in AI data centres, so the data centre route adds far less employment for the capital it draws.",
    "The IT, Electronics and Communications Department should publish a jobs and investment target for the robotics policy and report realised jobs against each target every year.",
    "jobs")

s4 = insight(
    "Andhra Pradesh data centre approvals cost Rs 61 to Rs 121 crore per MW",
    bars("Approved Andhra Pradesh data centres cost Rs 61.3 to Rs 120.9 crore per MW",
         [(DC[0][0], PER_MW[0]), (DC[1][0], PER_MW[1]), (DC[2][0], PER_MW[2]), (DC[3][0], PER_MW[3]), ("Karnataka officials&rsquo; estimate, July 2026", KA_PER_MW)],
         accent=DC[0][0], unit=" crore", fmt=lambda v: _rs(v, "crore"), vmax=125,
         sub=f"Rs crore of proposed investment per MW of capacity, computed here. The Renew AP figures (Rs 85,200 crore, 1,000 MW) are inferred from MediaNama&rsquo;s totals and the Times of India sum; Reliance capacity of 1,500 MW is from the Economic Times. The four orders total Rs 2,83,340 crore and 3,498 MW, which is {100 * 3_498 / 6_000:.1f}% of the 6 GW hosting target and {100 * 3_498 / 15_016:.1f}% of the state&rsquo;s record peak load of 15,016 MW (computed).",
         source="G.O.Ms.No.59, 22 August 2026 (third-party copy); MediaNama, 24 August 2026; The New Indian Express, 24 August 2026; Economic Times Manufacturing, 28 April 2026; Deccan Herald, 18 July 2026 (excerpts). Secondary.")
    + numbers(["Item", "Value", "Source and status"],
              [["AM AI Factory (Vizag)", f"512 MW, Rs 31,387 crore, 1,000 jobs ({1_000 / 512:.2f} a MW, computed), completion within two years and four months; exemptions from transmission charges, electricity duty and cross-subsidy surcharge for 20 years (summary)", "G.O.Ms.No.59; MediaNama (the order&rsquo;s incentive paragraphs were not read)"],
               ["Data Centre Holdings India", f"486 MW, Rs 58,743 crore, 1,250 jobs ({1_250 / 486:.2f} a MW), 200 acres at Jagnadhapuram at a 25% land discount capped at Rs 30 crore; 10% capital subsidy capped at Rs 1,800 crore, so eligible spending of Rs 18,000 crore (computed); Rs 1 a unit power discount for 15 years", "TNIE, 24 August; MediaNama"],
               ["Renew AP Green Data Center", f"About Rs 85,200 crore and 1,000 MW (inferred); caps in the same report sum to Rs {sum(CAPS_RENEW):,} crore, {100 * 14_405 / 85_200:.1f}% of the investment, if all apply to this project and all are separate (computed; the excerpt does not label the project line by line)", "TNIE, 24 August (excerpt)"],
               ["Reliance", "Up to 854.97 acres and Rs 1,08,010 crore in a July order; 1.5 GW and Rs 1.6 lakh crore including renewables in an Economic Times report; first 500 MW targeted for October 2028", "MediaNama; Economic Times (excerpts)"],
               ["State target", "A hosting target of 6 GW was stated by the IT minister in September 2025; MoUs total 5.6 GW (April 2026); orders total 3,498 MW", "Economic Times; MediaNama"],
               ["Operating capacity", "Not found for Andhra Pradesh; the Google and Adani campus was reported as having broken ground on 28 April 2026", "FlexiCloud tracker (excerpt)"],
               ["Mega project rule", "More than Rs 5,000 crore and more than 50 MW qualifies for tailor-made incentives under the Data Center Policy 4.0 2024&ndash;29", "G.O.Ms.No.59"]],
              "Show the data centre figures and checks"),
    "The approved costs range from Rs 61.3 to Rs 120.9 crore a MW, a spread of 1.97 times, so the headline investment figures are not comparable without knowing what each includes, such as power plants, land and later phases.",
    "The IT, Electronics and Communications Department should publish, for each data centre order, the capacity in MW of IT load, the items inside the investment figure and the incentive caps in rupees.",
    "datacentre")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>IT, Electronics and Communications Department:</b> publish the AVGC-XR and robotics policies and G.O.Ms.No.87 with their eligibility guidelines, and state the semiconductor park area and the policy validity date in one table.</li>
<li><b>IT, Electronics and Communications Department:</b> set a jobs and investment target for the robotics policy and report realised figures against every target each year.</li>
<li><b>Andhra Pradesh Economic Development Board:</b> list, for each cabinet investment item, the earlier order or board decision it follows, so that repeat approvals are not counted as new.</li>
<li><b>IT, Electronics and Communications Department:</b> state capacity as MW of IT load for every data centre order, with the items inside the investment figure and the incentive caps in rupees.</li>
<li><b>Information and Public Relations Department:</b> release each cabinet decision in one dated note, with the government order number once it is issued.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Dates come from reports of 10 to 19 November 2026 and from the dated order G.O.Ms.No.59; weekdays were checked against the calendar. The 12 November dateline on the semiconductor report does not fit the Wednesday release or the order of 16 November, and is flagged rather than corrected.</li>
<li>Sums, ratios, per-job and per-MW figures are computed here from the figures shown, and each is checked by an assertion in the builder; the semiconductor percentages were checked for consistency (40 plus 40, 9 plus 4.5, 30 plus 18, 15 plus 7.5, and the rupee caps in crore against tele.net&rsquo;s million and billion).</li>
<li>A target is a figure for a policy period; an outcome is something that has happened. No outcome under the three policies was found.</li>
<li>Page text was read for The New Indian Express, Deccan Chronicle, Telugu360, GKToday, BusinessLine and tele.net. The Hindu, Times of India, ETV Bharat, Hans India (a feature article), MediaNama, Economic Times and the copy of G.O.Ms.No.59, hosted by a third party, were read as search excerpts. News sites are secondary.</li>
<li>The Renew AP project figures are inferred from totals printed by MediaNama and The New Indian Express and are labelled as such.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The text of the AVGC-XR policy, the robotics policy and G.O.Ms.No.87. The incentive terms for AVGC-XR come from one wire report and the Times of India excerpt; the robotics incentives were not found.</li>
<li>Any investment or jobs target for the robotics policy itself. The Gudipalli park figures come from a feature article, not from the order.</li>
<li>The park area for semiconductors: about 5,000 acres at Tirupati (BusinessLine, tele.net) against a 495-acre park at Reddipalle (Hans India). Whether they are one park or two was not established.</li>
<li>Whether the five-year validity of the amended semiconductor policy runs from 2026 or ends with the policy period in 2029.</li>
<li>The correct dateline of the semiconductor release (12 November on the page, 16 November for the order, Wednesday 18 November for the release).</li>
<li>The incentive paragraphs of G.O.Ms.No.59 and what the 512 MW project&rsquo;s Rs 31,387 crore includes; the cabinet reports do not say whether the 10 November item added anything to the August order.</li>
<li>The Renew AP project&rsquo;s own capacity and cost, which are inferred, and how the 25 acres approved on 10 November for Reliance relate to up to 854.97 acres in the July order.</li>
<li>Operating data centre capacity in Andhra Pradesh, Andhra Pradesh&rsquo;s present AVGC-XR employment, the source of the 20 lakh professionals figure, and any realised investment or jobs under any of the three policies.</li>
</ul></details>
'''

step(7, "assembling body")
body = STYLE + top + tvo + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://www.newindianexpress.com/states/andhra-pradesh/2026/Nov/11/ap-cabinet-clears-rs-313k-crore-ai-data-centre-at-bhimili">The New Indian Express, 11 November 2026</a>, '
    '<a href="https://www.deccanchronicle.com/southern-states/andhra-pradesh/ap-cabinet-clears-over-30-agenda-items-2003293">Deccan Chronicle, 10 November 2026</a>, '
    '<a href="https://www.telugu360.com/ap-cabinet-clears-ai-data-centres-robotics-policy-semiconductor-reforms-and-major-industrial-projects/">Telugu360, 10 November 2026</a> and '
    '<a href="https://www.gktoday.in/andhra-pradesh-cabinet-approves-ai-policies-and-investments">GKToday, 11 November 2026</a> (secondary; page text read: the cabinet decisions); '
    '<a href="https://www.thehindu.com/news/national/andhra-pradesh/andhra-pradesh-cabinet-clears-policy-frameworks-to-attract-investments-in-ai-electronics-renewable-energy/article71686342.ece">The Hindu, 10 November 2026</a> and '
    '<a href="http://timesofindia.indiatimes.com/city/vijayawada/andhra-pradesh-cabinet-approves-37000-crore-investments/articleshow/135717412.cms">Times of India, 10 November 2026</a> (secondary, excerpts); '
    '<a href="http://www.thehindubusinessline.com/news/national/andhra-pradesh-launches-semiconductor-policy-offers-up-to-80-capital/article71715026.ece">The Hindu BusinessLine, 18 November 2026</a> and '
    '<a href="https://tele.net.in/national-news/andhra-pradesh-amends-its-semiconductor-and-display-fab-policy-40-12822252">tele.net, 19 November 2026</a> (secondary; page text read: the semiconductor amendment); '
    '<a href="https://etvbharat.com/en/state/andhra-pradesh-govt-to-develop-media-city-in-amaravati-under-avgc-xr-policy-enn26111704138">ETV Bharat, 17 November 2026</a>, '
    '<a href="http://timesofindia.indiatimes.com/city/vijayawada/andhra-pradesh-launches-avgc-xr-policy-plans-200-acre-park-in-amaravati/articleshow/135935282.cms">Times of India, 17 November 2026</a>, '
    '<a href="https://www.thehindu.com/news/national/andhra-pradesh/ap-govt-approves-robotics-and-physical-ai-policy-202636-aimed-at-total-ecosystem-for-state/article71708466.ece">The Hindu, 16 November 2026</a>, '
    '<a href="https://www.thehansindia.com/news/cities/amaravati/ap-takes-aim-at-global-race-for-chips-robots-ai-1143082">Hans India, 17 November 2026</a> (a feature article), '
    '<a href="https://cio.eletsonline.com/artificial-intelligence/andhra-pradesh-physical-ai-policy/76839">Elets CIO, 11 November 2026</a> and '
    '<a href="https://peepalsglobal.com/bharat/article/andhra-pradesh-cabinet-avgc-xr-robotics-physical-ai-policy-2026-11-10">Peepals, 10 November 2026</a> (secondary, excerpts: AVGC-XR and robotics); '
    '<a href="https://stopdirtydatacenters.org/media/resources/files/2026ITC_43626_MS59_E.pdf">G.O.Ms.No.59, 22 August 2026</a> (official order, copy hosted by a third party, excerpt); '
    '<a href="https://www.medianama.com/2026/08/223-andhra-pradesh-ai-data-centres">MediaNama, 24 August 2026</a>, '
    '<a href="https://www.newindianexpress.com/states/andhra-pradesh/2026/Aug/24/two-major-data-centres-get-land-and-incentives-in-andhra-pradesh">The New Indian Express, 24 August 2026</a>, '
    '<a href="https://manufacturing.economictimes.indiatimes.com/news/hi-tech/reliance-industries-to-set-up-indias-largest-data-centre-cluster-in-andhra-pradesh/130571771?utm_source=tagListing&amp;utm_medium=tagListing">Economic Times Manufacturing, 28 April 2026</a> and '
    '<a href="https://www.deccanherald.com/story/business/karnataka-eyes-rs-60k-crore-investment-under-new-data-centre-policy-4077831">Deccan Herald, 18 July 2026</a> (secondary, excerpts: data centre figures). '
    'Percentages, ratios and sums computed by this blog. Analysed 21 November 2026.')
RELATED = []

step(8, "writing page")
build("Policy &middot; Andhra Pradesh", TITLE,
      "Andhra Pradesh&rsquo;s cabinet approved AVGC-XR, robotics and semiconductor policy changes on 10 November 2026 alongside Rs 36,894 crore of projects; this piece sets out the incentives, the projected jobs per rupee, the data centre cost per MW, and what the sources do not show.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(plain), "chars in title")
step(9, "complete")
