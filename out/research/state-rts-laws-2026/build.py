"""Right-to-services laws across Indian states and UTs: who is covered, penalty and cap, appeal tiers, how many states and UTs have such laws, and what is counted.
Build from the repo root:  python3 out/research/state-rts-laws-2026/build.py   (writes out/post-india-right-to-service-laws-states.html)
Read in full from PRS copies on 21 November 2026: Delhi Act 10 of 2026; Karnataka Act 1 of 2012 with 2014 and 2026 amendments; Bihar Right to Public Services Act, 2011;
the English 2013 amendment to the Rajasthan Act (the principal Rajasthan text and the MP Act are page scans in the PRS PDFs with no text layer: their
English sections 6 to 8 were read by viewing the page images on 21 November 2026, which is a visual reading and not a text extract); PRS Legislative Brief of 27 September 2012 (comparison table of the 2011 state laws); PRS Annual Review of State Laws 2025 (ARSL 2025).
The count of 22 is from a Parliament answer published by PIB (Department of Administrative Reforms and Public Grievances); ARSL 2025 prints no count and the PIB text prints no list.
Names beyond the PRS documents come from the PIB text, a Lok Sabha answer, Acts and gazettes read as search excerpts (Meghalaya, Sikkim, Arunachal Pradesh, Chhattisgarh, Mizoram, Ladakh, Lakshadweep), commission pages (Chandigarh, Maharashtra) and lists (Wikipedia, Kerala Calling, SAFAR), all read on 21 November 2026. A blank cell means the figure was not read in an Act or named report."""
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
# Tier A: named in an Act, gazette, commission page or PRS document read (some only as search excerpts, see the post's source notes)
TIER_A = BRIEF_2012 | {"Karnataka", "Assam", "Kerala", "Meghalaya", "Sikkim", "Arunachal Pradesh", "Chandigarh", "Ladakh", "Lakshadweep",
                       "Chhattisgarh", "Mizoram", "Maharashtra"}
