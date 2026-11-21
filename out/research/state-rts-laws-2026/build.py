"""Right-to-services laws across Indian states and UTs: who is covered, penalty and cap, appeal tiers, how many states and UTs have such laws, and what is counted.
Build from the repo root:  python3 out/research/state-rts-laws-2026/build.py   (writes out/post-india-right-to-service-laws-states.html)
Read in full from PRS copies on 21 November 2026: Delhi Act 10 of 2026; Karnataka Act 1 of 2012 with 2014 and 2026 amendments; Bihar Right to Public Services Act, 2011;
the English 2013 amendment to the Rajasthan Act (the principal Rajasthan text and the MP Act pages are scanned or font-garbled in the PRS PDFs and gave only
their header lines); PRS Legislative Brief of 27 September 2012 (comparison table of the 2011 state laws); PRS Annual Review of State Laws 2025 (ARSL 2025).
The count of 22 comes from a search excerpt of a Wikipedia article; ARSL 2025 does not print a count. A blank cell means the figure was not read in an Act or named report."""
import pathlib
import re
import sys
import time
import html as _h

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-right-to-service-laws-states.html"
B = "https://blog.vertistratsolution.com"
STEPS = 7


def step(n, what):
    el = time.time() - T0
    eta = el / n * (STEPS - n) if n else 0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {eta:.1f}s left)", flush=True)


HEADS = []


def H(t):
    HEADS.append(t)
    return t


# ---- 1. Laws named in documents that were read
step(1, "count of laws named in documents read, with consistency checks")
# PRS brief of 27 Sep 2012, table 'Sources' line: nine state laws
BRIEF_2012 = {"Madhya Pradesh", "Uttar Pradesh", "Jammu and Kashmir", "Delhi", "Bihar", "Himachal Pradesh", "Rajasthan", "Uttarakhand", "Punjab"}
assert len(BRIEF_2012) == 9
# Read as Acts on PRS: Karnataka (Act 1 of 2012). ARSL 2025: Assam (Right to Public Services Amendment Bill and Ordinance) and Kerala (Right to Public Service Bill, 2025).
ARSL_2025 = {"Assam", "Kerala"}
OTHER_READ = {"Karnataka"}
NAMED = BRIEF_2012 | ARSL_2025 | OTHER_READ
assert len(NAMED) == 12 and not (BRIEF_2012 & ARSL_2025) and not (BRIEF_2012 & OTHER_READ)
REPORTED = 22                      # Wikipedia, 'as of 2025, 22 States and Union Territories' (search excerpt; no list read)
UNNAMED = REPORTED - len(NAMED)
assert UNNAMED == 10
# Delhi: 2011 law replaced by Delhi Act 10 of 2026, so Delhi is one state or UT with a law, not two
assert "Delhi" in BRIEF_2012
FIRST_YEAR, SECOND_YEAR_COUNT = 2010, 8       # brief: MP 2010; eight more state laws dated 2011 in the table's source list
assert len(BRIEF_2012) - 1 == SECOND_YEAR_COUNT
assert FIRST_YEAR == 2010

# ---- 2. Penalty and cap, as printed in Acts read
step(2, "penalty and appeal figures with consistency checks")
K_RATE, K_CAP = 20, 500
D_RATE, D_CAP = 250, 5000
assert K_CAP / K_RATE == 25 and D_CAP / D_RATE == 20
assert D_CAP / K_CAP == 10 and D_RATE / K_RATE == 12.5
GROUP_LUMP_LOW, GROUP_LUMP_HIGH, GROUP_RATE, GROUP_CAP = 500, 5000, 250, 5000      # PRS 2012 brief, grouped Bihar/MP/UP/Rajasthan row
assert GROUP_CAP == GROUP_LUMP_HIGH == D_CAP and GROUP_RATE == D_RATE and GROUP_CAP / GROUP_RATE == 20
DELHI2011_COST = 10
assert D_RATE / DELHI2011_COST == 25
APPEAL = {  # days allowed for the step after the first appeal
    "Bihar (reviewing authority)": 60,       # Act section 6(3)
    "Karnataka (appellate authority)": 60,   # Act section 13(3) as in the Karnataka post
    "Rajasthan (revision to the Commission)": 60,   # 2013 amendment, new section 8
    "Delhi (Commission)": 30,                # Act 10 of 2026 section 9(2)
}
assert sorted(APPEAL.values()) == [30, 60, 60, 60]
# Disposal counters named in the two single-state posts
KA_DISPOSAL = round(100 * 431_632_443 / 432_426_014, 2)
assert f"{KA_DISPOSAL:.2f}" == "99.82"
DL_IN_TIME = 65.02
assert 100 - DL_IN_TIME == 34.98 or round(100 - DL_IN_TIME, 2) == 34.98

