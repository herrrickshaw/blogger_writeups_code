import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-csr-threshold.html'

# --- MCA estimate given to the Joint Committee (reported by ETCFO, 31 Aug 2026; The News Minute, 6 Aug 2026)
EXIT_COS = 11204                 # companies leaving the CSR mandate when the net-profit trigger rises to Rs 10 crore
EXIT_OBLIG = 1281.67             # Rs crore, their estimated CSR obligation in 2025-26 under the current Rs 5 crore trigger

# --- IICA India CSR Factbook 2024-25 (MCA National CSR Data Portal, data extracted 20 Sep 2026)
SPEND_FY25 = 40794.0             # Rs crore, CSR spend disclosed for 2024-25
COS_SPENDING = 24228             # companies with spend records
COS_FILING = 29544               # companies filing CSR disclosures
BANDS = [  # annual CSR spend band, companies
    ("Below Rs 1 crore", 20019),
    ("Rs 1&ndash;10 crore", 3720),
    ("Rs 10&ndash;50 crore", 396),
    ("Rs 50 crore and above", 93),
]
SHARE_BELOW_1CR = 13.3           # % of spend from companies spending below Rs 1 crore
SHARE_50CR_PLUS = 42.4           # % of spend from the 93 companies spending Rs 50 crore or more
SHARE_TOP10 = 17.5
STATES_TOP = [("Maharashtra", 21.16), ("Gujarat", 11.15), ("Karnataka", 8.32), ("Delhi", 6.75), ("Tamil Nadu", 6.71)]
PENALISED = 26                   # companies penalised for CSR non-compliance, FY20-FY24 (MCA to Parliament, via IICA)

# National CSR spend by year, Rs crore. IICA Factbook table 15.1 except where noted (different portal snapshots).
SERIES = [
    ("FY15", 10065.93, ""), ("FY16", 14517.21, ""), ("FY17", 14542.51, ""), ("FY18", 17098.57, ""),
    ("FY19", 20196.95, "a"), ("FY20", 24965.82, "b"), ("FY21", 26210.95, "c"),
    ("FY22", 27141.45, ""), ("FY23", 30932.08, ""), ("FY24", 34908.75, ""), ("FY25", 40794.0, ""),
]

# Voluntary spending (Sattva, CSR's Next Act, FY 2023-24): companies with no obligation still spent
VOL_COS, VOL_SPEND = 380, 809    # Rs crore
OVERSPEND_SHARE = 61             # % of companies spending more than prescribed, FY24 (IndiaDataInsights)

# --- arithmetic
assert sum(n for _, n in BANDS) == COS_SPENDING
below_1cr = BANDS[0][1]
assert round(below_1cr / COS_SPENDING * 100, 1) == 82.6
exit_share_cos = EXIT_COS / COS_SPENDING * 100            # ~46%
exit_share_filers = EXIT_COS / COS_FILING * 100           # ~38%
exit_share_money = EXIT_OBLIG / SPEND_FY25 * 100          # ~3.1%
exit_avg_lakh = EXIT_OBLIG * 100 / EXIT_COS               # Rs lakh per company
below_1cr_spend = SHARE_BELOW_1CR / 100 * SPEND_FY25      # Rs crore
exit_of_below = EXIT_OBLIG / below_1cr_spend * 100
remaining = COS_SPENDING - EXIT_COS
remaining_below_1cr = below_1cr - EXIT_COS
board_only_share = remaining_below_1cr / remaining * 100
middle_share = 100 - SHARE_BELOW_1CR - SHARE_50CR_PLUS
top5_states = sum(s for _, s in STATES_TOP)
growth_10y = (SPEND_FY25 / SERIES[0][1] - 1) * 100
assert 45 < exit_share_cos < 47 and 3.0 < exit_share_money < 3.2 and 11 < exit_avg_lakh < 12

def pct(v, d=1):
    return f"{v:.{d}f}%"


