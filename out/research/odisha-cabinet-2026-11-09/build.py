"""Odisha cabinet of Monday 9 November 2026: the Rs 4,708.64 crore Upper Indravati pumped storage project, the Rs 393.62 crore Shikshanet college Wi-Fi scheme,
the paddy procurement policy for kharif 2026-27 (Rs 3,100 a quintal, 78 lakh tonnes), unlimited attempts at the civil services examination, and the rest of the 13 proposals.
Build from the repo root:  python3 out/research/odisha-cabinet-2026-11-09/build.py            (writes out/post-odisha-cabinet-9-november-2026.html)
                           python3 out/research/odisha-cabinet-2026-11-09/build.py --check    (arithmetic and asserts only)
Every figure is from the source named beside it, or computed below with an assert. Analysed 21 November 2026.
All sources were read as search excerpts (PTI via ThePrint and India Today, the Odisha Chief Minister's page, New Indian Express, Business Standard, ANI, Sambad English,
Swarajya, Industry Odisha, OdishaBytes, propnewstime (UNI and PTI), OHPC's own project pages, the Odisha Pumped Storage Policy 2025, and Lok Sabha reply 713). No cabinet
note, project report or procurement policy document was found. The post says so."""
import datetime as dt
import html as _h
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
OUT = ROOT / "out/post-odisha-cabinet-9-november-2026.html"
STEPS = 9


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. dates
step(1, "dates and weekday checks")
assert D(2026, 11, 9).strftime("%A") == "Monday"             # PTI: cabinet 'on Monday'; Swarajya '(9 November)'
assert D(2026, 11, 4).strftime("%A") == "Wednesday"          # Union Cabinet storage VGF, per this blog's piece on the scheme
assert D(2026, 11, 6).strftime("%A") == "Friday"             # Chief Minister's remarks on 6 November
assert (D(2026, 11, 9) - D(2026, 7, 27)).days == 105         # OHPC letter of intent for the EPC contract, 27 Jul 2026, to the cabinet item
assert (D(2026, 11, 9) - D(2025, 4, 25)).days == 563          # state Project Approval Committee (25 Apr 2025) to the cabinet's cost decision
assert (D(2026, 11, 9) - D(2026, 11, 1)).days == 8           # kharif procurement runs from 1 Nov 2026; the policy was approved eight days into it
assert D(2025, 4, 25) < D(2026, 7, 27) and D(2024, 8, 19) < D(2025, 4, 25)

# ---- 2. Upper Indravati pumped storage
step(2, "pumped storage cost, financing and efficiency")
TOTAL, CONSTR_CS, EPC, EARLIER, MW = 4_708.64, 3_371.88, 3_372.88, 3_394.48, 600
assert EPC - CONSTR_CS == 1.0                                # Chief Secretary's 'construction' figure and the EPC price differ by exactly Rs 1 crore: flagged, not reconciled
assert round(TOTAL - EPC, 2) == 1_335.76 and round(TOTAL - CONSTR_CS, 2) == 1_336.76
assert f"{100 * EPC / TOTAL:.1f}" == "71.6"
assert f"{TOTAL / MW:.2f}" == "7.85" and f"{EPC / MW:.2f}" == "5.62" and f"{EARLIER / MW:.2f}" == "5.66"
assert round(TOTAL * 1e7 / (MW * 1e3)) == 78_477             # Rs a kW
PRIV_CR, PRIV_MW = 48_863, 7_200                              # Chief Minister, 6 Nov: proposals received
assert f"{PRIV_CR / PRIV_MW:.2f}" == "6.79" and f"{100 * (TOTAL / MW / (PRIV_CR / PRIV_MW) - 1):.1f}" == "15.6"
assert f"{100 * (TOTAL / EARLIER - 1):.1f}" == "38.7"        # new total against the earlier state-level approval; the basis of the earlier figure is not stated
EQ, LOAN = round(0.2 * TOTAL, 2), round(0.8 * TOTAL, 2)
assert (EQ, LOAN) == (941.73, 3_766.91) and round(EQ + LOAN, 2) == TOTAL
GEN, PUMP = 1_040, 1_283                                      # MU a year, OHPC
assert f"{100 * GEN / PUMP:.1f}" == "81.1"
assert f"{GEN * 1e3 / MW / 365:.2f}" == "4.75"                 # hours a day at full output
assert f"{100 * GEN / (MW * 8.76):.1f}" == "19.8"              # share of a 600 MW plant's year (5,256 MU)
LAND_OHPC, LAND_RPT = 151.916, 164
assert f"{100 * (LAND_RPT / LAND_OHPC - 1):.1f}" == "8.0"
assert 4 * 150 == MW and 600 + 600 == 1_200                    # four 150 MW units; combined with the existing 600 MW Upper Indravati station

