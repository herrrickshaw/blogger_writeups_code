"""Digital Bharat Nidhi: Thirty-second Report of the Standing Committee on Communications and Information Technology
(presented 6 August 2026) on schemes and projects under the fund, read from the report itself (105 pages) and its press release.
Build from the repo root:  python3 out/research/digital-bharat-nidhi-2026/build.py   (writes out/post-digital-bharat-nidhi-32nd-report.html)
Every figure is from the report (paragraph or Annexure named beside it), from the PIB release of 6 November 2026, or computed below with an assert.
Analysed 25 November 2026."""
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-digital-bharat-nidhi-32nd-report.html"
STEPS = 7


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


# ---- 1. BharatNet budget against actual expenditure (report para 124)
step(1, "BharatNet budget and spend, 2022-23 to 2024-25")
BUD = {"2022-23": (1500.00, 1500.00), "2023-24": (5000.00, 3075.54), "2024-25": (6500.00, 3995.01)}
SH = {k: round(100 * s / b, 1) for k, (b, s) in BUD.items()}
assert SH == {"2022-23": 100.0, "2023-24": 61.5, "2024-25": 61.5}
TOT_B = sum(b for b, _ in BUD.values())
TOT_S = round(sum(s for _, s in BUD.values()), 2)
assert (TOT_B, TOT_S) == (13000.0, 8570.55)
assert f"{100 * TOT_S / TOT_B:.1f}" == "65.9"
assert round(TOT_B - TOT_S, 2) == 4429.45
assert round(BUD["2023-24"][0] - BUD["2023-24"][1] + BUD["2024-25"][0] - BUD["2024-25"][1], 2) == 4429.45

# ---- 2. State-wise disbursal under BharatNet phases I and II (Annexure III, as on 28.2.2026)
step(2, "state-wise disbursal and sum checks")
ANX3 = {  # state: (phase I, phase II), Rs crore
    "Andaman and Nicobar Islands": (16.60, 15.01), "Andhra Pradesh": (300.56, 1435.39), "Assam": (177.70, 88.69),
    "Bihar": (506.30, 1075.92), "Chhattisgarh": (560.04, 2059.01), "Gujarat (with Dadra and Nagar Haveli and Daman and Diu)": (504.62, 3293.65),
    "Haryana": (394.70, 237.55), "Himachal Pradesh": (85.05, 36.95), "Jammu and Kashmir (with Ladakh)": (77.11, 218.19),
    "Jharkhand": (301.93, 782.00), "Karnataka": (673.27, 551.61), "Kerala (with Lakshadweep)": (59.81, 193.55),
    "Madhya Pradesh": (1749.14, 2040.98), "Maharashtra": (1777.72, 3566.43), "NE-I (Meghalaya, Mizoram, Tripura)": (214.60, 52.89),
    "NE-II (Arunachal Pradesh, Manipur, Nagaland)": (216.32, 135.80), "Odisha": (541.47, 737.84), "Puducherry": (5.20, 5.02),
    "Punjab (with Chandigarh)": (385.78, 1015.09), "Rajasthan": (1023.05, 640.31), "Sikkim": (15.21, 71.82),
    "Tamil Nadu": (10.81, 1356.51), "Telangana": (230.76, 1912.05), "Uttar Pradesh": (1769.33, 3556.25),
    "Uttarakhand": (277.03, 68.86), "West Bengal": (439.31, 177.74),
    "Central and other (NOC, BBNL administrative expenses and others)": (0.0, 2995.99),
}
P1 = round(sum(v[0] for v in ANX3.values()), 2)
P2 = round(sum(v[1] for v in ANX3.values()), 2)
assert (P1, P2) == (12313.42, 28321.10), (P1, P2)             # the Annexure prints 12,313.42 and 28,321.1
ALL = round(P1 + P2, 2)
assert ALL == 40634.52 and round(ALL) == 40635                  # para 112: 'Rs. 40,635 crore have been disbursed'
TOT = {k: round(a + b, 2) for k, (a, b) in ANX3.items()}
assert TOT["Maharashtra"] == 5344.15 and TOT["Uttar Pradesh"] == 5325.58 and TOT["Telangana"] == 2142.81
assert TOT["Madhya Pradesh"] == 3790.12
GUJ = "Gujarat (with Dadra and Nagar Haveli and Daman and Diu)"
assert TOT[GUJ] == 3798.27
top4 = round(TOT["Maharashtra"] + TOT["Uttar Pradesh"] + TOT[GUJ] + TOT["Madhya Pradesh"], 2)
assert top4 == 18258.12 and f"{100 * top4 / ALL:.1f}" == "44.9"
assert f"{100 * TOT['Telangana'] / ALL:.1f}" == "5.3"
assert f"{100 * 2995.99 / ALL:.1f}" == "7.4"
assert sorted(TOT, key=TOT.get, reverse=True)[:4] == ["Maharashtra", "Uttar Pradesh", GUJ, "Madhya Pradesh"]
# the report's own paragraph 22 figures
assert (1769.33, 3556.25) == ANX3["Uttar Pradesh"] and (1777.72, 3566.43) == ANX3["Maharashtra"]