def table(head, rows, cls=""):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def chart_shares():
    """Two panels, one colour: share of companies vs share of CSR money for three groups."""
    groups = [
        ("Leaving", exit_share_cos, exit_share_money),
        ("Spend under Rs 1 cr", below_1cr / COS_SPENDING * 100, SHARE_BELOW_1CR),
        ("Spend Rs 50 cr+", BANDS[3][1] / COS_SPENDING * 100, SHARE_50CR_PLUS),
    ]
    W, L, lab, bh, gap = 340, 4, 128, 18, 8
    sc = (W - L - lab - 48) / 100
    s = [f'<text x="{L}" y="16" font-size="15" fill="#212529" font-weight="700">Share of companies vs share of money</text>',
         f'<text x="{L}" y="34" font-size="12" fill="#6c757d">% of {COS_SPENDING:,} CSR spenders and of Rs 40,794 cr, 2024-25</text>']
    y = 60
    for title, idx in (("Share of companies", 1), ("Share of CSR money", 2)):
        s.append(f'<text x="{L}" y="{y}" font-size="13" fill="#212529" font-weight="700">{title}</text>')
        y += 9
        for g in groups:
            v = g[idx]
            w = max(v * sc, 2)
            s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="12" fill="#212529" text-anchor="end">{g[0]}</text>')
            s.append(f'<rect x="{L + lab}" y="{y}" width="{w:.1f}" height="{bh}" fill="#1c5d99"/>')
            s.append(f'<text x="{L + lab + w + 4:.1f}" y="{y + 13}" font-size="12" fill="#212529">{v:.1f}%</text>')
            y += bh + gap
        y += 16
    s.append(f'<text x="{L}" y="{y}" font-size="11" fill="#6c757d">Leaving: companies with Rs 5&ndash;10 cr profit; MCA</text>')
    s.append(f'<text x="{L}" y="{y + 14}" font-size="11" fill="#6c757d">estimate of 2025-26 obligation vs 2024-25 spend.</text>')
    s.append(f'<text x="{L}" y="{y + 28}" font-size="11" fill="#6c757d">Other rows: IICA India CSR Factbook 2024-25.</text>')
    H = y + 36
    head = f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Share of CSR-spending companies and share of CSR money for three groups: companies leaving the mandate, companies spending under Rs 1 crore, and the 93 largest spenders.">'
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + head + "\n".join(s) + '</svg></figure>'


