import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-nsap-pensions.html'

# --- Cabinet decision, 14 October 2026 (PIB PRID 2323264) and PIB backgrounder (22 October 2026)
OUTLAY_2631 = 53428          # Rs crore, 2026-27 to 2030-31
BENEF = 3.20                 # crore beneficiaries, 36 States/UTs
DIS_OLD, DIS_NEW = (300, 500), (375, 625)
DIS_B_OLD, DIS_B_NEW = 8.33, 27.48   # lakh disability-pension beneficiaries
OUTLAY_YR = OUTLAY_2631 / 5
assert round(OUTLAY_YR) == 10686
PER_B_MONTH = OUTLAY_YR * 1e7 / (BENEF * 1e7) / 12
assert round(PER_B_MONTH) == 278
assert DIS_NEW[0] == DIS_OLD[0] * 1.25 and DIS_NEW[1] == DIS_OLD[1] * 1.25   # RPwD Act: 25% higher

# --- Budget: Rajya Sabha USQ 429 (6 Dec 2023)
OUTLAY_2126 = 47808.31
ALLOC_2324 = 9636.32
OUTLAY_RISE = (OUTLAY_YR / (OUTLAY_2126 / 5) - 1) * 100
assert round(OUTLAY_RISE) == 12
# Lok Sabha USQ 2477 (6 Aug 2024): old-age beneficiaries
OLD_AGE_B = 21656162

# --- Prices: RBI Handbook Table 34, CPI for agricultural labourers (1986-87=100), annual averages
CPI_AL = {"2007-08": 409, "2011-12": 611, "2012-13": 672, "2024-25": 1299}
CPI_AL_YOY_SEP26 = 6.30      # Labour Bureau, Sep 2026, new 2019=100 series

def real(amount, base):
    m = CPI_AL["2024-25"] / CPI_AL[base]
    return m, amount * m, amount / m

M07, NEED_200, WORTH_200 = real(200, "2007-08")
M11, NEED_500, WORTH_500 = real(500, "2011-12")
M12, NEED_300, WORTH_300 = real(300, "2012-13")
assert round(WORTH_200) == 63 and round(NEED_200) == 635
assert round(NEED_300) == 580 and round(NEED_500) == 1063
DIS_REAL_SH = DIS_NEW[0] / NEED_300 * 100
assert round(DIS_REAL_SH) == 65

# Cost of restoring the 60-79 old-age amount to its 2007 value, upper bound (all old-age beneficiaries)
RESTORE_CR = OLD_AGE_B * (NEED_200 - 200) * 12 / 1e7
assert 11000 < RESTORE_CR < 11600

# --- World Bank $3.00/day (2021 PPP) line, converted at the 2021 PPP rate for India
LINE_DAY, LINE_MONTH = 58, 1777
SH_200 = 200 / LINE_MONTH * 100
assert round(SH_200) == 11

# --- State top-ups for old age (60-79), Rs/month: Lok Sabha USQ 357 (21 July 2026), annex
TOPUP = [("Andhra Pradesh", 3800), ("Haryana", 2800), ("A&amp;N Islands", 2300), ("Puducherry", 2300),
         ("Telangana", 1816), ("Kerala", 1400), ("Arunachal Pradesh", 1300), ("Chandigarh", 1000),
         ("Tamil Nadu", 1000), ("Bihar", 900), ("Gujarat", 800), ("Jharkhand", 800), ("Rajasthan", 800),
         ("Madhya Pradesh", 400), ("Chhattisgarh", 300), ("Assam", 50)]
RANGES = [("Delhi", "1,800&ndash;2,300"), ("Karnataka", "400&ndash;1,000")]
assert TOPUP == sorted(TOPUP, key=lambda x: -x[1])

# --- CAG Report No. 10 of 2023
CAG_SHORT_CR, CAG_SHORT_B, CAG_MONTHLY = 61.71, 92602, 11
CAG_DEAD_B, CAG_DEAD_CR = 2103, 2