# Tier B: named in a report, paper or list (PIB Commission list, Wikipedia, Kerala Calling, SAFAR 2021, a Jharkhand paper), Act text not opened
TIER_B = {"Haryana", "West Bengal", "Gujarat", "Goa", "Jharkhand", "Odisha"}
PIB_COMMISSIONS = {"Assam", "Chandigarh", "Maharashtra", "Punjab", "Haryana", "Meghalaya", "Uttarakhand", "West Bengal"}   # PIB text: Commissions in 8
WIKI_TABLE = BRIEF_2012 | {"Kerala", "Karnataka", "Chhattisgarh", "Odisha", "Assam", "Gujarat", "West Bengal", "Goa", "Haryana", "Maharashtra", "Mizoram", "Jharkhand"}
assert len(PIB_COMMISSIONS) == 8 and len(WIKI_TABLE) == 21
assert not (TIER_A & TIER_B)
NAMED = TIER_A | TIER_B
assert (len(TIER_A), len(TIER_B), len(NAMED)) == (21, 6, 27)
assert PIB_COMMISSIONS <= NAMED and WIKI_TABLE <= NAMED
REPORTED = 22                      # PIB Rajya Sabha reply (3 April 2025) and Lok Sabha unstarred question 4216 (26 March 2025): 'enacted by 22 States and Union Territories'
OVER = len(NAMED) - REPORTED
assert OVER == 5                   # the names found exceed the reported count by five, so the 22 cannot be a complete list of the names found
# Left out of the 27 on purpose: Andaman and Nicobar Islands (a 2026 draft Regulation, after the PIB statement), Telangana and Tamil Nadu (listed in one law journal whose cited
# sources are a petition and a newspaper piece; no Act was found)
EXCLUDED = {"Andaman and Nicobar Islands", "Telangana", "Tamil Nadu"}
assert not (EXCLUDED & NAMED)
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
# MP Act 24 of 2010, section 7(1) and 7(2), and Rajasthan Act 23 of 2011, section 7(1) and 7(2) (English text, read from page images)
MPRJ_LUMP_LOW, MPRJ_LUMP_HIGH, MPRJ_RATE, MPRJ_CAP = 500, 5000, 250, 5000
assert MPRJ_CAP == MPRJ_LUMP_HIGH == D_CAP and MPRJ_RATE == D_RATE and MPRJ_CAP / MPRJ_RATE == 20
# The PRS 2012 brief's grouped Bihar/MP/UP/Rajasthan row (Rs 500 to Rs 5,000; Rs 250 a day up to Rs 5,000) matches the MP and Rajasthan Acts read
GROUP_LUMP_LOW, GROUP_LUMP_HIGH, GROUP_RATE, GROUP_CAP = 500, 5000, 250, 5000
assert (GROUP_LUMP_LOW, GROUP_LUMP_HIGH, GROUP_RATE, GROUP_CAP) == (MPRJ_LUMP_LOW, MPRJ_LUMP_HIGH, MPRJ_RATE, MPRJ_CAP)
MP_FIRST_DAYS, MP_SECOND_DAYS, MP_REVISION_DAYS = 30, 60, 60     # MP Act sections 6(1), 6(3), 8
RJ_FIRST_DAYS, RJ_SECOND_DAYS, RJ_REVISION_DAYS = 30, 60, 60     # Rajasthan Act sections 6(1), 6(3), 8 (section 8 replaced in 2013: revision to the Commission)
assert MP_FIRST_DAYS == RJ_FIRST_DAYS == 30 and MP_SECOND_DAYS == RJ_SECOND_DAYS == 60
DELHI2011_COST = 10
assert D_RATE / DELHI2011_COST == 25
APPEAL = {  # days allowed for the step after the first appeal
    "Madhya Pradesh (second appellate authority)": MP_SECOND_DAYS,   # Act section 6(3)
    "Rajasthan (second appellate authority)": RJ_SECOND_DAYS,        # Act section 6(3)
    "Bihar (reviewing authority)": 60,       # Act section 6(3)
    "Karnataka (appellate authority)": 60,   # Act section 13(3) as in the Karnataka post
    "Delhi (Commission)": 30,                # Act 10 of 2026 section 9(2)
}
assert sorted(APPEAL.values()) == [30, 60, 60, 60, 60]
# Disposal counters named in the two single-state posts
KA_DISPOSAL = round(100 * 431_632_443 / 432_426_014, 2)
assert f"{KA_DISPOSAL:.2f}" == "99.82"
DL_IN_TIME = 65.02
assert 100 - DL_IN_TIME == 34.98 or round(100 - DL_IN_TIME, 2) == 34.98

TITLE = H("India&rsquo;s right-to-service laws: 22 states and UTs reported, caps from Rs 500 to Rs 5,000")
assert 55 <= len(_h.unescape(TITLE)) <= 90, len(_h.unescape(TITLE))

step(3, "writing sections")
top = top_line([
    (f"{REPORTED}", f" states and union territories have enacted right-to-service laws, according to two 2025 answers to Parliament; sources read name {len(NAMED)}, so the 22 is not a complete list and none of the answers names them."),
    (f"Rs {K_CAP} to Rs {D_CAP:,}", f" is the range of per-case caps in the Acts read: Karnataka Rs {K_RATE} a day to Rs {K_CAP}, and Madhya Pradesh, Rajasthan and Delhi Rs {D_RATE} a day to Rs {D_CAP:,}."),
    ("2010", " is the year Madhya Pradesh enacted the first such law, followed by eight state laws dated 2011 in a 2012 PRS table, including Bihar, Rajasthan and the first Delhi Act."),
])

