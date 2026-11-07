import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-poverty-brief.html'

# World Bank, "India's long-term poverty trend, 2011-12 to 2023-24" (technical note, April 2026),
# Figures 1-2; and PIP September 2026 update, Table 5. Rates in %, by survey year
# (2011 = 2011-12 CES, 2022 = 2022-23 HCES, 2023 = 2023-24 HCES).
POV = {  # line: {area: (2011, 2022, 2023)}
    '$3.00': {'All India': (27.1, 5.3, 2.6), 'Rural': (31.0, 6.2, 3.1), 'Urban': (17.4, 2.9, 1.4)},
    '$4.20': {'All India': (57.7, 23.9, 16.1), 'Rural': (64.9, 27.7, 19.3), 'Urban': (39.7, 14.3, 8.6)},
}
POOR_M = {'$3.00': (344, 75, 37), '$4.20': (732, 342, 233)}  # millions of people, technical note Fig 1B
LIFTED_420 = 496      # million, October 2026 Poverty and Equity Brief
LIFTED_300 = 307      # million, technical note
PPP = 19.47           # rupees per 2021 international dollar (technical note, footnote 2)
DAYS = 365 / 12

# Inequality, different yardsticks (Gini, 0-100)
GINI_CONS = (28.8, 25.5, 23.0)          # World Bank, consumption, 2011 / 2022 / 2023
GINI_RURAL, GINI_URBAN = (26.6, 23.7), (31.4, 28.4)   # MoSPI HCES 2022-23 / 2023-24 (x100)
GINI_EARN = 43.0                        # PLFS 2023-24 labour earnings, cited in technical note Annex 3
GINI_INC_WID = (52, 62)                 # World Inequality Database income Gini, 2004 / 2023 (World Bank brief, Apr 2025)
TOP10_INC, TOP1_INC, TOP1_WEALTH = 57.7, 22.6, 40.1   # WID shares, %
TOP10_CONS = 20.5                       # WDI: top 10% share of consumption, 2023
# Lok Sabha unstarred Q1274, 27 July 2026: individuals reporting gross total income of Rs 100 crore or more
RICH = [('2021-22', 142), ('2022-23', 301), ('2023-24', 284), ('2024-25', 415), ('2025-26', 576)]

line300_day, line420_day = 3.00 * PPP, 4.20 * PPP
line300_mo, line420_mo = line300_day * DAYS, line420_day * DAYS
assert round(line300_day, 2) == 58.41 and round(line420_day) == 82

a300, a420 = POV['$3.00']['All India'], POV['$4.20']['All India']
yr1_300 = (a300[1] - a300[2]) / a300[1] * 100          # one-year fall, %
yr1_420 = (a420[1] - a420[2]) / a420[1] * 100
assert round(yr1_420) == 33 and round(yr1_300) == 51
pp_per_yr_420 = (a420[0] - a420[2]) / 12
assert round(pp_per_yr_420, 1) == 3.5
share_of_drop_in_last_year = (a420[1] - a420[2]) / (a420[0] - a420[2]) * 100   # of the 12-year fall, how much came in 2023
assert round(share_of_drop_in_last_year) == 19
diff_poor = POOR_M['$4.20'][0] - POOR_M['$4.20'][2]
assert diff_poor == 499
rich_jump = (415 - 284) / 284 * 100
assert round(rich_jump) == 46


def table(head, rows, num_from=1):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_poverty():
    rows = []
    for line in ('$3.00', '$4.20'):
        for area, (a, b, c) in POV[line].items():
            rows.append([f'{line} {area}', f'{a:.1f}', f'{c:.1f}'])
    return table(['Line, area', '2011-12, %', '2023-24, %'], rows)


def t_rich():
    rows = [[ay, str(n)] for ay, n in RICH]
    return table(['Assessment year', 'People reporting Rs 100 cr+'], rows)


