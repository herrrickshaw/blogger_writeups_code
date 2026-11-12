"""Lawyers and AI, as of 12 November 2026. Build: PYTHONPATH=tools/postbuild python3 out/research/legal-ai-2026/build_legal_ai.py
Every figure is from the source named next to it; vendor-run surveys are labelled as such in the text."""
import sys
sys.path.insert(0, 'tools/postbuild')
from buildpost import build

OUT = 'out/post-lawyers-and-ai-india-2026.html'

# --- Adoption (Thomson Reuters 2026 AI in Professional Services Report; vendor)
TR_FIRM_25, TR_FIRM_26 = 28, 41          # % of law firms using GenAI organisation-wide
TR_INHOUSE_25, TR_INHOUSE_26 = 23, 47
TR_SHADOW = 34                            # Future of Professionals 2026: use AI the firm has not sanctioned

# --- Money
HARVEY = [("Jun 2025", 5.0), ("Dec 2025", 8.0), ("Mar 2026", 11.0), ("Sep 2026", 15.5)]   # $ bn; first two via Sacra
LEGORA_BN = 8.8                           # 21 Oct 2026, Reuters
COMBINED = HARVEY[-1][1] + LEGORA_BN
assert round(COMBINED, 1) == 24.3
HOURLY_SH = 90                            # TR Legal Tracker: share of legal spend billed hourly

# --- Fake citations (Damien Charlotin's AI Hallucination Cases database)
DB_TOTAL, DB_JAN = 2292, 719              # 12 Nov 2026; Jan 2026 via HAQQ's tracker
IN_ENTRIES = 16
IN_PARTY = [("Judge, tribunal or adjudicating officer", 10), ("Lawyer", 3), ("Litigant in person", 2),
            ("Tax assessing officer (filed as &ldquo;expert&rdquo;)", 1)]
assert sum(v for _, v in IN_PARTY) == IN_ENTRIES
IN_BENCH = IN_PARTY[0][1] + IN_PARTY[3][1]
assert IN_BENCH == 11

# --- Accuracy (Stanford RegLab, Journal of Empirical Legal Studies 2025)
STANFORD = [("Lexis+ AI", 17), ("Ask Practical Law AI", 17), ("Westlaw AI-Assisted Research", 33), ("GPT-4 (general model)", 43)]