s1 = insight(
    H(f"Per-case caps: Rs {K_CAP} in Karnataka, Rs {D_CAP:,} in MP, Rajasthan and Delhi, none in Bihar"),
    bars(H(f"Three of five Acts cap a penalty at Rs {D_CAP:,} a case; Karnataka caps it at Rs {K_CAP}"),
         [("Karnataka Act, section 9 (compensation to the citizen)", K_CAP),
          ("Delhi Act 10 of 2026, section 8 (penalty to the treasury)", D_CAP),
          ("Madhya Pradesh Act, section 7 (penalty on the officer)", MPRJ_CAP),
          ("Rajasthan Act, section 7 (penalty recovered from salary)", MPRJ_CAP),
          ("Bihar Act, section 7: rates set in the rules", None),
          ("Delhi Act of 2011: Rs 10 an application, no cap printed (PRS 2012)", None)],
         accent="Delhi Act 10 of 2026, section 8 (penalty to the treasury)", unit="", fmt=lambda v: f"Rs {v:,.0f}", vmax=5500,
         sub="Maximum per case, rupees, as printed in each Act. A dashed bar means no cap is printed in the Act. The Madhya Pradesh and Rajasthan Acts were read from page scans.",
         source="Karnataka, Delhi, Bihar, Madhya Pradesh and Rajasthan Acts (PRS copies); PRS Legislative Brief, 27 September 2012 for Delhi 2011.")
    + numbers(["State and Act", "Delay", "Rejection", "Who receives it", "Basis"],
              [["Madhya Pradesh, 2010", f"Rs {MPRJ_RATE} a day, to Rs {MPRJ_CAP:,} (section 7(1)(b))", f"Lump sum Rs {MPRJ_LUMP_LOW} to Rs {MPRJ_LUMP_HIGH:,} for failure to provide the service (section 7(1)(a))", "Penalty on the designated officer; the second appellate authority may order part of it paid to the appellant as compensation, not above the penalty (section 7(3))", "Act text read from the PRS page scan; a first appeal officer who fails to decide an appeal in time faces Rs 500 to Rs 5,000 (section 7(2))"],
               ["Bihar, 2011", "Rate set in the rules (section 7(1)(b))", "Lump sum at the rate in the rules (section 7(1)(a))", "Charged on the officer, appellate authority or staff (section 7(3))", "Act text read; the rupee amounts are in rules that were not found, although the 2012 brief&rsquo;s group figure of Rs 250 a day up to Rs 5,000 matches the Madhya Pradesh and Rajasthan Acts"],
               ["Rajasthan, 2011", f"Rs {MPRJ_RATE} a day, to Rs {MPRJ_CAP:,} (section 7(1)(b))", f"Lump sum Rs {MPRJ_LUMP_LOW} to Rs {MPRJ_LUMP_HIGH:,} (section 7(1)(a))", "Recovered from the designated officer&rsquo;s salary (section 7(1)(c)); compensation to the appellant out of the penalty, not above it (section 7(3))", "Act text read from the PRS page scan; first appeal officer who fails to decide in time faces Rs 500 to Rs 5,000 (section 7(2))"],
               ["Karnataka, 2011", f"Rs {K_RATE} a day, to Rs {K_CAP} an application", "&ndash;", "Citizen is paid; cost recovered from the official", "Act text read (section 9); the 2026 amendment lets the Schedule set other rates"],
               ["Delhi, 2026", f"Rs {D_RATE} a day, to Rs {D_CAP:,} a case", f"Lump sum Rs {D_RATE} to Rs {D_CAP:,}", "Government treasury", "Act text read (section 8)"],
               ["Delhi, 2011 (repealed on commencement of the 2026 Act)", f"Rs {DELHI2011_COST} an application", "&ndash;", "&ndash;", "PRS 2012 brief, comparison table (secondary)"]]),
    "A citizen in Karnataka is paid for a delay and a citizen in Delhi is not, while Madhya Pradesh and Rajasthan let the appellate authority order compensation out of the penalty and Bihar leaves the amounts to rules that were not read.",
    "Each state should print the delay rate, the cap and the payee in the Schedule entry for each service so that a rule change is visible to applicants.",
    "money")