def rs(v):
    return f"{v:,}"


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_components():
    rows = [
        ("Old age, 60&ndash;79", "&#8377;200", "2007", "Unchanged"),
        ("Old age, 80+", "&#8377;500", "2011", "Unchanged"),
        ("Widow, 40&ndash;79", "&#8377;300", "2012", "Unchanged"),
        ("Widow, 80+", "&#8377;500", "2011", "Unchanged"),
        ("Disability, under 80", "&#8377;300", "2012", "&#8377;375"),
        ("Disability, 80+", "&#8377;500", "2011", "&#8377;625"),
        ("Family benefit", "&#8377;20,000 once", "2012", "Unchanged"),
    ]
    return table(["Scheme", "Centre pays", "Since", "From 2026-27"], rows)


def t_real():
    rows = [
        ("&#8377;200 old age", "2007-08", f"{M07:.2f}&times;", f"&#8377;{NEED_200:,.0f}", f"&#8377;{WORTH_200:.0f}"),
        ("&#8377;500 aged 80+", "2011-12", f"{M11:.2f}&times;", f"&#8377;{NEED_500:,.0f}", f"&#8377;{WORTH_500:.0f}"),
        ("&#8377;300 widow, disability", "2012-13", f"{M12:.2f}&times;", f"&#8377;{NEED_300:,.0f}", f"&#8377;{WORTH_300:.0f}"),
    ]
    return table(["Amount", "Set in", "Prices since", "Same value in 2024-25", "Buys at set-year prices"], rows)


def t_states():
    rows = [(st, rs(v), rs(v + 200), f"{(v + 200) / LINE_MONTH * 100:.0f}%") for st, v in TOPUP]
    rows += [(st, r, "", "") for st, r in RANGES]
    return table(["State", "Top-up, &#8377;", "Total, &#8377;", "Of $3 line"], rows)


