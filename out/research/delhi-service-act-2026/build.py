"""Delhi (Right of Citizen to Time Bound and Ease of Delivery of Services) Act, 2026 (Delhi Act 10 of 2026): what it guarantees, how appeals and
penalties work, how it differs from the Karnataka Sakaala Act, transition of pending 2011-law applications, and commencement.
Build from the repo root:  python3 out/research/delhi-service-act-2026/build.py   (writes out/post-delhi-service-delivery-act-2026.html)
Statute figures were read from the PRS copy of the Delhi Gazette Extraordinary of 27 August 2026 (English text, sections 1 to 21), downloaded and
converted to text on 21 November 2026. Karnataka figures were read from the PRS compilation of the Karnataka Act. The e-SLA dashboard figures,
the 9 November 2026 notification and the Rs 249 report are from search-result excerpts only; the post labels each. Every computed figure is asserted.
The Schedule (services and time limits) is not in the PRS PDF; the post says so."""
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-delhi-service-delivery-act-2026.html"
B = "https://blog.vertistratsolution.com"
STEPS = 7


def step(n, what):
    el = time.time() - T0
    eta = el / n * (STEPS - n) if n else 0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {eta:.1f}s left)", flush=True)


HEADS = []   # every title and heading, checked against docs/HEADLINE_STYLE.md at the end


def H(t):
    HEADS.append(t)
    return t


# ---- 1. Delhi Act 10 of 2026, as printed in the Gazette (PRS copy)
step(1, "Delhi Act figures and consistency checks")
D_RATE, D_CAP = 250, 5000          # section 8(i): Rs 250 per day of default, at most Rs 5,000 in each case
D_LUMP_MIN, D_LUMP_MAX = 250, 5000  # section 8(ii): lump sum for unreasonable rejection, Rs 250 to Rs 5,000
D_COMM_MAX = 5000                  # section 15(2)(vii): Commission may impose a penalty of up to Rs 5,000
AUTH_DAYS = 30                     # section 7(7): Authority decides within 30 days of receipt of appeal
COMM_DAYS = 30                     # section 9(2): appeal to the Commission within 30 days of the order
REPLY_DAYS = 7                     # section 7(9): representation within seven days of the notice
DIRECT_DAYS = 7                    # section 7(5) proviso: direction to give the service within 07 days
DAYS_TO_CAP = D_CAP / D_RATE
assert DAYS_TO_CAP == 20
assert D_LUMP_MIN == D_RATE and D_LUMP_MAX == D_CAP == D_COMM_MAX
assert (AUTH_DAYS, COMM_DAYS, REPLY_DAYS, DIRECT_DAYS) == (30, 30, 7, 7)

# ---- 2. Karnataka Sakaala Act, section 9 (PRS compilation 2012KA1.pdf; same figures in the sibling post)
step(2, "Karnataka comparison figures and checks")
K_RATE, K_CAP = 20, 500
K_DAYS_TO_CAP = K_CAP / K_RATE
assert K_DAYS_TO_CAP == 25
RATE_X = D_RATE / K_RATE
CAP_X = D_CAP / K_CAP
assert RATE_X == 12.5 and CAP_X == 10.0
assert DAYS_TO_CAP < K_DAYS_TO_CAP          # Delhi reaches its cap sooner (20 against 25 days)
# the 2011 PRS comparison table prints the same Rs 250 a day, Rs 5,000 cap for other states' laws: the Delhi 2026 formula is not new
PRS2012_RATE, PRS2012_CAP = 250, 5000
assert (PRS2012_RATE, PRS2012_CAP) == (D_RATE, D_CAP)
DELHI2011_COST = 10                # PRS brief of 27 Sep 2012, table: Delhi 2011 Act, cost of Rs 10 per application
assert D_RATE / DELHI2011_COST == 25.0

# ---- 3. e-SLA dashboard (esla.delhi.gov.in; figures read from a search-result excerpt on 21 Nov 2026; the page prints no date)
step(3, "e-SLA dashboard figures and checks")
SERVICES, DEPTS = 567, 46
APPS_LAKH = 36                     # printed as "36+ lakhs"
APPS_MIN = APPS_LAKH * 100_000
IN_TIME = 65.02
NOT_IN_TIME = round(100 - IN_TIME, 2)
assert NOT_IN_TIME == 34.98
assert abs(IN_TIME + NOT_IN_TIME - 100) < 1e-9
AVG_MIN = APPS_MIN / SERVICES
assert int(AVG_MIN) == 6349                 # at least this many applications per notified service, on average
assert round(APPS_MIN * IN_TIME / 100) == 2_340_720   # lower bound on applications disposed in time, since the count is '36+'
assert round(APPS_MIN * NOT_IN_TIME / 100) == 1_259_280

