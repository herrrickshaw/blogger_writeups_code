import sys, runpy
sys.path.insert(0, '.')
from buildpost import build

OUT = '/home/user/blogger_writeups_code/out/post-data-centre-cooling-loops.html'
C = runpy.run_path('/home/user/blogger_writeups_code/out/research/dc-cooling/calc.py', run_name='calc')
wue, pen, offsite, e_wc, e_ac, km, LAND, SITES = C['wue'], C['pen'], C['offsite'], C['e_wc'], C['e_ac'], C['km'], C['LAND'], C['SITES']
W3, W6 = wue(3), wue(6)
TARIFF = C['TARIFF']
PER_KL = (pen * TARIFF / (W3 - offsite) * 1000, pen * TARIFF / (W6 - offsite) * 1000)
it_kwh = 100e3 * 8760 * 0.7
MLD100 = W3 * it_kwh / 365 / 1e6
GWH100 = pen * it_kwh / 1e6
CR100 = pen * it_kwh * TARIFF / 1e7


def dist(site):
    c = SITES[site]
    n = min(LAND, key=lambda k: km(c, LAND[k]))
    return n, km(c, LAND[n])

# campus, site key, announced capacity (MW, for the chart), capacity text, coastal, cooling as disclosed
CAMPUSES = [
    ("Google, with AdaniConneX and Airtel", "Visakhapatnam", 1000, "About 1 GW; $15 bn; opens 2028", True,
     "&ldquo;Advanced air cooling&rdquo;, chosen after a watershed assessment; a public-interest case on water is before the Andhra Pradesh High Court"),
    ("Reliance, leased to Meta", "Jamnagar", 1000, "168 MW first phase, within a 1 GW plan", True,
     "Desalinated seawater for cooling, per reports of the June 2026 deal"),
    ("TCS HyperVault (OpenAI first customer)", "Hyderabad", 1000, "Up to 1 GW; Rs 70,000 crore", False,
     "Direct-to-chip liquid cooling; &ldquo;water-neutral design principles&rdquo;, no figures"),
    ("Navi Mumbai hub, seven projects", "Navi Mumbai", 4040, "4,040 MW (state assessment, as reported)", True,
     "State condition: treated wastewater for operations, potable water for staff only"),
    ("AWS, Balkum", "Thane", 0, "Rs 7,203 crore on 53.7 acres", True,
     "Air-cooled chillers (as at its operating Indian sites); disclosed 125 kL a day, while the city has offered 12 MLD of treated sewage"),
    ("Microsoft India South Central", "Hyderabad", 0, "Microsoft&rsquo;s largest in India; live August 2026", False, "Not disclosed"),
    ("AdaniConneX Chennai 1 / Sify Siruseri", "Chennai (Siruseri)", 400, "400 MW campus (Adani); Sify has its own cable landing", True, "Not disclosed"),
    ("Yotta", "Greater Noida", 250, "250 MW project", False, "Not disclosed"),
]


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def t_terms():
    return table(["Design", "Loop", "Where the heat goes", "Water used on site"], [
        ("Open evaporative cooling tower", "Open: water is sprayed through air", "Mostly by evaporating water", f"About {W6:.1f}&ndash;{W3:.1f} litres per kWh of IT load, including blowdown"),
        ("Once-through (seawater or river)", "Open: water is drawn, warmed and returned", "Into the sea or river, a few degrees warmer", "Large withdrawal, little consumed; needs intake and outfall permits"),
        ("Dry cooler or air-cooled chiller", "Closed: sealed loop, no evaporation", "Into the air through fans and fins", "Near zero after the first fill"),
        ("Adiabatic or hybrid cooler", "Closed process loop; water sprayed only on hot hours", "Air, with evaporative assist at peaks", "A fraction of a tower&rsquo;s, depending on hours of spraying"),
        ("Direct-to-chip or immersion liquid cooling", "Closed at the rack", "Into whichever system above serves the building", "Depends entirely on that system"),
    ])


