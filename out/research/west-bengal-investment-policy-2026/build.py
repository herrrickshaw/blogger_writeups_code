"""West Bengal Investment Promotion Policy, 2026 (in force from 9 May 2026, unveiled Thursday 5 November 2026): the assistance ceilings, the annual limits and what they imply,
the incentive fund against the estimated backlog, the state's clocks, and the places where press accounts differ from the policy booklet.
Build from the repo root:  python3 out/research/west-bengal-investment-policy-2026/build.py            (writes out/post-west-bengal-investment-policy-2026.html)
                           python3 out/research/west-bengal-investment-policy-2026/build.py --check    (arithmetic and asserts only)
Every figure is from the source named beside it, or computed below with an assert. Analysed 21 November 2026.
Official document (text fetched): West Bengal Investment Promotion Policy, 2026, launch booklet of the West Bengal Industrial Development Corporation (wbidc.com): the Preface, Executive Summary and
Investor's Guide with clause references. The booklet states that it summarises the Policy and that the Policy and the Scheme prevail where they differ; the Policy itself and the
West Bengal Investment Promotion Scheme, 2026 were not found.
Reports (search excerpts, most of them the opening of the article): KPMG Flash News 6 Nov (page text fetched), Business Standard 5 and 12 Nov, The Hindu 5 and 6 Nov, BusinessLine 5 and 6 Nov,
Economic Times 5 Nov, Indian Express 4 Nov, ETV Bharat 5 Nov, NDTV 7 Nov, Suvidha Consultancy synopsis (a consultant's note)."""
import datetime as dt
import html as _h
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
OUT = ROOT / "out/post-west-bengal-investment-policy-2026.html"
STEPS = 8


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. dates
step(1, "dates and weekday checks")
for d, wd in [(D(2026, 5, 9), "Saturday"), (D(2026, 11, 4), "Wednesday"), (D(2026, 11, 5), "Thursday"), (D(2026, 11, 12), "Thursday")]:
    assert d.strftime("%A") == wd, d
assert (D(2026, 11, 5) - D(2026, 5, 9)).days == 180               # in force 180 days before it was unveiled
assert (D(2026, 11, 12) - D(2026, 11, 5)).days == 7

# ---- 2. ceilings and annual limits (booklet, Investor's Guide, Cl. 19, 20, 24, 25)
step(2, "ceilings, annual limits and the years needed to draw them")
UNITS = [("Regular unit", 100, 15), ("Thrust Sector unit", 110, 20), ("Unit in a Priority Area", 110, 20), ("Thrust Sector unit in a Priority Area", 120, 20)]   # name, ceiling % of Eligible FCI, annual limit %
YEARS = {n: round(c / a, 2) for n, c, a in UNITS}
assert YEARS == {"Regular unit": 6.67, "Thrust Sector unit": 5.5, "Unit in a Priority Area": 5.5, "Thrust Sector unit in a Priority Area": 6.0}
assert all(c / a < 10 for _, c, a in UNITS)                        # every unit can reach its ceiling inside the 10-year window
SLACK = {n: round(10 - y, 2) for n, y in YEARS.items()}
assert SLACK == {"Regular unit": 3.33, "Thrust Sector unit": 4.5, "Unit in a Priority Area": 4.5, "Thrust Sector unit in a Priority Area": 4.0}
# the booklet's own worked example: a Thrust Sector unit in a Priority Area invests Rs 200 crore
EX_FCI = 200
assert EX_FCI * 120 / 100 == 240 and EX_FCI * 20 / 100 == 40 and 240 / 40 == 6.0     # up to Rs 240 crore in total, at most Rs 40 crore a year, so six years at the least
# the same arithmetic at the Strategic and Mega threshold: Eligible FCI above Rs 500 crore (own land) or Rs 1,000 crore (State-allotted land)
for fci in (500, 1_000):
    assert [fci * c / 100 for _, c, _ in UNITS] == [fci * 1.0, fci * 1.1, fci * 1.1, fci * 1.2]
