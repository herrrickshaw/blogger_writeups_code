"""DILRMP: Forty-first Report of the Standing Committee on Rural Development and Panchayati Raj (18th Lok Sabha), presented to Lok Sabha and laid in Rajya Sabha on 11 Aug 2026.
Source read in full: sansad.in 18_Rural_Development_and_Panchayati_Raj_41.pdf (53 pages, text extracted). Paragraph numbers cited below are the report's own.
Build from the repo root:  python3 out/research/dilrmp-standing-committee-41/build.py            (writes out/post-dilrmp-standing-committee-41.html)
                           python3 out/research/dilrmp-standing-committee-41/build.py --check    (arithmetic and asserts only)
Analysed 25 November 2026."""
import html as _h
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
OUT = ROOT / "out/post-dilrmp-standing-committee-41.html"
STEPS = 7


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


# ---- 1. coverage as on 31 January 2026 (paras 3.5, 3.9, 3.12, 3.16, 3.17, 3.19; recommendation 1)
step(1, "coverage figures and gaps")
COV = [("Records of Rights computerised", 99.81), ("Cadastral maps digitised", 97.42), ("Sub-Registrar Offices computerised", 95.73),
       ("Registration Offices integrated with Revenue Offices", 88.56), ("Villages with textual and spatial records integrated", 84.32),
       ("Modern Record Rooms in sanctioned tehsils", 72.50)]
GAP = {k: round(100 - v, 2) for k, v in COV}
assert GAP["Records of Rights computerised"] == 0.19 and GAP["Cadastral maps digitised"] == 2.58 and GAP["Sub-Registrar Offices computerised"] == 4.27
assert GAP["Registration Offices integrated with Revenue Offices"] == 11.44 and GAP["Villages with textual and spatial records integrated"] == 15.68
assert GAP["Modern Record Rooms in sanctioned tehsils"] == 27.5
assert [v for _, v in COV] == sorted((v for _, v in COV), reverse=True)                   # ordered from most to least complete
assert f"{99.81 - 72.50:.2f}" == "27.31"
assert f"{97.42 - 84.32:.2f}" == "13.10"                                                  # maps digitised but not yet integrated with records, in percentage points (different denominators: maps vs villages)

# ---- 2. outlay (paras 2.7 to 2.12) in Rs crore
step(2, "outlay table and sums")
EXIST = {"Modern record room (tehsil)": 130, "Survey and re-survey, innovative initiatives": 300, "Data entry and re-entry": 15,
         "Digitisation of cadastral maps, FMBs, tippans": 52, "State level data centre": 32, "Computerisation of registration": 50,
         "DILRMP Cell": 12, "Programme management unit": 47, "Evaluation studies, IEC and training": 40, "Core GIS and software applications": 20}
NEW = {"Consent-based Aadhaar integration with land records": 62, "Computerisation of Revenue Courts and integration": 115}
assert sum(EXIST.values()) == 698 and sum(NEW.values()) == 177 and 698 + 177 == 875      # printed sub-totals and grand total
assert len(EXIST) == 10 and len(NEW) == 2
OUTLAY, REVISED, EXTRA = 875, 984.61, 109.61
assert round(OUTLAY + EXTRA, 2) == REVISED and f"{100 * EXTRA / OUTLAY:.1f}" == "12.5"
assert f"{100 * 300 / OUTLAY:.1f}" == "34.3"                                              # survey: 'nearly one-third' (para 2.11)
assert f"{100 * 177 / OUTLAY:.1f}" == "20.2" and f"{100 * 698 / OUTLAY:.1f}" == "79.8"
assert f"{100 * 115 / OUTLAY:.1f}" == "13.1" and f"{100 * 130 / OUTLAY:.1f}" == "14.9" and f"{100 * 62 / OUTLAY:.1f}" == "7.1"
assert max(EXIST, key=EXIST.get) == "Survey and re-survey, innovative initiatives"
assert 300 > 130 > 115 > 62                                                               # ranking used in the chart
RELEASED = 2664.33                                                                        # cumulative releases to States and UTs since 2008-09 to 31 Jan 2026 (para 2.12), all phases
assert RELEASED > REVISED                                                                 # so the cumulative figure cannot be set against this phase's outlay
SPENT_PCT = 71                                                                            # 2025-26 expenditure 'approximately 71 per cent of the revised financial allocation' to 31 Jan 2026 (para 2.15)