TITLE = H("Delhi Act 10 of 2026: Rs 250 a day for service delay, up to Rs 5,000 a case")
assert 55 <= len(TITLE) <= 90, len(TITLE)

step(4, "writing sections")
top = top_line([
    (f"Rs {D_CAP:,}", f" is the most an official can be fined per case under section 8: Rs {D_RATE} a day of delay, reached after {DAYS_TO_CAP:.0f} days, paid into the government treasury and not to the applicant."),
    (f"{RATE_X:g} times", f" Karnataka&rsquo;s daily rate of Rs {K_RATE}, with a cap {CAP_X:g} times Karnataka&rsquo;s Rs {K_CAP}; Karnataka pays the citizen, Delhi does not."),
    (f"{IN_TIME}%", f" of over {APPS_LAKH} lakh applications are shown as disposed in time on the e-SLA dashboard, a count of {SERVICES} services in {DEPTS} departments that carries no date."),
])

s1 = insight(
    f"A late application becomes an appeal automatically and must be decided within {AUTH_DAYS} days",
    bars(f"Both appeal stages run {AUTH_DAYS} days; officials get {REPLY_DAYS} days to reply to a notice",
         [("Authority decides an appeal (section 7)", AUTH_DAYS),
          ("Appeal to the Commission against the Authority&rsquo;s order (section 9)", COMM_DAYS),
          ("Official&rsquo;s reply to a show-cause notice (section 7)", REPLY_DAYS),
          ("Direction to give the service when the default is plainly wrong (section 7)", DIRECT_DAYS)],
         accent=["Authority decides an appeal (section 7)", "Appeal to the Commission against the Authority&rsquo;s order (section 9)"],
         unit=" days", vmax=35,
         sub="Time limits written into the Act, in days. The Commission may admit a late appeal for reasonable cause.",
         source="Delhi Act 10 of 2026, Delhi Gazette Extraordinary, 27 August 2026 (PRS copy).")
    + numbers(["Step", "Who acts", "Limit", "Section"],
              [["Application gets a unique number and online tracking", "Department or local body", "On receipt", "5(2)"],
               ["Service given, or rejection with written reasons", "Designated Officer", "The time limit in the Schedule", "5(4)"],
               ["Appeal on a missed deadline", "Citizen Grievance Redressal Authority, at least one or two levels senior to the officer", "Lodged automatically; the original application is treated as the appeal", "7(1), 7(2), 6(2)"],
               ["Appeal against a rejection", "Applicant to the Authority, online", "No window printed", "7(3)"],
               ["Authority decides the appeal on merits, without sending it back", "Authority", f"{AUTH_DAYS} days", "7(6), 7(7)"],
               ["Show-cause notice to the officer; reply", "Authority; officer", f"{REPLY_DAYS} days", "7(8), 7(9)"],
               ["Appeal to the Delhi Right to Service Commission", "Applicant or officer", f"{COMM_DAYS} days; also automatic if the Authority misses a deadline; order final and binding", "9(1) to 9(4)"],
               ["Commission", "Chairman and three Members; Public Grievance Commission may act until it is formed", "&ndash;", "10, 11"]]),
    "A citizen does not have to file anything for a missed deadline, because the application itself is treated as the first appeal, and a second appeal goes to a Commission whose order is final.",
    "The Government should publish the rules under section 19 that set the appeal forms and the online tracking procedure before the Act is applied to any service.",
    "appeals")