# ---- 3. Telangana: report spend to 28 Feb 2026 against the PIB figure of 6 Nov 2026 (different programmes)
step(3, "Telangana: PIB figure against the report")
PIB_CR, PIB_GP = 3189, 12769
assert 1946 + 10787 + 36 == PIB_GP                              # PIB: 1,946 Phase I + 10,787 Phase II + 36 new
PER_GP_LAKH = PIB_CR * 100 / PIB_GP                              # Rs crore -> Rs lakh (1 crore = 100 lakh)
assert f"{PER_GP_LAKH:.1f}" == "25.0"
assert f"{PIB_CR / TOT['Telangana']:.2f}" == "1.49"

# ---- 4. Mobile connectivity projects: towers against money (status table para 16 and Annexure I)
step(4, "mobile projects: towers against money")
TOW_DONE, TOW_PLAN = 24198, 34780
assert f"{100 * TOW_DONE / TOW_PLAN:.1f}" == "69.6"             # report: 69.6%
G4_DONE, G4_PLAN, G4_COST, G4_SPENT = 14301, 23570, 30620, 9417.88
assert f"{100 * G4_DONE / G4_PLAN:.1f}" == "60.7"               # report: 60.7%
assert f"{100 * G4_SPENT / G4_COST:.1f}" == "30.8"
BOP_DONE, BOP_PLAN, BOP_COST_A1, BOP_SPENT, BOP_COST_ST = 251, 602, 737, 119.93, 1546
assert f"{100 * BOP_DONE / BOP_PLAN:.1f}" == "41.7"             # report: 41.7%
assert f"{100 * BOP_SPENT / BOP_COST_A1:.1f}" == "16.3" and f"{100 * BOP_SPENT / BOP_COST_ST:.1f}" == "7.8"
ANX1 = {"4G saturation": (30620, 9417.88), "BOP/BIP": (737, 119.93), "Lakshadweep": (63, 14.86), "LWE Phase-I": (2426, 848.53),
        "354 uncovered villages": (301, 245.17), "Meghalaya": (398, 249.80), "502 Aspirational Districts": (233, 152.55),
        "Andaman and Nicobar": (110, 40.46), "LWE Phase-II": (1578, 683.47), "Andhra Pradesh and 2 Assam districts": (667, 331.11),
        "7,287 Aspirational Districts": (2876, 1357.36)}
assert sum(c for c, _ in ANX1.values()) == 40009                # Annexure I total project cost
assert round(sum(s for _, s in ANX1.values()), 2) == 13461.12   # Annexure I total disbursed
assert f"{100 * 13461.12 / 40009:.1f}" == "33.6"
# the status table (para 16) gives a different cost for four of these projects: report-internal conflict
ST_COST = {"BOP/BIP": 1546, "Lakshadweep": 36, "Andaman and Nicobar": 130}
CONFLICTS = [k for k, v in ST_COST.items() if ANX1[k][0] != v]
assert CONFLICTS == ["BOP/BIP", "Lakshadweep", "Andaman and Nicobar"]
assert 34628 + 7839 == 42467                                    # status table: BSNL projects + private TSP projects
assert f"{100 * 16864 / 26549:.1f}" == "63.5"                  # BSNL sub-total
assert f"{100 * 7334 / 8231:.1f}" == "89.1"                    # private TSP sub-total
assert f"{100 * 2275 / 2340:.1f}" == "97.2"
# cost of the 4G saturation project: the Cabinet figure of July 2022 (excluding taxes) against the table
CAB_4G = 26316
assert 30620 - CAB_4G == 4304