TITLE = H("India&rsquo;s right-to-service laws: a reported 22 states and UTs, caps from Rs 500 to Rs 5,000")
assert 55 <= len(_h.unescape(TITLE)) <= 90, len(_h.unescape(TITLE))

step(3, "writing sections")
top = top_line([
    (f"{REPORTED}", f" states and union territories are reported to have right-to-service laws as of 2025 by one source, Wikipedia; the PRS annual review of 2025 prints no count, and only {len(NAMED)} are named in documents read for this piece."),
    (f"Rs {K_CAP} to Rs {D_CAP:,}", f" is the range of the per-case caps printed in the two Acts read in full for the figure: Karnataka at Rs {K_RATE} a day to Rs {K_CAP}, Delhi at Rs {D_RATE} a day to Rs {D_CAP:,}."),
    ("2010", " is the year Madhya Pradesh enacted the first such law, followed by eight state laws dated 2011 in a 2012 PRS table, including Bihar, Rajasthan and the first Delhi Act."),
])

s1 = insight(
    H(f"Per-case caps: Rs {K_CAP} in Karnataka, Rs {D_CAP:,} in Delhi, none printed in Bihar&rsquo;s Act"),
    bars(H(f"Delhi caps a penalty at Rs {D_CAP:,} a case, ten times Karnataka&rsquo;s Rs {K_CAP}"),
         [("Karnataka Act, section 9 (compensation to the citizen)", K_CAP),
          ("Delhi Act 10 of 2026, section 8 (penalty to the treasury)", D_CAP),
          ("MP, Rajasthan and UP, PRS 2012 brief, grouped (secondary)", GROUP_CAP),
          ("Bihar Act, section 7: rates set in the rules", None),
          ("Delhi Act of 2011: Rs 10 an application, no cap printed (PRS 2012)", None)],
         accent="Delhi Act 10 of 2026, section 8 (penalty to the treasury)", unit="", fmt=lambda v: f"Rs {v:,.0f}", vmax=5500,
         sub="Maximum per case, rupees, as printed. A dashed bar means no cap was read. The grouped bar is a 2012 summary of several states&rsquo; laws, not read from their Acts.",
         source="Karnataka Act and Delhi Act 10 of 2026 (PRS copies); Bihar Act (PRS copy); PRS Legislative Brief, 27 September 2012.")
    + numbers(["State and Act", "Delay", "Rejection", "Who receives it", "Basis"],
              [["Madhya Pradesh, 2010", "&ndash;", "&ndash;", "&ndash;", "Act pages are scanned in the PRS PDF and were not read; PRS 2012 brief groups MP with Bihar, UP and Rajasthan at Rs 250 a day up to Rs 5,000 and Rs 500 to Rs 5,000 lump sum (secondary)"],
               ["Bihar, 2011", "Rate set in the rules (section 7(1)(b))", "Lump sum at the rate in the rules (section 7(1)(a))", "Charged on the officer, appellate authority or staff (section 7(3))", "Act text read; the 2012 brief&rsquo;s Rs 250 and Rs 5,000 for this group does not appear in the Act, so it may come from the rules"],
               ["Rajasthan, 2011", "&ndash;", "&ndash;", "&ndash;", "Principal Act text is garbled in the PRS PDF; the 2013 amendment was read; the 2012 brief groups Rajasthan with the figures above (secondary)"],
               ["Karnataka, 2011", f"Rs {K_RATE} a day, to Rs {K_CAP} an application", "&ndash;", "Citizen is paid; cost recovered from the official", "Act text read (section 9); the 2026 amendment lets the Schedule set other rates"],
               ["Delhi, 2026", f"Rs {D_RATE} a day, to Rs {D_CAP:,} a case", f"Lump sum Rs {D_RATE} to Rs {D_CAP:,}", "Government treasury", "Act text read (section 8)"],
               ["Delhi, 2011 (repealed on commencement of the 2026 Act)", f"Rs {DELHI2011_COST} an application", "&ndash;", "&ndash;", "PRS 2012 brief, comparison table (secondary)"]]),
    "A citizen in Karnataka receives money for a delay and a citizen in Delhi does not, while Bihar&rsquo;s Act leaves every rupee amount to rules that were not read.",
    "Each state should print the delay rate, the cap and the payee in the Schedule entry for each service so that a rule change is visible to applicants.",
    "money")

