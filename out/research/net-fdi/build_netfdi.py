import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-net-fdi.html'

# ---------------------------------------------------------------- data, US$ billion, RBI
# FY20-FY23: RBI Handbook of Statistics, Table 146 (FY23 provisional).
# FY24: gross 71.3 and net 10.1 as later restated (Drishti/Lok Sabha); repatriation 44.5 (Business Standard, May 2025);
#       outward is the residual. First estimate (May 2024): gross 70.9, outward 15.96, net 10.58.
# FY25: first annual estimate, RBI Bulletin May 2025 (gross 81.04, repatriation 51.49, outward 29.2, net 0.353).
# FY26: RBI, as reported May 2026 (gross 94.53, repatriation 53.58, outward 33.3, net 7.65).
YEARS = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
GROSS = [74.390, 81.973, 84.835, 71.355, 71.3, 81.04, 94.53]
REPAT = [18.384, 27.046, 28.605, 29.349, 44.5, 51.49, 53.58]
OUTW = [12.993, 10.972, 17.644, 14.020, None, 29.2, 33.3]
NET_REPORTED = [43.013, 43.955, 38.587, 27.986, 10.1, 0.353, 7.65]
OUTW[4] = round(GROSS[4] - REPAT[4] - NET_REPORTED[4], 2)
NET = [round(g - r - o, 2) for g, r, o in zip(GROSS, REPAT, OUTW)]
for n, rep in zip(NET, NET_REPORTED):
    assert abs(n - rep) < 0.06, (n, rep)
TO_INDIA = [round(g - r, 2) for g, r in zip(GROSS, REPAT)]
REPAT_SH = [r / g * 100 for g, r in zip(GROSS, REPAT)]
OUTW_SH = [o / g * 100 for g, o in zip(GROSS, OUTW)]
NET_SH = [n / g * 100 for g, n in zip(GROSS, NET)]
G_A, N_A = sum(GROSS[:3]), sum(NET[:3])
G_B, N_B = sum(GROSS[4:]), sum(NET[4:])
R_B, O_B = sum(REPAT[4:]), sum(OUTW[4:])

# Foreign parents selling down through IPOs (offer for sale), US$ bn
HYUNDAI_USD = 3.3          # Hyundai Motor India, Oct 2024, entirely offer for sale by the Korean parent
LG_CR = 11607              # LG Electronics India, Oct 2025, entirely offer for sale by the Korean parent (Rs crore)
INR_USD_OCT25 = 88.8       # approximate rupee rate, Oct 2025 (assumption for conversion)
LG_USD = LG_CR * 1e7 / INR_USD_OCT25 / 1e9


