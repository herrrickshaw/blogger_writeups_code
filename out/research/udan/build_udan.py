import sys
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-modified-udan-route-survival.html'

# ---------------------------------------------------------------- data
# Modified UDAN, Cabinet 25 Mar 2026 (PIB / PM India), FY2026-27 to FY2035-36, Rs crore
OUTLAY = 28840
AIRPORTS_CR, AIRPORTS_N = 12159, 100
HELI_CR, HELI_N = 3661, 200
VGF_CR = 10043
OM_CR, OM_N = 2577, 441
assert AIRPORTS_CR + HELI_CR + VGF_CR + OM_CR <= OUTLAY
OTHER_CR = OUTLAY - (AIRPORTS_CR + HELI_CR + VGF_CR + OM_CR)

# CAG performance audit, UDAN rounds 1-3, position to March 2023
CAG = [("Routes awarded", 774), ("Routes that started", 371),
       ("Completed 3 years of subsidy", 112), ("Still flying after subsidy ended", 54)]
# Rajya Sabha reply, position 10 Jul 2026
RS_OPS, RS_LIVE, RS_EARLY = 679, 348, 165
RS_DISC = RS_OPS - RS_LIVE
assert RS_DISC == 331
RS_LATE = RS_DISC - RS_EARLY
# PIB ten-year note, VGF to 15 Oct 2026
PIB_ROUTES, PIB_AERO, PIB_FLIGHTS, PIB_PAX, PIB_VGF = 687, 95, 3.68e5, 1.72e7, 5091.23
VGF_PER_PAX = PIB_VGF * 1e7 / PIB_PAX
VGF_PER_FLIGHT = PIB_VGF * 1e7 / PIB_FLIGHTS
PAX_PER_FLIGHT = PIB_PAX / PIB_FLIGHTS
OLD_YEARS = 9.5   # first UDAN flight April 2017 to October 2026
OLD_RATE = PIB_VGF / OLD_YEARS
NEW_RATE = VGF_CR / 10
# Support as a share of the full gap, by route year (Minister, July 2026)
OLD_TAPER = [100, 100, 100, 0, 0]
NEW_TAPER = [100, 100, 75, 50, 25]
OLD_SUM, NEW_SUM = sum(OLD_TAPER) / 100, sum(NEW_TAPER) / 100
assert (OLD_SUM, NEW_SUM) == (3.0, 3.5)