s2 = insight(
    H("Second-stage appeal windows: 60 days in four states, 30 days in Delhi"),
    bars(H("Four states allow 60 days for the second appeal step and Delhi allows 30"),
         [("Bihar: second appeal to the reviewing authority", APPEAL["Bihar (reviewing authority)"]),
          ("Karnataka: second appeal to the appellate authority", APPEAL["Karnataka (appellate authority)"]),
          ("Madhya Pradesh: second appeal to the second appellate authority", APPEAL["Madhya Pradesh (second appellate authority)"]),
          ("Rajasthan: second appeal to the second appellate authority", APPEAL["Rajasthan (second appellate authority)"]),
          ("Delhi: appeal to the Commission", APPEAL["Delhi (Commission)"])],
         accent="Delhi: appeal to the Commission", unit=" days", vmax=70,
         sub="Days allowed to take the step after the first one, as printed in each Act. All five first stages allow 30 days except Delhi, where the first appeal is automatic.",
         source="Madhya Pradesh Act and Rajasthan Act section 6(3); Bihar Act section 6(3); Karnataka Act section 13(3); Delhi Act 10 of 2026, section 9(2) (PRS copies).")
    + numbers(["State", "First stage", "Second stage", "Basis"],
              [["Madhya Pradesh", f"First appeal officer, {MP_FIRST_DAYS} days", f"Second appellate authority, {MP_SECOND_DAYS} days; revision to an officer the State nominates, {MP_REVISION_DAYS} days", "Act sections 6 and 8 (page scan)"],
               ["Bihar", "Appellate authority, 30 days", "Reviewing authority, 60 days", "Act sections 6(1) and 6(3)"],
               ["Rajasthan", f"First appeal officer, {RJ_FIRST_DAYS} days", f"Second appellate authority, {RJ_SECOND_DAYS} days; revision, {RJ_REVISION_DAYS} days, to a nominated officer in 2011 and to the Commission after the 2013 amendment", "Act sections 6 and 8 (page scan); 2013 amendment"],
               ["Karnataka", "Competent officer, 30 days", "Appellate authority, 60 days", "Act sections 13(1) and 13(3)"],
               ["Delhi (2026)", "Citizen Grievance Redressal Authority, appeal lodged automatically on a missed deadline", "Commission, 30 days", "Act sections 7 and 9"]]),
    "Each law read provides two stages of appeal inside the administration, with a revision step in Madhya Pradesh and Rajasthan and a Commission at the top in Rajasthan since 2013 and in Delhi.",
    "A citizen who is refused should note the date of the rejection or of the missed deadline, because the first window runs from that date in Bihar and Karnataka.",
    "appeals")

