"""Corporate Laws (Amendment) Bill 2026: what the Bill changes and what the Joint Parliamentary Committee recommended (report of 3 Aug 2026).
Build from the repo root:  python3 out/research/corporate-laws-2026/build.py   (writes out/post-corporate-laws-amendment-bill-2026-jpc-changes.html). Analysed 18 November 2026."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-corporate-laws-amendment-bill-2026-jpc-changes.html"
B = "https://blog.vertistratsolution.com"

# ---- Thresholds (PRS bill page and JPC summary), Rs crore ----
SMALL_CAP_OLD, SMALL_CAP_NEW = 10, 20          # upper limit for the prescribed paid-up share capital of a small company
SMALL_TO_OLD, SMALL_TO_NEW = 100, 200          # upper limit for the prescribed turnover
CSR_OLD, CSR_NEW = 5, 10                       # net profit trigger for CSR
assert SMALL_CAP_NEW == 2 * SMALL_CAP_OLD and SMALL_TO_NEW == 2 * SMALL_TO_OLD and CSR_NEW == 2 * CSR_OLD
# CSR: 2% of average net profit of the last three years; a company at the Rs 10 crore trigger would owe Rs 20 lakh
CSR_RATE = 2
OWED_NEW = 10 * CSR_RATE / 100          # Rs crore
OWED_OLD = 5 * CSR_RATE / 100
assert OWED_NEW == 0.2 and OWED_OLD == 0.1
# ---- Timeline ----
# Introduced Lok Sabha 23 Mar 2026 and referred to JPC (Chair Sudhir Gupta) the same day; report presented 3 Aug 2026 (PRS).
from datetime import date
D_INTRO, D_REPORT = date(2026, 3, 23), date(2026, 8, 3)
DAYS = (D_REPORT - D_INTRO).days
assert DAYS == 133

TITLE = "Corporate Laws (Amendment) Bill 2026: what the joint committee changed in August"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    ("Rs 10 crore", " is the net-profit trigger for CSR under the Bill, doubled from Rs 5 crore; the committee asked the government to give up the power to change it by rule."),
    ("Rs 200 crore", " is the turnover ceiling for a small company under the Bill, from Rs 100 crore, with paid-up capital raised from Rs 10 crore to Rs 20 crore."),
    ("133 days", " passed between introduction on 23 March 2026 and the committee report on 3 August; this piece did not establish whether the Bill has been passed."),
])

s1 = insight(
    "The Bill doubles the CSR profit trigger and two small-company limits",
    bars("CSR trigger, small-company capital and turnover ceilings each double under the Bill",
         [("CSR net-profit trigger, now", CSR_OLD), ("CSR net-profit trigger, Bill", CSR_NEW), ("Small-company capital ceiling, now", SMALL_CAP_OLD), ("Small-company capital ceiling, Bill", SMALL_CAP_NEW),
          ("Small-company turnover ceiling, now", SMALL_TO_OLD), ("Small-company turnover ceiling, Bill", SMALL_TO_NEW)],
         accent=["CSR net-profit trigger, Bill", "Small-company capital ceiling, Bill", "Small-company turnover ceiling, Bill"], unit="₹ crore",
         sub="Rs crore. The CSR duty is 2% of average net profit of the last three years for firms meeting a net worth, turnover or net-profit test.",
         source="PRS Legislative Research, Corporate Laws (Amendment) Bill 2026 page and Joint Committee report summary (31 August 2026).")
    + numbers(["Provision", "Now", "Bill", "Joint committee"],
              [["CSR net-profit trigger", "Rs 5 crore", "Rs 10 crore, revisable by the central government", "delete the power to revise"],
               ["Small company: paid-up capital", "up to Rs 50 lakh, or a higher prescribed amount up to Rs 10 crore", "up to Rs 20 crore", "not covered in the extract read"],
               ["Small company: turnover", "up to Rs 2 crore, or a higher prescribed amount up to Rs 100 crore", "up to Rs 200 crore", "not covered in the extract read"],
               ["Annual general meeting", "&ndash;", "physical, video or audio-visual; physical at least once in three years", "&ndash;"],
               ["Offences", "criminal", "civil penalties for several offences, including contravention of rules", "&ndash;"]]),
    "At the new trigger a company would owe Rs 20 lakh a year in CSR instead of Rs 10 lakh at the old one, so the change releases small firms from a small sum and the question is how many firms and how much money it covers.",
    "The Ministry of Corporate Affairs should publish the number of companies and the CSR amount that the Rs 10 crore trigger and the exemption power would remove from the obligation, before the Bill is passed.",
    "thresholds")

s2 = insight(
    "The committee asked to delete three delegated powers and narrow the auditor exemption",
    flow([("CSR threshold", "The Bill lets the government revise the Rs 10 crore trigger by rule. The committee recommended removing that power."),
          ("CSR exemption for classes of companies", "The committee said the provision lacks statutory guidance and amounts to excessive delegation."),
          ("Fit-and-proper director test", "The Bill bars a person the board has not assessed as fit and proper. The committee called the delegated power excessively broad and recommended deleting the amendment.", True),
          ("NFRA investigations", "The Bill lets NFRA make regulations on how it investigates. The committee recommended deleting this and keeping the government&rsquo;s power to prescribe by rule."),
          ("Auditor exemption", "The Bill exempts classes of companies from appointing an auditor. The committee recommended limiting it to private companies."),
          ("NCLT benches", "The committee recommended dedicated benches for the Insolvency and Bankruptcy Code, so that statutory timelines are kept.")]),
    "Four of the six items concern rule-making power that the Bill would hand to the government, boards or NFRA, and the committee asked for narrower discretion in each, so the Bill would return with less delegation than it left with.",
    "The Ministry of Corporate Affairs should state which of the committee&rsquo;s recommendations it accepts and publish the revised text before the Bill is taken up again.",
    "jpc")

s3 = insight(
    "The Bill went to a joint committee on introduction and came back 133 days later",
    flow([("23 Mar 2026", "Introduced in the Lok Sabha and referred to the Joint Parliamentary Committee, chaired by Sudhir Gupta."),
          ("3 Aug 2026", "The committee presented its report.", True),
          ("13 Aug 2026", "The Monsoon Session of Parliament was adjourned sine die; the session was still not prorogued on 15 November."),
          ("First week of December 2026", "The Winter Session is expected to begin; the Bill&rsquo;s place in its business was not established.")]),
    f"A committee that took {DAYS} days produced a report with changes to the Bill, so the next question is whether the government will bring the Bill back with them.",
    "Parliament&rsquo;s business bulletin should list the Bill and the changes proposed by the committee at the start of the Winter Session, so that the date can be tracked.",
    "timeline")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Corporate Affairs:</b> publish the count of companies and the CSR rupees that the new trigger and exemption power would remove.</li>
<li><b>Ministry of Corporate Affairs:</b> publish its response to each committee recommendation with the revised clause text.</li>
<li><b>Lok Sabha Secretariat:</b> publish the Bill&rsquo;s status in the Winter Session list of business.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''
method = '''<details class="xv-n"><summary>Method and definitions</summary><ul>
<li>CSR is corporate social responsibility spending of 2% of average net profit over three years under the Companies Act, 2013.</li>
<li>The thresholds are those printed in PRS&rsquo;s bill page and summaries; the owed amount is 2% of the trigger profit.</li>
<li>The committee items are those in the part of the PRS summary read; the summary has more.</li></ul></details>
'''
gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary><ul>
<li>Whether the Bill has been passed by either House.</li>
<li>The committee&rsquo;s recommendations beyond those in the extract of the PRS summary read.</li>
<li>How many companies the CSR trigger and the small-company limits would affect.</li>
<li>The Winter Session dates: reports say the first week of December, and one headline says 1 to 19 December.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + fixes + method + gaps
SOURCES = ('<a href="https://prsindia.org/billtrack/the-corporate-laws-amendment-bill-2026">PRS, The Corporate Laws (Amendment) Bill, 2026</a>; '
  '<a href="https://prsindia.org/files/bills_acts/bills_parliament/2026/JPC_Report_Summary_Corporate_Laws_%28A%29_Bill_2026.pdf">PRS, JPC report summary, 31 August 2026</a>; '
  '<a href="https://prsindia.org/policy/monthly-policy-review/august-2026">PRS, Monthly Policy Review, August 2026</a>; '
  '<a href="https://theprint.in/india/winter-session-likely-in-first-week-of-december-govt-may-push-womens-quota-bill/3099342/">ThePrint (PTI), 15 November 2026</a> (session not prorogued). Computed by this blog. Analysed 18 November 2026.')
RELATED = [(f"{B}/2026/11/doubling-indias-csr-profit-trigger.html", "Doubling India's CSR trigger: 11,204 companies released, about 3% of the money"),
           (f"{B}/2026/10/states-won-right-to-tax-mines-in-2024.html", "Mining taxes: MMDR Amendment Act 2026 cancels up to Rs 2 lakh crore of state dues"),
           (f"{B}/2026/10/the-rbi-has-put-bonds-and-rupees-on-one.html", "RBI's Unified Markets Interface: pilots settled Rs 1,025 crore of tokenised corporate bonds")]
build("Policy &middot; Companies", TITLE, "The joint committee on the Corporate Laws (Amendment) Bill 2026 asked the government to drop three delegated powers, after a Bill that doubles the CSR trigger to Rs 10 crore.", body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE))
