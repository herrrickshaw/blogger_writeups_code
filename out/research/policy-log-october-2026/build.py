"""One-month policy log, October 2026, from the PRS Legislative Research Monthly Policy Review (October 2026, published 2 November 2026,
27 pages, read in full). The review summarises official notifications; this post is therefore a secondary source for every item and names the
notification date PRS gives in its footnotes. Items already on this blog (repo rate, IDBI Bank sale, SME Growth Fund, draft steel policy, E100 flex-fuel
rules, mobile phone manufacturing scheme guidelines) are left out.
Build from the repo root:  python3 out/research/policy-log-october-2026/build.py   (writes out/post-policy-log-october-2026.html)
Analysed 25 November 2026."""
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

OUT = ROOT / "out/post-policy-log-october-2026.html"
STEPS = 6


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. dates (the weekdays are computed, not quoted)
step(1, "dates")
ASOF = D(2026, 11, 25)
DATES = {"gst": D(2026, 10, 9), "rbi": D(2026, 10, 10), "cabinet_nsap": D(2026, 10, 14), "container": D(2026, 10, 28),
         "vayuyan": D(2026, 10, 31), "vayuyan_in_force": D(2027, 1, 1), "bs7": D(2026, 10, 12), "bs7_comments": D(2026, 11, 11),
         "dac": D(2026, 10, 26), "itla": D(2026, 10, 6), "gram": D(2026, 10, 28), "sebi_sme": D(2026, 10, 14), "sebi_sme_comments": D(2026, 11, 4),
         "trai": D(2026, 10, 30), "trai_comments": D(2026, 11, 27), "csr": D(2026, 10, 26)}
assert (DATES["vayuyan_in_force"] - DATES["vayuyan"]).days == 62
assert (DATES["bs7_comments"] - DATES["bs7"]).days == 30                 # a 30-day window
assert (DATES["sebi_sme_comments"] - DATES["sebi_sme"]).days == 21
assert (DATES["trai_comments"] - DATES["trai"]).days == 28
assert (DATES["trai_comments"] - ASOF).days == 2                          # comment window still open on the analysis date
assert all(d < ASOF for k, d in DATES.items() if k in ("gst", "rbi", "container", "dac", "itla", "gram", "sebi_sme_comments", "bs7_comments"))
assert DATES["gst"].strftime("%A") == "Friday"

# ---- 2. GST Council, 57th meeting (PRS p. 2; Council press release 9 Oct 2026)
step(2, "GST changes")
GST = {"prosecution threshold (Rs crore)": (1, 5), "maximum general penalty (Rs)": (25000, 10000), "refund acknowledgement window (days)": (15, 10)}
assert GST["prosecution threshold (Rs crore)"][1] / GST["prosecution threshold (Rs crore)"][0] == 5
assert f"{100 * (25000 - 10000) / 25000:.0f}" == "60"                      # penalty cap cut by 60%
assert (15 - 10) / 15 > 0.33 and f"{100 * (15 - 10) / 15:.1f}" == "33.3"

# ---- 3. Container Manufacturing Promotion Scheme (PIB 28 Oct 2026 via PRS p. 4)
step(3, "container scheme")
CMP = {"Operational expenditure assistance": 8891, "Interest subvention (3% a year)": 859, "Testing and certification": 150}
OUTLAY = 10000
SUM_PARTS = sum(CMP.values())
assert SUM_PARTS == 9900 and OUTLAY - SUM_PARTS == 100                     # Rs 100 crore not itemised in the PRS summary
assert f"{100 * CMP['Operational expenditure assistance'] / OUTLAY:.1f}" == "88.9"
CAP_TEU = 7.5e5
assert CAP_TEU == 750000 and 2 * 10 ** 6 / CAP_TEU > 2.6                    # ~2 million empty containers imported a year (PRS); 7.5 lakh TEU target capacity
assert 2 * 10 ** 6 / CAP_TEU == 2.6666666666666665