def chart_tradeoff():
    W, L, top, bh, gap, lab = 400, 10, 40, 16, 6, 140
    rows = [("Evaporative tower", W3, e_wc, "#1c5d99"), ("Dry cooling, compressors on", offsite, e_ac, "#a5402c")]
    H = top + 2 * (2 * bh + gap + 16) + 34
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Per kWh of IT load: an evaporative tower uses about {W3:.1f} litres of water on site and {e_wc:.2f} kWh for cooling; dry cooling with compressors running uses about {offsite:.2f} litres of water at the power plant and {e_ac:.2f} kWh.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Per kWh of IT load: water and cooling power</text>',
         f'<rect x="{L}" y="20" width="9" height="9" fill="#868e96"/><text x="{L + 13}" y="28" font-size="9.5" fill="#212529">Water, litres (dry: at the power plant)</text>',
         f'<rect x="{L + 200}" y="20" width="9" height="9" fill="#ced4da"/><text x="{L + 213}" y="28" font-size="9.5" fill="#212529">Cooling power, kWh &times; 10</text>']
    sc = (W - L - lab - 40) / 3.6
    y = top
    for n, w, e, col in rows:
        s.append(f'<text x="{L}" y="{y + 11}" font-size="10.5" font-weight="700" fill="{col}">{n}</text>')
        y += 16
        for v, fill, lbl in ((w, "#868e96", f"{w:.2f} L"), (e * 10, "#ced4da", f"{e:.2f} kWh")):
            s.append(f'<rect x="{L + lab}" y="{y}" width="{max(v * sc, 1.5):.1f}" height="{bh}" fill="{fill}"/>')
            s.append(f'<text x="{L + lab - 6}" y="{y + 12}" font-size="9.5" fill="#212529" text-anchor="end">{"water" if fill == "#868e96" else "cooling power"}</text>')
            s.append(f'<text x="{L + lab + v * sc + 4:.1f}" y="{y + 12}" font-size="9.5" fill="#212529">{lbl}</text>')
            y += bh + 4
        y += gap
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Tower at 3 cycles of concentration; chiller COPs at ECBC 2017 minimums;</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">grid water 2.68 L/kWh at coal plants &times; 74.5% thermal share. This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def chart_distance():
    rows = []
    for name, site, mw, cap, coastal, cool in CAMPUSES:
        if site in [r[0] for r in rows]:
            continue
        n, d = dist(site)
        rows.append((site, d, n, coastal))
    rows.sort(key=lambda r: r[1])
    W, L, top, bh, gap, lab = 400, 10, 36, 15, 7, 112
    H = top + len(rows) * (bh + gap) + 34
    sc = (W - L - lab - 110) / 1150
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Straight-line distance from announced data-centre campuses to the nearest subsea cable landing city.">',
         f'<text x="{L}" y="12" font-size="12" fill="#495057">Campus to nearest subsea cable landing, km</text>',
         f'<rect x="{L}" y="20" width="9" height="9" fill="#1c5d99"/><text x="{L + 13}" y="28" font-size="9.5" fill="#212529">Coastal site</text>',
         f'<rect x="{L + 90}" y="20" width="9" height="9" fill="#a5402c"/><text x="{L + 103}" y="28" font-size="9.5" fill="#212529">Inland site</text>']
    for i, (site, d, n, coastal) in enumerate(rows):
        y = top + i * (bh + gap)
        col = "#1c5d99" if coastal else "#a5402c"
        s.append(f'<text x="{L + lab - 6}" y="{y + 11}" font-size="10" fill="#212529" text-anchor="end">{site}</text>')
        s.append(f'<rect x="{L + lab}" y="{y}" width="{max(d * sc, 2):.1f}" height="{bh}" fill="{col}"/>')
        s.append(f'<text x="{L + lab + max(d * sc, 2) + 4:.1f}" y="{y + 11}" font-size="9.5" fill="#212529">{d:,.0f} &middot; {n}</text>')
    s.append(f'<text x="{L}" y="{H - 16}" font-size="9" fill="#6c757d">Great-circle distance between city centres; landing cities: Mumbai, Chennai,</text>')
    s.append(f'<text x="{L}" y="{H - 4}" font-size="9" fill="#6c757d">Kochi, Thoothukudi, Visakhapatnam (cables planned). This blog&rsquo;s arithmetic.</text>')
    s.append('</svg>')
    return '<figure class="gb-figure" style="margin:1.4rem 0">' + "\n".join(s) + '</figure>'


