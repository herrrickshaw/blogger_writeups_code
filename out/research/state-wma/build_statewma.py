import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-state-wma.html'

# Aggregate WMA limit for all states/UTs, Rs crore (RBI press releases as reported; 2026 figure is a committee recommendation)
LIMITS = [
    ("Before Feb 2016", 15360, "Earlier formula"),
    ("Feb 2016", 32225, "Revised formula"),
    ("Apr 2021", 47010, "Shrivastava committee"),
    ("Jul 2024", 60118, "Finance secretaries&rsquo; group"),
    ("Jan 2026", 61008, "Delhi added"),
    ("Sep 2026 (proposed)", 67839, "Prasad committee"),
]
OLD, NEW = 61008, 67839
RISE = (NEW / OLD - 1) * 100
DELHI = 61008 - 60118

# Usage days, all states (ICRA, May 2025 and June 2026)
WMA_DAYS = {"FY2024": 2029, "FY2025": 1873, "FY2026": 1586}
OD_DAYS = {"FY2025": 570, "FY2026": 386}
SDF = {"FY2025": (16, 2809), "FY2026": (19, 3008)}

# Surplus cash parked by states in 14-day intermediate treasury bills, monthly average (ICRA): Rs lakh crore
ITB_APR26, ITB_MAY26 = 2.0, 1.6
ITB_X_LO = ITB_MAY26 * 1e5 / OLD
ITB_X_HI = ITB_APR26 * 1e5 / OLD

# Year-end bunching of market loans (CCIL for FY25; NSE-Cogencis for Q4 FY26), Rs lakh crore
FY25_TOTAL, FY25_Q4 = 10.73, 4.34
Q4_SHARE_25 = FY25_Q4 / FY25_TOTAL * 100
Q4_FY26, Q4_FY26_PLAN = 5.23, 4.99

REPO = 5.50   # after the RBI's 7 October 2026 hike


def pct(a, b):
    return (b / a - 1) * 100


