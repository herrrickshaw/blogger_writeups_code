"""Karnataka Sakaala Services Act (Karnataka Act 1 of 2012): what it guarantees, how appeals and compensation work, the 2014 and 2026
amendments, the portal's cumulative counters, and other Karnataka service-delivery measures that have a dated source.
Build from the repo root:  python3 out/research/karnataka-sakaala-act-2026/build.py   (writes out/post-karnataka-sakaala-services-act.html)
Statute figures were read from the PRS compilation of the Act (principal Act, Act 31 of 2014, Act 39 of 2026), cross-checked against the
Karnataka Legislative Council copy of the 2026 Bill. Every other figure is from the source named beside it, or computed below with an assert.
Analysed 21 November 2026. The Schedule of notified services, the Sakala MIS report page and the October 2026 notification were not readable
from the build environment; the post says so."""
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-karnataka-sakaala-services-act.html"
B = "https://blog.vertistratsolution.com"
STEPS = 7


def step(n, what):
    el = time.time() - T0
    eta = el / n * (STEPS - n) if n else 0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {eta:.1f}s left)", flush=True)


# ---- 1. Statute (PRS compilation of the Act and its amendments). Days and rupees as written in the sections.
step(1, "statute figures and consistency checks")
REPLY_DAYS = 7            # section 11(2): public servant may represent within seven days of the notice
NOTICE_DAYS = 15          # section 11(1): notice within fifteen days of payment of compensatory cost
APPEAL1_DAYS = 30         # section 13(1): citizen's appeal to the competent officer, thirty days
APPEAL2_DAYS = 60         # section 13(3): appeal to the appellate authority, sixty days
SERVANT_APPEAL_DAYS = 30  # section 12(1): public servant's appeal against the competent officer's order
HRMS_DAYS = 30            # section 11(4), inserted 2014: debit note entered in HRMS within thirty days
RATE, CAP = 20, 500       # section 9: Rs 20 a day, at most Rs 500 an application
DAYS_TO_CAP = CAP / RATE
assert DAYS_TO_CAP == 25
assert APPEAL2_DAYS == 2 * APPEAL1_DAYS
assert REPLY_DAYS < NOTICE_DAYS < APPEAL1_DAYS < APPEAL2_DAYS
DEFAULTS_FOR_ACTION = 7   # section 14(4), inserted 2014: more than seven defaults -> enquiry; Government acts within one month

# 2026 slab reported by The Hindu (18 Oct 2026, excerpt only): Rs 20 a day for days 1-5 capped at Rs 100, up to Rs 100 a day for days 21-25, maximum Rs 1,500.
SLAB_FIRST_DAY, SLAB_FIRST_CAP, SLAB_LAST_DAY, SLAB_MAX = 20, 100, 100, 1500
assert SLAB_FIRST_DAY * 5 == SLAB_FIRST_CAP
# Consistency check on the reported figures (the middle bands are inferred, not reported): five bands of five days at 20, 40, 60, 80, 100 a day sum to the stated maximum.
assert sum(5 * r for r in (20, 40, 60, 80, 100)) == SLAB_MAX
assert SLAB_MAX == 3 * CAP

# ---- 2. Sakala portal home page counters (sakala.kar.nic.in/index.aspx, read 21 Nov 2026; the page prints no as-of date)
step(2, "portal counters and consistency checks")
RECEIPTS, DISPOSALS = 432_426_014, 431_632_443
DEPTS, SERVICES = 114, 1446
OPEN = RECEIPTS - DISPOSALS
assert OPEN == 793_571
DISPOSAL_PCT = 100 * DISPOSALS / RECEIPTS
assert f"{DISPOSAL_PCT:.2f}" == "99.82"
OPEN_PCT = 100 * OPEN / RECEIPTS
assert f"{OPEN_PCT:.2f}" == "0.18"
assert abs(DISPOSAL_PCT + OPEN_PCT - 100) < 1e-9
AVG_PER_SERVICE = RECEIPTS / SERVICES
assert round(AVG_PER_SERVICE) == 299_050         # simple average over notified services, not a per-year rate
M = 1e6
assert round(RECEIPTS / M, 2) == 432.43 and round(DISPOSALS / M, 2) == 431.63 and round(OPEN / M, 2) == 0.79
# an earlier, dated reading of scale (DARPG webinar report: 1,115 services as on 20 April 2022)
SERV_2022 = 1115
assert SERVICES - SERV_2022 == 331
assert round(100 * (SERVICES - SERV_2022) / SERV_2022, 1) == 29.7