# ---- 3. urban pilot and ULPIN (paras 5.5, 5.22, 5.23; recommendation 9)
step(3, "NAKSHA, ULPIN, registration systems")
ULB_ALL, ULB_PILOT, ULB_AERIAL, ULB_ORTHO, ULB_NEXT, NAKSHA_CR = 4912, 157, 119, 113, 1000, 194
assert f"{100 * ULB_PILOT / ULB_ALL:.1f}" == "3.2" and f"{100 * ULB_AERIAL / ULB_PILOT:.1f}" == "75.8" and f"{100 * ULB_ORTHO / ULB_PILOT:.1f}" == "72.0"
assert ULB_PILOT - ULB_AERIAL == 38 and ULB_PILOT - ULB_ORTHO == 44
assert f"{NAKSHA_CR * 100 / ULB_PILOT:.1f}" == "123.6"                                    # Rs lakh per pilot urban local body, computed
assert ULB_NEXT / ULB_PILOT > 6 and f"{ULB_NEXT / ULB_PILOT:.1f}" == "6.4" and f"{100 * ULB_NEXT / ULB_ALL:.1f}" == "20.4"
REC_ULB = 150                                                                             # recommendation 9 says 'pilot project in 150 Urban Local Bodies'; para 5.22 says 157
assert REC_ULB != ULB_PILOT                                                               # source conflict inside the report, flagged in the text
ULPIN_PARCELS_CR, ULPIN_STATES = 37, 29                                                   # 'more than 37 crore' parcels, rolled out in 29 States and UTs; pilots in four
AUTO_MUT, NGDRS, NGDRS_PAPERLESS = 17, 17, 5

TITLE = "DILRMP land records: 99.81% of records computerised, 84.32% of villages linked to maps"
plain = _h.unescape(TITLE)
assert 55 <= len(plain) <= 90, len(plain)
assert not any(w in plain.lower().split() for w in ("you", "your", "we", "our"))
print(f"consistency checks passed (coverage gaps, outlay sums, urban pilot, title {len(plain)} characters)", flush=True)
if "--check" in sys.argv:
    sys.exit(0)

from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

step(4, "writing sections")
top = top_line([
    ("99.81%", " of Records of Rights were computerised and 97.42% of cadastral maps digitised on 31 January 2026, but textual and spatial records were integrated in 84.32% of villages and Modern Record Rooms built in 72.50% of sanctioned tehsils (Standing Committee, 11 August 2026)."),
    ("Rs 300 crore", f" of the Rs 875 crore approved for 2021&ndash;22 to 2025&ndash;26 went to survey and re-survey, {100 * 300 / OUTLAY:.1f}% of the outlay; the Finance Ministry added Rs 109.61 crore in 2025&ndash;26, raising it to Rs 984.61 crore."),
    ("157", f" urban local bodies are in the NAKSHA pilot against 4,912 across the country ({100 * ULB_PILOT / ULB_ALL:.1f}%); the report publishes no state-wise table of progress."),
])

tvo = ('<table class="gb-table"><thead><tr><th>Kind</th><th>What this piece includes</th></tr></thead><tbody>'
       '<tr><td><b>Reported by the Department</b></td><td>Coverage percentages as on 31 January 2026, the approved outlay and component table, ULPIN and NAKSHA counts, as the Department of Land Resources told the Committee.</td></tr>'
       '<tr><td><b>Committee&rsquo;s own view</b></td><td>Observations and ten recommendations, such as completing survey and re-survey on a time-bound roadmap and approving DILRMP 3.0 with milestones.</td></tr>'
       '<tr><td><b>Computed here</b></td><td>Shares of the outlay, gaps to 100% and urban-pilot ratios, each checked in the build script.</td></tr>'
       '<tr><td><b>Not found</b></td><td>A state-wise table, year-wise spend in rupees, and the text of the proposed DILRMP 3.0.</td></tr>'
       '</tbody></table>\n')