def t_campuses():
    rows = []
    for name, site, mw, cap, coastal, cool in CAMPUSES:
        n, d = dist(site)
        where = f"{site.replace(' (Siruseri)', '')}; {'coastal' if coastal else 'inland'}, {d:,.0f} km to {n}" if d > 1 else f"{site}; coastal, cable landing in the city"
        rows.append((name, where, cap, cool))
    return table(["Campus", "Site and nearest cable landing", "Announced size", "Cooling, as disclosed"], rows)


def t_estimates():
    return table(["Published figure", "Implied litres per kWh of IT load", "Comment"], [
        ("1 MW of evaporative cooling uses 25&ndash;26 million litres a year (press and advocacy reports)", f"{25.5e6 / 8760e3:.1f} at full load", "Above the physics range; plausible with few cycles of concentration or humidification"),
        ("A 30 MW facility can use about 780 million litres a year (this blog, earlier)", f"{780e6 / (30e3 * 8760):.1f} at full load", "Same source family as the line above"),
        ("A 100 MW hyperscale facility uses nearly 2 million litres a day (CEEW, as reported)", f"{2e6 / (100e3 * 24):.2f} at full load", "Consistent with a mostly air- or dry-cooled design"),
        ("India&rsquo;s data centres used about 150 billion litres in 2025 (CEEW)", f"{150e9 / (1.5e6 * 8760):.0f} or more", "On about 1.5 GW; likely includes water used to generate their electricity, which the summary does not say"),
    ])


def t_reco():
    return table(["Site", "Recommended design", "Why"], [
        ("Coastal, at a cable landing (Mumbai, Navi Mumbai, Chennai, Visakhapatnam, Jamnagar)",
         "Closed loop inside the building; reject heat to seawater, either once-through through a heat exchanger or via cooling towers fed with desalinated, seawater or treated-sewage make-up; never municipal drinking water",
         f"Non-potable water costs about Rs 30&ndash;50 a kL to produce; dry cooling with compressors costs the equivalent of about Rs {PER_KL[0]:,.0f}&ndash;{PER_KL[1]:,.0f} a kL of water saved"),
        ("Inland and water-stressed (Hyderabad, Delhi-NCR, Pune, Bengaluru)",
         "Direct-to-chip liquid cooling at warm facility-water temperatures (ASHRAE W40 or higher), dry coolers, adiabatic assist on the hottest hours using treated sewage; buy renewable power",
         "Warm water lets dry coolers run without compressors for most hours, which removes most of the energy penalty; renewable power removes most of the off-site water"),
        ("Any site, existing air-cooled halls",
         "Keep closed-loop air-cooled chillers; raise supply temperatures and add economiser hours rather than converting to towers",
         "Conversion would add on-site water use in exactly the cities with the tightest supply"),
    ])


stats = f'''<div class="gb-stats">
<div class="gb-stat"><b>{W6:.1f}&ndash;{W3:.1f} L</b><span>of water an open evaporative tower uses per kWh of IT load, by this blog&rsquo;s physics</span></div>
<div class="gb-stat"><b>{offsite:.2f} L</b><span>of water at the power plant for the extra electricity dry cooling needs, in the worst case</span></div>
<div class="gb-stat"><b>~50%</b><span>of India&rsquo;s operational data-centre capacity is in Mumbai, within 20 km of its cable landings</span></div>
<div class="gb-stat"><b>3 of 4</b><span>gigawatt-scale projects in this piece&rsquo;s table are on the coast, and each has chosen differently on water</span></div>
</div>'''

