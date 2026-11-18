"""Foreign Contribution (Regulation) Amendment Bill 2026: what it does, the issues PRS flags, and committee status (to 18 Nov 2026).
Build from the repo root:  python3 out/research/fcra-2026/build.py   (writes out/post-fcra-amendment-bill-2026-designated-authority.html). Analysed 18 November 2026."""
import pathlib, sys
from datetime import date
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-fcra-amendment-bill-2026-designated-authority.html"
B = "https://blog.vertistratsolution.com"

JAIL_NOW, JAIL_BILL = 5, 1
assert JAIL_NOW - JAIL_BILL == 4
INTRO, JC_REF, HEARING, DELIB = date(2026, 3, 25), date(2026, 8, 12), date(2026, 11, 12), date(2026, 11, 19)
assert (JC_REF - INTRO).days == 140 and (DELIB - JC_REF).days == 99 and (DELIB - HEARING).days == 7
# The joint committee has 31 Rajya Sabha members listed from number 24 onward; membership total not established here.

TITLE = "FCRA Amendment Bill 2026: a new authority takes assets, jail cut to 1 year"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    ("1 year", " would be the maximum jail term for violating the Act under the Bill, down from 5 years; a Designated Authority would take over assets of organisations whose FCRA certificate ends."),
    ("No appeal", " is provided in the Act or the Bill when the government refuses to renew a certificate, and no hearing before refusal, according to PRS."),
    ("19 November", " is the date of the next Joint Committee sitting, with the Home and Law ministries; the committee heard stakeholders including Oxfam International and a law-firm chairman on 12 November."),
])

s1 = insight(
    "The Bill cuts the maximum jail term from 5 years to 1 and adds asset vesting",
    bars("The maximum jail term for violating the FCRA falls from 5 years to 1 under the Bill",
         [("Maximum imprisonment now", JAIL_NOW), ("Maximum imprisonment under the Bill", JAIL_BILL)],
         accent="Maximum imprisonment under the Bill", unit=" years",
         sub="Years of imprisonment, the maximum for violation of the Act. The Bill adds a Designated Authority to supervise, manage and dispose of assets and foreign contribution.",
         source="PRS Legislative Research, The Foreign Contribution (Regulation) Amendment Bill, 2026, Highlights.")
    + numbers(["Feature", "Detail"],
              [["When assets vest", "when a certificate is cancelled, surrendered, or renewal is not applied for or is denied"], ["Who takes them", "a Designated Authority for vesting, supervision, management and disposal"],
               ["Places of worship", "the Authority must maintain the religious character"], ["Penalty", "maximum imprisonment reduced from 5 years to 1 year"]]),
    "The lower jail term and the new asset provisions cut in different directions, since an organisation that stops renewing loses assets that foreign funds paid for, even if it breaks no rule.",
    "The Home Ministry should state how many organisations would have assets vested under the Bill in the last five years of certificate cancellations and non-renewals.",
    "bill")

s2 = insight(
    "PRS flags four issues: asset loss on exit, unequal treatment, no appeal and no hearing",
    flow([("Loss of assets on cessation", "An organisation that has not renewed would see assets created from past foreign funds vested in the Designated Authority.", True),
          ("No clean exit", "An organisation cannot leave the FCRA framework without losing assets built with foreign funds, so it has to keep renewing, and the Rules add spending obligations."),
          ("Different routes", "The Bill may treat assets created by certificate holders differently from those created through the prior-permission route."),
          ("No appeal or hearing", "Neither the Act nor the Bill provides an appeal when renewal is denied, or a hearing before denial.")]),
    "Each of the four points concerns what happens to an organisation after a decision by the government, and in each the Bill supplies a consequence without supplying a remedy.",
    "The Joint Committee should ask the Home Ministry to table the renewal-refusal numbers and the stated reasons for them, since the Bill&rsquo;s effect depends on how often renewal is denied.",
    "issues")

s3 = insight(
    "The Bill has been with a joint committee for 99 days; it sits again on 19 November",
    flow([("25 Mar 2026", "Introduced in the Lok Sabha."), ("12 Aug 2026", "Referred to a Joint Parliamentary Committee.", True),
          ("12 Nov 2026", "The committee heard stakeholders, among them Amitabh Behar of Oxfam International and Dr Shardul S. Shroff of Shardul Amarchand Mangaldas."),
          ("19 Nov 2026", "Deliberations with the Ministry of Home Affairs and the Ministry of Law and Justice.")]),
    "A committee that has met stakeholders on 12 November and the ministries on 19 November is at the stage of taking evidence, and its report date was not found.",
    "The committee should publish the written submissions it receives, so that the organisations the Bill affects can see what has been argued.",
    "committee")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Home Affairs:</b> publish yearly counts of FCRA certificates cancelled, surrendered, not renewed and denied, with the assets and funds involved.</li>
<li><b>Joint Committee:</b> publish stakeholder submissions and the ministry replies.</li>
<li><b>Parliament:</b> consider an appeal and a hearing before denial of renewal, as PRS notes neither exists.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''
method = '''<details class="xv-n"><summary>Method and definitions</summary><ul>
<li>FCRA is the Foreign Contribution (Regulation) Act. The Bill&rsquo;s provisions and the issues listed are as summarised by PRS Legislative Research.</li>
<li>Day counts are between the dates on PRS&rsquo;s bill page and the committee schedule.</li></ul></details>
'''
gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary><ul>
<li>The size of the problem the Bill addresses: no count of organisations that would be affected was found.</li>
<li>The Bill&rsquo;s text beyond the PRS highlights and issues.</li>
<li>The committee&rsquo;s report date and membership; only part of the member list was read.</li>
<li>What the stakeholders said on 12 November; only their names are published.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + fixes + method + gaps
SOURCES = ('<a href="https://prsindia.org/billtrack/the-foreign-contribution-regulation-amendment-bill-2026">PRS, The Foreign Contribution (Regulation) Amendment Bill, 2026</a>; '
  '<a href="http://prsindia.org/parliamentary-committees/joint-committee-on-the-foreign-contribution-regulation-amendment-bill-2026">PRS, Joint Committee on the Bill (schedule and members)</a>. Day counts computed by this blog. Analysed 18 November 2026.')
RELATED = [(f"{B}/2026/10/states-won-right-to-tax-mines-in-2024.html", "Mining taxes: MMDR Amendment Act 2026 cancels up to Rs 2 lakh crore of state dues"),
           (f"{B}/2026/11/doubling-indias-csr-profit-trigger.html", "Doubling India's CSR trigger: 11,204 companies released, about 3% of the money")]
build("Policy &middot; Civil society", TITLE, "The FCRA Amendment Bill 2026 would vest assets of organisations that lose their certificate in a Designated Authority and cut the maximum jail term from 5 years to 1.", body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE))
