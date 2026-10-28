import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-gas-share.html'

# ---------------------------------------------------------------- data
# MoSPI Energy Statistics, energy balance, total primary energy supply (PJ), via MoSPI API
TPES = {"2014-15": 26908.15, "2015-16": 28202.99, "2016-17": 28656.80, "2017-18": 30073.30, "2018-19": 31882.45,
        "2019-20": 31908.15, "2020-21": 29728.89, "2021-22": 32586.16, "2022-23": 35075.37, "2023-24": 37813.41}
GAS = {"2014-15": 2012.82, "2015-16": 2065.72, "2016-17": 2185.42, "2017-18": 2314.15, "2018-19": 2372.91,
       "2019-20": 2506.05, "2020-21": 2389.64, "2021-22": 2519.29, "2022-23": 2352.88, "2023-24": 2642.50}
SHARE = {y: GAS[y] / TPES[y] * 100 for y in TPES}
# Gas volumes, bcm (PPAC): FY24 68.76 (Gas Outlook citing PPAC); FY16 and FY26 from PPAC NG-H workbook (this blog's CGD post)
BCM = {"2015-16": 47.849, "2023-24": 68.76, "2025-26": 69.048}
FY26_FALL = 3.0                 # % fall in FY2025-26 consumption, PPAC
BCM["2024-25"] = BCM["2025-26"] / (1 - FY26_FALL / 100)
PJ_PER_BCM = GAS["2023-24"] / BCM["2023-24"]        # calibration on 2023-24
PJ_PER_BCM_16 = GAS["2015-16"] / BCM["2015-16"]     # same on 2015-16, to show the drift
G = (TPES["2023-24"] / TPES["2019-20"]) ** (1 / 4) - 1      # TPES growth, 2019-20 to 2023-24
G_LOW = (TPES["2023-24"] / TPES["2014-15"]) ** (1 / 9) - 1  # ten-year growth
def tpes(year_offset, g=G): return TPES["2023-24"] * (1 + g) ** year_offset
TPES26, TPES30, TPES30_LOW = tpes(2), tpes(6), tpes(6, G_LOW)
SHARE26 = BCM["2025-26"] * PJ_PER_BCM / TPES26 * 100
TARGET = 15
NEED_BCM = TARGET / 100 * TPES30 / PJ_PER_BCM
NEED_BCM_LOW = TARGET / 100 * TPES30_LOW / PJ_PER_BCM
MMSCMD = lambda bcm: bcm * 1000 / 365
NEED_GROWTH = (NEED_BCM / BCM["2025-26"]) ** (1 / 4) - 1
PAST_GROWTH = (BCM["2025-26"] / BCM["2015-16"]) ** (1 / 10) - 1
IMPORT_SHARE26 = 50.1          # % of consumption imported, Apr-Sep 2025 (PPAC via Moneycontrol)
DOM26 = BCM["2025-26"] * (1 - IMPORT_SHARE26 / 100)
DOM30 = 38.0                      # IEA: domestic output just under 38 bcm by 2030
BCM_PER_MT = 1.36                 # 1 Mt LNG ~ 1.36 bcm
LNG_NEED_BCM = NEED_BCM - DOM30
LNG_NEED_MT = LNG_NEED_BCM / BCM_PER_MT
REGAS_MT = 58.5                   # nameplate incl. Dahej 22.5 (this blog's LNG-capacity post)
LNG_2025_MT = 25.5                # calendar 2025 (Petronet CEO)
# Other 2030 views
PNGRB_LO, PNGRB_HI = 260, 300     # MMSCMD, PNGRB expert committee base case 2030
IEA_LNG30 = 64.0                  # bcm
def share30(bcm): return bcm * PJ_PER_BCM / TPES30 * 100
PNGRB_SH = (share30(PNGRB_LO * 365 / 1000), share30(PNGRB_HI * 365 / 1000))
IEA_BCM = DOM30 + IEA_LNG30
IEA_SH = share30(IEA_BCM)
# Gas power
POWER_BCM16, POWER_BCM26 = 10.889, 7.960   # PPAC, gas to power
PLF26, PLF18 = 10.52, 24.0                 # CEA gas stations 2025-26; 2017-18 per parliamentary committee
POWER_EXTRA = POWER_BCM26 * (PLF18 / PLF26 - 1)
POWER_PP = POWER_EXTRA * PJ_PER_BCM / TPES26 * 100
assert 6 < SHARE26 < 7 and 180 < NEED_BCM < 200


