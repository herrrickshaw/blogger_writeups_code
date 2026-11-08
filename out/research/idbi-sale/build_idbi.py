import sys
from datetime import date
sys.path.insert(0, '/home/user/blogger_writeups_code/tools/postbuild')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-idbi-sale.html'

# ---- The deal (PIB 14 Oct 2026; BSE filing) ----
PRICE = 81.0
CONSIDERATION = 52878.0806181          # Rs crore, for 60.72%
GOI_SOLD, LIC_SOLD = 30.48, 30.24      # % of equity
GOI_PRE, LIC_PRE = 45.48, 49.24        # % before the sale
GOI_KEEP, LIC_KEEP = round(GOI_PRE - GOI_SOLD, 2), round(LIC_PRE - LIC_SOLD, 2)
SHARES = 1075.24                       # crore shares (equity capital Rs 10,752.40 cr, FV Rs 10)
BENCH, RESERVE, BID1 = 75.99, 94.42, 75.0
P_PRE_EOI, P_JAN26, P_MAY26 = 42.40, 108.12, 70.38
CLOSE_14OCT = 89.85                    # Business Standard
BV_MAR26, BV_SEP26 = 55.41, 59.22

assert abs(GOI_SOLD + LIC_SOLD - 60.72) < 1e-9
assert (GOI_KEEP, LIC_KEEP) == (15.0, 19.0)
sold_shares = SHARES * 60.72 / 100
assert abs(sold_shares * PRICE - CONSIDERATION) / CONSIDERATION < 0.001, sold_shares * PRICE

GOI_PROCEEDS = CONSIDERATION * GOI_SOLD / 60.72
LIC_PROCEEDS = CONSIDERATION * LIC_SOLD / 60.72
GOI_KEEP_VAL = SHARES * GOI_KEEP / 100 * PRICE
LIC_KEEP_VAL = SHARES * LIC_KEEP / 100 * PRICE
MCAP_81 = SHARES * PRICE
PB_SEP, PB_MAR = PRICE / BV_SEP26, PRICE / BV_MAR26
DISC_CLOSE = (CLOSE_14OCT - PRICE) / CLOSE_14OCT * 100
OVER_BENCH = (PRICE / BENCH - 1) * 100
OVER_MAY = (PRICE / P_MAY26 - 1) * 100
assert abs(OVER_BENCH - 6.6) < 0.05

# ---- Dividends declared since PCA exit (ET / Moneycontrol dividend lists) ----
DIVS = [(date(2023, 7, 6), 1.00), (date(2024, 7, 16), 1.50), (date(2025, 7, 15), 2.10)]
DPS = sum(d for _, d in DIVS)

# ---- Government money in, Rs crore (CAG Report 28 of 2017 to 2016-17; DFS banking analytics; Lok Sabha AU171) ----
GOI_IN = [
    (date(2010, 10, 1), 3119, "2010-11", "budget"),
    (date(2011, 10, 1), 810, "2011-12", "budget"),
    (date(2012, 10, 1), 555, "2012-13", "budget"),
    (date(2013, 10, 1), 1800, "2013-14", "budget"),
    (date(2015, 10, 1), 2229, "2015-16", "budget (Indradhanush)"),
    (date(2017, 3, 21), 1900, "2016-17", "budget (Indradhanush)"),
    (date(2017, 8, 9), 1861, "Aug 2017", "budget"),
    (date(2017, 12, 29), 2729, "Dec 2017", "budget"),
    (date(2018, 3, 28), 7881, "Mar 2018", "recapitalisation bonds"),
    (date(2019, 10, 23), 4557, "Oct 2019", "recapitalisation bonds"),
]
GOI_IN_TOTAL = sum(a for _, a, _, _ in GOI_IN)
assert GOI_IN_TOTAL == 27441, GOI_IN_TOTAL
assert 1861 + 2729 + 7881 == 12471          # DFS: FY18 total for IDBI
assert 3119 + 810 + 555 + 1800 + 2229 + 1900 == 10413   # CAG 2008-09 to 2016-17 total for IDBI
GOI_BONDS = 7881 + 4557
GOI_SINCE_1516 = sum(a for d, a, _, _ in GOI_IN if d >= date(2015, 4, 1))

