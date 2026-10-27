import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-steelpolicy.html'

# ---------------------------------------------------------------- data
# Crude steel capacity and production, Mt (JPC via Lok Sabha replies; 2025-26 Ministry of Steel overview, provisional)
YEARS = ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
CAP = [143.91, 154.06, 161.30, 179.51, 200.33, 220.41]
PROD = [103.54, 120.29, 127.20, 144.30, 152.18, 170.15]
FIN_PROD_2526 = 162.47                 # finished steel production 2025-26, Mt
CAP_1718 = 137.97                      # 2017-18 capacity, Ministry monthly analysis
# National Steel Policy 2017 targets for 2030-31
NSP17_CAP, NSP17_PROD = 300, 255
# Draft National Steel Policy - Vision 2047 (released for comment Oct 2026)
D_CAP, D_DEMAND = 604, 505             # Mt capacity, Mt finished steel demand
D_COKING, D_COKING_ALT = 236, 214      # Mt coking coal demand 2047 (SteelOrbis/SMM; one summary says 214)
D_COKING_NOW = 72                      # Mt current coking coal demand per the draft
D_IMPORT_SHARE = 0.92                  # share of coking coal imported
D_ORE = 772                            # Mt iron ore demand 2047
D_CO2_NOW, D_CO2_2047 = 2.54, 1.54     # t CO2 per t crude steel
SCRAP_NOW, SCRAP_2047 = 36, 123        # Mt scrap processed (BigMint, via GMK Center)
COKING_IMP_2526 = 66.25                # Mt coking coal imports 2025-26 (port data, provisional)
ORE_2425 = 289                         # Mt iron ore production 2024-25 (Ministry of Mines, provisional)
BF_SHARE_NOW = 0.41                    # BF-BOF share of crude steel, FY25 (BigMint)
EU_EXPORTS = (2.4, 4.0)                # Mt steel to the EU in 2025, by definition

# Derived
UTIL_2526 = PROD[-1] / CAP[-1]
YIELD = FIN_PROD_2526 / PROD[-1]                 # finished per tonne crude
P2047 = D_DEMAND / YIELD                         # crude steel needed for 505 Mt finished demand, no net trade
UTIL_2047 = P2047 / D_CAP
BF_NOW = BF_SHARE_NOW * PROD[-1]
COAL_INT_IN = D_COKING_NOW / BF_NOW              # t coking coal per t BF-BOF steel, calibrated to the draft
COAL_INT_WS = 0.78                               # worldsteel average for BF-BOF
ADD_PER_YR_RECENT = (CAP[-1] - CAP[2]) / 3       # 2022-23 to 2025-26
ADD_PER_YR_NEED = (D_CAP - CAP[-1]) / 21         # 2025-26 to 2046-47
PROD_CAGR_RECENT = (PROD[-1] / PROD[0]) ** (1 / 5) - 1
PROD_CAGR_2031 = (NSP17_PROD / PROD[-1]) ** (1 / 5) - 1

# Emission intensities, t CO2 per t crude steel (BigMint, citing industry sources)
EF_BF, EF_GASDRI, EF_SCRAP = 2.6, 1.6, 1.2

def scenario(name, bf):
    scrap = SCRAP_2047
    dri = P2047 - bf - scrap
    s_bf, s_sc, s_dri = bf / P2047, scrap / P2047, dri / P2047
    req_bf = (D_CO2_2047 - s_sc * EF_SCRAP - s_dri * EF_GASDRI) / s_bf     # best case: all DRI gas-based
    return dict(name=name, bf=bf, scrap=scrap, dri=dri, s_bf=s_bf, s_sc=s_sc, s_dri=s_dri,
                coal_in=bf * COAL_INT_IN, coal_ws=bf * COAL_INT_WS, req_bf=req_bf)

SC = [
    scenario("Today&rsquo;s share of blast furnaces, 41%", BF_SHARE_NOW * P2047),
    scenario("Draft&rsquo;s 236 Mt coal, at India&rsquo;s coal use per tonne", D_COKING / COAL_INT_IN),
    scenario("Draft&rsquo;s 236 Mt coal, at world-average coal use", D_COKING / COAL_INT_WS),
]
IMP_2047 = D_COKING * D_IMPORT_SHARE
ORE_PER_PRIMARY = D_ORE / (P2047 - SCRAP_2047)


