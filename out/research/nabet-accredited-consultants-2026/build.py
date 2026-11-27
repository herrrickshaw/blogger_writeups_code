"""NABET-accredited EIA consultants: who is on the list, where, in which sectors, how many renew soon, and what audits and courts have said.
Build from the repo root:  python3 out/research/nabet-accredited-consultants-2026/build.py   (writes out/post-nabet-accredited-eia-consultants-register.html)
Arithmetic lives in calc.py beside this file and is asserted there; this file re-asserts what it prints. Researched 27 November 2026.
Opened and read: the NABET portal list (fetched 27 Nov 2026), NABET's 'List of ACOs' PDFs of 14 Feb and 9 May 2022, the NABET EIA scheme (version 3) and FAQs,
the EIA Notification as consolidated on PARIVESH, CAG Report 39 of 2016 (chapter 2), India Together (2013), Mint (2010), two Delhi High Court judgments (7 Nov 2013),
the NGT case note and order of 27 May 2026. Search excerpts only (not opened in full): an NGT appeal rejoinder of Sep 2026 that quotes an audit report."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402
import calc as c  # noqa: E402  (importing runs the asserts)

OUT = ROOT / "out/post-nabet-accredited-eia-consultants-register.html"
B = "https://blog.vertistratsolution.com"
TITLE = f"NABET-accredited EIA consultants: {c.N} listed, {c.DUE_SHARE}% lapsed or due for renewal within a year"
assert 55 <= len(TITLE) <= 90, len(TITLE)
assert (c.N, c.DUE, c.DUE_SHARE, c.GROWTH) == (256, 109, 43, 41)

top = top_line([
    (f"{c.N}", f" organisations are on the NABET portal&rsquo;s accredited list (27 November 2026), up {c.GROWTH}% from {len(c.feb22)} in February 2022. Of those {len(c.feb22)}, {c.STAYED} are still listed, {c.GONE} are not, and {c.NEW} on today&rsquo;s list were not there then."),
    (f"{c.DUE}", f" of the {c.N} ({c.DUE_SHARE}%) show a validity date that has passed ({c.LAPSED}) or falls by 27 November 2027 ({c.SOON}), counting any extension letter."),
    ("4", f" organisations are accredited for nuclear power and fuel processing, 6 each for soda ash and ship breaking, and 2 for aerial ropeways, against {c.tot['38']} for building and construction. Accreditation is sector by sector, so the choice in a thin sector is a handful."),
])

# ---------------------------------------------------------------- s0: how accreditation became a condition
chart0 = flow([
    ("August 2007", "NABET, part of the Quality Council of India (QCI), launches a voluntary accreditation scheme for EIA consultant organisations."),
    ("2 December 2009", "A Ministry office memorandum says EIA and EMP reports from consultants not registered with QCI or NABET will not be considered after 30 June 2010 (as recited by the Delhi High Court and by CAG)."),
    ("June and November 2010", "Memoranda let 157 and then 265 applicants appear before the committees while their applications were pending (as recited by the Delhi High Court)."),
    ("30 June and 30 September 2011", "The Ministry issues the final scheme memoranda. NABET&rsquo;s own history dates version 3 of the scheme to June 2015."),
    ("5 October 2011", "The Ministry makes the project proponent answerable for an EIA&rsquo;s contents after finding data copied from other reports (as quoted by India Together)."),
    ("3 March 2016", "S.O. 648(E) inserts para 13 into the EIA Notification: only organisations accredited for the sector and category may prepare the EIA and EMP and appear before the EAC or SEAC.", True),
    ("10 March 2017", "CAG Report 39 of 2016 is tabled. It finds EIAs prepared by consultants not registered for the activity in a sample of clearances granted 2011 to July 2015."),
    ("27 May 2026", "The National Green Tribunal dismisses an application asking for disciplinary action against an accredited consultant, holding the grievance outside its jurisdiction (Original Application 137 of 2026)."),
])
means0 = "Accreditation moved from a voluntary scheme in 2007 to a ministry memorandum in 2009 and to a rule in the EIA Notification in 2016, but the enforcement record in this article runs through audits and complaints, not through published sanctions."
todo0 = "Applicants should treat accreditation as a legal condition of the EIA and verify it themselves, because the audit and tribunal record below shows the check was not always made."
s0 = insight("How it became a condition: voluntary in 2007, a memorandum in 2009, a rule in 2016", chart0, means0, todo0, "history")

# ---------------------------------------------------------------- s1: growth and turnover
rows1 = [(a, b) for a, b in c.SERIES]
chart1 = bars(f"The accredited list grew from {len(c.feb22)} in February 2022 to {c.N} in November 2026", rows1,
              accent="27 Nov 2026, NABET portal", unit=" organisations", vmax=280, from_zero=True,
              sub="Organisations on each list. The lists are not strictly alike: the 2013 and 2015 figures are as printed in an article and in the scheme text, the 2022 lists are NABET&rsquo;s own PDFs, and 2026 is the portal page.",
              source="India Together (25 September 2013); NABET EIA scheme, version 3 (about 170); NABET &lsquo;List of ACOs&rsquo; Rev. 19 (14 February 2022) and Rev. 23 (9 May 2022); NABET portal (27 November 2026). Counts for 2022 and 2026 by this blog.")
vint = [[str(y), str(c.VINT[y])] for y in range(2010, 2027) if c.VINT.get(y)]
tbl1 = numbers(["Item", "Count"], [["On the list 14 February 2022", str(len(c.feb22))], ["Still on the list 27 November 2026 (matched by NABET organisation code)", str(c.STAYED)],
                                  ["On the 2022 list, not on the 2026 list", str(c.GONE)], ["On the 2026 list, not on the 2022 list", str(c.NEW)],
                                  ["2026 entries with no organisation code shown", "2"]], "Show the turnover since February 2022") + numbers(
    ["Year of first accreditation", "Organisations on the 2026 list"], vint, "Show first-accreditation years")
means1 = f"The list grew {c.GROWTH}% in under five years because {c.NEW} organisations joined while {c.GONE} dropped off, so {c.NEW_SHARE}% of today&rsquo;s coded entries are new since February 2022 and {c.SINCE_2021} of the {c.N} were first accredited in 2021 or later."
todo1 = "A buyer should ask how many EIAs a young organisation has completed in the sector, because the scheme examines at least two of an organisation&rsquo;s reports at each assessment and a new entrant has had fewer."
s1 = insight(f"Growth: the list is {c.GROWTH}% longer than in February 2022, with {c.NEW} new organisations", chart1 + tbl1, means1, todo1, "growth")

# ---------------------------------------------------------------- s2: states
top8 = c.ST.most_common(8)
rows2 = [(k, v) for k, v in top8] + [(f"Other {c.N_STATES - 8} States and Union Territories", c.OTHER_STATES)]
chart2 = bars(f"Six States hold {c.TOP6} of the {c.N} registered addresses; Maharashtra has {c.ST['Maharashtra']}", rows2,
              accent="Maharashtra", unit=" organisations", vmax=70, from_zero=True,
              sub="Organisations by the State in the registered address on the NABET list. This is where an organisation is registered, not where it works.",
              source="NABET portal (27 November 2026); State parsed from each address by this blog, with twelve addresses assigned by hand from the town named.")
tbl2 = numbers(["State or Union Territory", "Organisations"], [[k, str(v)] for k, v in c.ST.most_common()], "Show all States")
means2 = f"Maharashtra, Gujarat and Uttar Pradesh together hold {c.TOP3} registered addresses ({round(100 * c.TOP3 / c.N)}%) and six States hold {round(100 * c.TOP6 / c.N)}%, while Odisha, Jharkhand and Chhattisgarh, where mining projects cluster, hold {c.MINING3} ({round(100 * c.MINING3 / c.N, 1)}%)."
todo2 = "Project proponents in mining States should ask where the consultant&rsquo;s field team and laboratory are, since the registered address does not show where the baseline data will be collected."
s2 = insight(f"Where: six States hold {round(100 * c.TOP6 / c.N)}% of the registered addresses", chart2 + tbl2, means2, todo2, "states")

# ---------------------------------------------------------------- s3: sectors
sec_rows = [("Building and construction (B projects only)", c.tot["38"]), ("Mining of minerals", c.tot["1"]), ("Thermal power plants", c.tot["4"]),
            ("Integrated paint industry", c.tot["23"]), ("Leather and hide processing", c.tot["15"]), ("Soda ash", c.tot["14"]), ("Ship breaking yards", c.tot["30"]),
            ("Nuclear power and fuel processing", c.tot["5"]), ("Aerial ropeways", c.tot["35"])]
chart3 = bars(f"Accredited organisations by sector run from {c.tot['38']} for construction to 4 for nuclear power", sec_rows,
              accent=["Nuclear power and fuel processing", "Aerial ropeways", "Soda ash", "Ship breaking yards", "Leather and hide processing"], unit=" organisations", vmax=220, from_zero=True,
              sub="Organisations whose scope on the NABET list includes the sector. Nine of the 41 sector codes are shown: the three most covered and six of the thinnest.",
              source="NABET portal (27 November 2026), scope tables; counts by this blog. Sector 26 was deleted from the scheme, and 255 of the 256 entries show sector lines.")
allsec = []
for k in sorted(c.tot, key=lambda x: (int(__import__("re").match(r"\d+", x).group(0)), x)):
    nm = c.names[k].split("(")[0].strip()
    allsec.append([k, nm[:70], str(c.tot[k]), str(c.a_cap[k])])
tbl3 = numbers(["Sector no.", "Sector", "Organisations", "of which category A for the sector"], allsec, "Show all 41 sector codes")
means3 = f"Each organisation is accredited sector by sector (median {int(c.MEDIAN_SECTORS)}, up to {c.MAX_SECTORS}, with {c.FEW} listing three or fewer and {c.MANY} listing ten or more), so a nuclear-power, ship-breaking or soda-ash project has between 4 and 6 accredited organisations to choose from."
todo3 = "A proponent in a thin sector should confirm the organisation&rsquo;s approved EIA coordinator for that exact sector and category on the portal before signing, because losing that one expert can cancel the sector."
s3 = insight("Sectors: 4 organisations for nuclear power, 6 each for soda ash and ship breaking", chart3 + tbl3, means3, todo3, "sectors")

# ---------------------------------------------------------------- s4: renewals
rows4 = [("Validity date already passed", c.LAPSED)] + [(a, b) for a, b in c.QUARTERS] + [("Beyond 27 November 2027", c.BEYOND)]
chart4 = bars(f"{c.DUE} of {c.N} certificates have lapsed or fall due within a year; {c.BEYOND} run longer", rows4,
              accent=["Validity date already passed"], unit=" organisations", vmax=160, from_zero=True,
              sub="Organisations by the later of the certificate date and any extension-letter date, counted from 27 November 2026. Ten entries carry an extension letter.",
              source="NABET portal (27 November 2026); the page&rsquo;s own &lsquo;as on&rsquo; date was blank. Grouping by this blog.")
means4 = f"Accreditation lasts three years with a surveillance assessment at 18 months, so {c.DUE} organisations ({c.DUE_SHARE}%) are lapsed or due for renewal inside the next year, and {c.LAPSED} of those already show a passed date with no valid extension letter."
todo4 = "Anyone relying on an organisation should record the validity date on the day they sign and recheck the portal before the EIA is filed, because the scheme can move an organisation to a non-accredited list if a shortfall is not met within 90 days."
s4 = insight(f"Renewals: {c.DUE} of {c.N} certificates have lapsed or fall due within a year", chart4, means4, todo4, "renewals")

# ---------------------------------------------------------------- s5: audit and tribunal record
rows5 = [(f"{k} ({a} of {b} projects)", a) for k, (a, b) in c.CAG.items()]
chart5 = bars(f"CAG: the consultant was not registered for the activity in {c.CAG_NOT} of {c.CAG_CASES} projects", rows5,
              accent=[f"River valley and hydro (5 of 7 projects)"], unit=" projects", vmax=16, from_zero=True,
              sub="Projects in the CAG sample where the EIA was prepared by a consultant not registered with NABET for that project activity. The audit sampled files for projects cleared 2011 to July 2015.",
              source="CAG Report 39 of 2016, chapter 2, para 2.12 and Table 2.8 (216 files of 249 sampled from 2,917 projects granted EC); counts by this blog from the table.")
tbl5 = numbers(["Group in the CAG sample", "Cases", "What the audit recorded"],
               [["Coal mining", "39", "17 not applicable or expansion; 5 provisionally accredited or in process; 1 EIA not in the scanned file; 10 could not be ascertained"],
                ["Industry", "34", "Consultant said to be accredited but certificate not attached in 27"],
                ["Non-coal mining", "37", "5 provisional, in process or waitlisted; certificate not attached in 3; EIA silent on accreditation in 11"],
                ["Construction", "20", "Not applicable: ToR and EIA are not prepared"],
                ["Infrastructure", "38", "13 not registered for the activity; 9 said they were, certificates not attached"],
                ["River valley and hydro-electric", "7", "5 not registered for the activity"],
                ["Thermal power", "41", "10 not registered for the activity"]], "Show the audit table") + numbers(
    ["Source", "What it says", "Date"],
    [["NABET scheme, clause 9.3", "NABET may suspend, cancel or debar an organisation for false or misleading information, unapproved expert changes, breach of the code of conduct and other grounds; a complaint or a finding by a court, the NGT or a statutory body can trigger action; the accreditation committee decides", "Scheme version 3"],
     ["NABET FAQs", "Complaints can be lodged with the NABET CEO; an organisation that does not meet an assessment shortfall within 90 days moves to a second list, then to the non-accredited list", "NABET FAQ document"],
     ["India Together (Kanchi Kohli)", "QCI is backed by three industry associations, project developers fund EIAs, and several listed organisations had a history of shoddy reports (an opinion piece, 2013)", "25 September 2013"],
     ["Mint", "Reported consultants passing off EIAs of projects in the US and Russia as Indian ones; the Ministry said it would stop accepting reports from unaccredited consultants after June 2010", "7 January 2010"],
     ["National Green Tribunal, OA 137 of 2026", "An applicant sought an inquiry and NABET proceedings under clause 9.3 against an accredited consultant; the Tribunal held the matter outside its jurisdiction and dismissed it. The Tribunal made no finding on the allegations", "27 May 2026"],
     ["NABET, &lsquo;Reflections&rsquo;", "At least two EIA reports by an organisation are scrutinised by assessors, on a 9-point quality criteria list", "undated NABET document"]],
    "Show other sources on enforcement and quality")
means5 = f"A CAG audit tabled in March 2017, covering clearances granted before the 2016 rule, found {c.CAG_NOT} of {c.CAG_CASES} projects in three sectors with a consultant not registered for the activity, and the sources found here record complaints and an appeal for action but no published list of suspended or debarred organisations."
todo5 = "NABET and the Ministry should publish suspensions, cancellations and debarments with their reasons and dates, so that the scheme&rsquo;s own enforcement powers can be checked from outside."
s5 = insight(f"The record: CAG found {c.CAG_NOT} of {c.CAG_CASES} projects with a consultant not registered", chart5 + tbl5, means5, todo5, "record")

steps = '''<section class="xv-sec"><h2 class="gb-h2" id="check">How to check a consultant on the portal</h2>
<ol>
<li><b>Find the organisation</b> on the NABET portal list and note its certificate number, category and validity date. Check any extension-letter date too.</li>
<li><b>Match the sector.</b> The scope table lists the sectors it covers and the Schedule item for each. The organisation must be accredited for your sector and for your project&rsquo;s category.</li>
<li><b>Read the category marks.</b> Category A organisations can take category A and B projects. Where a sector shows A followed by a star, the expert qualified for category A but the organisation as a whole scored under 60%, so it cannot take category A projects in that sector.</li>
<li><b>Read the remarks</b> (for example &lsquo;Conditions apply&rsquo;) and the Human Resource link, which shows the approved EIA coordinator and experts.</li>
<li><b>Ask for the organisation&rsquo;s accreditation certificate</b> and attach the sector and category to the application. A complaint about an organisation can go to the NABET CEO.</li>
</ol></section>
'''

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>NABET:</b> print an &lsquo;as on&rsquo; date on the list, flag entries whose validity date has passed, and publish a dated list of suspensions, cancellations and debarments with reasons.</li>
<li><b>MoEFCC:</b> require the EIA Notification&rsquo;s accreditation check to be made on PARIVESH, by matching the consultant, sector and category against NABET&rsquo;s list when an application is filed, which the CAG audit found was not always done on paper.</li>
<li><b>NABET:</b> publish, per organisation and sector, the number of EIAs submitted and the outcome of appraisal, so that experience is visible and not only accreditation.</li>
<li><b>The Ministry:</b> state where a complaint against an accredited consultant should go, given that the NGT held in 2026 that its own jurisdiction did not cover one.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The register counts come from one fetch of the NABET portal page &lsquo;Accredited EIA Consultant Organisations&rsquo; on 27 November 2026. Names, certificate numbers, States, categories, dates and sector scopes are saved with this piece; contact details are not.</li>
<li>State is the State named in each organisation&rsquo;s registered address, read by this blog (twelve addresses were assigned by hand from the town named). It is not where the organisation works.</li>
<li>Sector counts are the number of organisations whose scope table lists the sector. The &lsquo;category A for the sector&rsquo; column counts entries marked A without a star.</li>
<li>Effective validity is the later of the certificate date and any extension-letter date. &lsquo;Lapsed&rsquo; means that date was before 27 November 2026.</li>
<li>Turnover since 2022 matches NABET organisation codes between the 14 February 2022 list and the 2026 list; two 2026 entries show no code and are left out of the match.</li>
<li>Audit figures are the CAG&rsquo;s counts in Table 2.8; the 28 of 86 sums the three sectors where the audit states a count of consultants not registered for the activity, and does not cover the other four groups.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>Whether the lapsed or soon-expiring entries have renewals in progress. The portal page&rsquo;s own &lsquo;as on&rsquo; date was blank, so how current the list is was not established.</li>
<li>Whether the 2013 and 2015 counts match the 2022 and 2026 lists in definition. They come from an article and the scheme text, and are shown as given.</li>
<li>Where organisations actually work. Registered addresses are a rough proxy, and one organisation may serve several States.</li>
<li>How many organisations, if any, have been suspended, cancelled or debarred. No published list was found, and absence from the list is not evidence that none was taken.</li>
<li>How many EIAs each organisation has prepared, or how appraisal committees rated them. The portal does not show it.</li>
<li>The merits of any complaint. The 2026 Tribunal order dismissed an application on jurisdiction and made no finding on the allegations; no organisation is named here for that reason.</li>
<li>Whether accreditation has improved EIA quality. The CAG audit predates the 2016 rule and covers files from 2011 to 2015; no later audit of the same kind was found.</li>
<li>An NGT appeal rejoinder of September 2026 quotes an audit as observing 21 approvals where the consultant was non-accredited or not accredited for the sector. Only a search excerpt was seen, the audit it quotes was not identified, and it is not used here.</li>
<li>One organisation (entry 128) shows no sector lines on the portal page, and two show no organisation code.</li>
</ul></details>
'''

body = STYLE + top + s0 + s1 + s2 + s3 + s4 + s5 + steps + fixes + method + gaps

SOURCES = (
    'Register (opened): <a href="https://eia.nabet.qci.org.in/Accredited_EIA_Consultant.aspx">NABET portal, Accredited EIA Consultant Organisations</a> (fetched 27 November 2026); '
    '<a href="https://nabet.qci.org.in/allnews/Validity%20of%20ACOs%20-%20February%2014%202022.pdf">NABET list of ACOs, 14 February 2022</a> and <a href="https://nabet.qci.org.in/eiafile/Validity%20of%20ACOs%20-%20May%2009%202022.pdf">9 May 2022</a>; '
    '<a href="https://nabet.qci.org.in/wp-content/uploads/2026/07/NABET-EIA-Scheme.pdf">NABET Scheme for Accreditation of EIA Consultant Organizations</a>; <a href="https://nabet.qci.org.in/eia-scheme">NABET EIA scheme page and FAQs</a>; '
    '<a href="https://nabet.qci.org.in/eiafile/Reflections.pdf">NABET, Reflections</a>. '
    '</p><p class="gb-note" style="margin:.6rem 0 0">Rules and audit: <a href="https://parivesh.nic.in/publicdocument/UPLOAD_OM_NOTIFICATION/IA_DOCS/1018_23072026010355.pdf">EIA Notification 2006, consolidated text as on 13 July 2026</a> (para 13, S.O. 648(E) of 3 March 2016); '
    '<a href="https://cag.gov.in/uploads/download_audit_report/2016/Chapter_2_Process_of_grant_of_Environment_Clearance_Union_Government_Report_39_of_2016.pdf">CAG Report 39 of 2016, chapter 2</a> and <a href="https://cag.gov.in/en/audit-report/details/27540">the report page</a> (tabled 10 March 2017). '
    '</p><p class="gb-note" style="margin:.6rem 0 0">Courts and press: <a href="https://www.greentribunal.gov.in/Ejournal/uploads/case_pdfs/case-2026-010_case_note.pdf">NGT case note, OA 137 of 2026</a> and <a href="https://www.greentribunal.gov.in/Ejournal/uploads/case_pdfs/case-2026-010_judgment.pdf">order of 27 May 2026</a>; '
    '<a href="https://voxjuris.org/judgment/dhc-dlhc011795772012-131107/rani-gupta-v-ministry-of-environment-and-forest-and-ors">Delhi High Court, 7 November 2013</a> (history of the memoranda); '
    '<a href="https://indiatogether.org/eiareport-environment">India Together, 25 September 2013</a> (opinion); <a href="https://www.livemint.com/Home-Page/TOpzFYjFqt6QKbCmujwoAM/Ministry-insists-on-accreditation-for-EIA-reports.html">Mint, 7 January 2010</a>. '
    'Researched 27 November 2026. Counts, groupings and the comparison of lists are this blog&rsquo;s work.')

RELATED = [
    (f"{B}/2026/07/india-ec-approval-funnel-parivesh-20.html", "Environmental clearances on PARIVESH 2.0: 88.7% of decided proposals approved"),
    (f"{B}/2026/07/india-forest-wildlife-crz-clearances.html", "India's forest, wildlife and coastal clearances: 1.05 million ha in the PARIVESH pipeline"),
    (f"{B}/2026/07/india-environmental-clearances-state.html", "Environmental clearances in India by state and sub-sector: an early investment signal"),
    (f"{B}/2026/10/how-to-use-india-ec-subsector-analysis.html", "How to use india-ec-subsector-analysis: see which states lead each Environmental Clearance"),
    (f"{B}/2026/11/eight-open-source-tools-for-tracking.html", "Indian government records: 8 open-source tools for gazette, Parliament and clearances"),
]

build("Policy &middot; Environment", TITLE,
      "Who is on the NABET list of accredited EIA consultants in November 2026: how it grew, where the organisations are registered, which sectors have few, how many certificates lapse within a year, and what a government audit and the courts have recorded.",
      body, SOURCES, RELATED, str(OUT))
assert "masaladeutsch" not in OUT.read_text().lower()
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
