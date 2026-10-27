import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-semicon-2.html'

# ---------------------------------------------------------------- data
ISM1_OUTLAY = 76000            # Rs crore, notified Dec 2021
ISM2_OUTLAY = 127500           # Rs crore, Cabinet July 2026
# name, place, type, investment Rs crore (Cabinet approvals as reported), approved, status Oct 2026, producing
PROJECTS = [
    ("Tata Electronics with PSMC", "Dholera, Gujarat", "Silicon wafer fab", 91526, "Feb 2024", "Under construction; commissioning targeted for 2028", False),
    ("Tata Semiconductor Assembly and Test", "Jagiroad, Assam", "Assembly and test (ATMP)", 27000, "Feb 2024", "Under construction; one industry blog calls it operational, not confirmed", False),
    ("Micron Technology", "Sanand, Gujarat", "Memory assembly and test", 22516, "Jun 2023", "In commercial production (DRAM and NAND)", True),
    ("CG Power with Renesas and Stars", "Sanand, Gujarat", "Outsourced assembly and test (OSAT)", 7584, "Feb 2024", "In commercial production", True),
    ("HCL with Foxconn", "Jewar, Uttar Pradesh", "OSAT, display-driver chips", 3706, "May 2025", "Foundation laid Feb 2026; full operation targeted for 2028", False),
    ("Kaynes Semicon", "Sanand, Gujarat", "OSAT", 3307, "Sep 2024", "In commercial production", True),
    ("SiCSem", "Bhubaneswar, Odisha", "Silicon-carbide fab and ATMP", 2066, "Aug 2025", "No construction update found", False),
    ("3D Glass Solutions", "Bhubaneswar, Odisha", "Advanced packaging", 1943, "Aug 2025", "No construction update found", False),
    ("ASIP Technologies", "Andhra Pradesh", "OSAT", 468, "Aug 2025", "No construction update found", False),
    ("CDIL", "Mohali, Punjab", "Discrete devices", 117, "Aug 2025", "In commercial production from Sep 2026", True),
    ("Crystal Matrix; Suchi Semicon", "Dholera and Surat, Gujarat", "GaN micro-LED display fab with ATMP; packaging", 3936, "May 2026", "Suchi in commercial production from Sep 2026; Crystal Matrix approved", None),
]
N_PROJECTS = 12                # the last row is two projects
TOTAL_INV = sum(p[3] for p in PROJECTS)
PRODUCING_INV = sum(p[3] for p in PROJECTS if p[6])
FAB_INV = PROJECTS[0][3]
assert 163000 < TOTAL_INV < 165000          # reported as about Rs 1.64 lakh crore
AUG25_FOUR = sum(p[3] for p in PROJECTS if p[4] == "Aug 2025")
assert AUG25_FOUR == 4594                   # reported total for the four August 2025 approvals
MAX_SUPPORT = TOTAL_INV * 0.5               # if every project got ISM 1.0's maximum 50%

# central spending on the semiconductor programme, Rs crore
SPEND = [("2023-24", 681.11, "actual"), ("2024-25", 638, "actual"), ("2025-26", 4300, "revised estimate"), ("2026-27", 8000, "budget")]
ISM2_BE = 1000                              # separate ISM 2.0 line, BE 2026-27
SPENT_TO_FY26 = sum(v for y, v, k in SPEND[:3])
SHARE_SPENT = SPENT_TO_FY26 / ISM1_OUTLAY * 100
SHARE_PRODUCING = PRODUCING_INV / TOTAL_INV * 100
SHARE_FAB = FAB_INV / TOTAL_INV * 100
N_PRODUCING = 5