def chart_limits():
    W, L, top, bw, gap = 400, 34, 34, 44, 18
    base = 200
    sc = (base - top - 16) / 70000
    H = base + 46
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Aggregate ways-and-means advance limit for states, Rs crore, from before 2016 to the 2026 proposal.">',
         f'<text x="4" y="12" font-size="12" fill="#495057">Ways-and-means limit for all states, Rs crore</text>',
         f'<text x="4" y="25" font-size="9.5" fill="#6c757d">Last bar (outlined) is a recommendation, not yet in force</text>']
    for g in (0, 20000, 40000, 60000):
        y = base - g * sc
        s.append(f'<line x1="{L}" x2="{W - 4}" y1="{y:.1f}" y2="{y:.1f}" stroke="#dee2e6"/>')
        s.append(f'<text x="{L - 4}" y="{y + 3:.1f}" font-size="8.5" fill="#6c757d" text-anchor="end">{g // 1000}k</text>')
    for i, (lab, v, _) in enumerate(LIMITS):
        x = L + 10 + i * (bw + gap)
        h = v * sc
        if "proposed" in lab:
            s.append(f'<rect x="{x}" y="{base - h:.1f}" width="{bw}" height="{h:.1f}" fill="#fff" stroke="#1c5d99" stroke-width="1.6" stroke-dasharray="4 2"/>')
        else:
            s.append(f'<rect x="{x}" y="{base - h:.1f}" width="{bw}" height="{h:.1f}" fill="#1c5d99"/>')
        s.append(f'<text x="{x + bw / 2}" y="{base - h - 4:.1f}" font-size="9" fill="#212529" text-anchor="middle">{v:,}</text>')
        short = lab.replace(" (proposed)", "*").replace("Before ", "pre-")
        s.append(f'<text x="{x + bw / 2}" y="{base + 13}" font-size="9" fill="#212529" text-anchor="middle">{short}</text>')
    s.append(f'<text x="4" y="{H - 16}" font-size="9" fill="#6c757d">RBI press releases as reported. * Sep 2026 committee proposal.</text>')
    s.append(f'<text x="4" y="{H - 4}" font-size="9" fill="#6c757d">Apr 2021 limit applied from Apr 2022, after an interim Rs 51,560 crore.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_limits():
    rows, prev = [], None
    for lab, v, note in LIMITS:
        ch = "&mdash;" if prev is None else f"{pct(prev, v):+.1f}%"
        rows.append((lab, f"{v:,}", ch, note))
        prev = v
    return table(["When", "Limit (Rs crore)", "Change", "Set by"], rows)


def t_tiers():
    return table(["Tier", "Security", "Rate", "At 5.50% repo"],
                 [("1. SDF", "State&rsquo;s own securities", "Repo &minus; 1", f"{REPO - 1:.2f}%"),
                  ("2. WMA", "None, capped", "Repo", f"{REPO:.2f}%"),
                  ("3. Overdraft", "None", "Repo + 2 / + 5", f"{REPO + 2:.2f}% / {REPO + 5:.2f}%")])


def t_usage():
    return table(["All states", "FY2024", "FY2025", "FY2026"],
                 [("WMA, state-days", f"{WMA_DAYS['FY2024']:,}", f"{WMA_DAYS['FY2025']:,}", f"{WMA_DAYS['FY2026']:,}"),
                  ("Overdraft, state-days", "&mdash;", f"{OD_DAYS['FY2025']}", f"{OD_DAYS['FY2026']} (five-year low)"),
                  ("SDF, state-days (states using it)", "&mdash;", f"{SDF['FY2025'][1]:,} ({SDF['FY2025'][0]})", f"{SDF['FY2026'][1]:,} ({SDF['FY2026'][0]})")])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>Rs {NEW:,} cr</b><span>proposed limit on states&rsquo; short-term RBI advances, up {RISE:.1f}% from Rs {OLD:,} crore</span></div>
<div class="gb-stat"><b>Rs {ITB_MAY26:g}&ndash;{ITB_APR26:g} lakh cr</b><span>states&rsquo; spare cash parked in 14-day treasury bills each month in April&ndash;May 2026: {ITB_X_LO:.1f}&ndash;{ITB_X_HI:.1f} times the whole limit</span></div>
<div class="gb-stat"><b>250+ days</b><span>Punjab and Himachal Pradesh each spent on a ways-and-means advance in 2025-26, about two-thirds of the year</span></div>
<div class="gb-stat"><b>{Q4_SHARE_25:.0f}%</b><span>of states&rsquo; 2024-25 market borrowing came in the last three months of the year</span></div>
</div>'''

body = f"""
{stats}

<p>A state government&rsquo;s bank is the Reserve Bank of India (RBI). When tax and transfer receipts arrive later than salaries, pensions and contractor bills fall due, the RBI lends the state money for a few days or weeks. That short-term credit is called a ways-and-means advance (WMA), and the RBI caps how much each state can draw. On 29 September 2026 an RBI advisory committee chaired by I S N Prasad, a former Additional Chief Secretary of Karnataka, recommended raising the cap for all states and union territories together from Rs {OLD:,} crore to Rs {NEW:,} crore, an increase of {RISE:.1f}%. The RBI has said it will examine the report; the new limits are not yet in force.</p>

<p>The number is small next to state budgets, and that is the point of this piece. Using the RBI&rsquo;s past press releases and rating agency ICRA&rsquo;s counts of how often states draw on the facility, it sets out how the limit has moved, how the three tiers of RBI credit work, which states lean on them most, and why the same states collectively hold several times the whole limit in idle cash.</p>

<h2 class="gb-h2">Three tiers, in a fixed order</h2>
<p>States draw on the RBI in sequence. First comes the Special Drawing Facility (SDF), which is secured against the state&rsquo;s own investments in central government securities and treasury bills, and part of its Consolidated Sinking Fund (CSF, money set aside to repay loans) and Guarantee Redemption Fund (GRF). Next is the ordinary WMA, which is unsecured and capped. Only when both are used up does the state&rsquo;s account go into overdraft (OD). Each step costs more.</p>
{t_tiers()}
<p>The rates are the terms the RBI published in 2021-22. SDF borrowing against sinking and guarantee fund holdings is charged at repo minus 2 points. A WMA outstanding for more than three months is charged repo plus 1. Overdraft costs repo plus 2 points up to the size of the state&rsquo;s WMA limit and repo plus 5 points beyond it.</p>
<p>Overdraft has a time limit. Under the RBI&rsquo;s standing rules, a state can stay in overdraft for at most 14 consecutive working days and 36 working days in a quarter; beyond that the RBI stops its payments. During the pandemic those limits were relaxed to 21 and 50 days until March 2022. The 2026 committee proposes tightening them to 10 consecutive days and 30 days a quarter, and letting states use 75% of their sinking and guarantee fund investments for the SDF instead of 50%.</p>

<h2 class="gb-h2">How the limit has moved</h2>
{chart_limits()}
{t_limits()}
<p>The limit doubled in 2016. In April 2021 the RBI accepted the recommendations of an advisory committee chaired by Sudhir Shrivastava and set the limit at Rs 47,010 crore, though a higher pandemic-era interim limit of Rs 51,560 crore ran until March 2022. In July 2024 a group of state finance secretaries, working from recent expenditure data, took it up by over a quarter. The January 2026 step of Rs {DELHI} crore was not a policy change: it was Delhi&rsquo;s own limit, added when the Delhi government moved its banking to the RBI. The 2026 proposal also changes the method. Earlier limits were worked out from each state&rsquo;s total expenditure; the committee would base them on revenue receipts after certain adjustments, using 2022-23 to 2024-25 accounts, revise them every year rather than every few years, and cap each year&rsquo;s rise at 4%. No state&rsquo;s limit would fall below what it has now.</p>

<h2 class="gb-h2">Who uses it</h2>
{t_usage()}
<p>A &ldquo;state-day&rdquo; is one state on the facility for one day, so 1,586 WMA state-days in 2025-26 means, for example, six states on WMA for most of the year or many states for a few weeks each. ICRA&rsquo;s counts show use of the WMA and overdraft windows falling for two years running while the cheaper SDF rose: 19 states used it for 3,008 days in 2025-26.</p>
<p>The users are concentrated. In 2024-25, Andhra Pradesh, Manipur and Telangana each spent more than 250 days on WMA and more than 80 days in overdraft; Kerala was on WMA for more than 288 days and Punjab more than 201. In 2025-26 Manipur&rsquo;s WMA days fell by about 190 and Kerala, Jammu and Kashmir, Telangana and Andhra Pradesh each cut theirs by 62 to 100 days, while Punjab and Himachal Pradesh were each on WMA for more than 250 days, Himachal&rsquo;s count up 103. The pattern is older than the latest data: a Bank of Baroda study found Andhra Pradesh used the SDF on 133 of the 153 days from April to August 2022, WMA on 122 and overdraft on 51.</p>
<p>Several of these states also appear in the earlier piece on this blog, &ldquo;Seven States Plan to Borrow Above the New 3% Limit. Last Year, Most Missed Their Targets Anyway&rdquo;: Punjab, Andhra Pradesh and Kerala budget deficits above the Finance Commission&rsquo;s cap for 2026-27, and Punjab already spends 23% of its revenue on interest. A state that lives on WMA is usually not short of cash for a few days; it is financing a gap that its budget did not admit to.</p>

<h2 class="gb-h2">The cash nobody uses</h2>
<p>At the other end, any state whose cash is above its minimum balance has the surplus invested automatically by the RBI in 14-day intermediate treasury bills. These bills cannot be traded and pay less than a state&rsquo;s own market loans cost. ICRA puts states&rsquo; average monthly holdings at about Rs {ITB_APR26:g} lakh crore in April 2026 and Rs {ITB_MAY26:g} lakh crore in May 2026: {ITB_X_LO:.1f} to {ITB_X_HI:.1f} times the entire WMA limit for all states, sitting idle while a handful of states overdraw. The cost is a negative carry: those states are borrowing at market rates and lending the money back to the RBI at a lower one.</p>
<p>Part of the reason is timing. States raised Rs {FY25_Q4:g} lakh crore of their Rs {FY25_TOTAL:g} lakh crore of 2024-25 market loans, about {Q4_SHARE_25:.0f}%, in January&ndash;March. In January&ndash;March 2026 they raised Rs {Q4_FY26:g} lakh crore against an indicated Rs {Q4_FY26_PLAN:g} lakh crore. Borrowing bunched at the year&rsquo;s end leaves cash balances high at the start of the next year and pushes up the interest all states pay. The committee asked states to spread their borrowing through the year and to use SDF, WMA and overdraft only for genuine short gaps.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The RBI should publish each state&rsquo;s SDF, WMA and overdraft days every quarter, so a state that is on credit for most of the year shows up in its own budget debate rather than in a rating agency&rsquo;s note.</li>
<li>A state on WMA or overdraft for more than 180 days in a year should have to explain the gap in its next medium-term fiscal policy statement, as a structural deficit rather than a timing gap.</li>
<li>States with large treasury-bill balances should be able to lend short-term to other states through the RBI at a rate between the treasury-bill yield and the WMA rate, so idle cash is used before the RBI lends.</li>
<li>Each state&rsquo;s quarterly borrowing calendar should cap the January&ndash;March share, for example at 35% of the year&rsquo;s gross borrowing, unless the state publishes the reason for going over.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The RBI&rsquo;s website could not be opened from the research machine, so the committee report, the press releases and the RBI&rsquo;s State Finances tables were read only through search-engine text and news reports. State-by-state limits, both current and proposed, are in annexes that were not seen. The interest rates in the tiers table are the terms published in 2021-22 and may have changed since; whether the standing 14-day and 36-day overdraft limits are the ones in force today was not confirmed from an RBI document, though the committee&rsquo;s proposal to cut them from those numbers suggests so. ICRA&rsquo;s state counts are thresholds (&ldquo;more than 250 days&rdquo;), not exact figures, and overdraft days for 2023-24 were not found. The treasury-bill figures are ICRA&rsquo;s monthly averages; the RBI&rsquo;s own March-end series was not read cleanly. The 2025-26 full-year market borrowing total was not found, so the January&ndash;March share is given only for 2024-25.</p>
"""

sources = ("RBI Advisory Committee on Ways and Means Advances to State Governments (chair I S N Prasad), report and RBI press release of 29 September 2026, as reported by Business Standard, PRS Legislative Research (Monthly Policy Review, September 2026), ICRA (thematic note, 1 October 2026) and other news summaries. "
           "Earlier limits: RBI press releases of January 2016 (Rs 32,225 crore), April 2021 (Rs 47,010 crore, Sudhir Shrivastava committee; interim Rs 51,560 crore), 28 June 2024 (Rs 60,118 crore from 1 July 2024) and January 2026 (Delhi, Rs 890 crore), as reported. "
           "Interest rates and overdraft rules: RBI press releases on the WMA scheme, 2021-22. Usage days: ICRA, state government finance reports of May 2025 and June 2026, as reported by Business Standard; Bank of Baroda Economics, State Finances (October 2022). "
           "Treasury-bill balances: ICRA monthly state finance compendium. Market borrowing: CCIL SDL quarterly (2024-25); NSE-Cogencis Debt Market Report Q4 FY26. Repo rate: RBI policy of 7 October 2026. Ratios and the multiple of the WMA limit are this blog&rsquo;s arithmetic (builder in the repository at out/research/state-wma/). Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/who-collects-indias-gst-and-who.html", "Who Collects India&rsquo;s GST, and Who Actually Gets It Back"),
    ("https://masaladeutsch.blogspot.com/2026/08/would-more-sgst-fix-donor-state-problem.html", "Would More SGST Fix the &ldquo;Donor State&rdquo; Problem?"),
    ("https://masaladeutsch.blogspot.com/2026/08/discom-debt-relief-token-charge.html", "DISCOM Debt Relief &mdash; Token Charge Calculator"),
    ("https://masaladeutsch.blogspot.com/2026/10/biogas-is-priority-sector-loan-43.html", "Biogas Is a Priority-Sector Loan. The 43% Higher CBG Price Is Worth About 50 Times the Cost of the Repo Hike"),
]

build("Public Finance · 30 October 2026",
      "States Can Draw Rs 61,008 Crore of Short-Term Credit From the RBI. A Few Live on It, While the Rest Park Up to Three Times That in Treasury Bills",
      f"An RBI committee wants the ways-and-means limit raised {RISE:.0f}% to Rs {NEW:,} crore and overdrafts cut short. The bigger problem is distribution: Punjab and Himachal were on RBI credit for two-thirds of 2025-26, while states together held Rs 1.6&ndash;2 lakh crore of idle cash.",
      body, sources, related, OUT)
print("rise", round(RISE, 2), "itb x", round(ITB_X_LO, 2), round(ITB_X_HI, 2), "q4", round(Q4_SHARE_25, 1), [round(pct(a[1], b[1]), 1) for a, b in zip(LIMITS, LIMITS[1:])])
