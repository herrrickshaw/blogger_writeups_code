"""Karnataka State Civil Aviation Policy 2026: cabinet approval of 19 November 2026, what is and is not known about its content,
the regional-airport baseline (movements, passengers, UDAN support periods), and the Hassan airport cost revision approved the same day.
Build from the repo root:  python3 out/research/karnataka-civil-aviation-policy-2026/build.py   (writes out/post-karnataka-civil-aviation-policy-2026.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 21 November 2026.
The policy text was not found. The approval rests on one wire report (IANS); the content rests on the minister's statements of 10 and 18 November.
Sources were read as search excerpts, apart from parliamentary answers (excerpts) and the PIB releases (excerpts); the post says so."""
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

OUT = ROOT / "out/post-karnataka-civil-aviation-policy-2026.html"
STEPS = 8


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. dates
step(1, "dates and weekday checks")
for d, wd in [(D(2026, 11, 10), "Tuesday"), (D(2026, 11, 18), "Wednesday"), (D(2026, 11, 19), "Thursday"), (D(2026, 11, 20), "Friday"), (D(2026, 11, 21), "Saturday")]:
    assert d.strftime("%A") == wd, d                  # each weekday is the one the report gives
SHIV_OPS = D(2023, 11, 21)                            # Shivamogga operationalised under UDAN, 21 Nov 2023 (Rajya Sabha reply 988, annexure B)
assert SHIV_OPS.replace(year=SHIV_OPS.year + 3) == D(2026, 11, 21)    # three-year support period ends 21 Nov 2026, as The Hindu reports

# ---- 2. Hassan airport (cabinet 19 Nov 2026; The Hindu 20 Nov, PTI, IANS)
step(2, "Hassan airport arithmetic")
H_OLD, H_NEW, H_ADD, H_LAND, H_WORKS = 193.65, 542.96, 349.31, 122.0, 227.31
assert round(H_OLD + H_ADD, 2) == H_NEW and round(H_LAND + H_WORKS, 2) == H_ADD
H_X = H_NEW / H_OLD
assert f"{H_X:.1f}" == "2.8" and f"{100 * H_ADD / H_OLD:.1f}" == "180.4"
assert round(H_ADD) == 349 and round(H_OLD) == 194         # PTI rounds to Rs 349 crore and Rs 193 crore spent; 193.65 is the 2021 sanction, not the amount spent

# ---- 3. regional airports: movements and passengers (TOI 11-12 Nov 2026), Shivamogga, central UDAN expenditure (Lok Sabha 3101)
step(3, "regional airport figures")
MOV_A, MOV_B = 13_180, 5_372                            # Kalaburagi, Hubballi, Mysuru, Belagavi, 2021-22 and 2024-25
assert f"{100 * (MOV_A - MOV_B) / MOV_A:.1f}" == "59.2"
PAX_A, PAX_B = 4.9, 3.3                                 # lakh, as published to one decimal
assert 32 < 100 * (PAX_A - PAX_B) / PAX_A < 33
KLB_A, KLB_B = 79_143, 30_924
assert f"{100 * (KLB_A - KLB_B) / KLB_A:.1f}" == "60.9"
SHV_A, SHV_B = 817, 1_400
assert f"{100 * (SHV_B - SHV_A) / SHV_A:.1f}" == "71.4"
CENTRAL = {"Hubli": 37.69, "Belgaum": 20.88, "Vidyanagar": 5.99, "Bidar": 12.29, "Mysore": 41.40, "Shivamogga": 0.00, "Kalaburgi": 28.64}
assert round(sum(CENTRAL.values()), 2) == 146.89 and len(CENTRAL) == 7       # the seven Karnataka airports in the UDAN annexure
KLB_CLAIM, KLB_TOI, KLB_UDAN = 1000, 175, 28.64                               # minister's figure; TOI 'over Rs 175 crore'; central UDAN expenditure
assert KLB_CLAIM / KLB_TOI > 5.7 and KLB_UDAN < KLB_TOI < KLB_CLAIM
SHV_COST = 583                                                                # Rs crore, The Hindu 12 Nov (KSIIDC)
# Bengaluru and AAI regional traffic, FY2025-26
BLR_M, BLR_INTL, BLR_DOM, BLR_CAP, BLR_2030 = 44.47, 7.23, 37.24, 51.5, 80
assert round(BLR_INTL + BLR_DOM, 2) == BLR_M and f"{100 * BLR_M / BLR_CAP:.1f}" == "86.3" and f"{100 * BLR_2030 / BLR_CAP - 100:.1f}" == "55.3"
HUB, BEL, MYS = 376_286, 301_516, 91_739
REG3 = HUB + BEL + MYS
assert REG3 == 769_541 and f"{100 * REG3 / (BLR_M * 1e6):.2f}" == "1.73"
assert (HUB + BEL + MYS) / 1e5 > 2 * PAX_B          # AAI FY26 for three airports is over twice TOI's 3.3 lakh for four airports in 2024-25: not reconciled (flagged)

