import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-storage-vgf.html'

# ---------------------------------------------------------------- data
# Cabinet, 4 Nov 2026 (PIB PRID 2332474): VGF for 92 GWh, FY2026-27 to FY2030-31
NEW_VGF_CR = 14500
PSP, BESS, ALT = 60, 30, 2
NEW_GWH = PSP + BESS + ALT
assert NEW_GWH == 92
NEW_INV_CR = 97600
NEED_GWH = 411            # storage needed by 2031-32, per the release
PCT_OF_PRESENT = 170      # "170% of present-day grid-scale ESS capacity"
DCR = 40                  # minimum domestic content for BESS, %

# 2023 BESS VGF (Cabinet 6 Sep 2023): budgetary support within a Rs 9,400 cr outlay
T1_VGF_CR, T1_INV_CR, T1_GWH = 3760, 9400, 4
T1_REBID_LAKH_MWH = 27        # Rs lakh/MWh in later rounds (CEA BESS portal; PIB Feb 2026)
T1_EXT_GWH = 13.8             # extended capacity, MoP answers
T1_COMM_GWH, T1_PAID_CR, T1_BESPA_GWH, T1_FC_GWH = 0.5, 168.04, 12.7, 6.54  # RS Q152, 20 Jul 2026
# 2025 PSDF VGF (MoP order 9 Jun 2025)
P_VGF_CR, P_GWH, P_RATE_LAKH, P_INV_CR = 5400, 30, 18, 33000
P_LOA, P_BESPA, P_FC, P_SANC_CR = 22.43, 19.65, 5, 180
COMBINED_OLD_GWH = 43.8        # LS Q697, 23 Jul 2026: both BESS VGF schemes
assert abs(T1_EXT_GWH + P_GWH - COMBINED_OLD_GWH) < 1e-9
# Installed base, June 2026 (IEEFA-JMK EnergyWatts)
PHS_GWH, BESS_GWH = 36, 8.3
INSTALLED = PHS_GWH + BESS_GWH
# Costs
CTUIL_CR_MWH = 0.80            # CTUIL BESS capex benchmark, Sept 2026 (secondary)
VENDOR_LO, VENDOR_HI = 1.25, 1.8   # vendor turnkey Rs cr/MWh (vendor blogs)
CN_CELL_RS_KWH = 5114          # IEEFA Sept 2026, China cell price ~$53.57/kWh
# GEC-III (Cabinet 30 Sep 2026): Rs 50,000 cr for 50 GWh BESS, by 2032-33
GEC_GWH, GEC_CR = 50, 50000
# ACC PLI (this blog's battery piece, 7 Nov refresh)
ACC_AWARD, ACC_COMM = 40, 1.4

# ---------------------------------------------------------------- arithmetic
def rs_kwh(cr, gwh):           # Rs crore over GWh -> Rs per kWh
    return cr * 1e7 / (gwh * 1e6)

