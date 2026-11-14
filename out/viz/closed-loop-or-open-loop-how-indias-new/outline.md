1.8–2.2 Lof water an open evaporative tower uses per kWh of IT load, by this blog’s physics

0.27 Lof water at the power plant for the extra electricity dry cooling needs, in the worst case

~50%of India’s operational data-centre capacity is in Mumbai, within 20 km of its cable landings

3 of 4gigawatt-scale projects in this piece’s table are on the coast, and each has chosen differently on water

Three of India’s largest announced data-centre campuses have each made a different choice about water. Google says its 1 GW AI hub in Visakhapatnam will use “advanced air cooling”, after its own assessment found pressure on the local watershed. Reliance’s first 168 MW in Jamnagar, leased to Meta, is reported to cool with desalinated seawater. In Thane, Amazon says its new site will use air-cooled chillers and almost no water, while the city has offered it 12 million litres a day of treated sewage. Maharashtra has meanwhile told data centres to run on treated wastewater, and in October set up a committee under Anil Kakodkar to assess their water use.

Behind these choices is one question, usually framed as “closed loop or open loop”. This piece explains what the terms mean, works out the water and energy each uses per unit of computing, maps the announced campuses against the coast and the subsea cables that pull them there, and recommends a design for each kind of site. It follows this blog’s [piece on where the gigawatt data-centre bets land](https://blog.vertistratsolution.com/2026/08/where-indias-gigawatt-data-centre-bets.html).

[kept verbatim: dated update notes]

## What “open” and “closed” actually mean


[T1 "What “open” and “closed” actually mean" 5 rows; use rows by number in a chart "table" spec]
  cols: c0 Design | c1 Loop | c2 Where the heat goes | c3 Water used on site
  r0: Open evaporative cooling tower | Open: water is sprayed through air | Mostly by evaporating water | About 1.8–2.2 litres per kWh of IT load, including blowdown
  r1: Once-through (seawater or river) | Open: water is drawn, warmed and returned | Into the sea or river, a few degrees warmer | Large withdrawal, little consumed; needs intake and outfall permits
  r2: Dry cooler or air-cooled chiller | Closed: sealed loop, no evaporation | Into the air through fans and fins | Near zero after the first fill
  r3: Adiabatic or hybrid cooler | Closed process loop; water sprayed only on hot hours | Air, with evaporative assist at peaks | A fraction of a tower’s, depending on hours of spraying
  r4: Direct-to-chip or immersion liquid cooling | Closed at the rack | Into whichever system above serves the building | Depends entirely on that system


Two things are easy to miss. First, “closed loop” often describes only the loop inside the building. A direct-to-chip liquid-cooled hall is closed at the rack, but the heat it collects still has to leave the site, and if it leaves through an open cooling tower the site still evaporates water. Microsoft’s “zero water for cooling” design, announced in 2024 and avoiding a projected 125 million litres a year per data centre, is closed at both ends, and Microsoft acknowledged that it raises energy use. Second, “open” covers two different things: a cooling tower, which consumes water by evaporating it, and once-through cooling, which borrows water and returns it warmer. Google’s Hamina centre in Finland pumps seawater through heat exchangers that cool a separate closed freshwater loop, and mixes the outflow so it returns at close to the sea’s temperature.

## The trade: water on site, or electricity

[chart: 
 Per kWh of IT load: water and cooling power 
 Water, litres (dry: at the power plant) 
 Cooling power, kWh × 10 
 Evaporative tower 
 
 water 
 2.19 L 
 
 cooling power 
 0.20 kWh 
 Dry cooling, compressors on 
 
 water 
 0.27 L 
 
 cooling power 
 0.33 kWh 
 Tower at 3 cycles of concentration; chiller COPs at ECBC 2017 minimums; 
 grid water 2.68 L/kWh at coal plants × 74.5% thermal share. This blog’s arithmetic. 
]

The water an evaporative tower uses follows from physics. Evaporating a litre of water near 30°C absorbs about 2.43 megajoules, and a kWh is 3.6 megajoules. A tower serving a water-cooled chiller has to reject the IT heat plus the chiller’s own work, about 1.16 kWh of heat per kWh of IT load, and does about 85% of that by evaporation: about 1.46 litres. Because evaporation leaves salts behind, some water has to be bled off. At three cycles of concentration the total is about 2.2 litres per kWh of IT load, and at six cycles about 1.8.

Dry cooling saves that water but costs electricity. At the minimum efficiencies in India’s Energy Conservation Building Code (2017), a large water-cooled chiller plant uses about 0.20 kWh, tower fans and pumps included, to remove a kWh of heat; an air-cooled chiller uses about 0.33 kWh. That is a penalty of 0.135 kWh per kWh of IT load when compressors run every hour, which is the worst case. India’s electricity is still about three-quarters thermal, and NTPC’s coal plants consumed 2.68 litres per kWh in 2023-24, so the extra electricity carries about 0.27 litres of water at the power plant.

So even in the worst case, dry cooling saves about 88% of the water once the power plant’s share is counted, and the water it does use is drawn in the coal belt rather than from a city’s reservoirs. The cost is energy. For 100 MW of IT load running at 70% on average, an open tower would use about 3.7 million litres a day; dry cooling with compressors would instead use about 83 GWh a year more electricity, about Rs 58 crore at an assumed Rs 7 a unit. That works out to Rs 491–636 for every kilolitre of water saved. Seawater desalination in Chennai has been costed at Rs 30–49 a kilolitre, and tertiary-treated sewage for industry at about Rs 45.

The worst case is avoidable. Modern AI chips are increasingly cooled by liquid at the chip, and ASHRAE’s classes allow facility water at up to 40°C or 45°C. A dry cooler can supply water a few degrees above the outside air temperature, so at those temperatures it can run without compressors on all but the hottest hours. An Uptime Institute briefing in April 2026 found that well-designed dry and adiabatic systems can match evaporative ones on energy across ASHRAE climate zones 2 to 6. Most of lowland India is in the hotter zones 0 and 1, outside that range, and a July 2026 preprint found dry cooling alone infeasible at design conditions in the hottest US desert cities. That is why the design temperature of the liquid loop matters more in India than the label on the cooling plant.

## How much water India’s data centres use is not known


[T2 "How much water India’s data centres use is not known" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Published figure | c1 Implied litres per kWh of IT load | c2 Comment
  r0: 1 MW of evaporative cooling uses 25–26 million litres a year (press and advocacy reports) | 2.9 at full load | Above the physics range; plausible with few cycles of concentration or humidification
  r1: A 30 MW facility can use about 780 million litres a year (this blog, earlier) | 3.0 at full load | Same source family as the line above
  r2: A 100 MW hyperscale facility uses nearly 2 million litres a day (CEEW, as reported) | 0.83 at full load | Consistent with a mostly air- or dry-cooled design
  r3: India’s data centres used about 150 billion litres in 2025 (CEEW) | 11 or more | On about 1.5 GW; likely includes water used to generate their electricity, which the summary does not say


The figures in circulation imply anything from under 1 to more than 11 litres per kWh. The physics puts evaporative cooling at about 1.8–2.2 and dry cooling near zero on site. The gap is a measurement problem: the Bureau of Indian Standards has adopted the international Water Usage Effectiveness metric (IS/ISO/IEC 30134-9:2022), but no state or central rule requires operators to report it.

## Where the campuses are, and why the coast matters

[chart: 
 Campus to nearest subsea cable landing, km 
 Coastal site 
 Inland site 
 Visakhapatnam 
 
 0 · Visakhapatnam 
 Navi Mumbai 
 
 17 · Mumbai 
 Thane 
 
 19 · Mumbai 
 Chennai (Siruseri) 
 
 29 · Chennai 
 Jamnagar 
 
 478 · Mumbai 
 Hyderabad 
 
 503 · Visakhapatnam 
 Greater Noida 
 
 1,146 · Mumbai 
 Great-circle distance between city centres; landing cities: Mumbai, Chennai, 
 Kochi, Thoothukudi, Visakhapatnam (cables planned). This blog’s arithmetic. 
]

India’s data centres cluster at its subsea cable landings. Mumbai held about half of operational capacity in the first half of 2026 (890 MW of 1,789 MW, per Cushman & Wakefield), and Chennai is second. Visakhapatnam is becoming a third landing hub, with Google’s America–India Connect cable due to land in the city where its campus is being built. Proximity to cables matters most for cloud and content services that serve users; AI training is far less sensitive to latency, which is why gigawatt campuses are also going inland to Hyderabad and Greater Noida.


[T3 "Where the campuses are, and why the coast matters" 8 rows; use rows by number in a chart "table" spec]
  cols: c0 Campus | c1 Site and nearest cable landing | c2 Announced size | c3 Cooling, as disclosed
  r0: Google, with AdaniConneX and Airtel | Visakhapatnam; coastal, cable landing in the city | About 1 GW; $15 bn; opens 2028 | “Advanced air cooling”, chosen after a watershed assessment; a public-interest case on water is before the Andhra Pradesh High Court
  r1: Reliance, leased to Meta | Jamnagar; coastal, 478 km to Mumbai | 168 MW first phase, within a 1 GW plan | Desalinated seawater for cooling, per reports of the June 2026 deal
  r2: TCS HyperVault (OpenAI first customer) | Hyderabad; inland, 503 km to Visakhapatnam | Up to 1 GW; Rs 70,000 crore | Direct-to-chip liquid cooling; “water-neutral design principles”, no figures
  r3: Navi Mumbai hub, seven projects | Navi Mumbai; coastal, 17 km to Mumbai | 4,040 MW (state assessment, as reported) | State condition: treated wastewater for operations, potable water for staff only
  r4: AWS, Balkum | Thane; coastal, 19 km to Mumbai | Rs 7,203 crore on 53.7 acres | Air-cooled chillers (as at its operating Indian sites); disclosed 125 kL a day, while the city has offered 12 MLD of treated sewage
  r5: Microsoft India South Central | Hyderabad; inland, 503 km to Visakhapatnam | Microsoft’s largest in India; live August 2026 | Not disclosed
  r6: AdaniConneX Chennai 1 / Sify Siruseri | Chennai; coastal, 29 km to Chennai | 400 MW campus (Adani); Sify has its own cable landing | Not disclosed
  r7: Yotta | Greater Noida; inland, 1,146 km to Mumbai | 250 MW project | Not disclosed


Capacity and cooling as announced or reported; none of these operators publishes water use for an Indian site. Distances are straight lines between city centres, not fibre routes.

The coast changes the cooling choice. Every coastal campus in the table has seawater next to it, which can cool a closed loop through a heat exchanger without any fresh water, or be desalinated for a tower. Desalination takes about 3.5 kWh per cubic metre, so feeding a tower with it adds about 0.0077 kWh per kWh of IT load, about a twentieth of dry cooling’s worst-case penalty. The constraints are permits and the sea itself: intake and outfall structures need coastal regulation zone clearance, coastal power plants are typically bound to discharge water no more than 7°C above the sea, and pipes foul and corrode. An IIT Bombay study modelled cooling a 100 MW centre with cold water from the deep ocean and reported energy savings of 79%, while noting that the long pipelines are costly to build and run. The same coast is also where the water stress is acute: Mumbai cut supply by 10% from 15 May 2026 with its lakes at 23% of capacity, and Chennai’s reservoirs ran almost dry in 2019.

## Recommendation


[T4 "Recommendation" 3 rows; use rows by number in a chart "table" spec]
  cols: c0 Site | c1 Recommended design | c2 Why
  r0: Coastal, at a cable landing (Mumbai, Navi Mumbai, Chennai, Visakhapatnam, Jamnagar) | Closed loop inside the building; reject heat to seawater, either once-through through a heat exchanger or via cooling towers fed with desalinated, seawater or treated-sewage make-up; never municipal drinking water | Non-potable water costs about Rs 30–50 a kL to produce; dry cooling with compressors costs the equivalent of about Rs 491–636 a kL of water saved
  r1: Inland and water-stressed (Hyderabad, Delhi-NCR, Pune, Bengaluru) | Direct-to-chip liquid cooling at warm facility-water temperatures (ASHRAE W40 or higher), dry coolers, adiabatic assist on the hottest hours using treated sewage; buy renewable power | Warm water lets dry coolers run without compressors for most hours, which removes most of the energy penalty; renewable power removes most of the off-site water
  r2: Any site, existing air-cooled halls | Keep closed-loop air-cooled chillers; raise supply temperatures and add economiser hours rather than converting to towers | Conversion would add on-site water use in exactly the cities with the tightest supply


Neither loop wins everywhere. On the coast, an open seawater loop serving a closed inner loop is the efficient answer, and the rule should be that no data centre cools with drinking water. Inland, the closed loop wins, but only if the building is designed for warm-water liquid cooling, so that dry coolers are not running compressors through an Indian summer. The one design that should not be built in either place is an open tower fed from a city’s potable supply.

## What would fix this

[kept verbatim, open: What would fix this; 4 items]

## What this piece could not establish

[kept verbatim, collapsed: What this piece could not establish]