# ---- 4. central support: UDAN and Modified UDAN (PIB 25 Mar and 17 Jul 2026; Rajya Sabha replies)
step(4, "Modified UDAN figures")
MU_TOTAL, MU_CAPEX, MU_OM, MU_HELI, MU_VGF = 28_840, 12_159, 2_577, 3_661, 10_043
MU_SUM = MU_CAPEX + MU_OM + MU_HELI + MU_VGF
assert MU_SUM == 28_440 and MU_TOTAL - MU_SUM == 400                        # four components read fall Rs 400 crore short of the total: flagged, fifth component not read
assert 200 * 15 == 3_000 and MU_HELI > 3_000                                 # 200 helipads at Rs 15 crore is Rs 3,000 crore; the stated Rs 3,661 crore is inflation-adjusted
YEARS_UDAN, YEARS_MOD, YEARS_STATE = 3, 5, 10
assert YEARS_STATE == 5 + 5
VGF_TOTAL = {"Jan 2026 (to 2025-26 provisional)": 4494.16, "16 Mar 2026": 4593.28, "20 Jul 2026": 4881}
assert list(VGF_TOTAL.values()) == sorted(VGF_TOTAL.values())               # cumulative disbursement rises with each later date

TITLE = "Karnataka State Civil Aviation Policy 2026: cabinet approval on 19 November 2026"
assert 55 <= len(TITLE) <= 90, len(TITLE)
assert not any(w in TITLE.lower().split() for w in ("you", "your", "we", "our"))

step(5, "writing sections")
top = top_line([
    ("19 November 2026", " is the date the Karnataka cabinet approved the proposal to implement the State Civil Aviation Policy 2026, in one wire report; no policy text, target, outlay or incentive rate was found, so only the minister&rsquo;s statements of 10 and 18 November describe it."),
    (f"Rs {H_NEW} crore", f" is the revised cost approved the same day for Hassan airport, {H_X:.1f} times the Rs {H_OLD} crore sanctioned in 2021."),
    (f"{100 * (MOV_A - MOV_B) / MOV_A:.1f}%", f" is the fall in aircraft movements at four Karnataka UDAN airports from 2021-22 to 2024-25, and the three-year subsidy at Shivamogga ended on 21 November 2026, with the last subsidised flights on 20 November."),
])

tvo = ('<table class="gb-table"><thead><tr><th>Kind</th><th>What this piece includes</th></tr></thead><tbody>'
       '<tr><td><b>Decided</b></td><td>Cabinet approval of the proposal to implement the policy, and the revised Hassan airport cost, on 19 November 2026.</td></tr>'
       '<tr><td><b>Stated, not published</b></td><td>The policy&rsquo;s coverage as the minister described it: financial assistance, viability gap funding, state-managed airports, MRO, manufacturing and the supply chain.</td></tr>'
       '<tr><td><b>Not found</b></td><td>The policy text, its targets, outlay, VGF rates and list of airports.</td></tr>'
       '</tbody></table>\n')