s2 = insight(
    f"Delhi&rsquo;s cap is Rs {D_CAP:,} a case against Rs {K_CAP} in Karnataka, paid to the treasury",
    bars(f"Delhi&rsquo;s maximum per case is Rs {D_CAP:,}, ten times Karnataka&rsquo;s Rs {K_CAP}",
         [("Karnataka Sakaala Act, section 9", K_CAP),
          ("Delhi Act 10 of 2026, section 8", D_CAP)],
         accent="Delhi Act 10 of 2026, section 8", unit="", fmt=lambda v: f"Rs {v:,.0f}", vmax=5500,
         sub=f"Maximum per application or case, rupees. Daily rate: Rs {K_RATE} in Karnataka and Rs {D_RATE} in Delhi. Karnataka&rsquo;s 2026 amendment lets its Schedule set other rates; Delhi&rsquo;s figures are in the Act.",
         source="Delhi Act 10 of 2026 (PRS copy); Karnataka Sakaala Services Act, 2011, section 9 (PRS compilation). Ratios computed here.")
    + numbers(["Item", "Delhi Act 10 of 2026", "Karnataka Sakaala Act"],
              [["Rate for delay", f"Rs {D_RATE} a day (section 8(i))", f"Rs {K_RATE} a day (section 9)"],
               ["Cap for delay", f"Rs {D_CAP:,} a case", f"Rs {K_CAP} an application"],
               ["Days of delay to reach the cap", f"{DAYS_TO_CAP:.0f} (computed)", f"{K_DAYS_TO_CAP:.0f} (computed)"],
               ["Improper rejection", f"Lump sum of Rs {D_LUMP_MIN} to Rs {D_LUMP_MAX:,} (section 8(ii))", "Not a separate figure in section 9"],
               ["Who receives the money", "Government treasury (section 8(iii))", "The citizen is paid first; the cost is then recovered from the official&rsquo;s salary"],
               ["Commission&rsquo;s own power", f"Penalty up to Rs {D_COMM_MAX:,} (section 15(2)(vii))", "&ndash;"],
               ["Official&rsquo;s hearing", f"Representation within {REPLY_DAYS} days before any penalty (section 7(9))", f"Reply within {REPLY_DAYS} days of the notice (section 11(2))"],
               ["Applies to", "Substantive government servants and employees of bodies the Government owns, controls or substantially finances; not casual, daily-wage or (unless the contract says so) contract staff (section 1(4))", "Notified services in the Schedule"]]),
    f"Delhi sets a heavier fine on the official than Karnataka does, but the Act as printed gives the applicant nothing from it, whereas Karnataka compensates the citizen first and then recovers the cost from the official.",
    "The Delhi Government should state in the rules whether any part of a penalty is paid to the applicant, because the Act as printed sends all of it to the treasury.",
    "money")

s3 = insight(
    f"The e-SLA dashboard shows {IN_TIME}% of over {APPS_LAKH} lakh applications disposed in time",
    bars(f"{IN_TIME}% of applications are shown as disposed in time and {NOT_IN_TIME}% are not",
         [("Disposed in time, as reported", IN_TIME), ("Not shown as disposed in time (computed)", NOT_IN_TIME)],
         accent="Not shown as disposed in time (computed)", unit="%", vmax=100,
         sub=f"Share of applications received under the 2011 law&rsquo;s e-SLA system, {SERVICES} services in {DEPTS} departments. The page prints no date, and the second bar can include late, rejected and pending applications.",
         source="Delhi e-SLA dashboard, esla.delhi.gov.in (read as a search-result excerpt on 21 November 2026). Difference computed here.")
    + numbers(["Item", "Value", "Basis"],
              [["Notified and integrated services", f"{SERVICES}", "e-SLA dashboard excerpt"],
               ["Departments covered", f"{DEPTS}", "e-SLA dashboard excerpt"],
               ["Applications received", f"{APPS_LAKH}+ lakh", "e-SLA dashboard excerpt; printed as a floor"],
               ["Disposed in time", f"{IN_TIME}%", "e-SLA dashboard excerpt; the definition of in time was not read"],
               ["Not shown as disposed in time", f"{NOT_IN_TIME}%", "Computed: 100 minus 65.02"],
               ["Average applications per service", f"At least {int(AVG_MIN):,}", "Computed: 36 lakh divided by 567; cumulative, not a yearly rate"],
               ["Pending applications moved to the new Act", "Not published", "Section 21(3) deems them to be applications under the 2026 Act; no count was found"]]),
    f"About a third of applications are not shown as disposed in time, and the figure cannot be set beside Karnataka&rsquo;s portal counter, which shows disposals of any kind and not timeliness.",
    "The Delhi Government should print the as-of date on the dashboard and split the remainder into late, rejected and pending applications for each department.",
    "scale")