body = f"""
{stats}

<p>Three of India&rsquo;s largest announced data-centre campuses have each made a different choice about water. Google says its 1 GW AI hub in Visakhapatnam will use &ldquo;advanced air cooling&rdquo;, after its own assessment found pressure on the local watershed. Reliance&rsquo;s first 168 MW in Jamnagar, leased to Meta, is reported to cool with desalinated seawater. In Thane, Amazon says its new site will use air-cooled chillers and almost no water, while the city has offered it 12 million litres a day of treated sewage. Maharashtra has meanwhile told data centres to run on treated wastewater, and in October set up a committee under Anil Kakodkar to assess their water use.</p>
<p>Behind these choices is one question, usually framed as &ldquo;closed loop or open loop&rdquo;. This piece explains what the terms mean, works out the water and energy each uses per unit of computing, maps the announced campuses against the coast and the subsea cables that pull them there, and recommends a design for each kind of site. It follows this blog&rsquo;s <a href="https://masaladeutsch.blogspot.com/2026/08/where-indias-gigawatt-data-centre-bets.html">piece on where the gigawatt data-centre bets land</a>.</p>

<h2 class="gb-h2">What &ldquo;open&rdquo; and &ldquo;closed&rdquo; actually mean</h2>
{t_terms()}
<p>Two things are easy to miss. First, &ldquo;closed loop&rdquo; often describes only the loop inside the building. A direct-to-chip liquid-cooled hall is closed at the rack, but the heat it collects still has to leave the site, and if it leaves through an open cooling tower the site still evaporates water. Microsoft&rsquo;s &ldquo;zero water for cooling&rdquo; design, announced in 2024 and avoiding a projected 125 million litres a year per data centre, is closed at both ends, and Microsoft acknowledged that it raises energy use. Second, &ldquo;open&rdquo; covers two different things: a cooling tower, which consumes water by evaporating it, and once-through cooling, which borrows water and returns it warmer. Google&rsquo;s Hamina centre in Finland pumps seawater through heat exchangers that cool a separate closed freshwater loop, and mixes the outflow so it returns at close to the sea&rsquo;s temperature.</p>

<h2 class="gb-h2">The trade: water on site, or electricity</h2>
{chart_tradeoff()}
<p>The water an evaporative tower uses follows from physics. Evaporating a litre of water near 30&deg;C absorbs about 2.43 megajoules, and a kWh is 3.6 megajoules. A tower serving a water-cooled chiller has to reject the IT heat plus the chiller&rsquo;s own work, about {C['heat']:.2f} kWh of heat per kWh of IT load, and does about 85% of that by evaporation: about {C['evap']:.2f} litres. Because evaporation leaves salts behind, some water has to be bled off. At three cycles of concentration the total is about {W3:.1f} litres per kWh of IT load, and at six cycles about {W6:.1f}.</p>
<p>Dry cooling saves that water but costs electricity. At the minimum efficiencies in India&rsquo;s Energy Conservation Building Code (2017), a large water-cooled chiller plant uses about {e_wc:.2f} kWh, tower fans and pumps included, to remove a kWh of heat; an air-cooled chiller uses about {e_ac:.2f} kWh. That is a penalty of {pen:.3f} kWh per kWh of IT load when compressors run every hour, which is the worst case. India&rsquo;s electricity is still about three-quarters thermal, and NTPC&rsquo;s coal plants consumed 2.68 litres per kWh in 2023-24, so the extra electricity carries about {offsite:.2f} litres of water at the power plant.</p>
<p>So even in the worst case, dry cooling saves about {(W3 - offsite) / W3 * 100:.0f}% of the water once the power plant&rsquo;s share is counted, and the water it does use is drawn in the coal belt rather than from a city&rsquo;s reservoirs. The cost is energy. For 100 MW of IT load running at 70% on average, an open tower would use about {MLD100:.1f} million litres a day; dry cooling with compressors would instead use about {GWH100:.0f} GWh a year more electricity, about Rs {CR100:.0f} crore at an assumed Rs {TARIFF:.0f} a unit. That works out to Rs {PER_KL[0]:,.0f}&ndash;{PER_KL[1]:,.0f} for every kilolitre of water saved. Seawater desalination in Chennai has been costed at Rs 30&ndash;49 a kilolitre, and tertiary-treated sewage for industry at about Rs 45.</p>
<p>The worst case is avoidable. Modern AI chips are increasingly cooled by liquid at the chip, and ASHRAE&rsquo;s classes allow facility water at up to 40&deg;C or 45&deg;C. A dry cooler can supply water a few degrees above the outside air temperature, so at those temperatures it can run without compressors on all but the hottest hours. An Uptime Institute briefing in April 2026 found that well-designed dry and adiabatic systems can match evaporative ones on energy across ASHRAE climate zones 2 to 6. Most of lowland India is in the hotter zones 0 and 1, outside that range, and a July 2026 preprint found dry cooling alone infeasible at design conditions in the hottest US desert cities. That is why the design temperature of the liquid loop matters more in India than the label on the cooling plant.</p>

<h2 class="gb-h2">How much water India&rsquo;s data centres use is not known</h2>
{t_estimates()}
<p>The figures in circulation imply anything from under 1 to more than 11 litres per kWh. The physics puts evaporative cooling at about {W6:.1f}&ndash;{W3:.1f} and dry cooling near zero on site. The gap is a measurement problem: the Bureau of Indian Standards has adopted the international Water Usage Effectiveness metric (IS/ISO/IEC 30134-9:2022), but no state or central rule requires operators to report it.</p>

<h2 class="gb-h2">Where the campuses are, and why the coast matters</h2>
{chart_distance()}
<p>India&rsquo;s data centres cluster at its subsea cable landings. Mumbai held about half of operational capacity in the first half of 2026 (890 MW of 1,789 MW, per Cushman &amp; Wakefield), and Chennai is second. Visakhapatnam is becoming a third landing hub, with Google&rsquo;s America&ndash;India Connect cable due to land in the city where its campus is being built. Proximity to cables matters most for cloud and content services that serve users; AI training is far less sensitive to latency, which is why gigawatt campuses are also going inland to Hyderabad and Greater Noida.</p>
{t_campuses()}
<p class="gb-note">Capacity and cooling as announced or reported; none of these operators publishes water use for an Indian site. Distances are straight lines between city centres, not fibre routes.</p>
<p>The coast changes the cooling choice. Every coastal campus in the table has seawater next to it, which can cool a closed loop through a heat exchanger without any fresh water, or be desalinated for a tower. Desalination takes about 3.5 kWh per cubic metre, so feeding a tower with it adds about {C['wue'](3) / 1000 * 3.5:.4f} kWh per kWh of IT load, about a twentieth of dry cooling&rsquo;s worst-case penalty. The constraints are permits and the sea itself: intake and outfall structures need coastal regulation zone clearance, coastal power plants are typically bound to discharge water no more than 7&deg;C above the sea, and pipes foul and corrode. An IIT Bombay study modelled cooling a 100 MW centre with cold water from the deep ocean and reported energy savings of 79%, while noting that the long pipelines are costly to build and run. The same coast is also where the water stress is acute: Mumbai cut supply by 10% from 15 May 2026 with its lakes at 23% of capacity, and Chennai&rsquo;s reservoirs ran almost dry in 2019.</p>

<h2 class="gb-h2">Recommendation</h2>
{t_reco()}
<p>Neither loop wins everywhere. On the coast, an open seawater loop serving a closed inner loop is the efficient answer, and the rule should be that no data centre cools with drinking water. Inland, the closed loop wins, but only if the building is designed for warm-water liquid cooling, so that dry coolers are not running compressors through an Indian summer. The one design that should not be built in either place is an open tower fed from a city&rsquo;s potable supply.</p>

<h2 class="gb-h2">What would fix this</h2>
<ul>
<li>States hosting data centres should require annual reporting of Water Usage Effectiveness under IS/ISO/IEC 30134-9, split by source (potable, groundwater, treated sewage, seawater, desalinated), together with PUE, for every site above 5 MW.</li>
<li>&ldquo;Closed loop&rdquo; and &ldquo;zero water&rdquo; claims in project approvals should state how heat leaves the site, not only how it leaves the rack.</li>
<li>Coastal states should set out a clearance route for seawater intake and outfall for data centres, with a discharge temperature limit and monitoring, so that seawater cooling is a practical alternative to municipal water.</li>
<li>Maharashtra&rsquo;s Kakodkar committee, due to report within three months of its October order, should publish the water allocation for each data-centre hub and the source it comes from.</li>
</ul>
<p class="gb-note">These are proposals from this blog, not recommendations any agency has adopted.</p>

<h2 class="gb-h2">What this piece could not establish</h2>
<p>No Indian operator publishes site-level water or cooling energy, so the comparison rests on physics and code-minimum efficiencies rather than measured plants; real towers and chillers can do better than the code minimums. Hourly weather data for Indian cities could not be obtained for this piece, so it does not estimate how many hours a year dry coolers could run without compressors in each city. The Rs 30&ndash;49 desalination and Rs 45 treated-sewage costs are older Chennai estimates, and the Rs {TARIFF:.0f} electricity tariff is an assumption. Maharashtra&rsquo;s 4,040 MW Navi Mumbai figure and the water demand attached to it come from a syndicated report of a state assessment that could not be opened. Several sources, including government releases, could not be opened directly and were read through search-engine text and news reports.</p>
"""

