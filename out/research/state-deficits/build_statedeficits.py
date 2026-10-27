import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-state-deficits.html'
LIMIT = 3.0   # 16th Finance Commission, states' annual fiscal deficit limit, % of GSDP, 2026-31

# PRS state budget analyses, 2026-27 budget estimates. None = not found in PRS text read for this piece.
# state, FD 2026-27 BE %GSDP, FD 2025-26 RE %GSDP, outstanding liabilities end-2026-27 %GSDP, interest % of revenue receipts 2026-27
S = [
    ("Punjab",         4.1, 4.2,  45.1, 23),
    ("Madhya Pradesh", 3.9, None, 32.5, 10.9),
    ("Andhra Pradesh", 3.8, 4.6,  36.0, 16),
    ("Rajasthan",      3.7, None, 36.8, 13),
    ("Kerala",         3.5, 3.8,  34.0, 20),
    ("Odisha",         3.5, 3.5,  14.1, None),
    ("Meghalaya",      3.5, None, 42.0, None),
    ("Telangana",      3.0, None, 28.7, None),
    ("Tamil Nadu",     3.0, 3.5,  27.0, 22),
    ("Uttar Pradesh",  3.0, 3.0,  23.1, None),
    ("Bihar",          3.0, 11.8, 34.0, 9),
    ("West Bengal",    2.9, 3.4,  38.0, 17),
    ("Karnataka",      2.9, 3.0,  25.0, 17),
    ("Maharashtra",    2.8, None, 20.4, 11),
    ("Haryana",        2.7, None, 25.8, 20),
    ("Jharkhand",      2.2, None, 25.8, None),
    ("Gujarat",        2.0, None, None, None),
]
# Gujarat interest share derived from PRS budget table: interest Rs 33,019 cr / revenue receipts Rs 2,71,602 cr
GUJ_INT = 33019 / 271602 * 100
S = [(n, fd, re, d, (round(GUJ_INT) if n == "Gujarat" else i)) for n, fd, re, d, i in S]
ABOVE = [r for r in S if r[1] > LIMIT]
AT = [r for r in S if r[1] == LIMIT]
RE_ABOVE = [r for r in S if r[2] is not None and r[2] > LIMIT]
RE_KNOWN = [r for r in S if r[2] is not None]

# SASCI (50-year interest-free capex loans): PRS State of State Finances, Oct 2025, all states 2025-26 BE
ALL_FD_INCL, ALL_FD_EXCL = 3.2, 2.8
MEG_REPORTED, MEG_AS_GRANT = 8.7, 4.7          # Meghalaya 2024-25 actuals, % GSDP (PRS)
MEG_DEBT, MEG_DEBT_EX = 42.0, 35.0             # Meghalaya end-2026-27 liabilities incl/excl SASCI
# Uttar Pradesh: ratio falls because projected GSDP jumps
UP_GSDP_27 = 39_75_500                          # Rs crore, 2026-27 BE (PRS table)
UP_GSDP_JUMP = 0.28
UP_GSDP_26 = UP_GSDP_27 / (1 + UP_GSDP_JUMP)
UP_DEBT_26, UP_DEBT_27 = 27.6, 23.1
UP_L26 = UP_DEBT_26 / 100 * UP_GSDP_26
UP_L27 = UP_DEBT_27 / 100 * UP_GSDP_27
UP_L_GROWTH = (UP_L27 / UP_L26 - 1) * 100
# Tamil Nadu contingent liabilities (PRS)
TN_GSDP = 40_67_000
TN_GUAR, TN_POWER = 1_80_000, 2_47_000
UP_GUAR_PCT = 5.8


