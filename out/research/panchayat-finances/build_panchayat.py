import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-panchayat-finances.html'

# RBI, Finances of Panchayati Raj Institutions (24 January 2024), Table II.3: village panchayat revenue receipts, Rs crore
# (eGramSwaraj data compiled by MoPR; about 2.41 lakh village panchayats, 95% of the total, report receipts)
RR = {  # year: (total, own tax, own non-tax, grants, central grants, state grants)
    "2020-21": (41744, 703, 1365, 39675, 30264, 9138),
    "2021-22": (37971, 786, 1415, 35770, 27060, 8412),
    "2022-23": (35354, 737, 1494, 33123, 24699, 8148),
}
TOT, OWNTAX, NONTAX, GRANTS, CENTRAL, STATE = RR["2022-23"]
OTHER = GRANTS - CENTRAL - STATE
assert TOT == OWNTAX + NONTAX + GRANTS
SH = lambda v: v / TOT * 100
OWN_SH, NONTAX_SH, OWNREV_SH = SH(OWNTAX), SH(NONTAX), SH(OWNTAX + NONTAX)
CENTRAL_SH, STATE_SH = SH(CENTRAL), SH(STATE)
assert round(OWN_SH, 1) == 2.1 and round(CENTRAL_SH, 1) == 69.9

# RBI Table II.4 key ratios (computed by the RBI from per-panchayat averages), per cent
RATIO_OWNTAX = {"2020-21": 1.1, "2021-22": 1.1, "2022-23": 1.0}
RATIO_CENTRAL = {"2020-21": 77.5, "2021-22": 79.6, "2022-23": 79.8}
RATIO_STATE = {"2020-21": 17.8, "2021-22": 15.8, "2022-23": 15.4}
RR_GDP = {"2020-21": 0.21, "2021-22": 0.16, "2022-23": 0.13}
EXP_GDP = {"2020-21": 0.13, "2021-22": 0.10, "2022-23": 0.08}
# Per panchayat, Rs thousand (Table II.3, II.5)
PP_RR, PP_OWNTAX, PP_NONTAX, PP_EXP = 2123, 21, 73, 1250
PP_EXP_2021 = 1732
# Revenue expenditure 2022-23, Rs crore, and shares (Table II.5)
EXP_2223, EXP_PRP_SH, EXP_WSS_SH = 20712, 63, 27
CAPEX_SH = 29.6  # capital spending as % of total, 2022-23

# RBI Appendix I, Rs per village panchayat, 2022-23 (blank = "data not available" in eGramSwaraj)
APPX = {  # state: (total receipts, own tax, own non-tax)
    "Tamil Nadu": (3321014, 127783, None),
    "Maharashtra": (2041112, 191968, 339856),
    "Telangana": (1152065, 72257, None),
    "Odisha": (3376376, 25, 118937),
}
MH_OWN_SH = (APPX["Maharashtra"][1] + APPX["Maharashtra"][2]) / APPX["Maharashtra"][0] * 100
assert round(MH_OWN_SH) == 26

# Per-capita State Finance Commission grants, Rs a year, 2015-19 average (RBI Table II.2.1)
SFC_PC = {"Karnataka": 6090.0, "Kerala": 2999.7, "Tamil Nadu": 1426.2, "Uttar Pradesh": 449.5,
          "Bihar": 356.7, "Odisha": 146.7}

# Devolution Index 2024 (MoPR / IIPA, Feb 2025; data to 2021-22), general-category states
DI = {"Karnataka": (72.23, 1), "Kerala": (70.59, 2), "Tamil Nadu": (68.38, 3), "Maharashtra": (61.44, 4),
      "Uttar Pradesh": (60.07, 5), "Gujarat": (58.26, 6), "West Bengal": (56.52, 8), "Telangana": (55.10, 10),
      "Madhya Pradesh": (50.94, 12), "Odisha": (50.03, 13)}
DI_NAT, DI_FUNCTIONS_NAT, DI_FINANCES_NAT = 43.89, 29.18, 37.04