def chart_states():
    W, L, R, top, bh, gap = 340, 126, 300, 44, 20, 8
    n = len(TOPUP)
    H = top + n * (bh + gap) + 22
    mx = TOPUP[0][1]
    sc = (R - L) / mx
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="State top-ups on the Centre&rsquo;s &#8377;200 old-age pension, rupees a month: '
         + ", ".join(f"{st.replace('&amp;', 'and')} {v:,}" for st, v in TOPUP) + '.">',
         '<text x="4" y="13" font-size="13" fill="#495057">State top-up on the Centre&rsquo;s &#8377;200</text>',
         '<text x="4" y="30" font-size="11" fill="#6c757d">Old-age pension, age 60&ndash;79, &#8377; a month</text>']
    for i, (st, v) in enumerate(TOPUP):
        y = top + i * (bh + gap)
        w = max(v * sc, 2)
        s.append(f'<text x="{L - 6}" y="{y + bh / 2 + 4:.1f}" font-size="13" fill="#212529" text-anchor="end">{st}</text>')
        s.append(f'<rect x="{L}" y="{y}" width="{w:.1f}" height="{bh}" fill="#0b3d6b"/>')
        if w > 60:
            s.append(f'<text x="{L + w - 5:.1f}" y="{y + bh / 2 + 4:.1f}" font-size="13" fill="#fff" text-anchor="end">{v:,}</text>')
        else:
            s.append(f'<text x="{L + w + 5:.1f}" y="{y + bh / 2 + 4:.1f}" font-size="13" fill="#212529">{v:,}</text>')
    s.append(f'<text x="4" y="{H - 6}" font-size="10.5" fill="#6c757d">Source: Lok Sabha USQ 357, 21 July 2026, annex</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>&#8377;200</b><span>a month: the Centre&rsquo;s old-age pension for those aged 60&ndash;79, unchanged since 2007 and kept unchanged for 2026-31</span></div>
<div class="gb-stat"><b>&#8377;{WORTH_200:.0f}</b><span>what &#8377;200 buys in 2007-08 rupees, deflated by the price index for agricultural labourers to 2024-25</span></div>
<div class="gb-stat"><b>{BENEF:.2f} crore</b><span>people on the Centre&rsquo;s pensions and family benefit across 36 States and UTs</span></div>
<div class="gb-stat"><b>&#8377;{OUTLAY_2631:,} cr</b><span>approved for 2026-31, about &#8377;{OUTLAY_YR:,.0f} crore a year, {OUTLAY_RISE:.0f}% more a year than 2021-26</span></div>
</div>'''

body = f"""
{stats}

<p>On 14 October 2026 the Union Cabinet extended the National Social Assistance Programme, the Centre&rsquo;s pension scheme for poor elderly people, widows and disabled people, for five more years, to March 2031. It renamed the programme the Pradhan Mantri Samajik Sahayata Yojana, with the old-age, widow and disability pensions becoming the PM Vridhavastha, PM Vidhawa and PM Divyangjan Pension Yojanas, and the family benefit becoming the PM Parivar Labh Yojana. It approved &#8377;{OUTLAY_2631:,} crore for the five years.</p>

<p>It raised one amount. Disability pensions go up by a quarter, and more people will qualify. The old-age pension stays at &#8377;200 a month for people aged 60 to 79, the amount set in 2007. At the prices farm labourers pay, that &#8377;200 now buys about what &#8377;{WORTH_200:.0f} did then. Most pensioners get more because their state adds a top-up, but those top-ups range from &#8377;50 in Assam to &#8377;3,800 in Andhra Pradesh.</p>

<h2 class="gb-h2">What the Cabinet changed, and what it left alone</h2>

<p>The programme pays only households below the poverty line. The Centre sets a minimum amount and funds it; states administer it and may add their own money. The Cabinet note says the old-age, widow and family benefit schemes &ldquo;continue unchanged&rdquo;.</p>

{t_components()}
<p class="gb-note">Centre&rsquo;s share, per month unless stated. Old-age amounts: &#8377;75 when the scheme began in 1995, &#8377;200 from 2007, &#8377;500 for those 80 and over from 2011; widow and disability pensions rose from &#8377;200 to &#8377;300 in 2012 (Lok Sabha USQ 1159, 11 February 2025).</p>

<p>The disability change does three things. The pension rises from &#8377;{DIS_OLD[0]} to &#8377;{DIS_NEW[0]} below age 80 and from &#8377;{DIS_OLD[1]} to &#8377;{DIS_NEW[1]} above it. The qualifying level of disability falls from 80% to 40%, the &ldquo;benchmark disability&rdquo; of the Rights of Persons with Disabilities Act, 2016, and the pension is now payable from birth rather than from age 18. The government&rsquo;s backgrounder expects disability beneficiaries to rise from {DIS_B_OLD} lakh to {DIS_B_NEW} lakh. The 25% rise is the margin the 2016 Act requires: disability assistance must be at least a quarter higher than similar schemes. Guidelines are due within three months of the decision.</p>

<h2 class="gb-h2">What &#8377;200 bought in 2007, and buys now</h2>

<p>The Consumer Price Index for Agricultural Labourers, the index the government uses to revise rural job-guarantee wages, averaged {CPI_AL["2007-08"]} in 2007-08 and {CPI_AL["2024-25"]:,} in 2024-25 (1986-87 = 100). Prices for farm labourers&rsquo; households rose {M07:.2f} times in those 17 years. To buy what it bought when it was set, the &#8377;200 would have had to be &#8377;{NEED_200:,.0f} in 2024-25. Read the other way, &#8377;200 in 2024-25 bought what &#8377;{WORTH_200:.0f} did in 2007-08.</p>

{t_real()}
<p class="gb-note">CPI-AL annual averages from the RBI Handbook of Statistics on the Indian Economy, Table 34. 2024-25 is the last full year on the 1986-87 base; the index was re-based to 2019 = 100 from June 2025 and rose a further {CPI_AL_YOY_SEP26:.2f}% in the year to September 2026, so today&rsquo;s gap is wider than shown.</p>

<p>The new disability pension of &#8377;{DIS_NEW[0]} is {DIS_REAL_SH:.0f}% of what the 2012 amount of &#8377;300 would need to be in 2024-25. The increase recovers part of the loss and is not a real rise.</p>

<h2 class="gb-h2">Against the World Bank&rsquo;s poverty line</h2>

<p>The World Bank&rsquo;s international extreme-poverty line is $3.00 a day at 2021 purchasing-power prices. Converted at the 2021 rate for India it is about &#8377;{LINE_DAY} a day, or &#8377;{LINE_MONTH:,} a month for one person. The Centre&rsquo;s &#8377;200 is about &#8377;6.6 a day, {SH_200:.0f}% of that line. The government told the Lok Sabha in March 2025 that, with state top-ups, the average pension in most states is about &#8377;1,000, roughly 56% of the line. These comparisons flatter the pension, because the line is in 2021 prices and the pension in 2026 rupees.</p>

<h2 class="gb-h2">Where you live decides the pension</h2>

<p>In July 2026 the government told the Lok Sabha that about 3 crore people get the central pensions and about 5.9 crore more are on state-funded schemes, roughly 9 crore in all. State top-ups on the central amount range from &#8377;50 to &#8377;5,700 a month, the highest being Andhra Pradesh&rsquo;s disability pension. The annex to that answer gives the top-up for old-age pensioners aged 60&ndash;79:</p>

{chart_states()}

{t_states()}
<p class="gb-note">Total = top-up plus the Centre&rsquo;s &#8377;200. &ldquo;Of $3 line&rdquo; = total as a share of &#8377;{LINE_MONTH:,} a month. Delhi and Karnataka pay a range by age or category. States not listed were truncated or absent in the annex as read.</p>

<p>The states&rsquo; own announcements put some totals higher than the annex. Andhra Pradesh pays &#8377;4,000 under NTR Bharosa (&#8377;6,000 for disabled people) to about 62 lakh pensioners, of whom 9.34 lakh are on the central scheme, at a cost of &#8377;33,485 crore in 2026-27. That one state&rsquo;s pension bill is about three times the Centre&rsquo;s yearly NSAP outlay for the whole country. Haryana raised its old-age allowance to &#8377;3,200 from 1 November 2025; it was &#8377;100 when it began in 1987. Bihar raised its pension from &#8377;400 to &#8377;1,100 from June 2025 for about 1.11 crore people.</p>

<p>At the other end, the Comptroller and Auditor General found in 2023 that pensioners in Goa, Nagaland, Manipur, Punjab and Assam received only &#8377;200 to &#8377;250, because those states added nothing or almost nothing to the central amount for NSAP beneficiaries.</p>

<h2 class="gb-h2">The budget has grown slowly</h2>

<p>The Centre set aside &#8377;{OUTLAY_2126:,.2f} crore for NSAP for 2021-26 and allocated &#8377;{ALLOC_2324:,.2f} crore in 2023-24. The new &#8377;{OUTLAY_2631:,} crore is &#8377;{OUTLAY_YR:,.0f} crore a year, {OUTLAY_RISE:.0f}% more a year than the 2021-26 outlay, in nominal terms, with more disabled people to cover. Spread across {BENEF:.2f} crore beneficiaries, it works out to about &#8377;{PER_B_MONTH:.0f} per person a month, consistent with amounts that stay mostly at &#8377;200 to &#8377;500.</p>

<p>A revision of the central amounts was considered for 2021-26 and not approved; in August 2024 the government told the Lok Sabha this was &ldquo;considering the available financial space&rdquo;. Parliament&rsquo;s Standing Committee on Rural Development, in its April 2025 report on the programme, called the amounts inadequate and asked for a periodic reassessment to reflect inflation and a larger central contribution. As a rough upper bound, paying all {OLD_AGE_B / 1e5:.1f} lakh old-age pensioners the 2007 value of &#8377;{NEED_200:,.0f} instead of &#8377;200 would cost about &#8377;{RESTORE_CR:,.0f} crore a year more, slightly more than the whole programme costs now.</p>

<h2 class="gb-h2">Late, short and sometimes to the dead</h2>

<p>The CAG&rsquo;s performance audit of NSAP (Report No. 10 of 2023) found that only {CAG_MONTHLY} States and UTs paid pensions monthly, as the guidelines require. States were slow to claim the Centre&rsquo;s second instalment, which delayed payments down the line. Pensions not paid from the date they became due left {CAG_SHORT_B:,} beneficiaries in 11 States and UTs short by &#8377;{CAG_SHORT_CR} crore. In 26 States and UTs, &#8377;{CAG_DEAD_CR} crore was paid for {CAG_DEAD_B:,} beneficiaries after they had died, and 2,243 people drew more than one pension. The CAG also found eligible people left out because no one went looking for them.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>Index the central amounts to CPI-AL and revise them every year, as rural job-guarantee wages already are, so the minimum stops being set only when a five-year renewal comes up.</li>
<li>Restore the old-age pension in steps. Moving the &#8377;200 to its 2007 value would roughly double the programme&rsquo;s cost, so a phased path over the 2026-31 cycle, published with the guidelines, would be easier to fund than a single jump.</li>
<li>Set a floor for the combined pension in states that add little or nothing, with central matching for poorer states, so a pensioner in Assam or Punjab is not left on &#8377;200 to &#8377;250.</li>
<li>Publish each state&rsquo;s payment frequency, days of delay and deaths struck off on the NSAP portal every month, so the CAG&rsquo;s findings can be tracked between audits.</li>
<li>Publish one annual table of each state&rsquo;s total pension by category, rather than leaving it to a Parliament question annex.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The CPI-AL calculation ends in 2024-25 because the index changed base in June 2025 and no official linking factor was found, so the real loss to today is understated. The World Bank conversion uses 2021 prices. The state top-up annex was read in part; some states were cut off, and its figures do not always match the states&rsquo; own announcements: Haryana&rsquo;s &#8377;2,800 top-up implies &#8377;3,000, below the &#8377;3,200 it has paid since November 2025, and Rajasthan&rsquo;s &#8377;800 top-up implies &#8377;1,000, while secondary sources give &#8377;1,450. The annex&rsquo;s date and reference period were not established. The disability guidelines, including how the 40% threshold will be certified and when payments at the new rate start, were not yet public. The restoration cost assumes every old-age beneficiary gets the 60&ndash;79 amount and uses the 2024 beneficiary count. The CAG audit covers 2017-21; no later audit was found.</p>
"""

sources = ("Cabinet decision: <a href=\"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2323264\">PIB, 14 October 2026</a>; "
           "<a href=\"https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/oct/doc_10230_20261022_14200001.pdf\">PIB backgrounder, 22 October 2026</a>; "
           "<a href=\"https://prsindia.org/policy/monthly-policy-review/october-2026\">PRS Monthly Policy Review, October 2026</a> (read through search text). "
           "Amount history, beneficiaries, state top-ups: Lok Sabha unstarred questions "
           "<a href=\"https://www.sansad.in/getFile/loksabhaquestions/annex/184/AU1159_RpZosw.pdf?source=pqals\">1159 (11 February 2025)</a>, 4109 (25 March 2025), 2477 (6 August 2024) and "
           "<a href=\"https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU357_yE0DCQ.pdf?source=lsapps\">357 (21 July 2026) with annex</a>. "
           "Family benefit amount: <a href=\"https://eparlib.nic.in/bitstream/123456789/2978407/1/AU1310_gQh2hv.pdf\">Lok Sabha unstarred question 1310 (2024)</a>. "
           "Budget: <a href=\"https://sansad.in/getFile/annex/262/AU429.pdf?source=pqars\">Rajya Sabha unstarred question 429 (6 December 2023)</a>. "
           "Prices: <a href=\"https://rbidocs.rbi.org.in/rdocs/Publications/PDFs/34T_HBIE3107202600704861E33A4A10A0C9B807828AABEA.PDF\">RBI Handbook of Statistics, Table 34 (31 July 2026)</a>; Labour Bureau CPI-AL release for September 2026 (search text). "
           "Poverty line: World Bank international poverty line of $3.00 a day (2021 PPP), June 2025 update; the rupee conversion is this blog&rsquo;s. "
           "Audit: <a href=\"https://cag.gov.in/uploads/download_audit_report/2023/Report-No.-10-of-2023_NSAP_English_PDF-A-064d229f832dad7.55068084.pdf\">CAG Report No. 10 of 2023</a> and "
           "<a href=\"https://cag.gov.in/uploads/PressRelease/PR-PRESS-RELEASE-ON-REPORT-NO-10-ENGLISH-064d24ae4473743-65161718.pdf\">CAG press release, 8 August 2023</a>. "
           "Committee: <a href=\"https://www.deccanherald.com/amp/story/india%2Fparl-panel-flags-delays-in-mgnrega-payments-calls-for-pension-reforms-in-nsap-3476193\">Deccan Herald, 3 April 2025</a>, on the Standing Committee&rsquo;s ninth report. "
           "States: <a href=\"https://www.newindianexpress.com/states/andhra-pradesh/2026/Sep/23/rs-33485-crore-for-ntr-bharosa-pensions-in-2026-27-minister-kondapalli-srinivas\">New Indian Express, 23 September 2026</a> (Andhra Pradesh); "
           "<a href=\"https://sewa.haryana.gov.in/old-age-samman-allowance-scheme\">Haryana Social Justice department</a>; "
           "<a href=\"https://www.business-standard.com/india-news/bihar-cm-releases-first-instalment-of-hiked-pension-to-10-mn-beneficiaries-125071100499_1.html\">Business Standard, 11 July 2025</a> (Bihar). "
           "Real values, shares, per-beneficiary and restoration costs are this blog&rsquo;s arithmetic (builder at out/research/nsap-pensions/).")

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/rural-job-guarantee-pay-rose-96-in-july.html", "Rural Job-Guarantee Pay Rose 9.6% in July. In Eight States It Buys Less Than in 2025"),
    ("https://masaladeutsch.blogspot.com/2026/08/a-17-rural-pay-rise-that-nobody-received.html", "A 17% Rural Pay Rise That Nobody Received"),
    ("https://masaladeutsch.blogspot.com/2026/08/cpi-inflation-heatmap-india-june-2026.html", "CPI Inflation Heatmap &mdash; India, June 2026"),
    ("https://masaladeutsch.blogspot.com/2026/10/most-of-what-indians-pay-for-health-is.html", "Most of What Indians Pay for Health Is Outpatient Care. Ayushman Bharat Pays Only for Hospital Stays"),
]

build("Welfare &middot; 8 November 2026",
      "The Centre&rsquo;s Old-Age Pension Has Been &#8377;200 a Month Since 2007. It Now Buys What &#8377;63 Did Then",
      "On 14 October the Cabinet renewed India&rsquo;s national pension scheme for the poor to 2031 with &#8377;53,428 crore, and raised only the disability pension. The old-age and widow amounts stay where they were set in 2007 and 2012, so what a pensioner gets depends almost entirely on the state.",
      body, sources, related, OUT)
print("per-yr", round(OUTLAY_YR), "rise%", round(OUTLAY_RISE, 1), "per-b/mo", round(PER_B_MONTH), "M07", round(M07, 3),
      "need200", round(NEED_200), "worth200", round(WORTH_200, 1), "need300", round(NEED_300), "need500", round(NEED_500),
      "dis real%", round(DIS_REAL_SH, 1), "restore", round(RESTORE_CR), "sh200", round(SH_200, 1))