# ---- LIC money in, shares bought from Oct 2018 (SEBI post-offer advertisement; CARE Mar 2019; Oct 2019 allotment) ----
LIC_LOTS = [  # date, crore shares, price, Rs crore, label
    (date(2018, 10, 4), 33.9897328, 61.73, "Oct 2018", "preferential"),
    (date(2018, 12, 28), 238.7617322, 60.73, "Dec 2018", "preferential"),
    (date(2019, 1, 18), 5.6682182, 61.73, "Jan 2019", "open offer (paid to public)"),
    (date(2019, 1, 21), 82.7590885, 60.73, "Jan 2019", "preferential"),
    (date(2019, 10, 23), 134.86, 35.17, "Oct 2019", "preferential"),
]
LIC_IN = [(d, n * p, lab, k) for d, n, p, lab, k in LIC_LOTS]
LIC_NEW_SHARES = sum(n for _, n, _, _, _ in LIC_LOTS)
LIC_IN_TOTAL = sum(a for _, a, _, _ in LIC_IN)
LIC_OLD_SHARES = 33.3722672                   # held before Oct 2018 (7.98%)
assert abs(LIC_NEW_SHARES + LIC_OLD_SHARES - SHARES * LIC_PRE / 100) < 0.3, LIC_NEW_SHARES + LIC_OLD_SHARES
# the four preferential lots equal LIC's Rs 21,624 cr (CARE) and Rs 4,743 cr (2019)
pref19 = sum(n * p for d, n, p, _, k in LIC_LOTS if k == "preferential" and d < date(2019, 4, 1))
assert abs(pref19 - 21624) < 2, pref19
assert abs(134.86 * 35.17 - 4743) < 1

# Of LIC's new shares, how many are sold vs kept (treat shares as interchangeable; old shares excluded)
LIC_NEW_VAL = LIC_NEW_SHARES * PRICE
LIC_NEW_DIV = LIC_NEW_SHARES * DPS
LIC_NEW_COST = LIC_IN_TOTAL / LIC_NEW_SHARES

GOI_SHARES = SHARES * GOI_PRE / 100
GOI_VAL = GOI_SHARES * PRICE
GOI_DIV = GOI_SHARES * DPS

# ---- Time value: grow every flow at R a year to an assumed completion date ----
R = 0.07
END = date(2027, 3, 31)


def fv(flows):
    return sum(a * (1 + R) ** ((END - d).days / 365.25) for d, a in flows)


GOI_IN_FV = fv([(d, a) for d, a, _, _ in GOI_IN])
LIC_IN_FV = fv([(d, a) for d, a, _, _ in LIC_IN])
GOI_OUT = GOI_VAL + GOI_DIV
LIC_OUT = LIC_NEW_VAL + LIC_NEW_DIV
GOI_OUT_FV = GOI_VAL + fv([(d, GOI_SHARES * x) for d, x in DIVS])
LIC_OUT_FV = LIC_NEW_VAL + fv([(d, LIC_NEW_SHARES * x) for d, x in DIVS])

# break-even rate for LIC's 2018-19 money
def irr_lic():
    lo, hi = 0.0, 0.2
    for _ in range(80):
        mid = (lo + hi) / 2
        v = sum(a * (1 + mid) ** ((END - d).days / 365.25) for d, a, _, _ in LIC_IN)
        o = LIC_NEW_VAL + sum(LIC_NEW_SHARES * x * (1 + mid) ** ((END - d).days / 365.25) for d, x in DIVS)
        lo, hi = (mid, hi) if o > v else (lo, mid)
    return mid


LIC_IRR = irr_lic() * 100
GOI_MULT = GOI_OUT / GOI_IN_TOTAL
LIC_MULT = LIC_OUT / LIC_IN_TOTAL