# ---- 3. other cabinet items
step(3, "irrigation, Shikshanet, paddy")
IRR = [("Seven mega lift irrigation schemes, Nuapada", 268.22, 59), ("In-stream storage, Patharla, Balangir", 99.99, 12), ("Kursud in-stream storage, Indra river, Balangir", 81.36, 17)]
IRR_SUM = round(sum(i[1] for i in IRR), 2)
assert IRR_SUM == 449.57 and round(IRR_SUM) == 450               # PTI: three proposals 'worth Rs 450 crore'
assert [round(i[1] / i[2], 2) for i in IRR] == [4.55, 8.33, 4.79]
assert f"{268.22e7 / 8_800 / 1e5:.2f}" == "3.05"                # Rs lakh a hectare at Nuapada
SHIK = 393.62
assert round(TOTAL + SHIK + IRR_SUM, 2) == 5_551.83 and f"{100 * TOTAL / 5_551.83:.1f}" == "84.8"
assert f"{SHIK * 100 / 601:.1f}" == "65.5" and f"{SHIK * 100 / 731:.1f}" == "53.8" and f"{SHIK * 100 / 750:.1f}" == "52.5"
assert 601 + 130 == 731 and 731 < 750                           # 601 colleges plus 130 phase-I colleges is below the 'over 750' the minister cites
assert round(SHIK * 1e7 / 6e5) == 6_560 and round(SHIK * 1e7 / 6e5 / 3) == 2_187
assert 393.63 - SHIK == 0.01 or round(393.63 - SHIK, 2) == 0.01  # TNIE prints Rs 393.63 crore; all others Rs 393.62 crore
PADDY_T, PRICE, MSP, RICE_T = 78e5, 3_100, 2_441, 53e5          # tonnes of paddy, Rs a quintal, common-grade MSP (BigHaat, secondary), tonnes of rice
assert PRICE - MSP == 659 and f"{100 * (PRICE - MSP) / MSP:.1f}" == "27.0"
Q = PADDY_T * 10                                                # quintals
assert round(Q * PRICE / 1e7, 1) == 24_180.0 and round(Q * MSP / 1e7, 1) == 19_039.8 and round(Q * (PRICE - MSP) / 1e7, 1) == 5_140.2
assert round(Q * MSP / 1e7 + Q * (PRICE - MSP) / 1e7, 1) == 24_180.0
assert f"{100 * RICE_T / PADDY_T:.1f}" == "67.9"                  # rice as a share of paddy, near the 67% milling outturn
assert 2_461 - MSP == 20                                         # Grade A MSP is Rs 20 above common
KMS_SUB_T, KMS_SUB_CR = 3_863_275, 8_030.35                      # a printed sub-total in Lok Sabha reply 713 (excerpt): quantity and MSP value
assert round(KMS_SUB_CR * 1e7 / (KMS_SUB_T * 10)) == 2_079      # Rs a quintal: not an MSP-like figure, so the sub-total is not used as a baseline

TITLE = "Odisha cabinet 9 Nov 2026: Rs 4,708.64 crore pumped storage, college Wi-Fi, paddy purchase"
plain = _h.unescape(TITLE)
assert 55 <= len(plain) <= 90, len(plain)
assert not any(w in plain.lower().split() for w in ("you", "your", "we", "our"))
print(f"consistency checks passed (pumped storage, irrigation, Shikshanet, paddy); title {len(plain)} characters", flush=True)
if "--check" in sys.argv:
    sys.exit(0)

from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402


def _rs(v, unit, dec=None):
    s = f"{v:,.2f}"
    if dec is None:
        s = s.rstrip("0").rstrip(".")
    elif float(v).is_integer():
        s = f"{v:,.0f}"
    return f"Rs {s} {unit}"