s2 = insight(
    H("Second-stage appeal windows: 60 days in Bihar, Karnataka and Rajasthan, 30 in Delhi"),
    bars(H("Three states allow 60 days for the second step and Delhi allows 30"),
         [("Bihar: second appeal to the reviewing authority", APPEAL["Bihar (reviewing authority)"]),
          ("Karnataka: second appeal to the appellate authority", APPEAL["Karnataka (appellate authority)"]),
          ("Rajasthan: revision to the Commission (2013 amendment)", APPEAL["Rajasthan (revision to the Commission)"]),
          ("Delhi: appeal to the Commission", APPEAL["Delhi (Commission)"])],
         accent="Delhi: appeal to the Commission", unit=" days", vmax=70,
         sub="Days allowed to take the step after the first one, as printed in each Act. Madhya Pradesh has a first appeal officer and a second appellate authority per the PRS file header; its windows were not read.",
         source="Bihar Act section 6(3); Karnataka Act section 13(3); Rajasthan 2013 amendment, section 8; Delhi Act 10 of 2026, section 9(2) (PRS copies).")
    + numbers(["State", "First stage", "Second stage", "Basis"],
              [["Madhya Pradesh", "First appeal officer", "Second appellate authority", "PRS file header keywords; Act text not read"],
               ["Bihar", "Appellate authority, 30 days", "Reviewing authority, 60 days", "Act sections 6(1) and 6(3)"],
               ["Rajasthan", "First appeal officer", "Second appellate authority, then revision to the Commission in 60 days", "PRS file header keywords; 2013 amendment, section 8"],
               ["Karnataka", "Competent officer, 30 days", "Appellate authority, 60 days", "Act sections 13(1) and 13(3)"],
               ["Delhi (2026)", "Citizen Grievance Redressal Authority, appeal lodged automatically on a missed deadline", "Commission, 30 days", "Act sections 7 and 9"]]),
    "Each law read provides two stages of appeal inside the administration, and the Rajasthan and Delhi Acts add a Commission at the top.",
    "A citizen who is refused should note the date of the rejection or of the missed deadline, because the first window runs from that date in Bihar and Karnataka.",
    "appeals")

s3 = insight(
    H(f"The count of {REPORTED} comes from one source; {len(NAMED)} states are named in documents read"),
    bars(H(f"Only {len(NAMED)} of the reported {REPORTED} states and UTs are named in documents read here"),
         [("Named in documents read for this piece", len(NAMED)),
          ("Reported by one source for 2025", REPORTED),
          ("Reported but not named (computed)", UNNAMED)],
         accent="Reported but not named (computed)", unit="", vmax=24,
         sub=f"States and union territories. The {len(NAMED)} are the nine in the 2012 PRS table, Karnataka, and Assam and Kerala from the PRS 2025 review. The 22 is from a Wikipedia excerpt with no list; the PRS review prints no total.",
         source="PRS Legislative Brief, 27 September 2012; PRS Annual Review of State Laws 2025; Karnataka Act (PRS copy); Wikipedia excerpt for the 22. Difference computed here.")
    + numbers(["Group", "States and UTs", "Basis"],
              [["Madhya Pradesh (2010)", "1", "PRS file for Act 24 of 2010; Wikipedia gives 18 August 2010 (secondary)"],
               ["State laws with a 2011 source in the PRS table", "8: Uttar Pradesh, Jammu and Kashmir, Delhi, Bihar, Himachal Pradesh, Rajasthan, Uttarakhand, Punjab", "PRS brief, 27 September 2012; Delhi and Bihar also read as Acts"],
               ["Karnataka", "1", "Act 1 of 2012 (PRS copy)"],
               ["Assam, Kerala", "2", "PRS ARSL 2025 lists the Assam Right to Public Services (Amendment) Bill, 2025 and Ordinance, 2024, and the Kerala Right to Public Service Bill, 2025"],
               ["Named total", f"{len(NAMED)}", "Computed; Delhi counted once although its 2011 law is replaced by Act 10 of 2026"],
               ["Reported for 2025", f"{REPORTED}", "Wikipedia excerpt; no list read; counts differ by source and by whether Bills and Ordinances count"],
               ["Reported but not named", f"{UNNAMED}", "Computed"]]),
    "A count of 22 may be right, but it cannot be checked from the PRS review, which covers 2025 enactments only, and it depends on whether Bills, Ordinances and repealed laws are counted.",
    "A reader quoting the number should name the source and year, and state whether a Bill that has passed but is not in force counts.",
    "count")

