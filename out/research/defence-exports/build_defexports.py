import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-defence-exports.html'

# Defence exports, Rs crore (Ministry of Defence releases; FY17 from the data.gov.in series, FY18-FY21 as tabled in
# news coverage of MoD figures). FY = April-March; "FY26" = 2025-26.
EXP = [("FY17", 1522), ("FY18", 4682), ("FY19", 10745), ("FY20", 9115), ("FY21", 8434),
       ("FY22", 12814), ("FY23", 15920), ("FY24", 21083), ("FY25", 23622), ("FY26", 38424)]
# Value of defence production, Rs crore. FY18/FY19 from DDP-linked reports (rounded); FY24 and FY25 are the
# later, revised MoD figures (first announced as 1,26,887 and 1,50,590). FY26 is "about 1.78 lakh crore"
# (= 15.6% over 1,54,071), so it is computed, not quoted.
PROD = [("FY17", 74054), ("FY18", 78817), ("FY19", 80502), ("FY20", 79071), ("FY21", 84643),
        ("FY22", 94845), ("FY23", 108684), ("FY24", 127434), ("FY25", 154071)]
PROD.append(("FY26", round(154071 * 1.156)))
PRODD = dict(PROD)
EXPD = dict(EXP)

# Export split by exporter type, Rs crore (MoD releases, April 2025 and April 2026)
SPLIT = {"FY24": (15209, 5874), "FY25": (15233, 8389), "FY26": (17353, 21071)}   # (private, DPSU and other PSU)
PRIV_PROD_26 = 42000      # private-sector production FY26, "around Rs 42,000 crore" (PIB, June 2026), rounded
AUTH_24, AUTH_25 = 1507, 1762          # export authorisations issued by DDP
EXPORTERS_25, EXPORTERS_26 = 128, 145  # registered exporters
TGT_PROD, TGT_EXP, TGT_YEAR = 300000, 50000, "2028-29"

def cagr(a, b, n):
    return ((b / a) ** (1 / n) - 1) * 100

e26, e25, e24, e17 = EXPD["FY26"], EXPD["FY25"], EXPD["FY24"], EXPD["FY17"]
p26 = PRODD["FY26"]
EXP_GROWTH = (e26 / e25 - 1) * 100
DPSU_RISE = SPLIT["FY26"][1] - SPLIT["FY25"][1]
PRIV_RISE = SPLIT["FY26"][0] - SPLIT["FY25"][0]
DPSU_SHARE_OF_RISE = DPSU_RISE / (e26 - e25) * 100
DPSU_GROWTH = (SPLIT["FY26"][1] / SPLIT["FY25"][1] - 1) * 100
PRIV_GROWTH = (SPLIT["FY26"][0] / SPLIT["FY25"][0] - 1) * 100
PRIV_2YR = cagr(SPLIT["FY24"][0], SPLIT["FY26"][0], 2)
EXP_CAGR_9 = cagr(e17, e26, 9)
EXP_CAGR_3 = cagr(EXPD["FY23"], e26, 3)
PROD_CAGR_9 = cagr(PRODD["FY17"], p26, 9)
PROD_CAGR_3 = cagr(PRODD["FY23"], p26, 3)
NEED_EXP = cagr(e26, TGT_EXP, 3)
NEED_PROD = cagr(p26, TGT_PROD, 3)
EXP_SHARE_26 = e26 / p26 * 100
EXP_SHARE_17 = e17 / PRODD["FY17"] * 100
PRIV_EXPORT_RATIO = SPLIT["FY26"][0] / PRIV_PROD_26 * 100
PSU_EXPORT_RATIO = SPLIT["FY26"][1] / (p26 - PRIV_PROD_26) * 100

def L(v):  # Rs crore in Indian grouping
    s = f"{v:,.0f}"
    if v >= 100000:
        a, b = divmod(int(round(v)), 1000)
        hs = f"{a:,}".replace(",", "")
        # 1,23,456 style
        h = hs[::-1]
        parts = [h[i:i + 2] for i in range(0, len(h), 2)]
        s = ",".join(parts)[::-1] + "," + f"{b:03d}"
    return s