assert 500 * 1.2 == 600 and 500 * 20 / 100 == 100 and 500 * 15 / 100 == 75
# net SGST needed to draw the annual limit from SGST alone, if net SGST is the SGST rate times value added (all inputs creditable): value added as a multiple of plant and machinery
VA_MULT = {rate: round(15 / rate, 2) for rate in (9, 6, 2.5)}      # SGST at 9% (goods at 18% GST), 6% (12%) and 2.5% (5%); 15% is the annual limit for a regular unit
assert VA_MULT == {9: 1.67, 6: 2.5, 2.5: 6.0}

# ---- 3. the money: Budget provision against the estimated backlog (Business Standard 5 and 12 Nov; Adhikari quoted)
step(3, "fund against backlog")
FUND, BACKLOG = 5_000, 50_000
assert BACKLOG / FUND == 10.0
assert FUND / (500 * 20 / 100) == 50.0                            # one year of maximum claims from 50 units at the Rs 500 crore threshold, drawing 20% of plant and machinery

# ---- 4. the state's clocks and the smaller caps (Cl. 28, 32, 33, 39-42, 45, 71-75)
step(4, "clocks, caps and thresholds")
CLOCKS = [("Deficiency notice", 7), ("Certificate of Intent", 30), ("Certificate of Eligibility", 45), ("Claim sanction", 30)]
assert sum(d for n, d in CLOCKS[1:]) == 105                        # three approval clocks, excluding the 7-day notice, the build and the claim preparation
assert 4 / 0.05 == 80                                              # interest subvention: the lower of Rs 4 crore and 5% of the loan; they cross at a loan of Rs 80 crore
assert 20 / 0.5 == 40 and 25 / 0.5 == 50                           # lease rental: the lower of Rs 20 (Rs 25) a sq ft and half the rent; they cross at rents of Rs 40 (Rs 50)
assert 1_000 * 10 / 100 + 1_000 * 10 / 100 == 200                  # large projects (Eligible FCI above Rs 1,000 crore): up to 10% plus 10% of Eligible FCI for infrastructure, Rs 200 crore at Rs 1,000 crore
THRUST = ["Semiconductors and electronics", "Green hydrogen and waste-to-energy", "Emerging digital technologies", "Electric vehicles and batteries", "Defence",
          "Food and marine processing", "Textiles", "Biotech, pharma and medical devices", "Critical minerals processing", "Automobile manufacturing", "Research and development",
          "Specialty steel", "Petrochemicals", "Aviation", "Shipbuilding and maritime training"]
STRATEGIC = ["Semiconductors", "EVs", "Advanced batteries", "Green hydrogen", "Specialty steel", "Defence", "Gems and jewellery", "Data centres", "Petrochemicals", "Textile parks", "Multi-modal logistics parks"]
assert len(THRUST) == 15 and len(STRATEGIC) == 11

TITLE = "West Bengal investment policy 2026: 100% to 120% ceilings, Rs 5,000 crore fund"
plain = _h.unescape(TITLE)
assert 55 <= len(plain) <= 90, len(plain)
assert not any(w in plain.lower().split() for w in ("you", "your", "we", "our"))
print(f"consistency checks passed (dates, ceilings and years, worked example, fund and backlog, clocks); title {len(plain)} characters", flush=True)
if "--check" in sys.argv:
    sys.exit(0)

from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

step(5, "writing sections")
top = top_line([
    ("100% to 120%", " of plant and machinery cost is the ceiling on total assistance, drawn at no more than 15% to 20% a year, so the full ceiling takes at least 5.5 to 6.7 years."),
    ("10 times", " as much as the Rs 5,000 crore set aside for 2026-27 is the estimated Rs 50,000 crore of earlier incentives, which the policy does not cover."),
    ("2 reports", " read state the 120% ceiling as available more widely than the policy allows; the booklet gives it only to a thrust-sector unit in a priority area."),
])

