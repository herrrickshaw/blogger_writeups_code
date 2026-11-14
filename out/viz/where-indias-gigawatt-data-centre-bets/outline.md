The pattern in one line: India's AI data-centre build-out is concentrating in a handful of coastal and near-coastal clusters — Chennai above all — not because that's where power is cheapest, but because that's where the submarine cables that can actually move an AI-scale training dataset already come ashore. Land and power get a company into the game; a cable landing station gets its data out of the country fast enough to matter.

Chennai's advantage is under the sea as much as on land — six cables and 14.8 Tbps of capacity are why so many gigawatt-scale bets cluster here. [Chennai Port aerial view](https://commons.wikimedia.org/wiki/File:Chennai_Port_aerial_view.jpg), Saiphani02, CC BY-SA 4.0, via Wikimedia Commons.

[kept verbatim: dated update notes]

## 1. The number everyone's building toward

India's operational data-centre capacity is roughly 1.2–1.5 gigawatts today. Forecasts for 2030 disagree sharply — S&P Global's consensus range is 6–6.5 GW with a 9 GW bull case, Mordor Intelligence projects 15.21 GW by 2031, and a Jefferies estimate cited by industry trackers runs to 17 GW — but the one figure with an actual government commitment behind it is more concrete: the Ministry of Power built a projection of 13.56 GW of data-centre electricity demand by FY2031–32 directly into national transmission planning, published via the Press Information Bureau in March 2026. Whichever forecast turns out closest, every one of them describes a four-to-tenfold expansion inside five years, and private capital is already moving at that scale: Adani and Reliance alone have committed more than $210 billion combined to AI infrastructure and the renewable power to run it, through 2035.

## 2. Where the money is actually landing

The projects aren't spread evenly across India — they cluster around a short list of cities, each chosen for a specific mix of land availability, renewable power access, and, critically, proximity to a submarine cable landing station.


[T1 "2. Where the money is actually landing" 10 rows; use rows by number in a chart "table" spec]
  cols: c0 Company | c1 Location | c2 Capacity / commitment | c3 Status / timeline
  r0: Adani Group (AdaniConneX) | Chennai; land bank 1,000+ acres in Panvel, Maharashtra | $100bn by 2035; portfolio expanding 2 GW → 5 GW; Chennai 1 campus 400 MW with 200 MW integrated renewables | Chennai 1 commissioned Dec 2025, Tier 4 certified
  r1: Reliance Industries | Jamnagar, Gujarat; land holdings ~0.5 million acres nationally, 5,000+ acres in Navi Mumbai | ~$110–120bn AI-infrastructure commitment; Jamnagar phase 1 >120 MW | Announced Feb 2026; captive renewable-power model
  r2: Google (with Adani) | Bengaluru, Delhi-NCR, Mumbai; separately, Visakhapatnam, Andhra Pradesh | $15bn cloud-region alliance with Adani; separate $15bn Visakhapatnam project | First 80 MW site (Adani JV) due mid-2026
  r3: Microsoft | Hyderabad, Telangana | $17.5bn India commitment; Hyderabad region 100 MW → 150 MW | Expanded by 50 MW, January 2026, adding GPU clusters for Azure OpenAI
  r4: AWS | Mumbai | Mumbai availability zone expanded 40% | January 2025
  r5: Yotta Infrastructure | Greater Noida, Uttar Pradesh | 500 MW roadmap; Greater Noida project 250 MW (100 MW solar + 50 MW battery), existing 30 MW live | $200mn debt raised November 2025
  r6: NTT | Mumbai | 500 MW pre-funded | Ongoing
  r7: Nxtra (Bharti Airtel) | Multi-city | 800 MW footprint target | By 2028
  r8: Sify Technologies | Chennai (Siruseri) | 25.92 MW IT load, Chennai 02 campus; national renewable contracts of 309.6 MWp | Targeting 70% renewable-powered
  r9: CtrlS | Karnataka, Tamil Nadu, Uttar Pradesh; Hyderabad | Multi-MW builds; 15 MW replicable design, deployable in 9 months | Ongoing; direct-to-chip liquid cooling for 40 kW racks in Hyderabad