def chart_series():
    W, L, top, bh, gap, lab = 340, 4, 48, 16, 6, 40
    H = top + len(SERIES) * (bh + gap) + 40
    sc = (W - L - lab - 64) / 41000
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="India&rsquo;s reported CSR spend by financial year, 2014-15 to 2024-25.">',
         f'<text x="{L}" y="16" font-size="15" fill="#212529" font-weight="700">Reported CSR spend, Rs crore</text>',
         f'<text x="{L}" y="34" font-size="12" fill="#6c757d">Financial years 2014-15 to 2024-25</text>']
    for i, (fy, v, note) in enumerate(SERIES):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 12}" font-size="12" fill="#212529" text-anchor="end">{fy}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="#1c5d99"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 12}" font-size="12" fill="#212529">{v:,.0f}{"*" if note else ""}</text>')
    s.append(f'<text x="{L}" y="{H - 18}" font-size="11" fill="#6c757d">IICA Factbook (MCA portal). *Earlier portal</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="11" fill="#6c757d">snapshots; not strictly comparable.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{EXIT_COS:,}</b><span>companies would leave the CSR mandate if the net-profit trigger rises from Rs 5 crore to Rs 10 crore, by the corporate affairs ministry&rsquo;s estimate</span></div>
<div class="gb-stat"><b>Rs {EXIT_OBLIG:,.0f} cr</b><span>their estimated CSR obligation for 2025-26: about {exit_share_money:.1f}% of the Rs 40,794 crore companies reported spending in 2024-25</span></div>
<div class="gb-stat"><b>Rs {exit_avg_lakh:.1f} lakh</b><span>the average obligation of a company that would leave</span></div>
<div class="gb-stat"><b>93</b><span>companies spending Rs 50 crore or more each account for {SHARE_50CR_PLUS}% of all CSR money</span></div>
</div>'''

t_bill = table(
    ["Provision (now)", "Bill", "Committee"],
    [
        ("Profit trigger (Rs 5 cr)", "Rs 10 cr, or as prescribed", "Rs 10 cr, fixed in the Act"),
        ("Net worth, turnover (Rs 500 cr, Rs 1,000 cr)", "Same", "Same"),
        ("No CSR committee if spend up to (Rs 50 lakh)", "Rs 1 cr, or more", "Endorsed; two dissents"),
        ("Power to exempt classes of companies (none)", "Added", "Drop it"),
        ("Time to move unspent money (30 days)", "90 days", "Endorsed"),
        ("Giving to barred agencies (not covered)", "Not covered", "Should not count as CSR"),
        ("CSR in kind (not allowed)", "Not covered", "Examine; disaster relief first"),
    ])

t_bands = table(
    ["Spend band", "Firms (share)", "Money"],
    [
        ("Under Rs 1 cr", f"{BANDS[0][1]:,} ({BANDS[0][1] / COS_SPENDING * 100:.1f}%)", pct(SHARE_BELOW_1CR)),
        ("Rs 1&ndash;10 cr", f"{BANDS[1][1]:,} ({BANDS[1][1] / COS_SPENDING * 100:.1f}%)", f"{middle_share:.1f}%*"),
        ("Rs 10&ndash;50 cr", f"{BANDS[2][1]:,} ({BANDS[2][1] / COS_SPENDING * 100:.1f}%)", "*"),
        ("Rs 50 cr+", f"{BANDS[3][1]:,} ({BANDS[3][1] / COS_SPENDING * 100:.1f}%)", pct(SHARE_50CR_PLUS)),
        ("<b>Total</b>", f"<b>{COS_SPENDING:,}</b>", "<b>100%</b>"),
    ])

body = f"""
{stats}

<p>Since 2014, any Indian company with a net worth of Rs 500 crore, a turnover of Rs 1,000 crore or a net profit of Rs 5 crore has had to spend at least 2% of its average profit of the previous three years on corporate social responsibility (CSR): schools, hospitals, sanitation, the environment and the other activities listed in Schedule VII of the Companies Act. The Corporate Laws (Amendment) Bill, 2026, introduced in the Lok Sabha on 23 March, would double the profit trigger to Rs 10 crore. A Joint Parliamentary Committee examined it and reported on 3 August, backing the higher threshold with changes. The Bill has not yet been passed.</p>

<p>The change sounds large, and by one measure it is: the corporate affairs ministry told the committee that {EXIT_COS:,} companies would leave the CSR regime. By the measure that matters to the schools and clinics that receive the money, it is small. Those companies were expected to spend about Rs {EXIT_OBLIG:,.0f} crore in 2025-26, roughly {exit_share_money:.0f}% of what Indian companies now report spending each year.</p>

<h2 class="gb-h2">What the Bill changes, and what the committee wants</h2>

{t_bill}

<p class="gb-note">Bill provisions and committee recommendations as summarised by PRS Legislative Research, the committee&rsquo;s report and law-firm notes on it (Fox Mandal, Vinod Kothari &amp; Co., Cyril Amarchand Mangaldas). The 378-page report itself was read only in part.</p>

<p>Only the profit test moves. A company with a net worth of Rs 600 crore and a profit of Rs 4 crore stays in the regime; a company with a net worth of Rs 100 crore and a profit of Rs 9 crore leaves it. Lawyers have pointed out the asymmetry. The likely reason is simply that Rs 5 crore of profit was always a much lower bar than Rs 500 crore of net worth or Rs 1,000 crore of turnover, so it pulled in far more small companies.</p>

<p>The committee also objected to the Bill handing the government open-ended power, both to change the Rs 10 crore figure by rules and to exempt whole classes of companies, and asked that both be removed. It added a rule the Bill lacked: money given to trusts, societies or NGOs that a law, court or regulator has barred should not count as CSR.</p>

<h2 class="gb-h2">Many companies, little money</h2>

<p>The ministry&rsquo;s figures are for obligations, not actual spending, and they are for 2025-26, a year whose spending is not yet reported. Set against the latest complete year, they look like this. In 2024-25, {COS_SPENDING:,} companies reported CSR spending, totalling Rs 40,794 crore. The {EXIT_COS:,} companies that would leave are about {exit_share_cos:.0f}% of them, and their obligation is about {exit_share_money:.1f}% of the money. The average company leaving owed about Rs {exit_avg_lakh:.1f} lakh a year.</p>

{chart_shares()}

<p>This is the shape of CSR in India generally. An analysis of the ministry&rsquo;s 2024-25 data by the Indian Institute of Corporate Affairs (IICA), published in October, shows that companies spending under Rs 1 crore each make up 82.6% of spenders but provide 13.3% of the money. The 93 companies spending Rs 50 crore or more provide {SHARE_50CR_PLUS}%, and the 10 largest alone {SHARE_TOP10}%.</p>

{t_bands}

<p class="gb-note">Source: IICA, India CSR Factbook 2024-25, from the MCA National CSR Data Portal (data extracted 20 September 2026). The Factbook gives the spend share only for the smallest and largest bands; the middle two bands are shown together (*). Money: share of Rs 40,794 crore.</p>

<p>Practically every company that would leave falls into the smallest band: its obligation averages Rs 11 lakh, far below Rs 1 crore. On these figures they are a little over half of the {below_1cr:,} small spenders, and their Rs {EXIT_OBLIG:,.0f} crore is about a quarter of the roughly Rs {below_1cr_spend:,.0f} crore that band spent.</p>

<h2 class="gb-h2">The burden being lifted was already light</h2>

<p>The case for the change is compliance cost. But the heaviest piece of compliance, a separate board CSR committee, was already waived in 2021 for any company whose CSR spend is Rs 50 lakh or less. Almost none of the {EXIT_COS:,} companies has needed one: a company whose profits have stayed under Rs 10 crore owes at most about Rs 20 lakh. What they still carry is the spending itself, an annual CSR report in the board report and the CSR-2 form, and a penalty if money is left unspent and not transferred: twice the unspent amount or Rs 1 crore, whichever is lower. That penalty is rarely used. The ministry told Parliament that {PENALISED} companies were penalised for CSR defaults in the five years to 2023-24.</p>

<p>The Bill also lifts the committee exemption to Rs 1 crore. If the {EXIT_COS:,} small companies leave and the rest stay roughly where they were, about {remaining:,} companies would remain in the regime, and about {board_only_share:.0f}% of them would spend under Rs 1 crore and so need no committee. Committees would be required of roughly {BANDS[1][1] + BANDS[2][1] + BANDS[3][1]:,} companies, the ones that spend most of the money. Two committee members dissented on this point, arguing that oversight of CSR spending was being thinned without any independent check put in its place.</p>

<h2 class="gb-h2">Will the money actually go?</h2>

<p>Not all of it. Small companies are the most generous relative to their obligation: about {OVERSPEND_SHARE}% of companies spent more than they had to in 2023-24, according to IndiaDataInsights, and Sattva Consulting found that small spenders were the most likely to overshoot. Sattva also counted {VOL_COS} companies with no CSR obligation at all that spent Rs {VOL_SPEND} crore in 2023-24. Some of the companies leaving the mandate will go on giving, especially those whose spending is tied to a local hospital, school or trust near their plant.</p>

<p>The loss will be local. Companies spending under Rs 1 crore work in an average of 1.9 development sectors and 1.4 states, against 8.4 sectors and 11 states for the largest spenders. Small-company CSR tends to stay close to home. The ministry&rsquo;s estimate does not say which states or causes the Rs {EXIT_OBLIG:,.0f} crore currently reaches. CSR as a whole is concentrated: Maharashtra, Gujarat, Karnataka, Delhi and Tamil Nadu receive {top5_states:.0f}% of what can be traced to a state.</p>

{chart_series()}

<p>Set against the growth of CSR, the loss is small. Reported spending has risen from about Rs 10,066 crore in 2014-15 to Rs 40,794 crore in 2024-25, and by 13% to 17% a year in each of the last three years. A 3% cut in obligations would be made up within a few months of that growth, if it continues.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li><b>Publish the ministry&rsquo;s estimate in full.</b> The {EXIT_COS:,}-company figure and its Rs {EXIT_OBLIG:,.0f} crore were given to the committee but reached the public only through press reports. A table by state, development sector and implementing agency would show which NGOs and districts lose money.</li>
<li><b>Let leaving companies finish what they started.</b> Companies with multi-year &ldquo;ongoing projects&rdquo; at the time of the change should be required, or at least allowed, to complete them under the old rules, so that a scholarship or clinic funded for three years is not dropped after one.</li>
<li><b>Simplify the form rather than only shrinking the list.</b> For obligations under Rs 50 lakh, a one-page CSR filing would cut most of the cost of compliance while keeping the spending.</li>
<li><b>Keep thresholds in the Act, and review them on a schedule.</b> The committee is right that a figure which decides whether 11,000 companies pay should be set by Parliament, not by rules. A requirement to review all three triggers every five years, against inflation and company size, would avoid another long gap like 2013 to 2026.</li>
<li><b>Count voluntary CSR.</b> The CSR portal already records spending by companies with no obligation. Reporting it separately each year would show whether companies released from the mandate keep giving.</li>
</ul>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The {EXIT_COS:,}-company and Rs {EXIT_OBLIG:,.0f} crore figures are the ministry&rsquo;s, as reported by ETCFO and The News Minute from the committee&rsquo;s report; the relevant pages of the report were not read directly. They are obligations for 2025-26 and are compared here with actual spending in 2024-25, the latest complete year; the true share of spending lost could be a little higher or lower. How many of the leaving companies would keep spending voluntarily, and which states, districts and causes receive their money now, could not be found. The IICA Factbook gives spend shares only for the smallest and largest spending bands. The yearly series mixes portal snapshots: 2018-19 to 2020-21 come from earlier extracts quoted in Parliament and by Factly, and the portal&rsquo;s figures for past years are revised as late filings arrive. Whether the Bill will be taken up in the Winter Session, and in what form, is not known. Nothing here is legal advice.</p>
"""

sources = ("Bill and committee: PRS Legislative Research, The Corporate Laws (Amendment) Bill, 2026 (bill page and Joint Committee report summary, 31 August 2026); "
           "Report of the Joint Committee on the Corporate Laws (Amendment) Bill, 2026, presented 3 August 2026 (sansad.in), read in part; "
           "Fox Mandal &amp; Associates (Lexology, 5 August 2026), Vinod Kothari &amp; Co. and CS Pratik Shah summaries of the report; Cyril Amarchand Mangaldas and EY client alerts (March&ndash;April 2026); Chambers and Partners / S.S. Rana on the threshold asymmetry. "
           "Companies leaving and their obligation: Ministry of Corporate Affairs data given to the committee, as reported by ETCFO (&ldquo;Proposed corporate law raises CSR thresholds, draws dissent over accountability&rdquo;, 31 August 2026) and The News Minute (6 August 2026). "
           "CSR data: Indian Institute of Corporate Affairs, India CSR Factbook 2024-25 (October 2026), from the MCA National CSR Data Portal; 2018-19 from a Rajya Sabha annexure (data to 30 September 2022), 2019-20 from an MCA statement (February 2026), 2020-21 from Factly (portal as of August 2023). "
           "Voluntary and over-spending: Sattva Consulting, CSR&rsquo;s Next Act (October 2025), as reported by Newslaundry; IndiaDataInsights, The State of CSR in India 2014&ndash;24. "
           "Shares and averages are this blog&rsquo;s arithmetic (builder at out/research/csr-threshold/). Not legal advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/09/indias-labour-codes-took-six-years-to.html", "India&rsquo;s Labour Codes Took Six Years to Become Law. The Rules That Enforce Them Are Still Rolling Out State by State"),
    ("https://masaladeutsch.blogspot.com/2026/08/indias-state-incentive-war-gujarats.html", "India&rsquo;s State Incentive War: Gujarat&rsquo;s Execution Edge, Karnataka&rsquo;s FDI Inversion, and Why Nobody Can Tell You Who Actually Got Paid"),
    ("https://masaladeutsch.blogspot.com/2026/09/fourteen-states-reimburse-investors.html", "Fourteen States &ldquo;Reimburse&rdquo; Investors&rsquo; SGST. None of Them Can Actually Refund GST."),
]

build("Corporate Law · 7 November 2026",
      "Doubling India&rsquo;s CSR Profit Trigger Removes 11,204 Companies but About 3% of the Money",
      "The Corporate Laws (Amendment) Bill would raise the net profit that triggers mandatory CSR from Rs 5 crore to Rs 10 crore. Nearly half of today&rsquo;s CSR spenders would be released. Their combined obligation is about Rs 1,282 crore, against Rs 40,794 crore spent in 2024-25.",
      body, sources, related, OUT)
print("exit share cos", round(exit_share_cos, 1), "of filers", round(exit_share_filers, 1), "money", round(exit_share_money, 2),
      "avg lakh", round(exit_avg_lakh, 2), "below1cr spend", round(below_1cr_spend), "exit of below", round(exit_of_below, 1),
      "remaining", remaining, "board-only share", round(board_only_share, 1), "middle", round(middle_share, 1), "top5 states", round(top5_states, 1),
      "growth", round(growth_10y))
