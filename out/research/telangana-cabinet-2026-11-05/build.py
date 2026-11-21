"""Telangana cabinet meeting of 5 November 2026 (38th, chaired by Chief Minister A. Revanth Reddy): Kaleshwaram barrage restoration (Rs 4,193 crore),
Invest Telangana Global Summit 2026 (7-9 December), the Siddipet public meeting of 19 November, and 136 posts for six courts.
Build from the repo root:  python3 out/research/telangana-cabinet-2026-11-05/build.py   (writes out/post-telangana-cabinet-5-november-2026.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 21 November 2026.
The UNI report is paywalled after its first paragraph; the Siasat report was read in full; other outlets were read as search excerpts. The post says so."""
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

OUT = ROOT / "out/post-telangana-cabinet-5-november-2026.html"
STEPS = 8


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. dates (weekdays as the reports state them)
step(1, "dates and weekday checks")
CAB, SIDD, SUMMIT0, SUMMIT1, ASOF = D(2026, 11, 5), D(2026, 11, 19), D(2026, 12, 7), D(2026, 12, 9), D(2026, 11, 21)
assert CAB.strftime("%A") == "Thursday" and SIDD.strftime("%A") == "Thursday"      # Siasat: 'Thursday, November 19'; UNI: cabinet 'on Thursday'
assert D(2026, 10, 24).strftime("%A") == "Saturday"                               # TNIE 25 Oct: minister's press conference 'on Saturday'
assert SUMMIT0.strftime("%A") == "Monday" and SUMMIT1.strftime("%A") == "Wednesday"
assert (SUMMIT0 - CAB).days == 32 and (SUMMIT0 - ASOF).days == 16
assert (SUMMIT1 - SUMMIT0).days + 1 == 3                                          # 'three-day summit'
SLIP = (D(2026, 12, 31) - D(2026, 11, 14)).days       # mid-November start (second week of November, 26 Sep) to the end-December start target
assert SLIP == 47
ENROL_DAYS = (D(2026, 12, 18) - SIDD).days + 1        # 19 Nov to 18 Dec, inclusive
EARLIER_DAYS = (D(2026, 11, 30) - D(2026, 11, 20)).days + 1       # 20 to 30 Nov, inclusive (cabinet-day reports)
assert ENROL_DAYS == 30 and EARLIER_DAYS == 11