s1 = insight(
    "Cabinet approved the policy on 19 November 2026; no text, target or outlay was found",
    flow([("10 Nov 2026 (Tuesday)", "Infrastructure Development Minister M.B. Patil says a comprehensive civil aviation policy will go to the next cabinet; it covers financial assistance, viability gap funding (VGF) and the management of state-run airports (The Hindu, ANI, Deccan Chronicle)."),
          ("18 Nov 2026 (Wednesday)", "Minister: the policy will be approved at the next cabinet meeting, with priority for MRO, aircraft manufacturing, components and the supply chain, and a suppliers&rsquo; conference before the Global Investors Meet (IANS, ANI)."),
          ("19 Nov 2026 (Thursday)", "Cabinet approves the proposal to implement the Karnataka State Civil Aviation Policy-2026, and administrative approval for Hassan airport at a revised Rs 542.96 crore (IANS; the Hassan item is also in PTI and The Hindu).", True),
          ("20 Nov 2026 (Friday)", "Star Air ends its UDAN flights from Shivamogga as the three-year subsidy period closes; it takes weekend bookings on the Hyderabad route only, at commercial fares without subsidy (The Hindu)."),
          ("21 Nov 2026 (Saturday)", "Date from which no scheduled flights were expected at Shivamogga (The Hindu, 6 and 12 November).")])
    + numbers(["Item", "Statement", "Source and status"],
              [["Approval", "&lsquo;Approved the proposal to implement the Karnataka State Civil Aviation Policy-2026&rsquo;", "IANS, 19 November, as carried by SocialNews and CityAir News (secondary; one wire only)"],
               ["Coverage", "Financial assistance, VGF, grants, operating models for state-managed airports", "The Hindu and ANI, 10 November; Times of India, 11 November (minister&rsquo;s statements)"],
               ["Industry side", "Aircraft manufacturing, components, MRO and the supply chain", "IANS and ANI, 18 November (minister&rsquo;s statement)"],
               ["State-run airports", "Shivamogga, Raichur and Vijayapura, which the state says it will keep managing itself", "Minister, 10 November (Deccan Chronicle, ANI)"],
               ["Text, targets, outlay", "Not found in any report read", "Unknown"]],
              "Show what is stated about the policy and its sources"),
    "Everything known about the policy&rsquo;s content comes from the minister&rsquo;s statements before approval, and the approval itself is reported by one wire service in a list of cabinet decisions.",
    "The Infrastructure Development Department should publish the approved policy with its targets, VGF rates, outlay and list of airports, so that its provisions can be read rather than inferred.",
    "approval")