step(4, "writing sections")
top = top_line([
    ("84.8%", f" of the Rs 5,551.83 crore of listed project outlays approved on 9 November 2026 is one 600 MW pumped storage plant at Upper Indravati (Rs {TOTAL:,.2f} crore, Rs {TOTAL / MW:.2f} crore a MW), the state&rsquo;s first."),
    ("Rs 1", " crore is the gap between the Chief Secretary&rsquo;s construction figure (Rs 3,371.88 crore) and the contract price in other reports (Rs 3,372.88 crore); an earlier state approval put the project at Rs 3,394.48 crore, and no report explains the difference."),
    ("Rs 3,100", f" a quintal is the paddy price for kharif 2026-27, Rs {PRICE - MSP} above the reported support price of Rs {MSP:,}, for a target of 78 lakh tonnes; the policy was approved eight days after procurement began on 1 November."),
])

tvo = ('<table class="gb-table"><thead><tr><th>Kind</th><th>What this piece includes</th></tr></thead><tbody>'
       '<tr><td><b>Decided</b></td><td>On Monday 9 November 2026 the cabinet, chaired by Chief Minister Mohan Charan Majhi, approved 13 proposals from 10 departments, including the pumped storage project cost, contractor and financing, Shikshanet, the paddy policy and unlimited attempts at the civil services examination.</td></tr>'
       '<tr><td><b>Targets</b></td><td>Commissioning in 2030-31 for the pumped storage plant; 78 lakh tonnes of paddy (53 lakh tonnes of rice); Wi-Fi in 601 colleges for over six lakh users.</td></tr>'
       '<tr><td><b>Outcomes</b></td><td>None found. The pumped storage plant has no construction progress reported, Shikshanet phase I covers 130 colleges, and paddy procurement has run for eight days.</td></tr>'
       '<tr><td><b>Not found</b></td><td>The cabinet notes, the project report and procurement policy text, any procurement result for 2025-26, and whether the pumped storage plant will draw the Union viability gap funding approved on 4 November.</td></tr>'
       '</tbody></table>\n')