# ---- 2. Kaleshwaram: stilling basin lengths (TNIE 25 Oct 2026, broad designs) and the Rs 4,193 crore estimate
step(2, "Kaleshwaram figures")
COST_CR = 4193
BASIN = {"Medigadda": (46.8, 66.0), "Annaram": (45.0, 66.0), "Sundilla": (30.0, 58.0)}
EXT = {k: round(b - a, 1) for k, (a, b) in BASIN.items()}
assert EXT == {"Medigadda": 19.2, "Annaram": 21.0, "Sundilla": 28.0}
PCT = {k: round(100 * (b - a) / a, 1) for k, (a, b) in BASIN.items()}
assert PCT == {"Medigadda": 41.0, "Annaram": 46.7, "Sundilla": 93.3}
assert round(COST_CR / 3) == 1398          # equal split across three barrages is NOT stated by any source; shown only as the arithmetic mean
# ---- 3. Invest Telangana Global Summit 2026
step(3, "summit figures")
RAKSHA_INV, RAKSHA_INT = 575, 49
RAKSHA_PCT = 100 * RAKSHA_INT / RAKSHA_INV
assert f"{RAKSHA_PCT:.1f}" == "8.5"
STARTUPS_PAV, STARTUPS_EXPO, PHARMA_COS, SESSIONS, HALLS_MAIN = 136, 45, 60, 52, 4
assert STARTUPS_PAV + STARTUPS_EXPO == 181
assert SESSIONS / HALLS_MAIN == 13
HALLS_NOW, HALLS_BEFORE, INVESTORS = 6, 1, 3500
# ---- 4. Indiramma family life insurance (launched at Siddipet 19 Nov)
step(4, "insurance figures")
COVER, OLD_LIFE, OLD_ACC, FAMILIES = 5, 2, 10, 1                # Rs lakh; families in crore
assert COVER / OLD_LIFE == 2.5
TOTAL_COVER_CR = COVER * 1e5 * FAMILIES * 1e7 / 1e7             # Rs crore of cover if every one of 1 crore families enrolled: Rs 5 lakh x 1 crore
assert TOTAL_COVER_CR == 500_000                                # Rs 5 lakh crore
# eligible birth dates 19 Nov 1967 to 18 Nov 2008 for ages 18 to 59 on 19 Nov 2026
assert (D(2026, 11, 19).year - D(1967, 11, 19).year) == 59 and (D(2026, 11, 18).year - D(2008, 11, 18).year) == 18
# ---- 5. courts
step(5, "court figures")
POSTS_TOTAL, POSTS_NEW, POSTS_ADD = 136, 56, 80
N_NEW, N_ADD = 2, 4
assert POSTS_NEW + POSTS_ADD == POSTS_TOTAL and N_NEW + N_ADD == 6
PER_NEW, PER_ADD = POSTS_NEW / N_NEW, POSTS_ADD / N_ADD
assert (PER_NEW, PER_ADD) == (28.0, 20.0)
PEND, PEND5, PEND10 = 1_011_003, 178_176, 20_277                # NJDG via Rajya Sabha Q597, 16 Jul 2026, Telangana district and subordinate courts
SANC, WORK, VAC = 619, 474, 145                                 # Nyaya Vikas Portal 2.0, 3 Aug 2026 (Lok Sabha Q3251)
assert WORK + VAC == SANC
HC_SANC, HC_WORK, HC_VAC = 619, 477, 142                        # Telangana High Court report, 31 Mar 2026
assert HC_WORK + HC_VAC == HC_SANC
PER_WORKING, PER_SANCT = PEND / WORK, PEND / SANC
assert f"{PER_WORKING:,.0f}" == "2,133" and f"{PER_SANCT:,.0f}" == "1,633"
assert f"{100 * VAC / SANC:.1f}" == "23.4" and f"{100 * HC_VAC / HC_SANC:.1f}" == "22.9"
assert f"{100 * PEND5 / PEND:.1f}" == "17.6" and f"{100 * PEND10 / PEND:.1f}" == "2.0"

TITLE = "Telangana cabinet, 5 November 2026: Rs 4,193 crore for three Kaleshwaram barrages"
assert 55 <= len(TITLE) <= 90, len(TITLE)
assert not any(w in TITLE.lower().split() for w in ("you", "your", "we", "our"))

step(6, "writing sections")
top = top_line([
    ("Rs 4,193 crore", " is the estimated cost of restoring the Medigadda, Annaram and Sundilla barrages; the Chief Minister set the end of November for final approvals and the end of December to start work, and contractors are to bear repairs of construction defects, in a split no source gives."),
    ("7 to 9 December", f" is the Invest Telangana Global Summit 2026, {(SUMMIT0 - CAB).days} days after the cabinet meeting; the Chief Minister asked for a full plan by 15 November, and reports differ on the investors expected (3,500 or hundreds)."),
    ("136 posts", f" were sanctioned for six courts (56 for two new courts, 80 for four additional ones) while Telangana&rsquo;s subordinate courts held {PEND:,} pending cases on 16 July 2026; no report says how many of the posts are judge posts."),
])

dvo = ('<table class="gb-table"><thead><tr><th>Status on 21 November 2026</th><th>Items</th></tr></thead><tbody>'
       '<tr><td><b>Decided on 5 November</b></td><td>Kaleshwaram restoration plan at Rs 4,193 crore; summit arrangements; the Siddipet meeting; 136 court posts.</td></tr>'
       '<tr><td><b>Done by 21 November</b></td><td>The Siddipet meeting of 19 November was held and the insurance scheme launched there (The Hindu, 19 and 20 November).</td></tr>'
       '<tr><td><b>Still ahead</b></td><td>Final Kaleshwaram approvals by 30 November, works by 31 December, the summit on 7 to 9 December, filling of the court posts.</td></tr>'
       '</tbody></table>\n')