sources = ("Cooling choices: Google on Visakhapatnam air cooling and the Andhra Pradesh High Court case (Kuwait Times, Gulf News, Malay Mail, TechEnclave, October 2026); Reliance&ndash;Meta Jamnagar 168 MW and desalinated seawater (pv magazine India, The Next Web, Zerodha Daily Brief, June 2026); Amazon&rsquo;s Indian sites and the Thane project (aboutamazon.in; Business Today, August 2026; Free Press Journal; Drishti IAS); TCS HyperVault (The News Minute, Swarajya, September 2026); Microsoft Hyderabad region (Indian Infrastructure, August 2026); Maharashtra conditions and the Kakodkar committee (Free Press Journal, June 2026; Telangana Today, October 2026). "
           "Design references: Microsoft zero-water design (Microsoft via ITPro, Data Centre Magazine, 2024); Google Hamina (DatacenterDynamics, Trellis); Uptime Institute Briefing Report 200 (April 2026, public summary); arXiv 2606.21760 and 2607.22617 and an engrXiv preprint (July 2026); ASHRAE liquid-cooling classes (Upsite, DatacenterDynamics); ECBC 2017 chiller minimums (secondary summaries of the BEE code); IIT Bombay deep-seawater cooling study (IIT Bombay research highlight; The Week, August 2025). "
           "Water and power: NTPC specific water consumption 2023-24 (NTPC Brighter Plan 2032); MoEFCC water norms for thermal plants (Lok Sabha replies, 2018); thermal share of generation 2024-25 (CERC market monitoring report, from CEA); thermal discharge condition (Adani Power Mundra compliance reports); BIS WUE standard (BIS; Schneider Electric blog; India Briefing); CEEW on data-centre water (CEEW; Analytics India Magazine); Jal Shakti reply on capacity and cooling (The Hitavada, May 2026); Chennai desalination and treated-water costs (Wikipedia citing CMWSSB; Swarajya); Mumbai water cut (The Week, May 2026). "
           "Capacity by city: Cushman &amp; Wakefield H1 2026 and MeitY (March 2026), as reported; cable landings (Shankar IAS, Civilsdaily, Drishti IAS, 2026). "
           "Litres and kWh per kWh of IT load, the cost per kilolitre saved and distances are this blog&rsquo;s arithmetic (method and inputs in the repository at out/research/dc-cooling/calc.py). Nothing here is investment or engineering advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/where-indias-gigawatt-data-centre-bets.html", "Where India&rsquo;s Gigawatt Data-Centre Bets Actually Land: Projects, Cables, and the $210 Billion Behind Them"),
    ("https://masaladeutsch.blogspot.com/2026/08/the-water-bill-nobody-mentions-what.html", "The Water Bill Nobody Mentions: What Taiwan&rsquo;s Chip Crisis Says About India&rsquo;s Fab Plans"),
]

build("Data Centres · 27 October 2026",
      "Closed Loop or Open Loop? How India&rsquo;s New Data Centres Should Be Cooled, Site by Site",
      "An open cooling tower uses about two litres of water per kWh of computing; a closed dry loop uses almost none but costs more power. Most of India&rsquo;s big new campuses sit on the coast near subsea cables, where seawater changes the answer.",
      body, sources, related, OUT)