# ---- 5. Liquidated damages (Annexure II)
step(5, "liquidated damages")
LD = {"2020-21": 1.31, "2021-22": 2.33, "2022-23": 1.01, "2023-24": 4.51, "2024-25": 6.29, "2025-26": 31.01}
assert round(sum(LD.values()), 2) == 46.46
assert f"{100 * LD['2025-26'] / 46.46:.1f}" == "66.7"
assert f"{LD['2025-26'] / LD['2024-25']:.1f}" == "4.9"
assert f"{LD['2025-26'] / LD['2020-21']:.1f}" == "23.7"

# ---- 6. Other figures read in the report
step(6, "other report figures")
PH1_SCOPE, PH1_POP = 120210, 40610
assert f"{100 * PH1_POP / PH1_SCOPE:.1f}" == "33.8"
POPS = {"Phase I": 40610, "Phase II": 38289, "Amended BharatNet": 2884}
assert POPS["Phase I"] + POPS["Phase II"] == 78899              # the report's stated total of operational PoPs
assert sum(POPS.values()) == 81783 and sum(POPS.values()) - 78899 == 2884   # the stated total leaves out the third term
TTDF = [271, 34.5, 22, 174, 19, 22.5]
assert round(sum(TTDF), 1) == 543.0                              # sanctioned R&D funding of about Rs 543 crore
assert 104 + 11 + 5 + 3 + 4 + 9 == 136                           # TTDF project count by domain

TITLE = "Digital Bharat Nidhi: 61.5% of the BharatNet budget spent in 2023-24 and 2024-25"
assert 55 <= len(TITLE) <= 90, len(TITLE)
assert not any(w in TITLE.lower().split() for w in ("you", "your", "we", "our"))

step(7, "writing sections")
top = top_line([
    ("Rs 40,635 crore", f" had been disbursed from the fund for BharatNet phases I and II by 28 February 2026, and the committee found that operational gram panchayats remain below universal coverage; four states account for {100 * top4 / ALL:.1f}% of the money (Annexure III, computed)."),
    ("61.5%", " of the BharatNet budget allotment was spent in each of 2023-24 and 2024-25 (Rs 3,075.54 crore of Rs 5,000 crore, then Rs 3,995.01 crore of Rs 6,500 crore), against 100% in 2022-23."),
    ("60.7%", " of 4G saturation towers were commissioned by 28 February 2026 while 30.8% of the project cost had been disbursed; the project is due in December 2026."),
])

mech = ('<section class="xv-sec"><h2 class="gb-h2" id="fund">How the fund is financed and spent</h2>\n'
        + flow([("Levy", "Licensees pay a Universal Access Levy of 5% of Adjusted Gross Revenue (report, para 5)."),
                ("Consolidated Fund", "The levy is credited to the Consolidated Fund of India, so the fund does not hold the cash itself."),
                ("Appropriation", "Money reaches Digital Bharat Nidhi only through a budget provision that Parliament appropriates; the fund is non-lapsable.", True),
                ("Schemes", "BharatNet fibre to gram panchayats, 4G saturation, mobile services in left-wing extremism, aspirational-district, border, island and north-eastern areas, and research and pilots."),
                ("Name and scope", "The Telecommunications Act, 2023 widened the former Universal Service Obligation Fund to urban areas and research; the Rules of 30 August 2024 renamed it Digital Bharat Nidhi.")])
        + '</section>\n')