s1 = insight(
    "Kaleshwaram barrages: Rs 4,193 crore estimate, with works due to start by December-end",
    bars("Proposed stilling basins are 19.2, 21 and 28 metres longer at the three barrages",
         [(f"Sundilla: {BASIN['Sundilla'][0]:g} m to {BASIN['Sundilla'][1]:g} m (+{PCT['Sundilla']:g}%)", EXT["Sundilla"]),
          (f"Annaram: {BASIN['Annaram'][0]:g} m to {BASIN['Annaram'][1]:g} m (+{PCT['Annaram']:g}%)", EXT["Annaram"]),
          (f"Medigadda: {BASIN['Medigadda'][0]:g} m to {BASIN['Medigadda'][1]:g} m (+{PCT['Medigadda']:g}%)", EXT["Medigadda"])],
         accent=f"Sundilla: {BASIN['Sundilla'][0]:g} m to {BASIN['Sundilla'][1]:g} m (+{PCT['Sundilla']:g}%)", unit=" m", vmax=30,
         sub="Added length of the stilling basin, metres, from the broad designs the Irrigation Minister described on 24 October 2026; existing and proposed lengths are in the labels, and the extensions and percentages are computed here. Final designs go through technical scrutiny and may differ.",
         source="New Indian Express, 25 October 2026 (secondary, reporting the Irrigation Minister&rsquo;s press conference).")
    + numbers(["Item", "Statement", "Source and status"],
              [["Estimated cost", "Rs 4,193 crore for the three barrages", "UNI and Siasat, 5 November; Telangana Today, New Indian Express (secondary)"],
               ["Cost split", "Contractors bear the cost of repairs of construction defects; the state meets additional works; no amount for either share", "Telangana Today and New Indian Express, 5 and 6 November"],
               ["Phasing", "Two phases: restoring the water-holding capacity, and protective measures; approvals and contracts to run in parallel", "Chief Minister&rsquo;s review, 5 November (as reported)"],
               ["Technical basis", "National Dam Safety Authority guidelines; a Centre-appointed expert committee gave in-principle approval to preliminary plans", "Siasat; Telangana Today"],
               ["Damage", "Piers of the Medigadda barrage sank in October 2023; Annaram and Sundilla developed leakages", "Siasat, 6 November"],
               ["Gates", "The National Dam Safety Authority has advised keeping the Annaram and Sundilla gates open", "Officials, as reported 5 November"],
               ["Mean per barrage", f"Rs {COST_CR / 3:,.0f} crore if split equally; no source gives a per-barrage cost", "Computed arithmetic only"]],
              "Show the Kaleshwaram figures and sources"),
    "The estimate is the first rupee figure for the work, and reports differ on whether the cabinet approved spending of Rs 4,193 crore or the Chief Minister reviewed proposals estimated at that cost.",
    "The Irrigation Department should publish the cost of each barrage, the defect-repair share borne by contractors and the share borne by the state, with the date of each approval.",
    "kaleshwaram")

s1b = ('<section class="xv-sec"><h2 class="gb-h2" id="dates">Dates stated for the Kaleshwaram works, 30 June to 31 December 2026</h2>\n'
       + flow([("October 2023", "Medigadda barrage piers sink; Annaram and Sundilla develop leakages (Siasat)."),
               ("30 Jun 2026", "Union Jal Shakti Ministry constitutes a Technical Oversight Committee; it later met on 31 July and 14 October (Irrigation Minister, as reported)."),
               ("26 Sep 2026", "Irrigation Minister: works to start from the second week of November, with designs vetted by the Central Water Commission&rsquo;s committee on 5 October (The Hindu)."),
               ("24 Oct 2026 (Saturday)", "Minister&rsquo;s roadmap: estimates and approvals by October-end, agencies mobilised by November-end, work on all fronts by December-end, repairs before the 2027 monsoon, subject to technical clearances (New Indian Express)."),
               ("5 Nov 2026", "Chief Minister reviews the plan and the cabinet meets: final approvals by the end of November, work to begin by the end of December; the start has moved by about " + str(SLIP) + " days from mid-November (computed).", True),
               ("30 Nov 2026", "Target for final approvals (not reached on 21 November, as far as reports show)."),
               ("31 Dec 2026", "Target for starting work. No completion date is given beyond the minister&rsquo;s aim of the 2027 monsoon.")])
       + '</section>\n')

