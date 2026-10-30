import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-securities-markets-code.html'

# SEBI investigations taken up / completed by year (SEBI annual reports as reported by PTI, Business Standard, Moneylife, Factly).
# FY22 completed not found; FY22 taken up implied by the 2022-23 report ("144, way higher than 59").
INV = [("2019-20", 161, 170), ("2020-21", 94, 140), ("2021-22", 59, None),
       ("2022-23", 144, 152), ("2023-24", 342, 197), ("2024-25", 400, 301)]
CUM_UP, CUM_DONE = 1667, 1603            # Factly/Dataful: 2013-14 to 2023-24, completions include backlog
PRE_UP = CUM_UP - 342                    # 2013-14 to 2022-23
PRE_DONE = CUM_DONE - 197
PRE_NET = PRE_UP - PRE_DONE              # negative = stock of open cases shrank
NET_24, NET_25 = 342 - 197, 400 - 301
NET_2Y = NET_24 + NET_25

# Recovery (Business Standard analysis of annual reports, Aug 2024; FY25 annual report coverage Aug 2025)
NOTICES_CR, RECOVERED_CR = 106_000, 1_768
REC_PCT = RECOVERED_CR / NOTICES_CR * 100
DTR = [("March 2023", 73_287), ("March 2024", 76_293), ("March 2025", 77_800)]
DTR_COURT = 61_200

# SAT appeals against SEBI orders, FY25 (SEBI annual report as reported)
SAT_NEW_24, SAT_NEW_25, SAT_DISPOSED = 821, 533, 422
SAT_OUT = [("Dismissed", 308), ("Upheld with modification", 42), ("Withdrawn", 28), ("Allowed", 23), ("Remanded", 21)]
assert sum(n for _, n in SAT_OUT) == SAT_DISPOSED