s1 = insight(
    "BharatNet budget: 61.5% spent in 2023-24 and in 2024-25, against 100% in 2022-23",
    bars("BharatNet spent 100%, then 61.5% and 61.5% of the budget allotment in three years",
         [("2022-23: Rs 1,500 crore allotted, Rs 1,500 crore spent", SH["2022-23"]),
          ("2023-24: Rs 5,000 crore allotted, Rs 3,075.54 crore spent", SH["2023-24"]),
          ("2024-25: Rs 6,500 crore allotted, Rs 3,995.01 crore spent", SH["2024-25"])],
         accent=["2023-24: Rs 5,000 crore allotted, Rs 3,075.54 crore spent", "2024-25: Rs 6,500 crore allotted, Rs 3,995.01 crore spent"],
         unit="%", vmax=100,
         sub="Actual expenditure as a share of budget allotment, per cent; shares computed here from the Department&rsquo;s reply in paragraph 124 of the report. Over the three years Rs 8,570.55 crore was spent against Rs 13,000 crore allotted, or 65.9%.",
         source="Standing Committee on Communications and Information Technology, 32nd Report, 6 August 2026, para 124 (official).")
    + numbers(["Year", "Allotment, Rs crore", "Actual, Rs crore", "Share spent"],
              [[k, f"{b:,.2f}", f"{s:,.2f}", f"{SH[k]}%"] for k, (b, s) in BUD.items()]
              + [["Total", f"{TOT_B:,.2f}", f"{TOT_S:,.2f}", "65.9%"]],
              "Show the budget and spend figures"),
    "The report gives no reason for the gap of Rs 4,429.45 crore in the last two years, and the Department said there was no delay in fund release due to pending utilisation certificates in the State-led model.",
    "The Department of Telecommunications should publish the budget allotment, revised estimate and actual expenditure for each fund scheme in every year, with the reason for each shortfall.",
    "budget")

s2 = insight(
    "BharatNet phases I and II: four states received 44.9% of Rs 40,635 crore",
    bars("Maharashtra and Uttar Pradesh each received over Rs 5,300 crore; Telangana Rs 2,143 crore",
         [("Maharashtra", TOT["Maharashtra"]), ("Uttar Pradesh", TOT["Uttar Pradesh"]),
          ("Gujarat, with Dadra and Nagar Haveli and Daman and Diu", TOT[GUJ]), ("Madhya Pradesh", TOT["Madhya Pradesh"]),
          ("Central and other expenses, not by state", 2995.99), ("Telangana", TOT["Telangana"])],
         accent="Telangana", unit="₹ crore", vmax=5600,
         sub="Disbursed from the fund under BharatNet phases I and II to 28 February 2026, Rs crore, phase I and phase II added here. Total Rs 40,634.52 crore (the report states Rs 40,635 crore); the four named states sum to 44.9% and Telangana to 5.3%, computed.",
         source="Standing Committee on Communications and Information Technology, 32nd Report, Annexure III and para 112 (official).")
    + numbers(["State or item", "Phase I, Rs crore", "Phase II, Rs crore", "Total, Rs crore"],
              [[k, f"{a:,.2f}", f"{b:,.2f}", f"{TOT[k]:,.2f}"] for k, (a, b) in sorted(ANX3.items(), key=lambda kv: -TOT[kv[0]])]
              + [["Total", f"{P1:,.2f}", f"{P2:,.2f}", f"{ALL:,.2f}"]],
              "Show spending in every state"),
    f"Telangana&rsquo;s Rs {TOT['Telangana']:,.2f} crore was disbursed under the State-led model, which the Department listed among the models that were delayed by procurement, disputes and right-of-way clearances, so spending to date does not show how many panchayats are lit.",
    "The Department should publish, for each state and phase, the panchayats connected, lit and in use next to the money disbursed, so that spending can be read against outcomes.",
    "states")

