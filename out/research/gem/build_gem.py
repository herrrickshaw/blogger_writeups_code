import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-gem-procurement.html'

# ---------------------------------------------------------------- data, Rs crore
# Lok Sabha unstarred Q4819, 29 Mar 2023 (FY18-FY22); later years as reported by the Commerce Ministry
GMV = [("2017-18", 5876.53, True), ("2018-19", 17461.61, True), ("2019-20", 22916.22, True),
       ("2020-21", 38570.57, True), ("2021-22", 106510.27, True),
       ("2022-23", 200000, False),       # "Rs 2 lakh crore" at year end (reported)
       ("2023-24", 400000, False),       # "Rs 4 lakh crore" (reported)
       ("2024-25", 543000, True),        # Rs 5.43 lakh crore, Commerce Minister's letter (Outlook: 5.42)
       ("2025-26", None, False)]         # derived below
MSE_GMV_FY26 = 236000                    # Rs 2.36 lakh crore of orders to MSEs
MSE_GMV_SHARE_FY26 = 47.1                # % of GMV
MSE_ORDER_SHARE_FY26 = 68                # % of orders
GMV_FY26 = MSE_GMV_FY26 / (MSE_GMV_SHARE_FY26 / 100)
GMV[-1] = ("2025-26", GMV_FY26, False)
CHANGE_FY26 = (GMV_FY26 / GMV[-2][1] - 1) * 100
WOMEN_FY26_CR, WOMEN_FIRMS = 28000, 2.1   # Rs crore to women-led MSEs; lakh firms
WOMEN_SHARE_GEM = WOMEN_FY26_CR / GMV_FY26 * 100
CUM_APR26, CUM_AUG26, ORDERS_AUG26 = 18.4, 20.0, 3.78     # lakh crore; crore orders
COAL_FY25, COAL_HANDLING_FY25 = 163000, 42000
COAL_SHARE_FY25 = COAL_FY25 / GMV[-2][1] * 100
STATE_GROWTH_FY26 = 38.3
# MSME Sambandh, central ministries/departments/CPSEs, FY2024-25 to 28 Jan 2025 (Rajya Sabha, 3 Feb 2025)
SAMB_TOTAL, SAMB_MSE, SAMB_SCST, SAMB_WOMEN = 147332, 59976, 1884, 3208
samb = {k: v / SAMB_TOTAL * 100 for k, v in (("mse", SAMB_MSE), ("scst", SAMB_SCST), ("women", SAMB_WOMEN))}
# GDP at current prices, 2022-23 base (MoSPI NAS), Rs crore
GDP = {"2022-23": 26177001, "2023-24": 29073287, "2024-25": 31798524, "2025-26": 34536796}
gdp_share = {y: v / GDP[y] * 100 for y, v, _ in GMV if y in GDP}
PP_LO, PP_HI = 20, 22                    # public procurement, % of GDP (government factsheet)
gem_of_pp = (GMV_FY26 / (GDP["2025-26"] * PP_HI / 100) * 100, GMV_FY26 / (GDP["2025-26"] * PP_LO / 100) * 100)
assert round(GMV_FY26, -3) == 501000 and round(samb["mse"], 1) == 40.7


