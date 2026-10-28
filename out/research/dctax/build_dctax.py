import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-dctax.html'

# ---------------------------------------------------------------- illustrative arithmetic (all assumptions stated in text)
SAFE_HARBOUR = 0.15          # cost-plus margin for Indian related data-centre operator (Budget 2026-27)
CORP_TAX = 0.2517            # 22% + 10% surcharge + 4% cess, domestic company under the concessional regime
COST = 100.0
PRICE = COST * (1 + SAFE_HARBOUR)
PROFIT = COST * SAFE_HARBOUR
TAX = PROFIT * CORP_TAX
TAX_SHARE_OF_PRICE = TAX / PRICE * 100

# a 100 MW IT campus, using the cooling post's load and efficiency assumptions
IT_MW, LOAD, PUE, TARIFF = 100, 0.70, 1.4, 7.0       # MW, average load, power usage effectiveness, Rs/kWh
POWER_SHARE = 0.5                                     # assumed share of power in the operator's annual cost
KWH = IT_MW * 1e3 * 8760 * LOAD * PUE
POWER_CR = KWH * TARIFF / 1e7
COST_CR = POWER_CR / POWER_SHARE
TAX_CR = COST_CR * SAFE_HARBOUR * CORP_TAX
WATER_MLD = 3.68                                      # evaporative cooling, 100 MW at 70% (cooling post)
WATER_ML_YR = WATER_MLD * 365
TAX_PER_KL = TAX_CR * 1e7 / (WATER_ML_YR * 1e3)       # Rs of tax per kL of cooling water if evaporative
assert round(TAX_SHARE_OF_PRICE, 1) == 3.3


