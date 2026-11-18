"""Delimitation-linked Constitution amendment: the 17 April 2026 vote, the numbers needed, session mechanics and seat proposals (to 18 Nov 2026).
Build from the repo root:  python3 out/research/special-session-2026/build.py   (writes out/post-delimitation-amendment-votes-needed-winter-session-2026.html). Analysed 18 November 2026."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402
import math

OUT = ROOT / "out/post-delimitation-amendment-votes-needed-winter-session-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- 17 April 2026 vote (New Indian Express, 13 Nov 2026) ----
FOR, AGAINST = 298, 230
VOTING = FOR + AGAINST
NEED_VOTING = math.ceil(2 * VOTING / 3)
SHORT_APRIL = NEED_VOTING - FOR
assert VOTING == 528 and NEED_VOTING == 352 and SHORT_APRIL == 54
assert round(100 * FOR / VOTING, 1) == 56.4
# ---- Now (PTI, 15 Nov 2026): House of 543 with 3 vacancies = 540 members; 361 votes needed; NDA 320 ----
MEMBERS, NEED_NOW, NDA = 540, 361, 320
assert math.ceil(2 * MEMBERS / 3) == 360 and NEED_NOW == 361          # PTI's 361 is above 2/3 of 540 (360); the Constitution requires two-thirds of members present and voting plus a majority of total membership
assert NEED_NOW - NDA == 41
MAJ_TOTAL = MEMBERS // 2 + 1
assert MAJ_TOTAL == 271
FIFTEEN_ABOVE = NDA + 15
assert FIFTEEN_ABOVE == 335                                            # "a margin of 15 to 18 votes" is a margin over the threshold on the votes cast, not above NDA strength
# ---- Seats (PTI, TNIE): 543 now; maximum 850; proposal to raise every state's seats by 50% ----
SEATS, MAXSEATS = 543, 850
HALF_UP = SEATS * 1.5
assert round(HALF_UP, 1) == 814.5 and round(100 * (MAXSEATS / SEATS - 1), 1) == 56.5
assert HALF_UP < MAXSEATS
# ---- Session mechanics ----
ADJ, DAYS_UNPROROGUED_NOV15, OLD_RECORD = "13 Aug 2026", 94, 87
assert DAYS_UNPROROGUED_NOV15 - OLD_RECORD == 7
NOTICE_EXTENDED, NOTICE_NEW = 2, 14

TITLE = "Delimitation bill: 298 votes in April, 361 needed now, NDA holds 320 seats"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    ("298 to 230", " was the Lok Sabha vote on 17 April 2026 on the Constitution (131st Amendment) Bill, short of the two-thirds needed: 352 of the 528 who voted."),
    ("41 votes", " is the gap between the 361 votes PTI says are needed in the 540-member House and the 320 seats of the ruling NDA; government sources say the Bill would pass by 15 to 18 votes."),
    ("94 days", " is how long the Monsoon Session had stayed unprorogued by 15 November, a record, which lets Parliament be recalled on two days&rsquo; notice instead of 14."),
])

s1 = insight(
    "The April vote fell 54 short of two-thirds; 41 votes beyond NDA seats are needed now",
    bars("The 17 April Constitution amendment drew 298 votes against 352 needed from those voting",
         [("Votes in favour, 17 April", FOR), ("Votes against, 17 April", AGAINST), ("Two-thirds of those voting, 17 April", NEED_VOTING), ("NDA seats, November", NDA), ("Votes PTI says are needed now", NEED_NOW)],
         accent="Votes in favour, 17 April", unit=" votes",
         sub="Lok Sabha votes. A Constitution amendment needs a majority of the total membership and two-thirds of members present and voting.",
         source="New Indian Express, 13 November 2026 (vote); PTI via The Economic Times and ThePrint, 15 November 2026 (361; 320; 540 members).")
    + numbers(["Item", "Figure", "Note"],
              [["Vote on 17 April", "298 for, 230 against", "total 528 voting"], ["Two-thirds of 528", "352", "computed here: 54 more than the votes in favour"],
               ["House strength now", "540 members, 3 vacancies", "PTI"], ["Votes PTI says are needed", "361", "two-thirds of 540 is 360; attendance changes the figure"],
               ["NDA strength", "320", "PTI; BJP sources say 320 in the Lok Sabha and 155 in the Rajya Sabha"], ["Gap to 361", "41", "computed here"]]),
    "The number of votes needed depends on attendance, because the test is two-thirds of those present and voting, so a government with 320 seats needs either opposition support or absences, and the 15 to 18 vote margin that officials cite cannot be checked until attendance is known.",
    "The Lok Sabha Secretariat should publish before the vote the number of members expected present and the two-thirds figure it implies, so that the margin claimed can be checked against the rule.",
    "votes")

s2 = insight(
    "The session is unprorogued at 94 days, a record, so a recall needs two days' notice",
    flow([("13 Aug 2026", "The Monsoon Session was adjourned sine die and not prorogued."),
          ("12 Nov 2026", "91 days unprorogued, passing the earlier record of 87 days set in 2008.", True),
          ("15 Nov 2026", "94 days; reports say the Winter Session is likely in the first week of December. One report puts it from 1 to 19 December and BJP sources named 30 November or 4 December."),
          ("Notice rules", "An extended sitting of the existing session needs at least 2 days&rsquo; notice; a fresh session needs at least 14.")]),
    "Keeping the session open lets the government choose between a special sitting and the Winter Session, and an NDA ally was told that the Winter Session was the more likely route.",
    "The government should announce the date and the list of business of the next sitting with at least the 14 days that a fresh session gives, so that members can examine a Constitution amendment.",
    "mechanics")

s3 = insight(
    "The proposal would raise the Lok Sabha from 543 to as many as 850 seats",
    bars("A 50% rise gives about 815 seats; the Bill's ceiling is 850, 56.5% above today's 543",
         [("Seats now", SEATS), ("If every state's seats rise 50% (computed)", round(HALF_UP)), ("Maximum in the Bill", MAXSEATS)],
         accent="Maximum in the Bill", unit=" seats",
         sub="Lok Sabha seats. Reports say the plan keeps each state's share fixed at the 1971 Census basis; no final decision has been taken.",
         source="PTI via ThePrint, 15 November 2026; Indian Express, 13 November 2026; New Indian Express, 16 November 2026.")
    + numbers(["Item", "Detail"],
              [["Package", "Constitution amendment, a Delimitation Bill and a Union Territories Laws (Amendment) Bill"], ["Purpose", "33% reservation for women in the Lok Sabha and assemblies before the 2029 election"],
               ["Seats", "543 now; maximum 850"], ["Concern", "southern states fear loss of share under a population-based redistribution"],
               ["Related", "the One Nation One Election JPC (129th Amendment Bill) has until the first day of the last week of the Winter Session to report"]]),
    "A 50% rise for every state would keep each state&rsquo;s share unchanged, which answers the southern states&rsquo; main objection, but it leaves open how the 33% reservation is allocated across the extra seats.",
    "The government should publish the seat table by state under the proposal before the vote, so that members can compare each state&rsquo;s share with the 1971 base.",
    "seats")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Lok Sabha Secretariat:</b> publish the expected attendance and the two-thirds figure it implies before a Constitution amendment vote.</li>
<li><b>Ministry of Parliamentary Affairs:</b> announce the sitting dates with at least 14 days&rsquo; notice for a Constitution amendment.</li>
<li><b>Ministry of Law and Justice:</b> publish the state-wise seat table and the allocation of women&rsquo;s seats under the proposal.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''
method = '''<details class="xv-n"><summary>Method and definitions</summary><ul>
<li>A Constitution amendment needs a majority of the total membership of each House and two-thirds of members present and voting; it cannot be passed in a joint sitting.</li>
<li>Two-thirds of 528 voting is 352 after rounding up; two-thirds of 540 members is 360, and PTI&rsquo;s 361 is as reported.</li>
<li>The 50% seat figure is 543 times 1.5 and is a computation, not a figure from a bill text.</li></ul></details>
'''
gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary><ul>
<li>Whether a special sitting will be held: no date has been announced and the Opposition says it has not been consulted.</li>
<li>The text of the revised proposal: reports describe it, and no bill text was read.</li>
<li>The Winter Session dates: a headline says 1 to 19 December, BJP sources said 30 November or 4 December, and PTI says the first week of December.</li>
<li>Whether the votes that officials expect will turn up; the outcome depends on attendance and on parties outside the NDA.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + fixes + method + gaps
SOURCES = ('<a href="https://www.newindianexpress.com/india/2026/Nov/13/no-information-on-special-parliament-session-on-delimitation-priyanka-says-opposition-not-consulted">New Indian Express, 13 November 2026</a> (17 April vote; unprorogued 91 days); '
  '<a href="https://m.economictimes.com/news/india/winter-session-likely-in-first-week-of-december-govt-may-push-womens-quota-bill/amp_articleshow/135852937.cms">Economic Times (PTI), 15 November 2026</a> and <a href="https://theprint.in/india/winter-session-likely-in-first-week-of-december-govt-may-push-womens-quota-bill/3099342/">ThePrint (PTI)</a>; '
  '<a href="https://indianexpress.com/article/political-pulse/modi-government-special-parliament-session-womens-quota-delimitation-10960897">Indian Express, 13 November 2026</a>; '
  '<a href="http://indianexpress.com/article/explained/explained-politics/parliament-special-session-features-process-delimitation-10961393">Indian Express explained, 13 November 2026</a>; '
  '<a href="https://www.newindianexpress.com/story/india/2026/nov/16/crucial-bills-lined-up-for-winter-session-in-december-first-week">New Indian Express, 16 November 2026</a>; '
  '<a href="https://www.newindianexpress.com/india/2026/Jul/29/lok-sabha-panel-on-one-nation-one-election-gets-extension-till-winter-session">New Indian Express, 29 July 2026</a> (JPC extension); '
  '<a href="https://prsindia.org/billtrack/the-constitution-one-hundred-and-twenty-ninth-amendment-bill-2024">PRS, Constitution (129th Amendment) Bill, 2024</a>. Computed by this blog. Analysed 18 November 2026.')
RELATED = [(f"{B}/2026/08/lok-sabha-question-registry-1843-scheme.html", "Parliament questions on schemes: 3,773 in Lok Sabha and Rajya Sabha, 2019-2026"),
           (f"{B}/2026/08/the-most-discussed-schemes-in.html", "Schemes most discussed in Parliament: 51 actively monitored, 10 never questioned"),
           (f"{B}/2026/10/how-to-use-lok-rajya-sabha-qa-see-which.html", "How to use lok-rajya-sabha-qa: see which parties and ministries Parliament questions")]
build("Policy &middot; Parliament", TITLE, "The delimitation-linked amendment failed on 17 April with 298 votes; 361 are needed now against 320 NDA seats, and the unprorogued session lets Parliament be recalled on two days' notice.", body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE))