s3 = insight(
    H(f"Sources name {len(NAMED)} states and UTs against {REPORTED} reported; {len(TIER_A)} are named in an Act or gazette"),
    bars(H(f"{len(NAMED)} names found against the {REPORTED} reported by the Government of India"),
         [("Named in an Act, gazette or commission page (tier A)", len(TIER_A)),
          ("Named in a report or list, Act not opened (tier B)", len(TIER_B)),
          ("All names found (computed)", len(NAMED)),
          ("Reported to Parliament, 2025", REPORTED)],
         accent="Reported to Parliament, 2025", unit="", vmax=30,
         sub=f"States and union territories. The names exceed the reported count by {OVER}. No source read lists the 22, so which names the Government of India counts is not known.",
         source="PIB and Lok Sabha answers, 2025; Acts, gazettes and commission pages named in the sources; PRS brief 2012; Wikipedia, Kerala Calling and SAFAR lists. Totals computed here.")
    + numbers(["Tier", "States and UTs", "Basis"],
              [["A: Madhya Pradesh, Uttar Pradesh, Jammu and Kashmir, Delhi, Bihar, Himachal Pradesh, Rajasthan, Uttarakhand, Punjab", "9", "PRS Legislative Brief, 27 September 2012; Delhi, Bihar, Madhya Pradesh, Rajasthan and Karnataka Acts also read"],
               ["A: Karnataka, Assam, Kerala", "3", "Karnataka Act (PRS copy); Assam Act IX of 2012 (India Code excerpt) and PRS ARSL 2025; Kerala Bill of 2025 in PRS ARSL 2025 and an Act of 2012 per Kerala Calling"],
               ["A: Meghalaya, Sikkim, Arunachal Pradesh", "3", "Meghalaya Act 18 of 2020; Sikkim Public Services Delivery (Right to Service) Act, 2022 (Act 15 of 2022); Arunachal Pradesh Right to Public Services Act, 2016 (Act 3 of 2016); gazette excerpts"],
               ["A: Chandigarh, Ladakh, Lakshadweep", "3", "Chandigarh: Punjab Act extended by a Ministry of Home Affairs notification of 14 August 2017 (commission website); Ladakh: the Jammu and Kashmir Act as adapted for the Union Territory (Ladakh text, 2026); Lakshadweep: a Regulation of 2022, not an Act"],
               ["A: Chhattisgarh, Mizoram, Maharashtra", "3", "Chhattisgarh Lok Sewa Guarantee Act, 2011 (No. 23 of 2011), gazette notification of 18 June 2026; Mizoram Right to Public Services Act, 2015 (Act 6 of 2015), gazette of 7 November 2024; Maharashtra Right to Public Services Act, 2015, state commission annual report 2019-20"],
               ["B: Haryana, West Bengal, Gujarat, Goa, Jharkhand, Odisha", "6", "PIB Commission list (Haryana, West Bengal); SAFAR 2021 report (Gujarat, Jharkhand, Odisha); Wikipedia and Kerala Calling lists; a 2025 paper on Jharkhand&rsquo;s Act; Acts not opened"],
               ["All names", f"{len(NAMED)}", "Computed; Delhi counted once although its 2011 law is replaced by Act 10 of 2026"],
               ["Reported", f"{REPORTED}", "PIB Rajya Sabha reply and Lok Sabha question 4216 (answered 26 March 2025): enacted by 22 States and Union Territories, Commissions in 8; no list printed"],
               ["Names above the reported count", f"{OVER}", "Computed"]]),
    f"The Government of India&rsquo;s 22 is lower than the {len(NAMED)} names found, so it is a rounded or older count and not a list that could be matched name by name, and the five or more names it leaves out cannot be identified.",
    "The Department of Administrative Reforms and Public Grievances should publish the list of 22 with each Act, its year and whether it is in force, and say how Union Territory Regulations are counted.",
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
<li><b>PRS Legislative Research and state legislative departments:</b> post searchable text of the Acts, since the Madhya Pradesh and Rajasthan files are page scans.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Who is covered, and what is counted</summary>
<ul>
<li><b>Delhi 2026:</b> substantive government servants and employees of local bodies and authorities the Government owns, controls or substantially finances; casual, daily-wage and (unless the contract says otherwise) contract staff are excluded; only services in the Schedule are covered (section 1(4) and (5)).</li>
<li><b>Karnataka:</b> services in the Schedule, with the penalty falling on the designated officer or the subordinate who defaults; nothing applies where the Government has banned or restricted the service (section 9).</li>
<li><b>Madhya Pradesh and Rajasthan:</b> services, designated officers, first appeal officers, second appellate authorities and time limits notified by the State Government under section 3 of each Act; Rajasthan&rsquo;s Act defines a public authority to include bodies owned, controlled or substantially financed by the State.</li>
<li><b>Bihar:</b> services, designated public servants and appellate authorities notified by the Government under section 3; the penalty may be charged to the designated public servant, the appellate authority or staff (section 7(3)).</li>
<li><b>What is counted as a law:</b> the 2012 PRS table counts Acts and, for Madhya Pradesh, a Vidheyak (Bill) of 2010; the 2025 PRS review counts Bills passed and an Ordinance; the Wikipedia table mixes Acts, Bills and a 2015 Maharashtra Ordinance. This piece counts a state or union territory once whatever the number of its laws, counts a Regulation made by the President for Lakshadweep as a law, and does not know how the PIB count treats Bills, Ordinances or Regulations.</li>
<li><b>Stipulated time limits:</b> each Act fixes limits in a Schedule or notification, which this piece did not read for any state.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>Which 22. Two 2025 answers to Parliament (Rajya Sabha reply, PIB release dated 3 April 2025, and Lok Sabha unstarred question 4216 answered 26 March 2025) say the Right to Service Act has been enacted by 22 States and Union Territories, with Commissions in eight, and print no list. The names found reach 27, so at least five are left out, and which five was not established. The reason may be an older count, a different treatment of Union Territory Regulations, or both; no source says. Haryana, West Bengal, Gujarat, Goa, Jharkhand and Odisha are named in reports or lists whose Acts were not opened.</li>
<li>Names not counted among the 27. The Andaman and Nicobar Islands (Right to Public Services) Regulation, 2026 appears only as a draft with a blank number, dated July 2026. One law journal lists a Telangana Right to Services Act, 2016 and a Tamil Nadu Public Services Guarantee Act, 2019, but its footnotes point to a petition and a newspaper piece asking for such a law, and no Act was found for either.</li>
<li>Date conflicts. The fetched PIB page carries a date of 3 April 2025, while Wikipedia cites a PIB release of 22 June 2025 for the same count. Wikipedia gives Bihar&rsquo;s enactment as 25 July 2011 and a Kerala Calling article as 25 July 2012; the Act itself is titled 2011. Kerala has an Act of 2012 per Kerala Calling and a Bill of 2025 per PRS; how the two relate was not established.</li>
<li>Machine-readable text of the Madhya Pradesh and Rajasthan Acts. The PRS PDFs are page scans with no text layer, so sections 6 to 8 of each were read by viewing the page images. The Madhya Pradesh amendments (Acts 22 of 2011 and 5 of 2012, and later amendments listed in PRS reviews) and the rest of the Rajasthan Act were not read for changes to the penalty.</li>
<li>Bihar&rsquo;s rupee amounts. The Act says the rates are those in the rules; the rules were not found. The 2012 PRS brief groups Bihar with Madhya Pradesh, Uttar Pradesh and Rajasthan at Rs 250 a day up to Rs 5,000; that figure is confirmed in the Madhya Pradesh and Rajasthan Acts but not in Bihar&rsquo;s, so Bihar is treated as unreconciled.</li>
<li>The Rajasthan Right to Hearing Act, 2012 is a different Act from the Rajasthan Guaranteed Delivery of Public Services Act, 2011; a search excerpt about a Rs 500 to Rs 5,000 fine on a Public Hearing Officer relates to the former and is not used here.</li>
<li>Pending applications: no pending or disposal figure was found for Madhya Pradesh, Bihar or Rajasthan, and none is given.</li>
<li>Whether each law is in force today, which Schedules exist, and how many services each state has notified (other than the Karnataka and Delhi counters in the single-state posts).</li>
<li>The 2012 PRS brief reflects laws as of its date, and the figures for Uttar Pradesh, Jammu and Kashmir, Himachal Pradesh, Uttarakhand and Punjab come from it alone; later amendments may have changed them.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://prsindia.org/files/legislature/ARSL_2025.pdf">PRS Legislative Research, Annual Review of State Laws 2025</a> (primary report; no count of right-to-service laws); '
    '<a href="https://prsindia.org/files/bills_acts/bills_parliament/2011/Legislative_Brief_Citizens_Charter_27_Sep.pdf">PRS Legislative Brief, Citizens Charter Bill, 2011, 27 September 2012</a> (named report; comparison table of the 2011 state laws); '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/delhi/2026/Act10of2026DL.pdf">Delhi Act 10 of 2026, PRS copy</a>; '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/karnataka/2012/2012KA1.pdf">Karnataka Sakaala Services Act, PRS compilation</a>; '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/bihar/2011/2011Bihar4.pdf">The Bihar Right to Public Services Act, 2011, PRS copy</a>; '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/rajasthan/2011/2011Rajasthan23.pdf">The Rajasthan Guaranteed Delivery of Public Services Act, 2011 with the 2013 amendment, PRS copy</a> (page scan; amendment has a text layer); '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/madhya-pradesh/2010/2010MP24.pdf">Madhya Pradesh Lok Sewaon ke Pradan ki Guarantee Adhiniyam, 2010, PRS copy</a> (page scan); '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2118276">PIB, Parliament question on Sevottam and redressal of public grievances</a> (primary; 22 states and UTs, eight Commissions); '
    '<a href="https://sansad.in/getFile/loksabhaquestions/annex/184/AU4216_YkZmPz.pdf?source=pqals">Lok Sabha unstarred question 4216, answered 26 March 2025</a> (primary; same 22 and eight Commissions); '
    '<a href="https://meghalaya.gov.in/sites/default/files/acts/LL_B_55_2013_50.pdf">Meghalaya Right to Public Services Act, 2020</a> (primary Gazette; read as a search excerpt); '
    '<a href="https://www.sikkim.gov.in/uploads/Gazette/363_20240720.pdf">Sikkim Gazette, Act 15 of 2022</a> and '
    '<a href="https://eodb.arunachal.gov.in/uploads/policyguideline_documents/f6f6fd30f1ebb16e359805e98781cfd9.pdf">Arunachal Pradesh Gazette, Act 3 of 2016</a> (primary; search excerpts); '
    '<a href="http://rtsc.chd.gov.in/">Chandigarh Right to Service Commission</a> (primary; Punjab Act extended in 2017); '
    '<a href="https://eodb.ladakh.gov.in/storage/uploads/incentives/20260514225404_6a060534d66f9.pdf">Ladakh text of the Public Services Guarantee Act, 2011</a> and '
    '<a href="https://thc.nic.in/Central%20Governmental%20Regulations/Lakshadweep%20(Right%20To%20Public%20Services)%20Regulation,%202022.pdf">Lakshadweep (Right to Public Services) Regulation, 2022</a> (primary; search excerpts); '
    '<a href="https://egazette.servantsofknowledge.in/details/in.gazette.chhattisgarh.eo.2026-06-19.334">Chhattisgarh Gazette, 19 June 2026</a>, '
    '<a href="https://dpar.mizoram.gov.in/page/mizoram-right-to-public-services-act-2015">Mizoram Department of Personnel and Administrative Reforms page</a> and '
    '<a href="https://aaplesarkar.mahaonline.gov.in/pdf/Annual_Report_2019-20_English.pdf">Maharashtra State Commission annual report, 2019-20</a> (official; search excerpts); '
    '<a href="https://safar-india.org/documents/RTPSD_Final.pdf">SAFAR scoping study of right-to-public-service Acts, 2021</a> and '
    '<a href="https://ijcrt.org/papers/IJCRT2509471.pdf">IJCRT paper on the Jharkhand Right to Service Act, 2025</a> (secondary; search excerpts); '
    '<a href="https://mspsdc.meghalaya.gov.in/viewpresentation.htm?presentationid=8">Meghalaya State Public Services Delivery Commission presentation, 2023</a> (state document, excerpt: Karnataka, Jammu and Kashmir, Haryana, Gujarat and Delhi Acts); '
    '<a href="https://keralacalling.kerala.gov.in/right-to-service-act-a-leap-in-governance">Kerala Calling, 23 September 2023</a> (secondary; list of states); '
    '<a href="https://en.wikipedia.org/wiki/Right_to_Public_Services_legislation">Wikipedia, Right to Public Services legislation</a> (secondary; table of implementing states); '
    '<a href="https://accountabilityindia.in/wp-content/uploads/2020/03/policy_brief_right_to_service_laws_0.pdf">Accountability Initiative policy brief, January 2012</a> (secondary; the eight 2011 laws). '
    'Ratios and differences computed by this blog. Analysed 21 November 2026.')
RELATED = [(B + "/2026/11/karnataka-sakaala-services-act-rs-20.html", "Karnataka Sakaala Services Act: Rs 20 a day for delay, capped at Rs 500")]
step(4, "assembling page")
build("Governance &middot; India", TITLE,
      "A comparison of right-to-service laws across Indian states: who is covered, the penalty per day and its cap, the appeal tiers, and how the reported 22 states and union territories compare with the 27 names found in sources.",
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