s4 = insight(
    "Delhi Act timeline: passed 11 Aug 2026, gazetted 27 Aug, notification reported 9 Nov",
    flow([("2011", "The Delhi (Right of Citizen to Time Bound Delivery of Services) Act, 2011 applies; a 2012 PRS table records its cost of Rs 10 an application on a defaulting servant."),
          ("11 Aug 2026", "The Legislative Assembly of the National Capital Territory passes the Bill."),
          ("25 Aug 2026", "The Lieutenant Governor gives assent."),
          ("27 Aug 2026", "The Act is published in the Delhi Gazette Extraordinary as Delhi Act 10 of 2026; it comes into force on a date the Government appoints by notification (section 1(3)).", True),
          ("About 9 Nov 2026 (as reported)", "News reports say the Government notified the Act; the notification text was not read, and whether it sets the commencement date under section 1(3) is not confirmed."),
          ("On commencement", "The 2011 Act is repealed; applications pending under it are deemed applications under the 2026 Act (section 21).")])
    + numbers(["Item", "Fact", "Basis"],
              [["Passed by the Assembly", "11 August 2026", "Gazette heading"],
               ["Assent of the Lieutenant Governor", "25 August 2026", "Gazette notification"],
               ["Published", "27 August 2026", "Gazette notification"],
               ["Commencement", "Date set by notification (section 1(3))", "Act text"],
               ["Reported notification", "About 9 November 2026", "News On AIR and NewKerala, search excerpts (secondary)"],
               ["Repeal", "Delhi Act of 2011 and its rules repealed on commencement; past actions and accrued rights saved", "Section 21(1), 21(2)"],
               ["Pending applications", "Deemed to be applications under the 2026 Act", "Section 21(3)"],
               ["Difficulty-removal order power", "Two years from commencement", "Section 20"]]),
    "The Act applies only after a commencement notification, so a citizen can rely on its penalties from the date the notification names and not from the date of passage.",
    "The Government should publish the commencement notification, the Schedule of services and the Commission&rsquo;s constitution order together so that applicants can see which deadlines now apply.",
    "timeline")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Delhi Government:</b> publish the Schedule of services, time limits, Designated Officers and Authorities with the commencement notification.</li>