TOTAL_IN = GOI_IN_TOTAL + LIC_IN_TOTAL


def cr(x):
    s = f"{round(x):,}"
    # Indian grouping
    n = str(round(x))
    if len(n) > 5:
        head, tail = n[:-3], n[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        parts.insert(0, head)
        s = ",".join(parts) + "," + tail
    elif len(n) > 3:
        s = n[:-3] + "," + n[-3:]
    else:
        s = n
    return s


def lk(x):
    return f"{x / 1e5:.2f}"


# ---- Chart: in vs out, single hue ----
def chart():
    C = "#1c5d99"
    groups = [
        ("Government (since 2010-11)", [("Put in", GOI_IN_TOTAL, .35), ("Put in, grown at 7% a year", GOI_IN_FV, .6), ("Stake at &#8377;81 + dividends", GOI_OUT, 1)]),
        ("LIC (shares bought 2018-19)", [("Put in", LIC_IN_TOTAL, .35), ("Put in, grown at 7% a year", LIC_IN_FV, .6), ("Stake at &#8377;81 + dividends", LIC_OUT, 1)]),
    ]
    W, L, bh, gap = 340, 10, 18, 18
    mx = 57200
    sc = (W - L - 58) / mx
    y = 44
    s = [f'<svg viewBox="0 0 {W} 300" width="100%" role="img" aria-label="Money the government and LIC put into IDBI Bank against the value of their stakes at the sale price plus dividends, in rupees crore.">',
         f'<text x="{L}" y="15" font-size="14" fill="#495057">Money in vs value out, &#8377; crore</text>',
         f'<text x="{L}" y="31" font-size="11.5" fill="#6c757d">Value out = stake at &#8377;81 a share + dividends</text>']
    for g, bars in groups:
        s.append(f'<text x="{L}" y="{y + 10}" font-size="13" font-weight="bold" fill="#212529">{g}</text>')
        y += 20
        for lab, v, op in bars:
            s.append(f'<text x="{L}" y="{y + 9}" font-size="12" fill="#212529">{lab}</text>')
            y += 14
            s.append(f'<rect x="{L}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{C}" fill-opacity="{op}"/>')
            s.append(f'<text x="{L + v * sc + 4:.1f}" y="{y + 14}" font-size="12" fill="#212529">{cr(v)}</text>')
            y += bh + 6
        y += 10
    H = y + 16
    s[0] = s[0].replace(f'0 0 {W} 300', f'0 0 {W} {H}')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="11" fill="#6c757d">CAG, DFS, SEBI, CARE, PIB; this blog&rsquo;s arithmetic</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_in():
    rows = [(lab, "Govt", cr(a)) for d, a, lab, k in GOI_IN]
    lic = {}
    for d, a, lab, k in LIC_IN:
        lic[lab] = lic.get(lab, 0) + a
    rows += [(lab, "LIC", cr(a)) for lab, a in lic.items()]
    rows.append(("<b>Total</b>", "", f"<b>{cr(TOTAL_IN)}</b>"))
    return table(["When", "Who", "&#8377; cr"], rows)


def t_out():
    return table(["", "Govt", "LIC"], [
        ("Cash from Fairfax", cr(GOI_PROCEEDS), cr(LIC_PROCEEDS)),
        ("Stake kept", f"{GOI_KEEP:g}%", f"{LIC_KEEP:g}%"),
        ("Kept stake at &#8377;81", cr(GOI_KEEP_VAL), cr(LIC_KEEP_VAL)),
        ("Dividends FY23&ndash;25", cr(GOI_DIV), cr(SHARES * LIC_PRE / 100 * DPS)),
    ])


body = f"""<div class="gb-stats">
<div class="gb-stat"><b>&#8377;{CONSIDERATION:,.0f} cr</b><span>Fairfax&rsquo;s price for 60.72% of IDBI Bank, at &#8377;81 a share (Cabinet approval, 14 October 2026)</span></div>
<div class="gb-stat"><b>&#8377;{cr(TOTAL_IN)} cr</b><span>put into the bank as new capital since 2010-11: &#8377;{cr(GOI_IN_TOTAL)} cr by the government, &#8377;{cr(LIC_IN_TOTAL)} cr by LIC</span></div>
<div class="gb-stat"><b>31.8% &rarr; 2.1%</b><span>gross bad loans, September 2018 to September 2026</span></div>
<div class="gb-stat"><b>{PB_SEP:.2f}&times;</b><span>book value at &#8377;81, on September 2026 accounts</span></div>
</div>

<p>On 14 October 2026 the Cabinet Committee on Economic Affairs approved the sale of 60.72% of IDBI Bank to 10955230 Canada Inc., a company owned by Fairfax Financial Holdings of Toronto, for &#8377;52,878 crore. The government sells 30.48% and LIC sells 30.24%, both at &#8377;81 a share. The Finance Minister called it &ldquo;not a disinvestment, but a restructuring&rdquo;. The government described it as the largest foreign investment in India&rsquo;s financial sector.</p>
<p>The question this piece answers is narrower than whether &#8377;81 was a good price. It adds up what the two owners put into the bank while it was failing, and what they get back from this sale, the stakes they keep and the dividends already paid.</p>

<h2 class="gb-h2">How the price was set</h2>
<p>The sale began with an expression-of-interest notice on 7 October 2022, when the share traded at &#8377;42.40. Five parties expressed interest, four qualified and two bid. By January 2026, when first bids were invited, the share had run up to &#8377;108.12, and the reserve price was set at &#8377;94.42. The best bid, about &#8377;75, fell short and was rejected. The government then asked for best offers in May 2026, when the share was at &#8377;70.38.</p>
<p>For that round two independent valuers estimated the bank&rsquo;s worth from its March 2026 accounts, one by comparing it with listed public-sector banks and one by valuing its assets net of liabilities. Their average, &#8377;75.99 a share, was the benchmark. Fairfax&rsquo;s &#8377;81 is {OVER_BENCH:.1f}% above that and above each valuer&rsquo;s figure. It is {OVER_MAY:.0f}% above the May price, and about {DISC_CLOSE:.0f}% below the &#8377;89.85 close on the day of the decision. The share fell about 7% the next day.</p>
<p>At &#8377;81 the whole bank is valued at about &#8377;{cr(MCAP_81)} crore, or {PB_SEP:.2f} times its September 2026 book value of &#8377;{BV_SEP26} a share ({PB_MAR:.2f} times on the March 2026 book of &#8377;{BV_MAR26}). Profit for 2025-26 was &#8377;9,513 crore, so the price is about {PRICE / 8.85:.1f} times that year&rsquo;s earnings per share of &#8377;8.85.</p>

<h2 class="gb-h2">The money that went in</h2>
<p>IDBI Bank&rsquo;s gross bad loans peaked at 31.78% of loans in September 2018, and the Reserve Bank of India kept it under Prompt Corrective Action, which limits lending and spending, from May 2017 to March 2021. The government recapitalised it almost every year from 2010-11, more heavily than any other state bank in 2017-18. In 2018-19 LIC bought control, and both owners added more in October 2019.</p>
{t_in()}
<p>The total is &#8377;{cr(TOTAL_IN)} crore. LIC&rsquo;s lines are the shares it bought from October 2018, at the issue and open-offer prices in its SEBI filings. They include about &#8377;350 crore paid to public shareholders in the open offer, which did not reach the bank. LIC also held about 33 crore shares from before 2018; those are left out of both sides of the sums below. Of the government&rsquo;s &#8377;{cr(GOI_IN_TOTAL)} crore, &#8377;{cr(GOI_BONDS)} crore came as recapitalisation bonds rather than cash. These bonds cost nothing upfront, but the government pays interest on them every year until they mature.</p>

<h2 class="gb-h2">What comes back</h2>
{t_out()}
<p>The government receives about &#8377;{cr(GOI_PROCEEDS)} crore in cash and LIC about &#8377;{cr(LIC_PROCEEDS)} crore, in proportion to the shares each sells. The government keeps 15% and LIC 19%; both will withdraw their nominees from the board. The government plans to sell its remaining 15% on the stock market later. The dividends are &#8377;1.00, &#8377;1.50 and &#8377;2.10 a share declared for 2022-23 to 2024-25; this piece found no dividend declared for 2025-26. The table covers each owner&rsquo;s whole holding; the LIC comparison below uses only the shares it bought from 2018.</p>
{chart()}
<p><b>The government.</b> Its whole 45.48% stake at &#8377;81, plus dividends, comes to about &#8377;{cr(GOI_OUT)} crore against &#8377;{cr(GOI_IN_TOTAL)} crore put in since 2010-11, about {GOI_MULT:.1f} times. That flatters the government in one way and understates it in another. The government owned the bank long before 2010, and the value of that original stake is not counted as money in. Against that, grown at 7% a year to March 2027 (roughly what the government paid to borrow over the period), the money put in comes to about &#8377;{cr(GOI_IN_FV)} crore. The value coming back, with dividends grown the same way, is about &#8377;{cr(GOI_OUT_FV)} crore, about {(1 - GOI_OUT_FV / GOI_IN_FV) * 100:.0f}% less.</p>
<p><b>LIC.</b> The shares it bought in 2018-19 cost &#8377;{cr(LIC_IN_TOTAL)} crore, an average of &#8377;{LIC_NEW_COST:.2f} a share. At &#8377;81 they are worth about &#8377;{cr(LIC_NEW_VAL)} crore, and they have earned about &#8377;{cr(LIC_NEW_DIV)} crore in dividends, about {LIC_MULT:.1f} times the money put in. Grown at 7% a year, that money would have reached about &#8377;{cr(LIC_IN_FV)} crore by March 2027, about &#8377;{cr(LIC_IN_FV - LIC_OUT_FV)} crore more than what comes back. The return works out at about {LIC_IRR:.0f}% a year, and only if LIC can also sell the 19% it keeps at about &#8377;81. LIC invests policyholders&rsquo; money. On these figures its rescue made a profit, but a smaller one than a government bond would have paid.</p>
<p>Both results depend on the price of the stakes still held. A &#8377;10 move in the share price changes the value of the government&rsquo;s 15% by about &#8377;{cr(SHARES * 0.15 * 10)} crore and LIC&rsquo;s 19% by about &#8377;{cr(SHARES * 0.19 * 10)} crore.</p>

<h2 class="gb-h2">What still has to happen</h2>
<ul>
<li>The RBI must confirm Fairfax as fit and proper and approve its plan for meeting ownership rules. The government expects completion by March 2027.</li>
<li>Fairfax must make an open offer to the remaining public shareholders, who hold about 5.3%. The offer price will be set under SEBI&rsquo;s takeover rules, which can put it above &#8377;81 if the share has traded higher.</li>
<li>Fairfax already controls CSB Bank. It has two years to merge it with IDBI Bank or sell out, and the IDBI name is to be kept for three years after completion, Indian Express reports.</li>
<li>CRISIL put IDBI Bank&rsquo;s rating on watch with positive implications on 23 October 2026.</li>
</ul>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>When the government sells a company, the Department of Investment and Public Asset Management (DIPAM) should publish one table of every rupee put in since the company first needed support, split into cash and bonds, next to the sale proceeds.</li>
<li>The cost of recapitalisation bonds should be reported bank by bank, including the interest paid to date, so that a &ldquo;cash-neutral&rdquo; rescue shows its true cost.</li>
<li>LIC should report in its annual report the cost, dividends and sale value of its IDBI holding, as it would for any large single investment of policyholders&rsquo; money.</li>
<li>The two independent valuations should be published in summary once the deal closes, so that the &#8377;75.99 benchmark can be checked.</li>
<li>The government&rsquo;s remaining 15% should be sold on a published timetable, so that the overhang on the share price is known in advance.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>Government capital before 2010-11, and the value of the government&rsquo;s stake when IDBI became a bank in 2004, are not counted, so the government&rsquo;s &ldquo;money in&rdquo; is a floor, not the full cost. The interest actually paid on IDBI&rsquo;s share of recapitalisation bonds could not be found; the 7% rate stands in for it. Dates for the pre-2017 tranches are placed at mid-year. The FY 2025-26 dividend could not be confirmed either way. LIC&rsquo;s cost for the shares it held before 2018 was not found, so those shares are left out. The open-offer price, the two valuers&rsquo; separate figures and how the &#8377;52,878 crore will count against this year&rsquo;s disinvestment target were not public at the time of writing. Price-to-book figures for other banks were not compiled for comparison. Several 2026 figures (Q2 results, the CRISIL action, the post-deal share moves) were read through news reports and search-engine text rather than the filings themselves.</p>
"""

sources = (
    'Deal terms, bidding history and valuation: PIB, &ldquo;Government Approves Strategic Restructuring of IDBI Bank Ltd.&rdquo;, 14 October 2026, '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2323318&amp;reg=48&amp;lang=2">pib.gov.in (PRID 2323318)</a> (read via search-engine text) and the FAQ filed with BSE, '
    '<a href="https://www.bseindia.com/xml-data/corpfiling/AttachLive/d1434487-8320-42bf-8f92-67e9d2651856.pdf">bseindia.com</a>. '
    'Valuation methods and the &#8377;89.85 close: <a href="https://www.business-standard.com/companies/news/why-was-idbi-bank-sold-at-rs-81-a-share-understanding-the-valuation-126101500541_1.html">Business Standard, 15 October 2026</a>; '
    '<a href="https://bfsi.economictimes.indiatimes.com/articles/idbi-deal-why-fairfax-paid-above-the-governments-assessed-fair-value/134955562">ETBFSI, 15 October 2026</a>. '
    'Share fall: <a href="https://www.cnbc.com/2026/10/15/india-canada-fairfax-idbi-fdi.html">CNBC, 15 October 2026</a>. '
    'Government capital by year: CAG Report No. 28 of 2017, <a href="https://cag.gov.in/webroot/uploads/download_audit_report/2017/Report_No.28_of_2017_-_Performance_audit_Union_Government_Recapitalisation_of_Public_Sector_Banks_Reports_of_Ministry_of_Finance.pdf">Recapitalisation of Public Sector Banks</a>, Table 3.1; '
    'Department of Financial Services, <a href="https://financialservices.gov.in/banking-analytics">Banking Analytics</a> (read via search-engine text); '
    'Lok Sabha Unstarred Question 171, 15 December 2017, <a href="https://sansad.in/getFile/loksabhaquestions/annex/13/AU171.pdf?source=pqals">annex</a>; '
    'split of the 2017-18 amount: <a href="https://www.livemint.com/Industry/N7uE9GfrlwYEOUSOx86vyL/Govt-weighs-various-options-to-bring-down-its-stake-in-IDBI.html">Mint, 10 June 2018</a> and '
    '<a href="https://insights.dsij.in/article-details/articleid/22058/idbi-bank-gets-government%E2%80%99s-share-application-money-of-rs-1-861-crore">DSIJ, 10 August 2017</a>. '
    'LIC&rsquo;s purchases: SEBI, <a href="https://www.sebi.gov.in/sebi_data/commondocs/jan-2019/IDBI%20BANK%20LIMITED%20Post%20Offer%20Advertisement_p.pdf">IDBI Bank post-offer advertisement</a>, 24 January 2019; '
    '<a href="https://www.careratings.com/upload/CompanyFiles/PR/IDBI%20Bank%20Limited-03-15-2019.pdf">CARE Ratings, 15 March 2019</a>; '
    'the October 2019 allotment (&#8377;9,300 crore at &#8377;35.17 a share) from IDBI Bank&rsquo;s exchange filings as reported at the time. '
    'Dividends: <a href="https://economictimes.indiatimes.com/idbi-bank-ltd/infocompanydividends/companyid-11689.cms">Economic Times dividend list</a>; '
    '<a href="https://www.moneycontrol.com/company-facts/idbibank/dividends/IDB05">Moneycontrol</a>. '
    'Asset quality, capital, profits and book value: IDBI Bank results releases for September 2018, March 2026 and September 2026, as reported. '
    'Post-deal conditions (CSB Bank, name): Indian Express, October 2026, as reported; CRISIL rating action of 23 October 2026, as reported. '
    'Returns, values of retained stakes and 7% growth comparisons are this blog&rsquo;s arithmetic (builder at out/research/idbi-sale/ in the repository). Nothing here is investment advice.'
)

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/the-price-and-tap-two-levers-behind.html", "The Price and the Tap: The Two Levers Behind Every Central Bank, and Why RBI Pulls Them Differently"),
    ("https://masaladeutsch.blogspot.com/2026/09/what-failed-bankruptcy-auction-actually.html", "What a Failed Bankruptcy Auction Actually Costs, in India&rsquo;s Own Numbers"),
    ("https://masaladeutsch.blogspot.com/2026/09/where-indias-fdi-actually-lands-state.html", "Where India&rsquo;s FDI Actually Lands: 24 Quarters of DPIIT&rsquo;s Own State-and-District Data"),
    ("https://masaladeutsch.blogspot.com/2026/10/abu-dhabi-paid-2-billion-for-binance.html", "Abu Dhabi Paid $2 Billion for a Binance Stake in Stablecoins. India&rsquo;s FDI Rules Have No Box for That."),
]

