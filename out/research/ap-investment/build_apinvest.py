import sys, csv, collections
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-ap-investment.html'
REPO = '/home/user/blogger_writeups_code'

# ---------------------------------------------------------------- claims
SIPB_TOTAL_LCR = 14.05          # Rs lakh crore, 387 projects, 21 SIPB meetings (official release, 18 Sep 2026)
SIPB_PROJECTS, SIPB_JOBS_LAKH = 387, 10.79
SIPB21_CR, SIPB21_N, SIPB21_JOBS = 22177.84, 28, 19739
BOB_NATIONAL_LCR, BOB_AP_SHARE = 26.6, 25.3   # Bank of Baroda: proposed investment, Apr-Dec FY26
BOB_AP_LCR = BOB_NATIONAL_LCR * BOB_AP_SHARE / 100
GSDP_2526_LCR, GSDP_2627_LCR = 18.3, 19.75   # AP budget estimates (PRS budget analyses)
LS_PROJECTS, LS_CR, LS_DONE = 10, 6962, 2      # Lok Sabha reply, July 2026: DPIIT/Invest India-monitored projects grounded

# ---------------------------------------------------------------- this blog's IEM data
# Part B (implemented), Rs crore, by year, from the published state analysis (DPIIT IEM Part B)
PARTB = {
    "Andhra Pradesh": [10350, 45217, 10536, 23662, 50680],
    "Tamil Nadu": [13684, 9268, 6746, 7763, 7166],
    "Karnataka": [6327, 8042, 6368, 7272, 14454],
    "Telangana": [6739, 3915, 3464, 6158, 4858],
    "Maharashtra": [45855, 35675, 52201, 42949, 61308],
    "Gujarat": [104968, 39259, 61407, 208025, 246595],
}
YEARS = [2021, 2022, 2023, 2024, 2025]
# 2020-2025 window: Part A filed, Part B implemented (Rs crore), same post
WINDOW = {
    "Andhra Pradesh": (174194, 150285),
    "Tamil Nadu": (97274, 45811),
    "Karnataka": (361856, 49028),
    "Telangana": (96692, 31191),
    "Maharashtra": (726292, 271703),
    "Gujarat": (417504, 695120),
}
AP_B5 = sum(PARTB["Andhra Pradesh"])
AP_B_AVG = AP_B5 / 5
AP_B_PEAK = max(PARTB["Andhra Pradesh"])
AP_A6 = WINDOW["Andhra Pradesh"][0]
assert AP_B5 == 140445
YEARS_AT_PEAK = SIPB_TOTAL_LCR * 1e5 / AP_B_PEAK
YEARS_AT_AVG = SIPB_TOTAL_LCR * 1e5 / AP_B_AVG
MULT_A = SIPB_TOTAL_LCR * 1e5 / AP_A6
MULT_B = SIPB_TOTAL_LCR * 1e5 / AP_B5
SHARE_GSDP = SIPB_TOTAL_LCR / GSDP_2526_LCR * 100

# Long-run follow-through by count, from the parsed IEM register (data/iem/iem_records.csv):
# Part A memoranda filed 2015-2022 that later appear in a Part B list (by memo number or company name).
csv.field_size_limit(10 ** 9)
NAMES = {"ANDHRA PRADESH": "Andhra Pradesh", "TAMIL NADU": "Tamil Nadu", "KARNATAKA": "Karnataka",
         "TELANGANA": "Telangana", "MAHARASHTRA": "Maharashtra", "GUJARAT": "Gujarat"}
filed, reached = collections.Counter(), collections.Counter()
for row in csv.DictReader(open(f"{REPO}/data/iem/iem_records.csv", encoding="utf-8")):
    st = NAMES.get(row["state"].strip().upper())
    if not st or row["part"] != "A":
        continue
    y = int(row["period_from"][:4])
    if 2015 <= y <= 2022:
        filed[st] += 1
        if row["in_part_b"] in ("memo", "name"):
            reached[st] += 1
CONV = {s: reached[s] / filed[s] * 100 for s in NAMES.values()}

