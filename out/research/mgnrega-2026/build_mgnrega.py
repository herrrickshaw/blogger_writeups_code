import sys, json
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-rural-wage-floor-real-pay.html'
D = json.load(open('/home/user/blogger_writeups_code/out/research/mgnrega-2026/data.json'))
J25, S26, W = D['cpi_al_jun2025'], D['cpi_al_sep2026'], D['wages_fy26_to_jul2026']

# All-India CPI-AL (2019=100), MoSPI data service
MONTHS = ["Jun 25", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan 26", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep 26"]
IDX = [134.08, 135.31, 136.34, 136.23, 136.40, 137.40, 137.12, 137.07, 136.57, 136.99, 137.30, 138.52, 140.06, 141.65, 143.40, 144.82]
YOY = {"Jun 2025": 1.73, "Dec 2025": 0.04, "Jun 2026": 4.46, "Sep 2026": 6.30}

ROWS = []
for s, (o, n) in W.items():
    if s == "All India":
        continue
    w = (n / o - 1) * 100
    p = (S26[s] / J25[s] - 1) * 100
    r = ((n / o) / (S26[s] / J25[s]) - 1) * 100
    ROWS.append((s, o, n, w, p, r))
ROWS.sort(key=lambda x: x[5])
LOSERS = [r for r in ROWS if r[5] < 0]
AI_O, AI_N = W["All India"]
AI_W = (AI_N / AI_O - 1) * 100
AI_P = (S26["All India"] / J25["All India"] - 1) * 100
AI_R = ((AI_N / AI_O) / (S26["All India"] / J25["All India"]) - 1) * 100
JUN_SEP = (IDX[-1] / IDX[12] - 1) * 100
SIMPLE_OLD = sum(o for _, o, _, _, _, _ in ROWS) / len(ROWS)
AT_370 = [s for s, o, *_ in ROWS if o >= 370]
assert len(LOSERS) == 8 and len(ROWS) == 17 and round(AI_W, 1) == 9.6 and sorted(AT_370) == ["Goa", "Haryana", "Karnataka"]