s2 = insight(
    "Aircraft movements at four Karnataka UDAN airports fell 59.2% from 2021-22 to 2024-25",
    bars("Aircraft movements at four Karnataka UDAN airports fell from 13,180 to 5,372",
         [("2021-22", MOV_A), ("2024-25", MOV_B)], accent="2024-25", vmax=14_000,
         sub=f"Aircraft movements a year at Kalaburagi, Hubballi, Mysuru and Belagavi, together; the fall is computed here ({100 * (MOV_A - MOV_B) / MOV_A:.1f}%). Passengers at the same four fell from 4.9 lakh to 3.3 lakh, about 33% (computed from figures given to one decimal).",
         source="Times of India, 11 and 12 November 2026 (secondary; the basis of the figures is not stated).")
    + numbers(["Item", "Value", "Source and status"],
              [["Movements, four airports", f"{MOV_A:,} in 2021-22; {MOV_B:,} in 2024-25", "Times of India, 12 November (secondary)"],
               ["Passengers, four airports", "4.9 lakh in 2021-22; 3.3 lakh in 2024-25", "Times of India, 12 November"],
               ["Kalaburagi passengers", f"{KLB_A:,} in 2022-23; {KLB_B:,} in 2024-25 ({100 * (KLB_A - KLB_B) / KLB_A:.1f}% lower, computed)", "Times of India, 12 November"],
               ["Shivamogga movements", f"{SHV_A:,} in 2024-25; {SHV_B:,} in 2025-26 ({100 * (SHV_B - SHV_A) / SHV_A:.1f}% higher, computed); IndiGo left in May and SpiceJet in June 2026", "Times of India, 11 November"],
               ["Shivamogga passengers", "About 4.2 lakh in three years, as stated by the local MP", "Times of India, 9 November (a statement, not a record)"],
               ["Shivamogga cost", f"About Rs {SHV_COST} crore, built by the state, handled by KSIIDC", "The Hindu, 12 November"],
               ["AAI traffic, FY2025-26", f"Hubballi {HUB:,}; Belagavi {BEL:,}; Mysuru {MYS:,}; together {REG3:,}, {100 * REG3 / (BLR_M * 1e6):.2f}% of Bengaluru&rsquo;s traffic (computed)", "Airports Authority of India list of 22 May 2026 (official)"],
               ["Bengaluru, FY2025-26", f"{BLR_M} million passengers ({BLR_INTL} million international, {BLR_DOM} million domestic); terminal capacity {BLR_CAP} million, so {100 * BLR_M / BLR_CAP:.1f}% used (computed); {BLR_2030} million planned by 2030", "BLR Airport release of 30 April 2026; Lok Sabha reply 6324 (official)"],
               ["UDAN airports in Karnataka", "Seven: Hubli, Belgaum, Vidyanagar, Bidar, Mysore, Kalaburgi, Shivamogga; central expenditure Rs 146.89 crore in all (computed), of which Rs 0.00 crore at Shivamogga", "Lok Sabha reply 3101, 6 August 2026 (official)"]],
              "Show the airport figures and sources"),
    "The traffic fall was measured to 2024-25, before the policy, and the three airports for which the Airports Authority gives 2025-26 totals (7.7 lakh passengers) exceed the 3.3 lakh given for four airports in 2024-25, so the two series are not on one basis.",
    "The Civil Aviation Department should publish yearly movements, passengers and subsidy paid for each of the state&rsquo;s airports on one basis, with the source of each series.",
    "airports")

s3 = insight(
    "Central support runs 3 years under UDAN and up to 5 under Modified UDAN",
    bars("Support period: 3 years in UDAN, up to 5 in Modified UDAN, 10 in the state proposal",
         [("Original UDAN: three-year concession period", YEARS_UDAN), ("Modified UDAN: VGF up to five years, tapering from year three", YEARS_MOD),
          ("State proposal of 10 November: 5 years, then 5 years shared equally", YEARS_STATE)],
         accent="Modified UDAN: VGF up to five years, tapering from year three", unit=" years", vmax=11,
         sub="Years of support for an airline route. The Modified UDAN figure is from the Government of India description of the scheme approved on 25 March 2026; the state proposal is the minister&rsquo;s account, and the reports differ on who bears the cost of the second five years.",
         source="PIB, 25 March and 17 July 2026 (government releases); Lok Sabha reply 168, January 2026; Deccan Chronicle, 11 November 2026 (minister&rsquo;s statement).")
    + numbers(["Item", "Statement", "Source and status"],
              [["Modified UDAN outlay", f"Rs {MU_TOTAL:,} crore for FY2026-27 to FY2035-36", "PIB, 25 March 2026"],
               ["Components read", f"Aerodromes Rs {MU_CAPEX:,} crore (100 airports); O&amp;M Rs {MU_OM:,} crore (three years, up to Rs 3.06 crore an airport a year); helipads Rs {MU_HELI:,} crore (200 at Rs 15 crore each, inflation-adjusted); VGF Rs {MU_VGF:,} crore over 10 years", "PIB, 25 March and 17 July 2026"],
               ["Check", f"The four components sum to Rs {MU_SUM:,} crore, Rs {MU_TOTAL - MU_SUM} crore below the total; the remaining component was not in the excerpts read", "Computed here"],
               ["Modified UDAN launch", "4 July 2026, to target 120 new destinations and 4 crore passengers in 10 years", "Rajya Sabha starred reply 7, 20 July 2026"],
               ["VGF disbursed to date", "Rs 4,494.16 crore (January 2026 reply, 2025-26 provisional); Rs 4,593.28 crore (16 March); Rs 4,881 crore (20 July)", "Rajya Sabha and Lok Sabha replies"],
               ["Airports not operating under UDAN", "15 on 20 January 2026, including Kalaburagi; the minister said on 10 November that 17 across the country had stopped", "Lok Sabha reply 168; ANI, 10 November: counts and dates differ"],
               ["State request", "Extend the subsidy from three to five years, with the state bearing 50% for another five years; Star Air says it will fly from Shivamogga if it gets 100% VGF from the state", "ANI and IANS, 18 November; The Hindu, 20 November"]],
              "Show the support schemes and the checks"),
    "The state asks for five years of central support, while the central description of Modified UDAN already gives VGF for up to five years, and the sources do not say whether that scheme covers routes awarded earlier, such as Shivamogga&rsquo;s.",
    "The Civil Aviation Ministry and the state should state in one note which support period applies to routes awarded under the original scheme and which to routes awarded under Modified UDAN.",
    "support")