TITLE = "Karnataka Sakaala Services Act: Rs 20 a day for delay, capped at Rs 500, amended 2026"
assert 55 <= len(TITLE) <= 90, len(TITLE)
for h in (TITLE,):
    assert not any(w in h.lower().split() for w in ("you", "your", "we", "our"))

step(3, "writing sections")
top = top_line([
    ("Rs 500", f" is the most an official owes per application under section 9: Rs {RATE} a day of delay, reached after {DAYS_TO_CAP:.0f} days, recovered from the official&rsquo;s salary after the citizen is paid."),
    (f"{DISPOSAL_PCT:.2f}%", f" of the {RECEIPTS:,} applications on the Sakala portal&rsquo;s home counter show a recorded disposal, leaving {OPEN:,} open; the page carries no date, and a disposal is not the same as an on-time service."),
    (f"{APPEAL1_DAYS} and {APPEAL2_DAYS} days", " are the windows for a citizen&rsquo;s first appeal to the competent officer and second appeal to the appellate authority."),
])

s1 = insight(
    f"A citizen has {APPEAL1_DAYS} days to appeal a rejection or delay, then {APPEAL2_DAYS} days to appeal again",
    bars(f"Citizens get {APPEAL1_DAYS} days for a first appeal and {APPEAL2_DAYS} for a second, both extendable",
         [("Public servant replies to a notice (section 11)", REPLY_DAYS),
          ("Notice issued after compensation is paid (section 11)", NOTICE_DAYS),
          ("Citizen&rsquo;s first appeal, to the competent officer (section 13)", APPEAL1_DAYS),
          ("Public servant&rsquo;s appeal against a recovery order (section 12)", SERVANT_APPEAL_DAYS),
          ("Debit note entered in the HRMS software, added 2014 (section 11)", HRMS_DAYS),
          ("Citizen&rsquo;s second appeal, to the appellate authority (section 13)", APPEAL2_DAYS)],
         accent=["Citizen&rsquo;s first appeal, to the competent officer (section 13)", "Citizen&rsquo;s second appeal, to the appellate authority (section 13)"],
         unit=" days", vmax=70,
         sub="Time limits written into the Act, in days. The competent officer and the appellate authority may admit a late appeal if the delay had sufficient cause.",
         source="Karnataka Sakaala Services Act, 2011 (Karnataka Act 1 of 2012) as amended in 2014 and 2026, PRS Legislative Research compilation.")
    + numbers(["Step", "Who acts", "Limit", "Section"],
              [["Application acknowledged; clock starts", "Designated officer", "Stipulated time in the Schedule", "5(1)"],
               ["Service given, or rejection with written reasons and appeal details", "Designated officer", "Within the stipulated time", "5(2)"],
               ["First appeal, for rejection or no service in time", "Citizen to competent officer", f"{APPEAL1_DAYS} days", "13(1)"],
               ["Second appeal against the competent officer", "Citizen or official to appellate authority", f"{APPEAL2_DAYS} days", "13(3)"],
               ["Direct application if the officer ignores an acknowledged application or an order", "Citizen to competent officer or appellate authority", "Decided as an appeal", "13(5), 13(6)"],
               ["Notice to the responsible public servant", "Competent officer", f"{NOTICE_DAYS} days from payment", "11(1)"],
               ["Reply to the notice", "Public servant", f"{REPLY_DAYS} days", "11(2)"],
               ["Appeal against the recovery order", "Public servant to appellate authority", f"{SERVANT_APPEAL_DAYS} days; the order is final", "12(1)"],
               ["Competent officer: at least Group B/C rank; appellate authority: at least Deputy Secretary", "Government appoints", "&ndash;", "10(1), 12(2)"]]),
    "Each missed deadline gives the citizen two rungs of appeal inside the administration, and the civil courts have no jurisdiction over matters those authorities decide (section 18).",
    "A citizen who is refused or kept waiting should keep the acknowledgement number, because the first appeal clock runs from the date of rejection or the end of the stipulated time.",
    "appeals")