s4 = insight(
    H(f"Disposal counters: Karnataka {KA_DISPOSAL}%, Delhi {DL_IN_TIME}% in time, none found elsewhere"),
    bars(H("Karnataka and Delhi publish a counter; none found for Madhya Pradesh, Bihar, Rajasthan"),
         [("Karnataka: share of receipts with a recorded disposal", KA_DISPOSAL),
          ("Delhi: share of applications disposed in time", DL_IN_TIME),
          ("Madhya Pradesh", None), ("Bihar", None), ("Rajasthan", None)],
         accent="Delhi: share of applications disposed in time", unit="%", vmax=100,
         sub="Per cent. The two counters measure different things: Karnataka counts any recorded disposal and Delhi counts disposal in time. Both are undated portal figures read from search excerpts. A dashed bar means no figure was found.",
         source="Sakala portal and Delhi e-SLA dashboard (search excerpts, 21 November 2026), as used in the Karnataka and Delhi posts.")
    + numbers(["State", "Counter found", "What it counts"],
              [["Karnataka", "99.82% of 432,426,014 receipts have a recorded disposal", "Disposal of any kind; no timeliness split"],
               ["Delhi", "65.02% of over 36 lakh applications disposed in time", "The e-SLA system of the 2011 law; definition of in time not read"],
               ["Madhya Pradesh, Bihar, Rajasthan", "None found", "No pending or disposal figure was found in any source read"]]),
    "A disposal rate and an in-time rate cannot be compared across states, and states with no published counter cannot be assessed at all.",
    "Each state should publish applications received, delivered in time, delivered late, rejected and pending, by service, on a stated date.",
    "counters")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>State right-to-service commissions:</b> publish an annual report with applications received, delivered in time, late, rejected and pending, by department.</li>