def chart_share():
    W, L, top, ch = 400, 30, 30, 140
    yrs = list(TPES)
    n = len(yrs) + 2
    bw = (W - L - 14) / n
    H = top + ch + 46
    base = top + ch
    sc = (ch - 10) / 16
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Natural gas share of India&rsquo;s primary energy supply, 2014-15 to 2023-24, from 7.5% to 7.0%, an estimate of about {SHARE26:.1f}% in 2025-26, and the 15% target for 2030.">',
         f'<text x="10" y="12" font-size="12" fill="#495057">Gas share of India&rsquo;s primary energy supply, %</text>']
    for v in (0, 5, 10, 15):
        y = base - v * sc
        s.append(f'<line x1="{L}" x2="{W - 8}" y1="{y:.1f}" y2="{y:.1f}" stroke="#dee2e6"/>')
        s.append(f'<text x="{L - 4}" y="{y + 3:.1f}" font-size="9" fill="#6c757d" text-anchor="end">{v}</text>')
    bars = [(y[2:], SHARE[y], "#1c5d99") for y in yrs] + [("25-26e", SHARE26, "#868e96"), ("2030 goal", TARGET, "#a5402c")]
    for i, (lab, v, col) in enumerate(bars):
        x = L + 6 + i * bw
        h = v * sc
        s.append(f'<rect x="{x:.1f}" y="{base - h:.1f}" width="{bw - 5:.1f}" height="{h:.1f}" fill="{col}"/>')
        s.append(f'<text x="{x + (bw - 5) / 2:.1f}" y="{base - h - 3:.1f}" font-size="8.5" fill="#212529" text-anchor="middle">{v:.1f}</text>')
        s.append(f'<text x="{x + (bw - 5) / 2:.1f}" y="{base + 11}" font-size="8" fill="#212529" text-anchor="middle">{lab}</text>')
    s.append(f'<text x="10" y="{H - 16}" font-size="9" fill="#6c757d">MoSPI energy balance (PJ), 2014-15 to 2023-24. 2025-26 is this blog&rsquo;s estimate</text>')
    s.append(f'<text x="10" y="{H - 4}" font-size="9" fill="#6c757d">from PPAC volumes. Fiscal years: 14-15 means 2014-15.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_2030():
    rows = [("Used in 2025-26", BCM["2025-26"], None),
            ("PNGRB committee, 2030 base (low)", PNGRB_LO * 365 / 1000, None),
            ("IEA, 2030", IEA_BCM, None),
            ("PNGRB committee, 2030 base (high)", PNGRB_HI * 365 / 1000, None),
            ("15% of primary energy, 2029-30", NEED_BCM, None)]
    W, L, top, bh, gap, lab = 400, 10, 34, 16, 9, 168
    H = top + len(rows) * (bh + gap) + 34
    sc = (W - L - lab - 46) / 200
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Gas needed in 2029-30 under different views, billion cubic metres: {BCM["2025-26"]:.0f} used in 2025-26; {PNGRB_LO * .365:.0f} to {PNGRB_HI * .365:.0f} in PNGRB&rsquo;s base case; {IEA_BCM:.0f} on the IEA&rsquo;s outlook; {NEED_BCM:.0f} for a 15% share.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Gas a year, billion cubic metres</text>',
         f'<rect x="{L}" y="18" width="9" height="9" fill="#1c5d99"/><text x="{L + 13}" y="26" font-size="9.5" fill="#212529">Domestic output (38 bcm cap)</text>',
         f'<rect x="{L + 170}" y="18" width="9" height="9" fill="#d9a441"/><text x="{L + 183}" y="26" font-size="9.5" fill="#212529">Imported LNG</text>']
    for i, (n, v, _) in enumerate(rows):
        y = top + i * (bh + gap)
        dom = min(v, DOM30) if i else DOM26
        s.append(f'<text x="{L + lab - 6}" y="{y + 12}" font-size="9.5" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{dom * sc:.1f}" height="{bh}" fill="#1c5d99"/>')
        s.append(f'<rect x="{L + lab + dom * sc:.1f}" y="{y}" width="{(v - dom) * sc:.1f}" height="{bh}" fill="#d9a441"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 12}" font-size="9.5" fill="#212529">{v:.0f}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">2025-26 split uses the April&ndash;September 2025 import share of 50.1%. Domestic output held at the</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">IEA&rsquo;s ~38 bcm for 2030 in every case. This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_need():
    return table(["What a 15% share in 2029-30 implies", "Value", "Basis"], [
        ("Primary energy supply, 2029-30", f"{TPES30:,.0f} PJ", f"2023-24 supply grown at {G * 100:.1f}% a year, the 2019-20 to 2023-24 rate"),
        ("Gas at 15%", f"{NEED_BCM:.0f} bcm ({MMSCMD(NEED_BCM):.0f} MMSCMD)", f"{PJ_PER_BCM:.1f} PJ per bcm, from 2023-24 MoSPI and PPAC data"),
        ("Against 2025-26 use", f"{NEED_BCM / BCM['2025-26']:.1f} times", f"Growth of {NEED_GROWTH * 100:.0f}% a year for four years"),
        ("LNG needed, if domestic output reaches 38 bcm", f"{LNG_NEED_BCM:.0f} bcm, about {LNG_NEED_MT:.0f} million tonnes", f"1 Mt of LNG &asymp; {BCM_PER_MT} bcm; India imported about {LNG_2025_MT} Mt in 2025"),
        ("Regasification capacity", f"{REGAS_MT} Mt a year", "All eight terminals, nameplate, including Dahej&rsquo;s expansion"),
        ("With slower energy growth", f"{NEED_BCM_LOW:.0f} bcm", f"Supply grown at the ten-year rate of {G_LOW * 100:.1f}% a year"),
    ])


def t_recs():
    return table(["Committee on Estimates finding or recommendation", "What the data in this piece shows"], [
        ("Gas is about 6% of India&rsquo;s energy mix, against about 24% worldwide; the target is 15% by 2030", f"The official energy balance puts it at {SHARE['2014-15']:.1f}% in 2014-15 and {SHARE['2023-24']:.1f}% in 2023-24; about {SHARE26:.1f}% in 2025-26 on this blog&rsquo;s estimate"),
        ("Only two deep-water blocks produce, giving about 31% of domestic output, though 39% of the sedimentary area is in deep water", "Domestic output has been flat at about 36 bcm; the IEA expects under 38 bcm by 2030"),
        ("A flexible gas allocation framework to use idle gas power plants", f"Gas to power fell from {POWER_BCM16:.1f} to {POWER_BCM26:.1f} bcm in a decade; the fleet ran at about {PLF26:.1f}% in 2025-26"),
        ("A Natural Gas Action Plan with yearly targets", "No year-by-year path to 15% has been published"),
        ("More balanced development of LNG terminals; 1,000 LNG fuel stations", "Dahej runs near full while the other seven terminals mostly run at a fifth to a half"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{SHARE['2023-24']:.1f}%</b><span>gas share of primary energy in 2023-24, down from {SHARE['2014-15']:.1f}% in 2014-15 (MoSPI)</span></div>
<div class="gb-stat"><b>{NEED_BCM:.0f} bcm</b><span>of gas a 15% share would need in 2029-30, {NEED_BCM / BCM['2025-26']:.1f} times what India used in 2025-26</span></div>
<div class="gb-stat"><b>~{LNG_NEED_MT:.0f} Mt</b><span>of LNG a year that would take, against about {LNG_2025_MT} Mt imported in 2025 and {REGAS_MT} Mt of terminal capacity</span></div>
<div class="gb-stat"><b>{PLF26:.1f}%</b><span>average load of India&rsquo;s gas power plants in 2025-26 (CEA)</span></div>
</div>'''

body = f"""
{stats}

<p>Parliament&rsquo;s Committee on Estimates reported on 7 August on the supply and distribution of natural gas. Its starting point is the government&rsquo;s target of raising gas to 15% of India&rsquo;s energy mix by 2030, from about 6% today against a world average near 24%. It recommends a yearly action plan, more help for deep-water and frontier exploration, a flexible way of allocating gas to idle power plants, and more balanced development of import terminals.</p>
<p>This piece checks the target against the official numbers. The Ministry of Statistics&rsquo; energy balance shows gas losing share, not gaining it, over the last decade. A 15% share by 2029-30 would need almost three times the gas India now uses, most of it imported, at a time when the 2026 Hormuz disruption has shown what depending on imported LNG costs.</p>

<h2 class="gb-h2">The share has been falling</h2>
{chart_share()}
<p>India&rsquo;s gas use grew {(GAS['2023-24'] / GAS['2014-15'] - 1) * 100:.0f}% in energy terms between 2014-15 and 2023-24, but its total primary energy supply grew {(TPES['2023-24'] / TPES['2014-15'] - 1) * 100:.0f}%, mostly from coal and oil. So gas&rsquo;s share slipped from {SHARE['2014-15']:.1f}% to {SHARE['2023-24']:.1f}%. Consumption then fell {FY26_FALL:.0f}% in 2025-26 to about {BCM['2025-26']:.0f} billion cubic metres (bcm), according to PPAC, which puts the share near {SHARE26:.1f}% on this blog&rsquo;s estimate. The committee&rsquo;s &ldquo;about 6%&rdquo; is consistent with that.</p>
<p>The decline is not spread evenly. City gas for vehicles and kitchens has tripled in a decade and is now the largest user, as this blog has <a href="https://masaladeutsch.blogspot.com/2026/08/city-gas-just-became-indias-largest-gas.html">reported</a>. Gas to power plants fell from {POWER_BCM16:.1f} to {POWER_BCM26:.1f} bcm over the same decade.</p>

<h2 class="gb-h2">What 15% would take</h2>
{t_need()}
<p>On recent growth in India&rsquo;s total energy use, primary energy supply would reach about {TPES30:,.0f} petajoules in 2029-30. Fifteen per cent of that is about {NEED_BCM:.0f} bcm of gas a year, or {MMSCMD(NEED_BCM):.0f} million standard cubic metres a day (MMSCMD). India used about {MMSCMD(BCM['2025-26']):.0f} MMSCMD in 2025-26. Reaching the target would need consumption to grow about {NEED_GROWTH * 100:.0f}% a year for four years, after a decade in which it grew about {PAST_GROWTH * 100:.1f}% a year.</p>
<p>Almost all of the increase would have to be imported. The IEA expects domestic output to stay just under 38 bcm by 2030, so the rest, about {LNG_NEED_BCM:.0f} bcm, would come as LNG: roughly {LNG_NEED_MT:.0f} million tonnes a year, more than four times the {LNG_2025_MT} million tonnes India bought in 2025 and nearly twice its {REGAS_MT} million tonnes of terminal capacity.</p>
{chart_2030()}
<p>The government&rsquo;s own forecasters do not expect anything close. PNGRB&rsquo;s expert committee, in a report this blog <a href="https://masaladeutsch.blogspot.com/2026/09/pngrbs-own-2025-committee-now-expects.html">reviewed in September</a>, put 2030 demand at {PNGRB_LO}&ndash;{PNGRB_HI} MMSCMD in its base case. On this piece&rsquo;s energy projection that is a share of about {PNGRB_SH[0]:.1f}&ndash;{PNGRB_SH[1]:.1f}%. The IEA&rsquo;s outlook, with LNG imports rising to {IEA_LNG30:.0f} bcm, gives about {IEA_SH:.0f}%. Both are roughly half of the target. An earlier industry vision, which this blog <a href="https://masaladeutsch.blogspot.com/2026/09/a-2013-vision-saw-india-needing-746.html">set against the outcome</a>, expected 746 MMSCMD and a 20% share by 2030.</p>

<h2 class="gb-h2">Idle gas power plants are a small lever</h2>
<p>India has about 25 GW of gas-fired power capacity, according to Petronet LNG&rsquo;s chief executive, much of it idle because imported gas is too expensive to burn for power. The Central Electricity Authority&rsquo;s gas-station reports put the fleet&rsquo;s average load at {PLF26:.1f}% in 2025-26, against a target of 14.8% and about 24% in 2017-18. The committee&rsquo;s flexible allocation framework is meant to put more gas through these plants.</p>
<p>Even a large recovery would move the national share only a little. Taking the fleet back to its 2017-18 load would need roughly {POWER_EXTRA:.0f} bcm more gas a year, on this blog&rsquo;s scaling of PPAC&rsquo;s figure for gas burned in power. That would add about {POWER_PP:.1f} percentage points to gas&rsquo;s share of primary energy. Industry estimates put the LNG price at which these plants run at meaningful loads at about $6&ndash;7 per million British thermal units, and at $9&ndash;10 for evening peaks only. The Asian spot benchmark was assessed at about $10.9 in early February 2026, before the Hormuz disruption cut global LNG supply by about a fifth.</p>

<h2 class="gb-h2">What 2026 showed about relying on LNG</h2>
<p>About 60% of India&rsquo;s LNG used to come through the Strait of Hormuz, mostly from Qatar and the UAE. After loaded Qatari tankers stopped transiting the strait in late February 2026, India&rsquo;s LNG imports fell about 13% in March and April, and Petronet issued a force majeure notice to QatarEnergy. Buyers then shifted to cargoes from the United States, Oman, Nigeria and Angola: imports in May to July rose 15.4% from a year earlier to 7.08 million tonnes, even as supplies from Qatar fell 91%. Gas was rationed by priority, with city gas, fertilisers, power and ceramics first in line.</p>
<p>Demand had already been weakening before the disruption. Consumption in April to October 2025 fell 8.6% from a year earlier, which an Observer Research Foundation analysis attributes to price shocks, supply problems and falling domestic output. Imports recovered in 2026-27, up 4.4% in April to September, but they now meet 52.3% of consumption, up from 50.1%. Every step toward 15% would raise that share further.</p>

<h2 class="gb-h2">Terminals are not the bottleneck</h2>
<p>India&rsquo;s eight LNG terminals worked at about 47% of capacity in 2025, down from 58% in 2024, according to the International Gas Union. This blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/10/indias-cheapest-lng-capacity-is-extra.html">comparison of terminal expansion and new-build</a> found that expanding Dahej cost about Rs 370 crore per million tonnes of yearly capacity, against Rs 950&ndash;1,290 crore for new onshore terminals, and that Dahej ran at about 92% while the other terminals ran at 10&ndash;40% in April&ndash;May 2026. The constraint is the pipeline capacity to move gas inland from the terminals and the price of the gas, not the tanks. That points the same way as the committee&rsquo;s call for more balanced terminal development: fewer new terminals, more pipeline out of the ones that exist.</p>

<h2 class="gb-h2">Where the committee&rsquo;s findings stand</h2>
{t_recs()}

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Ministry of Petroleum and Natural Gas should restate the 15% target with a published path: consumption, domestic output and LNG imports for each year to 2030, on the same basis as MoSPI&rsquo;s energy balance, as the committee&rsquo;s yearly action plan implies.</li>
<li>Gas policy should be judged against PNGRB&rsquo;s own 2030 demand range, which implies about {PNGRB_SH[0]:.0f}&ndash;{PNGRB_SH[1]:.0f}% of primary energy, rather than a 15% figure no forecaster expects.</li>
<li>The flexible allocation for gas power should be tied to peak hours, where higher prices can be paid, and its effect reported as gas burned and hours run each month.</li>
<li>Pipeline capacity out of the under-used terminals should take priority over approving new ones.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The committee&rsquo;s report was read through PRS Legislative Research&rsquo;s summary, not the report itself. The energy shares use MoSPI&rsquo;s energy balance, which ends in 2023-24; the 2025-26 share is an estimate that converts PPAC&rsquo;s volume into energy using the 2023-24 ratio of {PJ_PER_BCM:.1f} PJ per bcm. The same ratio for 2015-16 is {PJ_PER_BCM_16:.1f}, so the two sources do not convert consistently, and the estimate could be off by several tenths of a point. Primary energy growth to 2029-30 is assumed, not forecast. The 2024-25 consumption figure is derived from PPAC&rsquo;s reported fall in 2025-26. Gas-power capacity is 25 GW in industry statements but about 20 GW in the CEA&rsquo;s monitored-station reports, and the extra gas needed to raise the fleet&rsquo;s load is scaled from PPAC&rsquo;s power-sector consumption rather than modelled plant by plant. Full-year LNG import figures for 2025-26 were not found.</p>
"""

sources = ("Committee on Estimates, &ldquo;Supply and Distribution of Natural Gas &ndash; Challenges and Prospects&rdquo;, presented 7 August 2026, via PRS Legislative Research&rsquo;s summary (1 September 2026) and its 2026-27 petroleum Demand for Grants analysis. "
           "Primary energy supply and gas supply in petajoules, 2014-15 to 2023-24: MoSPI Energy Statistics, energy balance (MoSPI API). Gas volumes: PPAC Natural Gas Historical Sectoral Consumption workbook (FY2015-16 and FY2025-26, as used in this blog&rsquo;s city-gas post); FY2023-24 consumption 68.76 bcm per Gas Outlook citing PPAC; April&ndash;October 2025 consumption per Observer Research Foundation&rsquo;s Energy News Monitor; April&ndash;September 2026 LNG imports per Moneycontrol citing PPAC. "
           "2030 views: PNGRB High-Level Expert Committee &ldquo;Vision 2040&rdquo; (2025); IEA via Argus. LNG imports and the Hormuz disruption: The Indian Express via Business Today and Vision IAS (August 2026); Petronet LNG chief executive via S&amp;P Global (India Energy Week 2026 and Gastech 2026); IGX chief executive on price thresholds via S&amp;P Global. "
           "Terminal capacity and utilisation: International Gas Union World LNG Report 2026 via Swarajya; this blog&rsquo;s LNG-capacity post (PPAC Ready Reckoner). Gas power: CEA monthly gas-station generation reports (2025-26); 2017-18 load per a parliamentary committee via Down To Earth. "
           "Shares, conversions and the 15% arithmetic are this blog&rsquo;s (builder in the repository at out/research/gas-share/). Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/09/pngrbs-own-2025-committee-now-expects.html", "PNGRB&rsquo;s Own 2025 Committee Now Expects Less Gas Demand by 2040 Than a 2013 Report Predicted for 2030"),
    ("https://masaladeutsch.blogspot.com/2026/09/a-2013-vision-saw-india-needing-746.html", "A 2013 Vision Saw India Needing 746 MMSCMD of Gas by 2030. Actual Demand Is About a Quarter of That"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-cheapest-lng-capacity-is-extra.html", "India&rsquo;s Cheapest LNG Capacity Is an Extra Tank at Dahej. Its Newer Terminals Run a Quarter Full"),
    ("https://masaladeutsch.blogspot.com/2026/08/city-gas-just-became-indias-largest-gas.html", "City Gas Just Became India&rsquo;s Largest Gas Consumer"),
    ("https://masaladeutsch.blogspot.com/2026/10/india-has-27400-km-of-gas-pipeline.html", "India Has 28,000 km of Gas Pipeline Working and 7,000 km Still to Build"),
    ("https://masaladeutsch.blogspot.com/2026/09/global-lng-trade-hit-record-437-million.html", "Global LNG Trade Hit a Record 437 Million Tonnes in 2025"),
]

build("Gas &amp; LNG · 28 October 2026",
      "India Wants 15% of Its Energy From Gas by 2030. The Official Energy Balance Shows Gas&rsquo;s Share Falling",
      "A parliamentary committee has restated the 15% target. Gas&rsquo;s share of primary energy slipped from 7.5% to 7.0% over the decade to 2023-24, and reaching 15% would take almost three times today&rsquo;s gas, nearly all of it imported LNG.",
      body, sources, related, OUT)
print(f"share26 {SHARE26:.2f} pj/bcm {PJ_PER_BCM:.2f} vs16 {PJ_PER_BCM_16:.2f} G {G*100:.2f} Glow {G_LOW*100:.2f} TPES30 {TPES30:.0f} need {NEED_BCM:.1f} ({MMSCMD(NEED_BCM):.0f} mmscmd) low {NEED_BCM_LOW:.1f} growth {NEED_GROWTH*100:.1f} lng {LNG_NEED_BCM:.1f} bcm {LNG_NEED_MT:.1f} Mt pngrb {PNGRB_SH} iea {IEA_BCM} {IEA_SH:.2f} power+ {POWER_EXTRA:.2f} pp {POWER_PP:.2f} fy25 {BCM['2024-25']:.2f}")