# ---- 4. National Social Assistance Programme (PRS p. 5; Ministry of Rural Development 14 Oct 2026)
step(4, "social assistance")
NSAP_OUT = 53428
assert f"{NSAP_OUT / 5:,.1f}" == "10,685.6"                                 # Rs crore a year on average over 2026-27 to 2030-31
PENS = {"Under 80 years": (300, 375), "80 years and over": (500, 625)}
RISE = {k: round(100 * (b - a) / a, 1) for k, (a, b) in PENS.items()}
assert RISE == {"Under 80 years": 25.0, "80 years and over": 25.0}
assert 80 - 40 == 40                                                      # disability benchmark cut from 80% to 40%

# ---- 5. other items
step(5, "other items")
VIKSIT = {"total": 7396, "centre": 4869, "state": 2526}
assert VIKSIT["centre"] + VIKSIT["state"] == 7395 and VIKSIT["total"] - 7395 == 1      # Rs 1 crore rounding difference in the PRS figures
assert f"{100 * VIKSIT['centre'] / VIKSIT['total']:.1f}" == "65.8" and f"{100 * VIKSIT['state'] / VIKSIT['total']:.1f}" == "34.2"
DAC_CR = 2.12e5
assert round(DAC_CR * 0.82) == 173840                                       # 82% from Indian industry, about Rs 1.74 lakh crore (computed)
SME_LISTED, SME_RAISED = 1496, 40222
assert f"{SME_RAISED / SME_LISTED:.1f}" == "26.9"                           # Rs crore raised per company, average
FERR_USD, DER_OLD, DER_NEW = 2e6, 100, 5
assert DER_OLD / DER_NEW == 20
CRR_OLD, CRR_NEW = 90, 99
assert CRR_NEW - CRR_OLD == 9
SPORTS = {"production incentives": 1130, "certification": 105}
assert 1857 - 1130 - 105 == 622                                            # remainder of the Rs 1,857 crore not itemised in the PRS summary

TITLE = "India's policy log, October 2026: ten dated changes with figures and effective dates"
assert 55 <= len(TITLE) <= 90, len(TITLE)
assert not any(w in TITLE.lower().split() for w in ("you", "your", "we", "our"))

step(6, "writing sections")
top = top_line([
    ("Rs 5 crore", " is the prosecution threshold the GST Council recommended on 9 October 2026, up from Rs 1 crore, with the maximum general penalty cut from Rs 25,000 to Rs 10,000 and arrest powers to be removed from the CGST Act."),
    ("5 million dollars", " is the new limit for entering rupee currency derivative contracts without showing an underlying exposure, down from 100 million, in the RBI measures of 10 October; the daily Cash Reserve Ratio minimum rose from 90% to 99%."),
    ("1 January 2027", " is when the Bharatiya Vayuyan Niyam, 2026 takes effect, 62 days after its notification on 31 October 2026; it removes the aviation regulator&rsquo;s power to act on excessive airfares."),
])