def chart_flows():
    W, L, top, bh, gap, lab = 400, 10, 44, 18, 9, 54
    H = top + len(YEARS) * (bh + gap) + 30
    sc = (W - L - lab - 40) / 95
    cols = ("#a5402c", "#d9a441", "#1c5d99")
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Gross FDI into India split into repatriation by foreign investors, investment abroad by Indian firms, and net FDI, 2019-20 to 2025-26.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Where each year&rsquo;s gross FDI went, US$ billion</text>',
         f'<rect x="{L}" y="22" width="9" height="9" fill="{cols[0]}"/><text x="{L + 13}" y="30" font-size="9.5" fill="#212529">Taken out by foreign investors</text>',
         f'<rect x="{L + 160}" y="22" width="9" height="9" fill="{cols[1]}"/><text x="{L + 173}" y="30" font-size="9.5" fill="#212529">Indian firms abroad</text>',
         f'<rect x="{L + 280}" y="22" width="9" height="9" fill="{cols[2]}"/><text x="{L + 293}" y="30" font-size="9.5" fill="#212529">Net FDI</text>']
    for i, y_ in enumerate(YEARS):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 13}" font-size="10" fill="#212529" text-anchor="end">{y_}</text>')
        x = L + lab
        for v, col in zip((REPAT[i], OUTW[i], NET[i]), cols):
            w = v * sc
            s.append(f'<rect x="{x:.1f}" y="{y}" width="{max(w, 0.8):.1f}" height="{bh}" fill="{col}"/>')
            if w > 22:
                s.append(f'<text x="{x + w / 2:.1f}" y="{y + 13}" font-size="9.5" fill="#fff" text-anchor="middle" font-weight="700">{v:.0f}</text>')
            x += w
        s.append(f'<text x="{x + 4:.1f}" y="{y + 13}" font-size="9.5" fill="#212529">{GROSS[i]:.0f}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Bar length = gross inflow (number at end). Net FDI in 2024-25 was 0.35.</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">RBI data; 2023-24 to 2025-26 are first or restated estimates. This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_flows():
    rows = []
    for i, y in enumerate(YEARS):
        rows.append((y, f"{GROSS[i]:.1f}", f"{REPAT[i]:.1f} ({REPAT_SH[i]:.0f}%)", f"{TO_INDIA[i]:.1f}", f"{OUTW[i]:.1f} ({OUTW_SH[i]:.0f}%)", f"{NET[i]:.2f}" if NET[i] < 1 else f"{NET[i]:.1f}"))
    return table(["Year", "Gross inflow ($ bn)", "Repatriated (% of gross)", "Net into India ($ bn)", "Indian FDI abroad (% of gross)", "Net FDI ($ bn)"], rows)


def t_terms():
    return table(["Term", "What it counts"], [
        ("Gross inflow", "New equity, reinvested earnings and other capital that foreign direct investors put into Indian companies in the year"),
        ("Repatriation and disinvestment", "Money foreign direct investors take back out by selling shares (to other investors, in an IPO, or back to the company) or winding down holdings"),
        ("Direct investment to India", "Gross inflow minus repatriation"),
        ("FDI by India (outward)", "Money Indian companies invest in their own foreign subsidiaries and acquisitions"),
        ("Net FDI", "Direct investment to India minus FDI by India: the figure in the balance of payments that helps pay for the current-account deficit"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>${GROSS[-1]:.1f} bn</b><span>gross FDI into India in 2025-26, a record</span></div>
<div class="gb-stat"><b>${NET[-1]:.2f} bn</b><span>net FDI in 2025-26, after ${NET[-2]:.2f} bn in 2024-25 and ${NET[0]:.0f} bn in 2019-20</span></div>
<div class="gb-stat"><b>{REPAT_SH[-1]:.0f}%</b><span>of 2025-26&rsquo;s gross inflow left again as repatriation by foreign investors, against {REPAT_SH[0]:.0f}% in 2019-20</span></div>
<div class="gb-stat"><b>${OUTW[-1]:.1f} bn</b><span>invested abroad by Indian firms in 2025-26, {OUTW[-1] / OUTW[0]:.1f} times the 2019-20 level</span></div>
</div>'''

body = f"""
{stats}

<p>Foreign companies put a record ${GROSS[-1]:.1f} billion of direct investment into India in 2025-26, according to the Reserve Bank of India. Net foreign direct investment, the number that matters for the balance of payments, was ${NET[-1]:.2f} billion. A year earlier it had been ${NET[-2]:.2f} billion, the lowest on record, on gross inflows of ${GROSS[-2]:.0f} billion. In 2019-20 and 2020-21, on smaller gross inflows, net FDI was about ${NET[0]:.0f} billion a year.</p>
<p>Gross money has not stopped coming. What changed is how much leaves again: foreign investors selling out and taking their money home, and Indian companies investing abroad. This piece splits each year&rsquo;s gross inflow into those parts, shows what drives the outflows, and asks what the low net figure does and does not mean. It complements this blog&rsquo;s analyses of <a href="https://masaladeutsch.blogspot.com/2026/09/where-indias-fdi-actually-lands-state.html">where FDI lands by state</a> and <a href="https://masaladeutsch.blogspot.com/2026/10/indias-fdi-moved-to-software-and.html">which sectors it goes to</a>, which use DPIIT&rsquo;s gross equity data.</p>

<h2 class="gb-h2">Four numbers, not one</h2>
{t_terms()}
<p>DPIIT&rsquo;s widely quoted FDI figures are gross equity inflows. The RBI&rsquo;s balance-of-payments figures net out the money going the other way. Both are correct; they answer different questions.</p>

<h2 class="gb-h2">Gross held up; the outflows grew faster</h2>
{chart_flows()}
{t_flows()}
<p class="gb-note">US$ billion. 2019-20 to 2022-23 from the RBI&rsquo;s Handbook of Statistics (2022-23 provisional). 2023-24 uses the restated gross and net figures, with Indian FDI abroad as the residual; the first estimate in May 2024 was gross ${70.9:.1f} billion, abroad $15.96 billion, net $10.58 billion. 2024-25 is the first annual estimate (May 2025); later releases revise it, and one later report puts 2024-25 net FDI at about $1 billion. 2025-26 is as reported in May 2026; figures tabled in Parliament give repatriation of $54.04 billion and net FDI of $6.95 billion.</p>
<p>Over the three years 2019-20 to 2021-22, gross inflows totalled ${G_A:.0f} billion and net FDI ${N_A:.0f} billion. Over 2023-24 to 2025-26, gross inflows were higher, ${G_B:.0f} billion, but net FDI was ${N_B:.0f} billion. Of that later ${G_B:.0f} billion, ${R_B:.0f} billion went back out to foreign investors and ${O_B:.0f} billion went abroad with Indian companies.</p>
<p>Repatriation is the larger force. It rose from {REPAT_SH[0]:.0f}% of gross inflow in 2019-20 to {REPAT_SH[5]:.0f}% in 2024-25, and was still {REPAT_SH[-1]:.0f}% in 2025-26. Indian companies&rsquo; investment abroad also climbed, from ${OUTW[0]:.0f} billion to ${OUTW[-1]:.0f} billion a year, and in 2024-25 it alone absorbed {OUTW_SH[5]:.0f}% of gross inflow.</p>

<h2 class="gb-h2">Who is taking money out</h2>
<p>The RBI does not publish repatriation by sector or by type of investor, so the drivers have to be pieced together. Three stand out in the record.</p>
<p><b>Private-equity and venture-capital exits.</b> Funds that bought into Indian companies in the 2010s and the 2021 boom have been selling. Bain and the Indian Venture and Alternate Capital Association put PE/VC exits at about $24 billion in 2024, and EY-IVCA counted $11.6 billion in the first half of 2025 alone. A January 2026 note by MUFG Research found that equity-market deal values, including IPOs, track gross FDI repatriation closely over time, and expected sales by existing shareholders in IPOs to stay high in 2026.</p>
<p><b>Foreign parents listing Indian subsidiaries.</b> Hyundai Motor India&rsquo;s IPO in October 2024, about ${HYUNDAI_USD:.1f} billion and the largest in Indian history at the time, was entirely an offer for sale by its Korean parent: none of the money went to the Indian company. LG Electronics India&rsquo;s Rs {LG_CR:,} crore IPO in October 2025, about ${LG_USD:.1f} billion, was likewise all sold by the parent. Each counts as a foreign direct investor taking money out, even though the factories, jobs and control stay in India.</p>
<p><b>A strong stock market.</b> High valuations make India a good place to sell. The RBI has described the rise in repatriation as a sign of a mature market in which foreign investors can enter and exit easily, and pointed to the hot IPO market of 2024-25, including Hyundai and Swiggy, as the occasion for long-term investors to realise gains.</p>

<h2 class="gb-h2">Indian companies going abroad</h2>
<p>Outward FDI is the other half of the story. In April&ndash;September 2025 it was $16.32 billion, up from $12.17 billion a year earlier, and the main destinations were Singapore, Mauritius, the United Arab Emirates and the United States, according to RBI data. The sectors were mainly financial, insurance and business services, manufacturing, and agriculture and mining. UNCTAD&rsquo;s World Investment Report 2026, which uses a different method, put India&rsquo;s outward FDI for calendar 2025 at $35.66 billion, up 47%. Singapore and Mauritius are holding-company locations, so the final destination of much of this money is not visible in the data.</p>

<h2 class="gb-h2">What the low net figure does and does not mean</h2>
<p>It does not mean foreign companies have stopped investing in India: gross inflows are at a record, and much repatriation is a sale from one investor to another, often in an IPO, that leaves the company and its capital in place. Nor is outward investment a loss in itself; it reflects Indian firms buying assets and markets abroad.</p>
<p>It does mean that FDI now does much less to finance India&rsquo;s current-account deficit than it did. At ${NET[0]:.0f}&ndash;{NET[1]:.0f} billion a year before 2022, net FDI was a stable, long-term source of dollars. At ${NET[5]:.2f}&ndash;{NET[-1]:.1f} billion it is not, which leaves the deficit to be paid for by portfolio flows, which can reverse quickly, and by borrowing. And because a record-high gross number is the one most often quoted, it gives a misleading picture of how much new foreign capital is staying in the country.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The RBI should publish repatriation each quarter by route (IPO offer for sale, secondary sale, buyback, liquidation) and by broad investor type (PE/VC fund, foreign parent company, other), so that exits by funds can be told apart from parents reducing their stakes.</li>
<li>DPIIT&rsquo;s FDI factsheet should show RBI&rsquo;s repatriation and net FDI figures next to its gross equity numbers, with the difference explained.</li>
<li>Outward FDI data should report the ultimate destination of investment routed through Singapore, Mauritius and similar holding locations, as far as the reporting forms already allow.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The RBI&rsquo;s own pages could not be opened directly; figures for 2023-24 to 2025-26 come from news reports of its bulletins and from figures tabled in Parliament, and they are revised in later releases, so the most recent years may change. The 2023-24 outward figure here is a residual, not a published number. No breakdown of repatriation by sector, route or investor type was found, so the drivers above are drawn from IPO and private-equity data that overlap with, but are not the same as, the RBI&rsquo;s repatriation figures. The LG Electronics dollar value uses an approximate exchange rate of Rs {INR_USD_OCT25} to the dollar.</p>
"""

sources = ("RBI data: Handbook of Statistics on the Indian Economy, Table 146, Foreign Investment Inflows (2019-20 to 2022-23); RBI Monthly Bulletin, May 2024 and May 2025, as reported by Business Standard (21 May 2024; 22 May 2025), The South First and The Wire; 2025-26 annual figures as reported by Outlook Business and Vajiram &amp; Ravi (May 2026) and Finance Ministry figures tabled in Parliament (The South First); first-half 2025-26 figures and outward destinations and sectors (Business Standard, 24 November 2025); restated 2023-24 figures (Drishti IAS, June 2025). RBI Governor on repatriation as a sign of a mature market (Business Standard, DT Next, June 2025). "
           "Private equity: Bain &amp; Company and IVCA India Private Equity Report 2025 (via AMS Shardul and Law.asia); EY-IVCA monthly releases and Trendbook 2026. MUFG Research, IndiaPulse (16 January 2026). IPOs: Hyundai Motor India (Business Standard, October 2024); LG Electronics India (The Week, Business Standard, October 2025). UNCTAD World Investment Report 2026 (via Business Standard and Vision IAS). "
           "Shares of gross inflow, three-year totals and the residual 2023-24 outward figure are this blog&rsquo;s arithmetic (builder in the repository at out/research/net-fdi/). Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/09/where-indias-fdi-actually-lands-state.html", "Where India's FDI Actually Lands: 24 Quarters of DPIIT's Own State-and-District Data"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-fdi-moved-to-software-and.html", "India&rsquo;s FDI Moved to Software and Trading After 2017"),
    ("https://masaladeutsch.blogspot.com/2026/10/abu-dhabi-paid-2-billion-for-binance.html", "Abu Dhabi Paid $2 Billion for a Binance Stake in Stablecoins. India&rsquo;s FDI Rules Have No Box for That."),
]

build("Markets &amp; Finance · 27 October 2026",
      "India Got a Record $94.5 Billion of FDI Last Year. Net of Exits and Investment Abroad, $7.7 Billion Stayed",
      "Gross foreign direct investment is at a record, but most of it leaves again: foreign investors cashing out through IPOs and private-equity exits, and Indian companies investing abroad. Net FDI, which helps pay for the current-account deficit, has fallen from about $43 billion a year to single digits.",
      body, sources, related, OUT)
print("NET", NET, "OUTW24", OUTW[4], "REPATSH", [round(x) for x in REPAT_SH], "G_A", round(G_A), "N_A", round(N_A), "G_B", round(G_B), "N_B", round(N_B), "R_B", round(R_B), "O_B", round(O_B), "LG", round(LG_USD, 2))