def chart_exports():
    W, L0, top, bot = 360, 30, 34, 44
    H = 260
    n = len(EXP)
    plot_w = W - L0 - 8
    bw = plot_w / n * 0.68
    mx = 40000
    ph = H - top - bot
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="India&rsquo;s defence exports by financial year, 2016-17 to 2025-26, in rupees crore. They rose from 1,522 crore to 38,424 crore.">',
         f'<text x="10" y="12" font-size="12" fill="#495057">Defence exports, Rs crore, by financial year</text>',
         f'<text x="10" y="25" font-size="9.5" fill="#6c757d">April&ndash;March years; FY26 = 2025-26</text>']
    for g in (10000, 20000, 30000, 40000):
        y = top + ph - g / mx * ph
        s.append(f'<line x1="{L0}" x2="{W - 8}" y1="{y:.1f}" y2="{y:.1f}" stroke="#dee2e6"/>')
        s.append(f'<text x="{L0 - 4}" y="{y + 3:.1f}" font-size="9" fill="#6c757d" text-anchor="end">{g // 1000}k</text>')
    for i, (fy, v) in enumerate(EXP):
        x = L0 + i * plot_w / n + (plot_w / n - bw) / 2
        h = v / mx * ph
        y = top + ph - h
        s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="#1c5d99"/>')
        lab = f"{v / 1000:.1f}k"
        s.append(f'<text x="{x + bw / 2:.1f}" y="{y - 3:.1f}" font-size="9.5" fill="#212529" text-anchor="middle">{lab}</text>')
        s.append(f'<text x="{x + bw / 2:.1f}" y="{top + ph + 12:.1f}" font-size="9.5" fill="#212529" text-anchor="middle">{fy}</text>')
    s.append(f'<text x="10" y="{H - 16}" font-size="9" fill="#6c757d">k = thousand crore. Ministry of Defence figures as reported;</text>')
    s.append(f'<text x="10" y="{H - 4}" font-size="9" fill="#6c757d">FY18&ndash;FY21 from tables in news coverage.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_years():
    rows = []
    for fy, p in PROD:
        e = EXPD[fy]
        pl = "about 1,78,000" if fy == "FY26" else L(p)
        rows.append((fy, pl, L(e), f"{e / p * 100:.1f}%"))
    return table(["Year", "Production, Rs crore", "Exports, Rs crore", "Exports as % of production"], rows)


def t_split():
    rows = []
    for fy in ("FY24", "FY25", "FY26"):
        pv, ps = SPLIT[fy]
        rows.append((fy, L(pv), L(ps), L(pv + ps), f"{ps / (pv + ps) * 100:.0f}%"))
    return table(["Year", "Private firms", "DPSUs and other PSUs", "Total", "Public-sector share"], rows)


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>Rs {L(e26)} cr</b><span>defence exports in 2025-26, up {EXP_GROWTH:.1f}% from Rs {L(e25)} crore and about 25 times the Rs {L(e17)} crore of 2016-17</span></div>
<div class="gb-stat"><b>{DPSU_SHARE_OF_RISE:.0f}%</b><span>of last year&rsquo;s Rs {L(e26 - e25)} crore rise came from public-sector firms, whose exports grew {DPSU_GROWTH:.0f}%; private exports grew {PRIV_GROWTH:.0f}%</span></div>
<div class="gb-stat"><b>{NEED_EXP:.0f}% a year</b><span>is all exports now need to reach the Rs 50,000 crore target by {TGT_YEAR}; production needs {NEED_PROD:.0f}% a year to reach Rs 3 lakh crore</span></div>
<div class="gb-stat"><b>8.2%</b><span>of the world&rsquo;s major-arms imports went to India in 2021&ndash;25, the second-largest share after Ukraine (SIPRI)</span></div>
</div>'''

body = f"""
{stats}

<p>India&rsquo;s Ministry of Defence (MoD) reported two records in 2026. Defence exports in 2025-26 reached Rs {L(e26)} crore, announced on 2 April, and the value of domestic defence production reached about Rs 1.78 lakh crore, announced in June. Both are presented as proof that India is becoming an arms supplier rather than only a buyer. This piece sets the two numbers against their own history, asks who did the exporting, and checks what the government&rsquo;s 2029 targets actually require.</p>

<h2 class="gb-h2">Exports have grown 25-fold in nine years</h2>
{chart_exports()}
<p>From Rs {L(e17)} crore in 2016-17, exports rose to Rs {L(EXPD["FY19"])} crore in 2018-19, dipped in 2019-20 and 2020-21, and have risen every year since. Over the nine years the compound growth rate is about {EXP_CAGR_9:.0f}% a year; over the last three, about {EXP_CAGR_3:.0f}%. The 2025-26 jump of {EXP_GROWTH:.1f}% is the largest single-year rise since 2018-19. The Defence Secretary put the 2025-26 total at about &euro;3.6 billion.</p>
<p>Production grew far more slowly, about {PROD_CAGR_9:.0f}% a year over the same nine years and about {PROD_CAGR_3:.0f}% over the last three. Exports have therefore become a much bigger part of what the industry makes: about {EXP_SHARE_17:.0f}% of production in 2016-17 and about {EXP_SHARE_26:.0f}% in 2025-26. The two series are not strictly comparable (production is the value of output by public and private firms; exports are the value of export authorisations executed), so the ratio is indicative only.</p>
{t_years()}
<p class="gb-note">Rs crore; 1 lakh crore = 1,00,000 crore. Production for 2017-18 and 2018-19 is from reports citing the Department of Defence Production and may be rounded. The ministry later revised 2023-24 production from Rs 1,26,887 crore to Rs 1,27,434 crore and 2024-25 from Rs 1,50,590 crore to Rs 1,54,071 crore; the revised figures are used. 2025-26 production is calculated here as 15.6% above Rs 1,54,071 crore, matching the ministry&rsquo;s &ldquo;about Rs 1.78 lakh crore&rdquo;.</p>

<h2 class="gb-h2">The latest jump came from state-owned firms</h2>
<p>Until 2024-25 private companies did most of the exporting: they supplied about 72% of exports in 2023-24 and 64.5% in 2024-25. In 2025-26 that flipped. Defence public sector undertakings (DPSUs, such as Hindustan Aeronautics, Bharat Electronics and the former ordnance factories) and other public-sector firms exported Rs {L(SPLIT["FY26"][1])} crore, up {DPSU_GROWTH:.0f}% in one year. Private firms exported Rs {L(SPLIT["FY26"][0])} crore, up {PRIV_GROWTH:.0f}%.</p>
{t_split()}
<p>Of the Rs {L(e26 - e25)} crore increase, Rs {L(DPSU_RISE)} crore ({DPSU_SHARE_OF_RISE:.0f}%) came from the public sector and Rs {L(PRIV_RISE)} crore from private firms. Private exports were Rs {L(SPLIT["FY24"][0])} crore in 2023-24 and Rs {L(SPLIT["FY25"][0])} crore in 2024-25, so over two years they have grown about {PRIV_2YR:.0f}% a year. The record is real, but its growth is concentrated in a handful of state firms and a few large orders, which makes it lumpier than the headline suggests.</p>
<p>Relative to what each sector makes, private firms still export more. The ministry put private production at around Rs {L(PRIV_PROD_26)} crore in 2025-26, about 24% of the total. On that basis private firms exported roughly {PRIV_EXPORT_RATIO:.0f}% of their output and public-sector firms about {PSU_EXPORT_RATIO:.0f}%. This is rough, for the same reason as above: exports and production are measured differently.</p>

<h2 class="gb-h2">What is being sold, and to whom</h2>
<p>The ministry does not publish exports by country or product, so the picture comes from officials&rsquo; statements and reported contracts:</p>
<ul>
<li><b>Missiles.</b> The Philippines signed a $375 million contract for BrahMos shore-based anti-ship missile batteries in 2022 and has received its first deliveries. Indonesia and Vietnam deals have been reported, with values that differ between reports. Armenia became the first foreign buyer of the Akash air-defence system, with a first battery delivered in late 2024.</li>
<li><b>Ammunition and artillery shells.</b> On 23 October 2026 the Defence Secretary said India had become the third-largest supplier of defence goods to Europe, mainly because of European demand for standard ammunition and artillery shells. A Bloomberg report he cited, based on Indian trade data, put ammunition exports at about $872 million. Reuters has reported that some Indian shells sold to European buyers were passed on to Ukraine.</li>
<li><b>Parts for foreign manufacturers.</b> The United States is reported to be the largest destination, mainly for sub-systems and components: aircraft and helicopter structures made in India for Boeing and Lockheed Martin supply chains, including through Tata joint ventures in Hyderabad.</li>
<li><b>Other items</b> named by the ministry and in reports: bulletproof jackets and helmets, Dornier-228 aircraft, radars, small arms, fast interceptor boats and lightweight torpedoes.</li>
</ul>
<p>The ministry says Indian defence goods now reach more than 80 countries. The Department of Defence Production issued {L(AUTH_25)} export authorisations in 2024-25, up from {L(AUTH_24)} the year before. A full-year 2025-26 count was not found. The number of exporting firms rose from {EXPORTERS_25} to {EXPORTERS_26}.</p>

<h2 class="gb-h2">The 2029 targets: one is close, one is not</h2>
<p>The government&rsquo;s targets are Rs 3 lakh crore of annual production and Rs 50,000 crore of exports by 2029. Read as the 2028-29 financial year, three years from the 2025-26 base, exports need to grow only about {NEED_EXP:.0f}% a year, well below anything recorded in the last five years. Production needs about {NEED_PROD:.0f}% a year, slightly above its recent three-year pace of {PROD_CAGR_3:.0f}% and nearly twice its nine-year pace of {PROD_CAGR_9:.0f}%. Some reports date the export target to 2030; that would make it easier still.</p>
<p>So the export goal is likely to be met even if growth slows sharply, while the production goal depends on the large domestic orders now being placed actually being delivered on time.</p>

<h2 class="gb-h2">India still buys far more than it sells</h2>
<p>The Stockholm International Peace Research Institute (SIPRI), which tracks deliveries of major weapons, ranks India the world&rsquo;s second-largest arms importer in 2021&ndash;25, with 8.2% of global imports, behind Ukraine. India&rsquo;s imports fell about 4% between 2016&ndash;20 and 2021&ndash;25. Russia&rsquo;s share of them fell to about 40%, from about 70% in 2011&ndash;15, while France supplied about 29% and Israel about 15%. SIPRI counts only major weapons, not the parts, ammunition and body armour that make up much of India&rsquo;s exports, so its import and export rankings are not a like-for-like trade balance.</p>
<p>The ministry&rsquo;s main tool for cutting imports is the Positive Indigenisation List: items that defence public-sector firms and the armed forces may no longer import after a set date. This blog has <a href="https://masaladeutsch.blogspot.com/2026/08/5071-items-you-cannot-import-and-rs.html">tracked those lists separately</a>. Six DPSU lists now cover 5,417 items and five Department of Military Affairs lists another 509, and the ministry&rsquo;s own figures for how much has been replaced do not reconcile.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The ministry should publish exports by broad product group (complete platforms, ammunition, components, body armour and so on) and by region each year. This would show how much of the record is one-off missile orders or wartime ammunition demand.</li>
<li>Exports should be reported in the same units as production, with the authorisations executed (not just issued) and the delivered value shown separately, so that the export share of production can be calculated properly.</li>
<li>When production figures are revised, as 2023-24 and 2024-25 both were, the release should say so and give the old figure.</li>
<li>Private-sector exports, flat at around Rs 15,000&ndash;17,000 crore for three years, need their own review. Export finance, faster authorisations for repeat orders and government-to-government backing should not be available mainly to state firms.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The ministry&rsquo;s press releases on pib.gov.in and mod.gov.in could not be opened from the research machine, so every figure here comes from news coverage and study-guide summaries quoting them. Where those disagreed, the figure most often repeated with an exact value was used. The 2017-18 to 2020-21 export figures and the 2017-18 and 2018-19 production figures come from secondary tables, and the 2025-26 production figure is calculated from the stated growth rate. No country-wise or product-wise export data were found, the number of export authorisations for 2025-26 was not found, and reports differ on whether Indian defence goods reach more than 80 or more than 100 countries. The period covered by the Bloomberg ammunition figure is not clear from the reports. Whether the Rs 50,000 crore target is for 2028-29 or 2029-30 also varies between reports.</p>
"""

sources = ("Exports 2025-26, private/public split, exporters: Ministry of Defence release of 2 April 2026 as reported by IANS, Outlook Business, ETV Bharat and Bajaj Broking. "
           "Exports 2024-25, split and 1,762 authorisations: MoD release of 1 April 2025 as reported by The Tribune, Outlook Business and IDSA commentary (7 April 2025). "
           "Earlier export years: data.gov.in defence-export series (2016-17 Rs 1,521.86 crore); CUTS International briefing paper 8; Ajai Shukla, Business Standard (April 2023); Swarajya; Angel One. "
           "Production: MoD release of June 2026 (Rs 1.78 lakh crore, 15.6% over Rs 1,54,071 crore, private sector around Rs 42,000 crore) via IANS and Telangana Today; earlier years from The Tribune, Janes and Greater Kashmir quoting MoD and the Department of Defence Production. "
           "Targets: Drishti IAS summary (27 October 2026) and Outlook Business. Europe and ammunition: All India Radio/newsonair and South China Morning Post (24 October 2026); Reuters via Ukrinform. "
           "BrahMos, Akash and product lists: IMPRI, idrw.org, ThePrint, Eurasian Times, WION. Imports: SIPRI Trends in International Arms Transfers 2025 (March 2026) as summarised by Vision IAS and other study guides. "
           "Growth rates, shares and ratios are this blog&rsquo;s arithmetic (builder in the repository at out/research/defence-exports/). Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/5071-items-you-cannot-import-and-rs.html", "5,417 Items You Cannot Import &mdash; and the Ministry&rsquo;s Own Two Numbers for What Replaced Them"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-military-quantum-plan-has-four.html", "India&rsquo;s Military Quantum Plan Has Four Pillars. So Far, the Forces Have Bought Only One"),
    ("https://masaladeutsch.blogspot.com/2026/08/priority-export-destinations-by-growth.html", "Priority Export Destinations by Growth Sector, &amp; Real PLI Coverage"),
]

build("Defence · 30 October 2026",
      f"Defence Exports Rose 63% to Rs {L(e26)} Crore. State Firms Supplied {DPSU_SHARE_OF_RISE:.0f}% of the Rise, and the 2029 Export Target Is Already Within Reach",
      f"India sold a record Rs {L(e26)} crore of defence goods in 2025-26, 25 times the 2016-17 level. Public-sector exports grew {DPSU_GROWTH:.0f}% in a year while private exports grew {PRIV_GROWTH:.0f}%. Exports now need only {NEED_EXP:.0f}% a year to hit Rs 50,000 crore; production needs {NEED_PROD:.0f}% to hit Rs 3 lakh crore. India remains the world&rsquo;s second-largest arms importer.",
      body, sources, related, OUT)
print("exp growth", round(EXP_GROWTH, 2), "dpsu share of rise", round(DPSU_SHARE_OF_RISE, 1), "dpsu g", round(DPSU_GROWTH, 1), "priv g", round(PRIV_GROWTH, 1),
      "priv 2yr", round(PRIV_2YR, 1), "cagr9", round(EXP_CAGR_9, 1), "cagr3", round(EXP_CAGR_3, 1), "prod9", round(PROD_CAGR_9, 1), "prod3", round(PROD_CAGR_3, 1),
      "need exp", round(NEED_EXP, 1), "need prod", round(NEED_PROD, 1), "share17", round(EXP_SHARE_17, 1), "share26", round(EXP_SHARE_26, 1),
      "priv ratio", round(PRIV_EXPORT_RATIO), "psu ratio", round(PSU_EXPORT_RATIO), "p26", p26, L(p26), "x25", round(e26 / e17, 1),
      "priv share24", round(15209 / 21083 * 100, 1))