log = ('<section class="xv-sec"><h2 class="gb-h2" id="log">Ten dated changes, 6 to 31 October 2026</h2>\n'
       + flow([
           ("6 Oct", "<b>1.</b> Cabinet sets up the Integrated Transport and Logistics Authority, which will appraise and monitor central transport projects costing above Rs 500 crore and prepare a 10-year national transport master plan."),
           ("9 Oct", "<b>2.</b> GST Council (57th meeting) recommends a prosecution threshold of Rs 5 crore against Rs 1 crore, a maximum general penalty of Rs 10,000 against Rs 25,000, no show cause notice under Rs 10,000 of tax, and refund acknowledgement in 10 days against 15. The CGST (Amendment) Rules, 2026 followed on 26 October.", True),
           ("9 to 10 Oct", "<b>3.</b> RBI raises the daily minimum Cash Reserve Ratio maintenance from 90% to 99% (notification of 9 October) and tightens rupee currency derivatives: the limit without an underlying exposure falls from USD 100 million to USD 5 million, and specified contracts above USD 2 million need a Foreign Exchange Risk Reserve of 20% of the rupee amount (press release of 10 October). A special dollar window for three oil marketing companies opened on 12 October."),
           ("12 to 13 Oct", "<b>4.</b> Draft Bharat Stage VII emission rules proposed: limits would apply to cars from April 2029, light goods vehicles from April 2030 and larger vehicles from April 2031; comments invited until 11 November."),
           ("14 Oct", "<b>5.</b> Cabinet continues the National Social Assistance Programme from 2026-27 to 2030-31 with an expected outlay of Rs 53,428 crore, renamed Pradhan Mantri Samajik Sahayata Yojana. SEBI the same day invites comments on SME IPO rules until 4 November."),
           ("26 Oct", "<b>6.</b> Defence Acquisition Council gives in-principle approval to acquisition proposals worth Rs 2.12 lakh crore, with about 82% to be bought from Indian industry."),
           ("28 Oct", "<b>7.</b> Cabinet approves the Container Manufacturing Promotion Scheme, Rs 10,000 crore to 2039-40, and the Pradhan Mantri Viksit Gram Swaraj Yojana, Rs 7,396 crore for 2026-27 to 2030-31, and the Khelo India Sports Goods Manufacturing Scheme, Rs 1,857 crore for 2026 to 2034."),
           ("30 Oct", "<b>8.</b> TRAI issues draft guidelines on responsible use of artificial intelligence in telecom networks; comments invited until 27 November."),
           ("31 Oct", "<b>9.</b> Ministry of Civil Aviation notifies the Bharatiya Vayuyan Niyam, 2026, in force from 1 January 2027."),
           ("30 Sep, in force Oct", "<b>10.</b> Tribunal rules under the Tribunals Reforms Act, 2026 apply to 15 tribunals; serving judges and government officers appointed to them must resign or take voluntary retirement from their parent service."),
       ]) + '</section>\n')

s1 = insight(
    "GST Council, 9 October 2026: prosecution threshold up fivefold, penalty cap down 60%",
    bars("GST Council recommended a prosecution threshold of Rs 5 crore, five times Rs 1 crore",
         [("Prosecution threshold now: Rs 1 crore", GST["prosecution threshold (Rs crore)"][0]),
          ("Prosecution threshold recommended: Rs 5 crore", GST["prosecution threshold (Rs crore)"][1])],
         accent="Prosecution threshold recommended: Rs 5 crore", unit=" crore", fmt=lambda v: f"Rs {v:g} crore", vmax=5.5,
         sub="Monetary threshold for prosecution under the CGST Act, Rs crore. The maximum general penalty falls from Rs 25,000 to Rs 10,000 (60%, computed) and refund acknowledgement from 15 to 10 days (33.3%, computed). These are recommendations; only part was given effect by rules.",
         source="PRS Monthly Policy Review, October 2026, p. 2 (secondary, summarising the Council press release of 9 October 2026).")
    + numbers(["Subject", "Before", "Recommended or notified"],
              [["Arrest powers under the CGST Act", "In force", "Recommended to be removed by amending the Act"],
               ["Prosecution threshold", "Rs 1 crore", "Rs 5 crore"], ["Maximum general penalty", "Rs 25,000", "Rs 10,000"],
               ["Show cause notice", "Not stated", "None where the tax involved is under Rs 10,000"],
               ["Refund acknowledgement or deficiency memo", "15 days", "10 days"],
               ["Refund for zero-rated supplies and inverted duty structure", "Not stated", "90% sanctioned provisionally within three working days of acknowledgement"],
               ["Small B2C sellers on e-commerce platforms", "Place of business needed in each state of supply", "Registration without it; operator&rsquo;s warehouse may be the principal place of business"],
               ["Notified on 26 October 2026", "&mdash;", "CGST (Amendment) Rules, 2026, mainly on registration and refunds"]],
              "Show the GST changes"),
    "A recommendation of the Council takes effect only when the Act or the rules are amended, and PRS reports that rules were notified on 26 October 2026 only for the registration and refund changes.",
    "The Ministry of Finance should publish the date by which each remaining recommendation, including the removal of arrest powers, will be put before Parliament.",
    "gst")