def tw(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def hbars(title, sub, rows, fmt, source, colour="#0b3d6b", L=170, aria=""):
    W, R, top, bh, gap = 340, 300, 44, 18, 8
    H = top + len(rows) * (bh + gap) + 24
    mx = max(v for _, v in rows)
    sc = (R - L) / mx
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="{aria}">',
         f'<text x="4" y="13" font-size="13" fill="#495057">{title}</text>',
         f'<text x="4" y="30" font-size="11" fill="#6c757d">{sub}</text>']
    for i, (lab, v) in enumerate(rows):
        y = top + i * (bh + gap)
        w = max(v * sc, 2)
        s.append(f'<text x="{L - 6}" y="{y + bh / 2 + 4:.1f}" font-size="11" fill="#212529" text-anchor="end">{lab}</text>')
        s.append(f'<rect x="{L}" y="{y}" width="{w:.1f}" height="{bh}" fill="{colour}"/>')
        if w > 40:
            s.append(f'<text x="{L + w - 5:.1f}" y="{y + bh / 2 + 4:.1f}" font-size="11.5" fill="#fff" text-anchor="end">{fmt(v)}</text>')
        else:
            s.append(f'<text x="{L + w + 5:.1f}" y="{y + bh / 2 + 4:.1f}" font-size="11.5" fill="#212529">{fmt(v)}</text>')
    s.append(f'<text x="4" y="{H - 6}" font-size="10" fill="#6c757d">{source}</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


chart_india = hbars("Who put the fake law in the record: India", f"Indian entries in the AI Hallucination Cases database ({IN_ENTRIES})",
                    [("Judge, tribunal, officer", 10), ("Tax assessing officer", 1), ("Lawyer", 3), ("Litigant in person", 2)],
                    lambda v: str(v), "Source: Damien Charlotin, AI Hallucination Cases database, India filter", colour="#a5402c", L=150,
                    aria="Indian entries in the AI Hallucination Cases database by who relied on the fabricated material: judge, tribunal or adjudicating officer 10; tax assessing officer 1; lawyer 3; litigant in person 2.")
chart_harvey = hbars("Harvey&rsquo;s valuation", "US$ billion, at each funding round",
                     HARVEY, lambda v: f"${v:g} bn", "Source: Harvey (Mar, Sep 2026); Sacra (2025 rounds)", L=90,
                     aria="Harvey's valuation at each funding round: June 2025 5 billion dollars, December 2025 8 billion, March 2026 11 billion, September 2026 15.5 billion.")
chart_stanford = hbars("How often legal research AI got it wrong", "Share of test queries with a hallucinated answer, %",
                       STANFORD, lambda v: f"{v}%", "Source: Stanford RegLab, J. Empirical Legal Studies (2025)", L=165, colour="#495057",
                       aria="Hallucination rates in Stanford RegLab's test: Lexis+ AI 17%, Ask Practical Law AI 17%, Westlaw AI-Assisted Research 33%, GPT-4 43%.")

surveys = tw(["Survey (who ran it)", "Sample and fieldwork", "Headline finding"], [
    ["Thomson Reuters, AI in Professional Services 2026 (vendor)", "1,500+ professionals; late 2025",
     f"{TR_FIRM_26}% of law firms use GenAI organisation-wide, up from {TR_FIRM_25}%; corporate legal teams {TR_INHOUSE_26}%, up from {TR_INHOUSE_25}%"],
    ["Clio Legal Trends 2026 (vendor, US)", "Sample not stated; Oct 2026", "85% report some AI use at their firm, up from 79%"],
    ["8am Legal Industry Report 2026 (vendor)", "1,300 respondents", "69% personally use general AI at work, up from 31%; 34% report firm-wide adoption"],
    ["LexisNexis (vendor)", "543 lawyers; Sept 2026", "94% use AI for legal work, 34% daily; 83% worry about fabricated information"],
    ["Wolters Kluwer Future Ready Lawyer 2026 (vendor)", "810 lawyers, US, China, Europe; Aug 2025", "More than 90% use at least one AI tool"],
    ["ABA Legal Technology Survey (bar association)", "Survey of 2024, published 2025", "30% of offices use AI tools, up from 11%; 46% at firms of 100+ lawyers"],
    ["Manupatra, India (vendor)", "227 respondents; May 2025", "About 60% used AI in the past year; 4.1% fully trust its output; 11% have written AI policies"],
])

stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{TR_FIRM_25}% &rarr; {TR_FIRM_26}%</b><span>law firms using generative AI organisation-wide, in one year (Thomson Reuters, a vendor)</span></div>
<div class="gb-stat"><b>${COMBINED:.1f} bn</b><span>combined valuation of Harvey and Legora, the two legal-AI firms India&rsquo;s biggest law firms chose</span></div>
<div class="gb-stat"><b>{DB_TOTAL:,}</b><span>court decisions worldwide dealing with AI-fabricated or misused law, up from about {DB_JAN} in January</span></div>
<div class="gb-stat"><b>{IN_BENCH} of {IN_ENTRIES}</b><span>Indian entries where the fake law was relied on by a judge, tribunal or tax officer, not a lawyer</span></div>
</div>'''

body = f"""{stats}

<p>Lawyers are taking up generative AI quickly, at about the same pace as other professions. Thomson Reuters, which sells AI research tools to lawyers, found that {TR_FIRM_26}% of law firms used it across the organisation in its latest survey, against {TR_FIRM_25}% a year earlier. Investors have followed: Harvey and Legora, the two best-funded legal-AI start-ups, were valued at a combined ${COMBINED:.1f} billion in autumn 2026. India&rsquo;s largest law firms signed up in 2025.</p>

<p>The failure record has grown alongside. A public database of court decisions that deal with AI-fabricated or misused law had {DB_TOTAL:,} entries on 12 November 2026. India&rsquo;s entries have an unusual shape. Elsewhere it is mostly lawyers and litigants who are caught. In India, {IN_BENCH} of the {IN_ENTRIES} entries trace the fake law to a judge, a tribunal or a tax officer. In July the Supreme Court declared &ldquo;zero tolerance&rdquo; for unverified AI precedents from both the Bar and the Bench, and told the Bar Council of India to work out rules for lawyers. This blog found no such rules yet.</p>

<h2 class="gb-h2">How many lawyers use it</h2>
<p>Every recent survey finds that most lawyers now use AI in some form, but the figures range from about 30% to 94%. Most of that gap comes from what is being counted. Some surveys ask whether a lawyer personally uses a tool, some whether anyone at the firm does, and some whether the firm has rolled one out everywhere. Most are run by companies that sell legal software, and some sample their own customers. The one bar-association survey is the oldest and the lowest.</p>
{surveys}
<p>Two findings recur whoever runs the survey. Use is highest for legal research and drafting: in the Thomson Reuters data, 80% of legal users use it for research. And use runs ahead of policy. Thomson Reuters&rsquo; survey of law-firm professionals found {TR_SHADOW}% using AI tools their firm had not sanctioned. Clio&rsquo;s 2025 report found 53% of respondents saying their firm had no AI policy, or that they did not know of one. In India, Manupatra&rsquo;s small survey found 11% with written policies.</p>

<h2 class="gb-h2">The money, and the billable hour</h2>
<p>Harvey raised US$550 million in September 2026 at a valuation of $15.5 billion (Bloomberg put it at $15.6 billion). It says 80% of the 100 largest US law firms use it, and has been reported at more than $400 million in annual recurring revenue. Legora raised $550 million in October at $8.8 billion; its investor FirstMark puts its recurring revenue above $200 million. Clio, which sells practice-management software, bought the legal research firm vLex for $1 billion in November 2025.</p>
{chart_harvey}
<p>The evidence that AI is changing how lawyers are paid is thinner than the evidence that they use it. Thomson Reuters&rsquo; billing data show about {HOURLY_SH}% of legal spending still billed by the hour. In a November 2026 survey by Best Law Firms, 49% of firms said AI had had no effect on their billing, down from 58% a year earlier, and 25% said it had cut billable hours on some tasks. Clio projects billable time rising, not falling, to 42% of the working day in 2026 from 39% in 2025. Pressure is coming from clients instead. The New York Times reported in September that in-house teams were asking for 20&ndash;30% off bills, and some companies&rsquo; billing guidelines now refuse to pay for AI-generated work at all. Zscaler&rsquo;s says the time and cost of AI-generated work &ldquo;shall not be passed on.&rdquo;</p>

<h2 class="gb-h2">India&rsquo;s firms chose in 2025</h2>
<p>India&rsquo;s largest firms made their choices within a few months of each other. Shardul Amarchand Mangaldas rolled out Harvey across its seven offices in June 2025, and AZB &amp; Partners did the same in September. Cyril Amarchand Mangaldas ran a pilot of three platforms with 380 lawyers and chose Legora firm-wide in July 2025, after earlier trying Harvey and the Indian tool Lucio. Trilegal uses Lucio alongside tools built in-house. Khaitan &amp; Co has its own tools and picked Atlas as its knowledge platform in June 2026. Harvey opened a Bengaluru office in July 2025.</p>
<p>Indian data on use beyond these firms is thin. The only survey this blog found is Manupatra&rsquo;s, of 227 respondents in May 2025, and it was run by a legal database company. About 60% had used AI tools in the past year, and only 4.1% said they fully trusted the output.</p>

<h2 class="gb-h2">In India, the fake law mostly came from the bench</h2>
<p>The researcher Damien Charlotin maintains the most widely cited record of court decisions that deal with AI-fabricated or misused legal material. It had {DB_TOTAL:,} entries worldwide on 12 November 2026, up from about {DB_JAN} in January according to HAQQ, a legal-AI firm that tracks it. Most entries are from the United States, and most involve lawyers or people representing themselves.</p>
<p>India&rsquo;s {IN_ENTRIES} entries look different. In 10, the material was relied on by a judge, tribunal or adjudicating officer, and in one more by a tax assessing officer, whom the database files under &ldquo;expert&rdquo;. Lawyers account for three and litigants in person for two. Two disputes appear twice, at different stages, so the entries cover 14 matters.</p>
{chart_india}
<p>The cases include an order of the income-tax tribunal in Bengaluru, dated December 2024, that was later withdrawn; a Bombay High Court ruling in October 2025 that quashed a tax assessment because the officer had relied on three judgments that do not exist; and a Supreme Court order in September 2026 that set aside a customs penalty resting on fabricated and misdescribed authorities. In the case that set the rule, <i>Pooja Ramesh Singh v. Jammu and Kashmir Bank</i> (2 July 2026), the National Company Law Tribunal had admitted an insolvency petition citing judgments that do not exist, and the appeal tribunal had upheld it. The tribunal&rsquo;s own affidavit said the precedents came from its own research, not from counsel.</p>
<p>The Supreme Court set both orders aside. It held that citing AI-generated judgments without verification is &ldquo;misconduct on the part of an advocate&rdquo;, that it is &ldquo;a serious lapse if a judge relies on&rdquo; such material, and that a decision resting on it is &ldquo;no decision in the eyes of the law.&rdquo; It declared &ldquo;zero tolerance for the Bar as well as the Bench&rdquo;, and directed the Bar Council of India to set up a committee on lawyers who submit such material. This blog found no Bar Council rule on advocates&rsquo; use of AI as of November 2026.</p>
<p>The courts are writing their own rules. The Kerala High Court told district judges in July 2025 that AI may not be used &ldquo;to arrive at any findings, reliefs, order or judgment.&rdquo; In June 2026 the Supreme Court published draft Regulations for Use of AI in Courts, which would create a national oversight body and an AI committee in every High Court. The Supreme Court Advocates-on-Record Association objected to the draft&rsquo;s requirement that lawyers disclose their AI use. Chief Justice Surya Kant said in August that the courts use AI for research, for translating judgments into 16 languages through SUVAS, and for chat interfaces.</p>

<h2 class="gb-h2">The record elsewhere</h2>
<p>The case that started the count, <i>Mata v. Avianca</i> in New York in June 2023, ended in a $5,000 fine. Penalties have since grown. In June 2026 a federal court in Mississippi sanctioned all four lawyers on both sides of <i>Withers v. City of Aberdeen</i>, cancelled the trial and barred two of them from practising before it for two years. In England, the High Court&rsquo;s <i>Ayinde</i> judgment of June 2025 found five fake cases in one set of pleadings; in a linked case, 18 of 45 citations did not exist. The Solicitors Regulation Authority received 42 reports of possible AI misuse in the year to July 2026 and issued a warning notice in August.</p>
<p>Judges use it too. In a random-sample survey of US federal judges by the New York City Bar, published in March 2026, more than 60% had used an AI tool, but only 22.4% used one weekly or daily. Two federal judges told the Senate in October 2025 that error-filled orders had come from AI use in their chambers. Judges in England and Wales have a secure Copilot, and guidance first issued in December 2023 and updated twice since.</p>

<h2 class="gb-h2">Why caution is not just conservatism</h2>
<p>The specialist tools are better than general chatbots but not reliable enough to skip checking. Stanford&rsquo;s RegLab tested the leading legal research products and found hallucinated answers in 17% to 33% of queries, against 43% for GPT-4 used directly. A 2026 follow-up on statutory surveys found the Westlaw and Lexis tools accurate 58% and 64% of the time.</p>
{chart_stanford}
<p>Firms are still working out the return. Thomson Reuters&rsquo; UK data found that only 18% of law firms measure the return on their AI tools. One English firm, Hill Dickinson, restricted staff access in February 2025 after logging more than 32,000 visits to ChatGPT in a week. And in LexisNexis&rsquo;s own survey, the one with the highest use figure (94%), 83% of lawyers worried about colleagues relying on fabricated information.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Bar Council of India should publish the rules the Supreme Court asked for in <i>Pooja Ramesh Singh</i>, with a date: a duty to verify every authority against an official source before filing, and a graded scale of discipline.</li>
<li>The Central Board of Indirect Taxes and Customs and the Central Board of Direct Taxes should require adjudicating and assessing officers to check every judgment they cite against an official database before an order issues, since quasi-judicial officers account for a large share of India&rsquo;s entries.</li>
<li>The Supreme Court should open a free, machine-readable citation lookup for its own judgments, so a filing, an order or an AI tool can check a citation automatically before it reaches a bench.</li>
<li>The Supreme Court should finalise its AI regulations with disclosure aimed at what a court needs to know, such as whether a cited authority was checked, rather than a blanket declaration of any AI use.</li>
<li>High Court and tribunal registries should run automated citation checks on filings and draft orders, as some commercial tools already do.</li>
<li>A body without a product to sell, such as the National Law School or the Bar Council, should run a regular survey of Indian lawyers&rsquo; AI use, since every current figure comes from vendors.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<ul>
<li>Whether the Bar Council of India has set up the committee the Supreme Court ordered in July 2026. No public record was found.</li>
<li>Whether the Supreme Court&rsquo;s draft AI regulations have been finalised. A secondary tracker described them as still in draft on 31 October 2026.</li>
<li>How many Indian lawyers use AI. No large survey that is not run by a vendor exists, and the one Indian survey found had 227 respondents.</li>
<li>Whether India&rsquo;s count is complete. The database relies on reports from volunteers, and its Indian entries predate two Bombay High Court customs rulings of October and November 2026 on fabricated citations. Its India filter showed {IN_ENTRIES} entries when checked.</li>
<li>Clio&rsquo;s 2026 sample size, which its release does not state.</li>
<li>Primary texts for AI rules reported at the Gujarat and Punjab &amp; Haryana High Courts.</li>
</ul>
"""

sources = ("Surveys: <a href=\"https://www.thomsonreuters.com/en/institute/reports/2026-ai-in-professional-services-report\">Thomson Reuters, 2026 AI in Professional Services Report</a> and "
           "<a href=\"https://legal.thomsonreuters.com/blog/how-ai-is-transforming-the-legal-profession\">summary</a>; "
           "<a href=\"https://www.thomsonreuters.com/en/institute/c/future-of-professionals-legal\">Future of Professionals 2026</a>; "
           "<a href=\"https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2026/05/State-of-the-UK-Legal-Market-2026.pdf\">State of the UK Legal Market 2026</a>; "
           "<a href=\"https://www.clio.com/about/press/2026-legal-trends-report/\">Clio 2026 Legal Trends</a>; "
           "<a href=\"https://www.americanbar.org/groups/law_practice/resources/law-technology-today/2026/difference-between-general-and-legal-specific-ai-tools\">8am report via ABA Law Technology Today</a>; "
           "<a href=\"https://www.lawnext.com/2025/03/aba-tech-survey-finds-growing-adoption-of-ai-in-legal-practice-with-efficiency-gains-as-primary-driver.html\">ABA Legal Technology Survey (LawNext)</a>; "
           "<a href=\"https://www.lexisnexis.com/community/pressroom/b/news/posts/lawyer-preference-for-ai-grounded-in-legal-sources-rises-to-81\">LexisNexis, 2 Sept 2026</a>; "
           "<a href=\"https://www.wolterskluwer.com/en/know/future-ready-lawyer-2026\">Wolters Kluwer Future Ready Lawyer 2026</a>; "
           "<a href=\"https://www.business-standard.com/content/press-releases-ani/manupatra-conducts-a-survey-on-ai-adoption-in-the-india-legal-landscape-first-of-its-kind-in-india-125060201166_1.html\">Manupatra survey</a>. "
           "Money and billing: <a href=\"https://www.harvey.ai/blog/harvey-raises-dollar550m-at-a-dollar155b-valuation-to-help-legal-teams-own-their-intelligence\">Harvey, Sept 2026</a>; "
           "<a href=\"https://www.bloomberg.com/news/articles/2026-09-09/legal-ai-startup-harvey-hits-15-6-billion-value-with-550-million-round\">Bloomberg</a>; "
           "<a href=\"https://thenextweb.com/news/harvey-550m-round-15-6bn-guardrails-acquisition\">TNW on Harvey revenue</a>; "
           "<a href=\"https://www.prnewswire.com/news-releases/harvey-raises-at-11-billion-valuation-to-scale-agents-across-law-firms-and-enterprises-302724309.html\">Harvey, Mar 2026</a>; "
           "<a href=\"https://sacra.com/c/harvey/\">Sacra (2025 rounds)</a>; "
           "<a href=\"https://www.reuters.com/legal/transactional/legal-ai-startup-legora-valued-88-billion-new-550-million-funding-round-2026-10-21\">Reuters on Legora</a>; "
           "<a href=\"https://firstmark.com/story/legora-raises-550m-series-e-at-an-8-8b-valuation-as-arr-tops-200m\">FirstMark</a>; "
           "<a href=\"https://www.clio.com/about/press/clio-completes-landmark-1b-vlex-acquisition-series-g-5b-valuation/\">Clio&ndash;vLex</a>; "
           "<a href=\"https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2026/01/2026-State-of-the-US-Legal-Market.pdf\">State of the US Legal Market 2026</a>; "
           "<a href=\"http://www.bestlawfirms.com/articles/law-firm-alternative-fee-arrangements-survey/8611\">Best Law Firms survey</a>; "
           "<a href=\"https://www.nytimes.com/2026/09/26/business/dealbook/ai-law-discount-billable-hour.html\">New York Times, 26 Sept 2026</a>; "
           "<a href=\"https://www.zscaler.com/legal/outside-counsel-billing-guidelines\">Zscaler billing guidelines</a>. "
           "India: <a href=\"https://www.amsshardul.com/sam-leads-indian-legal-market-with-rollout-of-harvey-ai-2/\">SAM</a>; "
           "<a href=\"https://www.barandbench.com/law-firms/corporate/azb-partners-announces-adoption-of-harvey-ai\">AZB (Bar &amp; Bench)</a>; "
           "<a href=\"https://www.cyrilshroff.com/wp-content/uploads/2025/07/CAM-Announcement-Legora.pdf\">CAM announcement</a>; "
           "<a href=\"https://trilegal.com/news-insights/how-this-law-firm-is-using-ai-to-streamline-legal-practices\">Trilegal</a>; "
           "<a href=\"https://www.atlasfuse.com/insights/news/khaitan-selects-atlas-as-its-intelligent-knowledge-platform-ai-legal\">Khaitan&ndash;Atlas</a>; "
           "<a href=\"https://www.harvey.ai/blog/harvey-to-expand-team-with-new-bengaluru-office\">Harvey Bengaluru</a>; "
           "<a href=\"https://api.sci.gov.in/supremecourt/2025/52338/52338_2025_5_1501_71939_Judgement_02-Jul-2026.pdf\"><i>Pooja Ramesh Singh v. J&amp;K Bank</i>, 2026 INSC 668</a>; "
           "<a href=\"https://api.sci.gov.in/supremecourt/2026/21991/21991_2026_7_1501_73957_Judgement_02-Sep-2026.pdf\"><i>Vijay Ghanshyam Gadiya v. Union of India</i>, 2026 INSC 947</a>; "
           "<a href=\"https://lawchakra.in/high-court/tax-officer-fake-ai-generated-case-law-tax/\">KMG Wires (Bombay HC)</a>; "
           "<a href=\"https://www.barandbench.com/news/bombay-high-court-quashes-customs-order-flagged-for-citing-non-existent-ai-generated-judgments\">Bombay HC customs rulings</a>; "
           "<a href=\"https://www.livelaw.in/high-court/kerala-high-court/kerala-high-court-ai-use-district-judiciary-298139\">Kerala HC policy</a>; "
           "<a href=\"https://www.livelaw.in/pdf_upload/2026/06/03/2026060342-677789.pdf\">Supreme Court draft AI regulations</a>; "
           "<a href=\"https://www.barandbench.com/news/scaora-seeks-removal-of-mandatory-ai-disclosure-requirement-for-lawyers-in-supreme-court-draft-regulations\">SCAORA objection</a>; "
           "<a href=\"https://www.newindianexpress.com/india/2026/Aug/27/ai-can-augment-reasoning-but-cannot-substitute-judicial-conscience-cji-surya-kant-3\">CJI Surya Kant</a>. "
           "Failure record: <a href=\"https://www.damiencharlotin.com/hallucinations/\">AI Hallucination Cases database</a> (total checked 12 Nov 2026; India filter); "
           "<a href=\"https://www.haqq.ai/blog/ai-legal-hallucination-audit\">HAQQ tracker (January count)</a>; "
           "<a href=\"https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1%3A2022cv01461/575368/54\"><i>Mata v. Avianca</i></a>; "
           "<a href=\"https://www.nytimes.com/2026/06/09/us/ai-lawyers-sanctioned-mississippi.html\"><i>Withers v. City of Aberdeen</i> (NYT)</a>; "
           "<a href=\"https://caselaw.nationalarchives.gov.uk/ewhc/admin/2025/1383\"><i>Ayinde</i> [2025] EWHC 1383 (Admin)</a>; "
           "<a href=\"https://www.sra.org.uk/news/news/releases/responsible-use-ai\">SRA</a>; "
           "<a href=\"https://www.nycbar.org/reports/artificial-intelligence-in-federal-courts-a-random-sample-survey-of-judges\">NYC Bar survey of judges</a>; "
           "<a href=\"https://www.judiciary.senate.gov/press/rep/releases/grassley-releases-judges-responses-owning-up-to-ai-use-calls-for-continued-oversight-and-regulation\">Senate Judiciary (judges&rsquo; letters)</a>; "
           "<a href=\"https://www.judiciary.uk/guidance-and-resources/artificial-intelligence-ai-judicial-guidance-october-2025\">UK judicial guidance</a>; "
           "<a href=\"https://onlinelibrary.wiley.com/doi/10.1111/jels.12413\">Stanford RegLab</a> and "
           "<a href=\"https://law.stanford.edu/publications/benchmarking-legal-rag-the-promise-and-limits-of-ai-statutory-surveys\">2026 follow-up</a>; "
           "<a href=\"https://www.bbc.co.uk/news/articles/cglyjn7le2ko\">BBC on Hill Dickinson</a>. "
           "Most surveys cited are run by companies that sell legal software or AI, and are labelled as such. Shares and the combined valuation are this blog&rsquo;s arithmetic (builder at out/research/legal-ai-2026/).")

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/ai-is-not-taking-indias-offshore-work.html", "AI Is Not Taking India&rsquo;s Offshore Work Evenly: A Sector-by-Sector Check, and the Government Backlogs the Same Skills Could Clear"),
    ("https://masaladeutsch.blogspot.com/2026/08/indian-it-in-ai-era.html", "Indian IT in an AI Era"),
    ("https://masaladeutsch.blogspot.com/2026/07/ai-high-demand-launch-tracker.html", "AI Tools Edition 03: A Repo With 98,000 Stars This Tracker Had Never Heard Of"),
    ("https://masaladeutsch.blogspot.com/2026/09/a-supreme-court-ruling-on-intoxicating.html", "A Supreme Court Ruling on &ldquo;Intoxicating Liquor&rdquo; Just Became a Cost Risk for India&rsquo;s Ethanol Programme"),
]

TITLE = "India&rsquo;s Top Law Firms Have Signed Up for AI. Most of the Fake Citations India&rsquo;s Courts Have Caught Came From the Bench"
build("Law &amp; Technology &middot; 12 November 2026", TITLE,
      f"Lawyers are adopting generative AI fast, and the two biggest legal-AI start-ups are now worth ${COMBINED:.1f} billion between them. "
      f"India&rsquo;s largest firms chose their tools in 2025. But in {IN_BENCH} of the {IN_ENTRIES} Indian entries in a global record of AI-fabricated law, "
      "the fake precedent was relied on by a judge, tribunal or tax officer, not a lawyer, and the Bar Council has yet to write the rules the Supreme Court asked for in July.",
      body, sources, related, OUT)
print("built", OUT, "combined", COMBINED, "bench", IN_BENCH)