s2 = insight(
    "Compensation is Rs 20 a day up to Rs 500; a reported 2026 slab raises the cap to Rs 1,500",
    bars("A reported slab for staff services triples the maximum from Rs 500 to Rs 1,500",
         [("Act, section 9 (principal Act, 2014 and 2026 text)", CAP),
          ("Slab reported by The Hindu, 18 Oct 2026 (secondary)", SLAB_MAX)],
         accent="Slab reported by The Hindu, 18 Oct 2026 (secondary)", unit="", fmt=lambda v: f"Rs {v:,.0f}", vmax=1600,
         sub="Maximum cumulative compensation per application, rupees. The slab was seen only in a partial excerpt; the notification was not read. A day-by-day slab of 20, 40, 60, 80 and 100 rupees in five-day bands would reach the reported maximum after 25 days, the same 25 days the Rs 20 rate takes to reach Rs 500.",
         source="Act text: PRS compilation and Karnataka Legislative Council copy of the 2026 Bill. Slab: The Hindu, 18 October 2026 (secondary). Arithmetic computed here.")
    + numbers(["Item", "Figure", "Basis"],
              [["Rate, section 9", f"Rs {RATE} a day", "Act text, unchanged since 2012"],
               ["Maximum, section 9", f"Rs {CAP} an application", "Act text; 2026 adds &lsquo;or such rate and maximum as the Schedule specifies&rsquo;"],
               ["Days of delay to reach the maximum", f"{DAYS_TO_CAP:.0f}", f"Computed: {CAP} / {RATE}"],
               ["Reported first band", f"Rs {SLAB_FIRST_DAY} a day, days 1 to 5, capped at Rs {SLAB_FIRST_CAP}", "The Hindu, 18 Oct 2026 (secondary, excerpt)"],
               ["Reported last band", f"Rs {SLAB_LAST_DAY} a day, days 21 to 25", "The Hindu, 18 Oct 2026 (secondary, excerpt)"],
               ["Reported maximum", f"Rs {SLAB_MAX:,}", "The Hindu, 18 Oct 2026 (secondary, excerpt)"],
               ["Who pays", "The responsible public servant, by salary debit after the citizen is paid", "Sections 10 and 11"],
               ["When it does not apply", "If the Government has banned or restricted providing the service", "Section 9"]]),
    f"The Act&rsquo;s own figure is Rs {RATE} a day to a Rs {CAP} maximum, but since the 2026 amendment the Schedule can set other rates, so the figure that applies to a given service depends on the Schedule entry.",
    "Karnataka&rsquo;s Department of Personnel and Administrative Reforms should publish the notified compensation rate beside each service in the Sakala service compendium.",
    "money")

s3 = insight(
    f"The Sakala counter shows {RECEIPTS/M:.1f} million applications, {OPEN_PCT:.2f}% without a disposal",
    bars("Sakala counts 432.43 million receipts and 431.63 million disposals, leaving 0.79 million",
         [("Cumulative receipts", round(RECEIPTS / M, 2)), ("Cumulative disposals", round(DISPOSALS / M, 2)),
          ("Receipts without a recorded disposal (computed)", round(OPEN / M, 2))],
         accent="Receipts without a recorded disposal (computed)", unit=" million", vmax=450,
         sub=f"Applications, millions, taken from a search-tool excerpt of the portal home page retrieved on 21 November 2026 (the page prints no as-of date). {DEPTS} departments and institutions, {SERVICES:,} services. A disposal can be a rejection or a delivery; the counter does not show timeliness.",
         source="Sakala portal home page, sakala.kar.nic.in; differences computed here.")
    + numbers(["Item", "Value", "Basis"],
              [["Cumulative receipts", f"{RECEIPTS:,}", "Portal home page"],
               ["Cumulative disposals", f"{DISPOSALS:,}", "Portal home page"],
               ["Without a recorded disposal", f"{OPEN:,}", "Computed; includes applications still inside their time limit"],
               ["Share with a recorded disposal", f"{DISPOSAL_PCT:.2f}%", "Computed"],
               ["Departments and institutions", f"{DEPTS}", "Portal home page"],
               ["Notified services", f"{SERVICES:,}", f"Portal home page; {SERV_2022:,} as on 20 April 2022 (DARPG report), a rise of {SERVICES-SERV_2022}, or {100*(SERVICES-SERV_2022)/SERV_2022:.1f}%"],
               ["Average receipts per notified service", f"{AVG_PER_SERVICE:,.0f}", "Computed; cumulative since the Act, not a yearly rate"]]),
    f"Nearly every application has a recorded outcome, but the counter has no date, no split between delivered and rejected and no count of applications decided late, so it cannot show how often the guarantee was kept.",
    "The portal should print the as-of date on each counter and publish monthly delivered-in-time, delivered-late, rejected and pending counts by department.",
    "practice")

