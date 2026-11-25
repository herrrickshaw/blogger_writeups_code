"""Arjun Flour Mills v State of Orissa (Civil Appeal No. 8763 of 1994): the seven-judge reference on a state's power to levy an additional tax
computed on sales tax, disposed of on 4 November 2026. Sources are secondary and well-sourced legal reporting (Supreme Court Observer case page,
report and judgement summary; LiveLaw; CourtBook; Business Standard). The judgement PDF on api.sci.gov.in was not reachable from this environment
(proxy refused), so it was not read. Build from the repo root:  python3 out/research/arjun-flour-mills-2026/build.py   (writes out/post-arjun-flour-mills-sales-tax.html)
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

OUT = ROOT / "out/post-arjun-flour-mills-sales-tax.html"
STEPS = 5


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
step(1, "dates and intervals")
APPEAL, REF5, REF7, LIST, DIRN, ARGS_FIX, HEARD, JUDG, ASOF = (D(1994, 2, 11), D(1998, 8, 13), D(1999, 10, 6), D(2023, 10, 12), D(2024, 1, 9),
                                                              D(2026, 8, 12), D(2026, 9, 22), D(2026, 11, 4), D(2026, 11, 25))
assert APPEAL < REF5 < REF7 < LIST < DIRN < ARGS_FIX < HEARD < JUDG < ASOF


def yrs(a, b):
    return round((b - a).days / 365.25, 1)


GAPS = [("Appeal filed to reference to a five-judge bench, 1994 to 1998", yrs(APPEAL, REF5)),
        ("Five-judge reference to seven-judge reference, 1998 to 1999", yrs(REF5, REF7)),
        ("Seven-judge reference to first listing for directions, 1999 to 2023", yrs(REF7, LIST)),
        ("First listing to arguments, 2023 to 2026", yrs(LIST, HEARD)),
        ("Arguments and reservation to judgement, 22 September to 4 November 2026", yrs(HEARD, JUDG))]
assert [g for _, g in GAPS] == [4.5, 1.1, 24.0, 2.9, 0.1]
TOTAL_YRS = yrs(APPEAL, JUDG)
assert TOTAL_YRS == 32.7
assert (JUDG - HEARD).days == 43
assert yrs(REF7, JUDG) == 27.1 and (JUDG.year - REF7.year) == 27         # SC Observer and CourtBook: a 27-year-old reference
assert (JUDG - ARGS_FIX).days == 84 and (HEARD - ARGS_FIX).days == 41
assert (ASOF - JUDG).days == 21
assert D(2026, 11, 30) > ASOF                                            # the 30 November hearing in the topic list is after today but the case is already decided

step(2, "levy arithmetic")
# Section 5A: additional tax of 10% of the sales tax payable for turnover Rs 10 lakh to Rs 1 crore; 15% above Rs 1 crore (SC Observer report, LiveLaw)
RATES = {"Turnover Rs 10 lakh to Rs 1 crore": 10, "Turnover above Rs 1 crore": 15}
BASE_TAX = 100000                                                          # illustration only: Rs 1 lakh of sales tax payable
EXTRA = {k: BASE_TAX * r // 100 for k, r in RATES.items()}
assert EXTRA == {"Turnover Rs 10 lakh to Rs 1 crore": 10000, "Turnover above Rs 1 crore": 15000}
assert 10 * 100000 == 10 ** 6 and 10 ** 7 // 10 ** 6 == 10                 # Rs 10 lakh = 10 lakh; Rs 1 crore is ten times Rs 10 lakh

TITLE = "Arjun Flour Mills v State of Orissa: seven-judge reference disposed of on 4 November 2026"
assert 55 <= len(TITLE) <= 90, len(TITLE)
assert not any(w in TITLE.lower().split() for w in ("you", "your", "we", "our"))

step(3, "writing sections")
top = top_line([
    ("27 years", " after the reference to a seven-judge bench in October 1999, the Supreme Court disposed of Arjun Flour Mills on 4 November 2026, holding the question infructuous after GST and stating that S. Kodar (1974) continues to govern."),
    ("10% and 15%", " were the additional tax rates on sales tax payable in Section 5A of the Orissa Sales Tax Act, 1947, by turnover band, according to the Supreme Court Observer; other reports state only the 10% rate."),
    ("2 opinions", " were pronounced by a bench of 7 judges: Chief Justice Surya Kant for the Bench and Justice K.V. Viswanathan concurring separately; the judgement runs to 93 pages (as summarised by the Supreme Court Observer)."),
])

status = ('<table class="gb-table"><thead><tr><th>Status on 25 November 2026</th><th>What the sources say</th></tr></thead><tbody>'
          '<tr><td><b>Decided</b></td><td>Disposed of on 4 November 2026: the reference no longer needed an answer after GST (Supreme Court Observer, LiveLaw, CourtBook, Business Standard, all secondary).</td></tr>'
          '<tr><td><b>Still ahead</b></td><td>The Registry was directed to place the lead and connected matters before regular benches for disposal on their merits (CourtBook). No hearing date was found.</td></tr>'
          '<tr><td><b>Conflict</b></td><td>A hearing on 30 November 2026 reported earlier is not supported: the case page still shows &lsquo;Pending&rsquo; with a next hearing of 22 September 2026, and its own report records the disposal of 4 November.</td></tr>'
          '</tbody></table>\n')

q = ('<section class="xv-sec"><h2 class="gb-h2" id="question">The question, the law and the cases</h2>\n'
     + flow([
         ("Statute", "Section 5A of the Orissa Sales Tax Act, 1947 added an additional tax on dealers by annual turnover, calculated on the sales tax payable. The Supreme Court Observer dates the insertion to 15 November 1997."),
         ("Question", "Is a levy computed with reference to an existing sales tax a tax on the sale of goods, which a State may impose under Entry 54 of the State List, or a tax on the dealer&rsquo;s income, which lies outside State power?", True),
         ("Conflict", "The Court that made the reference saw conflict between Hoechst Pharmaceuticals (three judges, upholding a State surcharge under Entry 54) and India Cement (seven judges, in a case on the Madras Panchayats Act)."),
         ("Anchor case", "S. Kodar v State of Kerala (1974, five judges) upheld the Tamil Nadu Additional Sales Tax Act, 1970 as a tax on sales and not on income."),
         ("Answer on 4 November 2026", "The Bench held that Kodar governs: an additional tax computed as a percentage of sales tax enhances the rate and falls under Entry 54, and that the reference was academic because Entry 54 and the State laws were replaced when GST began (101st Amendment)."),
     ]) + '</section>\n')

s1 = insight(
    "Section 5A: 10% extra tax on sales tax payable, 15% above Rs 1 crore of turnover",
    bars("The additional tax was 10% for mid-size dealers and 15% above Rs 1 crore of turnover",
         [("Annual turnover Rs 10 lakh to Rs 1 crore", RATES["Turnover Rs 10 lakh to Rs 1 crore"]), ("Annual turnover above Rs 1 crore", RATES["Turnover above Rs 1 crore"])],
         accent="Annual turnover above Rs 1 crore", unit="%", vmax=16,
         sub="Additional tax as a percentage of the sales tax payable, as the Supreme Court Observer reports Section 5A. On Rs 1 lakh of sales tax that is Rs 10,000 or Rs 15,000 (illustration computed here, not from the case). CourtBook and Business Standard mention only the 10% rate, and the case page names only the Rs 10 lakh to Rs 1 crore band.",
         source="Supreme Court Observer, 4 November 2026 (secondary); LiveLaw, 4 November 2026 (secondary); CourtBook (secondary); Business Standard, 5 November 2026 (secondary).")
    + numbers(["Source", "Rate or band stated for Section 5A"],
              [["Supreme Court Observer report, 4 Nov 2026", "10% for turnover Rs 10 lakh to Rs 1 crore; 15% above Rs 1 crore"],
               ["LiveLaw, 4 Nov 2026", "10% for turnover Rs 10 lakh to Rs 1 crore; 15% above Rs 1 crore"],
               ["Supreme Court Observer case page", "10% for turnover Rs 10 lakh to Rs 1 crore (no second band)"],
               ["CourtBook", "10% of sales tax payable where gross turnover exceeded Rs 10 lakh"],
               ["Business Standard, 5 Nov 2026", "10% of the total sales tax payable"]],
              "Show what each source states"),
    "The sources agree on a 10% additional tax and differ on whether a 15% band applied above Rs 1 crore, which the Supreme Court Observer and LiveLaw report and the others omit.",
    "A reader relying on the rates should check Section 5A of the Orissa Sales Tax Act, 1947 as in force in the years of the dispute, because the post could not open the statute or the judgement.",
    "levy")

s2 = insight(
    "Reference history: 24 of 32.7 years passed between the 1999 reference and the 2023 listing",
    bars("24 of the 32.7 years to judgement passed between the 1999 reference and 2023 listing",
         [(lab, g) for lab, g in GAPS], accent=GAPS[2][0], unit=" years", fmt=lambda v: f"{v:g} years", vmax=26,
         sub="Years between dated steps, computed here from the dates on the Supreme Court Observer case page and its report: appeal filed 11 February 1994, five-judge reference 13 August 1998, seven-judge reference 6 October 1999, listing 12 October 2023, arguments 22 September 2026, judgement 4 November 2026.",
         source="Supreme Court Observer case page and report (secondary); CourtBook (secondary).")
    + numbers(["Date", "Step", "Source"],
              [["11 Feb 1994", "Civil Appeal No. 8763 of 1994 filed (LiveLaw notes the number is not 1863)", "Supreme Court Observer; LiveLaw"],
               ["13 Aug 1998", "Referred to a five-judge bench because of conflicting judgements", "Supreme Court Observer"],
               ["6 Oct 1999", "Referred, with S. Kodar, to a seven-judge bench", "Supreme Court Observer"],
               ["12 Oct 2023", "Listed with five other seven-judge cases for directions; hearing on 9 January 2024 set", "Supreme Court Observer"],
               ["12 Aug 2026", "Bench of Chief Justice Surya Kant and Justices Joymalya Bagchi and V. Mohana directed arguments from 22 September 2026", "Supreme Court Observer"],
               ["22 Sep 2026", "Seven-judge bench heard the matter and reserved judgement", "Supreme Court Observer"],
               ["4 Nov 2026", "Judgement pronounced: Chief Justice Surya Kant for the Bench, Justice K.V. Viswanathan concurring", "Supreme Court Observer; LiveLaw"]],
              "Show the dated steps"),
    "The Court spent 43 days between reserving and delivering judgement and 24 years waiting for the reference to be listed, and the disposal turned on GST replacing the State entry, not on a fresh answer to the question.",
    "A reader tracking pending constitutional references should use the Court&rsquo;s own case status and the order of 4 November 2026, which this post could not open, to confirm dates and the directions to the Registry.",
    "history")

stakes = '''<details class="xv-n" open><summary>The stakes, without a prediction</summary>
<ul>
<li><b>Under GST:</b> Business Standard reports that the judgement creates no new liability under GST. Entry 54 no longer exists after the 101st Constitutional Amendment, according to the Supreme Court Observer.</li>
<li><b>Old disputes:</b> Business Standard reports the observations could influence unresolved disputes on sales tax and surcharges under earlier State laws, and that individual challenges to old demands remain open; the result in each depends on the law and facts of the case.</li>
<li><b>Connected cases:</b> CourtBook reports that the Registry was directed to place the lead and connected matters before regular benches; their number, the States and the amounts involved were not found.</li>
<li><b>Open question:</b> whether a regular bench will accept the Kodar reasoning for a particular State levy has not been decided, and this post makes no forecast.</li>
</ul></details>
'''

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Supreme Court Registry:</b> publish the 4 November 2026 order and the list of connected appeals with the State and the amount involved in each.</li>
<li><b>State finance departments with pre-GST sales tax disputes:</b> publish the number and value of appeals that turn on a surcharge computed on sales tax.</li>
<li><b>Supreme Court Observer and similar trackers:</b> update a case page when a judgement is delivered, so that the page does not show a hearing date after disposal.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Sources are legal-news reports and the Supreme Court Observer case archive, all labelled secondary; the judgement of 4 November 2026 (93 pages, per the Supreme Court Observer) was not opened because the Court&rsquo;s server was not reachable from the analysis environment.</li>
<li>Intervals between dated steps are computed here in years of 365.25 days, rounded to one decimal; the illustration of the levy on Rs 1 lakh of sales tax is computed and is not from the case.</li>
<li>&lsquo;Infructuous&rsquo; means the question no longer needs an answer; &lsquo;academic&rsquo; is used by the reports in the same sense.</li>
<li>The State is spelled Orissa in the statute and the older case title and Odisha in the 2026 reports.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The text of the judgement and of Section 5A: neither was read, so every statement of law and every rate is as reported by secondary sources.</li>
<li>The date Section 5A was enacted: the case page says it was inserted on 15 November 1997, yet the appeal was filed on 11 February 1994 and the reference was made in 1999, so the 1997 date cannot be the whole history; LiveLaw says only that it was introduced in 1997 and another report says the provision dates from the 1947 Act. Not resolved.</li>
<li>Whether a 15% band for turnover above Rs 1 crore applied: two sources say so, three do not mention it.</li>
<li>Whether the Court found there was no conflict between the earlier judgements (the Supreme Court Observer judgement summary, CourtBook) or disposed of the reference because it was academic (all reports): the two statements are both reported and may be two limbs of one reasoning.</li>
<li>The number of connected appeals, the States concerned and the money in dispute.</li>
<li>The 30 November 2026 hearing: not found in any source; the case was decided on 4 November.</li>
<li>Whether Hoechst Pharmaceuticals and India Cement are cited by the reports as three-judge and seven-judge decisions respectively with the year of each: the years were not stated in the text read, so none is given here.</li>
</ul></details>
'''

body = STYLE + top + status + q + s1 + s2 + stakes + fixes + method + gaps

SOURCES = (
    '<a href="https://www.scobserver.in/cases/states-power-to-impose-taxes-based-on-annual-turnover-arjun-flour-mills-v-state-of-orissa/">Supreme Court Observer, case page: States&rsquo; power to impose taxes based on annual turnover</a> (secondary; page status not updated after disposal); '
    '<a href="https://www.scobserver.in/reports/sc-disposes-reference-on-states-power-to-impose-a-surcharge-on-sales-tax/amp/">Supreme Court Observer, 4 November 2026</a> and '
    '<a href="https://www.scobserver.in/reports/states-power-to-impose-tax-on-annual-turnover-judgement-summary/">judgement summary, 5 November 2026</a> (secondary); '
    '<a href="https://www.livelawbiz.com/gst/supreme-court/states-power-to-levy-additional-sales-tax-academic-after-gst-supreme-court-disposes-of-27-year-old-reference-557242">LiveLaw, 4 November 2026</a> (secondary); '
    '<a href="https://courtbook.in/posts/supreme-court-reaffirms-states-power-to-levy-additional-sales-tax-holds-27-year-old-reference-infructuous-after-gst">CourtBook, 4 November 2026</a> (secondary); '
    '<a href="https://www.business-standard.com/amp/economy/news/sc-sales-tax-ruling-what-it-means-for-businesses-with-old-tax-disputes-126110501383_1.html">Business Standard, 5 November 2026</a> (secondary). '
    'Intervals and the levy illustration computed by this blog. Analysed 25 November 2026.')
RELATED = [("https://blog.vertistratsolution.com/2026/08/fuel-and-bottle-two-taxes-states-never.html", "Fuel and liquor taxes: over a third of Indian states' own-tax revenue, outside GST"),
           ("https://blog.vertistratsolution.com/2026/08/who-collects-indias-gst-and-who.html", "India's GST by state: 5 states generate over 40% and get a fraction back")]

step(4, "assembling")
build("Law &middot; Supreme Court", TITLE,
      "A seven-judge bench ended a 27-year reference on whether a state can levy an additional sales tax by turnover; this piece sets out the question, the statute, the steps and what remains open.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
step(5, "done")
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