def chart_funnel():
    W, L, top, bh, gap, lab = 400, 10, 24, 20, 9, 176
    H = top + len(CAG) * (bh + gap) + 22
    sc = (W - L - lab - 70) / 774
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="UDAN routes in rounds one to three to March 2023: 774 awarded, 371 started, 112 completed three years of subsidy, 54 still flying after it ended.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">UDAN rounds 1&ndash;3: what happened to the routes</text>']
    cols = ["#868e96", "#1c5d99", "#1c5d99", "#a5402c"]
    for i, ((n, v), col) in enumerate(zip(CAG, cols)):
        y = top + i * (bh + gap)
        s.append(f'<text x="{L + lab - 6}" y="{y + 14}" font-size="10" fill="#212529" text-anchor="end">{n}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{v * sc:.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 14}" font-size="10" fill="#212529">{v} ({v / 774 * 100:.0f}%)</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">CAG performance audit of RCS-UDAN, position to March 2023.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_taper():
    W, L, top, ch = 400, 34, 34, 120
    bw, gw = 22, 64
    H = top + ch + 44
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Subsidy as a share of the route viability gap by year: old scheme 100% for three years then nothing; modified scheme 100%, 100%, 75%, 50%, 25%.">',
         f'<text x="10" y="12" font-size="12" fill="#495057">Airline subsidy by year of a route, % of the viability gap</text>',
         f'<rect x="10" y="20" width="9" height="9" fill="#868e96"/><text x="23" y="28" font-size="9.5" fill="#212529">Original UDAN (3 years)</text>',
         f'<rect x="150" y="20" width="9" height="9" fill="#a5402c"/><text x="163" y="28" font-size="9.5" fill="#212529">Modified UDAN (5 years, tapered)</text>']
    base = top + ch
    for pct in (0, 50, 100):
        y = base - pct / 100 * (ch - 10)
        s.append(f'<line x1="{L}" x2="{W - 10}" y1="{y:.1f}" y2="{y:.1f}" stroke="#dee2e6"/>')
        s.append(f'<text x="{L - 4}" y="{y + 3:.1f}" font-size="9" fill="#6c757d" text-anchor="end">{pct}</text>')
    for i, (o, n) in enumerate(zip(OLD_TAPER, NEW_TAPER)):
        x = L + 14 + i * gw
        for j, (v, col) in enumerate(((o, "#868e96"), (n, "#a5402c"))):
            h = v / 100 * (ch - 10)
            s.append(f'<rect x="{x + j * bw}" y="{base - h:.1f}" width="{bw - 2}" height="{max(h, 0.0):.1f}" fill="{col}"/>')
            s.append(f'<text x="{x + j * bw + bw / 2 - 1}" y="{base - h - 3:.1f}" font-size="8.5" fill="#212529" text-anchor="middle">{v}</text>')
        s.append(f'<text x="{x + bw - 1}" y="{base + 13}" font-size="9.5" fill="#212529" text-anchor="middle">Year {i + 1}</text>')
    s.append(f'<text x="10" y="{H - 16}" font-size="9" fill="#6c757d">Taper as stated by the Civil Aviation Minister, July 2026. Totals: {OLD_SUM:.1f} vs {NEW_SUM:.1f} years</text>')
    s.append(f'<text x="10" y="{H - 4}" font-size="9" fill="#6c757d">of full support; year three falls from 100% to 75%.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_outlay():
    rows = [
        ("Develop unserved airstrips into airports", f"{AIRPORTS_CR:,}", f"{AIRPORTS_N} airports over 8 years; about Rs {AIRPORTS_CR / AIRPORTS_N:.0f} crore each"),
        ("Helipads", f"{HELI_CR:,}", f"{HELI_N} helipads at Rs 15 crore each, adjusted for inflation over 8 years"),
        ("Viability gap funding (VGF) to airlines", f"{VGF_CR:,}", "Over 10 years; each route supported for up to 5 years, exclusivity still 3 years"),
        ("Operation and maintenance support", f"{OM_CR:,}", f"About {OM_N} aerodromes for 3 years; capped at Rs 3.06 crore a year an airport, Rs 0.90 crore a heliport or water aerodrome"),
    ]
    if OTHER_CR:
        rows.append(("Other, not itemised", f"{OTHER_CR:,}", "Not itemised among the four components the release lists"))
    rows.append(("<b>Total</b>", f"<b>{OUTLAY:,}</b>", "FY2026-27 to FY2035-36, from the Union budget"))
    return table(["Component", "Rs crore", "What it buys"], rows)


def t_counts():
    return table(["Source and date", "Routes", "What the count shows"], [
        ("CAG audit, rounds 1&ndash;3, to March 2023", "774 awarded", "403 (52%) never started; of 371 that did, 112 completed three years of subsidy and 54 (7% of awarded) were still flying after it ended"),
        ("Rajya Sabha reply, 10 July 2026", f"{RS_OPS} started", f"{RS_LIVE} flying; {RS_DISC} closed, {RS_EARLY} of them before their three years of subsidy ran out"),
        ("PIB ten-year note, October 2026", f"{PIB_ROUTES} started", f"{PIB_AERO} aerodromes (17 heliports, 2 water aerodromes); 3.68 lakh flights; 1.72 crore passengers; VGF paid Rs {PIB_VGF:,.2f} crore to 15 October"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{RS_DISC} of {RS_OPS}</b><span>UDAN routes that started had closed by July 2026; {RS_LIVE} were flying</span></div>
<div class="gb-stat"><b>{RS_EARLY}</b><span>of the closed routes shut while their subsidy was still being paid, about half of all closures</span></div>
<div class="gb-stat"><b>Rs {VGF_PER_PAX:,.0f}</b><span>of airline subsidy per UDAN passenger over ten years (Rs {PIB_VGF:,.0f} crore for 1.72 crore passengers)</span></div>
<div class="gb-stat"><b>Rs {VGF_CR:,} cr</b><span>set aside for airline subsidy in the next ten years, about twice the yearly rate so far</span></div>
</div>'''

body = f"""
{stats}

<p>This blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/09/india-is-piping-jet-fuel-to-five-new.html">piece on jet-fuel pipelines</a> noted that much of the new airport capacity India has added came through UDAN, the regional connectivity scheme, and that most of those airports still get their fuel by tanker truck. UDAN turned ten on 21 October. In March the Cabinet approved its successor, Modified UDAN, with Rs 28,840 crore for 2026-27 to 2035-36, and it was launched at Jodhpur on 4 July. The largest change for airlines is that a route&rsquo;s subsidy now lasts up to five years instead of three.</p>
<p>That change is a response to the scheme&rsquo;s main weakness: routes that close. This piece sets out what the new money buys, what the scheme&rsquo;s own counts show about route survival, and whether a longer, tapering subsidy addresses the way routes have actually failed.</p>

<h2 class="gb-h2">What Rs 28,840 crore buys</h2>
{t_outlay()}
<p>More than half the money goes to building and running airports and helipads rather than to flights. The airline subsidy, Rs {VGF_CR:,} crore over ten years, is about Rs {NEW_RATE:,.0f} crore a year. UDAN paid out Rs {PIB_VGF:,.0f} crore in the roughly {OLD_YEARS:g} years from its first flight in April 2017 to October 2026, about Rs {OLD_RATE:,.0f} crore a year, so the new scheme roughly doubles the yearly rate. It will also come from the budget rather than from the levy on flights on busy routes that funded the Centre&rsquo;s share of the original subsidy, as reported at launch. An airport now counts as unserved or underserved with up to 14 flights a week, up from 7, which widens the pool of routes that qualify.</p>

<h2 class="gb-h2">How routes have failed</h2>
{chart_funnel()}
<p>The Comptroller and Auditor General&rsquo;s audit of the first three bidding rounds is the most complete record. Of 774 routes awarded, 403 (52%) never started. Of the 371 that did, 112 had completed their three years of subsidy by March 2023, and only 54 of those were still flying afterwards. That is 7% of the routes awarded. Heliport routes did worse: 34 of 83 (41%) started.</p>
{t_counts()}
<p>The Rajya Sabha reply of July 2026 gives the latest position across all rounds: of {RS_OPS} routes that started, {RS_LIVE} were flying and {RS_DISC} had closed. The useful detail is when they closed. {RS_EARLY} closed before their three years of subsidy were over, and the other {RS_LATE} at or after the end of it. The reply lists low passenger demand, airlines&rsquo; marketing, public transport to the airport and the airport&rsquo;s distance from the towns it serves as reasons.</p>

<h2 class="gb-h2">What a five-year subsidy changes</h2>
{chart_taper()}
<p>The Civil Aviation Minister described the new support as tapered: the full viability gap in years one and two, then 75%, 50% and 25%. Over a route&rsquo;s life that is {NEW_SUM:.1f} years of full support against {OLD_SUM:.0f} before, about {(NEW_SUM / OLD_SUM - 1) * 100:.0f}% more. But it is spread more thinly. In year three a route now gets three-quarters of its gap covered, where it used to get all of it, and the drop from full support starts a year earlier.</p>
<p>Set against how routes have actually closed, that helps one group more than another. Routes that flew their three years and then stopped, {RS_LATE} of the {RS_DISC} closures, get a gentler end to support, which is what the change is designed for. The CAG&rsquo;s figures suggest this matters: of 112 routes that completed three years, 58 closed after the subsidy stopped. But the {RS_EARLY} routes that closed while still fully subsidised were not short of time on support. A longer taper does not help a route that cannot fill its seats when every seat is subsidised, and those routes would get less support in year three under the new terms, not more.</p>
<p>The cost per passenger shows the scale of what is being bought. Over ten years UDAN paid about Rs {VGF_PER_PAX:,.0f} of subsidy per passenger, about Rs {VGF_PER_FLIGHT / 1e5:.2f} lakh per flight, with an average of about {PAX_PER_FLIGHT:.0f} passengers a flight. Those are averages across aircraft from helicopters to 70-seaters and over routes that are flying and routes that closed, so they show the order of magnitude rather than the cost on any route.</p>

<h2 class="gb-h2">Where jet fuel comes in</h2>
<p>Fuel is typically a regional airline&rsquo;s largest single cost, and at most UDAN airports it is trucked in. To bring it down on UDAN routes, states were asked to cut value-added tax on jet fuel to 1% or less for ten years; Maharashtra, for example, set its 1% rate from 1 April 2017 for ten years, and Uttar Pradesh set zero for ten years in its 2017 aviation policy. Those ten-year concessions start running out in 2027, the first full year of Modified UDAN. If they lapse, a route&rsquo;s viability gap widens just as its subsidy starts to taper. The new pipelines in the earlier piece serve large airports; for the 100 new airports, fuel will again come by road unless the scheme plans for it.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>The Ministry of Civil Aviation should publish a route-level register: award date, start date, end date, aircraft, seats offered, load factor and VGF paid each year, so that survival can be measured by round, region and aircraft type rather than reconstructed from parliamentary answers.</li>
<li>Routes that close while still fully subsidised should trigger a review of the bid before the airport or the route is offered again, since a longer taper does not address them.</li>
<li>States should extend the jet-fuel VAT concession for UDAN routes to match the five-year support, and the Ministry should report which states have done so.</li>
<li>For each of the 100 new airports, the plan should say how fuel will be supplied and at what cost per kilolitre, alongside the runway and terminal.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>The Cabinet release, the PIB notes and the Rajya Sabha reply could not be opened directly; figures come from their text as indexed by search engines and from news and exam-preparation summaries. A Civil Aviation Ministry factsheet reported by IANS on 20 October gave 1.49 crore passengers and 625 routes, figures that match the scheme&rsquo;s April 2025 totals; this piece uses the October 2026 PIB figures (1.72 crore and {PIB_ROUTES}). The route counts differ slightly between sources ({RS_OPS} in July, {PIB_ROUTES} in October). How many of the {RS_LIVE} flying routes are still within their subsidy period, and how much of the Rs {PIB_VGF:,.0f} crore went to routes that later closed, is not published. The Rs {OTHER_CR:,} crore not itemised in the outlay table is the difference between the total and the four components the release lists.</p>
"""

sources = ("Modified UDAN: Cabinet decision of 25 March 2026 (PM India; PIB), as reported by The Pioneer, Morung Express, Governance Now, NBM&amp;CW and Vision IAS; launch at Jodhpur on 4 July 2026 and PIB document of 17 July 2026 (VGF up to five years, exclusivity three years); Civil Aviation Minister&rsquo;s description of the taper and the 14-flight threshold per IANS, Angel One and News Arena (July 2026); funding from the budget rather than the levy per The Logical Indian and Drishti IAS. "
           "Route survival: CAG performance audit of RCS-UDAN (rounds 1&ndash;3, to March 2023), as summarised by Drishti IAS and news reports; Rajya Sabha reply on routes operationalised, operating and discontinued as on 10 July 2026, as reported by The Daily Guardian and published by a member of Parliament (derek.in). "
           "Ten-year figures (687 routes, 95 aerodromes, 3.68 lakh flights, 1.72 crore passengers, VGF Rs 5,091.23 crore to 15 October 2026): PIB-based summaries via Drishti IAS (21 October 2026), Indian Masterminds and SuperKalam; the IANS-reported factsheet (1.49 crore passengers, 625 routes) via NewKerala and Telangana Today. "
           "Jet-fuel VAT concessions: Maharashtra trade circular (Taxsutra summary), Uttar Pradesh Civil Aviation Promotion Policy 2017 (Invest UP), Taxscan. "
           "Per-passenger, per-flight and yearly-rate figures and the taper totals are this blog&rsquo;s arithmetic. Nothing here is investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/09/india-is-piping-jet-fuel-to-five-new.html", "India Is Piping Jet Fuel to Five New Airports at Once. Only Six Had It Before"),
]

build("Scheme Delivery · 27 October 2026",
      "Half of UDAN&rsquo;s Closed Routes Shut While Still Subsidised. The New Scheme Pays for Longer",
      "Modified UDAN puts Rs 28,840 crore into regional flying over ten years and stretches each route&rsquo;s subsidy from three years to five, on a taper. Of 331 routes that had closed by July, 165 shut before their subsidy ran out, so a longer taper addresses only part of why routes fail.",
      body, sources, related, OUT)
print("other", OTHER_CR, "per pax", round(VGF_PER_PAX), "per flight", round(VGF_PER_FLIGHT), "pax/flight", round(PAX_PER_FLIGHT, 1), "old rate", round(OLD_RATE), "new", NEW_RATE, "late", RS_LATE)