s2 = insight(
    "Container scheme: Rs 10,000 crore to 2039-40, 88.9% as operating-cost aid",
    bars("Rs 8,891 crore of the Rs 10,000 crore scheme is operating-cost assistance",
         [("Operating-cost assistance", CMP["Operational expenditure assistance"]), ("Interest subvention at 3% a year", CMP["Interest subvention (3% a year)"]),
          ("Testing and certification facilities", CMP["Testing and certification"]), ("Not itemised in the summary", OUTLAY - SUM_PARTS)],
         accent="Operating-cost assistance", unit=" crore", fmt=lambda v: f"Rs {v:,.0f} crore", vmax=9500,
         sub="Allocation, Rs crore. The three itemised parts sum to Rs 9,900 crore; the remaining Rs 100 crore is computed here and the summary does not say what it covers. The scheme aims at about 7.5 lakh twenty-foot equivalent units a year, ten times present capacity.",
         source="PRS Monthly Policy Review, October 2026, p. 4 (secondary, citing the Cabinet decision of 28 October 2026).")
    + numbers(["Item", "Statement"],
              [["Duration and outlay", "Up to 2039-40; Rs 10,000 crore"],
               ["Imports", "India imports nearly two million empty containers a year, PRS says, for domestic demand and repositioning"],
               ["Capacity aim", "About ten-fold, to 7.5 lakh TEU of annual domestic capacity"],
               ["Eligibility for interest support", "New facility of at least 1,00,000 TEU a year; expansion adding at least 25,000 TEU; to be commissioned within three years of in-principle approval"],
               ["Share of outlay as operating-cost assistance", "88.9% (computed)"]],
              "Show the scheme terms"),
    "Most of the money pays the cost gap on containers sold, so the scheme&rsquo;s cost depends on how many containers eligible makers sell and not on factories built.",
    "The Ministry of Ports, Shipping and Waterways should publish the per-container rate of the cost-gap assistance and the yearly cap, so that the Rs 8,891 crore can be tested against the 7.5 lakh TEU aim.",
    "containers")

s3 = insight(
    "Social assistance programme: Rs 53,428 crore to 2030-31, disability pension up 25%",
    bars("Disability pension rises 25% in both age groups; the disability threshold falls to 40%",
         [("Under 80 years: Rs 300 to Rs 375 a month", RISE["Under 80 years"]), ("80 years and over: Rs 500 to Rs 625 a month", RISE["80 years and over"])],
         accent=["Under 80 years: Rs 300 to Rs 375 a month", "80 years and over: Rs 500 to Rs 625 a month"], unit="%", vmax=30,
         sub="Rise in the monthly disability pension, per cent, computed here from the old and new amounts. The minimum disability benchmark falls from 80% to 40% and the minimum age is removed. Average outlay is Rs 10,685.6 crore a year over five years, computed.",
         source="PRS Monthly Policy Review, October 2026, p. 5 (secondary, citing the Ministry of Rural Development release of 14 October 2026).")
    + numbers(["Item", "Statement"],
              [["Period and outlay", "2026-27 to 2030-31; Rs 53,428 crore expected"],
               ["New name", "Pradhan Mantri Samajik Sahayata Yojana"],
               ["Disability pension, under 80", "Rs 300 to Rs 375 a month"], ["Disability pension, 80 and over", "Rs 500 to Rs 625 a month"],
               ["Eligibility", "Disability benchmark 80% lowered to 40%; minimum age criterion removed"]],
              "Show the programme terms"),
    "Lowering the disability threshold from 80% to 40% widens who qualifies, and the summary gives no estimate of beneficiaries, so the outlay cannot be turned into a cost for each person.",
    "The Ministry of Rural Development should publish the expected number of disability pensioners under the 40% benchmark and the central and state shares of the monthly pension.",
    "nsap")