def chart_gini():
    bars = [
        ('Consumption 2011-12', GINI_CONS[0]),
        ('Consumption 2022-23', GINI_CONS[1]),
        ('Consumption 2023-24', GINI_CONS[2]),
        ('Earnings 2023-24', GINI_EARN),
        ('Income (WID) 2023', GINI_INC_WID[1]),
    ]
    W, L0, top, row, bh = 360, 172, 46, 34, 22
    H = top + row * len(bars) + 40
    mx = 70
    pw = W - L0 - 30
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Gini index for India on five yardsticks: consumption 28.8 in 2011-12, 25.5 in 2022-23 and 23.0 in 2023-24; labour earnings 43 in 2023-24; income 62 in 2023 on World Inequality Database estimates.">',
         '<text x="10" y="15" font-size="14" fill="#495057">India&rsquo;s Gini index on five yardsticks</text>',
         '<text x="10" y="32" font-size="11.5" fill="#6c757d">0 = everyone equal, 100 = one person has everything</text>']
    for i, (lab, v) in enumerate(bars):
        y = top + i * row
        w = v / mx * pw
        s.append(f'<text x="{L0 - 6}" y="{y + 16}" font-size="12.5" fill="#212529" text-anchor="end">{lab}</text>')
        s.append(f'<rect x="{L0}" y="{y}" width="{w:.1f}" height="{bh}" fill="#1c5d99"/>')
        s.append(f'<text x="{L0 + w + 4:.1f}" y="{y + 16}" font-size="12.5" fill="#212529">{v:g}</text>')
    s.append(f'<text x="10" y="{H - 18}" font-size="10.5" fill="#6c757d">Sources: World Bank (consumption; PLFS earnings);</text>')
    s.append(f'<text x="10" y="{H - 4}" font-size="10.5" fill="#6c757d">World Inequality Database via World Bank.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{a420[0]:.1f}% &rarr; {a420[2]:.1f}%</b><span>of Indians below the World Bank&rsquo;s $4.20-a-day line, 2011-12 to 2023-24; about {LIFTED_420} million people moved above it</span></div>
<div class="gb-stat"><b>{a300[0]:.1f}% &rarr; {a300[2]:.1f}%</b><span>in extreme poverty, below $3.00 a day: about Rs {line300_day:.0f} a person a day in 2021 prices</span></div>
<div class="gb-stat"><b>{yr1_420:.0f}%</b><span>fall in the $4.20 poverty rate in a single year, 2022-23 to 2023-24, which the World Bank calls &ldquo;unusually large&rdquo; and partly a better survey</span></div>
<div class="gb-stat"><b>23.0 vs 62</b><span>India&rsquo;s Gini index on consumption (World Bank, 2023) against income (World Inequality Database, 2023)</span></div>
</div>'''

body = f"""
{stats}

<p>On 9 October 2026 the World Bank published its latest Poverty and Equity Brief for India. Its headline: between 2011-12 and 2023-24 the share of Indians living below the poverty line used for lower-middle-income countries, $4.20 a person a day, fell from {a420[0]:.1f}% to {a420[2]:.1f}%, and about {LIFTED_420} million people moved above it. Extreme poverty, below $3.00 a day, fell from {a300[0]:.1f}% to {a300[2]:.1f}%. The same data put India&rsquo;s Gini index, the standard measure of inequality, at 23.0, which would make India one of the most equal countries in the world.</p>
<p>Both numbers come from the government&rsquo;s Household Consumption Expenditure Surveys (HCES). This piece sets out what they show, what the World Bank&rsquo;s own technical note says about the most recent year, and why the inequality figure tells us more about the survey than about the country.</p>

<h2 class="gb-h2">What the lines mean in rupees</h2>
<p>The World Bank sets its lines in &ldquo;international dollars&rdquo; at 2021 purchasing power parity (PPP), a conversion that allows for prices being lower in India than in the United States. Its technical note puts India&rsquo;s 2021 PPP conversion factor at Rs {PPP} per international dollar. On that basis the $3.00 extreme-poverty line is about Rs {line300_day:.0f} a person a day, or about Rs {line300_mo:,.0f} a month, and the $4.20 line about Rs {line420_day:.0f} a day, or Rs {line420_mo:,.0f} a month, both in 2021 prices. For comparison, the average monthly consumption the HCES found in 2023-24 was Rs 4,122 a person in rural India and Rs 6,996 in urban India, at 2023-24 prices and before counting free food and other handouts.</p>

<h2 class="gb-h2">Twelve years of decline, in two surveys</h2>
{t_poverty()}
<p class="gb-note">Share of population below each line, World Bank estimates from the 2011-12 Consumer Expenditure Survey and the 2023-24 HCES. The 2022-23 HCES gave {POV['$3.00']['All India'][1]}% (rural {POV['$3.00']['Rural'][1]}%, urban {POV['$3.00']['Urban'][1]}%) at $3.00 and {POV['$4.20']['All India'][1]}% (rural {POV['$4.20']['Rural'][1]}%, urban {POV['$4.20']['Urban'][1]}%) at $4.20. Source: World Bank technical note, &ldquo;India&rsquo;s long-term poverty trend, 2011-12 to 2023-24&rdquo; (April 2026), and Poverty and Inequality Platform update (September 2026).</p>
<p>The decline is large on any reading. The number of people below $4.20 a day fell from about {POOR_M['$4.20'][0]} million to {POOR_M['$4.20'][2]} million, and below $3.00 a day from {POOR_M['$3.00'][0]} million to {POOR_M['$3.00'][2]} million. Rural poverty fell most in percentage points; urban poverty fell slightly faster in proportion. The World Bank says consumption grew fastest at the bottom of the distribution: the poorest 60% saw growth above the national average of about 3% a year, and the richest 20% below it.</p>
<p>Other measures point the same way. NITI Aayog&rsquo;s multidimensional poverty index, which counts deprivations in health, schooling and living conditions rather than spending, fell from 29.17% in 2013-14 to 11.28% in 2022-23. The 2022-23 figure is a projection from the trend between the 2015-16 and 2019-21 health surveys, not a fresh measurement. The World Bank&rsquo;s own multidimensional measure was 15.5% in 2022-23.</p>

<h2 class="gb-h2">The last year is where the World Bank urges caution</h2>
<p>Between the two most recent surveys, 2022-23 and 2023-24, extreme poverty halved, from 5.3% to 2.6%, and the $4.20 rate fell from 23.9% to 16.1%, a {yr1_420:.0f}% drop in a single year. About {share_of_drop_in_last_year:.0f}% of the whole twelve-year fall at the $4.20 line came in that one year. The World Bank&rsquo;s technical note, published in April 2026, calls the change &ldquo;unprecedented relative to India&rsquo;s historical experience and to international benchmarks&rdquo; and roughly three times the long-term pace.</p>
<p>Its explanation is a mix of real gains and better measurement. In 2023-24 households reported consuming more items than in 2022-23, with a step-up of about 4.5 items on average at the very start of the new survey round in August 2023 rather than a gradual rise, a sign that the second year of a new questionnaire recorded spending more completely. The survey implies consumption growth of 10&ndash;15% among the poorest 10% in one year; the Periodic Labour Force Survey shows about 3&ndash;4% across the distribution, with employment up only modestly and real wages flat. Free grain under the Public Distribution System and the Pradhan Mantri Garib Kalyan Anna Yojana (PMGKAY) explains only about a third of that year&rsquo;s fall in extreme poverty, and food subsidies were falling in real terms over the period.</p>
<p>The World Bank does not dismiss the estimates: it says they strengthen confidence in the long-term trend and show no sampling or weighting problem. It says only that the one-year change &ldquo;should not be interpreted in isolation&rdquo;, and that it cannot yet separate real gains from better recording. The cleanest reading is the twelve-year one; the latest year&rsquo;s precise level is less certain than the headline suggests.</p>
<p>Independent economists have raised a longer-standing issue. The 2022-23 survey changed its questionnaire, item list, recall periods and interview method (tablets replaced paper). The World Bank adjusted the 2011-12 data to match, including valuing free and subsidised rations in both years, but Gaurav Datt, writing in <i>The India Forum</i> in November 2025, notes that alternative estimates of 2022-23 poverty range from 9.9% to 26.4% depending on method, and that the adjustments are not applied to earlier years, which overstates the decline relative to the long back series.</p>

<h2 class="gb-h2">A Gini of 23 measures the survey&rsquo;s reach</h2>
{chart_gini()}
<p>The consumption Gini fell from {GINI_CONS[0]} in 2011-12 to {GINI_CONS[1]} in 2022-23 and {GINI_CONS[2]} in 2023-24. MoSPI&rsquo;s own figures from the same surveys show the same direction: rural 0.266 to 0.237 and urban 0.314 to 0.284 between 2022-23 and 2023-24. On the World Bank&rsquo;s figures, the richest 10% accounted for {TOP10_CONS}% of consumption in 2023-24.</p>
<p>Other yardsticks for the same country give very different answers. The Gini for labour earnings in the 2023-24 Periodic Labour Force Survey is 0.43, with the median earnings of the top 10% of earners about 17 times those of the bottom 10%. The World Inequality Database, which combines surveys with income-tax records, puts India&rsquo;s income Gini at 62 in 2023, up from 52 in 2004, the top 10% share of income at {TOP10_INC}% and the top 1% share at {TOP1_INC}%; the top 1% holds {TOP1_WEALTH}% of wealth.</p>
<p>Three things push a consumption survey&rsquo;s inequality figure down. Consumption is more equal than income everywhere, because richer households save more of what they earn. Rich households are harder to survey: they refuse more often and under-report what they spend. And counting the value of free food and other transfers, as the World Bank now does, raises recorded welfare at the bottom. The World Bank says as much: its technical note warns that survey-based measures likely understate true inequality, and the latest survey even shows average spending of the top 5% falling between 2022-23 and 2023-24.</p>
<p>Tax data move the other way. The number of people reporting gross total income of Rs 100 crore or more rose from 284 in assessment year 2023-24 to 415 in 2024-25, the year covering incomes earned in 2023-24, a rise of {rich_jump:.0f}% in the same year the survey shows top-end spending falling.</p>
{t_rich()}
<p class="gb-note">Source: Ministry of Finance reply to Lok Sabha unstarred question 1274, 27 July 2026. An assessment year covers income earned in the previous financial year.</p>
<p>None of this means the poverty decline is false. The two questions use the survey differently: poverty depends on how well it captures the bottom of the distribution, which the World Bank says has improved; inequality depends on how well it captures the top, which it has never done well. A Gini of 23 is a statement about the survey&rsquo;s reach.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li><b>Run and publish the income survey.</b> MoSPI lists a National Household Income Survey in its 2025-26 annual report. A published income distribution, even an imperfect one, would give India an inequality figure that is not a by-product of a spending survey.</li>
<li><b>Link survey and tax data at the top.</b> Anonymised, aggregated income-tax data by income band, published each year alongside the HCES, would let researchers correct the top of the survey distribution, as many countries now do.</li>
<li><b>Publish the overlap between surveys.</b> When a questionnaire changes, run the old and new versions on a common sample for a period, so that changes in method can be separated from changes in welfare.</li>
<li><b>Release unit-level data with imputations flagged.</b> Show which items are imputed (free food, school uniforms, laptops and so on) and at what value, so that estimates with and without them can be reproduced.</li>
<li><b>Set an official national poverty line again.</b> India has had none since the 2014 Rangarajan report was not adopted; an official line on the new survey would end the reliance on international lines and inferred comparisons.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The World Bank brief and technical note were read through their published PDFs as indexed by search and fetch tools; the underlying microdata were not analysed here. The brief&rsquo;s own table lists 75.24 million people below $3.00 and 342.32 million below $4.20 against 2023 rates of 2.6% and 16.1%, numbers that match 2022 in the technical note; the technical note&rsquo;s counts (37 million and 233 million for 2023) are used here. The share of India&rsquo;s poor in the belt from Uttar Pradesh to West Bengal (about 57%) appears only in press coverage of the brief and is not used. The 2025 brief gave the top-10% to bottom-10% earnings ratio as 13 times for 2023-24; the 2026 technical note gives 17 times; the source of the difference was not established. The rupee value of the lines uses the 2021 PPP factor and is in 2021 prices; it is not adjusted to 2023-24 prices. Whether MoSPI&rsquo;s income survey is in the field was not confirmed.</p>
"""

sources = ("World Bank, India Poverty and Equity Brief, October 2026 (published 9 October 2026); World Bank, &ldquo;India&rsquo;s long-term poverty trend, 2011-12 to 2023-24&rdquo;, technical note, April 2026, including Annex 2 (caveats on the 2022-23 to 2023-24 change) and Annex 3 (limits of survey-based inequality); "
           "World Bank, September 2026 update to the Poverty and Inequality Platform, Table 5; World Bank, India Poverty and Equity Brief, April 2025 (WID income Gini); World Development Indicators Table 1.3 (Gini and consumption shares). "
           "MoSPI, HCES 2022-23 factsheet and 2023-24 press note (27 December 2024); MoSPI Annual Report 2025-26 (National Household Income Survey). NITI Aayog, &ldquo;Multidimensional Poverty in India since 2005-06&rdquo; (January 2024). "
           "Ministry of Finance, Lok Sabha unstarred question 1274, 27 July 2026. Gaurav Datt, &ldquo;The Great Indian Poverty Debate&rdquo;, The India Forum, November 2025. World Inequality Lab shares as reported by IDR and the World Bank. "
           "Rupee equivalents and percentages are this blog&rsquo;s arithmetic (builder in the repository at out/research/poverty-brief/).")

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/rural-job-guarantee-pay-rose-96-in-july.html", "Rural Job-Guarantee Pay Rose 9.6% in July. In Eight States It Buys Less Than in 2025"),
    ("https://masaladeutsch.blogspot.com/2026/08/a-17-rural-pay-rise-that-nobody-received.html", "A 17% Rural Pay Rise That Nobody Received"),
    ("https://masaladeutsch.blogspot.com/2026/09/the-wage-beats-crop-in-survey-that.html", "The Wage Beats the Crop &mdash; In the Survey That Leaves the Wage-Earners Out"),
    ("https://masaladeutsch.blogspot.com/2026/09/one-nation-one-ration-card-doesnt-move.html", "One Nation One Ration Card Doesn&rsquo;t Move Grain. FCI&rsquo;s Ethanol Tenders Move a Lot of It"),
    ("https://masaladeutsch.blogspot.com/2026/08/real-gdp-growth-india-fy2012-13-to.html", "Real GDP Growth &mdash; India, FY2012-13 to FY2025-26"),
]

build("Economy · 7 November 2026",
      "The World Bank Says 496 Million Indians Left Poverty. Its Own Note Says the Last Year&rsquo;s Drop Is Partly a Better Survey",
      "Poverty below $4.20 a day fell from 57.7% to 16.1% between 2011-12 and 2023-24, and extreme poverty to 2.6%. About a fifth of the twelve-year fall at the $4.20 line came in a single year that the World Bank flags as partly better recording, and the Gini of 23 says more about whom the survey misses than about India.",
      body, sources, related, OUT)
print('ok', round(line300_day, 2), round(line420_day, 2), round(line300_mo), round(line420_mo), round(yr1_300), round(yr1_420), round(share_of_drop_in_last_year), round(rich_jump))