def chart_spend():
    W, L, top, bh, gap, lab = 400, 10, 26, 20, 9, 120
    H = top + (len(SPEND) + 1) * (bh + gap) + 26
    sc = (W - L - lab - 60) / ISM1_OUTLAY
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Central spending on the semiconductor programme by year against the Rs 76,000 crore outlay.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Central spending on the chip programme, Rs crore</text>']
    rows = [(f"{y} ({k})", v, "#1c5d99" if k == "actual" else "#d9a441") for y, v, k in SPEND] + [("ISM 1.0 outlay", ISM1_OUTLAY, "#868e96")]
    for i, (n, v, col) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 14}" font-size="9.5" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{max(v * sc, 2):.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + max(v * sc, 2) + 4:.1f}" y="{y + 14}" font-size="10" fill="#212529">{v:,.0f}</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">2023-24: parliamentary committee; later years: Union Budget via PRS. Earlier years not found.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_invest():
    W, L, top, bh = 400, 10, 40, 26
    H = top + bh + 52
    sc = (W - 2 * L) / TOTAL_INV
    segs = [("Producing", PRODUCING_INV, "#1c5d99"), ("Tata fab, due 2028", FAB_INV, "#a5402c"),
            ("Other, not yet producing", TOTAL_INV - PRODUCING_INV - FAB_INV, "#868e96")]
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Of about Rs {TOTAL_INV / 1e5:.2f} lakh crore of approved chip investment, {SHARE_PRODUCING:.0f}% is in plants producing, {SHARE_FAB:.0f}% in the Tata fab due in 2028.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Approved investment, Rs {TOTAL_INV / 1e5:.2f} lakh crore, by status</text>']
    x = L
    for i, (n, v, col) in enumerate(segs):
        w = v * sc
        s.append(f'<rect x="{x:.1f}" y="{top}" width="{w:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{x + w / 2:.1f}" y="{top + 17}" font-size="10.5" fill="#fff" text-anchor="middle" font-weight="700">{v / TOTAL_INV * 100:.0f}%</text>')
        lx = L + i * 130
        s.append(f'<rect x="{lx}" y="20" width="9" height="9" fill="{col}"/><text x="{lx + 13}" y="28" font-size="9.5" fill="#212529">{n}</text>')
        x += w
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Producing: Micron, CG Semi, Kaynes, CDIL (Suchi&rsquo;s share of a joint approval not split out).</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Investment as approved by the Cabinet. This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_projects():
    return table(["Project", "Where", "What", "Investment (Rs crore)", "Approved", "Status, October 2026"],
                 [(n, w, t, f"{inv:,}", a, st) for n, w, t, inv, a, st, _ in PROJECTS])


