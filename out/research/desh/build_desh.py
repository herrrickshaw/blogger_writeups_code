import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-desh-bill-sez-reform.html'

# ---------------------------------------------------------------- data
# Lok Sabha written reply, position on 31 July 2026
ZONES = [("Approved", 436, "#495057"), ("Notified", 372, "#1c5d99"), ("Operational", 277, "#2b8a3e"),
         ("Notified but not operational", 95, "#a5402c"), ("De-notified since approval", 110, "#868e96")]
assert 277 + 95 == 372
IDLE_SHARE = 95 / 372 * 100

# SEZ exports, Rs lakh crore. Full years: Lok Sabha reply. April-December: SEZ fact sheet (31.12.2025),
# 2024-25 derived from the fact sheet's own 31.48% growth figure.
APRDEC_26 = 11.65711
APRDEC_25 = APRDEC_26 / 1.3148
FY25, FY26 = 14.63, 16.4
Q4_25, Q4_26 = FY25 - APRDEC_25, FY26 - APRDEC_26
EXPORTS = [("Apr&ndash;Dec 2024", APRDEC_25, "#868e96"), ("Apr&ndash;Dec 2025", APRDEC_26, "#1c5d99"),
           ("2024-25, full year", FY25, "#868e96"), ("2025-26, full year", FY26, "#1c5d99")]
SHARE_FY25 = 172.27 / 824.9 * 100   # SEZ India export page (US$ bn) / India's total exports (RBI revision)
assert round(APRDEC_25, 2) == 8.87 and round(SHARE_FY25) == 21


def chart_zones():
    W, L, top, bh, gap, lab = 400, 10, 24, 18, 9, 178
    H = top + len(ZONES) * (bh + gap) + 20
    sc = (W - L - lab - 40) / 450
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Special Economic Zones on 31 July 2026: 436 approved, 372 notified, 277 operational, 95 notified but not operational, 110 de-notified.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">India&rsquo;s SEZs, position on 31 July 2026 (number of zones)</text>']
    for i, (n, v, col) in enumerate(ZONES):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 13}" font-size="10" fill="#212529">{v}</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Source: Ministry of Commerce and Industry, Lok Sabha written reply (as reported).</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_exports():
    W, L, top, bh, gap, lab = 400, 10, 24, 18, 9, 120
    H = top + len(EXPORTS) * (bh + gap) + 32
    sc = (W - L - lab - 46) / 18
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="SEZ exports in rupees lakh crore: April to December 2024 about {APRDEC_25:.2f}, April to December 2025 {APRDEC_26:.2f}, full year 2024-25 {FY25:.2f}, full year 2025-26 {FY26:.1f}.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Exports from SEZs, Rs lakh crore</text>']
    for i, (n, v, col) in enumerate(EXPORTS):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 13}" font-size="10" fill="#212529">{v:.2f}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Full years: Lok Sabha reply. April&ndash;December: SEZ fact sheet, 31 Dec 2025;</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">2024 figure derived from the fact sheet&rsquo;s stated growth of 31.48%.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_timeline():
    return table(["When", "What happened", "Source"], [
        ("Feb 2022", "Budget announces a new law to replace the SEZ Act, 2005", "Union Budget 2022-23"),
        ("Mid 2022", "Draft DESH Bill circulated; tabling planned for the monsoon session", "Draft bill; press reports"),
        ("Oct&ndash;Dec 2022", "Finance Ministry rejects the 15% corporate tax rate and other tax incentives; NITI Aayog questions dropping the net foreign exchange test", "Business Standard; BW Businessworld"),
        ("Nov 2023", "Government reported to be weighing dropping DESH and amending the SEZ Act instead", "Business Standard"),
        ("Apr 2024", "SEZ amendment bill tipped for the next government&rsquo;s first 100 days", "Business Standard"),
        ("Jun 2025", "Rules changed: 10-hectare minimum for chip and electronic-component SEZs", "G.S.R. 364(E)"),
        ("Jul 2025", "Commerce department to seek Cabinet approval for a bill to replace the SEZ Act in the monsoon session", "Business Standard"),
        ("Mar 2026", "17-member committee set up to draft &ldquo;SEZ 2.0&rdquo; within six months", "Department of Commerce order, as reported"),
        ("Apr 2026", "One-year window opens for SEZ factories to sell in India at lower customs duty", "Customs Notification 11/2026"),
        ("Oct 2026", "Rules changed: goods rejected by domestic buyers can return to the zone within 30 days", "G.S.R. 893(E)"),
    ])