s1 = insight(
    "One pumped storage plant is 84.8% of the Rs 5,551.83 crore of project outlays listed",
    bars("One pumped storage plant is 84.8% of the Rs 5,551.83 crore of project outlays listed",
         [("Upper Indravati pumped storage, 600 MW", TOTAL), ("Three water resources projects, Nuapada and Balangir", IRR_SUM), ("Odisha Shikshanet, free college Wi-Fi", SHIK)],
         accent="Upper Indravati pumped storage, 600 MW", unit=" crore", fmt=lambda v: _rs(v, "crore", 2), vmax=5_000,
         sub=f"Rs crore, summed from the items that carry a project amount (computed): Rs {TOTAL:,.2f} crore, Rs {IRR_SUM} crore and Rs {SHIK} crore. The paddy policy has a procurement target but no outlay in the reports, so it is not in the sum; the other eight proposals carry no amount in the reports read.",
         source="PTI via ThePrint and India Today, 10 November 2026; Odisha Chief Minister&rsquo;s page, 9 November 2026 (excerpts). Secondary except the government page.")
    + flow([("19 Aug 2024", "Central Electricity Authority grants techno-economic clearance to the 600 MW Upper Indravati pumped storage project (OHPC project page, excerpt)."),
            ("25 Apr 2025", "State Project Approval Committee approves it, after the High-Level Clearance Authority in December 2024 (OHPC)."),
            ("27 Jul 2026", "OHPC issues the letter of intent for the engineering, procurement and construction contract to Megha Engineering and Infrastructures (OHPC, excerpt)."),
            ("1 Nov 2026", "Kharif paddy procurement opens and runs to 31 March 2027; the policy was approved eight days later (Sambad English, excerpt)."),
            ("4 Nov 2026 (Wednesday)", "Union Cabinet approves Rs 14,500 crore of viability gap funding for 92 GWh of storage, of which 60 GWh is pumped storage, per this blog&rsquo;s piece on the scheme."),
            ("9 Nov 2026 (Monday)", "Odisha cabinet approves the project cost, contractor and financing, 105 days after the letter of intent, with 12 other proposals (PTI, Odisha CM page).", True)])
    + numbers(["Item", "Statement", "Source and status"],
              [["Meeting", "Monday 9 November 2026, Bhubaneswar; 13 proposals from 10 departments; the Odisha CM page lists 12 items and the thirteenth was not identified", "PTI; Odisha CM page (excerpts)"],
               ["Pumped storage", f"Rs {TOTAL:,.2f} crore in total, including Rs 3,371.88 crore for construction; commissioning 2030-31; Megha Engineering selected", "PTI via ThePrint and India Today"],
               ["Water resources", f"Three proposals worth Rs 450 crore (sum of the three below is Rs {IRR_SUM} crore, computed): Rs 268.22 crore for seven mega lift schemes at Nuapada irrigating 8,800 hectares in 59 villages; Rs 99.99 crore at Patharla, Balangir, for 12 villages; Rs 81.36 crore at Kursud on the Indra river for 17 villages. Per village: Rs 4.55, Rs 8.33 and Rs 4.79 crore (computed)", "PTI; Odisha CM page"],
               ["Shikshanet", f"Rs {SHIK} crore over 2026-27 to 2028-29; free Wi-Fi at 601 government and aided colleges", "Business Standard; ANI; Odisha CM page"],
               ["Civil services", "Attempt limit at the Odisha Civil Services examination removed, subject to age eligibility", "PTI; Odisha CM page"],
               ["Other items", "Panchayat Executive Officer cadre restructured to 3,294 posts; 19 Assistant Town Planners to be recruited through the public service commission; one year of training and one year of law clerkship for trainee judicial officers; the Odisha Bovine Breeding (Regulation) Bill 2026; deadline for replacing institutional fair price dealers extended to 30 September 2027", "Odisha CM page (excerpt)"],
               ["Fair price dealers", "PTI says the tenure of about 5,000 private dealers is extended by a year to 30 September 2027; the CM page says the deadline for replacing institutional dealers with private dealers is extended to that date; the two descriptions differ", "PTI; Odisha CM page: not reconciled"]],
              "Show the cabinet items, dates and sources"),
    f"Most of the money in the meeting sits in one plant that took 563 days from the state project approval to a cabinet cost decision, so the other 12 proposals are mostly small amounts or have no amount reported.",
    "The Information and Public Relations Department should publish each cabinet note with the amount, the source of funds and the department for every proposal, including the thirteenth item.",
    "cabinet")