s2 = insight(
    "Global Summit on 7 to 9 December: 3,500 investors expected in one report",
    bars("Raksha Expo: 49 of 575 invited organisations had expressed interest by 5 November",
         [("Organisations invited to the Raksha Expo", RAKSHA_INV), ("Organisations that had expressed interest", RAKSHA_INT)],
         accent="Organisations that had expressed interest", vmax=600,
         sub=f"Count of organisations, as officials reported on 5 November; the share is {RAKSHA_PCT:.1f}% (computed). The same briefing gave {STARTUPS_PAV} startups in the Startup Pavilion and {PHARMA_COS} companies in the pharma and life sciences expo.",
         source="New Indian Express, 6 November 2026 (secondary); Telangana state press release, 5 November 2026 (official).")
    + numbers(["Item", "Statement", "Source and status"],
              [["Dates and venue", "7 to 9 December 2026 at the Young India Skills University campus, Bharat Future City (UNI calls it the Fourth City)", "State press release, 5 November; UNI"],
               ["Scale against 2025", f"{HALLS_NOW} exhibition halls against {HALLS_BEFORE} at the Telangana Rising summit of December 2025", "State press release; officials"],
               ["Sessions", f"{SESSIONS} sector sessions across {HALLS_MAIN} main halls ({SESSIONS // HALLS_MAIN} a hall on average, computed)", "New Indian Express"],
               ["Climate conclave", "8 December; about 200 scientists, farmers and experts", "State press release"],
               ["Startups", f"{STARTUPS_PAV} in the pavilion and {STARTUPS_EXPO} more in sector expos, {STARTUPS_PAV + STARTUPS_EXPO} in all (computed); challenge applications closed 20 November", "Invest Telangana startup page"],
               ["Investors expected", "3,500 investors and industrialists (Siasat); &lsquo;hundreds&rsquo; (UNI)", "Reports conflict"],
               ["Planning deadline", "Comprehensive plan by 15 November; whether it was completed is not reported", "State press release"],
               ["Edition", "Siasat calls it the second edition; the state release compares it with the Telangana Rising summit of 2025", "Naming differs"]],
              "Show the summit figures and sources"),
    f"The cabinet discussed arrangements and assigned ministers responsibilities, and the date is {(SUMMIT0 - ASOF).days} days from 21 November, so what is measurable now is preparation, not investment.",
    "The Industries and Commerce Department should publish after the summit the number of investors who attended and the value, sector and timeline of each agreement signed, separate from expressions of interest.",
    "summit")

s3 = insight(
    "Siddipet meeting launched Rs 5 lakh family life cover, with enrolment to 18 December",
    bars("Rs 5 lakh life cover is 2.5 times the Rs 2 lakh under some existing departmental schemes",
         [("Existing life cover in some departmental schemes", OLD_LIFE), ("Indiramma family life cover per family", COVER)],
         accent="Indiramma family life cover per family", unit=" lakh", fmt=lambda v: f"Rs {v:g} lakh", vmax=6,
         sub="Cover per family, Rs lakh. Officials said existing accident cover of up to Rs 10 lakh is to stay as it is. The ratio is computed here.",
         source="Deccan Chronicle, 17 November 2026; The Hindu BusinessLine, 18 November 2026 (secondary, citing a state release).")
    + numbers(["Item", "Statement", "Source and status"],
              [["Launch", "19 November 2026, Siddipet, Indira Gandhi&rsquo;s birth anniversary; cabinet had decided it on 5 November", "The Hindu, 19 and 20 November; Siasat"],
               ["Cover", "Rs 5 lakh life cover for one earning member aged 18 to 59 in each family, born from 19 November 1967 to 18 November 2008", "Samayam Telugu, 18 November, citing state guidelines"],
               ["Families", "One crore families targeted; the cover would total Rs 5 lakh crore if all enrolled, which is a sum insured and not a budget figure (computed)", "Deccan Chronicle; BusinessLine"],
               ["Enrolment window", f"19 November to 18 December ({ENROL_DAYS} days) in guidelines of 18 November; the cabinet-day reports said 20 to 30 November ({EARLIER_DAYS} days)", "Samayam Telugu; Siasat; New Indian Express (conflict)"],
               ["Indiramma sarees", "Distribution to start on 19 November (Hindu, Metro India); one aggregator summary says 26 November", "Conflict, not resolved"],
               ["Premium and insurer", "Not found in any report read", "Unknown"],
               ["Enrolments so far", "Not found", "Unknown"]],
              "Show the scheme details and the conflicts"),
    "The cover is a sum insured per family, so the state&rsquo;s annual cost depends on the premium, which no report gives, and the enrolment window is reported as 30 days in later guidelines against 11 days in the cabinet-day reports.",
    "The Finance Department should publish the premium, the insurer, the annual budget provision and the enrolment count, with one dated enrolment window.",
    "insurance")