s4 = insight(
    "Other Karnataka measures with a dated source: Praja Seva, land records, 2026 budget",
    flow([("Study dated 2024-25 (draft)", "A draft land-records study found 100% of villages and 100% of sub-registrar offices computerised, with 2.1 owners per record of rights on average."),
          ("6 Mar 2026 (budget, as reported)", "Bhoomi 8.0 (Rs 50 crore) and Kaveri 3.0 (Rs 65 crore) for land records and registration, and 207 sub-registrar offices to be digitised."),
          ("3 Sep 2026 (Act 39 of 2026)", "The Sakaala amendment received assent on 3 September and was published in the Gazette on 4 September 2026; it adds government revision (section 13-A, within three months of the order) and costs for malicious or vexatious complaints (section 13-B).", True),
          ("7 Sep 2026 (as reported)", "The Praja Seva Abhiyan, launched by the Chief Minister at Kudligi, had received over 25,000 grievance petitions."),
          ("Portal, retrieved 21 Nov 2026", f"Sakala covers {DEPTS} departments and institutions and {SERVICES:,} notified services.")])
    + numbers(["Measure", "Dated fact", "Source and status"],
              [["Praja Seva Abhiyan", "Over 25,000 petitions by 7 September 2026", "The Hindu (secondary)"],
               ["Bhoomi 8.0", "Rs 50 crore, announced in the 6 March 2026 budget", "Indian Express (secondary)"],
               ["Kaveri 3.0", "Rs 65 crore, AI-based paperless registration, announced 6 March 2026", "Indian Express (secondary)"],
               ["Sub-registrar offices", "207 to be digitised for pre-2003 documents", "Indian Express (secondary)"],
               ["Land records coverage", "100% of villages and sub-registrar offices computerised; Bhoomi servers often slow", "Draft for discussion; publisher not confirmed"],
               ["Sakala services, April 2022", f"{SERV_2022:,} notified services, called the highest in the country under a right-to-service Act", "DARPG webinar report"]],
              "Show the dated facts"),
    "Karnataka pairs a statutory guarantee for notified services with portal upgrades and grievance drives, but only the statute carries an appeal ladder and a compensation figure, so it is the part a citizen can enforce.",
    "A citizen should check the Sakala service compendium for the specific service and time limit before choosing between a Sakala appeal and a grievance petition.",
    "other")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Department of Personnel and Administrative Reforms, Karnataka:</b> date-stamp every counter on the Sakala portal home page.</li>