State-level policy is stacking incentives on top of this: Uttar Pradesh's Data Centre Policy 2026 targets 2 GW of capacity and ₹2 lakh crore of investment with capital and interest subsidies; Telangana has a stated vision for 5 GW by 2030; Maharashtra, Tamil Nadu, and Andhra Pradesh run comparable schemes.

## 3. Why Chennai keeps winning the location fight

The reason Chennai shows up so often in that table isn't coincidence: it's India's densest submarine-cable landing point, with six active cables offering a combined 14.8 Tbps of capacity, and it sits closer to the US West Coast than any other Indian landing city. Mumbai is the other major hub. Training and running large AI models means moving enormous, continuous volumes of data between compute clusters and, often, between countries — a single frontier-model training run can involve moving petabytes of data repeatedly between storage and GPU clusters, and hyperscalers serving global customers need low-latency routes out of India entirely. A data centre with cheap land and abundant power but no nearby cable landing station is still, in practical terms, an island.


[T2 "3. Why Chennai keeps winning the location fight" 6 rows; use rows by number in a chart "table" spec]
  cols: c0 Cable system | c1 Indian landing station(s) | c2 Capacity | c3 Notes
  r0: MIST (Myanmar/Malaysia/India/Singapore Transit) | Mumbai, Chennai | 216+ Tbps total (12 fibre pairs); 8,100 km length | Ready for service June 2025; Tata Communications bought 20 Tbps (1 fibre pair) for $63mn, June 2026; built by NEC for Orient Link Pte Ltd (NTT, JICT, WEN Capital)
  r1: i2i (Chennai–Singapore) | Chennai | 8.4 Tbps | Interconnects with C2C Cable Network, SEA-ME-WE 3, Asia Pacific Cable Network
  r2: SEA-ME-WE 4 | Chennai (Bharti Airtel), Mumbai (Tata Communications) | Added 5.12 Tbps into India | Connects onward to Singapore, the Gulf, and Europe
  r3: SEA-ME-WE 6 (upcoming) | Mumbai, Chennai | Not yet specified | Airtel to provide Express Route Landings at both cities
  r4: Bharat Lanka Cable System | Tuticorin, Tamil Nadu | Contributes to Tuticorin's 1 Tbps total landing capacity | 325 km, connects to Sri Lanka
  r5: Sify integrated Cable Landing Station | Chennai (Siruseri campus) | Up to 2 Pbps design capacity | Sited away from ports, fishing zones, oil blocks, and existing cable routes; built for transpacific fibre access


Chennai and Tuticorin together are why Tamil Nadu keeps appearing in the project table above — it isn't only a land-and-power story, it's a cable-landing story that predates the current AI build-out by well over a decade (i2i and the Tata Indicom Cable have served the Chennai–Singapore corridor for some 15 years) and is now being actively reinforced with new capacity purpose-built for hyperscale demand.

A data centre needs three things to actually compete for AI workloads: power, land, and a fast enough pipe out. India's current build-out is visibly sorting itself by all three at once — and the cable landing stations, the hardest of the three to relocate or duplicate quickly, are doing more to decide where the gigawatts land than most public commentary on the sector acknowledges.

## 4. What this doesn't fix

Cable capacity and campus announcements don't resolve the two constraints every source describing this build-out flags as the real bottleneck: transmission, not generation. India's data centres currently draw well under 1 per cent of national electricity (estimates range 0.5–0.8 per cent), so aggregate generation capacity isn't the near-term limit — the problem is that the specific substations serving Mumbai and the National Capital Region are approaching local capacity limits, and India's transmission and distribution losses, at 16.64 per cent, run more than double the global average. A hyperscale campus can secure land, a renewable power-purchase agreement, and a cable interconnect, and still be waiting on a substation upgrade. Water is the other quietly binding constraint in several of these same locations: a single 30 MW facility can consume close to 780 million litres of water a year for cooling, in states where water stress is already a live policy issue.

## What would fix this

[kept verbatim, open: What would fix this; 5 items]