# 15th Finance Commission grants to rural local bodies, Rs crore: allocation and release (PIB, 17 March 2026)
FC15_2526 = {"Karnataka": (2572, 0.00), "Tamil Nadu": (2884, 637.93), "Maharashtra": (4659, 2507.25),
             "Uttar Pradesh": (7797, 5441.38), "Gujarat": (2555, 1782.04), "West Bengal": (3528, 3403.92),
             "Telangana": (1477, 0.00), "Madhya Pradesh": (3185, 630.65), "Odisha": (1805, 1712.98)}
FC15_ALLOC_ALL, FC15_REL_ALL = 297555, 267250.78
FC15_ALLOC_2526, FC15_REL_2526 = 48573, 26656.33
FC15_2126 = 236805
REL_ALL_SH = FC15_REL_ALL / FC15_ALLOC_ALL * 100
REL_2526_SH = FC15_REL_2526 / FC15_ALLOC_2526 * 100
assert round(REL_ALL_SH, 1) == 89.8 and round(REL_2526_SH, 1) == 54.9

# 16th Finance Commission, 2026-31 (Lok Sabha answer, 4 August 2026)
FC16, FC16_BASIC, FC16_PERF = 435236, 348188, 87048
FC16_LB_PERF = 43524      # local body performance grant, tied to own-source revenue
FC16_YR = FC16 / 5
FC15_YR = FC15_2126 / 5
FC16_RISE = (FC16_YR / FC15_YR - 1) * 100
LB_PERF_YR = FC16_LB_PERF / 5
LB_PERF_X = LB_PERF_YR / OWNTAX
assert round(FC16_RISE) == 84 and round(LB_PERF_X) == 12


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def chart_mix():
    items = [("Central grants", CENTRAL), ("State grants", STATE), ("Own non-tax", NONTAX),
             ("Own tax", OWNTAX), ("Other grants", OTHER)]
    W, L, R, top, bh, gap = 340, 92, 334, 44, 26, 12
    H = top + len(items) * (bh + gap) + 24
    sc = (R - L) / CENTRAL
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Where village panchayats&rsquo; revenue came from in 2022-23: central grants Rs {CENTRAL:,} crore, state grants Rs {STATE:,} crore, own non-tax revenue Rs {NONTAX:,} crore, own tax Rs {OWNTAX:,} crore.">',
         f'<text x="4" y="13" font-size="13" fill="#495057">Village panchayats&rsquo; revenue, 2022-23, Rs crore</text>',
         f'<text x="4" y="30" font-size="11" fill="#6c757d">Total Rs {TOT:,} crore; dark bars: raised by panchayats</text>']
    for i, (lab, v) in enumerate(items):
        y = top + i * (bh + gap)
        w = max(v * sc, 2)
        own = lab.startswith("Own")
        fill = "#0b3d6b" if own else "#7ea7cf"
        s.append(f'<text x="{L - 6}" y="{y + bh / 2 + 4:.1f}" font-size="12" fill="#212529" text-anchor="end">{lab}</text>')
        s.append(f'<rect x="{L}" y="{y}" width="{w:.1f}" height="{bh}" fill="{fill}"/>')
        lbl = f"{v:,} ({SH(v):.1f}%)"
        if w > 150:
            s.append(f'<text x="{L + w - 6:.1f}" y="{y + bh / 2 + 4:.1f}" font-size="12" fill="#fff" text-anchor="end">{lbl}</text>')
        else:
            s.append(f'<text x="{L + w + 5:.1f}" y="{y + bh / 2 + 4:.1f}" font-size="12" fill="#212529">{lbl}</text>')
    s.append(f'<text x="4" y="{H - 6}" font-size="10.5" fill="#6c757d">Source: RBI (2024), Table II.3</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def fmt_rs(v):
    if v is None:
        return "n.r."
    s = f"{v:,}"
    # Indian grouping for six-digit and larger values
    if v >= 100000:
        a, b = divmod(v, 1000)
        s = f"{a // 100},{a % 100:02d},{b:03d}" if a >= 100 else f"{a},{b:03d}"
    return s


def t_states():
    order = ["Karnataka", "Tamil Nadu", "Maharashtra", "Uttar Pradesh", "Gujarat", "West Bengal",
             "Telangana", "Madhya Pradesh", "Odisha"]
    rows = []
    for st in order:
        sc, rk = DI[st]
        own = APPX.get(st, (None, None, None))[1]
        al, rel = FC15_2526[st]
        rows.append((f"{st} ({rk})", fmt_rs(own), f"{rel / al * 100:.0f}"))
    return table(["State (index rank)", "Own tax, Rs", "FC paid, %"], rows)


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{OWN_SH:.1f}%</b><span>of village panchayats&rsquo; Rs {TOT:,} crore revenue in 2022-23 came from their own taxes; the RBI&rsquo;s per-panchayat ratio puts it at {RATIO_OWNTAX["2022-23"]}%</span></div>
<div class="gb-stat"><b>{RR_GDP["2020-21"]}% &rarr; {RR_GDP["2022-23"]}%</b><span>panchayat revenue as a share of GDP, 2020-21 to 2022-23</span></div>
<div class="gb-stat"><b>{DI_NAT}</b><span>national average on the 2024 Devolution Index (out of 100); functions, the weakest of six dimensions, average {DI_FUNCTIONS_NAT}</span></div>
<div class="gb-stat"><b>Rs {FC16 / 1e5:.2f} lakh cr</b><span>16th Finance Commission grants to rural local bodies for 2026-31, about {FC16_RISE:.0f}% a year more than the 15th</span></div>
</div>'''

body = f"""
{stats}

<p>The 73rd Amendment, in force since April 1993, made village, block and district panchayats a constitutional tier of government. It gave them elections, reserved seats and a list of 29 subjects in the Eleventh Schedule that states could hand over. It did not give them money of their own. That was left to state laws, to State Finance Commissions and to whatever the Union Finance Commission chose to send. Thirty-three years later, two documents show how that has worked out: the Reserve Bank of India&rsquo;s study of panchayat finances, published in January 2024, and the report of Parliament&rsquo;s Standing Committee on Rural Development and Panchayati Raj, presented on 5 August 2026.</p>

<p>The short answer: India&rsquo;s roughly 2.5 lakh village panchayats raise about two rupees in every hundred they receive from taxes of their own, and about six rupees counting fees and interest. The rest comes from the Centre and the states. A much larger Finance Commission award for 2026-31 now rewards panchayats that raise more. It is still too early to tell whether that changes the habit.</p>

<h2 class="gb-h2">Ninety-four rupees in every hundred are grants</h2>

<p>The RBI study uses accounts that panchayats file on eGramSwaraj, the Ministry of Panchayati Raj&rsquo;s accounting portal, for 2020-21 to 2022-23. In 2022-23 the 2.41 lakh village panchayats that reported receipts took in Rs {TOT:,} crore. Rs {OWNTAX:,} crore of that, {OWN_SH:.1f}%, was their own tax revenue, mostly property tax on houses and buildings. Another Rs {NONTAX:,} crore ({NONTAX_SH:.1f}%) was non-tax income such as interest, fees and market dues. Central grants were Rs {CENTRAL:,} crore ({CENTRAL_SH:.1f}%) and state grants Rs {STATE:,} crore ({STATE_SH:.1f}%).</p>

{chart_mix()}

<p>The RBI&rsquo;s own ratio table, which it computes from per-panchayat averages rather than totals, gives an even lower figure: own taxes {RATIO_OWNTAX["2022-23"]}% of revenue, central grants {RATIO_CENTRAL["2022-23"]}% and state grants {RATIO_STATE["2022-23"]}%. On that basis the average panchayat collected about Rs {PP_OWNTAX * 1000:,} in taxes in 2022-23 out of Rs {PP_RR / 100:.1f} lakh of revenue. Either way, the figure is one or two rupees in a hundred.</p>

<p>The totals were also shrinking. Panchayat revenue fell from {RR_GDP["2020-21"]}% of GDP in 2020-21 to {RR_GDP["2022-23"]}% in 2022-23, and spending from {EXP_GDP["2020-21"]}% to {EXP_GDP["2022-23"]}%. Average spending per panchayat fell from Rs {PP_EXP_2021 / 100:.1f} lakh to Rs {PP_EXP / 100:.1f} lakh; the RBI attributes part of the fall to unusually high spending in the pandemic year. Of the Rs {EXP_2223:,} crore spent in 2022-23, {EXP_PRP_SH}% went on general Panchayati Raj programmes and {EXP_WSS_SH}% on water supply and sanitation, which the Finance Commission&rsquo;s tied grants pay for. Parliament&rsquo;s standing committee has warned that funding to panchayats has been eroded across successive Union Budgets.</p>

<h2 class="gb-h2">The states that devolve most report no own taxes</h2>

<p>How much a panchayat can do depends on its state. The Ministry&rsquo;s Devolution Index for 2024, prepared by the Indian Institute of Public Administration (IIPA) from data up to 2021-22, scores states on six dimensions: framework, functions, finances, functionaries (staff), capacity building and accountability. The national average rose from 39.9 to {DI_NAT} out of 100 between 2013-14 and 2021-22. The weakest dimension is functions, the actual transfer of the 29 subjects, where the national average is {DI_FUNCTIONS_NAT}. For finances it is {DI_FINANCES_NAT}. Karnataka leads at {DI["Karnataka"][0]}, followed by Kerala ({DI["Kerala"][0]}) and Tamil Nadu ({DI["Tamil Nadu"][0]}). Punjab, 17th among the general-category states, scores under 30.</p>

{t_states()}
<p class="gb-note">Index rank: position among general-category states on the Devolution Index 2024 (MoPR/IIPA); scores run from 72.2 for Karnataka to 50.0 for Odisha in this list. Own tax: rupees per village panchayat in 2022-23, from the RBI study&rsquo;s state appendix; n.r. means eGramSwaraj had no data, not that panchayats collected nothing. FC paid: share of the state&rsquo;s 2025-26 Finance Commission grant released by 17 March 2026 (PIB).</p>

<p>The table shows a data problem as much as a finance problem. Karnataka, the top-ranked state, and Kerala, second, show no own tax revenue at all in the RBI&rsquo;s appendix. Neither do Uttar Pradesh, Gujarat, West Bengal or Madhya Pradesh. Kerala&rsquo;s panchayats do levy property tax, so the gap almost certainly reflects what reaches eGramSwaraj rather than what is collected. Where the figures are reported, they vary widely. In Maharashtra, own taxes and non-tax income together were {MH_OWN_SH:.0f}% of the average panchayat&rsquo;s revenue; in Tamil Nadu own taxes were {APPX["Tamil Nadu"][1] / APPX["Tamil Nadu"][0] * 100:.1f}%; in Odisha they were Rs {APPX["Odisha"][1]} per panchayat for the whole year.</p>

<p>State Finance Commissions, which the Constitution requires every five years to decide what share of state revenue goes to local bodies, explain much of the rest. Per-capita grants on their recommendations averaged Rs {SFC_PC["Karnataka"]:,.0f} a year in Karnataka and Rs {SFC_PC["Kerala"]:,.0f} in Kerala over 2015-19, against Rs {SFC_PC["Uttar Pradesh"]:,.0f} in Uttar Pradesh, Rs {SFC_PC["Bihar"]:,.0f} in Bihar and Rs {SFC_PC["Odisha"]:,.0f} in Odisha, where they fell by 30%. Ministry data cited in the committee&rsquo;s work, as reported by The Tribune, showed only 25 states had constituted State Finance Commissions and only nine had reached the sixth one; some had not constituted the third, fourth or fifth.</p>

<h2 class="gb-h2">The Finance Commission money arrives late, and is about to double</h2>

<p>The 15th Finance Commission recommended Rs {FC15_2126:,} crore for rural local bodies for 2021-26, plus Rs 60,750 crore for 2020-21. By 17 March 2026, Rs {FC15_REL_ALL:,.0f} crore of the Rs {FC15_ALLOC_ALL:,} crore had been released, {REL_ALL_SH:.0f}%. In the final year, 2025-26, only Rs {FC15_REL_2526:,.0f} crore of Rs {FC15_ALLOC_2526:,} crore ({REL_2526_SH:.0f}%) had gone out two weeks before the year ended. Grants are released in instalments only after a state certifies it passed the previous one on to panchayats within 10 working days and meets conditions on audited accounts and its State Finance Commission. Karnataka and Telangana had received nothing for 2025-26 by mid-March; Arunachal Pradesh had received nothing since 2022-23. A later report put the release rate for the whole award at about 95%, which this piece could not reconcile with the March table.</p>

<p>The 16th Finance Commission, covering 2026-31, has recommended Rs {FC16:,} crore for rural local bodies, about {FC16_RISE:.0f}% a year more than its predecessor. Rs {FC16_BASIC:,} crore (80%) is a basic grant, half of it tied to sanitation and water. The remaining Rs {FC16_PERF:,} crore is for performance. Half of that, Rs {FC16_LB_PERF:,} crore, is a local body performance grant released according to how much own-source revenue panchayats raise and increase; the other half rewards states for passing on their own funds.</p>

<p>The performance grant is large next to the base it is meant to grow. Spread over five years it is about Rs {LB_PERF_YR:,.0f} crore a year, roughly {LB_PERF_X:.0f} times the Rs {OWNTAX:,} crore of own taxes that reporting panchayats collected in 2022-23. That is a strong incentive, and also a reason to watch how own revenue is measured: a grant tied to reported collections rewards reporting as much as collecting, and the RBI data show how incomplete reporting still is.</p>

<h2 class="gb-h2">What Parliament&rsquo;s committee found</h2>

<p>The committee&rsquo;s 35th report, on the effectiveness of the 73rd Amendment and coordination across the three tiers, makes 17 recommendations. It found that elections and representation have largely worked: women hold nearly half of elected panchayat seats, and 21 states and two union territories reserve 50% for them, though it called proxy representation by male relatives widespread. On functions, funds and functionaries it found devolution uneven, with panchayats often acting as implementing agencies for state departments rather than as governments. One panchayat secretary often serves four or five panchayats; the committee wants a dedicated cadre and, in phases, one secretary per gram panchayat. It found block and district panchayats weak, asked states to follow the 80:10:10 sharing of grants between village, block and district tiers, and noted that the generation of audit reports declined in 2024-25. On money, it asked for a strategy to raise own-source revenue, timely State Finance Commissions and performance incentives.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Ministry of Panchayati Raj should publish own-source revenue by state every year from eGramSwaraj, and mark each state&rsquo;s reporting coverage, so that a state showing no own tax is visibly a reporting gap and not mistaken for a panchayat that collects nothing. States that keep accounts in their own systems should push the totals to eGramSwaraj before any performance grant is calculated.</li>
<li>States should set a minimum property-tax rate for rural buildings, revised with inflation, as the 15th Finance Commission required of states for urban property tax. Panchayats would keep the right to charge more.</li>
<li>The Ministry should publish, each quarter, the date each state received and passed on every Finance Commission instalment, so delays like the 2025-26 shortfall can be traced to a state or to the Centre.</li>
<li>A state that has not constituted its State Finance Commission on time, or tabled the action-taken report, should see its share of the 16th Finance Commission&rsquo;s state performance grant reduced, as the 15th Commission already did for basic grants.</li>
<li>The cost of one secretary per gram panchayat should be costed and phased into the state performance grant, since staff, not schemes, is where most panchayats are thinnest.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The RBI study is the only national series on panchayat finances, and it ends in 2022-23; no later year was found. Its two measures of the own-tax share differ, {OWN_SH:.1f}% from totals and {RATIO_OWNTAX["2022-23"]}% from per-panchayat averages, because coverage varies by state. The state appendix also does not always add up: the all-states table lists component grants larger than total grants, so this piece uses the RBI&rsquo;s summary tables for national figures. Several large states report no own tax revenue in eGramSwaraj, and how much Karnataka&rsquo;s and Kerala&rsquo;s panchayats actually collect was not found. The Devolution Index uses data to 2021-22. The count of State Finance Commissions comes from a newspaper report of committee material, and its date could not be pinned down. The 15th Finance Commission release figures are as of 17 March 2026, and the later 95% figure appears only in a study-guide summary. The exact formula linking the 16th Commission&rsquo;s local body performance grant to own-source revenue was not found. The committee&rsquo;s full report was read only through the PRS summary and press coverage. How many panchayats are currently run by administrators because elections are overdue was not established.</p>
"""

sources = ("Panchayat revenue and spending: Reserve Bank of India, Finances of Panchayati Raj Institutions (24 January 2024), Tables II.3&ndash;II.5, Table II.2.1 and Appendix I, based on eGramSwaraj data compiled by the Ministry of Panchayati Raj; read through the RBI publication pages and search-engine text. "
           "Devolution Index: Ministry of Panchayati Raj and Indian Institute of Public Administration, Status of Devolution to Panchayats in States &ndash; An Indicative Evidence-Based Ranking, 2024 (February 2025); Lok Sabha unstarred questions 445 (21 July 2026) and 2615 (4 August 2026); Rajya Sabha unstarred question 3120 (20 August 2025). "
           "Finance Commission grants: PIB, Recommendation of 15th Finance Commission (17 March 2026), state-wise allocation and release table; Lok Sabha question 2615 (4 August 2026) and Policy Edge (7 August 2026) for the 16th Finance Commission&rsquo;s Rs 4,35,236 crore, its 80:20 split and the two performance grants; Superkalam (April 2026) for the later 95% release figure, unverified. "
           "Committee: Standing Committee on Rural Development and Panchayati Raj (chair Saptagiri Sankar Ulaka), 35th report, presented 5 August 2026, via the PRS Legislative Research report summary and Policy Edge; State Finance Commission counts from The Tribune. "
           "Shares, per-year averages and the performance-grant multiple are this blog&rsquo;s arithmetic (builder at out/research/panchayat-finances/).")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/indias-79-lakh-crore-rural-water.html", "India&rsquo;s &#8377;7.9 Lakh Crore Rural Water Pipeline: What &lsquo;Upcoming&rsquo; Actually Means, State by State"),
    ("https://masaladeutsch.blogspot.com/2026/08/west-bengal-sanctioned-126-lakh-pmay-g.html", "West Bengal Sanctioned 12.6 Lakh PMAY-G Houses. It Has Finished 1.5 Lakh. The Reason Is a Four-Year Funds Freeze."),
    ("https://masaladeutsch.blogspot.com/2026/08/who-collects-indias-gst-and-who.html", "Who Collects India&rsquo;s GST, and Who Actually Gets It Back"),
    ("https://masaladeutsch.blogspot.com/2026/08/amruts-197-lakh-crore-urban-portfolio.html", "AMRUT&rsquo;s &#8377;1.97 Lakh Crore Urban Portfolio: Water Supply Is 41% of Projects, 60% of the Money"),
    ("https://masaladeutsch.blogspot.com/2026/08/a-17-rural-pay-rise-that-nobody-received.html", "A 17% Rural Pay Rise That Nobody Received"),
]

build("Governance &middot; 7 November 2026",
      "Panchayats Raise Barely Two Rupees in Tax for Every Hundred They Receive, 33 Years After the 73rd Amendment",
      "Village panchayats took in Rs 35,354 crore in 2022-23; 2.1% came from their own taxes and 94% from grants. The states that devolve most report no own taxes at all, and a Finance Commission award that has nearly doubled now pays panchayats to raise more.",
      body, sources, related, OUT)
print("own tax", round(OWN_SH, 2), "own rev", round(OWNREV_SH, 1), "central", round(CENTRAL_SH, 1), "state", round(STATE_SH, 1),
      "MH own", round(MH_OWN_SH, 1), "rel all", round(REL_ALL_SH, 1), "rel 2526", round(REL_2526_SH, 1),
      "16FC rise", round(FC16_RISE, 1), "LB perf x", round(LB_PERF_X, 1))