s4 = insight(
    "Hassan airport cost approved at Rs 542.96 crore, 2.8 times the 2021 sanction",
    bars("Hassan airport: Rs 542.96 crore approved, 2.8 times the Rs 193.65 crore sanctioned in 2021",
         [("Sanctioned in 2021", H_OLD), ("Revised cost approved on 19 November 2026", H_NEW), ("Additional amount cleared", H_ADD)],
         accent="Revised cost approved on 19 November 2026", unit=" crore", fmt=lambda v: f"Rs {v:g} crore", vmax=600,
         sub=f"Rs crore. The additional Rs {H_ADD} crore is Rs {H_LAND:g} crore for more land and Rs {H_WORKS} crore for further works and the facilities needed to operate the airport; it is {100 * H_ADD / H_OLD:.1f}% of the 2021 sanction (computed).",
         source="The Hindu, 20 November 2026 (secondary); PTI and IANS, 19 and 20 November 2026 (secondary).")
    + numbers(["Item", "Value", "Source and status"],
              [["2021 sanction", "Rs 193.65 crore", "The Hindu, 20 November"],
               ["Revised cost", "Rs 542.96 crore (administrative approval)", "IANS; The Hindu"],
               ["Additional amount", "Rs 349.31 crore, of which Rs 122 crore for land and Rs 227.31 crore for works", "The Hindu; PTI says Rs 349 crore"],
               ["Spent so far", "Rs 193 crore on the runway and related works", "Deputy Chief Minister G. Parameshwara, via PTI, 19 November"],
               ["Check", "193.65 + 349.31 = 542.96 and 122 + 227.31 = 349.31", "Computed here; both sums hold"],
               ["Location and history", "About 190 km from Bengaluru; demand dates back more than six decades and land acquisition began in 1966; ground work began in 2021", "The Hindu, 20 November"],
               ["Completion date", "Not found", "Unknown"]],
              "Show the Hassan figures and sources"),
    f"The revised cost is {H_X:.1f} times the 2021 sanction, and the sources give no completion date or the expected flights and passengers.",
    "The Infrastructure Development Department should publish the cost build-up, the completion date and the operating model for Hassan airport, since the new policy is meant to cover state-managed airports.",
    "hassan")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Karnataka Infrastructure Development Department:</b> publish the approved Civil Aviation Policy 2026 with its targets, VGF rates, outlay and the list of airports it covers.</li>