NEW_KWH = rs_kwh(NEW_VGF_CR, NEW_GWH)
NEW_INV_KWH = rs_kwh(NEW_INV_CR, NEW_GWH)
NEW_SHARE = NEW_VGF_CR / NEW_INV_CR * 100
T1_KWH = rs_kwh(T1_VGF_CR, T1_GWH)
T1_INV_KWH = rs_kwh(T1_INV_CR, T1_GWH)
T1_REBID_KWH = T1_REBID_LAKH_MWH * 1e5 / 1000
P_KWH = rs_kwh(P_VGF_CR, P_GWH)
P_INV_KWH = rs_kwh(P_INV_CR, P_GWH)
P_SHARE = P_VGF_CR / P_INV_CR * 100
CTUIL_KWH = CTUIL_CR_MWH * 1e7 / 1000
assert round(NEW_KWH) == 1576 and round(NEW_SHARE, 1) == 14.9
assert T1_KWH == 9400 and T1_VGF_CR / T1_INV_CR == 0.4
assert P_KWH == P_RATE_LAKH * 1e5 / 1000 == 1800
assert CTUIL_KWH == 8000
P_OF_CTUIL = P_KWH / CTUIL_KWH * 100
NEW_OF_CTUIL = NEW_KWH / CTUIL_KWH * 100
REBID_OF_CTUIL = T1_REBID_KWH / CTUIL_KWH * 100
assert round(P_OF_CTUIL, 1) == 22.5
# If the 30 GWh of BESS were paid at the PSDF rate (illustration only)
BESS_AT_PSDF_CR = BESS * P_RATE_LAKH * 1e5 * 1000 / 1e7
REST_CR = NEW_VGF_CR - BESS_AT_PSDF_CR
REST_KWH = rs_kwh(REST_CR, PSP + ALT)
assert BESS_AT_PSDF_CR == 5400
# Cells as a share of system cost
CELL_SHARE_CTUIL = CN_CELL_RS_KWH / CTUIL_KWH * 100
CELL_SHARE_LO = CN_CELL_RS_KWH / (VENDOR_HI * 1e4) * 100
CELL_SHARE_HI_V = CN_CELL_RS_KWH / (VENDOR_LO * 1e4) * 100
# Coverage of 411 GWh
PRESENT_IMPLIED = NEW_GWH / (PCT_OF_PRESENT / 100)
OLD_PENDING = COMBINED_OLD_GWH - T1_COMM_GWH
COVER = INSTALLED + OLD_PENDING + NEW_GWH
COVER_PCT = COVER / NEED_GWH * 100
COVER_GEC = COVER + GEC_GWH
COVER_GEC_PCT = COVER_GEC / NEED_GWH * 100
GAP = NEED_GWH - COVER
GAP_GEC = NEED_GWH - COVER_GEC
assert round(COVER, 1) == 179.6 and round(COVER_PCT) == 44 and round(COVER_GEC_PCT) == 56
T1_PAID_PCT = T1_PAID_CR / T1_VGF_CR * 100
BESS_SUPPORTED = T1_EXT_GWH + P_GWH + BESS + GEC_GWH
PER_YEAR = NEW_GWH / 5