<li><b>Information Technology Department, Delhi:</b> print the as-of date on the e-SLA dashboard and report delivered-in-time, delivered-late, rejected and pending counts by department every month.</li>
<li><b>Delhi Right to Service Commission:</b> publish the annual report required by section 15(6) with the number of penalties imposed and the rupees recovered.</li>
<li><b>Delhi Government:</b> state in the rules whether any part of a penalty reaches the applicant, and publish the count of 2011-law applications carried over under section 21(3).</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>What the Act provides, section by section</summary>
<ul>
<li><b>Right and scope (sections 1 to 4):</b> every citizen has the right to notified services within the Schedule&rsquo;s time limit; the Act applies only to services in the Schedule and to departments, local bodies, autonomous bodies or statutory organisations the Government notifies; the Government may amend the Schedule by notification, laid before the Assembly.</li>
<li><b>Designated Officer (sections 2, 4, 5):</b> the officer responsible for a service, with a Link Designated Officer who covers absences; the officer must give the service or reject with written reasons within the time limit, which starts on receipt of a complete application, and an application submitted online counts as received.</li>
<li><b>Appeals (sections 6, 7, 9):</b> the Authority must be at least one or two levels senior to the Designated Officer; the Authority cannot send an appeal back; a second appeal lies to the Commission within 30 days.</li>
<li><b>Penalty (section 8):</b> if the default is without sufficient and reasonable cause, the Authority or Commission may impose Rs 250 a day up to Rs 5,000, or a lump sum of Rs 250 to Rs 5,000 for unreasonable rejection, after hearing the officer; the penalty may fall on any official involved in the default, and the Authority recovers it from salary under section 7(9).</li>
<li><b>Commission (sections 10 to 15):</b> a Chairman not below Chief Secretary rank and three Members; the Information Technology Department is its administrative department; it may inspect offices, recommend departmental action and issue instructions, and must prepare an annual report.</li>
<li><b>E-governance (section 16):</b> the Government may provide online filing, status updates and auto-escalation on default, and must set up an audit mechanism.</li>
<li><b>Service conditions (sections 17 and 18):</b> the Act is deemed part of the service conditions of government servants and adds to, and does not replace, disciplinary rules.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The Schedule of services and time limits: it is not in the PRS copy of the Act, so no notified service and no deadline is quoted here. The rules under section 19 were not found either.</li>
<li>Whether the notification reported on about 9 November 2026 is the commencement notification under section 1(3). It was read only in search-result excerpts from News On AIR and NewKerala, and one secondary analysis found in a search excerpt said no commencement notification could be located as of 4 September 2026. The text of any notification was not read.</li>
<li>The daily rate: the Gazette text prints Rs 250 a day, but a PTI-based newspaper report of the Bill, seen in a search excerpt, said Rs 249. The Act text is used here.</li>
<li>The e-SLA dashboard figures: 567 services, 46 departments, over 36 lakh applications and 65.02% disposed in time were read from a search-result excerpt of esla.delhi.gov.in, which prints no date. The meaning of in time and the split of the rest were not read, and the dashboard belongs to the 2011 law&rsquo;s system. Other Delhi government sources seen in the same search show other service counts for other portals, such as 453 services on eDistrict, so the counts are not interchangeable.</li>
<li>Pending or disposed applications under the 2011 law at the date of transition: none was found.</li>
<li>Whether the Delhi Right to Service Commission has been constituted; section 10 lets the Public Grievance Commission act until it is.</li>
<li>The Act&rsquo;s name differs between sources: the Gazette says &lsquo;Right of Citizen to Time Bound and Ease of Delivery of Services&rsquo;, while some reports say &lsquo;Right of Citizens to Time-Bound and Easy Delivery of Services&rsquo;. The Gazette form is used. The PRS copy carries a disclaimer that it is not the authoritative text, and the Hindi text was not compared with the English.</li>
<li>Karnataka comparison: the figures are from the PRS compilation of the Karnataka Act; Karnataka&rsquo;s 2026 amendment allows its Schedule to set other rates, and a reported 2026 slab is covered in the <a href="https://blog.vertistratsolution.com/2026/11/karnataka-sakaala-services-act-rs-20.html">Karnataka post</a>.</li>
<li>Whether the Act reduces delays: the sources read describe the law and a dashboard, not outcomes under it.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://prsindia.org/files/bills_acts/acts_states/delhi/2026/Act10of2026DL.pdf">PRS Legislative Research, copy of Delhi Act 10 of 2026, Delhi Gazette Extraordinary, 27 August 2026</a> (primary text via PRS; not authoritative per PRS); '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/karnataka/2012/2012KA1.pdf">PRS Legislative Research, The Karnataka Sakaala Services Act, 2011 (Act 1 of 2012) with later amendments</a> (compilation); '
    '<a href="https://prsindia.org/files/bills_acts/bills_parliament/2011/Legislative_Brief_Citizens_Charter_27_Sep.pdf">PRS Legislative Brief, Citizens Charter Bill, 2011, 27 September 2012</a> (secondary: comparison table of 2011 state laws); '
    '<a href="https://esla.delhi.gov.in/">Delhi e-SLA dashboard</a> (primary; read as a search excerpt, undated); '
    '<a href="https://newsonair.gov.in/delhi-govt-notifies-act-to-ensure-time-bound-delivery-of-government-services/">News On AIR, 9 November 2026</a> (secondary, search excerpt: notification reported); '
    '<a href="https://www.newkerala.com/news/a/delhi-govt-notifies-right-time-bound-delivery-services-act-729.htm">NewKerala, 9 November 2026</a> (secondary, search excerpt); '
    '<a href="https://openthemagazine.com/india/quick-take-delhi-officials-can-lose-up-to-5000-for-delaying-your-application-seven-things-to-know">Open magazine quick take</a> (secondary, search excerpt: Rs 5,000); '
    '<a href="https://dailypioneer.com/delhi/delhi-notifies-new-law-officials-face-rs-5000-penalty-for-service-delays">The Pioneer</a> (secondary, search excerpt: Rs 250 and Rs 249 reports); '
    '<a href="https://righttoinformation.wiki/delhi-time-bound-services-act-2026">righttoinformation.wiki analysis</a> (secondary, search excerpt: commencement). '
    'Ratios, days to the cap and shares computed by this blog. Analysed 21 November 2026.')
RELATED = [(B + "/2026/11/karnataka-sakaala-services-act-rs-20.html", "Karnataka Sakaala Services Act: Rs 20 a day for delay, capped at Rs 500")]
step(5, "assembling page")
build("Governance &middot; Delhi", TITLE,
      "Delhi&rsquo;s 2026 service-delivery Act fines officials Rs 250 a day for delay, up to Rs 5,000 a case, adds an automatic appeal and a Commission, and takes effect when the Government notifies it.",
      body, SOURCES, RELATED, str(OUT))
step(6, "checking output")
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
import re  # noqa: E402
import html as _h  # noqa: E402
for h2 in re.findall(r'<h2 class="gb-h2"[^>]*>(.*?)</h2>', body):
    HEADS.append(h2)
for t in re.findall(r'class="xv-t"[^>]*>(.*?)</span>', body):
    HEADS.append(t)
for h in HEADS:
    p = _h.unescape(h)
    assert len(p) <= 90, (len(p), p)
    assert "?" not in p, p
    assert not any(w in p.lower().replace(",", " ").split() for w in ("you", "your", "we", "our")), p
step(7, "complete")
print("wrote", OUT.relative_to(ROOT), "| title", len(TITLE), "chars | headings checked:", len(HEADS))