# ---------------------------------------------------------------- largest announced projects (Rs crore, as reported)
PROJECTS = [
    ("NTPC Green Energy&ndash;NREDCAP green hydrogen hub, Pudimadaka (Anakapalli)", 185000, "Green hydrogen and derivatives, with renewable power", "Land leased (1,200 acres, 2024); first phase scheduled 2026&ndash;28 in the project plan; construction status not confirmed", False),
    ("BPCL refinery and petrochemical complex, Ramayapatnam", 145000, "Refinery, 9 Mt a year", "Final environmental clearance was expected by end-September 2026; cost to be firmed up after an EIL study; state wants operations by January 2029", True),
    ("ArcelorMittal Nippon Steel India, Rajayyapeta (Anakapalli)", 135964, "Integrated steel, 17.8 Mt a year in two phases", "Foundation stone 23 March 2026; first phase (about Rs 56,000&ndash;80,000 crore by different reports) targeted for 2029", True),
    ("Google with AdaniConneX and Airtel, Visakhapatnam", 135000, "AI data centre, about 1 GW", "Foundation stone 28 April 2026; due to open in 2028; a public-interest case on water is before the High Court", False),
    ("Reliance, Vizianagaram", 108010, "AI data centre and cable landing station", "About 855 acres allotted by order of 20 May 2026; reported incentives of about Rs 19,100 crore", False),
]
TOP5 = sum(p[1] for p in PROJECTS)
TOP5_IEM = sum(p[1] for p in PROJECTS if p[4])


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def chart_scale():
    rows = [("Investment board approvals, about 2 years", SIPB_TOTAL_LCR, "#a5402c"),
            ("Proposals tracked by Bank of Baroda, Apr&ndash;Dec FY26", BOB_AP_LCR, "#d9a441"),
            ("Factory projects filed (IEM Part A), 2020&ndash;25", AP_A6 / 1e5, "#1c5d99"),
            ("Factory projects built (IEM Part B), 2021&ndash;25", AP_B5 / 1e5, "#1c5d99"),
            ("Factory projects built in 2025 alone", AP_B_PEAK / 1e5, "#1c5d99")]
    W, L, top, bh, gap, lab = 400, 10, 24, 18, 22, 0
    H = top + len(rows) * (bh + gap) + 22
    sc = (W - L - 60) / 15
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Andhra Pradesh investment in Rs lakh crore: {SIPB_TOTAL_LCR} approved by the investment board against {AP_B5 / 1e5:.2f} implemented in large factory projects over five years.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Andhra Pradesh: announced vs built, Rs lakh crore</text>']
    for i, (n, v, col) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L}" y="{y + 9}" font-size="10" fill="#212529">{n}</text>')
        s.append(f'<rect x="{L}" y="{y + 13}" width="{max(v * sc, 1.5):.1f}" height="{bh - 4}" fill="{col}"/>')
        s.append(f'<text x="{L + v * sc + 4:.1f}" y="{y + 24}" font-size="10" fill="#212529">{v:.2f}</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">IEM covers large manufacturing only; board approvals also include power, data centres, IT and tourism.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_conv():
    rows = sorted(CONV.items(), key=lambda kv: -kv[1])
    W, L, top, bh, gap, lab = 400, 10, 30, 16, 8, 104
    H = top + len(rows) * (bh + gap) + 30
    sc = (W - L - lab - 60) / 60
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Share of large factory projects filed in 2015 to 2022 that later reported production, by state.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Factory filings that later reported production, %</text>',
         f'<text x="{L}" y="24" font-size="9.5" fill="#6c757d">IEM Part A filed 2015&ndash;2022, found in a Part B list by 2024</text>']
    for i, (n, v) in enumerate(rows):
        y = top + i * (bh + gap)
        col = "#a5402c" if n == "Andhra Pradesh" else "#1c5d99"
        s.append(f'<text x="{L + lab - 6}" y="{y + 12}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 12}" font-size="10" fill="#212529">{v:.0f}% of {filed[n]:,}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Matching by memo number or company name; undercounts projects whose Part B</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">entry cites neither. This blog&rsquo;s parse of DPIIT&rsquo;s IEM lists.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def t_states():
    rows = []
    for st in ["Andhra Pradesh", "Gujarat", "Maharashtra", "Karnataka", "Tamil Nadu", "Telangana"]:
        a, b = WINDOW[st]
        rows.append((st, f"{a:,}", f"{b:,}", f"{sum(PARTB[st]):,}", f"{PARTB[st][-1]:,}", f"{CONV[st]:.0f}%"))
    return table(["State", "Filed, 2020&ndash;25 (Rs cr)", "Built, 2020&ndash;25 (Rs cr)", "Built, 2021&ndash;25 (Rs cr)", "Built in 2025 (Rs cr)", "Filings 2015&ndash;22 that reached production (by count)"], rows)


def t_projects():
    return table(["Project", "Rs crore (as reported)", "What", "Status, October 2026"],
                 [(n, f"{v:,}", w, st) for n, v, w, st, _ in PROJECTS])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>Rs 14 lakh cr</b><span>(Rs {SIPB_TOTAL_LCR} lakh crore) approved by Andhra Pradesh&rsquo;s investment board across {SIPB_PROJECTS} projects since mid-2024</span></div>
<div class="gb-stat"><b>Rs {AP_B5 / 1e5:.2f} lakh cr</b><span>of large factory projects the state actually commissioned in 2021&ndash;2025 (IEM Part B)</span></div>
<div class="gb-stat"><b>{YEARS_AT_PEAK:.0f} years</b><span>to build Rs {SIPB_TOTAL_LCR} lakh crore at 2025&rsquo;s record pace of factory commissioning</span></div>
<div class="gb-stat"><b>{CONV["Andhra Pradesh"]:.0f}%</b><span>of Andhra&rsquo;s 2015&ndash;22 factory filings later reported production, more than Tamil Nadu&rsquo;s {CONV["Tamil Nadu"]:.0f}%</span></div>
</div>'''

body = f"""
{stats}

<p>On 18 September Andhra Pradesh&rsquo;s State Investment Promotion Board, chaired by Chief Minister N. Chandrababu Naidu, cleared 28 proposals worth Rs {SIPB21_CR:,.0f} crore with {SIPB21_JOBS:,} jobs. That took the board&rsquo;s total across 21 meetings to {SIPB_PROJECTS} projects, Rs {SIPB_TOTAL_LCR} lakh crore of potential investment and about {SIPB_JOBS_LAKH} lakh jobs, according to the state. The Federal asked the obvious question: how much of this is on the ground? In Tamil Nadu, the opposition says projects are leaving for Andhra; the Tamil Nadu government says most of the projects named went to Andhra before it took office.</p>
<p>This blog keeps its own record that can test both claims: the Industrial Entrepreneurs Memoranda (IEM) that large manufacturers file with DPIIT when they plan a project (Part A) and when it starts production (Part B). This piece sets the board&rsquo;s total against that record, lists the largest projects behind the headline, and looks at whether the Tamil Nadu-to-Andhra story shows up in the data.</p>

<h2 class="gb-h2">How big Rs 14 lakh crore is</h2>
{chart_scale()}
<p>Rs {SIPB_TOTAL_LCR} lakh crore is about {SHARE_GSDP:.0f}% of Andhra Pradesh&rsquo;s entire 2025-26 economic output (GSDP budgeted at Rs {GSDP_2526_LCR} lakh crore). It is about {MULT_A:.0f} times the value of all large factory projects the state&rsquo;s companies filed in 2020&ndash;2025, and {MULT_B:.0f} times what they commissioned in 2021&ndash;2025. At 2025&rsquo;s record pace of Rs {AP_B_PEAK:,} crore a year it would take about {YEARS_AT_PEAK:.0f} years to build; at the five-year average of Rs {AP_B_AVG:,.0f} crore, about {YEARS_AT_AVG:.0f}.</p>
<p>The comparison is not like for like, and the gap is partly explained by that. IEM filings cover only manufacturing above a size threshold. The board&rsquo;s approvals also include solar and wind farms, pumped storage, data centres, IT campuses, ports and tourism, none of which file an IEM. Bank of Baroda, counting proposals across all sectors, found Andhra had 25.3% of all new investment proposed in India in April&ndash;December 2025, about Rs {BOB_AP_LCR:.1f} lakh crore, with power the largest sector nationally. So the state&rsquo;s pipeline is genuinely large; the question is how much of it becomes projects, and how fast.</p>

<h2 class="gb-h2">Five projects make up more than half the total</h2>
{t_projects()}
<p>These five announcements add up to about Rs {TOP5 / 1e5:.1f} lakh crore, {TOP5 / (SIPB_TOTAL_LCR * 1e5) * 100:.0f}% of the board&rsquo;s headline, though not every one necessarily passed through the board. Only two, the BPCL refinery and the steel plant, worth about Rs {TOP5_IEM / 1e5:.1f} lakh crore together, are the kind of project that files an IEM, and both are still years from production. The two data centres and the hydrogen hub are counted in investment totals but will not appear in the factory record at all. None of the five was producing in October 2026.</p>
<p>The only official check on the ground so far is narrow. In July 2026 the Centre told the Lok Sabha that {LS_PROJECTS} projects monitored by DPIIT and Invest India had been grounded in Andhra over the previous two years, with about Rs {LS_CR:,} crore of estimated investment, and the opposition YSRCP says only {LS_DONE} had finished construction. That list covers only projects those two agencies track, so it understates what is under way; but no fuller official count of projects started or completed has been published.</p>

<h2 class="gb-h2">What Andhra&rsquo;s factory record actually shows</h2>
{chart_conv()}
{t_states()}
<p class="gb-note">Rupee figures are from this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/where-indias-factories-actually-get.html">state analysis of DPIIT&rsquo;s IEM data</a> (window 2020&ndash;2025; built by year 2021&ndash;2025). The follow-through percentages are from this blog&rsquo;s parse of the IEM register 2001&ndash;2024, counting Part A filings from 2015 (after the state was divided) to 2022 that later appear in a Part B list; filings after 2022 have had too little time. Built can exceed filed because projects filed before 2020 were commissioned inside the window.</p>
<p>On the record, Andhra is one of the better states at turning filings into factories. About {CONV["Andhra Pradesh"]:.0f}% of the large projects its companies filed in 2015&ndash;2022 later reported production, second among these six states only to Gujarat ({CONV["Gujarat"]:.0f}%), and ahead of Telangana ({CONV["Telangana"]:.0f}%), Maharashtra ({CONV["Maharashtra"]:.0f}%), Tamil Nadu ({CONV["Tamil Nadu"]:.0f}%) and Karnataka ({CONV["Karnataka"]:.0f}%). By value, it commissioned Rs {WINDOW['Andhra Pradesh'][1] / 1e5:.2f} lakh crore in 2020&ndash;2025 against Rs {AP_A6 / 1e5:.2f} lakh crore filed, and 2025 was its best year, at Rs {AP_B_PEAK:,} crore. The problem with the Rs {SIPB_TOTAL_LCR} lakh crore figure is not that Andhra fails to build; it is that the figure is an order of magnitude larger than anything the state has built.</p>

<h2 class="gb-h2">Is Tamil Nadu losing projects to Andhra?</h2>
<p>The factory record says the shift in large manufacturing is older than Tamil Nadu&rsquo;s change of government. Andhra commissioned Rs {sum(PARTB["Andhra Pradesh"]):,} crore of large factory projects in 2021&ndash;2025 against Tamil Nadu&rsquo;s Rs {sum(PARTB["Tamil Nadu"]):,} crore, more than three times as much, and it out-built Tamil Nadu in four of those five years. Its filings in 2020&ndash;2025 (Rs {AP_A6 / 1e5:.2f} lakh crore) were also well ahead of Tamil Nadu&rsquo;s (Rs {WINDOW['Tamil Nadu'][0] / 1e5:.2f} lakh crore). That fits The Federal&rsquo;s reading that most projects cited in the current row were already headed to Andhra. It does not settle individual cases such as Hyundai&rsquo;s reported shipbuilding plan, which a record ending in 2024 cannot show.</p>
<p>Tamil Nadu&rsquo;s modest IEM numbers also need care: much of its auto and electronics base was built before this window, and expansions by existing plants may be filed differently. But for new large projects, Andhra has been the stronger destination of the two since at least 2021.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>Andhra Pradesh&rsquo;s investment board should publish, for every approved project, the date of approval, land allotted, statutory clearances, construction start, commercial production and jobs on the payroll, updated quarterly, so &ldquo;approved&rdquo; can be told apart from &ldquo;built&rdquo;.</li>
<li>States should report investment approvals split by sector (manufacturing, power, data centres, IT, tourism), so totals can be compared with DPIIT&rsquo;s IEM record and with each other.</li>
<li>DPIIT should resume publishing state-wise IEM Part A and Part B lists with investment values in machine-readable form, which would let any state&rsquo;s claims be checked within a quarter.</li>
<li>Incentive packages above a threshold (such as the reported Rs 19,100 crore for the Reliance data centre and up to Rs 28,000 crore for the steel plant) should be tabled in the state assembly with their milestones.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The board&rsquo;s project list is not public, so this piece could not tell how much of the Rs {SIPB_TOTAL_LCR} lakh crore is manufacturing, how much is power or data centres, or whether the five large projects are all inside it. The Rs {SIPB_TOTAL_LCR} lakh crore and {SIPB_PROJECTS}-project totals come from one state-government release reported by the press. The IEM record covers only manufacturing projects above Rs 50 crore of plant and machinery (Rs 125 crore from April 2025), and this blog&rsquo;s matching of filings to production lists misses projects whose production entry cites neither the memorandum number nor the same company name, so the follow-through percentages are lower bounds. Project costs are as reported and differ between sources (the steel plant&rsquo;s first phase is put at Rs 56,000 crore or Rs 80,000 crore). Whether the BPCL refinery received its final environmental clearance in October could not be confirmed.</p>
"""

sources = ("Investment board: 21st SIPB meeting, 18 September 2026, and cumulative totals, per the Andhra Pradesh government release as reported by ThePrint (PTI), UNI, Construction World and Asianet Newsable; The Federal on investments &ldquo;on paper vs on the ground&rdquo; and on the Tamil Nadu-Andhra claims (2026). "
           "Lok Sabha reply on projects grounded (July 2026), as reported by LatestLY (ANI), News Arena and The News Mill. Bank of Baroda report on proposed investments, April&ndash;December FY26, as reported by Outlook Business and Deccan Herald (January 2026). "
           "GSDP: PRS Legislative Research, Andhra Pradesh Budget Analysis 2025-26 and 2026-27. "
           "Projects: ArcelorMittal Nippon Steel (ETV Bharat, News on AIR, GMK Center, March 2026); BPCL Ramayapatnam (Maritime Gateway, PSU Watch, Deccan Chronicle, September 2026); NTPC Green hydrogen hub (MNRE National Green Hydrogen Mission project document; pv magazine India); Google Visakhapatnam (Drishti IAS, April 2026; Kuwait Times, Gulf News, October 2026); Reliance Vizianagaram (Indian Infrastructure, CXOToday, Deccan Herald, May 2026). "
           "Factory record: this blog&rsquo;s analysis of DPIIT Industrial Entrepreneurs Memoranda, Parts A and B (state analysis, August 2026; IEM register parse 2001&ndash;2024, data/iem in the repository). Multiples, years-to-build and shares are this blog&rsquo;s arithmetic (builder at out/research/ap-investment/). Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/where-indias-factories-actually-get.html", "Where India&rsquo;s Factories Actually Get Built &mdash; IEM State &amp; Sector Analysis"),
    ("https://masaladeutsch.blogspot.com/2026/08/iem-conversion-historical-performance.html", "IEM Conversion &mdash; A Historical Performance Review (2017&ndash;2025)"),
    ("https://masaladeutsch.blogspot.com/2026/10/india-will-spend-rs-33660-crore-on.html", "India Will Spend Rs 33,660 Crore on Ready-Made Factory Parks. Its Existing Parks Have 1.25 Lakh Empty Plots"),
    ("https://masaladeutsch.blogspot.com/2026/08/where-indias-gigawatt-data-centre-bets.html", "Where India&rsquo;s Gigawatt Data-Centre Bets Actually Land"),
    ("https://masaladeutsch.blogspot.com/2026/10/closed-loop-or-open-loop-how-indias-new.html", "Closed Loop or Open Loop? How India&rsquo;s New Data Centres Should Be Cooled, Site by Site"),
]

build("Industrial Policy · 27 October 2026",
      "Andhra Pradesh Has Approved Rs 14 Lakh Crore of Investment in Two Years. Its Large Factory Projects Built Rs 1.4 Lakh Crore in Five",
      "The state&rsquo;s investment board says it has cleared 387 projects worth Rs 14.05 lakh crore. The factory record shows Andhra builds more of what it files than most states, but the headline is ten times anything it has built, and five announcements make up more than half of it.",
      body, sources, related, OUT)
print({k: round(v, 1) for k, v in CONV.items()}, dict(filed), "multA", round(MULT_A, 1), "multB", round(MULT_B, 1), "yrs", round(YEARS_AT_PEAK, 1), round(YEARS_AT_AVG, 1), "gsdp%", round(SHARE_GSDP), "bob", round(BOB_AP_LCR, 2), "top5", TOP5, TOP5 / 1404500)