s2b = insight(
    "Telangana: Rs 3,189 crore approved, 1.49 times the Rs 2,143 crore disbursed so far",
    bars("The Amended BharatNet approval for Telangana is Rs 25.0 lakh for each of 12,769 panchayats",
         [("Amended BharatNet support approved, 6 November 2026", PIB_CR), ("Disbursed under phases I and II to 28 February 2026", TOT["Telangana"])],
         accent="Amended BharatNet support approved, 6 November 2026", unit="₹ crore", vmax=3400,
         sub=f"Rs crore. The two figures are for different programmes and dates and are compared only in size. The approved scope is {PIB_GP:,} panchayats: 1,946 phase I panchayats moved from linear to ring topology, 10,787 phase II panchayats and 36 new panchayats; Rs 25.0 lakh a panchayat is computed.",
         source="PIB, Department of Telecommunications, 6 November 2026 (official); Standing Committee 32nd Report, Annexure III (official).")
    + numbers(["Item", "Statement", "Source"],
              [["Agreement", "Signed on 6 November 2026 by Digital Bharat Nidhi, the Telangana Government, TRIICL, BSNL and T-Fiber under the State-led model", "PIB release"],
               ["Support approved", "Rs 3,189 crore for 12,769 gram panchayats; about three lakh rural home fibre connections expected with subsidy support", "PIB release"],
               ["Spent so far, phases I and II", f"Phase I Rs {ANX3['Telangana'][0]:,.2f} crore, phase II Rs {ANX3['Telangana'][1]:,.2f} crore, total Rs {TOT['Telangana']:,.2f} crore", "Report, Annexure III"],
               ["Report on Telangana", "Listed with Chhattisgarh, Maharashtra and Tamil Nadu as State-led model states in which delays arose from SPV-led procurement, disputes with implementing agencies and right-of-way clearances", "Report, para 3 of the observations"],
               ["Ratio", "1.49 (Rs 3,189 crore divided by Rs 2,142.81 crore); the two figures are for different programmes and dates, so the ratio shows size only", "Computed"]],
              "Show the Telangana figures and sources"),
    "The approval is a plan figure for a new agreement, and the report records that the State-led models were behind schedule, so the 12,769 panchayats are a plan and not yet a connection.",
    "The Telangana Information Technology Department and DBN should publish the panchayat-wise schedule of the 12,769 panchayats with the milestone dates in the agreement.",
    "telangana")

s3 = insight(
    "4G saturation: 60.7% of towers commissioned, 30.8% of cost disbursed, due December 2026",
    bars("4G saturation had 60.7% of towers up and 30.8% of the cost disbursed on 28 February 2026",
         [("Towers commissioned: 14,301 of 23,570", 100 * G4_DONE / G4_PLAN),
          ("Project cost disbursed: Rs 9,417.88 crore of Rs 30,620 crore", 100 * G4_SPENT / G4_COST)],
         accent="Project cost disbursed: Rs 9,417.88 crore of Rs 30,620 crore", unit="%", vmax=100,
         sub="Per cent; both shares computed here from the report&rsquo;s status table (para 16) and Annexure I. The two measures need not move together, because subsidy follows commissioning and quarterly uptime payments.",
         source="Standing Committee 32nd Report, para 16, para 93 and Annexure I (official).")
    + numbers(["Project", "Cost, Rs crore", "Towers done", "Share done", "Disbursed, Rs crore"],
              [["4G saturation (BSNL)", "30,620", "14,301 of 23,570", "60.7%", "9,417.88"],
               ["Border outpost and border intelligence post (BSNL)", "737 in Annexure I; 1,546 in the status table", "251 of 602", "41.7%", "119.93"],
               ["Left-wing extremism phase II", "1,578", "1,186 of 1,377", "86.1%", "683.47"],
               ["7,287 Aspirational District villages", "2,876", "3,050 of 3,747", "81.4%", "1,357.36"],
               ["All major mobile projects (status table)", "42,467", "24,198 of 34,780", "69.6%", "not given"],
               ["Eleven projects in Annexure I", "40,009", "not given", "not given", "13,461.12 (33.6% of cost)"]],
              "Show the project figures and the report&rsquo;s conflicts"),
    "The Committee called for priority on the 4G saturation and border outpost projects, and the report itself gives different costs for three projects in two places, which makes a share of cost disbursed uncertain for those three.",
    "The Department should publish one project-wise table giving approved cost, taxes, towers planned, towers commissioned and subsidy disbursed on a single date.",
    "mobile")