def chart_fd():
    W, L, top, bh, gap, lab = 400, 10, 34, 13, 5, 104
    H = top + len(S) * (bh + gap) + 30
    sc = (W - L - lab - 40) / 4.5
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Budgeted fiscal deficit 2026-27 as a share of GSDP for 17 states, against the 3% limit.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Budgeted fiscal deficit 2026-27, % of GSDP</text>',
         f'<text x="{L}" y="25" font-size="9.5" fill="#6c757d">Red: above the Finance Commission&rsquo;s 3% limit</text>']
    x3 = L + lab + LIMIT * sc
    for i, (n, fd, re, d, it) in enumerate(S):
        y = top + i * (bh + gap)
        col = "#a5402c" if fd > LIMIT else ("#d9a441" if fd == LIMIT else "#1c5d99")
        s.append(f'<text x="{L + lab - 6}" y="{y + 10}" font-size="9.5" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{fd * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{max(L + lab + fd * sc + 4, x3 + 4):.1f}" y="{y + 10}" font-size="9.5" fill="#212529">{fd:.1f}</text>')
    yb = top + len(S) * (bh + gap)
    s.insert(3, f'<line x1="{x3:.1f}" x2="{x3:.1f}" y1="{top - 4}" y2="{yb}" stroke="#212529" stroke-dasharray="3 2"/>')
    s.append(f'<text x="{x3 + 3:.1f}" y="{yb + 10}" font-size="9" fill="#212529">3% limit</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Budget estimates, as summarised by PRS Legislative Research. Amber: exactly 3%.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_interest():
    rows = sorted([r for r in S if r[4] is not None], key=lambda r: -r[4])
    W, L, top, bh, gap, lab = 400, 10, 24, 14, 6, 104
    H = top + len(rows) * (bh + gap) + 30
    sc = (W - L - lab - 40) / 25
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Interest payments as a share of revenue receipts, 2026-27 budget estimates, by state.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Interest payments, % of revenue receipts, 2026-27</text>']
    for i, (n, fd, re, d, it) in enumerate(rows):
        y = top + i * (bh + gap)
        col = "#a5402c" if it >= 20 else "#1c5d99"
        s.append(f'<text x="{L + lab - 6}" y="{y + 11}" font-size="9.5" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{it * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + it * sc + 4:.1f}" y="{y + 11}" font-size="9.5" fill="#212529">{it:g}%</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">PRS budget analyses; Gujarat derived from its budget table by this blog.</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Red: a fifth or more of revenue goes to interest.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def f(v, suf=""):
    return "&mdash;" if v is None else f"{v:g}{suf}"


def t_states():
    return table(["State", "Fiscal deficit 2026-27 (BE), % GSDP", "2025-26 revised, % GSDP", "Debt end-2026-27, % GSDP", "Interest, % of revenue receipts"],
                 [(n, f"<b>{fd:g}</b>" if fd > LIMIT else f"{fd:g}", f(re), f(d), f(it)) for n, fd, re, d, it in S])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{len(ABOVE)} of {len(S)}</b><span>states in this table budget a 2026-27 fiscal deficit above the new 3% of GSDP limit; {len(AT)} more sit exactly on it</span></div>
<div class="gb-stat"><b>{len(RE_ABOVE)} of {len(RE_KNOWN)}</b><span>states with published revised figures ended up above 3% in 2025-26, whatever they had budgeted</span></div>
<div class="gb-stat"><b>{ALL_FD_INCL - ALL_FD_EXCL:.1f} pts</b><span>of GSDP: how much the 50-year interest-free capex loans lowered all states&rsquo; reported 2025-26 deficit (3.2% vs 2.8%)</span></div>
<div class="gb-stat"><b>23%</b><span>of Punjab&rsquo;s revenue goes on interest, against 9% in Bihar and about 11% in Maharashtra and Madhya Pradesh</span></div>
</div>'''

above_names = ", ".join(r[0] for r in ABOVE)
body = f"""
{stats}

<p>The 16th Finance Commission, whose recommendations cover 2026-27 to 2030-31, has told states to keep their annual fiscal deficit within 3% of their gross state domestic product (GSDP). It also wants off-budget borrowing ended and counted in deficit and debt figures. The first budgets under that rule are now in. Using PRS Legislative Research&rsquo;s analyses of 17 state budgets for 2026-27, this piece sets out which states plan to borrow more than the limit, how far last year&rsquo;s budgets drifted from their targets, what the exclusion of the Centre&rsquo;s 50-year capital loans does to the headline numbers, and how much of each state&rsquo;s revenue already goes on interest.</p>

<h2 class="gb-h2">Seven states plan to borrow above the limit</h2>
{chart_fd()}
<p>{len(ABOVE)} of the {len(S)} states budget a deficit above 3% of GSDP in 2026-27: {above_names}. Punjab is highest at 4.1%, followed by Madhya Pradesh (3.9%), Andhra Pradesh (3.8%) and Rajasthan (3.7%). Telangana, Tamil Nadu, Uttar Pradesh and Bihar budget exactly 3%. Gujarat is lowest at 2.0%, followed by Jharkhand (2.2%) and Haryana (2.7%).</p>
{t_states()}
<p class="gb-note">BE: budget estimate. All figures as reported in PRS Legislative Research&rsquo;s 2026-27 state budget analyses; a dash means the figure was not found in the text read for this piece. Kerala&rsquo;s analysis reports outstanding debt where others report outstanding liabilities, which can differ. Gujarat&rsquo;s interest share is this blog&rsquo;s division of its budgeted interest (Rs 33,019 crore) by revenue receipts (Rs 2,71,602 crore).</p>

<h2 class="gb-h2">Budgets are targets, not outcomes</h2>
<p>The 2026-27 numbers are plans, and last year&rsquo;s plans moved. Of the {len(RE_KNOWN)} states in the table whose 2025-26 revised estimates were found, {len(RE_ABOVE)} ended above 3%: Andhra Pradesh at 4.6% against a budgeted 4.4%, Punjab at 4.2%, Kerala at 3.8%, Tamil Nadu and Odisha at 3.5% and West Bengal at 3.4%. Bihar is the outlier. It budgeted a 3% deficit for 2025-26 and now expects 11.8% of GSDP, because spending excluding debt repayment ran 36% above the budget, with the largest increases in social welfare (including Rs 21,050 crore under Mahila Sashaktikaran) and education. Its 2026-27 budget again plans 3%, which requires spending to fall 19% from last year&rsquo;s revised level.</p>

<h2 class="gb-h2">What the 50-year loans keep out of the numbers</h2>
<p>Since 2020-21 the Centre has lent states money for capital projects under the Special Assistance to States for Capital Investment (SASCI) scheme, interest-free and repayable over 50 years. Under the Centre&rsquo;s borrowing guidelines these loans are excluded when a state&rsquo;s borrowing ceiling is calculated, and PRS&rsquo;s state analyses note that the exclusion continues for 2026-27. The money is still borrowed and still has to be repaid.</p>
<p>The effect is visible in the aggregate. PRS estimates the states&rsquo; combined 2025-26 deficit at 3.2% of GSDP including SASCI loans and 2.8% excluding them, a difference of {ALL_FD_INCL - ALL_FD_EXCL:.1f} percentage points. In small states it is far larger: Meghalaya&rsquo;s 2024-25 deficit was 8.7% of GSDP as reported, and would have been 4.7% if the SASCI money were counted as grants, while its debt at the end of 2026-27 is 42% of GSDP including these loans and 35% without them. The Finance Commission&rsquo;s call to bring off-budget borrowing into the numbers points the other way; in Rajasthan, counting off-budget borrowing raises liabilities at the end of 2023-24 from 37.3% to 37.9% of GSDP.</p>
<p>Ratios can also move for reasons that have nothing to do with borrowing. Uttar Pradesh&rsquo;s liabilities fall from 27.6% of GSDP to 23.1% in its budget. But its projected GSDP for 2026-27 (Rs {UP_GSDP_27 / 1e5:.2f} lakh crore) is {UP_GSDP_JUMP * 100:.0f}% above last year&rsquo;s revised level, an unusually steep jump. On those figures its liabilities in rupees rise by about {UP_L_GROWTH:.0f}%, from about Rs {UP_L26 / 1e5:.2f} lakh crore to Rs {UP_L27 / 1e5:.2f} lakh crore; the ratio falls only because the denominator is projected to grow so fast.</p>

<h2 class="gb-h2">How much revenue already goes on interest</h2>
{chart_interest()}
<p>The deficit limit matters most where past borrowing already eats the budget. Punjab spends 23% of its revenue receipts on interest and 72% on salaries, pensions and interest together; Kerala&rsquo;s committed spending is also 72%, with interest at 20%. Tamil Nadu spends 22% on interest and Haryana 20%. At the other end, Bihar spends 9%, Madhya Pradesh 10.9%, Maharashtra 11% and Gujarat about 12%. For comparison, the Union government spends about 40% of its revenue receipts on interest in 2026-27.</p>
<p>Debt on the books is not the whole exposure. Tamil Nadu has about Rs 1.8 lakh crore of guarantees outstanding (about {TN_GUAR / TN_GSDP * 100:.1f}% of its projected GSDP) and its power-sector companies carry about Rs 2.47 lakh crore of debt (about {TN_POWER / TN_GSDP * 100:.1f}%). Uttar Pradesh&rsquo;s guarantees come to {UP_GUAR_PCT}% of GSDP. The Finance Commission put discom debt across states at about 2.3&ndash;2.5% of GSDP in 2024-25 and recommended privatising distribution companies; see this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/discom-debt-relief-token-charge.html">discom debt calculator</a>.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>States should publish their fiscal deficit and debt both with and without SASCI loans and off-budget borrowing, on the same page of the budget, so readers can see the full borrowing.</li>
<li>Each state&rsquo;s medium-term fiscal policy statement should explain any gap of more than half a percentage point between the budgeted and revised deficit, as Bihar&rsquo;s 2025-26 gap of 8.8 points shows is needed.</li>
<li>Debt-to-GSDP projections should be shown at the state&rsquo;s past GSDP growth as well as at its budget assumption, so a ratio cannot fall only because projected GSDP jumps.</li>
<li>Guarantees and the debt of state power companies should be reported as a share of GSDP alongside the state&rsquo;s own liabilities every year.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>All state figures come from PRS Legislative Research&rsquo;s budget analyses as read through search-engine text; the state budget documents themselves were not opened. Several cells could not be filled, including debt for Gujarat, interest shares for Uttar Pradesh, Telangana, Odisha and Jharkhand, and 2025-26 revised deficits for {len(S) - len(RE_KNOWN)} states. Telangana&rsquo;s interest share is reported to have fallen from 17% of revenue receipts in 2024-25 to 9% in 2025-26, a change this piece could not explain and so left out. Whether the 16th Finance Commission kept the 15th&rsquo;s extra 0.5% of GSDP of borrowing room for power-sector reform could not be confirmed. The Union&rsquo;s figures and the states&rsquo; are not strictly comparable. States not covered here, including Assam, Chhattisgarh and Himachal Pradesh, are left out rather than estimated.</p>
"""

sources = ("State figures: PRS Legislative Research, State Budget Analyses 2026-27 for Punjab, Madhya Pradesh, Andhra Pradesh, Rajasthan, Kerala, Odisha, Meghalaya, Telangana, Tamil Nadu, Uttar Pradesh, Bihar, West Bengal, Karnataka, Maharashtra, Haryana, Jharkhand and Gujarat (February&ndash;March 2026), as indexed by search engines; PRS Union Budget Analysis 2026-27; PRS State of State Finances (October 2025) for the all-states SASCI comparison. "
           "16th Finance Commission recommendations (3% of GSDP limit for 2026-31; ending off-budget borrowing; discom privatisation and discom debt of 2.3&ndash;2.5% of GSDP): PRS state analyses; CRISIL Ratings (March 2026); Drishti IAS summaries (February&ndash;March 2026). "
           "Uttar Pradesh rupee liabilities, Tamil Nadu guarantee shares and Gujarat&rsquo;s interest share are this blog&rsquo;s arithmetic from PRS figures (builder in the repository at out/research/state-deficits/). Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/who-collects-indias-gst-and-who.html", "Who Collects India&rsquo;s GST, and Who Actually Gets It Back"),
    ("https://masaladeutsch.blogspot.com/2026/08/would-more-sgst-fix-donor-state-problem.html", "Would More SGST Fix the &ldquo;Donor State&rdquo; Problem?"),
    ("https://masaladeutsch.blogspot.com/2026/08/securitising-deficit-what-it-would.html", "Is India a Dollar Salesman? Securitising the Deficit"),
    ("https://masaladeutsch.blogspot.com/2026/08/discom-debt-relief-token-charge.html", "DISCOM Debt Relief &mdash; Token Charge Calculator"),
]

build("Public Finance · 27 October 2026",
      "Seven States Plan to Borrow Above the New 3% Limit. Last Year, Most Missed Their Targets Anyway",
      "The 16th Finance Commission caps state deficits at 3% of GSDP from 2026-27. Seven of 17 budgets plan more, seven of the nine states with revised figures overshot last year, and the Centre&rsquo;s 50-year loans keep about 0.4% of GSDP out of the headline numbers.",
      body, sources, related, OUT)
print("above", [r[0] for r in ABOVE], "at", len(AT), "RE above", len(RE_ABOVE), "of", len(RE_KNOWN), "UP growth", round(UP_L_GROWTH, 1), round(UP_L26), round(UP_L27), "guj", round(GUJ_INT, 1), "TN", round(TN_GUAR/TN_GSDP*100,1), round(TN_POWER/TN_GSDP*100,1))