assert GOI_OUT_FV < GOI_IN_FV and LIC_OUT_FV < LIC_IN_FV and GOI_OUT > GOI_IN_TOTAL and LIC_OUT > LIC_IN_TOTAL
assert 5.5 < LIC_IRR < 6.5 and round(TOTAL_IN / 1000) == 54
TITLE = "IDBI Bank&rsquo;s Rescuers Put In &#8377;54,000 Crore. At Fairfax&rsquo;s &#8377;81 a Share They Make a Profit, but Less Than Government Bonds Would Have Paid"
build("Banking · 8 November 2026",
      TITLE,
      f"Fairfax is paying &#8377;52,878 crore for 60.72% of the bank. Counting the stakes they keep at &#8377;81 and the dividends paid, the government gets back about {GOI_MULT:.1f} times the &#8377;{cr(GOI_IN_TOTAL)} crore it put in since 2010-11, and LIC earns about {LIC_IRR:.0f}% a year on its 2018-19 rescue. Both fall short of what the same money would have earned at 7%, roughly the government&rsquo;s own borrowing rate.",
      body, sources, related, OUT)
print("GOI proceeds", round(GOI_PROCEEDS), "LIC proceeds", round(LIC_PROCEEDS))
print("keep vals", round(GOI_KEEP_VAL), round(LIC_KEEP_VAL), "mcap", round(MCAP_81), "PB", round(PB_SEP, 2), round(PB_MAR, 2), "disc", round(DISC_CLOSE, 1), "overMay", round(OVER_MAY, 1))
print("GOI in", GOI_IN_TOTAL, "fv", round(GOI_IN_FV), "out", round(GOI_OUT), "outfv", round(GOI_OUT_FV), "mult", round(GOI_MULT, 2), "since1516", GOI_SINCE_1516)
print("LIC in", round(LIC_IN_TOTAL), "shares", round(LIC_NEW_SHARES, 2), "avg", round(LIC_NEW_COST, 2), "val", round(LIC_NEW_VAL), "div", round(LIC_NEW_DIV), "fv", round(LIC_IN_FV), "outfv", round(LIC_OUT_FV), "irr", round(LIC_IRR, 2), "mult", round(LIC_MULT, 2))
print("total in", round(TOTAL_IN), TITLE)