s4 = insight(
    "Liquidated damages: Rs 31.01 crore in 2025-26, 66.7% of the six-year total",
    bars("Liquidated damages were Rs 46.46 crore since 2020-21, two-thirds of it in 2025-26",
         [(f"{y}", v) for y, v in LD.items()], accent="2025-26", unit="₹ crore", vmax=32,
         sub="Liquidated damages imposed on implementers of fund projects, Rs crore, up to 28 February 2026; the maximum is 10% of the subsidy for a site, and 5% of subsidy is the penalty for a site not built. The share and the multiples are computed here.",
         source="Standing Committee 32nd Report, para 93 to 94 and Annexure II (official).")
    + numbers(["Financial year", "Liquidated damages, Rs crore"],
              [[y, f"{v:,.2f}"] for y, v in LD.items()] + [["Total", "46.46"]], "Show the figures by year"),
    "The levy rose 4.9 times from 2024-25 to 2025-26, after office memoranda of 22 September 2025 directed damages on delayed sites in five schemes, so the figure reflects when enforcement began as much as how late the sites were.",
    "The Department should publish liquidated damages by scheme and operator with the days of delay for each site, so that the amount can be read against the delay.",
    "damages")

recs = numbers(["Recommendation", "What the Committee recommended"],
               [["No. 3", "A model-wise and State-wise performance audit of BharatNet, because operational gram panchayats remain below envisaged coverage and progress is uneven"],
                ["No. 4", "A focused strategy to raise BharatNet utilisation, with more home fibre connections and targeted, outcome-oriented use of fund money"],
                ["No. 5", "Finish pending Amended BharatNet packages and State-led strategies, closer coordination among BSNL, States and agencies, and milestone-based monitoring of each package"],
                ["No. 7", "Scheme-wise monitoring and strict timelines for mobile projects, with priority to 4G saturation and the border outpost scheme"],
                ["No. 10", "Standard guidelines for technology selection, timely approval of alternate technologies in difficult areas, and a mechanism to monitor reliability and minimum assured speeds"],
                ["No. 12", "Stronger third-party audit with time-bound compliance by operators, support for BharatNet Udyamis, and action on audit findings such as data outages, coverage gaps and weak signal"],
                ["No. 16", "Better appraisal and costing, performance-linked incentives and disincentives for public sector agencies, and one monitoring framework for fund and BharatNet projects"]],
               "Show the seven recommendations in the press release")