s2 = insight(
    "Odisha pumped storage: Rs 7.85 crore per MW at Upper Indravati, Rs 6.79 crore in proposals",
    bars("Odisha pumped storage: Rs 7.85 crore per MW at Upper Indravati, Rs 6.79 crore in proposals",
         [("Upper Indravati, total cost approved 9 Nov 2026", TOTAL / MW), ("Odisha proposals received: Rs 48,863 crore for 7,200 MW", PRIV_CR / PRIV_MW),
          ("Upper Indravati, earlier state approval (basis not stated)", EARLIER / MW), ("Upper Indravati, contract price only, excluding GST", EPC / MW)],
         accent="Upper Indravati, total cost approved 9 Nov 2026", unit=" crore", fmt=lambda v: _rs(v, "crore"), vmax=9,
         sub=f"Rs crore of cost per MW, computed here. The total of Rs {TOTAL:,.2f} crore includes GST, consultancy, land, forest clearances and interest during construction; the contract price of Rs {EPC:,.2f} crore is {100 * EPC / TOTAL:.1f}% of it. The total is {100 * (TOTAL / MW / (PRIV_CR / PRIV_MW) - 1):.1f}% above the per-MW cost of the proposals, which are not priced on a stated common basis.",
         source="PTI via ThePrint, 10 November 2026; propnewstime (UNI and PTI), 12 November 2026; Business Standard, 12 November 2026; Swarajya, 10 November 2026 (excerpts). Secondary.")
    + numbers(["Item", "Value", "Source and status"],
              [["Capacity and energy", f"600 MW in four 150 MW units; 1,040 MU generated and 1,283 MU used for pumping a year, so {100 * GEN / PUMP:.1f}% of the pumping energy comes back (computed); full output for {GEN * 1e3 / MW / 365:.2f} hours a day, {100 * GEN / (MW * 8.76):.1f}% of the plant&rsquo;s year (computed)", "OHPC project page (excerpt)"],
               ["Cost basis", f"Rs {TOTAL:,.2f} crore total; Rs {TOTAL * 1e7 / (MW * 1e3):,.0f} a kW (computed); contract price Rs {EPC:,.2f} crore excluding GST (UNI, Swarajya, Industry Odisha); the Chief Secretary&rsquo;s construction figure is Rs {CONSTR_CS:,.2f} crore, Rs 1 crore lower; the remainder of the total is Rs {TOTAL - EPC:,.2f} crore (computed)", "PTI; UNI; Swarajya; Industry Odisha (excerpts): the Rs 1 crore is not reconciled"],
               ["Earlier approval", f"Rs {EARLIER:,.2f} crore at an earlier state-level approval, when it was described as an OHPC project in Kalahandi; the new total is {100 * (TOTAL / EARLIER - 1):.1f}% higher (computed), and what each includes is not stated", "propnewstime (PTI), 12 November"],
               ["Financing", f"80:20 debt to equity: OHPC equity of Rs {EQ:,.2f} crore from internal reserves and a state loan of Rs {LOAN:,.2f} crore at the RBI repo rate, both in phases (computed from the total)", "Industry Odisha; OdishaBytes; Swarajya (excerpts)"],
               ["Site", f"151.916 hectares in OHPC&rsquo;s own table and 164 hectares in a report, {100 * (LAND_RPT / LAND_OHPC - 1):.1f}% more; mostly forest land; about 227 families in four villages affected", "OHPC; Swarajya (excerpts)"],
               ["Existing station", "Upper Indravati hydro station of 600 MW; with the new plant 1,200 MW. Business Standard attributes the 1,040 MU to the existing station, while OHPC gives it as the pumped storage plant&rsquo;s annual generation", "Business Standard; OHPC: not reconciled"],
               ["Policy context", "Odisha Pumped Storage Projects Policy 2025, amended in August 2026 (registration window for developers from three weeks to three months); Chief Minister on 6 November: proposals of Rs 48,863 crore for 7,200 MW (Rs 6.79 crore a MW, computed)", "Odisha policy document (excerpt); propnewstime"],
               ["Union support", "Rs 14,500 crore of viability gap funding for 92 GWh of storage approved by the Union Cabinet on 4 November; the share for pumped storage is 60 GWh; whether a state-owned plant such as this one qualifies was not found", "This blog&rsquo;s piece on the storage scheme; release not re-read"]],
              "Show the pumped storage figures, financing and conflicts"),
    f"The cost per MW is Rs {TOTAL / MW:.2f} crore, {100 * (TOTAL / MW / (PRIV_CR / PRIV_MW) - 1):.1f}% above the proposals pending in the state, and a Rs 1 crore difference between two reported construction figures and the earlier lower approval of Rs {EARLIER:,.2f} crore are not explained.",
    "The Energy Department and OHPC should publish the project cost by head, with the GST, land, interest during construction and contingency lines, and state how the earlier Rs 3,394.48 crore approval relates to the new total.",
    "pumped")