tvo = ('<table class="gb-table"><thead><tr><th>Kind</th><th>What this piece includes</th></tr></thead><tbody>'
       '<tr><td><b>Decided</b></td><td>The West Bengal Investment Promotion Policy, 2026 applies to eligible investment made on or after 9 May 2026 and was unveiled by Chief Minister Suvendu Adhikari on Thursday 5 November 2026, 180 days later.</td></tr>'
       '<tr><td><b>Rules</b></td><td>A ceiling of 100%, 110% or 120% of plant and machinery cost, an annual limit, up to ten years from production, and a list of reimbursements for SGST, electricity duty, EPF, stamp duty and other costs.</td></tr>'
       '<tr><td><b>Targets</b></td><td>None found. No investment, jobs or number-of-units target was printed in the booklet or in the reports.</td></tr>'
       '<tr><td><b>Outcomes</b></td><td>None. No Certificate of Intent, sanction or payment under the policy was reported.</td></tr>'
       '</tbody></table>\n')

CE = [(n, c) for n, c, a in UNITS]
s1 = insight(
    "The 120% ceiling needs both a thrust sector and a priority area",
    bars("Ceiling on total assistance, per cent of plant and machinery cost, by type of unit",
         CE, accent="Thrust Sector unit in a Priority Area", unit="%", vmax=130,
         sub="Per cent of Eligible FCI, the investment in plant and machinery including pollution control equipment made on or after 9 May 2026 and certified by an auditor, excluding land, working capital and pre-operative costs. A service unit in a thrust sector gets 110%. Assistance ends when the ceiling is reached or 10 years after production starts, whichever is earlier.",
         source="West Bengal Investment Promotion Policy, 2026, launch booklet of the West Bengal Industrial Development Corporation (Investor's Guide, clauses 19, 20, 24, 25 and 38; official).")
    + flow([("2025", "West Bengal revokes its earlier state industrial incentive schemes by a Gazette bill, retroactive to each scheme&rsquo;s notification (this blog&rsquo;s post of 9 September 2026; Business Standard, 5 November 2026, calls it a retrospective withdrawal)."),
            ("9 May 2026 (Saturday)", "The policy is deemed in force; the new government took office this day (Business Standard)."),
            ("June 2026", "The state Budget allocates Rs 5,000 crore for the current year to fund the policy (Business Standard, 12 November 2026)."),
            ("4 Nov 2026 (Wednesday)", "Indian Express previews the policy; its EPF terms match the booklet."),
            ("5 Nov 2026 (Thursday)", "Chief Minister unveils the policy, calling it &lsquo;a very small beginning&rsquo; (Business Standard).", True),
            ("12 Nov 2026 (Thursday)", "Business Standard notes that a separate land policy is in the offing and that delivery, especially on land, is the test.")])
    + numbers(["Account", "What it says about 120%", "Matches the booklet?"],
              [["Booklet, Investor&rsquo;s Guide (official)", "100% regular; 110% for a thrust-sector unit or a unit in a priority area; 120% for a thrust-sector unit in a priority area; 110% for a service unit in a thrust sector", "Reference"],
               ["KPMG, 6 November; The Hindu, 5 November; Economic Times, 5 November", "The same three tiers", "Yes"],
               ["Business Standard, 5 November", "Up to 120% for units in thrust sectors located in priority areas; 100% for regular units", "Yes"],
               ["ETV Bharat, 5 November", "100% general; thrust sectors 110%; priority or underdeveloped areas &lsquo;up to 120%&rsquo;", "No: a priority area alone gets 110%"],
               ["NDTV, 7 November", "The state &lsquo;will extend 120 per cent support to any industry&rsquo; setting up in the state", "No: a regular unit gets 100%"],
               ["Suvidha Consultancy synopsis (consultant)", "120% for a thrust-sector unit in a priority area, except a service unit", "Yes; the booklet gives such a service unit 110%"]],
              "Show how each account describes the 120% ceiling"),
    "The 120% ceiling is the top of a ladder that needs both a thrust sector and a priority area, and two of the reports read state it as available more widely.",
    "The industries department should publish the ceiling for each type of unit in one table with its clause number, and repeat it in each release.",
    "ceiling")

YR = [("Regular unit (15% a year)", YEARS["Regular unit"]), ("Thrust Sector or Priority Area unit (20% a year)", YEARS["Thrust Sector unit"]),
      ("Thrust Sector unit in a Priority Area (20% a year)", YEARS["Thrust Sector unit in a Priority Area"])]