def chart_path():
    W, L, top, H0 = 400, 34, 34, 150
    bars = list(zip(YEARS, CAP, PROD)) + [("2030-31 target", NSP17_CAP, NSP17_PROD), ("2047 draft", D_CAP, P2047)]
    n = len(bars)
    gw = (W - L - 10) / n
    bw = gw * 0.36
    sc = (H0 - 10) / 620
    base = top + H0
    H = base + 46
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="India crude steel capacity and production, 2020-21 to 2025-26, with the 2017 policy target for 2030-31 and the draft target for 2047.">',
         f'<text x="10" y="12" font-size="12" fill="#495057">Crude steel, million tonnes a year</text>',
         f'<rect x="10" y="20" width="9" height="9" fill="#868e96"/><text x="23" y="28" font-size="9.5" fill="#212529">Capacity</text>',
         f'<rect x="80" y="20" width="9" height="9" fill="#1c5d99"/><text x="93" y="28" font-size="9.5" fill="#212529">Production (2047: needed for the draft&rsquo;s demand)</text>']
    for v in (0, 200, 400, 600):
        y = base - v * sc
        s.append(f'<line x1="{L}" x2="{W - 6}" y1="{y:.1f}" y2="{y:.1f}" stroke="#dee2e6"/>')
        s.append(f'<text x="{L - 4}" y="{y + 3:.1f}" font-size="8.5" fill="#6c757d" text-anchor="end">{v}</text>')
    for i, (lab, c, p) in enumerate(bars):
        x = L + 4 + i * gw
        tgt = i >= len(YEARS)
        for j, (v, col) in enumerate(((c, "#868e96"), (p, "#1c5d99"))):
            h = v * sc
            op = ' fill-opacity="0.55"' if tgt else ''
            s.append(f'<rect x="{x + j * (bw + 1):.1f}" y="{base - h:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{col}"{op}/>')
        s.append(f'<text x="{x + bw:.1f}" y="{base - c * sc - 3:.1f}" font-size="7.5" fill="#212529" text-anchor="middle">{c:.0f}</text>')
        parts = lab.split(" ", 1)
        s.append(f'<text x="{x + bw:.1f}" y="{base + 11}" font-size="7.5" fill="#212529" text-anchor="middle">{parts[0]}</text>')
        if len(parts) > 1:
            s.append(f'<text x="{x + bw:.1f}" y="{base + 20}" font-size="7.5" fill="#212529" text-anchor="middle">{parts[1]}</text>')
    s.append(f'<text x="10" y="{H - 4}" font-size="9" fill="#6c757d">JPC and Ministry of Steel; 2017 policy; draft policy (Oct 2026). Faded bars are targets.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_routes():
    W, L, top, bh, gap, lab = 400, 10, 40, 18, 26, 0
    rows = [("2025-26 actual (approx.)", PROD[-1], BF_NOW, SCRAP_NOW, PROD[-1] - BF_NOW - SCRAP_NOW, D_COKING_NOW)] + \
           [(f"2047: {r['name']}", P2047, r['bf'], r['scrap'], r['dri'], r['coal_ws'] if i == 2 else r['coal_in']) for i, r in enumerate(SC)]
    H = top + len(rows) * (bh + gap) + 16
    sc = (W - L - 70) / 540
    cols = ("#a5402c", "#d9a441", "#1c5d99")
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Crude steel by route in 2025-26 and in three 2047 scenarios built from the draft policy&rsquo;s own coal and scrap figures.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Crude steel by route, Mt; label: coking coal needed, Mt</text>',
         f'<rect x="{L}" y="20" width="9" height="9" fill="{cols[0]}"/><text x="{L + 13}" y="28" font-size="9.5" fill="#212529">Blast furnace</text>',
         f'<rect x="{L + 95}" y="20" width="9" height="9" fill="{cols[2]}"/><text x="{L + 108}" y="28" font-size="9.5" fill="#212529">DRI (sponge iron)</text>',
         f'<rect x="{L + 210}" y="20" width="9" height="9" fill="{cols[1]}"/><text x="{L + 223}" y="28" font-size="9.5" fill="#212529">Scrap</text>']
    for i, (n, tot, bf, scrap, dri, coal) in enumerate(rows):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L}" y="{y + 10}" font-size="9.5" fill="#212529">{n}</text>')
        x = L
        yb = y + 14
        for v, col in ((bf, cols[0]), (dri, cols[2]), (scrap, cols[1])):
            w = v * sc
            s.append(f'<rect x="{x:.1f}" y="{yb}" width="{w:.1f}" height="{bh}" fill="{col}"/>')
            if w > 24:
                s.append(f'<text x="{x + w / 2:.1f}" y="{yb + 13}" font-size="9" fill="#fff" text-anchor="middle" font-weight="700">{v:.0f}</text>')
            x += w
        s.append(f'<text x="{x + 4:.1f}" y="{yb + 13}" font-size="9.5" fill="#212529">{coal:.0f} Mt coal</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">This blog&rsquo;s arithmetic; coal at India&rsquo;s rate except the last row (world rate).</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_policies():
    return table(["", "2017 policy, for 2030-31", "Actual, 2025-26", "Draft policy, for 2047"], [
        ("Crude steel capacity (Mt)", f"{NSP17_CAP}", f"{CAP[-1]:.1f}", f"{D_CAP}"),
        ("Crude steel production (Mt)", f"{NSP17_PROD}", f"{PROD[-1]:.1f} (provisional)", f"about {P2047:.0f} implied*"),
        ("Finished steel consumption (Mt)", "&mdash;", "about 164", f"{D_DEMAND}"),
        ("Coking coal (Mt)", "&mdash;", f"{D_COKING_NOW} needed; {COKING_IMP_2526:.1f} imported", f"{D_COKING} ({D_COKING_ALT} in one summary)"),
        ("Iron ore (Mt)", "&mdash;", f"{ORE_2425} mined (2024-25)", f"{D_ORE}"),
        ("Scrap processed (Mt)", "&mdash;", f"{SCRAP_NOW}", f"{SCRAP_2047}"),
        ("CO<sub>2</sub> per tonne of crude steel", "&mdash;", f"{D_CO2_NOW}", f"{D_CO2_2047}"),
    ])


def t_scen():
    rows = []
    for r in SC:
        rows.append((r['name'], f"{r['bf']:.0f} ({r['s_bf'] * 100:.0f}%)", f"{r['dri']:.0f} ({r['s_dri'] * 100:.0f}%)",
                     f"{r['coal_in']:.0f} / {r['coal_ws']:.0f}", f"{r['req_bf']:.2f}"))
    return table(["2047 scenario", "Blast-furnace steel, Mt", "DRI steel, Mt", "Coking coal, Mt (India rate / world rate)", "CO<sub>2</sub> the blast-furnace route may emit to hit 1.54 (t/t)"], rows)


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{D_CAP} Mt</b><span>crude steel capacity the draft policy targets for 2047, {D_CAP / CAP[-1]:.1f} times today&rsquo;s {CAP[-1]:.0f} Mt</span></div>
<div class="gb-stat"><b>{D_COKING} Mt</b><span>coking coal the draft expects to need, against {D_COKING_NOW} Mt now; {D_IMPORT_SHARE * 100:.0f}% is imported today</span></div>
<div class="gb-stat"><b>{SC[1]['s_bf'] * 100:.0f}&ndash;{SC[2]['s_bf'] * 100:.0f}%</b><span>of 2047 steel that would come from blast furnaces, if the draft&rsquo;s coal figure is right</span></div>
<div class="gb-stat"><b>~{(1 - max(r['req_bf'] for r in SC) / EF_BF) * 100:.0f}%</b><span>cut in blast-furnace emissions per tonne needed to reach the draft&rsquo;s 1.54 t CO<sub>2</sub>, even with all other steel gas- or scrap-based</span></div>
</div>'''

body = f"""
{stats}

<p>The Ministry of Steel has put out a draft National Steel Policy, Vision 2047, for comment until 30 October. It would replace the 2017 policy, whose horizon ends in 2030-31, with targets of {D_CAP} million tonnes (Mt) of crude steel capacity and {D_DEMAND} Mt of finished steel demand by 2047, close to three times today&rsquo;s levels. Alongside, it proposes a Rs 5,000 crore scheme, Viksit Bharat Ispat, to pay smaller producers incentives linked to output and lower emissions, and it aims to cut the industry&rsquo;s average emissions from {D_CO2_NOW} to {D_CO2_2047} tonnes of CO<sub>2</sub> per tonne of crude steel.</p>
<p>The capacity target is the headline, but the draft&rsquo;s raw-material figures say more about what kind of industry it expects. This piece checks how the 2017 policy is doing, works out from the draft&rsquo;s own numbers how much steel would come from coal-fired blast furnaces in 2047, and asks whether that fits its emissions goal and the carbon border tax India&rsquo;s exports will face.</p>

<h2 class="gb-h2">The 2017 policy is broadly on track</h2>
{chart_path()}
<p>The 2017 policy aimed for {NSP17_CAP} Mt of capacity and {NSP17_PROD} Mt of production by 2030-31. Capacity was {CAP_1718:.0f} Mt in 2017-18 and reached {CAP[-1]:.1f} Mt in 2025-26, having grown by about {ADD_PER_YR_RECENT:.0f} Mt a year over the last three years; another {NSP17_CAP - CAP[-1]:.0f} Mt by 2030-31 needs {(NSP17_CAP - CAP[-1]) / 5:.0f} Mt a year. Production grew {PROD_CAGR_RECENT * 100:.1f}% a year from 2020-21 to 2025-26, to {PROD[-1]:.1f} Mt (provisional); reaching {NSP17_PROD} Mt needs {PROD_CAGR_2031 * 100:.1f}% a year. The weak spot is use of the plants: capacity utilisation slipped to about {UTIL_2526 * 100:.0f}% in 2025-26, as capacity grew faster than output.</p>
<p>The 2047 target extends the same pace. Going from {CAP[-1]:.0f} Mt to {D_CAP} Mt in 21 years means adding about {ADD_PER_YR_NEED:.0f} Mt a year, close to what the industry has managed recently. Meeting {D_DEMAND} Mt of finished demand at today&rsquo;s ratio of finished to crude steel ({YIELD:.3f}) needs about {P2047:.0f} Mt of crude steel, or {UTIL_2047 * 100:.0f}% of the planned capacity, assuming imports and exports roughly balance.</p>
{t_policies()}
<p class="gb-note">*Production implied by this blog: the draft&rsquo;s {D_DEMAND} Mt of finished demand divided by the 2025-26 ratio of finished to crude steel. Draft figures are as reported by SteelOrbis, Reuters, Business Standard and others; one exam-prep summary gives 214 Mt of coking coal instead of 236 Mt.</p>

<h2 class="gb-h2">What the coal figure says about the route</h2>
<p>Steel is made in India in three main ways: in blast furnaces, which turn iron ore into iron with coke made from coking coal; from direct-reduced iron (DRI, or sponge iron), made with non-coking coal or natural gas and melted in electric or induction furnaces; and by melting scrap. Only the blast furnace needs coking coal in quantity. So the draft&rsquo;s coking-coal forecast implies how much steel it expects from blast furnaces.</p>
{chart_routes()}
<p>India used {D_COKING_NOW} Mt of coking coal for about {BF_NOW:.0f} Mt of blast-furnace steel in 2025-26 (41% of output in the latest route data), about {COAL_INT_IN:.2f} tonnes per tonne. That is above the world average of about {COAL_INT_WS} tonnes cited by the World Steel Association, which fits India&rsquo;s high-ash coal and its use of coal outside steelmaking. At India&rsquo;s rate, the draft&rsquo;s {D_COKING} Mt of coal supports about {SC[1]['bf']:.0f} Mt of blast-furnace steel in 2047, {SC[1]['s_bf'] * 100:.0f}% of the {P2047:.0f} Mt needed; at the world-average rate, about {SC[2]['bf']:.0f} Mt, or {SC[2]['s_bf'] * 100:.0f}%. Either way, the blast furnace keeps or increases its share. The draft&rsquo;s own scrap projection, {SCRAP_2047} Mt by 2047, is about {SCRAP_2047 / P2047 * 100:.0f}% of output, which leaves DRI to fill the rest.</p>
{t_scen()}
<p class="gb-note">Method: production {P2047:.0f} Mt in each scenario; scrap {SCRAP_2047} Mt (draft); DRI is the remainder. Coal per tonne of blast-furnace steel: India {COAL_INT_IN:.2f} (the draft&rsquo;s {D_COKING_NOW} Mt over 41% of 2025-26 output), world {COAL_INT_WS} (World Steel Association). Last column: the blast-furnace intensity at which the industry averages {D_CO2_2047} t, if every tonne of DRI steel is gas-based at {EF_GASDRI} t and scrap steel emits {EF_SCRAP} t (BigMint&rsquo;s ranges for India); coal-based DRI, which emits more than blast furnaces, would push it lower. Today&rsquo;s blast furnaces emit about 2.5&ndash;2.7 t.</p>

<h2 class="gb-h2">Coal imports would triple</h2>
<p>The draft says India imports about {D_IMPORT_SHARE * 100:.0f}% of its coking coal; port data put 2025-26 imports at {COKING_IMP_2526:.1f} Mt, mostly from Australia, with Russia the main supplier of coal injected into furnaces. At the same import share, {D_COKING} Mt in 2047 means about {IMP_2047:.0f} Mt of imports, {IMP_2047 / COKING_IMP_2526:.1f} times today. The draft&rsquo;s answers are more domestic mining and washeries, overseas mines, long-term contracts and better blending. Iron ore is less of a constraint in tonnage, since India is largely self-sufficient, but {D_ORE} Mt is {D_ORE / ORE_2425:.1f} times the record {ORE_2425} Mt mined in 2024-25, or about {ORE_PER_PRIMARY:.1f} tonnes of ore for every tonne of steel not made from scrap, which reflects the low grade of much Indian ore.</p>

<h2 class="gb-h2">The emissions goal needs cleaner blast furnaces, not only more scrap</h2>
<p>The table&rsquo;s last column is the main finding. Even in the best case, with every tonne of DRI steel made with gas and scrap at its planned level, the industry reaches {D_CO2_2047} t of CO<sub>2</sub> per tonne only if its blast furnaces emit about {min(r['req_bf'] for r in SC):.2f}&ndash;{max(r['req_bf'] for r in SC):.2f} t, against about 2.5&ndash;2.7 t today: a cut of roughly {(1 - max(r['req_bf'] for r in SC) / EF_BF) * 100:.0f}&ndash;{(1 - min(r['req_bf'] for r in SC) / EF_BF) * 100:.0f}%. Since most of India&rsquo;s DRI is coal-based today, the real requirement is tighter. That cut would have to come from capturing carbon, injecting hydrogen or gas into furnaces, or using biomass, none of which is yet in commercial use at scale in India. The draft mentions scrap and hydrogen; as reported, it does not say how much blast-furnace capacity it expects to be fitted with them.</p>
<p>This matters because most of the new capacity has not been built yet. About {D_CAP - CAP[-1]:.0f} Mt is to be added by 2047, and plants built in the 2030s will still be running then. The European Union&rsquo;s carbon border tax already applies to steel: India sent the EU between {EU_EXPORTS[0]} and {EU_EXPORTS[1]} Mt of steel in 2025, depending on the definition, and this blog has <a href="https://masaladeutsch.blogspot.com/2026/10/to-comply-or-not-to-comply-cbam-costs.html">estimated the charge at about &euro;93 a tonne with verified emissions data and &euro;270 without</a>. The draft&rsquo;s export ambitions, and the Rs 5,000 crore emissions-linked scheme for small producers, both depend on the average actually falling.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The final policy should publish the route mix behind its coal, ore and scrap projections (blast furnace, coal DRI, gas DRI, scrap), so the forecasts can be checked against each other and against the emissions target.</li>
<li>It should set an emissions ceiling per tonne for new blast-furnace capacity approved after 2030, or require new furnaces to be built ready for carbon capture or hydrogen injection.</li>
<li>The Ministry should publish emissions per tonne by plant, verified to the standard the EU accepts, so exporters avoid default CBAM values.</li>
<li>The Viksit Bharat Ispat scheme should pay against measured emissions per tonne, verified independently, rather than on reported technology upgrades.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The draft policy document could not be opened directly; its figures come from news reports and summaries, which give coking-coal demand as {D_COKING} Mt (most) or {D_COKING_ALT} Mt (one summary). The draft&rsquo;s own assumptions about routes and utilisation were not found. Route shares for 2025-26 are not yet published; this piece uses BigMint&rsquo;s 41% blast-furnace share for 2024-25. The emission factors by route are industry ranges, not plant data, and the coal per tonne is calibrated from the draft&rsquo;s current-demand figure, which may include coal used outside steelmaking. Capacity figures for 2018-19 and 2019-20 could not be confirmed and are not shown.</p>
"""

sources = ("Draft National Steel Policy, Vision 2047 (Ministry of Steel, October 2026): as reported by Business Standard and Reuters (via Mining Weekly, Kitco), 29&ndash;30 September 2026 (600 Mt, 500 Mt, Rs 5,000 crore Viksit Bharat Ispat, 772 Mt ore, 2.54 to 1.54 t CO<sub>2</sub>); SteelOrbis, Devdiscourse, Deccan Chronicle and KNN (604 Mt, 505 Mt, 236 Mt coking coal from 72 Mt, 92% imported, comments to 30 October 2026); Shankar IAS (214 Mt); GMK Center citing BigMint (scrap 36 Mt to 123 Mt), October 2026. "
           "2017 policy targets and 2025-26 capacity, production and consumption: Ministry of Steel overview of the steel sector (2026) and Rajya Sabha reply; 2020-21 to 2024-25 capacity and production: Joint Plant Committee via Lok Sabha replies (dataful.in compilation); 2017-18 capacity: Ministry of Steel monthly analysis. "
           "Route shares and emission ranges: BigMint (FY25 route data; route intensities 2023); coking coal imports: SteelOrbis (port data, 2025-26) and BigMint via GMK Center; iron ore: Ministry of Mines via SteelOrbis and GMK Center (2024-25); raw materials per tonne: World Steel Association figures as cited by Infomerics. "
           "EU exports: Sandbag (August 2026), GMK Center and SteelOrbis. Scenario arithmetic, implied production and required intensities are this blog&rsquo;s (builder in the repository at out/research/steelpolicy/). Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/10/to-comply-or-not-to-comply-cbam-costs.html", "To Comply or Not to Comply: CBAM Costs Indian Steel &euro;93 a Tonne With Verified Data and &euro;270 Without"),
    ("https://masaladeutsch.blogspot.com/2026/10/europe-wants-green-steel-it-cant-afford.html", "Europe Wants Green Steel It Can&rsquo;t Afford to Make. Why CBAM Should Be Rolled Out More Gently"),
    ("https://masaladeutsch.blogspot.com/2026/10/india-imported-295-more-steel-this-year.html", "India Imported 29.5% More Steel This Year Despite a Safeguard Duty"),
]

build("Industrial Policy · 27 October 2026",
      "India&rsquo;s Draft Steel Policy Plans 604 Mt by 2047. Its Own Coal Forecast Means More Blast Furnaces, Not Fewer",
      "The draft National Steel Policy nearly triples capacity and cuts emissions per tonne by 40%. Its forecast of 236 Mt of coking coal implies blast furnaces keep 43&ndash;57% of output, so the emissions target rests on cleaning up blast furnaces themselves.",
      body, sources, related, OUT)
for r in SC:
    print(r['name'][:30], round(r['bf']), round(r['s_bf'] * 100), round(r['dri']), round(r['coal_in']), round(r['coal_ws']), round(r['req_bf'], 2))
print("P2047", round(P2047), "util", round(UTIL_2047 * 100), "coal int", round(COAL_INT_IN, 2), "imp", round(IMP_2047), "ore/primary", round(ORE_PER_PRIMARY, 2), "add/yr", round(ADD_PER_YR_RECENT, 1), round(ADD_PER_YR_NEED, 1), "cagr", round(PROD_CAGR_RECENT * 100, 1), round(PROD_CAGR_2031 * 100, 1))