def chart_perkwh():
    rows = [("2023 scheme, as approved", T1_KWH),
            ("2023 scheme, later rounds", T1_REBID_KWH),
            ("2025 PSDF scheme", P_KWH),
            ("2026 scheme, average", NEW_KWH)]
    W, L, top, bh, gap, lab = 340, 4, 30, 24, 10, 150
    H = top + len(rows) * (bh + gap) + 14
    sc = (W - L - lab - 46) / 9400
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Viability gap funding per kWh of storage: 2023 scheme as approved Rs 9,400; 2023 scheme in later rounds Rs 2,700; 2025 PSDF scheme Rs 1,800; 2026 scheme average Rs 1,576.">',
         f'<text x="{L}" y="13" font-size="13.5" fill="#495057">Government support per kWh of storage, &#8377;</text>']
    for i, (n, v) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 16}" font-size="12.5" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="#1c5d99"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 16}" font-size="12.5" fill="#212529">{v:,.0f}</text>')
    s.append(f'<text x="{L}" y="{H - 2}" font-size="10.5" fill="#6c757d">Cabinet and MoP decisions; 2026 is an average.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_money():
    return table(["Scheme", "Money, capacity", "Per kWh"], [
        ("2023 BESS VGF<br>Cabinet, 6 Sep 2023", f"&#8377;{T1_VGF_CR:,} cr<br>4 GWh, later<br>about {T1_EXT_GWH} GWh", f"&#8377;{T1_KWH:,.0f} approved<br>&#8377;{T1_REBID_KWH:,.0f} later"),
        ("2025 PSDF VGF<br>MoP order, 9 Jun 2025", f"&#8377;{P_VGF_CR:,} cr<br>{P_GWH} GWh", f"&#8377;{P_KWH:,.0f}"),
        ("2026 storage VGF<br>Cabinet, 4 Nov 2026", f"&#8377;{NEW_VGF_CR:,} cr<br>{NEW_GWH} GWh: {PSP} PSP,<br>{BESS} BESS, {ALT} other", f"&#8377;{NEW_KWH:,.0f} average<br>(split not given)"),
    ])


def t_status():
    return table(["Scheme", "Local content", "Delivered so far"], [
        ("2023 BESS VGF", "20%, as<br>reported", f"{T1_COMM_GWH} GWh live<br>&#8377;{T1_PAID_CR:,.0f} cr paid<br>(July 2026)"),
        ("2025 PSDF VGF", "Not found<br>in sources", f"{P_FC} GWh<br>financed;<br>&#8377;{P_SANC_CR} cr<br>sanctioned<br>(July 2026)"),
        ("2026 storage VGF", f"{DCR}% minimum<br>for batteries", "Not yet bid"),
    ])


def t_cover():
    return table(["Storage, GWh", "Amount", "Share of 411"], [
        ("Installed, June 2026 (pumped hydro 36, batteries 8.3)", f"{INSTALLED:.1f}", f"{INSTALLED / NEED_GWH * 100:.0f}%"),
        ("2023 and 2025 battery VGF, not yet commissioned", f"{OLD_PENDING:.1f}", f"{OLD_PENDING / NEED_GWH * 100:.0f}%"),
        ("2026 scheme", f"{NEW_GWH}", f"{NEW_GWH / NEED_GWH * 100:.0f}%"),
        ("<b>Total if all is built</b>", f"<b>{COVER:.1f}</b>", f"<b>{COVER_PCT:.0f}%</b>"),
        ("Green Energy Corridor III batteries (due 2032-33)", f"{GEC_GWH}", f"{GEC_GWH / NEED_GWH * 100:.0f}%"),
        ("<b>Total with GEC III</b>", f"<b>{COVER_GEC:.1f}</b>", f"<b>{COVER_GEC_PCT:.0f}%</b>"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>&#8377;{NEW_VGF_CR:,} cr</b><span>viability gap funding for {NEW_GWH} GWh of storage, FY2026-27 to FY2030-31</span></div>
<div class="gb-stat"><b>&#8377;{NEW_KWH:,.0f}/kWh</b><span>average support, {NEW_SHARE:.1f}% of the &#8377;{NEW_INV_CR:,} crore investment the Cabinet expects</span></div>
<div class="gb-stat"><b>{DCR}%</b><span>minimum domestic content for the battery part; India&rsquo;s cell plants under the ACC PLI had commissioned about {ACC_COMM} GWh</span></div>
<div class="gb-stat"><b>{COVER_PCT:.0f}%</b><span>of the {NEED_GWH} GWh needed by 2031-32 if everything installed, supported and approved so far gets built</span></div>
</div>'''

WARN = 'style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px"'

body = f"""
{stats}

<p>On 4 November the Union Cabinet approved &#8377;{NEW_VGF_CR:,} crore of viability gap funding (VGF), a capital subsidy that covers part of a project&rsquo;s cost so that it can sell its service at a price buyers will pay, for {NEW_GWH} GWh of grid-scale energy storage that has not yet been commissioned. The money runs from 2026-27 to 2030-31. This blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/09/indias-battery-storage-boom-is.html">piece on India&rsquo;s battery storage boom</a> found tariffs for new battery projects climbing back above the viability benchmark in 2026 and a domestic cell industry far behind the pack assemblers. The new scheme is the third round of storage VGF in three years, and the first to include pumped hydro.</p>
<p>This piece sets the three schemes side by side, works out what each pays per kWh, checks how far they get toward the storage the Cabinet itself says the grid needs, and asks whether the {DCR}% domestic-content rule for batteries can be met with the cells India makes today.</p>

<h2 class="gb-h2">What the Cabinet approved</h2>
<p>The release splits the {NEW_GWH} GWh into {PSP} GWh of pumped storage (PSP), {BESS} GWh of battery energy storage (BESS) and {ALT} GWh of other technologies. It expects &#8377;{NEW_INV_CR:,} crore of investment, so the subsidy is {NEW_SHARE:.1f}% of the total. Projects will be awarded through tariff-based competitive bidding. Public and private distribution companies can get VGF for batteries and pumped storage, and public or private entities for the other technologies. Battery projects must have at least {DCR}% domestic content.</p>
<p>The release puts the need at {NEED_GWH} GWh of storage by 2031-32, and says the {NEW_GWH} GWh is {PCT_OF_PRESENT}% of present grid-scale capacity. It does not say how the &#8377;{NEW_VGF_CR:,} crore is split between pumped storage and batteries, or what rate per MWh each will get.</p>

<h2 class="gb-h2">Three schemes, falling support per kWh</h2>
{t_money()}
{chart_perkwh()}
<p>The 2023 scheme, approved on 6 September 2023, set aside &#8377;{T1_VGF_CR:,} crore of budget support for 4 GWh of batteries, up to 40% of capital cost. As approved, that was &#8377;{T1_KWH:,.0f} per kWh against an assumed cost of &#8377;{T1_INV_KWH:,.0f} per kWh. Battery prices then fell, and later rounds capped support at 30% of capital cost or &#8377;{T1_REBID_LAKH_MWH} lakh per MWh (&#8377;{T1_REBID_KWH:,.0f} per kWh). The same money was stretched to about {T1_EXT_GWH} GWh.</p>
<p>The second scheme, a Ministry of Power order of 9 June 2025, used &#8377;{P_VGF_CR:,} crore from the Power System Development Fund (PSDF), a fund built from grid congestion and deviation charges, for {P_GWH} GWh: 25 GWh across 15 states and 5 GWh for NTPC. It paid a flat &#8377;{P_RATE_LAKH} lakh per MWh, &#8377;{P_KWH:,.0f} per kWh, about {P_SHARE:.0f}% of the &#8377;{P_INV_CR:,} crore of investment reported at the time.</p>
<p>The new scheme averages &#8377;{NEW_KWH:,.0f} per kWh across all three technologies. The Central Transmission Utility&rsquo;s September 2026 benchmark for battery capital cost, as reported, is &#8377;{CTUIL_CR_MWH:.2f} crore per MWh, or &#8377;{CTUIL_KWH:,.0f} per kWh. Against that, the 2025 rate covers {P_OF_CTUIL:.1f}% of a battery&rsquo;s cost and the new average {NEW_OF_CTUIL:.1f}%. If the {BESS} GWh of batteries were paid at the 2025 rate, they would take &#8377;{BESS_AT_PSDF_CR:,.0f} crore, leaving &#8377;{REST_CR:,.0f} crore, or &#8377;{REST_KWH:,.0f} per kWh, for pumped storage and the rest. That is an illustration, not the scheme&rsquo;s split.</p>
<p>Lower support per kWh is partly good news, since it tracks cheaper hardware. But the battery piece showed 2026 tariffs rising, with Maharashtra&rsquo;s distribution company awarding 2-hour storage at &#8377;2.38 lakh per MW per month in September, above the viability benchmark of &#8377;2.3 lakh. Pumped storage costs are rising too: IEEFA&ndash;JMK report that a SECI 8-hour pumped-storage award in 2026 cleared at &#8377;108&ndash;110 lakh per MW per year, about 40&ndash;43% above a 2025 Uttar Pradesh award. A smaller subsidy per kWh is arriving as the price developers bid is going up.</p>

<h2 class="gb-h2">What the earlier money has built</h2>
{t_status()}
<p>The 2023 scheme was approved more than three years ago. By July 2026, according to a Rajya Sabha answer, battery energy storage purchase agreements had been signed for {T1_BESPA_GWH} GWh, {T1_FC_GWH} GWh had reached financial closure, {T1_COMM_GWH} GWh was commissioned and &#8377;{T1_PAID_CR:,.2f} crore had been paid, {T1_PAID_PCT:.1f}% of the budget. Under the 2025 scheme, letters of award covered {P_LOA} GWh and agreements {P_BESPA} GWh, {P_FC} GWh had reached financial closure, and &#8377;{P_SANC_CR} crore had been sanctioned. Projects under the 2025 order are due within 18 months of their agreements.</p>
<p>VGF is paid in stages, much of it only after a project starts running, so low payments do not mean the schemes have failed. But they do mean that almost none of the {COMBINED_OLD_GWH} GWh supported under the first two schemes was yet supplying the grid when the third was approved.</p>

<h2 class="gb-h2">Can batteries meet 40% domestic content?</h2>
<p>The release sets the {DCR}% floor but does not define it: whether it is measured on the whole project cost or on equipment, and whether imported cells assembled in India count. That matters because cells are a large share of the cost. IEEFA&ndash;JMK put Chinese cell prices at about $53.57 per kWh in September 2026, roughly &#8377;{CN_CELL_RS_KWH:,} per kWh. Against the &#8377;{CTUIL_KWH:,.0f} per kWh capital-cost benchmark, cells would be about {CELL_SHARE_CTUIL:.0f}% of a battery project. Against vendor turnkey prices of &#8377;{VENDOR_LO}&ndash;{VENDOR_HI} crore per MWh, they would be {CELL_SHARE_LO:.0f}&ndash;{CELL_SHARE_HI_V:.0f}%. At the low end of cost, a project with imported cells has little room to reach {DCR}% from containers, inverters, cabling and civil work alone.</p>
<p>Indian cells are scarce. The battery piece found India&rsquo;s lithium-ion cell capacity around 1 GWh at the end of 2025, against about 60 GWh of pack assembly, with estimates of China&rsquo;s share of India&rsquo;s cell imports at 63&ndash;85% or higher. The ACC PLI scheme for cell factories had awarded {ACC_AWARD} GWh and commissioned about {ACC_COMM} GWh. A 10 GWh tranche reserved for grid storage closed for bids on 13 October 2026. IEEFA&ndash;JMK also report that cells and containers landed in India cost 14&ndash;23% more than Chinese prices after tax.</p>
<p>The government-backed battery pipeline now covers about {BESS_SUPPORTED:.0f} GWh: about {T1_EXT_GWH} GWh under the 2023 scheme, {P_GWH} GWh under PSDF, {BESS} GWh under the new scheme and {GEC_GWH} GWh under Green Energy Corridor III. If the {DCR}% rule needs Indian cells, it will bind on a market where domestic supply is a fraction of one year&rsquo;s demand, and the 14&ndash;23% landed premium will be priced into bids. The VGF would then partly pay for that premium rather than for more storage.</p>

<h2 class="gb-h2">How far this gets toward 411 GWh</h2>
{t_cover()}
<p>The IEEFA&ndash;JMK tracker put installed storage at about {INSTALLED:.1f} GWh in June 2026: {PHS_GWH} GWh of pumped hydro and {BESS_GWH} GWh of batteries. The Cabinet release&rsquo;s &ldquo;{PCT_OF_PRESENT}%&rdquo; implies present capacity of about {PRESENT_IMPLIED:.0f} GWh. The difference may come from what each counts, and this piece uses the tracker&rsquo;s figure. Adding the undelivered capacity under the two earlier schemes and the new {NEW_GWH} GWh gives about {COVER:.0f} GWh, {COVER_PCT:.0f}% of {NEED_GWH} GWh, leaving a gap of about {GAP:.0f} GWh. Green Energy Corridor III&rsquo;s {GEC_GWH} GWh of batteries, due a year after the 2031-32 date, would take it to {COVER_GEC_PCT:.0f}%.</p>
<p>The totals assume every supported project is built. Some may overlap with capacity already counted, and pumped storage projects often take longer than five years to build. The new scheme needs about {PER_YEAR:.0f} GWh a year to be bid, built and commissioned through 2030-31, more than twice the battery capacity installed by mid-2026, every year.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Ministry of Power should publish the split of the &#8377;{NEW_VGF_CR:,} crore between pumped storage, batteries and other technologies, with the VGF rate per MWh for each, before the first tender.</li>
<li>The {DCR}% domestic content rule should be defined in the guidelines: the cost base it is measured on, whether cells must be made in India, and a schedule that ties any cell requirement to ACC PLI capacity actually commissioned.</li>
<li>A single public dashboard should track every VGF-supported storage project across all three schemes: agreement, financial closure, commissioning and VGF paid, updated quarterly.</li>
<li>The Central Electricity Authority should reconcile installed storage capacity with industry trackers, so that the base against which {NEED_GWH} GWh is measured is the same in every official document.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The Cabinet release does not split the &#8377;{NEW_VGF_CR:,} crore or the &#8377;{NEW_INV_CR:,} crore of investment by technology, so per-kWh support for batteries alone under the new scheme is not known; the &#8377;{NEW_KWH:,.0f} figure is an average across pumped storage, batteries and other technologies. The release does not define how the {DCR}% domestic content is measured. Whether the 2025 PSDF scheme had a domestic content rule was not found in the sources used. The 20% domestic content figure for the 2023 scheme comes from this blog&rsquo;s earlier piece. The CTUIL capital-cost benchmark is taken from a secondary report and vendor price ranges from vendor sites, not from a tender. Cell-cost shares mix an international cell price with Indian system costs and ignore the extra cell capacity a battery needs beyond its rated energy, so they are indicative. The gap between the tracker&rsquo;s {INSTALLED:.1f} GWh and the {PRESENT_IMPLIED:.0f} GWh implied by the release could not be explained from the release itself. Whether the 2023 scheme&rsquo;s {T1_COMM_GWH} GWh commissioned is already inside the tracker&rsquo;s {BESS_GWH} GWh is assumed, not confirmed.</p>
"""

sources = (
    'Cabinet decision of 4 November 2026: <a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2332474">PIB, PRID 2332474</a> (read directly). '
    '2023 BESS VGF: Cabinet decision of 6 September 2023; later-round rates from the <a href="https://intranet.cea.gov.in/bess/about">CEA BESS portal</a> and a PIB note of February 2026 (13,220 MWh at &#8377;27 lakh/MWh); status from <a href="https://sansad.in/getFile/annex/271/AU152_Uoc3WR.pdf?source=pqars">Rajya Sabha unstarred question 152, 20 July 2026</a>. '
    '2025 PSDF VGF: <a href="https://powermin.gov.in/sites/default/files/webform/notices/VGF_PSDF_order_dated_9June2025_0.pdf">Ministry of Power order, 9 June 2025</a>; investment estimate from <a href="https://energy.economictimes.indiatimes.com/news/power/government-approves-5400-cr-funding-for-30-gwh-battery-storage-to-boost-renewable-energy-infrastructure/121756430">ETEnergyWorld, 10 June 2025</a>; <a href="https://jmkresearch.com/vgf-scheme-expands-to-support-30-gwh-of-new-standalone-bess-development-in-india">JMK Research summary</a>; status and the 43.8 GWh combined figure from <a href="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU697_cnoTct.pdf">Lok Sabha unstarred question 697, 23 July 2026</a>. '
    'Storage requirement for 2029-30 (CEA optimal generation mix): <a href="https://pib.gov.in/PressReleasePage.aspx?PRID=2222473&amp;lang=1&amp;reg=3">PIB, 3 February 2026</a>. '
    'Installed storage, June 2026: <a href="https://ieefa.org/sites/default/files/2026-08/ESSjmk-0626.pdf">IEEFA&ndash;JMK EnergyWatts, June 2026</a>. Pumped-storage tariffs: <a href="https://ieefa.org/sites/default/files/2026-08/ESSjmk-0826.pdf">IEEFA&ndash;JMK, August 2026</a>. Cell prices and landed premium: <a href="https://ieefa.org/sites/default/files/2026-09/ESSjmk-0926.pdf">IEEFA&ndash;JMK, September 2026</a>. '
    'CTUIL capex benchmark of &#8377;0.80 crore/MWh as reported by <a href="https://www.sunwavetech.com/blog/bess-cost-per-kwh-india-2026">Sun Wave</a> (a vendor blog; secondary). '
    'ACC PLI progress, cell import estimates, MSEDCL tariff and Green Energy Corridor III: this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/09/indias-battery-storage-boom-is.html">battery storage piece</a> and its 7 November 2026 update, and the sources cited there. '
    'Per-kWh rates, subsidy shares, cell-cost shares and coverage of 411 GWh are this blog&rsquo;s arithmetic. Nothing here is investment advice.')

related = [
    ("https://masaladeutsch.blogspot.com/2026/09/indias-battery-storage-boom-is.html", "India&rsquo;s Battery Storage Boom Is Outrunning Both Its Tariffs and Its Factories"),
    ("https://masaladeutsch.blogspot.com/2026/08/the-battery-passport-was-built-for.html", "The Battery Passport Was Built for Recycling. Now It&rsquo;s Also the Fix for Battery Fires."),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-approved-solar-cell-makers-can.html", "India&rsquo;s Approved Solar-Cell Makers Can Now Make 37.8 GW a Year. Rooftop Projects Have Until 31 December to Use Them"),
    ("https://masaladeutsch.blogspot.com/2026/09/electrification-is-lngs-biggest.html", "Electrification Is LNG&rsquo;s Biggest Decarbonization Lever. The Grid Is What Actually Limits It"),
]

build("Power &middot; 8 November 2026",
      "&#8377;14,500 Crore for 92 GWh: India&rsquo;s Storage Subsidy Is Down to &#8377;1,576 a kWh. The 40% Local-Content Rule Is the Harder Part",
      f"The Cabinet&rsquo;s third storage subsidy in three years covers pumped hydro for the first time and pays less per kWh than either earlier scheme. Built in full, it takes India to about {COVER_PCT:.0f}% of the storage it says it needs by 2031-32, but the battery share depends on cells India barely makes.",
      body, sources, related, OUT)
print(dict(new_kwh=round(NEW_KWH), share=round(NEW_SHARE, 2), p_share=round(P_SHARE, 1), p_ctuil=P_OF_CTUIL, new_ctuil=round(NEW_OF_CTUIL, 1),
           rest_kwh=round(REST_KWH), cell=(round(CELL_SHARE_CTUIL), round(CELL_SHARE_LO), round(CELL_SHARE_HI_V)),
           implied=round(PRESENT_IMPLIED, 1), cover=COVER, pct=round(COVER_PCT, 1), gec=round(COVER_GEC_PCT, 1), gap=round(GAP, 1), paid=round(T1_PAID_PCT, 2), bess=BESS_SUPPORTED, per_year=PER_YEAR))