def chart_split():
    W, L, top, bh = 400, 10, 44, 30
    H = top + bh + 56
    sc = (W - 2 * L) / PRICE
    parts = [("Operator&rsquo;s costs", COST, "#868e96"), ("Profit after tax", PROFIT - TAX, "#1c5d99"), ("Indian tax", TAX, "#a5402c")]
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Of Rs {PRICE:.0f} a foreign cloud company pays a related Indian data-centre operator under the 15% safe harbour, Rs {COST:.0f} covers costs, Rs {PROFIT - TAX:.2f} is profit after tax and Rs {TAX:.2f} is Indian tax.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Where Rs {PRICE:.0f} paid to an Indian related operator goes</text>',
         f'<text x="{L}" y="26" font-size="9.5" fill="#6c757d">15% cost-plus safe harbour; 25.17% corporate tax</text>']
    x = L
    for i, (n, v, col) in enumerate(parts):
        w = v * sc
        s.append(f'<rect x="{x:.1f}" y="{top}" width="{w:.1f}" height="{bh}" fill="{col}"/>')
        if w > 40:
            s.append(f'<text x="{x + w / 2:.1f}" y="{top + 19}" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">{v:.1f}</text>')
        x += w
    y = top + bh + 16
    s.append(f'<rect x="{L}" y="{y - 9}" width="9" height="9" fill="#868e96"/><text x="{L + 13}" y="{y}" font-size="9.5" fill="#212529">Costs {COST:.0f}</text>')
    s.append(f'<rect x="{L + 95}" y="{y - 9}" width="9" height="9" fill="#1c5d99"/><text x="{L + 108}" y="{y}" font-size="9.5" fill="#212529">Profit after tax {PROFIT - TAX:.2f}</text>')
    s.append(f'<rect x="{L + 245}" y="{y - 9}" width="9" height="9" fill="#a5402c"/><text x="{L + 258}" y="{y}" font-size="9.5" fill="#212529">Indian tax {TAX:.2f}</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">The foreign company&rsquo;s income from reselling the capacity abroad is exempt. Blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_timeline():
    ev = [("1 Feb", "Budget: tax holiday to 2047"), ("5 Jun", "Ordinance"), ("4 Aug", "Bill in Lok Sabha"),
          ("10 Aug", "Passed by Parliament"), ("17 Aug", "Assent"), ("14 Sep", "UPI zero-MDR notice*")]
    W, L, top = 400, 10, 30
    H = top + len(ev) * 22 + 20
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Timeline of the data-centre tax change in 2026, from the 1 February Budget to assent on 17 August.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">2026: from Budget promise to law</text>',
         f'<line x1="{L + 60}" x2="{L + 60}" y1="{top - 4}" y2="{top + (len(ev) - 1) * 22 + 4}" stroke="#ced4da" stroke-width="2"/>']
    for i, (d, t) in enumerate(ev):
        y = top + i * 22
        s.append(f'<circle cx="{L + 60}" cy="{y}" r="4" fill="#1c5d99"/>')
        s.append(f'<text x="{L + 50}" y="{y + 4}" font-size="10" fill="#212529" text-anchor="end">{d}</text>')
        s.append(f'<text x="{L + 72}" y="{y + 4}" font-size="10" fill="#212529">{t}</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">*Under the Payment and Settlement Systems amendment passed alongside; single report.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_change():
    return table(["Condition for the exemption", "Finance Act 2026 (Budget)", "After the August 2026 Act"], [
        ("Foreign company", "Must be notified by the central government", "No notification; information to be filed in a prescribed form"),
        ("Data centre", "Set up under an approved scheme and notified (MeitY)", "No scheme approval or notification"),
        ("Who runs the data centre", "Owned and operated by an Indian company", "Owned <i>or leased</i> and operated by an Indian company"),
        ("Foreign company&rsquo;s role", "Must not own or operate the physical infrastructure", "Unchanged, as reported"),
        ("Sales to Indian customers", "Through an Indian reseller, taxed in India", "Unchanged"),
        ("Related Indian operator", "15% cost-plus safe harbour", "Unchanged"),
        ("Period", "Tax years to 31 March 2047", "Unchanged"),
    ])


def t_other():
    return table(["Provision", "What it does"], [
        ("Government securities", "Exempts interest and capital gains of foreign institutional investors and the Bank for International Settlements on government securities, from 1 April 2026; previously 20% on interest, 30% on short-term and 12.5% on long-term gains"),
        ("Electronics", "Extends the exemption for capital goods and tooling supplied to contract manufacturers from 2030-31 to 2040-41"),
        ("Diamonds and warehouses", "Exempts certain foreign companies&rsquo; income from rough-diamond sales in notified zones and from storing components in customs-bonded warehouses, from 1 October 2026 to 31 March 2041"),
        ("Fund management", "Drops conditions for foreign funds managed from India, including the 25-member minimum and the Rs 100 crore corpus"),
        ("REITs and InvITs", "Raises the surcharge on their special-purpose vehicles from 10% to 25%; exempts unit holders&rsquo; dividends from those vehicles"),
        ("UPI and RuPay (Payment and Settlement Systems Act)", "Lets the government decide by notification which digital payments stay free of merchant charges; the Finance Minister called it an enabling provision"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>2047</b><span>tax years to which foreign cloud companies serving customers abroad from Indian data centres pay no Indian income tax on that business</span></div>
<div class="gb-stat"><b>2 &rarr; 0</b><span>notifications needed: one for the foreign company and one for the data centre, both dropped by the August Act</span></div>
<div class="gb-stat"><b>Rs {TAX:.2f}</b><span>of Indian tax on every Rs {PRICE:.0f} a foreign cloud company pays a related Indian operator, under the 15% safe harbour</span></div>
<div class="gb-stat"><b>None</b><span>official estimate of the tax forgone that this blog could find</span></div>
</div>'''

body = f"""
{stats}

<p>In the February Budget the Finance Minister offered foreign cloud companies a tax holiday to 2047: if they serve customers outside India from data centres in India, that income is exempt. The Finance Act made it law with conditions attached, including government notification of each foreign company and each data centre. On 17 August the President signed the Taxation and Other Laws (Amendment) Act 2026, which removes those notifications and lets the data centre be leased rather than owned by its Indian operator. Nasscom called it a step towards tax certainty.</p>
<p>This piece sets out what changed, who stands to benefit, what India collects and gives up, and how that compares with the power and water the same campuses need. It is not tax advice.</p>

<h2 class="gb-h2">What changed between February and August</h2>
{chart_timeline()}
{t_change()}
<p>The changes turn an approval scheme into an entitlement. Before, a hyperscaler had to be named in a government notification and use a data centre approved under a MeitY scheme. Now any foreign company that meets the conditions and files the prescribed information qualifies, and so does capacity rented from a colocation company, which is how most cloud providers start in a new market. Nasscom&rsquo;s point was that tax certainty should not depend on which entity happened to be named in an approval.</p>
<p>The Act was introduced on 4 August, passed by both Houses by 10 August, and received assent on 17 August, replacing an ordinance issued in June. The changes reported in the enacted Act match those PRS described in the Bill as introduced; the eligibility rules and the information form were still to be notified, as reported.</p>

<h2 class="gb-h2">Who benefits</h2>
<p>The beneficiaries are the foreign cloud companies building or renting large capacity in India, named in this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/where-indias-gigawatt-data-centre-bets.html">piece on the gigawatt data-centre bets</a>: Google (with AdaniConneX and Airtel in Visakhapatnam), Microsoft (Hyderabad), Amazon Web Services (Mumbai and Hyderabad) and Meta (leasing from Reliance in Jamnagar). The leasing change matters most for those that rent rather than build, and for operators such as NTT, Sify, CtrlS, Yotta and STT, whose business is renting capacity. Sales to customers in India do not qualify; they must go through an Indian reseller and are taxed in India.</p>

<h2 class="gb-h2">What India collects, and what it gives up</h2>
{chart_split()}
<p>India still taxes the Indian company that runs the data centre. Under the 15% cost-plus safe harbour, an Indian operator serving a related foreign cloud company can report a profit of 15% on its costs. On Rs {COST:.0f} of costs it charges Rs {PRICE:.0f}, earns Rs {PROFIT:.0f} and pays about Rs {TAX:.2f} in tax at the 25.17% corporate rate: about {TAX_SHARE_OF_PRICE:.1f}% of what the foreign company pays it. What is exempt is the foreign company&rsquo;s income from selling computing to customers abroad, which can be several times the cost of the capacity it runs on.</p>
<p>No official estimate of the revenue forgone was found, and none could be made honestly without knowing how much global cloud business will be booked through Indian capacity. To give a sense of scale, take a 100 MW campus running at 70% load with a power usage effectiveness of {PUE}: it uses about {KWH / 1e6:,.0f} GWh a year, which at an assumed Rs {TARIFF:.0f} a unit costs about Rs {POWER_CR:,.0f} crore. If power is half the operator&rsquo;s costs, its total costs are about Rs {COST_CR:,.0f} crore and the safe harbour yields about Rs {TAX_CR:,.0f} crore a year of Indian tax. That is an illustration built on stated assumptions, not an estimate of any real campus.</p>
<p class="gb-note">Assumptions: average IT load 70%, PUE 1.4, power Rs 7/kWh, power 50% of operating cost, 25.17% tax on the safe-harbour margin. Change any of them and the result moves proportionately.</p>

<h2 class="gb-h2">The trade: tax, power and water</h2>
<p>The same campus, if cooled by open evaporative towers, would use about {WATER_MLD} million litres of water a day, by the arithmetic in this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/10/closed-loop-or-open-loop-how-indias-new.html">piece on data-centre cooling</a>. On the illustration above, India would collect about Rs {TAX_PER_KL:,.0f} of tax for every kilolitre of cooling water such a campus used, while the foreign company&rsquo;s export income is untaxed. The point is not that the exemption is wrong: India is competing with Singapore, Malaysia and the Gulf for these campuses, and the investment, jobs and fibre they bring count too. It is that the tax holiday is the one part of the bargain the government has now made unconditional, while the power and water the campuses draw are still negotiated site by site with states. The <a href="https://masaladeutsch.blogspot.com/2026/10/india-got-record-945-billion-of-fdi.html">record FDI of 2025-26</a> came with large outflows; how much of the data-centre money stays in India will depend on contracts this Act does not touch.</p>

<h2 class="gb-h2">What else the Act does</h2>
{t_other()}
<p>The government-securities exemption, which the June ordinance introduced, is the costliest-looking change for the exchequer: foreign investors&rsquo; interest income from government bonds was previously taxed at 20%. The Payment and Settlement Systems amendment matters for anyone who pays by UPI; this blog looked at <a href="https://masaladeutsch.blogspot.com/2026/08/upi-fees-are-now-legal-petrol-pumps.html">what UPI fees could mean for petrol pumps and rural payments</a> earlier this year.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Finance Ministry&rsquo;s annual statement of revenue forgone should list the data-centre exemption separately, with the number of foreign companies claiming it and the income exempted.</li>
<li>The prescribed information form should require each claimant to report the data centres it uses, their IT load, and their power and water use, so the exemption can be compared with what the campuses draw.</li>
<li>States allocating power and water to data-centre campuses should publish the allocation and the tariff, since the central tax regime no longer gives the government a project-by-project approval point.</li>
<li>The safe-harbour margin should be reviewed after three years against the margins actually reported by Indian operators.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The enacted text and the gazette notification could not be opened; the provisions come from PRS&rsquo;s summary of the Bill as introduced, law-firm and Nasscom commentary, and news reports of the assent. Whether any provision changed between introduction and passage could not be confirmed, though no report said so. The eligibility rules and the information form had not been seen. The assent date is reported by several outlets citing the Ministry of Law; the 14 September UPI notification rests on a single report. The tax illustration depends entirely on its stated assumptions, and no official revenue-forgone estimate was found.</p>
"""

sources = ("Act and Bill: PRS Legislative Research, The Taxation and Other Laws (Amendment) Bill 2026, bill summary (5 August 2026) and bill track, and Monthly Policy Review (August 2026); assent on 17 August 2026 per Outlook Business, Deccan Chronicle and Eastern Mirror citing the Ministry of Law notification; Nasscom (IANS, Inc42, 4 August 2026); Legal500, Lexology, TaxGuru, KSMG and A2Z Taxcorp commentary. "
           "Budget 2026-27 provisions (tax holiday to 2047, Indian reseller, 15% safe harbour, infrastructure condition): PIB releases on data centres; KPMG, EY, S&amp;R Associates; TechCrunch (1 February 2026). "
           "UPI: Moneylife, Outlook Money, Inc42. Campus names and capacities: this blog&rsquo;s gigawatt data-centre post; cooling water: this blog&rsquo;s cooling post. "
           "The safe-harbour split and the 100 MW illustration are this blog&rsquo;s arithmetic on stated assumptions (builder in the repository at out/research/dctax/). Nothing here is tax or investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/where-indias-gigawatt-data-centre-bets.html", "Where India&rsquo;s Gigawatt Data-Centre Bets Actually Land"),
    ("https://masaladeutsch.blogspot.com/2026/10/closed-loop-or-open-loop-how-indias-new.html", "Closed Loop or Open Loop? How India&rsquo;s New Data Centres Should Be Cooled, Site by Site"),
    ("https://masaladeutsch.blogspot.com/2026/10/india-got-record-945-billion-of-fdi.html", "India Got a Record $94.5 Billion of FDI Last Year. Net of Exits and Investment Abroad, $7.7 Billion Stayed"),
    ("https://masaladeutsch.blogspot.com/2026/08/upi-fees-are-now-legal-petrol-pumps.html", "Transaction Fees for UPI: Will Petrol Pumps Have More ATMs? A Case for Rural Financial Inclusion"),
]

build("Data Centres · 28 October 2026",
      "India Dropped the Last Approvals on Its Data-Centre Tax Holiday. It Never Said What the Holiday Costs",
      "An August amendment lets foreign cloud companies claim India&rsquo;s tax holiday to 2047 without being notified, and on capacity their Indian partners lease rather than own. India still taxes the Indian operator&rsquo;s 15% margin, but no estimate of what the exemption costs has been published.",
      body, sources, related, OUT)
print("tax per 115", round(TAX, 2), "share", round(TAX_SHARE_OF_PRICE, 2), "GWh", round(KWH / 1e6), "power cr", round(POWER_CR), "cost cr", round(COST_CR), "tax cr", round(TAX_CR), "Rs/kL", round(TAX_PER_KL))