s2 = insight(
    "A unit can draw its full ceiling in 5.5 to 6.7 years, inside the 10-year window",
    bars("Shortest time to draw the full ceiling: 5.5 to 6.7 years of a 10-year window",
         YR, accent=YR[0][0], unit=" years", fmt=lambda v: f"{v:.1f} years", vmax=10,
         sub="Years, computed here as the ceiling divided by the annual limit: 100 divided by 15, 110 divided by 20 and 120 divided by 20. The booklet&rsquo;s own example is a thrust-sector unit in a priority area investing Rs 200 crore, which can receive up to Rs 240 crore and at most Rs 40 crore a year, six years at the shortest.",
         source="West Bengal Investment Promotion Policy, 2026, launch booklet (Investor&rsquo;s Guide, clauses 24 and 25; official). Years computed here.")
    + numbers(["Item", "Value", "Source and status"],
              [["Annual limit", "15% of Eligible FCI for a regular unit; 20% for a unit in a priority area or thrust sector", "Booklet (official)"],
               ["Slack in the 10-year window", f"{SLACK['Regular unit']:.1f} years for a regular unit, {SLACK['Thrust Sector unit']:.1f} years for a unit in a thrust sector or priority area, and {SLACK['Thrust Sector unit in a Priority Area']:.1f} years for both (computed)", "Computed here"],
               ["Rupees at the mega threshold", "At Eligible FCI of Rs 500 crore: a ceiling of Rs 500 crore, Rs 550 crore or Rs 600 crore, and at most Rs 75 crore or Rs 100 crore a year (computed); a Strategic and Mega Project may apply for higher overall and annual ceilings", "Computed from the booklet"],
               ["SGST alone", "To draw the 15% annual limit from net SGST alone, annual value added must be 1.67 times plant and machinery at an SGST rate of 9%, 2.5 times at 6% and 6 times at 2.5% (computed; assumes every input is creditable)", "Illustration, computed here"],
               ["What counts as net SGST", "SGST paid in cash after input tax credit; tax paid with IGST credit, tax under dispute and tax later refunded do not count", "Booklet (official)"],
               ["Reduction", "A shortfall in investment or employment reduces assistance in proportion; it does not withdraw it", "Booklet (official)"]],
              "Show the annual limits, the rupee examples and the checks"),
    "A unit can reach its ceiling in 5.5 to 6.7 years, so the 10-year window is not the limit, and what limits assistance is how much SGST, electricity duty and EPF the unit actually pays.",
    "The industries department should publish, for each type of unit, a worked example showing the tax and contributions paid and the assistance claimed in each year.",
    "years")

FB = [("Provision in the 2026-27 Budget", FUND), ("Backlog of earlier incentives, estimated", BACKLOG)]
s3 = insight(
    "Incentive fund: Rs 5,000 crore for 2026-27 against an estimated Rs 50,000 crore backlog",
    bars("Rs 5,000 crore set aside against an estimated Rs 50,000 crore of earlier incentives",
         FB, accent=FB[0][0], unit=" crore", fmt=lambda v: f"Rs {v:,.0f} crore", vmax=55_000,
         sub="Rs crore. The provision is the Budget allocation for the current year to fund the policy; the backlog is an estimate of incentives promised under earlier regimes, which Business Standard reports remains outside the policy. The backlog is 10 times the provision (computed); the sources do not say how the two relate in the accounts.",
         source="Business Standard, 5 and 12 November 2026 (secondary; the backlog is an estimate attributed to no named document); Chief Minister Suvendu Adhikari as quoted by Business Standard; booklet (official) for the fund&rsquo;s rules.")
    + numbers(["Item", "Value", "Source and status"],
              [["Fund", "Sanctioned assistance is paid from a dedicated, non-lapsable Assured Incentive Fund; terms are fixed on the date of the Certificate of Intent and later amendments cannot reduce them", "Booklet (official); Business Standard, 12 November"],
               ["Scale", "Rs 5,000 crore equals one year of maximum claims from 50 units at the Rs 500 crore mega threshold in a thrust sector or priority area, at Rs 100 crore each (computed)", "Computed here"],
               ["When claims start", "A claim needs a Certificate of Eligibility, which a unit applies for within 6 months of starting production; the policy covers investment from 9 May 2026 only", "Booklet (official)"],
               ["Backlog", "Business Standard: estimated at Rs 50,000 crore and outside the policy. NDTV: the Chief Minister called it a legacy of the past that the government would gradually begin addressing", "Conflict: not reconciled"],
               ["Industry view", "Bengal Chamber of Commerce calls the fund the single biggest relief for industry; a Khaitan consultant says a commitment backed by a reserve fund is unusual", "Economic Times; Business Standard (opinion)"],
               ["Past record", "The earlier schemes were revoked retroactively, which is why the lock-in at the Certificate of Intent matters", "This blog&rsquo;s post of 9 September 2026; Business Standard"]],
              "Show the fund, the backlog and what is not known"),
    "The fund is ten times smaller than the estimated backlog that the policy leaves out, and no report says whether any of the Rs 5,000 crore will go to old claims.",
    "The state should publish the size, source and quarterly payments of the Assured Incentive Fund, and either a settlement schedule for the backlog or a statement that it is excluded, with a verified figure.",
    "fund")