s1 = insight(
    "Coverage on 31 January 2026: 99.81% of records computerised, 72.50% of record rooms built",
    bars("Completion falls from 99.81% for records of rights to 72.50% for modern record rooms",
         COV, accent="Villages with textual and spatial records integrated", unit="%", vmax=100,
         sub=("Per cent complete as on 31 January 2026, as reported by the Department of Land Resources. Denominators differ: Records of Rights and cadastral maps are shares of those &lsquo;available&rsquo;, offices are shares of offices, integration is a share of villages, record rooms are a share of sanctioned tehsils. The gaps to 100% are 0.19, 2.58, 4.27, 11.44, 15.68 and 27.50 points (computed)."),
         source="Standing Committee on Rural Development and Panchayati Raj, Forty-first Report, 11 August 2026, paragraphs 3.5, 3.9, 3.12, 3.16, 3.17 and 3.19 (official; read in full).")
    + numbers(["Component", "Complete", "Gap to 100%", "Paragraph"],
              [[k, f"{v:.2f}%", f"{GAP[k]:.2f} points", p] for (k, v), p in zip(COV, ["3.5", "3.9", "3.16", "3.17", "3.12", "3.19"])],
              "Show the coverage figures and gaps"),
    "Digitising records is nearly finished, and the unfinished work is the linking of records to maps and registration, where the Department itself says the quality, currency and legal validity of records are the remaining issues.",
    "The Department of Land Resources should report integration and record-room completion state by state each quarter, against dates set in DILRMP 3.0.",
    "coverage")

rows2 = sorted([(k, float(v)) for k, v in list(EXIST.items()) + list(NEW.items())], key=lambda r: -r[1])[:6]
s2 = insight(
    "Survey and re-survey take Rs 300 crore of the Rs 875 crore outlay, 34.3%",
    bars("Survey and re-survey is the largest of 12 components at Rs 300 crore of Rs 875 crore",
         rows2, accent="Survey and re-survey, innovative initiatives", unit=" crore", fmt=lambda v: f"Rs {v:,.0f} crore", vmax=320,
         sub=(f"Approved outlay by component for 2021&ndash;22 to 2025&ndash;26, Rs crore; the six largest of 12 are shown. Existing components total Rs 698 crore and the two new components Rs 177 crore, {100 * 177 / OUTLAY:.1f}% of the outlay. In 2025&ndash;26 the Finance Ministry approved Rs 109.61 crore more, a rise of {100 * EXTRA / OUTLAY:.1f}%, to Rs 984.61 crore; the report does not allocate the addition by component."),
         source="Standing Committee on Rural Development and Panchayati Raj, Forty-first Report, 11 August 2026, paragraphs 2.7 to 2.11 (official; read in full).")
    + numbers(["Component", "Rs crore", "Share of Rs 875 crore"],
              [[k, f"{v}", f"{100 * v / OUTLAY:.1f}%"] for k, v in list(EXIST.items()) + list(NEW.items())],
              "Show all 12 components"),
    "Nearly a third of the outlay funds fresh survey work, and the report finds survey is what makes digital records match the ground.",
    "The Department of Land Resources should publish survey and re-survey area completed against area pending, by state, so that spending can be read against output.",
    "outlay")