<li><b>Karnataka Civil Aviation Department:</b> publish yearly movements, passengers and subsidy for each state airport on one basis, with sources.</li>
<li><b>Union Ministry of Civil Aviation and the state:</b> state in one note which support period applies to routes awarded under the original UDAN scheme and which under Modified UDAN.</li>
<li><b>Karnataka Infrastructure Development Department:</b> publish the cost build-up, completion date and operating model for Hassan airport.</li>
<li><b>Karnataka Information and Public Relations Department:</b> release cabinet decisions in one dated note, so that a policy approval does not rest on a single wire report.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The approval date comes from a cabinet briefing reported by IANS on 19 November 2026; the Hassan item in the same briefing is also reported by PTI and The Hindu, which do not mention the policy in the excerpts read.</li>
<li>Percentage changes and ratios are computed here from the figures shown. The 33% passenger fall is computed from figures the source gives to one decimal in lakh and is approximate.</li>
<li>News reports were read as search excerpts and are labelled secondary. Parliamentary replies and Government of India releases were read as excerpts; the Modified UDAN components are those in the excerpts.</li>
<li>Statements by ministers and members of Parliament about the Centre, other states or each other are not reported; the piece keeps to dated decisions, figures and the stated scope of the policy.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The policy text, and with it any target, outlay, VGF rate, eligibility rule or list of airports: none was found. Its coverage is known only from the minister&rsquo;s statements of 10 and 18 November.</li>
<li>That the policy was approved as drafted: the report says the cabinet approved the proposal to implement it, one wire service carries this, and a second report was not found. A republished summary calls it &lsquo;formally adopted&rsquo;; that wording is not in the wire text.</li>
<li>Whether the policy replaces or adds to the state industrial and aerospace policies, including the Aerospace Policy 2026-2031 approved on 9 September 2026 that this blog has not reviewed.</li>
<li>The amount the state spent on Kalaburagi airport: the minister said Rs 1,000 crore, the Times of India says over Rs 175 crore, and the central UDAN expenditure shown for Kalaburgi is Rs 28.64 crore. The three may measure different things, and none was reconciled.</li>
<li>Why the Airports Authority&rsquo;s FY2025-26 traffic for Hubballi, Belagavi and Mysuru (7.7 lakh) is more than twice the Times of India figure for four airports in 2024-25 (3.3 lakh): the basis of the Times of India series is not stated.</li>
<li>Whether Modified UDAN&rsquo;s five-year VGF applies to Shivamogga&rsquo;s routes, and why the minister describes the support as three years: the scheme documents read do not say. The count of stopped airports also differs (15 on 20 January, 17 on 10 November).</li>
<li>Four Modified UDAN components sum to Rs 28,440 crore against a total of Rs 28,840 crore; the fifth component was not in the excerpts read.</li>
<li>Whether any flights resumed at Shivamogga after 21 November, and whether the state will fund VGF for Star Air: the airline&rsquo;s condition of 100% VGF was reported on 20 November and no decision was found.</li>
</ul></details>
'''

step(6, "assembling body")
body = STYLE + top + tvo + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://www.socialnews.xyz/2026/11/19/karnataka-cabinet-decides-to-initiate-legal-action-against-author-of-book-allegedly-insulting-basavanna">IANS via SocialNews, 19 November 2026</a> and '
    '<a href="https://www.cityairnews.com/content/karnataka-cabinet-decides-to-initiate-legal-action-against-author-of-book-allegedly-insulting-basavanna">IANS via CityAir News</a> (secondary: cabinet decisions of 19 November, including the policy); '
    '<a href="https://www.thehindu.com/news/national/karnataka/karnataka-cabinet-clears-projects-worth-4000-crore-for-bengaluru-city-approves-10250-crore-for-development-of-nine-state-highways/article71721571.ece">The Hindu, 19 November 2026</a>, '
    '<a href="https://www.deccanchronicle.com/southern-states/karnataka/ktaka-cabinet-approves-waiving-interest-on-loans-to-backward-communities-with-condition-2006140">PTI via Deccan Chronicle, 20 November 2026</a> and '
    '<a href="https://www.thehindu.com/news/national/karnataka/karnataka-govt-to-invest-on-hassan-airport-even-as-operations-face-uncertainty-in-other-district-airports/article71723672.ece">The Hindu, 20 November 2026</a> (secondary: Hassan airport); '
    '<a href="https://www.thehindu.com/news/national/karnataka/policy-to-promote-growth-of-civil-aviation-in-karnataka-to-be-placed-before-next-meeting-of-state-cabinet-for-clearance/article71685980.ece">The Hindu, 10 November 2026</a>, '
    '<a href="https://www.aninews.in/news/national/politics/karnatakas-comprehensive-civil-aviation-policy-to-be-placed-in-next-cabinet-meeting-state-minister-mb-patil16020261110173840">ANI, 10 November 2026</a> and '
    '<a href="https://www.deccanchronicle.com/southern-states/karnataka/karnatakas-comprehensive-aviation-policy-to-be-placed-before-next-cabinet-meeting-mb-patil-2003357">Deccan Chronicle, 11 November 2026</a> (secondary: the minister&rsquo;s statements); '
    '<a href="https://tennews.in/karnataka-to-approve-civil-aviation-policy-at-next-cabinet-meeting-airports-built-by-state-at-huge-cost-should-not-remain-idle-m-b-patil">IANS via tennews, 18 November 2026</a> and '
    '<a href="https://newsable.asianetnews.com/india/karnataka-to-approve-new-civil-aviation-policy-in-upcoming-meeting-articleshow-rtf2ac9">ANI via Asianet Newsable, 18 November 2026</a> (secondary); '
    '<a href="https://timesofindia.indiatimes.com/city/bengaluru/karnatakas-regional-airports-struggle-as-udan-subsidies-end/articleshow/135743465.cms">Times of India, 11 November 2026</a>, '
    '<a href="http://timesofindia.indiatimes.com/city/bengaluru/wheels-down-regional-airports-struggle-as-udan-subsidies-end/articleshow/135757742.cms">Times of India, 12 November 2026</a> and '
    '<a href="http://timesofindia.indiatimes.com/city/mysuru/shivamogga-mp-urges-karnataka-to-extend-funding-for-airport-operations/articleshow/135684323.cms">Times of India, 9 November 2026</a> (secondary: airport traffic); '
    '<a href="https://www.thehindu.com/news/national/karnataka/last-flights-under-udan-takes-off-from-shivamogga/article71723639.ece">The Hindu, 20 November 2026</a>, '
    '<a href="https://www.thehindu.com/news/national/karnataka/ksiidc-chairperson-calls-for-debate-on-necessity-of-airports-in-small-cities-says-shivamogga-airport-has-good-potential/article71693791.ece">The Hindu, 12 November 2026</a> and '
    '<a href="https://www.thehindu.com/news/national/karnataka/flight-operations-at-shivamogga-airport-unlikely-from-november-21-as-starair-halts-bookings/article71674338.ece">The Hindu, 6 November 2026</a> (secondary: Shivamogga); '
    '<a href="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU3101_vLSVfa.pdf?source=lsapps">Lok Sabha reply 3101, 6 August 2026</a>, '
    '<a href="https://sansad.in/getFile/loksabhaquestions/annex/187/AU168_cF3TcA.pdf?source=pqals">Lok Sabha reply 168, 29 January 2026</a>, '
    '<a href="https://sansad.in/getFile/annex/270/AU988_mnKaZH.pdf?source=pqars">Rajya Sabha reply 988, February 2026</a>, '
    '<a href="https://sansad.in/getFile/annex/271/AS7_Jxs5Bk.pdf?source=pqars">Rajya Sabha starred reply 7, 20 July 2026</a> and '
    '<a href="https://sansad.in/getFile/loksabhaquestions/annex/187/AU6324_Bn1DXq.pdf?source=pqals">Lok Sabha reply 6324, 2 April 2026</a> (official, excerpts); '
    '<a href="https://pib.gov.in/PressReleasePage.aspx?PRID=2245096">PIB, 25 March 2026</a> and '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2285671&amp;reg=48&amp;lang=1">PIB backgrounder, 17 July 2026</a> (government releases: Modified UDAN); '
    '<a href="https://www.aai.aero/sites/default/files/List%20of%20AAI%20Non-Major%20apts.pdf">Airports Authority of India, non-major airports list, 22 May 2026</a> (official); '
    '<a href="https://www.aci-asiapac.aero/media-centre/news/blr-airport-records-strong-growth-in-fy-2025-26-driven-by-surge-in-international-traffic-and-cargo-momentum">BLR Airport release, 30 April 2026</a> (operator). '
    'Percentages, ratios and sums computed by this blog. Analysed 21 November 2026.')
RELATED = []

step(7, "writing page")
build("Policy &middot; Karnataka", TITLE,
      "Karnataka&rsquo;s cabinet approved the proposal to implement a State Civil Aviation Policy on 19 November 2026; this piece sets out what is known about it, the regional-airport baseline and the Hassan airport cost.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
step(8, "complete")