s4 = insight(
    "The policy sets four clocks of 7 to 45 days and locks terms at the Certificate of Intent",
    bars("State clocks in days: 7 for a deficiency notice, 30, 45 and 30 for approvals and claims",
         CLOCKS, accent="Certificate of Eligibility", unit=" days", vmax=55,
         sub="Days the state has committed to, from the booklet: a deficiency in an application is raised once within 7 days; a Certificate of Intent within 30 days; a Certificate of Eligibility within 45 days of a complete application after production starts; a complete claim sanctioned within 30 days. The three approval clocks add to 105 days (computed), excluding the build and the unit&rsquo;s own preparation. No separate clock for the payment after sanction was found; the booklet&rsquo;s words &lsquo;sanctioned, and paid directly&rsquo; do not say whether the 30 days include payment.",
         source="West Bengal Investment Promotion Policy, 2026, launch booklet (Investor&rsquo;s Guide, clauses 71 to 75; official); KPMG Flash News, 6 November 2026 (secondary).")
    + numbers(["Benefit", "Terms", "Source and status"],
              [["Manufacturing and other units", "SGST-linked assistance of 100% of net SGST for up to 10 years; electricity duty reimbursed for up to 5 years; stamp duty and registration on the first purchase or lease of project land; R&amp;D assistance of 50% (75% for 100% export-oriented units) up to Rs 5 crore in 10 milestone instalments", "Booklet (official), clauses 26, 27, 29; KPMG"],
               ["MSMEs", "Interest subvention up to 50% of interest for 5 years, capped at the lower of Rs 4 crore and 5% of the loan (equal at a loan of Rs 80 crore, computed); EPF reimbursement 50% for men and 100% for women and transgender employees for 10 years, up to Rs 5 crore a year; technology upgrade help up to Rs 50 lakh", "Booklet (official), clauses 28, 32; Suvidha (technology)"],
               ["Large units, strategic and mega projects", "EPF reimbursement of up to 50% for 5 years, up to Rs 10 crore a year, for units that employ at least 200 people in a priority area or 400 elsewhere", "Booklet (official), clause 33"],
               ["Service units", "A separate set for 5 years: 100% of net SGST up to Rs 10 crore a year; EPF 50% (75% for women) above 200 eligible employees, up to Rs 10 crore a year; electricity duty for 3 years (5 in a priority area); lease rental the lower of Rs 20 a sq ft a month (Rs 25 in a priority area) and half the rent. A unit takes this set or the manufacturing set, not both", "Booklet (official), clauses 39 to 42"],
               ["Strategic and Mega Projects", "Any two of three tests: Eligible FCI above Rs 500 crore (own land) or Rs 1,000 crore (State-allotted land); one of 11 strategic sectors; at least 50 direct jobs for every acre of project land. They may apply for tailor-made benefits and, above Rs 1,000 crore, infrastructure support of up to 10% plus 10% of Eligible FCI, which is Rs 200 crore at Rs 1,000 crore (computed)", "Booklet (official), clause 45; BusinessLine"],
               ["Thrust sectors", "15 listed: semiconductors and electronics; green hydrogen and waste-to-energy; emerging digital technologies; electric vehicles and batteries; defence; food and marine processing; textiles; biotech, pharma and medical devices; critical minerals processing; automobile manufacturing; research and development; specialty steel; petrochemicals; aviation; shipbuilding and maritime training", "Booklet (official), Annexure III"],
               ["Priority areas", "Sub-divisions scoring below the State median on an index of industry and infrastructure, reviewed every three years; the list and the number of sub-divisions were not found", "Booklet (official)"],
               ["Green power", "Cross-subsidy and additional surcharge on green power from sources in West Bengal waived until March 2030", "Booklet (official), clause 53; ETV Bharat"],
               ["Named officers", "A Special Secretary-level officer above Rs 1,000 crore and a Secretary-level officer above Rs 2,500 crore, with monthly review by the Chief Secretary", "KPMG; booklet (official)"],
               ["Exclusions", "Polluting industries such as sponge iron, traditional brick kilns, fireworks and single-use plastics are reported as excluded; the exclusion list was not read in the booklet text", "ETV Bharat (secondary)"],
               ["Pre-release EPF ladder", "A report quoted by NDTV on 7 November described 50% support for 100 employees and up to 70% for 500; the booklet has 50% at 200 or 400 employees and no 70% tier", "Conflict: the booklet is used"]],
              "Show every benefit, threshold and the conflicts"),
    "The state has bound itself to 105 days of approval and sanction time, with the terms locked for each investor at the Certificate of Intent.",
    "The industries department should publish, every quarter, the number of Certificates of Intent and Eligibility issued, claims sanctioned and paid, and days taken against the clocks.",
    "clocks")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>West Bengal industries department:</b> publish the Policy itself, the West Bengal Investment Promotion Scheme, 2026 and the list of priority-area sub-divisions with their index scores.</li>