def t_status():
    return table(["DESH proposal (2022 draft)", "Position on 27 October 2026"], [
        ("A new law replacing the SEZ Act, 2005", "<b>Not done.</b> No bill has been introduced; the SEZ 2.0 committee is reviewing the Act"),
        ("Drop the net foreign exchange (NFE) test, under which a unit must earn more foreign exchange than it spends over five years", "<b>Not done.</b> The test still applies; chip units may count free-of-cost goods toward it (June 2025)"),
        ("Sales into India with duty charged on imported inputs, not on the finished product", "<b>A different, temporary version.</b> Duty on the finished product at a lower rate, capped at 30% of exports, until 31 March 2027"),
        ("15% corporate tax for hub units until 2032", "<b>Rejected</b> by the Finance Ministry in 2022"),
        ("Smaller, easier zones", "<b>Done for one sector:</b> 10 hectares for semiconductor and electronic-component SEZs"),
        ("Wider range of services; rupee payment by domestic buyers; job work for domestic firms", "<b>Under discussion</b> in the SEZ 2.0 committee"),
        ("Dropping export-linked tax breaks to fit WTO rules", "<b>Largely done by expiry:</b> SEZ income-tax holidays closed to new developers after March 2017 and new units after 2020"),
    ])


def t_rates():
    return table(["Customs duty on the item today", "Rate for eligible SEZ units, Apr 2026 &ndash; Mar 2027"], [
        ("7.5%", "6.5%"), ("10%", "9%"), ("12.5% or 15%", "10%"), ("20%", "12.5%"), ("Between 20% and 30%", "15%"), ("Between 30% and 40%", "20%"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>4 years</b><span>since the 2022 Budget promised a new law to replace the SEZ Act; no bill has reached Parliament</span></div>
<div class="gb-stat"><b>95 of 372</b><span>notified SEZs were not operating on 31 July 2026 ({IDLE_SHARE:.0f}%)</span></div>
<div class="gb-stat"><b>Rs 16.4 lakh crore</b><span>SEZ exports in 2025-26, up from Rs 14.63 lakh crore (Lok Sabha reply)</span></div>
<div class="gb-stat"><b>30%</b><span>of a unit&rsquo;s best export year that it may now sell in India at lower duty, until March 2027</span></div>
</div>'''

body = f"""
{stats}

<p>In February 2022 the Union Budget promised to replace the Special Economic Zones Act, 2005 with a new law. The draft that followed, the Development of Enterprise and Service Hubs (DESH) Bill, would have turned SEZs into &ldquo;development hubs&rdquo; that could serve the Indian market as well as export, dropped the rule that every unit must be a net earner of foreign exchange, and offered a 15% corporate tax rate. It is still the version of SEZ reform that exam-prep explainers, such as Drishti IAS&rsquo;s, describe.</p>
<p>The Bill never reached Parliament. Four and a half years later, the SEZ Act of 2005 is still the law. What has changed instead is a series of rules and notifications, each taking one piece of the DESH idea in a narrower form, while a government committee drafts an &ldquo;SEZ 2.0&rdquo; whose report has not been published. This piece sets out what the Bill proposed, why it stalled, which parts have arrived anyway, and what the zones themselves look like now.</p>

<h2 class="gb-h2">What the Bill proposed</h2>
<p>SEZs were built for export. A unit inside a zone imports inputs duty-free and does not pay domestic indirect taxes, but anything it sells into the rest of India, the &ldquo;domestic tariff area&rdquo;, is treated as an import and pays full customs duty on the finished good. It must also show positive net foreign exchange over five years. For most of the zones&rsquo; history the main attraction was an income-tax holiday, which the government let lapse: new zones stopped qualifying after March 2017 and new units after 2020, as this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/09/a-textile-sez-built-to-re-employ-mill.html">piece on a shrinking Ahmedabad textile SEZ</a> describes.</p>
<p>The DESH draft, as reported, tried to answer both problems. Zones would become development hubs, split into enterprise hubs and service hubs, and the list of permitted services would widen beyond IT. The net foreign exchange test would go. Goods sold into India would pay duty only on the imported inputs they contained, not on the finished product, with an equalisation levy where needed to keep competition fair with factories outside the hubs. States would gain a bigger role in proposing hubs, approvals would run through a single online window with deadlines, and a 15% corporate tax rate would apply to hub units until 2032.</p>
<p>There was also a trade-law reason. In October 2019 a World Trade Organization panel, in a case brought by the United States, found that India&rsquo;s SEZ scheme, along with four other export programmes, gave prohibited export subsidies, because its tax and duty benefits were tied to exporting. India appealed in November 2019, but the WTO&rsquo;s Appellate Body has had no quorum since December 2019, so the appeal sits unheard and the ruling has no force. Removing the export conditions was meant to put the zones beyond that challenge.</p>

<h2 class="gb-h2">Why it stalled</h2>
{t_timeline()}
<p>The Finance Ministry objected to the money. In October 2022 it rejected the 15% tax rate, reportedly because firms outside the hubs would demand the same, and it also resisted letting hub units sell into India on payment of duty on inputs alone. NITI Aayog questioned dropping the net foreign exchange test. By November 2023 the government was reported to be considering abandoning DESH and amending the existing Act instead. An amendment bill was then tipped for the new government&rsquo;s first 100 days in 2024 and for the 2025 monsoon session; the PRS Legislative Research bill tracker lists no SEZ bill after the 2019 amendment, and no report found for this piece says one was introduced.</p>

<h2 class="gb-h2">What has arrived anyway</h2>
<p>Three changes since 2025 carry parts of the DESH idea, each in narrower form, and none needed Parliament.</p>
<p><b>Smaller zones for chips.</b> Amended rules notified on 3 June 2025 cut the minimum area for SEZs making semiconductors or electronic components to 10 hectares (from 50, according to most reports), let semiconductor units count goods received or supplied free of charge toward net foreign exchange, and allowed relaxations on land that is mortgaged or leased to government agencies.</p>
<p><b>A one-year window to sell in India.</b> The 2026-27 Budget announced, and Customs Notification 11/2026 of 31 March 2026 put into effect, a lower customs rate for goods that SEZ factories sell into India between 1 April 2026 and 31 March 2027. The reason given was spare capacity caused by global trade disruption.</p>
{t_rates()}
<p>The conditions are tight. A unit must have started production by 31 March 2025; its domestic sales under the scheme are capped at 30% of its highest yearly export value in the previous three years; the goods need at least 20% value addition; duty drawback is not allowed on them; and warehousing zones are excluded. The duty is still charged on the finished good, only at a lower rate, which is not the inputs-only model DESH proposed.</p>
<p><b>Returned goods.</b> The Third Amendment Rules, notified on 15 October 2026, let an SEZ unit take back goods that a domestic buyer refuses, for example after a change in fashion or a breach of contract, if they come back within 30 days, and claim a refund of the duty paid. A Business Standard column argued that 30 days is too short to settle a failed delivery. A Fourth Amendment around 21 October eased rules for fund and aircraft- and ship-leasing units in the International Financial Services Centre at GIFT City.</p>
<p>The bigger rewrite is with a committee. In March 2026 the Department of Commerce set up a 17-member inter-ministerial panel, drawn from Commerce, Customs, NITI Aayog and DPIIT and chaired, according to the order, by the Additional Secretary for SEZs, to produce a concept paper and roadmap for &ldquo;SEZ 2.0&rdquo; within six months. Its remit includes reviewing the SEZ Act and aligning SEZs with the other duty-free schemes: export-oriented units, manufacturing in bonded warehouses (MOOWR), Advance Authorisation, EPCG and DFIA. In July it was reported to be close to submitting; topics included letting domestic buyers pay for SEZ services in rupees and allowing job work for domestic firms without an export link. No report had been published by 27 October.</p>

<h2 class="gb-h2">Scorecard: DESH against what exists</h2>
{t_status()}

<h2 class="gb-h2">The zones today</h2>
{chart_zones()}
<p>On 31 July 2026, according to a Lok Sabha reply, 436 SEZs had been approved and 372 notified, of which 277 were operating and 95, about a quarter, were not. Haryana had the most idle zones (14), followed by Telangana (12), Karnataka (11), Tamil Nadu and Uttar Pradesh (9 each). Another 110 had been de-notified. The reasons the ministry gave were slow approvals from statutory and state bodies, a poor global business climate and &ldquo;changes in fiscal incentives&rdquo;, which is to say the end of the tax holidays.</p>
<p>The zones that work still matter. Employment in SEZs rose from 26.96 lakh in 2021-22 to 32.61 lakh in 2025-26, and SEZ exports of US$172 billion in 2024-25 were about {SHARE_FY25:.0f}% of India&rsquo;s total exports of goods and services that year.</p>
{chart_exports()}
<p>Some reports in 2026 said SEZ exports &ldquo;fell&rdquo; to US$133.45 billion in 2025-26 from about US$172 billion. That compares nine months with twelve: US$133.45 billion (Rs 11.66 lakh crore) is the April&ndash;December 2025 figure in the government&rsquo;s own SEZ fact sheet, which says it was 31.5% higher than in the same months of 2024. For the full year, the Lok Sabha reply gives Rs 16.4 lakh crore in 2025-26 against Rs 14.63 lakh crore in 2024-25, a rise of about {(FY26 / FY25 - 1) * 100:.0f}%.</p>
<p>The official figures do not quite fit together, though. Taken at face value, the two releases imply January&ndash;March 2026 exports of about Rs {Q4_26:.2f} lakh crore, {abs(Q4_26 / Q4_25 - 1) * 100:.0f}% below the Rs {Q4_25:.2f} lakh crore of January&ndash;March 2025, after nine months of 31% growth. Either the last quarter fell sharply or the two releases measure different things, for example goods only against goods and services. The government&rsquo;s figures for 2024-25 also differ by source: US$172.27 billion on the SEZ export page, US$173.07 billion in the fact sheet.</p>

<h2 class="gb-h2">What it adds up to</h2>
<p>DESH tried to settle three questions at once: whether SEZs exist to export or to make things in India, who pays for the incentives, and whether the scheme can survive WTO rules. The government has answered the third by letting the tax holidays expire. It has refused the second, at least for corporate tax. On the first it is moving one notification at a time: a temporary, capped window for domestic sales, smaller zones for one strategic sector and more practical rules on returns. That is cheaper and reversible, but it leaves a quarter of notified zones idle and the export-only design of the 2005 Act in place. The SEZ 2.0 report is the next chance to decide what the zones are for, and its first test will be whether it is published.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Department of Commerce should publish the SEZ 2.0 committee&rsquo;s report and state whether the government intends a new Act, amendments to the 2005 Act or rule changes only.</li>
<li>Before deciding whether to extend the domestic-sales window beyond March 2027, the CBIC and the Department of Commerce should publish how many units used it, the value of goods cleared and the duty forgone.</li>
<li>The SEZ statistics on sezindia.gov.in, the fact sheets and replies to Parliament should use one export series, labelled goods, services or both, so that full-year and part-year figures can be compared.</li>
<li>For each of the 95 notified but idle zones, the Department of Commerce should publish the date of notification, the developer and the stated reason for delay, as it does in aggregate in replies to Parliament.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The government pages behind these figures, including the SEZ India portal, PIB and Drishti IAS&rsquo;s explainer, could not be opened directly for this piece; figures come from the text of those pages as indexed by search engines and from news reports, as listed below. The DESH draft is described as reported in 2022, not from the draft text. Whether the SEZ 2.0 committee has submitted its report, and what it recommends, is not known.</p>
"""

sources = ("DESH Bill: explainers by Drishti IAS, The Federal, IASGyan and Civilsdaily; Business Standard podcast (27 Jul 2022), &ldquo;Finance ministry rejects the 15% benign corporate tax in the DESH Bill&rdquo; (5 Oct 2022), &ldquo;DESH Bill explained: What it is and why the government may junk it&rdquo; (6 Nov 2023), &ldquo;Proposed SEZ amendment bill may figure in next govt&rsquo;s 100-day agenda&rdquo; (12 Apr 2024) and &ldquo;SEZ amendment Bill may be taken up in monsoon session&rdquo; (13 Jul 2025); BW Businessworld (5 Dec 2022); Policy Circle; PRS Legislative Research bill tracker. "
           "Rules and notifications: Special Economic Zones (Amendment) Rules, 2025, G.S.R. 364(E), 3 Jun 2025 (PIB; Business Standard; Taxguru); Union Budget 2026-27 PIB explainer on SEZs; Customs Notification 11/2026-Customs, 31 Mar 2026, and CBIC/PIB releases (PRID 2247628, 2247993); Special Economic Zones (Third Amendment) Rules, 2026, G.S.R. 893(E), 15 Oct 2026 (Business Standard, 22 and 25 Oct 2026; A2Z Taxcorp); Fourth Amendment Rules (report). "
           "SEZ 2.0 committee: Department of Commerce order, March 2026, as reported by A2Z Taxcorp, KNN India and Angel One; Business Standard (19 Jul 2026). "
           "Numbers: Ministry of Commerce and Industry Lok Sabha written reply on SEZs as on 31 Jul 2026, as reported by PSUWatch, Kashmir Life and Torbit Realty; SEZ fact sheet as on 31 Dec 2025 (sezindia.gov.in); SEZ India export-performance page (2024-25); RBI revision of India&rsquo;s 2024-25 exports (US$824.9 bn). "
           "WTO: DS541, India &mdash; Export Related Measures, panel report (31 Oct 2019) and India&rsquo;s notice of appeal (19 Nov 2019), WTO. "
           "Shares, the April&ndash;December 2024 figure and the January&ndash;March comparison are this blog&rsquo;s arithmetic from those figures. Research notes: out/research/desh/ in the blog&rsquo;s repository. Nothing here is legal, tax or investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/09/a-textile-sez-built-to-re-employ-mill.html", "A Textile SEZ Built to Re-Employ Mill Workers Has Shrunk 87% Since 2007"),
    ("https://masaladeutsch.blogspot.com/2026/09/india-built-offshore-insurance-hub-it.html", "India Built an Offshore Insurance Hub. It Writes $12 Million of Direct Cover a Year."),
    ("https://masaladeutsch.blogspot.com/2026/08/where-indias-factories-actually-get.html", "Where India&rsquo;s Factories Actually Get Built &mdash; IEM State &amp; Sector Analysis"),
    ("https://masaladeutsch.blogspot.com/2026/09/where-indias-fdi-actually-lands-state.html", "Where India&rsquo;s FDI Actually Lands: 24 Quarters of DPIIT&rsquo;s Own State-and-District Data"),
]

build("Trade · Industrial Policy · 27 October 2026",
      "The DESH Bill Never Came. India Is Rewriting Its SEZ Law One Rule at a Time",
      f"In 2022 the government promised a new law to turn export zones into development hubs that could also sell in India. The Bill stalled over tax breaks and never reached Parliament. Four years on, parts of it are arriving by notification, {95} of 372 notified zones sit idle, and an &ldquo;SEZ 2.0&rdquo; report has yet to be published.",
      body, sources, related, OUT)
print("idle", round(IDLE_SHARE, 1), "aprdec25", round(APRDEC_25, 2), "q4", round(Q4_25, 2), round(Q4_26, 2), round((Q4_26 / Q4_25 - 1) * 100, 1), "share", round(SHARE_FY25, 1), "fy growth", round((FY26 / FY25 - 1) * 100, 1))