def t_compare():
    return table(["", "Semicon India (ISM 1.0)", "Semicon 2.0"], [
        ("Outlay", f"Rs {ISM1_OUTLAY:,} crore (2021)", f"Rs {ISM2_OUTLAY:,} crore (July 2026)"),
        ("Silicon fabs", "Up to 50% of project cost", "40% of eligible capital spending, for 300-mm wafer fabs"),
        ("Compound, photonics, sensor and discrete fabs", "Up to 50%", "35% of eligible capital spending"),
        ("Assembly, test and packaging", "Up to 50%", "Covered as a pillar; rate not found in the sources checked"),
        ("Equipment, materials, chemicals and gases", "Not covered", "30% of capital spending for equipment R&amp;D facilities, plus an incentive tied to domestically sourced components"),
        ("Chip design", "Design Linked Incentive", "9% of net sales for five years, capped at Rs 30 crore an application"),
        ("Window", "Open-ended approvals", "Open for applications for three years; projects preferably within six; mid-term review after three"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{N_PRODUCING} of {N_PROJECTS}</b><span>approved chip projects in commercial production, all assembly or packaging; no wafer fab yet</span></div>
<div class="gb-stat"><b>~{SHARE_SPENT:.0f}%</b><span>of the Rs 76,000 crore first programme spent by the end of 2025-26 (Rs {SPENT_TO_FY26:,.0f} crore, at the revised estimate)</span></div>
<div class="gb-stat"><b>{SHARE_PRODUCING:.0f}%</b><span>of the Rs {TOTAL_INV / 1e5:.2f} lakh crore approved investment is in plants already producing</span></div>
<div class="gb-stat"><b>Rs 1.27 lakh cr</b><span>for Semicon 2.0, at lower support rates for fabs and with new money for equipment and materials</span></div>
</div>'''

body = f"""
{stats}

<p>This blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/indias-mobile-phone-pli-beat-every.html">piece on the electronics schemes</a> found that India&rsquo;s mobile-phone incentive beat every target while its chip programme had only a few plants producing. In July the Cabinet approved a second round, Semicon 2.0, with Rs {ISM2_OUTLAY:,} crore. This piece sets out where each of the first round&rsquo;s {N_PROJECTS} approved projects stands in October 2026, how much of the first round&rsquo;s money has been spent, and what the second round changes.</p>

<h2 class="gb-h2">Where the twelve projects stand</h2>
{t_projects()}
<p class="gb-note">Investment figures are the totals announced at Cabinet approval; Tata&rsquo;s Assam plant is also listed at Rs 27,120 crore in some sources. The four August 2025 approvals sum to Rs {AUG25_FOUR:,} crore, matching the reported total; Crystal Matrix and Suchi were approved together at about Rs 3,936 crore. Statuses are from news reports and ministers&rsquo; statements; no official project-wise table is published.</p>
<p>At SEMICON India in September, the government said five units were in commercial production: Micron, CG Semi and Kaynes in Sanand, and CDIL in Mohali and Suchi in Surat, which started then. All five assemble, test or package chips; none makes wafers. The one silicon fab, Tata&rsquo;s at Dholera, is due to be commissioned in 2028, and HCL and Foxconn&rsquo;s plant at Jewar is also aimed at 2028.</p>
{chart_invest()}
<p>Measured by money rather than plant count, the picture is starker. The producing plants account for about Rs {PRODUCING_INV:,} crore, {SHARE_PRODUCING:.0f}% of the approved Rs {TOTAL_INV:,} crore. The Tata fab alone is {SHARE_FAB:.0f}%. Most of what has been approved is capacity that does not yet exist.</p>

<h2 class="gb-h2">How much has been spent</h2>
{chart_spend()}
<p>The central government pays its support in instalments as projects reach milestones, so spending lags approvals. A parliamentary committee reported that the ministry spent Rs 681.11 crore of Rs 1,503.36 crore allocated to the programme in 2023-24, surrendering more than half. The Union Budget shows Rs 638 crore actually spent in 2024-25, a revised estimate of Rs 4,300 crore for 2025-26 and Rs 8,000 crore budgeted for 2026-27, with a further Rs {ISM2_BE:,} crore for Semicon 2.0. PRS Legislative Research put utilisation at 23% of the budget in 2023-24 and 9% in 2024-25.</p>
<p>Adding the three years gives about Rs {SPENT_TO_FY26:,.0f} crore by March 2026 if the revised estimate is fully spent, about {SHARE_SPENT:.0f}% of the Rs {ISM1_OUTLAY:,} crore outlay; spending before 2023-24 was not found but is likely small. Yet the outlay is effectively committed: if every approved project received the first round&rsquo;s maximum support of 50% of cost, the total would be about Rs {MAX_SUPPORT:,.0f} crore. Actual rates and state top-ups vary, so that figure is a ceiling, but it explains why new approvals needed a second round even though most of the first round&rsquo;s money has not yet been paid.</p>

<h2 class="gb-h2">What Semicon 2.0 changes</h2>
{t_compare()}
<p>The second round is larger but pays less per project. Silicon fabs get 40% of eligible capital spending instead of up to 50% of project cost, and compound and specialty fabs get 35%. It also pays for things the first round did not: equipment, materials, chemicals and gases, which are where much of a fab&rsquo;s supply chain lies, and chip design through a sales-linked incentive. Its time limit is tighter: applications close after three years, and projects are preferably to be completed within six.</p>
<p>The lesson of the first round is that approval is the easy part. The second round&rsquo;s money will be spent as slowly as the first&rsquo;s unless projects reach their milestones faster, and the five producing units so far are the smaller, quicker assembly plants.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>MeitY should publish a project-wise table for every approved project, updated quarterly: approved investment, central support approved, support released, investment made and date of commercial production.</li>
<li>The Union Budget should show approved commitments under the semiconductor programmes alongside yearly spending, so that the gap between money promised and money paid is visible.</li>
<li>Semicon 2.0 should set and publish milestones for each project at approval, with a review if a project misses two in a row.</li>
<li>Production figures for the five operating units, in chips or wafers a month, should be published so &ldquo;commercial production&rdquo; can be measured.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>No official project-wise status or disbursement table was found; statuses come from news reports and ministers&rsquo; remarks, and the status of SiCSem, 3D Glass Solutions and ASIP could not be confirmed. Spending figures come from a parliamentary committee report and PRS&rsquo;s budget analysis, read through search-engine text; the 2023-24 figure may be labelled differently from later years, and spending before 2023-24 was not found. The Semicon 2.0 support rates are from news coverage of the notification, and the rate for assembly and packaging units was not found. Sources disagree on whether the outlay was Rs 1.25 or Rs 1.27 lakh crore; Rs 1.25 lakh crore was the Finance Ministry&rsquo;s clearance in June and Rs 1.27 lakh crore the Cabinet&rsquo;s approval in July.</p>
"""

sources = ("Semicon 2.0: Cabinet approval, July 2026 (PM India; Upstox; Indian Chemical News; Vision IAS; NEXT IAS); notified support rates and design incentive per Upstox; Finance Ministry clearance of Rs 1.25 lakh crore, June 2026 (Republic World, DT Next, Angel One). "
           "Projects: Cabinet approvals for Micron (June 2023), Tata-PSMC, Tata Assam and CG Power (February 2024), Kaynes (September 2024), HCL-Foxconn (May 2025), SiCSem, 3D Glass Solutions, CDIL and ASIP (August 2025; Governance Now, Outlook Business, Morung Express) and Crystal Matrix and Suchi (May 2026; Entrepreneur India, Drishti IAS); 12 projects worth about Rs 1.64 lakh crore (Business Today, September 2026; Amitabh Kant, October 2026); five units in production (Upstox, NewKerala, Indian Infrastructure, SEMICON India 2026); HCL-Foxconn timeline (MySmartPrice). "
           "Spending: parliamentary standing committee on 2023-24 (Goodreturns, Inc42); PRS Legislative Research, Demand for Grants 2026-27 analysis for MeitY. "
           "Shares of investment, the spending share and the maximum-support ceiling are this blog&rsquo;s arithmetic (builder in the repository at out/research/semicon-2/). Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/indias-mobile-phone-pli-beat-every.html", "India&rsquo;s Mobile-Phone PLI Beat Every Target. Its Chip-Fab Scheme Has 5 of 12 Plants Actually Producing."),
    ("https://masaladeutsch.blogspot.com/2026/09/indias-display-fab-scheme-got-two.html", "India&rsquo;s Display Fab Scheme Got Two Billion-Dollar Bids and Approved Neither"),
    ("https://masaladeutsch.blogspot.com/2026/08/the-water-bill-nobody-mentions-what.html", "The Water Bill Nobody Mentions: What Taiwan&rsquo;s Chip Crisis Says About India&rsquo;s Fab Plans"),
]

build("Industrial Policy · 27 October 2026",
      "India Has Approved 12 Chip Plants and Paid Out About 7% of the Money. Semicon 2.0 Adds Rs 1.27 Lakh Crore",
      f"Five of the first round&rsquo;s twelve projects are producing, all of them assembly or packaging plants holding {SHARE_PRODUCING:.0f}% of the approved investment. About Rs {SPENT_TO_FY26:,.0f} crore of the Rs 76,000 crore had been spent by March 2026. The second round pays less per fab but covers equipment and materials.",
      body, sources, related, OUT)
print(dict(total=TOTAL_INV, producing=PRODUCING_INV, share_prod=round(SHARE_PRODUCING, 1), share_fab=round(SHARE_FAB, 1), spent=SPENT_TO_FY26, share_spent=round(SHARE_SPENT, 1), max_support=round(MAX_SUPPORT)))