<li><b>West Bengal finance and industries departments:</b> publish the size, source and quarterly payments of the Assured Incentive Fund, and state what part of the Rs 5,000 crore, if any, is for earlier claims.</li>
<li><b>West Bengal government:</b> publish a verified figure for the backlog of earlier incentives and a settlement schedule, or state plainly that it is excluded.</li>
<li><b>West Bengal industries department:</b> report every quarter the Certificates of Intent and Eligibility issued, investment and jobs recorded, claims sanctioned and paid, and days taken against each clock.</li>
<li><b>West Bengal industries department:</b> state the ceiling for each type of unit, with its clause, in every release, and state whether the 30-day claim clock includes payment to the unit.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The booklet of the West Bengal Industrial Development Corporation is the source for the rules; it summarises the Policy and says the Policy and the Scheme prevail where they differ. Clause numbers are as the booklet prints them.</li>
<li>A ceiling is a cap on total assistance as a share of Eligible FCI; an annual limit is a cap on any one year; neither is an amount the state pays automatically, since the assistance reimburses taxes and contributions the unit has paid.</li>
<li>Years to draw the ceiling, rupee examples, break-even loan and rent figures, the ratio of backlog to provision and the value-added multiples are computed here and each is checked by an assertion in the builder. The value-added multiples assume that net SGST is the SGST rate times value added with every input creditable; they are an illustration, not a forecast.</li>
<li>KPMG was read as page text; the Business Standard, The Hindu, BusinessLine, Economic Times, Indian Express, ETV Bharat and NDTV items were read as excerpts, mostly the opening of the article. News sites are secondary, and the Suvidha note is a consultant&rsquo;s summary.</li>
<li>Weekdays were checked against the calendar.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The text of the Policy and of the West Bengal Investment Promotion Scheme, 2026; only the booklet that summarises them was read, and only as extracted text.</li>
<li>Any investment, jobs or number-of-units target for the policy; none was printed.</li>
<li>The Rs 50,000 crore backlog beyond Business Standard&rsquo;s estimate: no named document, and the Chief Minister&rsquo;s own statement on it is reported differently by NDTV.</li>
<li>Whether any of the Rs 5,000 crore is meant for earlier claims, and the size of the Assured Incentive Fund beyond that provision.</li>
<li>The list and number of priority-area sub-divisions, and the exact exclusion list.</li>
<li>Whether the land the Finance Minister says is available for the next two to three years exists in the quantity stated; it is his statement in an interview.</li>
<li>Any Certificate of Intent, sanction or payment under the policy, and whether the 30-day claim clock includes payment after sanction.</li>
</ul></details>
'''

step(7, "assembling body")
body = STYLE + top + tvo + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://wbidc.com/assets/pdf/WBIP_2026_Launch_Booklet.pdf">West Bengal Investment Promotion Policy, 2026, launch booklet (WBIDC)</a> and its '
    '<a href="https://wbidc.com/assets/pdf/WBIP_2026_Launch_Booklet_English.pdf">English executive summary</a> (official; document text); '
    '<a href="https://assets.kpmg.com/content/dam/kpmgsites/in/pdf/2026/11/KPMG-Flash-News-West-Bengal-Investment-Promotion-Policy-2026.pdf">KPMG Flash News, 6 November 2026</a> (secondary; page text); '
    '<a href="https://www.business-standard.com/india-news/west-bengal-unveils-new-investment-policy-offers-up-to-120-assistance-126110502088_1.html">Business Standard, 5 November 2026</a> and '
    '<a href="https://www.business-standard.com/industry/news/delivering-on-the-promised-land-bengal-s-new-industrial-policy-faces-test-126111201910_1.html">Business Standard, 12 November 2026</a> (secondary); '
    '<a href="https://www.thehindu.com/news/national/west-bengal/key-takeaways-from-the-west-bengal-investment-promotion-policy-2026/article71673497.ece">The Hindu, 6 November 2026</a>, '
    '<a href="https://www.thehindubusinessline.com/economy/west-bengals-new-industrial-policy-offers-employment-linked-incentives-for-investors-dedicated-support-for-large-investment/article71670973.ece">The Hindu BusinessLine, 5 November 2026</a>, '
    '<a href="https://economictimes.indiatimes.com/news/india/west-bengal-investment-policy-puts-jobs-first-offers-up-to-120-assistance-to-industries/articleshow/135572363.cms">Economic Times, 5 November 2026</a> and '
    '<a href="http://indianexpress.com/article/cities/kolkata/west-bengal-investment-policy-2026-epf-incentives-women-msmes-10950934">Indian Express, 4 November 2026</a> (secondary, excerpts); '
    '<a href="https://www.etvbharat.com/en/state/bengals-new-investment-policy-eyes-job-creation-offers-up-to-120-percent-govt-aid-and-tax-concessions-enn26110506171">ETV Bharat, 5 November 2026</a> and '
    '<a href="https://www.ndtv.com/india-news/can-suvendu-adhikari-deliver-industrial-renaissance-bengals-been-waiting-for-12296704">NDTV, 7 November 2026</a> (secondary, excerpts; the two accounts of the 120% ceiling that differ from the booklet); '
    '<a href="https://www.suvidhagroup.in/wp-content/uploads/2026/11/WB_Investment_Promotion_Policy_2026_Synopsis_Suvidha.pdf">Suvidha Consultancy synopsis</a> (a consultant&rsquo;s summary, excerpt). '
    'Percentages, years, rupee examples and ratios computed by this blog. Analysed 21 November 2026.')
B = "https://blog.vertistratsolution.com"
RELATED = [(f"{B}/2026/09/fourteen-states-reimburse-investors.html", "SGST reimbursement: 14 states offer it to investors as a subsidy, not a GST refund"),
           (f"{B}/2026/08/indias-state-incentive-war-gujarats.html", "State investment incentives in India: offers easy to compare, payouts hard to trace")]

step(8, "writing page")
build("Policy &middot; West Bengal", TITLE,
      "West Bengal's Investment Promotion Policy, 2026, unveiled on 5 November 2026, caps total assistance at 100% to 120% of plant and machinery cost; this piece sets out what the ceilings and annual limits imply, the fund against the estimated backlog, the state's clocks, and where press accounts differ from the policy booklet.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(plain), "chars in title")