s4 = insight(
    f"Courts: 136 posts for six courts, while subordinate courts held {PEND / 1e5:.2f} lakh pending cases",
    bars("The 136 posts average 28 for each of two new courts, 20 for each of four others",
         [("Two newly established courts (Kataram, Elkathurthy): 56 posts", PER_NEW),
          ("Four additional courts (Siddipet, Choutuppal, Mahabubabad, Vemulawada): 80 posts", PER_ADD)],
         accent="Two newly established courts (Kataram, Elkathurthy): 56 posts", vmax=32, fmt=lambda v: f"{v:g} a court",
         sub="Average posts for each court, computed here from the group totals of 56 and 80; the sources give totals for each group, not for each court. The sources do not say how many of the 136 posts are judge posts.",
         source="The Hindu, 5 November 2026 (56 posts for the two new courts); TV9 Telugu, 5 November (80 posts for four additional courts); Siasat; New Indian Express (secondary).")
    + numbers(["Item", "Value", "Source and status"],
              [["Posts sanctioned", f"{POSTS_TOTAL}: {POSTS_NEW} for two newly established Junior Civil Judge-cum-Additional Judicial First Class Magistrate courts and {POSTS_ADD} for four additional courts", "The Hindu; TV9 Telugu (the 80 comes from the Telugu report only)"],
               ["Pending cases, district and subordinate courts", f"{PEND:,} on 16 July 2026; {PEND5:,} older than 5 years ({100 * PEND5 / PEND:.1f}%); {PEND10:,} older than 10 years ({100 * PEND10 / PEND:.1f}%)", "National Judicial Data Grid, Rajya Sabha reply of 23 July 2026 (official)"],
               ["Judges, subordinate courts", f"Sanctioned {SANC}, working {WORK}, vacant {VAC} ({100 * VAC / SANC:.1f}%) on 3 August 2026", "Nyaya Vikas Portal 2.0, Lok Sabha reply of 7 August 2026 (official)"],
               ["Judicial officers, High Court report", f"Sanctioned {HC_SANC}, working {HC_WORK}, vacant {HC_VAC} ({100 * HC_VAC / HC_SANC:.1f}%) on 31 March 2026", "Telangana High Court report (official); differs from the August count by 3 working judges"],
               ["Pending per working judge", f"{PER_WORKING:,.0f} ({PER_SANCT:,.0f} per sanctioned post)", "Computed; pendency date (16 July) and judge date (3 August) differ"],
               ["Stated purpose", "Minister: the move is expected to speed up disposal of cases in subordinate courts", "Siasat; this is an expectation, not a measured result"]],
              "Show the court figures and sources"),
    f"With {PER_WORKING:,.0f} pending cases for every working judge and {VAC} vacant judge posts, six more courts add capacity only when the posts are filled and the courts begin sitting, and no source gives either date.",
    "The Law Department should publish the number of judge posts among the 136, the recruitment schedule and the date each of the six courts is to start sitting.",
    "courts")