<li><b>State governments:</b> print the delay rate, the cap and the payee beside each service in the Schedule.</li>
<li><b>Department of Administrative Reforms and Public Grievances, Government of India:</b> keep one dated list of the states and union territories with a right-to-service law, with the Act, its year and whether it is in force.</li>
<li><b>PRS Legislative Research and state legislative departments:</b> post readable text of the Acts, since the Madhya Pradesh and Rajasthan files could not be read as text.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Who is covered, and what is counted</summary>
<ul>
<li><b>Delhi 2026:</b> substantive government servants and employees of local bodies and authorities the Government owns, controls or substantially finances; casual, daily-wage and (unless the contract says otherwise) contract staff are excluded; only services in the Schedule are covered (section 1(4) and (5)).</li>
<li><b>Karnataka:</b> services in the Schedule, with the penalty falling on the designated officer or the subordinate who defaults; nothing applies where the Government has banned or restricted the service (section 9).</li>
<li><b>Bihar:</b> services, designated public servants and appellate authorities notified by the Government under section 3; the penalty may be charged to the designated public servant, the appellate authority or staff (section 7(3)).</li>
<li><b>What is counted as a law:</b> the 2012 PRS table counts Acts and, for Madhya Pradesh, a Vidheyak (Bill) of 2010; the 2025 review counts Bills passed and an Ordinance. This piece counts a state once whatever the number of its laws, and a Bill that was reported as passed is counted as a law only where the review says it was passed.</li>
<li><b>Stipulated time limits:</b> each Act fixes limits in a Schedule or notification, which this piece did not read for any state.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The number of states and union territories with a right-to-service law. The figure of 22 is read only from a Wikipedia excerpt; the PRS Annual Review of State Laws 2025 prints no count and names only the Assam and Kerala measures. The remaining 10 were not identified from a source read.</li>
<li>The penalty and cap in the Madhya Pradesh and Rajasthan Acts. The PRS PDFs for the Madhya Pradesh Act (Act 24 of 2010, with Acts 22 of 2011 and 5 of 2012) and the principal Rajasthan Act (Act 23 of 2011) did not yield readable text, so those cells are blank in the table apart from the 2012 PRS brief&rsquo;s grouped summary, which is secondary.</li>
<li>Bihar&rsquo;s rupee amounts. The Act says the rates are those in the rules; the rules were not found. The 2012 PRS brief groups Bihar with states said to have Rs 250 a day up to Rs 5,000, which the Act text does not itself state, so the two are treated as unreconciled.</li>
<li>One search summary listed Kerala as having a law in 2012 and other states with later years (Odisha, West Bengal, Goa, Haryana, Maharashtra, Mizoram), while the PRS review for 2025 reports a Kerala Bill passed that year. These years were not read in any document and are not used.</li>
<li>The Rajasthan Right to Hearing Act, 2012 is a different Act from the Rajasthan Guaranteed Delivery of Public Services Act, 2011; a search excerpt about a Rs 500 to Rs 5,000 fine on a Public Hearing Officer relates to the former and is not used here.</li>
<li>Pending applications: no pending or disposal figure was found for Madhya Pradesh, Bihar or Rajasthan, and none is given.</li>
<li>Whether each law is in force today, which Schedules exist, and how many services each state has notified (other than the Karnataka and Delhi counters in the single-state posts).</li>
<li>The 2012 PRS brief reflects laws as of its date; later amendments to the Bihar, Madhya Pradesh and Rajasthan Acts may have changed the figures.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://prsindia.org/files/legislature/ARSL_2025.pdf">PRS Legislative Research, Annual Review of State Laws 2025</a> (primary report; no count of right-to-service laws); '
    '<a href="https://prsindia.org/files/bills_acts/bills_parliament/2011/Legislative_Brief_Citizens_Charter_27_Sep.pdf">PRS Legislative Brief, Citizens Charter Bill, 2011, 27 September 2012</a> (named report; comparison table of the 2011 state laws); '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/delhi/2026/Act10of2026DL.pdf">Delhi Act 10 of 2026, PRS copy</a>; '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/karnataka/2012/2012KA1.pdf">Karnataka Sakaala Services Act, PRS compilation</a>; '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/bihar/2011/2011Bihar4.pdf">The Bihar Right to Public Services Act, 2011, PRS copy</a>; '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/rajasthan/2011/2011Rajasthan23.pdf">The Rajasthan Guaranteed Delivery of Public Services Act, 2011 with the 2013 amendment, PRS copy</a> (only the amendment was readable); '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/madhya-pradesh/2010/2010MP24.pdf">Madhya Pradesh Lok Sewaon ke Pradan ki Guarantee Adhiniyam, 2010, PRS copy</a> (header only readable); '
    '<a href="https://en.wikipedia.org/wiki/Right_to_Public_Services_legislation">Wikipedia, Right to Public Services legislation</a> (secondary, search excerpt: 22 states and UTs as of 2025; MP 2010); '
    '<a href="https://accountabilityindia.in/wp-content/uploads/2020/03/policy_brief_right_to_service_laws_0.pdf">Accountability Initiative policy brief on right-to-service laws</a> (listed in search results; not opened). '
    'Ratios and differences computed by this blog. Analysed 21 November 2026.')
RELATED = [(B + "/2026/11/karnataka-sakaala-services-act-rs-20.html", "Karnataka Sakaala Services Act: Rs 20 a day for delay, capped at Rs 500")]
step(4, "assembling page")
build("Governance &middot; India", TITLE,
      "A comparison of right-to-service laws across Indian states: who is covered, the penalty per day and its cap, the appeal tiers, and why the reported count of 22 states and union territories cannot yet be checked.",
      body, SOURCES, RELATED, str(OUT))
step(5, "checking output")
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
for h2 in re.findall(r'<h2 class="gb-h2"[^>]*>(.*?)</h2>', body):
    HEADS.append(h2)
for t in re.findall(r'class="xv-t"[^>]*>(.*?)</span>', body):
    HEADS.append(t)
for h in HEADS:
    p = _h.unescape(h)
    assert len(p) <= 90, (len(p), p)
    assert "?" not in p, p
    assert not any(w in p.lower().replace(",", " ").split() for w in ("you", "your", "we", "our")), p
step(6, "headline checks done")
step(7, "complete")
print("wrote", OUT.relative_to(ROOT), "| title", len(_h.unescape(TITLE)), "chars | headings checked:", len(HEADS))