def chart_inv():
    W, H, L, B, top = 400, 250, 34, 200, 40
    mx = 450
    sc = (B - top) / mx
    gw = (W - L - 10) / len(INV)
    bw = gw * 0.32
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="SEBI investigations taken up and completed each year, 2019-20 to 2024-25.">',
         f'<text x="10" y="13" font-size="12" fill="#495057">SEBI investigations, cases per year</text>',
         f'<rect x="10" y="21" width="10" height="10" fill="#a5402c"/><text x="24" y="30" font-size="9.5" fill="#212529">Taken up</text>',
         f'<rect x="80" y="21" width="10" height="10" fill="#1c5d99"/><text x="94" y="30" font-size="9.5" fill="#212529">Completed (includes older cases)</text>']
    for v in (0, 100, 200, 300, 400):
        y = B - v * sc
        s.append(f'<line x1="{L}" x2="{W - 6}" y1="{y:.1f}" y2="{y:.1f}" stroke="#dee2e6"/>')
        s.append(f'<text x="{L - 4}" y="{y + 3:.1f}" font-size="9" fill="#6c757d" text-anchor="end">{v}</text>')
    for i, (yr, up, done) in enumerate(INV):
        x0 = L + i * gw + gw * 0.16
        s.append(f'<rect x="{x0:.1f}" y="{B - up * sc:.1f}" width="{bw:.1f}" height="{up * sc:.1f}" fill="#a5402c"/>')
        s.append(f'<text x="{x0 + bw / 2:.1f}" y="{B - up * sc - 3:.1f}" font-size="8.5" fill="#212529" text-anchor="middle">{up}</text>')
        x1 = x0 + bw + 2
        if done is None:
            s.append(f'<text x="{x1 + bw / 2:.1f}" y="{B - 4:.1f}" font-size="8" fill="#6c757d" text-anchor="middle">n/a</text>')
        else:
            s.append(f'<rect x="{x1:.1f}" y="{B - done * sc:.1f}" width="{bw:.1f}" height="{done * sc:.1f}" fill="#1c5d99"/>')
            s.append(f'<text x="{x1 + bw / 2:.1f}" y="{B - done * sc - 3:.1f}" font-size="8.5" fill="#212529" text-anchor="middle">{done}</text>')
        s.append(f'<text x="{L + i * gw + gw / 2:.1f}" y="{B + 13}" font-size="9" fill="#212529" text-anchor="middle">{yr}</text>')
    s.append(f'<text x="10" y="{H - 18}" font-size="9" fill="#6c757d">SEBI annual reports as reported by PTI, Business Standard, Moneylife and Factly.</text>')
    s.append(f'<text x="10" y="{H - 6}" font-size="9" fill="#6c757d">2021-22 completions not found; 2021-22 intake inferred from the 2022-23 report.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


CMP = [
    ("Deadline to finish an investigation", "180 days, unlimited extensions", "One year"),
    ("Defining &ldquo;market abuse&rdquo;", "SEBI can widen it by regulation", "Remove that power"),
    ("Appeals to the Securities Appellate Tribunal (SAT)", "Listed orders only", "Any SEBI order, including interim ones"),
    ("SEBI&rsquo;s rule-making discretion", "Broad, little guidance", "Limit each delegation"),
    ("Civil and criminal cases", "Clauses overlap", "Redraft them"),
    ("Investor grievances (Ombudsperson)", "Optional", "Mandatory, 120-day limit"),
    ("Cancelling an exchange&rsquo;s or depository&rsquo;s registration", "SEBI alone", "After consulting the Centre"),
    ("Exempting public-sector companies", "Centre can exempt", "Case by case, written reasons"),
    ("Unlawful gains", "No method set", "SEBI rules to quantify them"),
]


def t_cmp():
    return table(["Issue", "Code as introduced (Dec 2025)", "Standing Committee (Jul 2026)"], CMP)


def t_settle():
    rows = [("2021-22", "&mdash;", "107", "&mdash;", "59"),
            ("2023-24", "434", "&mdash;", "&mdash;", "&mdash;"),
            ("2024-25", "703", "284", "272", "799"),
            ("2025-26", "439", "170", "199", "110*")]
    return table(["Year", "Filed", "Settled", "Rejected or returned", "Charges, Rs cr"], rows)


def t_dtr():
    return table(["As of", "&ldquo;Difficult to recover&rdquo; dues, Rs crore"], [(d, f"{v:,}") for d, v in DTR])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>400 vs 301</b><span>investigations SEBI took up vs completed in 2024-25; it took up 342 and completed 197 the year before</span></div>
<div class="gb-stat"><b>+{NET_2Y}</b><span>net rise in open investigations over 2023-24 and 2024-25, after the stock fell by about {-PRE_NET} over the previous ten years</span></div>
<div class="gb-stat"><b>180 days &rarr; 1 year</b><span>the committee wants the Code&rsquo;s deadline for finishing an investigation doubled</span></div>
<div class="gb-stat"><b>Rs 77,800 cr</b><span>of penalties and refunds SEBI classed as &ldquo;difficult to recover&rdquo; in March 2025; about {REC_PCT:.1f}% of recovery notices since 2013-14 had been collected by 2024</span></div>
</div>'''

body = f"""
{stats}

<p>The Securities Markets Code, 2025 would replace the three laws that run India&rsquo;s stock and bond markets: the Securities Contracts (Regulation) Act, 1956, the Securities and Exchange Board of India (SEBI) Act, 1992 and the Depositories Act, 1996. Finance Minister Nirmala Sitharaman introduced it in the Lok Sabha on 18 December 2025 and it went to the Standing Committee on Finance, chaired by Bhartruhari Mahtab, which reported on 23 July 2026. The Code was not taken up in the Monsoon Session that ended on 13 August, so it remains pending. This piece sets out what the committee wants changed, and then checks the changes against how long SEBI&rsquo;s investigations, appeals and recoveries actually take.</p>

<h2 class="gb-h2">What the committee wants changed</h2>
<p>The committee broadly backed a single code and a stronger SEBI, but asked for limits on how SEBI uses its powers. Its main recommendations, as summarised by PRS Legislative Research, are below.</p>
{t_cmp()}
<p class="gb-note">Bill and committee positions from PRS Legislative Research&rsquo;s bill summary, legislative brief and report summary, read through search-engine text; the report itself was not opened.</p>
<p>Some details do not fit a table. The Code also bars SEBI from starting an inspection or investigation more than eight years after a breach. The committee chair told ANI the new investigation limit would be 360 days rather than a calendar year. For market infrastructure institutions (MIIs: stock exchanges, clearing corporations and depositories), the committee also wants public consultation on bye-law changes, a maximum period for any government takeover, and the Code to spell out which functions SEBI may hand to them.</p>
<p>Two of these changes restore what the 1992 law already allows. The SEBI Act lets &ldquo;any person aggrieved&rdquo; by a SEBI order appeal to SAT; the Code&rsquo;s list of appealable orders would have narrowed that, and the committee wants the wider wording back. And because market abuse is a jailable offence, letting SEBI redefine it by regulation would let a regulator decide what counts as a crime, which is why the committee wants that power deleted.</p>

<h2 class="gb-h2">Investigations: 180 days against a growing pile</h2>
{chart_inv()}
<p>SEBI took up 400 investigations in 2024-25, the most in decades, and completed 301; in 2023-24 it took up 342 and completed 197. The completed count includes cases opened in earlier years, so the two bars are not the same cases. What the gap does show is the direction of the backlog. Between 2013-14 and 2023-24 SEBI took up 1,667 cases and completed 1,603. Taking out 2023-24, the ten years to 2022-23 saw {PRE_UP:,} taken up and {PRE_DONE:,} completed, so the stock of open cases fell by about {-PRE_NET}. In the next two years it rose by {NET_24} and then {NET_25}, a net {NET_2Y} more open cases.</p>
<p>Against that, a 180-day deadline was never going to hold. PRS notes that most investigations take one to one-and-a-half years, and the Code allowed unlimited extensions, which would have made the deadline a formality. The committee&rsquo;s one year is closer to what happens, but only if the number of investigators keeps pace with a caseload that has more than doubled since 2022-23. Insider trading is now the largest category: 287 of the 400 cases in 2024-25, against 106 for market manipulation and price rigging.</p>

<h2 class="gb-h2">Appeals: fewer filed, most dismissed</h2>
<p>New appeals against SEBI to the Securities Appellate Tribunal fell from {SAT_NEW_24} in 2023-24 to {SAT_NEW_25} in 2024-25, according to SEBI&rsquo;s annual report. Of the {SAT_DISPOSED} appeals disposed of that year, {SAT_OUT[0][1]} ({SAT_OUT[0][1] / SAT_DISPOSED * 100:.0f}%) were dismissed, {SAT_OUT[1][1]} upheld with changes, {SAT_OUT[2][1]} withdrawn, {SAT_OUT[3][1]} allowed and {SAT_OUT[4][1]} sent back to SEBI. SAT itself received a record 1,192 appeals of all kinds in 2022-23, and has spent long stretches with a single bench and sometimes without a quorum.</p>
<p>Opening every SEBI order to appeal, as the committee wants, will add cases. The dismissal rate suggests most appeals do not overturn SEBI, but interim orders such as trading bans and freezes can do lasting harm before a final order arrives, which is the committee&rsquo;s reason for wanting them appealable. The cost is more work for a tribunal that has struggled to stay fully staffed.</p>

<h2 class="gb-h2">Settlements and recoveries</h2>
<p>Many cases end in settlement rather than an order. Applications rose from 434 in 2023-24 to 703 in 2024-25, when SEBI settled 284 and collected about Rs 799 crore. In 2025-26, according to secondary summaries of a SEBI consultation paper, applications fell to 439 and 170 were settled.</p>
{t_settle()}
<p class="gb-note">* 2025-26 figures are from secondary summaries of SEBI&rsquo;s August 2026 consultation paper on settlement regulations and could not be checked against the annual report; the charges figure in particular looks low and should be treated with caution. A dash means the figure was not found.</p>
<p>Collecting money is harder than ordering it paid. A Business Standard analysis of SEBI&rsquo;s annual reports found that recovery notices worth about Rs 1.06 lakh crore were issued from 2013-14 to 2023-24, and about Rs {RECOVERED_CR:,} crore was recovered, roughly {REC_PCT:.1f}%. SEBI classes dues as &ldquo;difficult to recover&rdquo; once every recovery route has been tried; that figure keeps rising.</p>
{t_dtr()}
<p>Most of it is not ordinary market fraud. Over Rs {DTR_COURT:,} crore of the March 2025 total sits in cases before court-appointed committees, chiefly the PACL and Sahara collective-investment schemes. The Code&rsquo;s faster investigation deadlines and the committee&rsquo;s appeal rights do not touch this pile; it depends on courts and asset sales.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>SEBI should publish, each year, its stock of open investigations at the start and end of the year and their age, not only cases taken up and completed, so the effect of any statutory deadline can be checked.</li>
<li>If the Code sets a one-year deadline, extensions should be capped and each one recorded with reasons in the annual report, so the limit cannot become routine.</li>
<li>The Code should require SAT to sit with its full statutory strength and report its pending appeals and median disposal time each year, since wider appeal rights will add to its load.</li>
<li>&ldquo;Difficult to recover&rdquo; dues should be reported in two parts: cases before court-appointed committees (PACL, Sahara) and everything else, so recovery from ordinary enforcement can be judged on its own.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The Code, the committee report and SEBI&rsquo;s annual reports were read only through PRS summaries and news coverage indexed by search engines; none of the documents were opened. The committee&rsquo;s investigation deadline is reported as &ldquo;one year&rdquo; by PRS and &ldquo;360 days&rdquo; by the chair in an interview. SEBI&rsquo;s 2025-26 annual report, released in August 2026, was located but its enforcement chapter could not be read, so no 2025-26 investigation counts are given. The number of investigations completed in 2021-22 and the number of appeals pending before SAT at the end of 2024-25 or 2025-26 could not be found from a reliable source; one secondary article&rsquo;s claim of over 2,800 pending appeals is not used. Whether the government will accept the committee&rsquo;s changes, and when the Code returns to Parliament, is not known. This is not legal advice.</p>
"""

sources = ("Code text and committee positions: PRS Legislative Research, The Securities Markets Code, 2025 (bill page, bill summary, legislative brief and Standing Committee report summary, July 2026); Standing Committee on Finance (2025-26), report on the Code presented 23 July 2026, as indexed; PRS Monsoon Session 2026 session wrap; AIR News (18 December 2025) on introduction; ANI/NewKerala (July 2026) on the chair&rsquo;s remarks. "
           "Investigations: SEBI annual reports as reported by PTI/The Week (August 2025), Business Standard, Moneylife (2020-21) and Factly/Dataful (2013-14 to 2023-24 and 2024-25 categories). "
           "Appeals: SEBI annual report 2024-25 as reported by Outlook Business and ETV Bharat (August 2025); Board Stewardship on SAT&rsquo;s 2022-23 caseload; Business Standard (February 2024) on SAT benches. "
           "Settlements: Outlook Business, YourStory (2024-25); Moneylife (2021-22); secondary summaries of SEBI&rsquo;s August 2026 consultation paper (2025-26). "
           "Recoveries: Business Standard (August 2023, August 2024, August 2025) and Angel One. Backlog arithmetic is this blog&rsquo;s (builder in the repository at out/research/securities-code/). Nothing here is legal or investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/09/indias-live-ipo-queue-has-232-companies.html", "India&rsquo;s Live IPO Queue Has 232 Companies in It"),
    ("https://masaladeutsch.blogspot.com/2026/09/engineering-and-auto-component-makers.html", "Engineering and Auto-Component Makers File More SEBI DRHPs Than Any Other Sector"),
    ("https://masaladeutsch.blogspot.com/2026/09/what-failed-bankruptcy-auction-actually.html", "What a Failed Bankruptcy Auction Actually Costs, in India&rsquo;s Own Numbers"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-petroleum-act-still-fines.html", "India&rsquo;s Petroleum Act Still Fines a Licence Breach &#8377;1,000. The Draft Fix Goes to &#8377;5 Crore"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-constitution-set-deadline.html", "India&rsquo;s Constitution Set a Deadline Parliament Hasn&rsquo;t Met: The Reforms Pending in 2026"),
]

build("Markets · 30 October 2026",
      "India&rsquo;s New Securities Code Gives SEBI 180 Days to Finish a Probe. Most Take a Year or More",
      "A parliamentary committee wants the deadline doubled, every SEBI order open to appeal and limits on SEBI&rsquo;s power to define offences. SEBI&rsquo;s own numbers show open investigations rising again and under 2% of recovery notices collected.",
      body, sources, related, OUT)
print("pre", PRE_UP, PRE_DONE, PRE_NET, "2y", NET_2Y, "rec%", round(REC_PCT, 2))