other = ('<section class="xv-sec"><h2 class="gb-h2" id="other">Other decisions reported for 5 November</h2>\n'
         + numbers(["Decision", "Detail as reported", "Source"],
                   [["Separate commissions for Scheduled Castes and Scheduled Tribes", "Joint commission abolished and the 2003 Act repealed; each new commission has a chairperson and five members", "Siasat; New Indian Express"],
                    ["Telangana Fire Service Act, 1999", "Amendment on fire prevention, causes of accidents, response and owners&rsquo; duties; an ordinance to follow", "Siasat; New Indian Express"],
                    ["Telangana Survey and Boundaries Act, 1923, section 12(A)", "Appeal period against notices cut from 60 days to 30 days", "Siasat; New Indian Express"],
                    ["Maa Indiramma Intlo Deepavali", "Programme on Diwali across the state; 2.25 lakh Indiramma houses completed so far, said the minister", "Siasat; New Indian Express"]],
                   "Show the other decisions")
         + '</section>\n')

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Telangana Irrigation Department:</b> publish the cost of each barrage, the contractors&rsquo; share and the state&rsquo;s share of the Rs 4,193 crore, and the date of each final approval.</li>
<li><b>Telangana Industries and Commerce Department:</b> report, after the summit, investors attending and each agreement&rsquo;s value, sector and timeline, apart from expressions of interest.</li>
<li><b>Telangana Finance Department:</b> publish the premium, insurer, budget provision and enrolment count for the Indiramma family life insurance, with one enrolment window.</li>
<li><b>Telangana Law Department:</b> publish how many of the 136 posts are judge posts and when each court is to start sitting.</li>
<li><b>Telangana Information and Public Relations Department:</b> release the cabinet decisions in one dated note, so that reports no longer differ on whether the cabinet approved or reviewed an item.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The cabinet meeting is dated 5 November 2026 (a Thursday) and called the 38th by UNI. Items the reports attribute to the Chief Minister&rsquo;s review meeting of the same day are labelled as such.</li>
<li>The UNI report was read only as far as its first paragraph, as the rest is for subscribers. The Siasat report was read in full. Other outlets were read as search excerpts and are labelled secondary.</li>
<li>Extensions, shares, per-court averages and per-judge counts are computed here from the figures shown; none is a published figure. Per-court post counts are averages of group totals.</li>
<li>Pending cases and judge counts come from parliamentary replies and a High Court report, which carry different dates; the per-judge figure joins two dates and is indicative.</li>
<li>Political statements made at the Siddipet meeting and in the debate around Kaleshwaram are left out; the post keeps to dated decisions, figures and deadlines.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>Whether the cabinet approved spending of Rs 4,193 crore or reviewed proposals estimated at that cost: Siasat says the cabinet cleared the works, while Telangana Today and The Hindu describe proposals at that estimate after the Chief Minister&rsquo;s review. The New Indian Express headline says the cabinet cleared restoration, and its first paragraph says restoration &lsquo;by the end of December&rsquo;, while its body says work is to begin by then; the start reading is used.</li>
<li>The split of Rs 4,193 crore between contractors and the state, the cost of each barrage, which contractors are involved, and whether they accept the liability: none is stated.</li>
<li>Whether final approvals were obtained by 30 November, the date work will start beyond the end-December target, and any completion date; the minister&rsquo;s 24 October aim of finishing before the 2027 monsoon is subject to technical clearances.</li>
<li>The text of the cabinet decisions: no cabinet note was read; the UNI report is paywalled after its first paragraph.</li>
<li>The investors expected at the summit: Siasat says 3,500, UNI says &lsquo;hundreds&rsquo;, and no investment-value target was found. Whether the 15 November summit plan was completed.</li>
<li>That UNI&rsquo;s &lsquo;Fourth City&rsquo; and the state&rsquo;s &lsquo;Bharat Future City&rsquo; are the same site: the dates and the cabinet discussion match, but no source says so.</li>
<li>Premium, insurer, budget and enrolment of the insurance scheme; the saree distribution start date (19 or 26 November); and the enrolment window (20 to 30 November in cabinet-day reports, 19 November to 18 December in guidelines).</li>
<li>How many of the 136 court posts are judge posts, their cost, and the dates the courts start sitting. The 80 posts for four additional courts come from a Telugu report; the English reports read give the 136 total and the 56. The Siasat list of six places and the New Indian Express list of districts differ in naming (Siddipet is absent from the latter).</li>
<li>Andhra Jyothy, a Telugu daily, lists further items (886 municipal posts, a Rs 3,000 crore HUDCO loan for roads, a Telangana Road Development Corporation borrowing limit raised from Rs 5,000 crore to Rs 10,000 crore, an amendment to the Bhu Bharati law); no English report read confirms them, so they are not included.</li>
<li>Whether disposal of cases will in fact speed up: the minister&rsquo;s statement is an expectation, and no target or measure was found.</li>
</ul></details>
'''

step(7, "assembling body")
body = STYLE + top + dvo + s1 + s1b + s2 + s3 + s4 + other + fixes + method + gaps

SOURCES = (
    '<a href="https://www.uniindia.com/south-india/cabinet-telangana-decisions-05ms43/237201">UNI, 5 November 2026</a> (secondary; first paragraph only, rest behind a subscription); '
    '<a href="https://www.siasat.com/telangana-okays-rs-4193-crore-kaleshwaram-barrage-repairs-3570572/amp/">Siasat, 5 and 6 November 2026</a> (secondary; read in full); '
    '<a href="https://www.newindianexpress.com/states/telangana/2026/Nov/06/telangana-cabinet-clears-restoration-of-three-klis-barrages">New Indian Express, 6 November 2026</a> and '
    '<a href="https://www.newindianexpress.com/states/telangana/2026/Oct/25/telangana-govt-targets-kaleshwaram-repairs-before-2027-monsoon">25 October 2026</a> (secondary); '
    '<a href="https://telanganatoday.com/revanth-reddy-sets-december-target-for-restoration-of-medigadda-annaram-and-sundilla-barrages">Telangana Today, 5 November 2026</a> and '
    '<a href="https://www.thehindu.com/news/national/telangana/cm-directs-officials-to-begin-kaleshwaram-barrage-restoration-works-in-december/article71670959.ece">The Hindu, 5 November 2026</a> (secondary: Kaleshwaram review); '
    '<a href="https://www.thehindu.com/news/national/telangana/kaleshwaram-barrages-rehab-works-will-begin-in-mid-nov-uttam/article71512647.ece">The Hindu, 26 September 2026</a> (secondary: earlier start date); '
    '<a href="https://www.telangana.gov.in/news/press-releases/2026/11/honble-cm-sri-a-revanth-reddy-reviewed-the-arrangements-for-invest-telangana-global-summit-2026-with-ministers-and-senior-officials">Telangana state press release, 5 November 2026</a> (official: summit); '
    '<a href="https://www.newindianexpress.com/states/telangana/2026/Nov/06/global-summit-to-focus-on-tech-climate-and-defence-in-hyderabad">New Indian Express, 6 November 2026</a> and '
    '<a href="https://invest.telangana.gov.in/global-summit-2026/startup-arena/">Invest Telangana startup page</a> (summit counts); '
    '<a href="https://www.thehindu.com/news/national/telangana/cm-launches-indiramma-family-life-insurance-scheme/article71721517.ece">The Hindu, 19 November 2026</a> (secondary: launch); '
    '<a href="https://www.thehindu.com/news/national/telangana/telangana-government-to-launch-family-insurance-scheme-on-november-19/article71671295.ece">The Hindu, 5 November 2026</a> (secondary: 136 posts, 56 for two courts); '
    '<a href="https://tv9telugu.com/telangana/telangana-cabinet-decisions-separate-sc-st-commissions-indiramma-insurance-scheme-and-saree-distribution-approved-1951652.html">TV9 Telugu, 5 November 2026</a> (secondary, Telugu: 80 posts for four courts); '
    '<a href="https://www.deccanchronicle.com/southern-states/telangana/revanth-orders-indiramma-life-insurance-cover-for-1-crore-families-2005310">Deccan Chronicle, 17 November 2026</a>, '
    '<a href="https://www.thehindubusinessline.com/news/national/telangana-cm-revanth-reddy-to-launch-indiramma-insurance-scheme-on-nov-19/article71714408.ece">BusinessLine, 18 November 2026</a> and '
    '<a href="https://telugu.samayam.com/telangana/news/telangana-govt-to-launch-rs-5-lakh-family-life-insurance-indiramma-jeevitha-bheema-scheme-on-november-19-eligibility-documents-and-application-process/articleshow/135944928.cms">Samayam Telugu, 18 November 2026</a> (secondary: insurance scheme); '
    '<a href="https://particle.news/story/revanth-launches-5-lakh-indiramma-insurance-brs-accuses-congress-of-graft">Particle news summary, 19 November 2026</a> (aggregator, weak: saree date only); '
    '<a href="https://sansad.in/getFile/annex/271/AU597_ZRzDHo.pdf?source=pqars">Rajya Sabha reply 597, 23 July 2026</a> (official: pending cases from the National Judicial Data Grid); '
    '<a href="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU3251_2NVPwp.pdf">Lok Sabha reply 3251, 7 August 2026</a> (official: judge strength); '
    '<a href="https://tg.tshc.gov.in/documents/2026_09_16T17_35_38VOLUME_8.pdf">Telangana High Court report, volume VIII</a> (official: officers at 31 March 2026). '
    'Extensions, shares, averages and ratios computed by this blog. Analysed 21 November 2026.')
RELATED = []

step(8, "writing page")
build("Governance &middot; Telangana", TITLE,
      "Telangana&rsquo;s cabinet met on 5 November 2026; this piece sets out four of its decisions with their figures, costs, deadlines and what the reports leave unstated.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