def chart_index():
    W_, L, T, H = 400, 34, 22, 170
    lo, hi = 132, 146
    pw, ph = W_ - L - 12, H - T - 34
    x = lambda i: L + i * pw / (len(IDX) - 1)
    y = lambda v: T + (hi - v) / (hi - lo) * ph
    s = [f'<svg viewBox="0 0 {W_} {H}" width="100%" role="img" aria-label="Consumer price index for agricultural labourers, all India, June 2025 to September 2026: from 134.08 to 144.82, flat until March 2026 and rising fast from April.">',
         f'<text x="{L - 24}" y="12" font-size="12" fill="#495057">Prices for farm labourers, all India (CPI-AL, 2019 = 100)</text>']
    for v in (134, 138, 142, 146):
        s.append(f'<line x1="{L}" y1="{y(v):.1f}" x2="{L + pw}" y2="{y(v):.1f}" stroke="#e9ecef"/>')
        s.append(f'<text x="{L - 4}" y="{y(v) + 3:.1f}" font-size="9" fill="#868e96" text-anchor="end">{v}</text>')
    xr = x(13)
    s.append(f'<line x1="{xr:.1f}" y1="{T}" x2="{xr:.1f}" y2="{T + ph}" stroke="#a5402c" stroke-dasharray="3 3"/>')
    s.append(f'<text x="{xr - 4:.1f}" y="{T + 10}" font-size="9" fill="#a5402c" text-anchor="end">new wages, 1 Jul 2026</text>')
    s.append('<polyline fill="none" stroke="#1c5d99" stroke-width="2.2" points="' + " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(IDX)) + '"/>')
    for i in (0, 7, 15):
        s.append(f'<text x="{x(i):.1f}" y="{T + ph + 13}" font-size="9" fill="#868e96" text-anchor="middle">{MONTHS[i]}</text>')
    s.append(f'<text x="{x(15) - 2:.1f}" y="{y(IDX[-1]) - 5:.1f}" font-size="9.5" fill="#1c5d99" text-anchor="end">{IDX[-1]}</text>')
    s.append(f'<text x="{x(0) + 2:.1f}" y="{y(IDX[0]) + 13:.1f}" font-size="9.5" fill="#1c5d99">{IDX[0]}</text>')
    s.append(f'<text x="{L - 24}" y="{H - 4}" font-size="9" fill="#6c757d">Source: Labour Bureau CPI-AL via MoSPI data service. Monthly, June 2025 &ndash; September 2026.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_states():
    W_, L, T, bh, gap, lab = 400, 10, 26, 13, 5, 100
    H = T + len(ROWS) * (bh + gap) + 24
    zero = L + lab + 120
    sc = 120 / 12
    s = [f'<svg viewBox="0 0 {W_} {H}" width="100%" role="img" aria-label="Real change in the job-guarantee wage by state, June 2025 to September 2026: from minus 9.1% in Andhra Pradesh to plus 10.9% in Uttar Pradesh.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Real change in the daily wage, Jun 2025 &rarr; Sep 2026 (%)</text>']
    s.append(f'<line x1="{zero}" y1="{T - 4}" x2="{zero}" y2="{H - 20}" stroke="#adb5bd"/>')
    for i, (st, o, n, w, p, r) in enumerate(ROWS):
        yy = T + i * (bh + gap)
        col = "#a5402c" if r < 0 else "#2b8a3e"
        x0 = zero + min(r, 0) * sc
        s.append(f'<text x="{L + lab - 4}" y="{yy + 10}" font-size="9.5" fill="#212529" text-anchor="end">{st}</text>')
        s.append(f'<rect x="{x0:.1f}" y="{yy}" width="{abs(r) * sc:.1f}" height="{bh}" fill="{col}"/>')
        tx = zero + r * sc + (3 if r >= 0 else -3)
        s.append(f'<text x="{tx:.1f}" y="{yy + 10}" font-size="9" fill="#212529" text-anchor="{"start" if r >= 0 else "end"}">{r:+.1f}</text>')
    s.append(f'<text x="{L}" y="{H - 6}" font-size="9" fill="#6c757d">Wage rise to Jul 2026 deflated by each state&rsquo;s CPI-AL, Jun 2025 to Sep 2026.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def t_states():
    h = "".join(f"<th>{c}</th>" for c in ["State", "2025-26 wage (Rs/day)", "From 1 Jul 2026", "Wage rise", "Farm-labour prices, Jun 2025 &rarr; Sep 2026", "Real change"])
    r = "".join(f"<tr><td>{s}</td><td>{o:.0f}</td><td>{n:.0f}</td><td>{w:+.1f}%</td><td>{p:+.1f}%</td><td><b>{rr:+.1f}%</b></td></tr>" for s, o, n, w, p, rr in ROWS)
    r += f"<tr><td><b>National average</b></td><td>{AI_O}</td><td>{AI_N}</td><td>{AI_W:+.1f}%</td><td>{AI_P:+.1f}%</td><td><b>{AI_R:+.1f}%</b></td></tr>"
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>+{AI_W:.1f}%</b><span>national average job-guarantee wage from 1 July 2026, Rs {AI_O} to Rs {AI_N} a day</span></div>
<div class="gb-stat"><b>+{JUN_SEP:.1f}%</b><span>rise in farm labourers&rsquo; prices in the three months to September 2026 alone</span></div>
<div class="gb-stat"><b>8 of 17</b><span>major states where the new wage buys less than the 2025-26 wage did in June 2025</span></div>
<div class="gb-stat"><b>&minus;9.1%</b><span>real change in Andhra Pradesh; +10.9% in Uttar Pradesh</span></div>
</div>'''

losers = ", ".join(f"{s} ({r:+.1f}%)" for s, _, _, _, _, r in LOSERS[:4])

body = f"""
{stats}

<p>For the first three months of 2026-27, the Centre did not revise wages under the rural employment guarantee. Workers were paid the 2025-26 rates while the scheme moved from MGNREGA to its replacement, the Viksit Bharat &ndash; Guarantee for Rozgar and Ajeevika Mission (Gramin) Act, known as VB-G RAM G. The new law took effect on 1 July 2026 with new wage rates (notification S.O. 3518(E) of 30 June): a national floor of Rs 300 a day and, by the ministry&rsquo;s figures, a national average of Rs {AI_N} against Rs {AI_O} before, a rise of {AI_W:.1f}% (described officially as &ldquo;over 10%&rdquo;).</p>
<p>This blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/a-17-rural-pay-rise-that-nobody-received.html">piece in August</a> showed how a change in the Labour Bureau&rsquo;s village sample made rural wages look as if they had jumped 17% when they had not, and how the same rebased price index for agricultural labourers (CPI-AL) feeds the rules that set these wages. This follow-up asks the next question: once prices are taken into account, did the July rise leave workers better off? Nationally, only just. State by state, the answer splits in two.</p>

<h2 class="gb-h2">Prices turned just as wages were reset</h2>
{chart_index()}
<p>For most of the year the price side helped. Year-on-year inflation for agricultural labourers was {YOY["Jun 2025"]}% in June 2025 and {YOY["Dec 2025"]}% in December, so a frozen wage lost little. Then it turned. The index rose from 140.06 in June 2026 to 144.82 in September, {JUN_SEP:.1f}% in three months, and year-on-year inflation reached {YOY["Sep 2026"]}% in September, the highest in the new series. Over the whole stretch from June 2025, when the rebased series begins, to September 2026, prices for agricultural labourers rose {AI_P:.1f}%. Against the {AI_W:.1f}% wage rise, that leaves a real gain of about {AI_R:.1f}% nationally, most of it gone within one quarter of the new rates taking effect.</p>

<h2 class="gb-h2">The floor lifted the poorest states; the rest fell behind</h2>
{chart_states()}
<p>The national figure hides two different outcomes. The Rs 300 floor raised wages by 15&ndash;19% in states that had been paying Rs 252&ndash;261, such as Uttar Pradesh, Bihar, Jharkhand, Assam, West Bengal, Madhya Pradesh and Chhattisgarh. Their workers came out 4&ndash;11% ahead after prices. States already above the floor got rises of 0.3&ndash;4.0%, apart from Goa (7.4%) and Kerala (8.7%), and several of them are where rural inflation has been highest; Gujarat, lifted from Rs 288 to the floor, got 4.2%. In {len(LOSERS)} of the 17 states examined the new wage buys less than the old one did in June 2025: {losers}, as well as Haryana, Karnataka, Punjab and Gujarat.</p>
{t_states()}
<p class="gb-note">Wage rates: S.O. 3518(E) of 30 June 2026 and the March 2025 notification for 2025-26, as reported by Upstox, SCC Online, The Tribune, Zee Business and others; some sites give different figures for a few states (Karnataka, Punjab, Goa, Kerala), and the gazette-based lists were used. Prices: CPI-AL (2019 = 100) for each state, June 2025 and September 2026, MoSPI data service. The 2025-26 rates took effect in April 2025; the rebased index starts in June 2025, and the all-India old-series index barely moved between April and May 2025. The comparison asks what the July 2026 wage buys in September 2026 against what the 2025-26 wage bought in June 2025.</p>
<p>Telangana is the starkest case. Its wage rose by one rupee, from Rs 307 to Rs 308, while prices for its agricultural labourers rose 9.7%. Andhra Pradesh&rsquo;s rose Rs 5 against prices up 11.8%. The notification does not say how each state&rsquo;s rate was calculated, so it is not possible to tell from the published material whether these small rises reflect a formula, the timing of the price data used, or a decision to concentrate the increase on the floor.</p>

<h2 class="gb-h2">Two corrections to the earlier piece</h2>
<p>The August piece reported that the March 2025 notification gave &ldquo;a national average of Rs 370 a day&rdquo;, and set that against the Rs 298.8 average in the VB-G RAM G announcement as two official figures it could not reconcile. The state rates settle it. In 2025-26 only Haryana (Rs 400), Goa (Rs 378) and Karnataka (Rs 370) paid Rs 370 or more; the simple average of the 17 states above is about Rs {SIMPLE_OLD:.0f}. Rs 370 cannot have been a national average, while Rs 298.8 is consistent with the state rates. The August piece also gave June 2025 inflation the wrong way round: per the MoSPI data service it was 1.73% for agricultural labourers (CPI-AL) and 1.42% for rural labourers (CPI-RL). Both points are corrected in that piece.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Ministry of Rural Development should publish, with every wage notification, the method used to set each state&rsquo;s rate: the price index, the months it covers and any floor or cap applied.</li>
<li>Wage rates under VB-G RAM G should be revised against the latest twelve months of each state&rsquo;s CPI-AL, so that a state with 9&ndash;12% price growth does not receive a rise of under 2%.</li>
<li>The ministry should publish its national average wage with the weights used, so figures such as Rs 298.8 and Rs 327.4 can be reproduced from the state rates.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The gazette notifications could not be opened directly; state wage rates come from news lists of the notifications, which disagree for a few states. The price comparison uses each state&rsquo;s overall CPI-AL; it does not account for the extra 25 days of work the new law guarantees, which raises what a household can earn without changing the daily rate. Whether workers in each state actually received the higher rate from 1 July, and how many days they worked, is not covered.</p>
"""

sources = ("Wage rates: Ministry of Rural Development notification S.O. 3518(E), 30 June 2026, effective 1 July 2026, as reported by Upstox, SCC Online, The Tribune and Outlook Business (national average Rs 298.8 to Rs 327.4, Rs 300 floor, Haryana Rs 409, Goa Rs 406, Kerala Rs 401, Karnataka Rs 382, Punjab Rs 360, Tamil Nadu Rs 345, Maharashtra Rs 317, Andhra Pradesh Rs 312, Telangana Rs 308); 2025-26 rates from the notification of 27 March 2025 as reported by Zee Business, Adda247, HR Informative and a Maharashtra government notice; the April&ndash;June 2026 freeze per Civilsdaily and Outlook Business. "
           "Prices: Consumer Price Index for Agricultural Labourers (2019 = 100), all India and by state, June 2025 to September 2026, and the 1986-87-base series for April and May 2025, Labour Bureau via the MoSPI data service. "
           "Wage rises, price changes and real changes are this blog&rsquo;s arithmetic; data in out/research/mgnrega-2026/ in the blog&rsquo;s repository. Nothing here is legal or financial advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/a-17-rural-pay-rise-that-nobody-received.html", "A 17% Rural Pay Rise That Nobody Received"),
    ("https://masaladeutsch.blogspot.com/2026/08/cpi-inflation-heatmap-india-june-2026.html", "CPI inflation heatmap, India"),
]

build("Rural Economy · Prices & Inflation · 27 October 2026",
      "Rural Job-Guarantee Pay Rose 9.6% in July. In Eight States It Buys Less Than in 2025",
      f"Wages were frozen for three months, then a Rs 300 floor lifted the poorest states by up to 19%. But prices for farm labourers rose {JUN_SEP:.1f}% in the next quarter alone, and in Andhra Pradesh, Telangana, Maharashtra and five other states the new wage buys less than the old one did.",
      body, sources, related, OUT)
print([(s, round(r, 1)) for s, *_, r in ROWS], round(AI_P, 1), round(AI_R, 1), round(SIMPLE_OLD))