s3 = insight(
    "NAKSHA covers 157 of 4,912 urban local bodies; aerial surveys are complete in 119",
    bars("The urban pilot covers 3.2% of urban local bodies; the next phase proposes 1,000 cities",
         [("Urban local bodies in the country", ULB_ALL), ("Proposed next phase: about 1,000 cities", ULB_NEXT), ("Pilot urban local bodies", ULB_PILOT),
          ("Aerial survey completed (2 Feb 2026)", ULB_AERIAL), ("Ortho-rectified imagery generated", ULB_ORTHO)],
         accent="Pilot urban local bodies", unit="", vmax=5000,
         sub=(f"Urban local bodies. The pilot project costs an estimated Rs {NAKSHA_CR} crore, about Rs {NAKSHA_CR * 100 / ULB_PILOT:.0f} lakh a pilot body (computed). Aerial survey is complete in {100 * ULB_AERIAL / ULB_PILOT:.1f}% and ortho-rectified imagery generated for {100 * ULB_ORTHO / ULB_PILOT:.1f}% of the 157. Recommendation 9 of the same report refers to 150 bodies, which is not reconciled with 157."),
         source="Standing Committee on Rural Development and Panchayati Raj, Forty-first Report, 11 August 2026, paragraphs 5.22 and 5.23 and recommendation 9 (official; read in full).")
    + numbers(["Item", "Value", "Source and status"],
              [["ULPIN", "More than 37 crore parcels assigned a 14-digit ULPIN; rolled out in 29 states and union territories; pilots in Puducherry, Telangana, Manipur and Andaman and Nicobar Islands (31 January 2026)", "Report, paragraph 5.5"],
               ["Auto-triggered mutation", "Implemented in 17 states; it starts the mutation request after registration and does not remove notice, objection or hearing steps", "Report, paragraphs 4.17 and 4.18"],
               ["NGDRS", "Adopted by 17 states and union territories; Assam, Chhattisgarh, Himachal Pradesh, Punjab and Madhya Pradesh run fully paperless registration on it", "Report, paragraphs 4.12 and 4.13"],
               ["Telangana", "Named by the Committee as a ULPIN pilot state and as one of ten states with notified Fifth Schedule areas; the Committee gives no Telangana-specific progress figure. Telangana&rsquo;s own Bhu Bharati portal figures are in the Telangana service delivery post on this blog and are not comparable with the Committee&rsquo;s national percentages", "Report, paragraphs 5.5 and 5.24; the Bhu Bharati figures come from that post&rsquo;s sources"],
               ["Recommendation 9", "Evaluate the NAKSHA pilot comprehensively before scaling, then adopt a phased strategy and give states technical and financial support", "Report, recommendation 9"]],
              "Show the ULPIN, mutation and registration figures"),
    "The urban programme is a pilot in 3.2% of urban local bodies, and the Committee asks for an evaluation of it before any extension.",
    "The Department of Land Resources should publish the NAKSHA pilot evaluation with cost per urban local body and the survey completion dates before the 1,000-city phase is approved.",
    "naksha")

s4 = insight(
    "The scheme period ended on 31 March 2026 and DILRMP 3.0 for 2026-31 is only proposed",
    flow([("2 Dec 2025", "Fourth sitting of the Committee takes evidence from the Department of Land Resources (minutes, Annexure I)."),
          ("31 Jan 2026", "Cut-off date for coverage percentages and for the Rs 2,664.33 crore released to states and union territories since 2008&ndash;09."),
          ("31 Mar 2026", "End of the approved five-year scheme period of Rs 875 crore."),
          ("10 Aug 2026", "Report signed by the Chairperson, Saptagiri Sankar Ulaka."),
          ("11 Aug 2026", "Report presented to Lok Sabha and laid in Rajya Sabha; DILRMP 3.0 for 2026&ndash;2031 is a proposal, and the Committee asks that its approval be expedited with milestones and measurable outcomes.", True)])
    + numbers(["Recommendation (number)", "What the Committee asks"],
              [["1", "Complete pending activities within a defined timeline; expedite approval of DILRMP 3.0 with milestones, outcomes and monitoring"],
               ["2", "All states and union territories to integrate Registration and Revenue Offices and adopt auto-triggered mutation"],
               ["3", "A dedicated strategy for Sixth Schedule areas after the TISS roadmap; progress in Meghalaya is described as negligible"],
               ["4", "Legal recognition of digitally signed Records of Rights in all states"],
               ["5", "A time-bound roadmap for pending survey and re-survey using modern technology"],
               ["6", "Computerise Revenue Courts and set time limits for mutation and correction cases"],
               ["7", "Complete consent-based Aadhaar and mobile seeding with automatic alerts to landowners"],
               ["8", "Strengthen training of revenue, registration and survey officials and the DILRMP Cells"],
               ["9", "Evaluate the NAKSHA pilot, then extend it in phases with technical and financial support"],
               ["10", "Complete Modern Record Rooms and preserve legacy records, with standards for physical and digital preservation"]],
              "Show the ten recommendations"),
    "The report asks for DILRMP 3.0 to be approved quickly with milestones, because the approved period of the current scheme ended before the report was presented.",
    "The Department of Land Resources should state the approval date of DILRMP 3.0 and the funding that applies between 1 April 2026 and approval.",
    "next")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Department of Land Resources:</b> publish a state-wise table of each coverage percentage, as on a stated date, with the denominator used.</li>