s3 = insight(
    "Shikshanet costs Rs 52.5 to 65.5 lakh per institution; coverage is 601 or 750",
    bars("Shikshanet costs Rs 52.5 to 65.5 lakh per institution; coverage is 601 or 750",
         [("601 colleges (Chief Secretary, Business Standard)", SHIK * 100 / 601), ("731 institutions (601 plus the 130 of phase I, computed)", SHIK * 100 / 731), ("Over 750 institutions (Minister, ANI)", SHIK * 100 / 750)],
         accent="601 colleges (Chief Secretary, Business Standard)", unit=" lakh", fmt=lambda v: _rs(round(v, 1), "lakh"), vmax=70,
         sub=f"Rs lakh of scheme outlay per institution over three years, 2026-27 to 2028-29, computed from Rs {SHIK} crore; the reports do not say whether the 601 includes the 130 colleges of phase I. At six lakh users the outlay is Rs {SHIK * 1e7 / 6e5:,.0f} each over three years, or Rs {SHIK * 1e7 / 6e5 / 3:,.0f} a year (computed).",
         source="The New Indian Express, 10 November 2026; Business Standard, 9 November 2026; ANI, 10 November 2026 (excerpts). Secondary.")
    + numbers(["Item", "Value", "Source and status"],
              [["Outlay", f"Rs {SHIK} crore over three years (2026-27 to 2028-29); The New Indian Express prints Rs 393.63 crore, a Rs 0.01 crore difference", "Business Standard; ANI; Odisha CM page; TNIE"],
               ["Coverage", "601 government and aided colleges; the Minister says more than 750 institutions including universities, after 130 institutions in the trial phase; 601 plus 130 is 731, below 750", "TNIE; ANI: not reconciled"],
               ["Service", "Up to 1 GB a day for each authenticated student within the campus; the Minister adds a speed of 200 Mbps; covers Wi-Fi infrastructure, bandwidth, network management, cyber security and operation and maintenance, with a monitoring dashboard", "TNIE; Business Standard; ANI"],
               ["Users", "More than six lakh students and faculty members", "TNIE; Business Standard"],
               ["Results from phase I", "Described as successful in 130 colleges; no usage, uptime or cost figure was found", "Not established"]],
              "Show the Shikshanet figures and conflicts"),
    "The cost per institution moves by Rs 13 lakh with the coverage count, and the reports give no usage or uptime result from the 130 colleges already connected.",
    "The Higher Education Department should publish the list of covered institutions, the cost per institution and the phase I usage and uptime, so that the 601 and 750 counts can be reconciled.",
    "wifi")

s4 = insight(
    "Odisha paddy price of Rs 3,100 a quintal is MSP Rs 2,441 plus Rs 659 of state assistance",
    bars("Odisha paddy price of Rs 3,100 a quintal is MSP Rs 2,441 plus Rs 659 of state assistance",
         [("Support price, common grade (Centre)", MSP), ("State input assistance (computed)", PRICE - MSP), ("Price to farmers, kharif 2026-27", PRICE)],
         accent="Price to farmers, kharif 2026-27", unit=" a quintal", fmt=lambda v: f"Rs {v:,.0f}", vmax=3_300,
         sub=f"Rs a quintal. The Rs 3,100 is stated by the state; the support price of Rs 2,441 for common-grade paddy is from a farm-advice site (secondary) and the Rs 659 is the difference between them, {100 * (PRICE - MSP) / MSP:.1f}% of the support price. At the 78 lakh tonne target the purchase value is Rs {Q * PRICE / 1e7:,.0f} crore, of which Rs {Q * (PRICE - MSP) / 1e7:,.1f} crore would be input assistance (computed; the target is for purchase, and who bears each part was not found).",
         source="Sambad English, 10 November 2026; The New Indian Express, 10 November 2026; Odisha CM page; BigHaat, 10 November 2026 (secondary, support price). All excerpts.")
    + numbers(["Item", "Value", "Source and status"],
              [["Target", f"53 lakh tonnes of rice, about 78 lakh tonnes of paddy; rice is {100 * RICE_T / PADDY_T:.1f}% of the paddy figure (computed); India Today says at least 78 lakh tonnes, the CM page calls it a target", "Odisha CM page; PTI via India Today"],
               ["Price", "Rs 3,100 a quintal including the support price and input assistance; the support price is Rs 2,441 (common) and Rs 2,461 (Grade A) per BigHaat", "Odisha CM page; BigHaat (secondary)"],
               ["Period", "1 November 2026 to 31 March 2027; approved 9 November", "Sambad English; BigHaat"],
               ["Payment and checks", "Payment within 24 to 48 hours to Aadhaar-linked accounts through NPCI; 100% field verification of paddy area with satellite imagery, digital crop survey and land records; sharecroppers can register with the landowner&rsquo;s consent; procurement through PACS, LAMPCS and Pani Panchayats", "Sambad English (excerpt)"],
               ["Baseline", "Lok Sabha reply 713 (4 February 2026) covers kharif 2025-26 procurement from 1 November 2025 to 31 March 2026, district by district; the excerpt read gives a printed sub-total of 38.6 lakh tonnes, 8.8 lakh farmers and Rs 8,030.35 crore, which works out to Rs 2,079 a quintal and is not a plausible support price, so it is not used", "Lok Sabha reply 713 (official, garbled excerpt)"],
               ["Civil services examination", "Attempt limit removed, subject to age eligibility; India Today says the limits were six for the general category and nine for SEBC, with SC and ST already unlimited; The New Indian Express says six with age relaxations for reserved categories", "India Today; TNIE: the two accounts differ"]],
              "Show the paddy figures, baseline and checks"),
    f"The state adds about 27% to the support price, and the policy was approved after procurement began on 1 November, so the reports do not say which terms applied to paddy sold in the first eight days.",
    "The Food Supplies and Consumer Welfare Department should publish the support price and input assistance as separate lines, the funds for each, and the 2025-26 procurement result by district, with the 2026-27 policy text.",
    "paddy")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Energy Department and OHPC:</b> publish the Upper Indravati cost by head and reconcile Rs 4,708.64 crore, Rs 3,371.88 crore, Rs 3,372.88 crore and the earlier Rs 3,394.48 crore in one note.</li>