dates = ('<section class="xv-sec"><h2 class="gb-h2" id="ahead">Dates still ahead on 25 November 2026</h2>\n'
         + flow([("27 Nov 2026", "Comments close on TRAI draft guidelines on responsible AI in telecom (28 days after 30 October); two days from the analysis date."),
                 ("1 Jan 2027", "Bharatiya Vayuyan Niyam, 2026 takes effect (62 days after notification)."),
                 ("April 2027", "SEBI common advertisement code for mutual funds, advisers and brokers comes into force; PRS gives no day."),
                 ("April 2029", "Proposed Bharat Stage VII limits start for cars with up to nine seats; light goods vehicles April 2030, larger vehicles April 2031."),
                 ("2039-40", "Container Manufacturing Promotion Scheme runs up to this year.")])
         + '</section>\n')

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Finance:</b> publish a single table of GST Council recommendations with the legal change each needs and the date it takes effect.</li>
<li><b>PRS and the ministries:</b> give each scheme summary the full itemisation, so that parts sum to the outlay (the container scheme leaves Rs 100 crore and the sports scheme Rs 622 crore unexplained).</li>
<li><b>Ministry of Rural Development:</b> state the number of people expected to qualify under the lowered disability benchmark.</li>
<li><b>Ministry of Road Transport and Highways:</b> publish the cost and fuel-price impact of the proposed Bharat Stage VII limits with the draft.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The Monthly Policy Review for October 2026 (27 pages, dated 2 November 2026) was read in full as a PDF. PRS summarises official notifications and names their dates in its footnotes; this post did not open those primary notifications, so every item is secondary.</li>
<li>Items already published on this blog were left out: the repo rate increase, the IDBI Bank sale, the SME Growth Fund, the draft National Steel Policy, E100 flex-fuel rules and the Mobile Phone Manufacturing Scheme guidelines. Titles of the 523 posts in the archive were checked by keyword.</li>
<li>Dates are those PRS gives for the decision or notification; weekdays, window lengths, percentages and averages are computed here.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The text of any notification, Cabinet note or Council press release: only PRS&rsquo;s summaries were read, and PRS footnote links were not opened.</li>
<li>The exact date the Tribunals Rules took effect: PRS cites a notification of 30 September 2026 and describes them as notified in the October review.</li>
<li>The DAC figure: PRS text says about Rs 2.1 lakh crore and its footnote title says Rs 2.12 lakh crore; Rs 2.12 lakh crore is used and the 82% share is as PRS reports it.</li>
<li>The Pradhan Mantri Viksit Gram Swaraj Yojana split: PRS gives Rs 7,396 crore, with a central share of Rs 4,869 crore and a state share of Rs 2,526 crore, which sum to Rs 7,395 crore; the Rs 1 crore difference is rounding in the source.</li>
<li>What part of the Rs 10,000 crore container scheme (Rs 100 crore) and the Rs 1,857 crore sports goods scheme (Rs 622 crore after the itemised Rs 1,130 crore and Rs 105 crore) the summaries leave unitemised.</li>
<li>Whether any October item took effect after 2 November 2026: the review stops on that date.</li>
<li>Other items in the review that are not in this log: an expert committee report on pipeline safety, hydrogen blending guidelines, right-of-way compensation guidelines for transmission lines, Census Rules, Mineral Auction Rules and parliamentary committee reports, which the review also covers.</li>
</ul></details>
'''

body = STYLE + top + log + s1 + s2 + s3 + dates + fixes + method + gaps

SOURCES = (
    '<a href="https://prsindia.org/files/policy/policy_annual_policy_review/Monthly%20Policy%20Review/2026-11-02/MPR_October_2026.pdf">PRS Legislative Research, Monthly Policy Review, October 2026, 2 November 2026</a> (secondary summary of official notifications, read in full). '
    'Notification dates as given in the PRS footnotes: GST Council press release 9 October 2026; RBI notification of 9 October and press release of 10 October 2026; Cabinet decisions of 6, 14 and 28 October 2026; Ministry of Civil Aviation notification of 31 October 2026; Defence Ministry release of 26 October 2026; TRAI draft of 30 October 2026. Computations by this blog. Analysed 25 November 2026.')
RELATED = [("https://blog.vertistratsolution.com/2026/10/the-sme-growth-fund-is-indias-fourth.html", "SME Growth Fund: India's fourth ₹10,000 crore government equity programme"),
           ("https://blog.vertistratsolution.com/2026/11/indias-retail-inflation-609-in-october.html", "India's retail inflation: 6.09% in October 2026, above the RBI's 6% upper limit")]

build("Policy &middot; Monthly log", TITLE,
      "A one-month log of dated policy changes in October 2026, taken from the PRS Monthly Policy Review, with the figures that change and the dates that follow.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