def chart_gmv():
    W, L, top, ch, bw = 400, 34, 40, 150, 30
    gap = (W - L - 10 - len(GMV) * bw) / (len(GMV) - 1)
    H = top + ch + 50
    mx = 6.0
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="GeM purchases by year in Rs lakh crore, rising from 0.06 in 2017-18 to 5.43 in 2024-25 and about 5.0 in 2025-26.">',
         f'<text x="10" y="12" font-size="12" fill="#495057">Purchases through GeM each year, Rs lakh crore</text>',
         f'<rect x="10" y="18" width="9" height="9" fill="#1c5d99"/><text x="23" y="26" font-size="9.5" fill="#212529">Official figure</text>',
         f'<rect x="110" y="18" width="9" height="9" fill="#8fb1d4"/><text x="123" y="26" font-size="9.5" fill="#212529">Rounded or derived</text>']
    base = top + ch
    for v in (0, 2, 4, 6):
        y = base - v / mx * ch
        s.append(f'<line x1="{L}" x2="{W - 10}" y1="{y:.1f}" y2="{y:.1f}" stroke="#e9ecef"/>')
        s.append(f'<text x="{L - 4}" y="{y + 3:.1f}" font-size="9" fill="#6c757d" text-anchor="end">{v}</text>')
    for i, (yr, v, exact) in enumerate(GMV):
        x = L + i * (bw + gap)
        h = v / 1e5 / mx * ch
        s.append(f'<rect x="{x:.1f}" y="{base - h:.1f}" width="{bw}" height="{max(h, 1):.1f}" fill="{"#1c5d99" if exact else "#8fb1d4"}"/>')
        s.append(f'<text x="{x + bw / 2:.1f}" y="{base - h - 3:.1f}" font-size="9" fill="#212529" text-anchor="middle">{v / 1e5:.2f}</text>')
        s.append(f'<text x="{x + bw / 2:.1f}" y="{base + 12}" font-size="8.5" fill="#495057" text-anchor="middle">{yr[2:4]}-{yr[5:]}</text>')
    s.append(f'<text x="10" y="{H - 16}" font-size="9" fill="#6c757d">2017-18 to 2021-22: Lok Sabha reply (2023); 2024-25: Commerce Minister. 2025-26 derived from</text>')
    s.append(f'<text x="10" y="{H - 4}" font-size="9" fill="#6c757d">Rs 2.36 lakh crore to MSEs being 47.1% of the total. This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_targets():
    return table(["Group", "Target (central ministries and CPSEs)", "On GeM, 2025-26", "All central procurement, 2024-25 to 28 Jan 2025"], [
        ("Micro and small enterprises", "25% of annual procurement", f"{MSE_ORDER_SHARE_FY26}% of orders; {MSE_GMV_SHARE_FY26}% of value (Rs {MSE_GMV_FY26 / 1e5:.2f} lakh crore)", f"{samb['mse']:.1f}% (Rs {SAMB_MSE:,} crore of Rs {SAMB_TOTAL:,} crore)"),
        ("of which, owned by women", "3%", f"About {WOMEN_SHARE_GEM:.1f}% of value (over Rs {WOMEN_FY26_CR:,} crore to {WOMEN_FIRMS} lakh women-led MSEs)", f"{samb['women']:.1f}% (Rs {SAMB_WOMEN:,} crore)"),
        ("of which, owned by Scheduled Castes or Tribes", "4%", "Not reported", f"{samb['scst']:.1f}% (Rs {SAMB_SCST:,} crore)"),
    ])


def t_buyers():
    return table(["Buyer", "What is known"], [
        ("Ministry of Coal and its companies", f"Largest buyer in 2024-25: Rs {COAL_FY25 / 1e5:.2f} lakh crore, about {COAL_SHARE_FY25:.0f}% of the year&rsquo;s total, including Rs {COAL_HANDLING_FY25:,} crore of handling and transport services"),
        ("Defence, Petroleum and Natural Gas, Power, Steel", "The next largest buying ministries in 2024-25; the Department of Military Affairs had bought Rs 1.35 lakh crore cumulatively by August 2026"),
        ("Central public sector enterprises", "Reported at 54%, 63% and 83% of GeM&rsquo;s value in different statements and years; the most recent split was not found"),
        ("States", f"Purchases grew {STATE_GROWTH_FY26}% in 2025-26, the fastest-growing group, from a base reported at about a fifth of the total"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>~Rs {GMV_FY26 / 1e5:.1f} lakh cr</b><span>bought through GeM in 2025-26, about {abs(CHANGE_FY26):.0f}% less than the Rs {GMV[-2][1] / 1e5:.2f} lakh crore of 2024-25</span></div>
<div class="gb-stat"><b>{MSE_ORDER_SHARE_FY26}% vs {MSE_GMV_SHARE_FY26}%</b><span>of orders and of value that went to micro and small enterprises in 2025-26</span></div>
<div class="gb-stat"><b>{samb['women']:.1f}%</b><span>of central procurement went to women-owned small firms in 2024-25 (to January), against a 3% target</span></div>
<div class="gb-stat"><b>~{gem_of_pp[0]:.0f}&ndash;{gem_of_pp[1]:.0f}%</b><span>of all public procurement passes through GeM, if procurement is 20&ndash;22% of GDP</span></div>
</div>'''

body = f"""
{stats}

<p>The Government e-Marketplace (GeM), the online portal through which ministries, public companies and, increasingly, states buy goods and services, turned ten in August. By then it had handled more than Rs {CUM_AUG26:.0f} lakh crore of purchases across {ORDERS_AUG26} crore orders, according to the Commerce Ministry. Figures still quoted in exam-preparation summaries this month, Rs 16.41 lakh crore across 3.27 crore orders, are from an earlier date; the total had already passed Rs {CUM_APR26} lakh crore in April.</p>
<p>The headline totals hide two things. Annual purchases seem to have fallen in 2025-26, after rising every year since the portal began. And the government&rsquo;s procurement targets for small firms, for women-owned firms and for firms owned by Scheduled Castes and Tribes give different answers depending on whether they are measured on GeM or across all central purchases. This follows this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/10/the-sme-growth-fund-is-indias-fourth.html">piece on the government&rsquo;s equity programmes for small firms</a>, which asked the same question of a different tool: what each one actually counts.</p>

<h2 class="gb-h2">Growth stalled in 2025-26</h2>
{chart_gmv()}
<p>GeM&rsquo;s purchases rose from under Rs 6,000 crore in 2017-18, its first full financial year, to Rs {GMV[-2][1] / 1e5:.2f} lakh crore in 2024-25, as the government made it the default channel for central purchases. For 2025-26 the ministry said only that purchases were &ldquo;about&rdquo; or &ldquo;over&rdquo; Rs 5 lakh crore. Its own breakdown pins the figure down: small firms received Rs {MSE_GMV_FY26 / 1e5:.2f} lakh crore, which it said was {MSE_GMV_SHARE_FY26}% of the total. That makes the total about Rs {GMV_FY26 / 1e5:.2f} lakh crore, roughly {abs(CHANGE_FY26):.0f}% less than the year before.</p>
<p>As a share of the economy, GeM&rsquo;s purchases went from {gdp_share['2022-23']:.2f}% of GDP in 2022-23 to {gdp_share['2024-25']:.2f}% in 2024-25 and back to about {gdp_share['2025-26']:.2f}% in 2025-26, on MoSPI&rsquo;s new GDP series. The government&rsquo;s own factsheet puts public procurement at 20&ndash;22% of GDP, so GeM carries perhaps {gem_of_pp[0]:.0f}&ndash;{gem_of_pp[1]:.0f}% of it. Most public buying, including large works contracts and most of what states buy, still goes through other tender portals.</p>

<h2 class="gb-h2">Who buys on GeM</h2>
{t_buyers()}
<p>GeM&rsquo;s volume is concentrated. The coal ministry and its companies alone bought about {COAL_SHARE_FY25:.0f}% of everything purchased through the portal in 2024-25, much of it services such as moving coal. A dip in one large buyer&rsquo;s purchases is enough to move the national total, which may explain 2025-26 better than any change in the portal itself; the ministry has not published the buyer-wise figures that would show it. States are where growth now is.</p>

<h2 class="gb-h2">Small firms: most of the orders, less than half the money</h2>
{t_targets()}
<p>Since 2012 the public procurement policy for micro and small enterprises has required central ministries, departments and public companies to buy at least 25% of what they purchase each year from such firms, including 4% from firms owned by Scheduled Castes and Tribes and 3% from firms owned by women. On GeM, small firms won {MSE_ORDER_SHARE_FY26}% of orders in 2025-26 but {MSE_GMV_SHARE_FY26}% of the value, which means their orders were on average less than half the size of others&rsquo;. Both numbers clear the 25% target with room to spare.</p>
<p>The sub-targets are another matter. On GeM, women-led small firms received over Rs {WOMEN_FY26_CR:,} crore in 2025-26, about {WOMEN_SHARE_GEM:.1f}% of the year&rsquo;s value, and the ministry reports that as exceeding the 3% target. But the target applies to all central procurement, which the MSME ministry monitors through its Sambandh portal, and there the latest figure found, for 2024-25 up to 28 January 2025, was {samb['women']:.1f}% for women-owned firms and {samb['scst']:.1f}% for firms owned by Scheduled Castes and Tribes, both short of their targets. &ldquo;Women-led&rdquo; on GeM and &ldquo;women-owned&rdquo; under the policy may not be the same test, and the periods differ, so the two numbers do not contradict each other; they show that the success on the portal has not yet carried over to central purchasing as a whole.</p>
<p>There is also a gap in coverage. Sambandh recorded Rs {SAMB_TOTAL / 1e5:.2f} lakh crore of central procurement in the ten months to January 2025, less than a third of what was bought through GeM in the full year, most of it by central buyers. The two count different things, but the gap suggests the targets are checked against only part of what the central government buys.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>GeM should publish annual purchases by buying ministry, public company and state, with the share going to small, women-owned and SC/ST-owned firms for each, so a fall like 2025-26&rsquo;s can be explained.</li>
<li>The MSME ministry should reconcile Sambandh with GeM and require every central buyer to report all procurement there, so the 25%, 4% and 3% targets are measured on the full base.</li>
<li>GeM should report women&rsquo;s participation using the policy&rsquo;s definition of a women-owned firm, alongside its own &ldquo;women-led&rdquo; count.</li>
<li>Both portals should report the time taken to pay small sellers, since late payment matters as much to them as winning orders.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The exact 2025-26 total was not published; the figure here is derived from the ministry&rsquo;s small-firm numbers and could be off if those were rounded. The 2022-23 and 2023-24 figures are rounded as reported. No buyer-wise breakdown for 2025-26 was found, and statements on the public-sector share of GeM&rsquo;s value differ by year and source. The Sambandh figures are for part of 2024-25; no full-year figure was found. GeM and government releases were read through news reports and search-engine text, since the official sites could not be opened.</p>
"""

sources = ("GeM annual and cumulative purchases: Lok Sabha unstarred question 4819 (29 March 2023) for 2017-18 to 2021-22; Commerce Minister&rsquo;s letter as reported by The Tribune, Asianet Newsable and ETV Bharat (2024-25, Rs 5.43 lakh crore; Outlook Business gives Rs 5.42 lakh crore); Commerce Ministry statements as reported by IANS, DD News and IBEF (6 April 2026: Rs 18.4 lakh crore cumulative, MSE shares, women-led firms, state growth) and GKToday and Drishti IAS (August 2026: over Rs 20 lakh crore, 3.78 crore orders). "
           "Buyers: The Tribune and Swarajya (January 2025) on the coal ministry and top ministries; PSU Watch, Daily Pioneer and TaxTMI on the public-sector share. MSE policy and Sambandh: Public Procurement Policy for MSEs Order, 2012; Rajya Sabha reply of 3 February 2025 (Sambandh data to 28 January 2025). "
           "Public procurement 20&ndash;22% of GDP: PIB factsheet on GeM. GDP: MoSPI National Accounts, 2022-23 base, current prices, via the MoSPI data service. The 2025-26 total, shares of GDP and of public procurement, and the women-led share of value are this blog&rsquo;s arithmetic. Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/the-sme-growth-fund-is-indias-fourth.html", "The SME Growth Fund Is India&rsquo;s Fourth Rs 10,000 Crore Government Equity Programme. Their Scorecards Count Different Things"),
]

build("Public Procurement · 27 October 2026",
      "GeM&rsquo;s Purchases Stopped Growing in 2025-26. Small Firms Won Two-Thirds of the Orders but Less Than Half the Money",
      "The government&rsquo;s online marketplace has handled over Rs 20 lakh crore in ten years, but its 2025-26 purchases appear to have fallen for the first time. Small firms clear their 25% target easily; women- and SC/ST-owned firms still fall short across central purchases as a whole.",
      body, sources, related, OUT)
print("FY26", round(GMV_FY26), "chg", round(CHANGE_FY26, 1), "women share", round(WOMEN_SHARE_GEM, 2), "coal share", round(COAL_SHARE_FY25, 1), "gdp", {k: round(v, 2) for k, v in gdp_share.items()}, "pp", [round(x, 1) for x in gem_of_pp], samb)