<li><b>Sakala Mission:</b> publish monthly delivered-in-time, delivered-late, rejected and pending counts for each department, not only cumulative receipts and disposals.</li>
<li><b>Sakala Mission:</b> publish the number of compensation payments and total rupees paid and recovered from salaries each year.</li>
<li><b>Karnataka Government:</b> list the notified compensation rate and the competent officer beside each service in the service compendium now that the Schedule can vary rates.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>How the law changed</summary>
<ul>
<li><b>Karnataka Guarantee of Services to Citizens Bill, 2011:</b> enacted as Karnataka Act 1 of 2012. The compiled text carries the header &lsquo;Amended vide Notification No. SAMVYASHAVI 32 Shasana 2012, Dated: 3.9.2012&rsquo;, and the 2014 amending Act already calls the principal Act the Karnataka Sakala Services Act, 2011, so the name had changed by September 2014. The instrument that renamed it was not read.</li>
<li><b>Karnataka Act 31 of 2014</b> (assent 2 September 2014, first published 6 September 2014): section 7 now covers delivery electronically or by post on payment of prescribed fees; section 9 extends liability to appellate authorities and competent officers; section 11(4) requires the debit note to be entered in the HRMS software within thirty days; section 14(4) sends an official who defaults more than seven times to enquiry, with Government action within one month of the report.</li>
<li><b>Karnataka Act 39 of 2026</b> (assent 3 September 2026, Gazette 4 September 2026; the Bill passed the Legislature on 24 August 2026 according to a report dated 25 August): section 4 lets the Government amend the Schedule, including compensation and punitive cost rates; section 9 allows rates set in the Schedule; section 13-A adds revision by the Government; section 13-B adds costs for malicious or vexatious complaints, recoverable as land revenue arrears; section 18 extends the bar on civil courts to matters the Government decides.</li>
<li><b>Exclusions and limits in the text:</b> only services listed in the Schedule are covered; compensation does not apply where the Government has banned or restricted the service (section 9); a default is not counted as misconduct unless habitual and wilful (section 14(1) and (2)); no suit lies for action in good faith (section 17).</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The Schedule of notified services and time limits: it was not in the compiled text, and the service compendium PDF was not opened.</li>
<li>The date of the portal counters (they were read from a search-tool excerpt of the home page, not from the live page), and any split between on-time, late and rejected applications; the portal&rsquo;s MIS report page did not load from the build environment.</li>
<li>District and department figures reported elsewhere (for example Mysuru placing second statewide for April 2026 with 1,19,801 applications received, 9,937 rejected and 98.34% cleared, and Rural Development and Panchayat Raj having 33,000 pending): none was found in a source that could be read, so none is used.</li>
<li>The Karnataka High Court order of 1 August 2025: The Hindu reports that a Division Bench (Chief Justice Vibhu Bakhru and Justice C.M. Joshi), on a petition by a Bengaluru resident, directed the State to file a status report on applications received and pending. The pending counts the State filed were not found.</li>
<li>The October 2026 slab: the Rs 20 to Rs 100 a day bands and the Rs 1,500 maximum are from an excerpt of one newspaper report; the notification and the middle bands were not read.</li>
<li>The renaming instrument, the commencement date of Act 1 of 2012 and the statutory penalty provisions for malicious complaints beyond sections 13-A and 13-B.</li>
<li>Whether Sakala reduced delays or corruption: the sources read count applications, not outcomes. Karnataka&rsquo;s other measures here are announcements and counts, not evaluations.</li>
<li>Spelling: the Gazette and the 2026 Act use &lsquo;Sakaala&rsquo;; the portal and most reports use &lsquo;Sakala&rsquo;.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://prsindia.org/files/bills_acts/acts_states/karnataka/2012/2012KA1.pdf">PRS Legislative Research, The Karnataka Sakaala Services Act, 2011 (Act 1 of 2012) with Acts 31 of 2014 and 39 of 2026</a> (compilation; PRS notes it is not authoritative); '
    '<a href="https://kla.kar.nic.in/council/house/bills/159/15e.pdf">Karnataka Legislative Council, Sakaala Services (Amendment) Bill, 2026</a> (primary; text of sections 4, 9, 13-A, 13-B and 18); '
    '<a href="https://sakala.kar.nic.in/index.aspx">Sakala portal home page</a> (primary; counters undated); '
    '<a href="https://www.thehindu.com/news/national/karnataka/sakaala-services-amendment-bill-passed-in-karnataka-legislature/article71388469.ece">The Hindu, 25 August 2026</a> (secondary: the Bill passed); '
    '<a href="https://www.thehindu.com/news/national/karnataka/karnataka-brings-government-employees-services-under-sakala-act-hefty-fines-for-delays-and-malicious-complaints/article71599457.ece">The Hindu, 18 October 2026</a> (secondary, excerpt: staff services and penalty slab); '
    '<a href="https://nammaward.in/wardpulse/karnataka-sakaala-amendment-service-delays-and-safeguards">NammaWard, 16 September 2026</a> (secondary: reading of Gazette 894); '
    '<a href="https://www.thehindu.com/news/national/karnataka/submit-status-report-on-applications-filed-under-sakala-scheme-hc/article69883487.ece">The Hindu, 1 August 2025</a> (secondary: High Court order); '
    '<a href="https://www.darpg.gov.in/static/uploads/2025/11/6d9021ab7807561ae0b1abec56e890f2.pdf">DARPG, NGGWS webinar report</a> (government; 1,115 services as on 20 April 2022); '
    '<a href="https://www.thehindu.com/news/national/karnataka/25000-applications-received-in-praja-seva-abhiyan/article71438989.ece">The Hindu, 7 September 2026</a> (secondary: Praja Seva Abhiyan); '
    '<a href="http://indianexpress.com/article/cities/bangalore/karnataka-bhoomi-8-kaveri-3-land-records-budget-2026-10568042">Indian Express, 6 March 2026</a> (secondary: budget); '
    '<a href="https://cdnbbsr.s3waas.gov.in/s3d69116f8b0140cdeb1f99a4d5096ffe4/uploads/2025/07/20250730596089689.pdf">Karnataka land records study, draft for discussion</a> (publisher not confirmed). '
    'Averages, shares, days to the cap and the slab check computed by this blog. Analysed 21 November 2026.')

RELATED = []

step(4, "assembling page")
build("Governance &middot; Karnataka", TITLE,
      "Karnataka guarantees notified citizen services within a stipulated time, with two appeals and compensation of Rs 20 a day up to Rs 500 recovered from the responsible official; the 2026 amendment lets the Schedule vary the rates.",
      body, SOURCES, RELATED, str(OUT))
step(5, "checking output")
html = OUT.read_text()
# The shared page template (tools/postbuild/buildpost.py) loads accordion.js from a path that contains the old name; that is in every post built
# with it. Everything written here (title, body, sources) must be free of the old name and domain.
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
step(6, "done writing")
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
step(7, "complete")
