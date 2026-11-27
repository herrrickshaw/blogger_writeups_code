"""Environmental clearance in India: who decides, what NABET does, the clocks, and the approval-finder tools.
Build from the repo root:  python3 out/research/ec-approval-process-2026/build.py   (writes out/post-india-environmental-clearance-process-nabet-seiaa.html)
Arithmetic lives in calc.py beside this file and is asserted there; this file re-asserts what it prints. Researched 27 November 2026.
Opened and read: EIA Notification 2006 as consolidated on PARIVESH (text 'as on 13 July 2026'), MoEFCC office memoranda on PARIVESH, the NABET EIA scheme page and FAQs, the NABET portal list of accredited
consultants, the NSWS pages and user guides, the PARIVESH Know Your Approvals FAQ and page, the Maharashtra MAITRI user manual, PIB (27 Mar 2023). Not used for any figure: the commercial summary on regaffairs (cross-check only)."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402
import calc as c  # noqa: E402  (importing runs the asserts)

OUT = ROOT / "out/post-india-environmental-clearance-process-nabet-seiaa.html"
B = "https://blog.vertistratsolution.com"
TITLE = "Environmental clearance in India: central or state, NABET's role and a 105-day clock"
assert 55 <= len(TITLE) <= 90, len(TITLE)
assert (c.N, len(c.A), len(c.B), c.LAPSED, c.TOTAL_AFTER_FINAL_EIA) == (256, 225, 31, 27, 105)

top = top_line([
    (f"{c.TOTAL_AFTER_FINAL_EIA} days", " is the limit the EIA Notification sets from the final EIA report to a decision: 60 days for the expert committee and 45 for the authority. If the authority stays silent, the applicant may proceed as the committee finally recommended."),
    (f"{len(c.A)} of {c.N}", f" accredited EIA consultant organisations on the NABET portal are category A, the only kind that may prepare the EIA for a category A project. {c.LAPSED} of the {c.N} entries show a validity date that had already passed on 27 November 2026."),
    ("5 km", " from a protected area, critically polluted area, eco-sensitive area or inter-state boundary moves a category B project from the State authority to the Ministry, which then appraises it as category A (10 km for river valley, thermal power, industrial estates and hazardous-waste sites)."),
])

# ---------------------------------------------------------------- section 1: who decides
chart1 = flow([
    ("1. Find the item in the Schedule", "The Schedule to the EIA Notification lists each activity with a threshold. The threshold makes the project category A or B."),
    ("Category A", "The Ministry of Environment, Forest and Climate Change (MoEFCC) decides, on the advice of the Expert Appraisal Committee (EAC). Scoping, an EIA report and a public hearing apply, with a few exceptions.", True),
    ("Category B", "The State or Union Territory Environment Impact Assessment Authority (SEIAA) decides, on the advice of its State Expert Appraisal Committee (SEAC). The SEAC screens the application first.", True),
    ("B1 and B2", "B1 needs an EIA report, terms of reference and a public hearing. B2 skips all three and is appraised on Form 1 and its documents."),
    ("Minor minerals, 5 ha or less", "These are B2 projects. A District Environment Impact Assessment Authority (DEIAA) decides on its district committee&rsquo;s advice, and the SEIAA supervises it."),
    ("The General Condition", "A category B project within 5 km of a protected area, critically polluted area, eco-sensitive area or inter-state or international boundary is appraised by the Ministry as category A. The distance is 10 km for river valley, thermal power, industrial estates and parks, and common hazardous-waste facilities. Two States sharing a boundary can agree to reduce or waive the boundary distance."),
    ("When the State body does not exist", "A Ministry memorandum of 28 February 2025 says a category B project is considered centrally if no SEIAA or SEAC is duly constituted. A notification of 13 July 2026 (S.O. 3862(E)) sets a four-year term for a SEIAA&rsquo;s chairman and non-official members and lets a Standing Authority on EIA act for up to six months, extendable by six."),
])
tbl1 = numbers(["Activity (Schedule item)", "Category A", "Category B", "Status"],
               [["Mining of minerals, 1(a)", "Above 250 ha of lease for major minerals other than coal; above 500 ha for coal; asbestos at any size", "250 ha or less for major minerals other than coal; all minor-mineral leases", "Consolidated text, July 2026"],
                ["Thermal power, 1(d)", "500 MW and above for coal, lignite, naphtha and gas", "Above 5 MW and below 500 MW for the same fuels; General Condition applies", "Consolidated text; the &lsquo;and above&rsquo; symbol did not survive the text extraction, the B row reads &lsquo;below 500&rsquo;"],
                ["Distilleries, 5(g)", "Molasses-based above 100 KLD; non-molasses above 200 KLD", "Molasses-based below 100 KLD; non-molasses below 200 KLD", "The exact 100 and 200 KLD boundary cases were not legible in the text read"]],
               "Show three Schedule examples")
means1 = "The category, set by the size of the activity in the Schedule, decides whether the Ministry or the State authority grants the clearance, and a site next to a protected area or a State boundary can override the size."
todo1 = "Companies should read the Schedule row, the General Condition and the project&rsquo;s coordinates together before choosing the authority, because a wrong choice means filing again."
s1 = insight("Who decides: category A goes to the Ministry, B to the State, and 5 km can move B to A", chart1 + tbl1, means1, todo1, "who")

# ---------------------------------------------------------------- section 2: the clock
rows2 = [("Standard terms of reference online, listed cases (working days)", c.TOR_STANDARD_WORKING_DAYS),
         ("Application referred to the committee, or standard terms issue on day 30", c.TOR_REFERRAL),
         ("Minimum public notice before a hearing", c.HEARING_NOTICE_MIN),
         ("Pollution board forwards the hearing proceedings, from the request", c.HEARING_PROCEEDINGS),
         ("Expert committee completes appraisal", c.APPRAISAL),
         ("Authority decides, from the committee&rsquo;s recommendation", c.DECISION),
         ("Final EIA report to decision: 60 + 45", c.TOTAL_AFTER_FINAL_EIA)]
chart2 = bars(f"Up to {c.TOTAL_AFTER_FINAL_EIA} days from the final EIA report to a decision, and each step has its own limit", rows2,
              accent="Final EIA report to decision: 60 + 45", unit=" days", vmax=120,
              sub="Limits written into the EIA Notification, days unless stated. They are separate clocks, not one running total, except the last row. The time to prepare the EIA study is not in the notification.",
              source="EIA Notification 2006 (S.O. 1533(E), 14 September 2006) as consolidated on PARIVESH, text as on 13 July 2026: para 7(i), para 8 and Appendix IV.")
tbl2 = numbers(["Stage", "Applies to", "What happens", "Limit in the notification"],
               [["Screening", "Category B only", "The SEAC decides whether the project needs an EIA (B1) or not (B2)", "None stated for screening alone; a B2 is decided within 105 days of a complete application"],
                ["Scoping", "A and B1", "The committee fixes the terms of reference (ToR) for the EIA study", "Standard ToR in 7 working days for listed cases; others referred within 30 days or standard ToR issue on day 30; ToR valid 4 years (5 for river valley and hydro projects)"],
                ["Public consultation", "A and B1", "The State pollution board holds a hearing near the site, and written comments are taken", "At least 30 days&rsquo; notice; proceedings forwarded within 45 days of the request; if the board does not, another agency gets 45 more days"],
                ["Appraisal", "All except exempt cases", "The committee examines the final EIA, hearing outcome and replies, with the applicant invited", "60 days to complete; recommendation to the authority within the next 15 days"],
                ["Decision", "All", "The authority accepts or sends the case back to the committee with reasons", "45 days after the recommendation (105 days from the final EIA); if it disagrees it must say so within the same 45 days"],
                ["If the authority is silent", "All", "Paragraph 8(iii): the applicant may proceed as if the clearance were granted or denied in line with the committee&rsquo;s final recommendation", "After the period lapses"],
                ["Validity of the clearance", "Granted projects", "Ten years for most projects (13 river valley, 15 nuclear), extendable by 1, 2 and 5 years; mining for the mine-plan life up to 30 years, extendable by 20", "S.O. 1807(E), 12 April 2022; confirmed in the Ministry memorandum of 13 December 2022"]],
               "Show the stage-by-stage table")
means2 = "The notification caps the official review at 105 days after the final EIA report and lets the applicant proceed if the authority is silent, but it sets no limit on the time spent preparing the study."
todo2 = "Companies should plan the schedule from the date of the final EIA report and track each query on PARIVESH, because the statutory clock covers the review and not the preparation."
s2 = insight(f"The clock: up to {c.TOTAL_AFTER_FINAL_EIA} days from the final EIA report to a decision", chart2 + tbl2, means2, todo2, "clock")

# ---------------------------------------------------------------- section 3: NABET
rows3 = [("Category A, certificate current", c.A_OK), ("Category A, validity date passed", c.A_LAPSED),
         ("Category B, certificate current", c.B_OK), ("Category B, validity date passed", c.B_LAPSED)]
chart3 = bars(f"{len(c.A)} of {c.N} accredited EIA consultant organisations are category A", rows3,
              accent="Category A, certificate current", unit=" organisations", vmax=230, from_zero=True,
              sub="Organisations on the NABET portal list, fetched 27 November 2026. &lsquo;Validity date passed&rsquo; means the certificate date, and any extension-letter date, was before 27 November 2026.",
              source="NABET EIA portal, Accredited EIA Consultant Organisations (eia.nabet.qci.org.in); the page&rsquo;s own &lsquo;as on&rsquo; date was blank. Counts by this blog from the list; the list is saved with this piece.")
tbl3 = numbers(["Point", "What the sources say", "Source"],
               [["Who must prepare the EIA", "Only consultant organisations accredited by the Quality Council of India (QCI) or its NABET board for the sector and category of the project may prepare the EIA report and environment management plan and appear before the EAC or SEAC", "EIA Notification para 13, inserted by S.O. 648(E) of 3 March 2016"],
                ["Minor minerals", "Form 1M, pre-feasibility report and mine plan for B2 minor-mineral projects may come from a registered qualified person or an accredited consultant; the EIA and plan for A and B1 must be from an accredited consultant", "Notification, minor-mineral section"],
                ["Two categories", "An organisation scoring at least 60% at the office assessment may take category A and B projects; one scoring above 40% but below 60% is category B and takes B projects only", "NABET FAQs"],
                ["Sector scope", "Accreditation is per sector, tied to approved EIA coordinators; a category A organisation with only a category B coordinator in a sector can take only B projects in that sector", "NABET scheme, section 7.5"],
                ["Duration", "Three years, with a surveillance assessment after 18 months and re-accreditation after three years", "NABET EIA scheme page"],
                ["What the list shows", "Each entry gives the certificate number, validity date, category and the sectors covered; some carry remarks such as &lsquo;Conditions apply&rsquo;", "NABET portal list"]],
               "Show the rules and where they come from")
means3 = f"Only a consultancy accredited for the project&rsquo;s sector and category can write the EIA that the committee will take up, and while {len(c.A)} of {c.N} listed organisations are category A, accreditation is sector by sector and {c.LAPSED} entries show a validity date already passed."
todo3 = "Companies should check the consultant&rsquo;s sector, category and validity date on the NABET portal on the day they sign, and again before the EIA is filed, because an expired certificate can stall an appraisal."
s3 = insight(f"NABET: {len(c.A)} of {c.N} listed EIA consultancies are category A, sector by sector", chart3 + tbl3, means3, todo3, "nabet")

# ---------------------------------------------------------------- section 4: approval finders
rows4 = [("Central approvals listed on NSWS", c.NSWS_CENTRAL), ("State approvals listed on NSWS", c.NSWS_STATE)]
chart4 = bars(f"NSWS lists {c.NSWS_CENTRAL} central and {c.NSWS_STATE:,} State approvals, {c.RATIO_STATE_TO_CENTRAL} State approvals for each central one", rows4,
              accent="State approvals listed on NSWS", unit=" approvals", vmax=2600, from_zero=True,
              sub="Approvals available on the National Single Window System, as the portal&rsquo;s home page states them. Know Your Approvals guides across 32 central departments and 35 States.",
              source="nsws.gov.in home page and About page, read 27 November 2026; the ratio is this blog&rsquo;s division.")
tbl4 = numbers(["Tool", "What you give it", "What it returns", "Weight"],
               [["NSWS: Know Your Approvals (nsws.gov.in)", "Answers to a questionnaire. The central part has four sections: business registration, business activity, foreign investment and project land. The State part has three: utility requirement, business-related and sector-specific questions", "A tailored list of central and State approvals, saved to a dashboard where you can apply, pay and track", "Advisory only; the portal tells users to run their own assessment, and the final decision stays with each authority"],
                ["PARIVESH: Know Your Approval (parivesh.nic.in/kya)", "A project activity and sub-activity, the capacity or area, and a KML file of the site. A single point is turned into a 50-metre buffer", "A tentative list of clearances (EC, forest, wildlife, CRZ) for the location, with the associated documents, as a downloadable report", "Not for legal use; it relies on the map layers loaded so far. Mapping an EIA consultant in the tool is optional (the NABET rule for the EIA itself is separate); no e-KYC needed"],
                ["Maharashtra MAITRI: Investor Wizard", "Answers to a set of questions on the investment", "A list of State services that may be needed, with Apply and Track", "Guidance for Maharashtra only"],
                ["State EIA authorities (for example Tamil Nadu SEIAA)", "A PARIVESH account; the State site links to PARIVESH to apply and to track", "Status of State-level proposals and the minutes of committee meetings", "State authority sites point back to the same single window"]],
               "Show how the tools compare")
means4 = "The finders cover different ground, with NSWS answering which licences a business needs across ministries and States and the PARIVESH tool answering which environmental, forest, wildlife and coastal clearances a particular site needs, and each says its result is guidance only."
todo4 = "A company should run NSWS for the full list of approvals, then the PARIVESH tool with the site boundary for the clearances, and treat both results as a starting checklist to confirm with the Schedule."
s4 = insight(f"Finding the approvals: NSWS asks about the business, PARIVESH asks for a map", chart4 + tbl4, means4, todo4, "finders")

# ---------------------------------------------------------------- section 5: outcomes
rows5 = [("Proposals filed (2022 to 2026)", c.FILED), ("Auto-delisted", c.AUTO_DELISTED), ("Still in the pipeline", c.PIPELINE),
         ("Reached a decision", c.DECIDED), ("Clearance granted", c.GRANTED)]
chart5 = bars(f"{c.GRANT_RATE_DECIDED}% of decided proposals were granted; 22% of filings were auto-delisted", rows5,
              accent="Clearance granted", unit=" proposals", vmax=120000, from_zero=True,
              sub="Environmental-clearance proposals on PARIVESH 2.0, current-state snapshot. A proposal counted as granted has already passed the terms-of-reference and appraisal stages.",
              source="PARIVESH 2.0 open API (advanceSearchData), analysed in this blog&rsquo;s earlier piece on the approval funnel; figures repeated here, not recomputed.")
means5 = f"Once a proposal reaches a decision it is almost always granted ({c.GRANT_RATE_DECIDED}% of {c.DECIDED:,}), so the risk for a company lies in an application that lapses or waits and not in a rejection."
todo5 = "Companies should answer queries inside the portal&rsquo;s time limits and watch for delisting notices, because an auto-delisted application starts again from the beginning."
s5 = insight("After filing: rejection is rare, delay and delisting are the risk", chart5, means5, todo5, "outcomes")

steps = '''<section class="xv-sec"><h2 class="gb-h2" id="steps">The path a company follows on PARIVESH</h2>
<ol>
<li><b>Check the Schedule and the site.</b> Find the activity and its threshold, apply the General Condition to the coordinates, and run the PARIVESH Know Your Approval tool with a KML file.</li>
<li><b>Register.</b> The PARIVESH steps are Know Your Approval (optional), e-KYC (mandatory, with a PAN), a Common Application Form and the clearance-specific form.</li>
<li><b>Engage a NABET-accredited consultant</b> for the sector and category, and file Form 1 with the pre-feasibility report. Construction projects add Form 1A and a conceptual plan, and minor minerals up to 5 ha use Form 1M.</li>
<li><b>Get the terms of reference</b> (category A and B1). The committee, or the standard ToR route, sets what the EIA must cover.</li>
<li><b>Prepare the draft EIA and request a hearing</b> from the State pollution board, with at least 10 hard copies and the summary in English and the local language. The board gives at least 30 days&rsquo; notice.</li>
<li><b>File the final EIA</b> with the answers to the hearing, and Part C of the form. Under the 2022 PARIVESH form structure, Part A and Part B entered at the ToR stage can be edited if the detailed studies change them.</li>
<li><b>Appraisal and decision</b> by the EAC (category A, Ministry) or the SEAC (category B, SEIAA).</li>
<li><b>After the grant:</b> forms exist for a corrigendum (Form 2), amendment of ToR or clearance (Forms 3 and 4), extension of validity (Form 6) and transfer (Forms 7 and 8). Compliance reporting runs on the same portal.</li>
</ol>
<p>Clearances from other bodies are not needed before an application is received, screened, scoped, appraised or decided, unless the sequence depends on one in law (para 8(v)). Forest, wildlife and coastal clearances have their own paths; see this blog&rsquo;s article on them.</p></section>
'''

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>NABET:</b> print an &lsquo;as on&rsquo; date on the accredited list and mark entries whose certificate or extension date has passed, so that a company can tell a lapsed entry from a current one without opening each certificate.</li>
<li><b>MoEFCC:</b> publish the median days each stage takes on PARIVESH, by category and by State, beside the statutory limits, so that planning does not depend on anecdote.</li>
<li><b>NSWS and PARIVESH:</b> let the NSWS questionnaire hand its project details to the PARIVESH Know Your Approval tool, so that a company enters the site and capacity once.</li>
<li><b>The Ministry:</b> publish a consolidated EIA Notification that states in the text, not only in footnotes, which clauses are suspended or under appeal.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Rules and limits are read from the EIA Notification 2006 (S.O. 1533(E), 14 September 2006) in the consolidated text hosted on PARIVESH, marked as on 13 July 2026, with the Schedule rows quoted from that text. Amendments cited by their S.O. numbers are those footnoted in it.</li>
<li>Counts of accredited consultancies come from one fetch of the NABET portal list on 27 November 2026. The list is saved with this piece (names, certificate numbers, category and dates only). A certificate counts as current if its validity date, or its extension-letter date, was on or after 27 November 2026.</li>
<li>The funnel figures are from the PARIVESH 2.0 register as analysed in this blog&rsquo;s earlier article, not recomputed here.</li>
<li>The NSWS counts are the portal&rsquo;s own statements on its pages; the ratio is a division of those two numbers.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>How long clearances take in practice. The notification gives limits, and the PARIVESH register could be used to measure elapsed days by stage, but that was not done here.</li>
<li>How a query returned to the applicant, or a postponed hearing, affects the statutory clock: the paragraphs read give the limits but not the stop-and-restart rules.</li>
<li>The time and cost of preparing an EIA, including baseline data, and the fees for the application, the consultant or the hearing. None is in the notification.</li>
<li>Whether the NSWS questionnaire lists the environmental clearance among its results for a given project. The NSWS pages read were its user guides, FAQs and home page, not a run of the live questionnaire, so the NSWS row above describes its inputs and stated purpose only.</li>
<li>Which clauses of the notification are suspended. The consolidated text marks some 2016 amendments (S.O. 141(E)) as suspended by the National Green Tribunal on 11 December 2018 and under appeal in the Supreme Court; which obligations that changes today was not worked out.</li>
<li>The exact Schedule boundary cases (for example a distillery at exactly 100 KLD), because the symbols did not survive text extraction.</li>
<li>Whether the 27 NABET entries with a passed validity date are awaiting renewal, and the portal&rsquo;s own &lsquo;as on&rsquo; date, which was blank in the fetched page.</li>
<li>Consents under the Water and Air Acts from the State pollution board, building permissions and other licences that sit outside the environmental clearance. A commercial summary site was used only to cross-check the stage timings and is not cited for any figure.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + s5 + steps + fixes + method + gaps

SOURCES = (
    'Primary (opened): <a href="https://parivesh.nic.in/publicdocument/UPLOAD_OM_NOTIFICATION/IA_DOCS/1018_23072026010355.pdf">EIA Notification 2006, consolidated text as on 13 July 2026 (PARIVESH)</a>; '
    '<a href="https://parivesh.nic.in/publicdocument/UPLOAD_OM_NOTIFICATION/IA_DOCS/1001_16072026094223.pdf">S.O. 3862(E), 13 July 2026</a>; '
    '<a href="https://parivesh.nic.in/publicdocument/UPLOAD_OM_NOTIFICATION/IA_DOCS/1002_03032025121113.pdf">Ministry office memorandum, 28 February 2025</a> (State bodies not constituted); '
    '<a href="https://dste.py.gov.in/SEIAA/pdf/OM/C86.pdf">Ministry memorandum on validity of clearances, 13 December 2022</a>; '
    '<a href="https://environmentclearance.nic.in/report/downloadForm.html">PARIVESH forms list</a>; '
    '<a href="https://cpc.parivesh.nic.in/writereaddata/ENV/Environment_Clearance_FAQ.pdf">PARIVESH environmental clearance FAQ</a>; '
    '<a href="https://cpc.parivesh.nic.in/writereaddata/ENV/Know_Your_Approval_FAQ.pdf">PARIVESH Know Your Approval FAQ</a> and <a href="https://parivesh.nic.in/kya">the tool</a>; '
    '<a href="https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1911130">PIB, 27 March 2023</a> (PARIVESH). '
    '</p><p class="gb-note" style="margin:.6rem 0 0">NABET: <a href="https://nabet.qci.org.in/eia-scheme">EIA accreditation scheme page and FAQs</a>; <a href="https://nabet.qci.org.in/wp-content/uploads/2026/07/NABET-EIA-Scheme.pdf">Scheme for Accreditation of EIA Consultant Organizations, version 3</a>; '
    '<a href="https://eia.nabet.qci.org.in/Accredited_EIA_Consultant.aspx">the accredited list</a> (fetched 27 November 2026). '
    '</p><p class="gb-note" style="margin:.6rem 0 0">Approval finders: <a href="https://www.nsws.gov.in/about-us">NSWS About page</a>, <a href="https://www.nsws.gov.in/">home page</a> and <a href="https://www.ppe.nsws.gov.in/faqs">FAQs</a>; '
    '<a href="https://www.nsws.gov.in/s3fs/2021-11/NSWS_Investor_Guide_v3.3.pdf">NSWS investor guide</a>; <a href="https://maitri.maharashtra.gov.in/wp-content/uploads/2024/12/User-Manual_MAITRI-Single-Window-System.pdf">Maharashtra MAITRI user manual</a>; '
    '<a href="http://www.seiaa.tn.gov.in/">Tamil Nadu SEIAA</a>. Researched 27 November 2026. Figures from this blog&rsquo;s PARIVESH analysis are repeated from the earlier article linked below.')

RELATED = [
    (f"{B}/2026/07/india-ec-approval-funnel-parivesh-20.html", "Environmental clearances on PARIVESH 2.0: 88.7% of decided proposals approved"),
    (f"{B}/2026/07/india-forest-wildlife-crz-clearances.html", "India's forest, wildlife and coastal clearances: 1.05 million ha in the PARIVESH pipeline"),
    (f"{B}/2026/07/india-environmental-clearances-state.html", "Environmental clearances in India by state and sub-sector: an early investment signal"),
    (f"{B}/2026/10/how-to-use-india-ec-subsector-analysis.html", "How to use india-ec-subsector-analysis: see which states lead each Environmental Clearance"),
    (f"{B}/2026/11/eight-open-source-tools-for-tracking.html", "Indian government records: 8 open-source tools for gazette, Parliament and clearances"),
    (f"{B}/2026/08/not-drop-out-ethanols-zero-liquid.html", "Ethanol distilleries: zero-liquid-discharge rule and the treatment-capacity gap"),
]

build("Policy &middot; Environment", TITLE,
      "How a project gets environmental clearance in India: the category that decides between the Ministry and the State authority, the 105-day clock, the NABET consultant rule, and what the NSWS and PARIVESH approval finders can and cannot tell a company.",
      body, SOURCES, RELATED, str(OUT))
assert "masaladeutsch" not in OUT.read_text().lower()
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