<li><b>Energy Department:</b> state whether the Upper Indravati plant will bid for the Union viability gap funding approved on 4 November, and how that would change the state loan.</li>
<li><b>Higher Education Department:</b> publish the list of institutions covered by Shikshanet, the cost per institution and the phase I usage and uptime.</li>
<li><b>Food Supplies and Consumer Welfare Department:</b> publish the paddy support price and state input assistance as separate lines, with the 2025-26 procurement result by district.</li>
<li><b>Information and Public Relations Department:</b> release each cabinet note with the amount, source of funds and department for all 13 proposals.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The meeting date is Monday 9 November 2026 (PTI, Swarajya); weekdays were checked against the calendar. The Union Cabinet date of 4 November is taken from this blog&rsquo;s earlier piece on the storage scheme and was not re-read.</li>
<li>Per-MW, per-institution, per-user and percentage figures, the 80:20 split of the cost and the paddy purchase value are computed here from the figures shown, and each is checked by an assertion in the builder. The paddy purchase value assumes the whole 78 lakh tonnes is bought at Rs 3,100 a quintal.</li>
<li>A target is a figure for a plan or a season; an outcome is something that has happened. No outcome under any of the three main decisions was found.</li>
<li>Every source was read as a search excerpt; no cabinet note, project report or policy text was found. News sites, a farm-advice site and a regional outlet are secondary; the Odisha Chief Minister&rsquo;s page, OHPC, the Odisha policy and the Lok Sabha reply are official.</li>
<li>The sub-total in the Lok Sabha reply was in a garbled excerpt and is reported but not used.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The cabinet notes, the Upper Indravati project report and the procurement policy text. The thirteenth proposal was not identified.</li>
<li>Why the Chief Secretary&rsquo;s construction figure (Rs 3,371.88 crore) is Rs 1 crore below the contract price in four other reports (Rs 3,372.88 crore), and what the earlier Rs 3,394.48 crore approval covered.</li>
<li>The correct land requirement (151.916 or 164 hectares) and whether the 1,040 MU belongs to the new plant, as OHPC states, or the existing station, as Business Standard says.</li>
<li>Whether the plant will get the Union viability gap funding or the state loan terms as reported; the Union release was not re-read for this piece.</li>
<li>The Shikshanet coverage count (601, 731 or over 750 institutions) and any usage or cost result from phase I.</li>
<li>The paddy support price of Rs 2,441 from a primary source, who bears the Rs 659 and the support-price part of the Rs 3,100, and procurement results for 2025-26: the Lok Sabha annexure excerpt was garbled.</li>
<li>What price the farmers who sold between 1 and 9 November received, and what the fair price dealer extension covers: PTI and the Chief Minister&rsquo;s page describe it differently.</li>
<li>Any construction progress, college connected, or tonne of paddy bought under these approvals.</li>
</ul></details>
'''

step(5, "assembling body")
body = STYLE + top + tvo + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://theprint.in/india/odisha-cabinet-approves-proposal-for-rs-4708-crore-pumped-storage-project/3094621">PTI via ThePrint, 10 November 2026</a>, '
    '<a href="https://www.indiatoday.in/india/odisha/story/odisha-cabinet-approves-pumped-storage-free-college-wifi-unlimited-civil-services-attempts-ptag-3035711-2026-11-10">India Today, 10 November 2026</a> and '
    '<a href="https://cm.odisha.gov.in/en/latest-news/odisha-cabinet-approves-development-oriented-proposals-focus-good-governance-employment">Odisha Chief Minister&rsquo;s page, 9 November 2026</a> (the cabinet decisions; the last is official, excerpts); '
    '<a href="https://propnewstime.com/latestnewsstories/NDAwMzc=/odisha-cabinet-approves-proposal-for-inr-4-708-crore-pumped-storage-project">propnewstime, 12 November 2026</a>, '
    '<a href="https://www.industryodisha.com/odisha-1/odisha-cabinet-approves-600-mw-hydro-power-project-worth-rs-4708-cr">Industry Odisha, 10 November 2026</a>, '
    '<a href="https://swarajyamag.com/news-brief/odisha-cabinet-approves-4708-crore-upper-indravati-pumped-storage-project-in-kalahandi-district">Swarajya, 10 November 2026</a>, '
    '<a href="https://odishabytes.com/odisha-to-spend-rs-4708-crore-for-upper-indravati-pumped-storage-project">OdishaBytes, 10 November 2026</a> and '
    '<a href="https://www.business-standard.com/industry/news/odisha-to-build-first-large-scale-pumped-storage-project-for-4-708-crore-126111201582_1.html">Business Standard, 12 November 2026</a> (secondary, excerpts: pumped storage); '
    '<a href="https://www.ohpc.co.in/project/new-upcoming-project/">OHPC, new and upcoming projects</a>, '
    '<a href="https://www.ohpc.co.in/events/a-landmark-milestone-for-odishas-clean-energy-journey">OHPC, 27 July 2026</a> and '
    '<a href="https://investodisha.gov.in/download/odisha-psp-policy-2025.pdf">Odisha Pumped Storage Projects Policy 2025</a> (official, excerpts); '
    '<a href="https://www.newindianexpress.com/story/states/odisha/2026/nov/10/odisha-state-cabinet-approves-shikshanet-scheme-to-provide-free-wifi-to-601-colleges">The New Indian Express, 10 November 2026</a>, '
    '<a href="https://www.business-standard.com/education/news/odisha-approves-394-crore-scheme-for-free-wi-fi-in-601-state-colleges-126110901615_1.html">Business Standard, 9 November 2026</a> and '
    '<a href="https://www.aninews.in/news/national/general-news/odisha-cabinet-approves-rs-39362-crore-shiksha-net-scheme-to-provide-free-wi-fi-in-750-plus-institutions-suryabanshi-suraj20261110220145">ANI, 10 November 2026</a> (secondary, excerpts: Shikshanet); '
    '<a href="https://sambadenglish.com/latest-news/odisha-cabinet-approves-paddy-procurement-policy-for-kms-2026-27-farmers-to-get-rs-3100-per-quintal-12797252">Sambad English, 10 November 2026</a> and '
    '<a href="https://www.bighaat.com/kisan-vedika/blogs/odisha-paddy-procurement">BigHaat, 10 November 2026</a> (secondary, excerpts: paddy); '
    '<a href="https://sansad.in/getFile/loksabhaquestions/annex/187/AU713_Bl91bq.pdf?source=pqals">Lok Sabha reply 713, 4 February 2026</a> (official, garbled excerpt); '
    '<a href="https://www.newindianexpress.com/states/odisha/2026/Nov/10/odisha-govt-removes-caps-on-ocs-examination-attempts">The New Indian Express, 10 November 2026</a> and '
    '<a href="https://www.indiatoday.in/education-today/news/story/odisha-removes-attempt-limit-for-ocs-exam-allows-unlimited-attempts-for-all-categories-3035797-2026-11-10">India Today, 10 November 2026</a> (secondary, excerpts: civil services examination). '
    'Percentages, ratios and sums computed by this blog. Analysed 21 November 2026.')
RELATED = []

step(6, "writing page")
build("Policy &middot; Odisha", TITLE,
      "Odisha&rsquo;s cabinet approved a Rs 4,708.64 crore pumped storage plant, college Wi-Fi, a paddy procurement policy and 10 other proposals on 9 November 2026; this piece sets out the figures, the source conflicts and what the reports do not show.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(plain), "chars in title")
step(7, "page checks")
step(8, "complete")
step(9, "done")