<li><b>Department of Land Resources:</b> publish expenditure in rupees by year and component against the Rs 984.61 crore revised outlay, instead of a share of an unstated allocation.</li>
<li><b>Department of Land Resources:</b> publish area surveyed or re-surveyed against area pending by state, with the time-bound roadmap the Committee asks for.</li>
<li><b>State revenue departments:</b> report the volume of errors found in computerised Records of Rights and the share corrected, which the Department undertook to supply in evidence.</li>
<li><b>Department of Land Resources:</b> publish the NAKSHA pilot evaluation and reconcile the pilot size of 157 with the 150 in the recommendation.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Every figure is from the text of the Forty-first Report, extracted from the PDF on sansad.in; paragraph numbers are the report&rsquo;s. Percentages are the Department&rsquo;s own, as told to the Committee, and are not audited here.</li>
<li>The component table sums were checked: the existing components total Rs 698 crore, the new components Rs 177 crore, and the grand total Rs 875 crore.</li>
<li>Gaps to 100% subtract a percentage from 100 and are not comparable across rows, because each row has its own denominator.</li>
<li>The revised outlay is Rs 875 crore plus Rs 109.61 crore, Rs 984.61 crore, as the report states. The cumulative release of Rs 2,664.33 crore since 2008&ndash;09 covers earlier phases, so it is not set against this phase&rsquo;s outlay.</li>
<li>Shares and ratios are computed here and checked by assertions in the builder.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>State-wise coverage. The report gives national percentages and names only a few regions (Meghalaya progress described as negligible, early stage in Ladakh, slower progress in several north-eastern states), and no table by state.</li>
<li>Year-wise expenditure in rupees. The report says expenditure was broadly consistent with allocations and that 2025&ndash;26 spend was approximately 71% of the revised allocation to 31 January 2026, but does not say whether the base is the year&rsquo;s allocation or the Rs 984.61 crore, and gives no rupee figure.</li>
<li>How the added Rs 109.61 crore is split by component.</li>
<li>What &lsquo;available&rsquo; means for Records of Rights and cadastral maps, which sets the denominator for 99.81% and 97.42%.</li>
<li>Error rates in computerised records: the Department was asked to supply state-wise information on errors reported after computerisation, and the Committee&rsquo;s own note records it as outstanding.</li>
<li>The pilot size of the urban programme: 157 urban local bodies in paragraph 5.22 and 150 in recommendation 9.</li>
<li>The text of DILRMP 3.0, its outlay and its approval date.</li>
<li>Any link between the Committee&rsquo;s figures and Telangana&rsquo;s Bhu Bharati figures; the report names Telangana only as a ULPIN pilot and a Fifth Schedule state.</li>
</ul></details>
'''

step(5, "assembling body and page")
body = STYLE + top + tvo + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://sansad.in/getFile/app/lsscommittee/Rural%20Development%20and%20Panchayati%20Raj/18_Rural_Development_and_Panchayati_Raj_41.pdf?source=app">Standing Committee on Rural Development and Panchayati Raj (2025&ndash;26), Forty-first Report on the Digital India Land Records Modernization Programme, presented to Lok Sabha on 11 August 2026</a> '
    '(official; the full text was read, 53 pages). Percentages, shares and ratios computed by this blog. Analysed 25 November 2026.')
RELATED = []

step(6, "building page")
build("Policy &middot; Land records", TITLE,
      "A parliamentary committee reports 99.81% of land records of rights computerised and 84.32% of villages with records and maps integrated; this piece sets out coverage, outlay, the urban pilot and the ten recommendations, and lists what the report does not show.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(plain), "chars in title")
step(7, "complete")