conflicts = ('<details class="xv-n"><summary>Where the report&rsquo;s own figures differ</summary><ul>'
             '<li><b>Operational panchayats:</b> the report gives 78,899 gram panchayats with operational points of presence, said to include 40,610 under phase I, 38,289 under phase II and 2,884 under the Amended BharatNet Programme; 40,610 plus 38,289 is 78,899, so the third term is either not included or the total is stated without it (computed sum of all three: 81,783).</li>'
             '<li><b>Project costs:</b> the border outpost scheme costs Rs 737 crore in Annexure I and Rs 1,546 crore in the status table; Lakshadweep Rs 63 crore and Rs 36 crore; the Andaman and Nicobar project Rs 110 crore and Rs 130 crore.</li>'
             '<li><b>4G saturation cost:</b> the Cabinet approved Rs 26,316 crore excluding taxes on 27 July 2022, and the report tables show Rs 30,620 crore; the Rs 4,304 crore difference is not explained in the passages read (taxes are the likely cause but the report does not say so).</li>'
             '<li><b>Mobile project totals:</b> the status table covers Rs 42,467 crore of projects and Annexure I Rs 40,009 crore, as the two lists are not the same projects.</li>'
             '<li><b>Phase I coverage:</b> the scope was raised to 1,20,210 gram panchayats, of which 40,610 are operational (33.8%, computed); the report also says over one lakh were completed by December 2017, so &lsquo;completed&rsquo; and &lsquo;operational&rsquo; mean different things.</li>'
             '</ul></details>\n')

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Department of Telecommunications:</b> publish annual levy collections, budget allotment, appropriation and actual spending of the fund in one table, so that collections can be read against disbursals.</li>
<li><b>Digital Bharat Nidhi administration:</b> publish for every BharatNet phase and state the panchayats connected, lit and in use next to the money disbursed.</li>
<li><b>Department of Telecommunications:</b> reconcile the project costs, tower counts and operational panchayat totals in the report, and publish one dated project table.</li>
<li><b>Department of Telecommunications:</b> publish liquidated damages by scheme, operator and days of delay, with the reason for any waiver.</li>
<li><b>Ministry of Communications:</b> table the action-taken reply to the Committee&rsquo;s seven highlighted recommendations with a date for each.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The report (105 pages, presented to Lok Sabha on 6 August 2026 and signed on 5 August 2026) and its two-page press release were read in full as PDFs from sansad.in; paragraph and annexure numbers are cited beside each figure.</li>
<li>Expenditure figures are in Rs crore and are as on 28 February 2026 unless stated. &lsquo;Disbursed&rsquo; is the report&rsquo;s word for money released from the fund.</li>
<li>Shares, sums, multiples and the per-panchayat figure are computed here; none is published in the report, except 60.7%, 69.6% and 41.7% tower completion and Rs 40,635 crore, which the report states and the build re-derives.</li>
<li>The Telangana figures of Rs 3,189 crore and 12,769 panchayats are from the PIB release of 6 November 2026, read in full.</li>
<li>The recommendation numbers are those printed in the press release; the report contains more recommendations than the seven in the release.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>Collections against disbursements: the report states the levy rate (5% of Adjusted Gross Revenue) and gives disbursals, but no table of annual levy collections or of the fund balance appeared in the text read, so the fund&rsquo;s collections cannot be set against what was disbursed from this report alone.</li>
<li>Scheme-wise outlay and spend for every scheme: spend figures are given for BharatNet by state and by year and for eleven mobile projects; the outlay for the Amended BharatNet Programme (Rs 1.39 lakh crore, approved 4 August 2023) has no matching spend because the report gives none for it.</li>
<li>How many of the 78,899 operational panchayats are in use: the report gives usage figures for some projects, but no figure for connected panchayats with active traffic.</li>
<li>The cause of the 38.5% shortfall in BharatNet spend in 2023-24 and 2024-25: no reason is given in the passages read.</li>
<li>Whether the Rs 3,189 crore for Telangana is a ceiling or a commitment, and how much of it falls in each year: the PIB release says financial support is approved.</li>
<li>The Department&rsquo;s reply to the Committee: an action-taken report had not been located at the time of analysis.</li>
</ul></details>
'''

body = STYLE + top + mech + s1 + s2 + s2b + s3 + s4 + recs + conflicts + fixes + method + gaps

SOURCES = (
    '<a href="https://sansad.in/getFile/app/lsscommittee/Communications%20and%20Information%20Technology/18_Communications_and_Information_Technology_32.pdf?source=app">Thirty-second Report, Standing Committee on Communications and Information Technology (2025-26), presented 6 August 2026</a> (official, read in full); '
    '<a href="https://sansad.in/getFile/app/lsscommittee/Communications%20and%20Information%20Technology/pr_files/Press%20Release%20of%2032nd%20Report.pdf?source=app">Press release of the report, Lok Sabha Secretariat, 6 August 2026</a> (official); '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2333683&amp;lang=2&amp;reg=48">PIB, Department of Telecommunications, 6 November 2026: agreement for the Amended BharatNet Program in Telangana</a> (official, read in full). '
    'Shares, sums and ratios computed by this blog. Analysed 25 November 2026.')
RELATED = [("https://blog.vertistratsolution.com/2026/11/telangana-cabinet-5-november-2026-rs.html", "Telangana cabinet, 5 November 2026: Rs 4,193 crore for three Kaleshwaram barrages")]

build("Telecom &middot; Digital Bharat Nidhi", TITLE,
      "A parliamentary committee reviewed the fund that pays for rural broadband and mobile towers; this piece sets out its spending, delays and recommendations, and where the report&rsquo;s figures differ.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
