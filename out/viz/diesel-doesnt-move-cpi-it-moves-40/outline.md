Revised 6 August 2026 · v2.2.0

A diesel-dispensing fuel station in Kerala — the retail side of the ₹40-per-litre direct-sales/retail gap this piece traces through fifteen years of price data. [Bharat Petroleum Fuel Filling Station Chengannor](https://commons.wikimedia.org/wiki/File:Bharat_Petroleum_Fuel_Filling_Station_Chengannor_(Joseph_Joseph).jpg), Dr. Chinchu C., CC BY-SA 3.0, via Wikimedia Commons.

+0.11Correlation, diesel WPI growth vs CPI headline growth, FY2012–FY2026

>₹40Per-litre gap between direct-sales and retail diesel, PPAC, May 2026

43.3%Diesel’s share of India’s total petroleum product market, May 2026

−34.7%Private oil marketing companies’ diesel sales, May 2026, year on year

Correction, 22 October 2026. The source lines below described the wholesale price series as “rebased 2022-23 = 100”. The FY2012–FY2026 series used here are the 2011-12-base indices, which ran from April 2012 to April 2026; the official 2022-23-base series starts only in April 2023. The labels have been corrected. The correlations are calculated from year-on-year growth rates, so the base does not change them, and the findings stand. Nothing else has changed.

[kept verbatim: dated update notes]

## The claim

Everyone knows diesel drives inflation. The data does not.

The argument is intuitive enough that it rarely gets tested. Diesel moves freight; freight moves food; food moves the consumer price index. Therefore holding diesel prices down holds inflation down. It appears in market commentary as settled fact — one widely-read explainer walks through the entire chain, from tractors to irrigation to the Reserve Bank’s rate stance, without offering a single pass-through estimate, basket weight or citation.

So we tested it against fifteen years of official series: wholesale price indices for diesel, urea and DAP from DPIIT’s Office of the Economic Adviser, consumer price indices from MoSPI, April-anchored, FY2012 through FY2026.

Exhibit 1

Diesel tracks the wholesale index almost perfectly, and the retail index barely at all

Pearson correlation of year-on-year growth rates, April anchor, n = 15 years


[T1 "The claim" 5 rows; use rows by number in a chart "table" spec]
  cols: c0 Pair | c1 r | c2 Reading
  r0: Diesel vs WPI headline | +0.92 | Mechanical — diesel is a WPI component
  r1: WPI headline vs CPI headline | +0.25 | Weak wholesale-to-retail link
  r2: Diesel vs CPI headline | +0.11 | Essentially nothing
  r3: Diesel vs CPI food | −0.16 | Wrong sign
  r4: Diesel (t) vs CPI food (t+1) | +0.09 | The lag does not rescue it


Source: WPI — DPIIT/Office of the Economic Adviser, base 2011-12 = 100, April 2012 to April 2026. CPI — MoSPI. Author’s calculation on April-anchored annual growth rates.

The +0.92 is not evidence of transmission. Diesel sits inside the wholesale index, so the index partly measures diesel by construction. The number that would matter is diesel against retail inflation, and it is +0.11 — indistinguishable from noise. Against food inflation specifically, where the freight story is supposed to be strongest, the sign is negative. Lagging diesel by a year, which is how a cost shock would plausibly reach the shelf, gives +0.09.

What this test can and cannot settle. Fifteen annual observations cannot see a pass-through that operates over weeks; monthly data would be a fairer test. Neither series is controlled for crude, so diesel and food could co-move simply because both follow Brent. And there is a peer-reviewed study on precisely this question — Ghosh, Impact of India’s diesel subsidy reforms and pricing policy on growth and inflation, Energy Economics 113 (2022) — which we have not been able to read. If it finds transmission at higher frequency, the finding here is a frequency artefact. Treat this as a null result at annual frequency, not a settled fact.

## What is actually happening

Two prices for one fuel, forty rupees apart

If diesel’s wholesale signal is not reaching retail prices, something is absorbing it. PPAC’s Industry Consumption Report for May 2026 says what.

Diesel sold directly by oil marketing companies to bulk buyers — industry, railways, mining, shipping — is priced more than ₹40 per litre above the same fuel at a retail pump. Bulk buyers have responded exactly as anyone would: they buy at the pump instead.

Exhibit 2

The direct-sales channel is collapsing into the retail channel

Diesel sales by channel and by seller, April–May 2026 against April–May 2025


[T2 "What is actually happening" 6 rows; use rows by number in a chart "table" spec]
  cols: c0 Measure | c1 Apr–May 2025 | c2 Apr–May 2026
  r0: Retail share of diesel (%) | 88 | 92
  r1: Direct-sales share (%) | 12 | 8
  r2: Direct-sales volume (TMT) | 2,090 | 1,411
  r3: PSU OMC market share (%) | 87.3 | 91.8
  r4: PSU sales growth, May (%) | — | +6.9
  r5: Private OMC sales growth, May (%) | — | −34.7


Source: PPAC, Industry Consumption Report POL & NG, May 2026. PSU share gain of 4.54 percentage points as stated in the report.

A ₹40 gap between two channels for an identical commodity is not a market outcome. It is the visible edge of an administered retail price, measured against a channel left closer to cost. Private marketers, who have no obligation to sell below cost and no PSU balance sheet to absorb the difference, lost more than a third of their volume in a single year.

This is the strongest available evidence that Indian retail diesel is held below cost-reflective levels. It is a current, official, unambiguous number, and it does not depend on a correlation. It also reframes the policy question. Price control is real and large. Its observable effect is not a lower CPI print — it is channel arbitrage and the retreat of private competition.

## Where the fuel goes

Diesel is a freight fuel, and the freight is growing faster than the fuel

Diesel remains India’s dominant petroleum product at 43.3% of the market. May 2026 consumption was 8.73 million tonnes, up 1.6% year on year; the April–May total was 17.06 MMT, up 1.2%.

That is modest growth, and it sits oddly beside every proxy for freight activity in the same report.

Exhibit 3

Freight indicators are running three to seven times faster than diesel demand

Year-on-year growth, May 2026


[T3 "Where the fuel goes" 5 rows; use rows by number in a chart "table" spec]
  cols: c0 Indicator | c1 Growth (%)
  r0: E-way bills generated | +11.0
  r1: Commercial vehicle sales | +5.3
  r2: Major-port cargo throughput | +4.5
  r3: Tractor sales | +11.2
  r4: Diesel consumption | +1.6


Source: PPAC Industry Consumption Report, May 2026, drawing on GSTN (e-way bills, 1,360.79 lakh in May), FADA (vehicle sales) and ipa.nic.in (port cargo, 153.91 MMT).

Goods are moving considerably faster than diesel is being burnt. Some of that is efficiency and some is a shift to rail — railways rose from 9% to 12% of direct-sales diesel over the year. But the gap is wide enough to be worth naming as an open question rather than explaining away, and it is the natural place to ask what else could be carrying freight.

A caution on the sectoral numbers. PPAC publishes an end-use breakdown for direct sales only — that is 8% of diesel, and the channel shrank by a third this year, so its internal shares shift for composition reasons rather than demand reasons. Within that 8%: road transport 27%, miscellaneous industry 22%, mining and quarrying 18%, railways 12%, shipping 10%, manufacturing 7%, agriculture 2%, power generation 2%. The last economy-wide end-use survey is the PPAC/Nielsen study of 2,000-plus retail outlets across 16 states — whose fieldwork ran from January 2012 to June 2013. It found transport at about 70% of diesel, with heavy and light commercial vehicles at 28.25%, buses 9.55% and agriculture 13%. Those proportions are thirteen years old, they predate the collapse of the diesel passenger car after BS-VI, and they predate diesel deregulation in October 2014. Use them for structure; do not quote them as today’s levels.

## The leakage

A price gap on a bulk liquid is an invitation

Arbitrage on a commodity does not stay theoretical. When the same litre is worth ₹40 more depending on who is buying it, and a second subsidised liquid exists that looks similar in a tank, the incentive to move fuel between categories is substantial.

Both halves of that incentive appear in the same PPAC report. The ₹40 gap is one. The other is kerosene: subsidised PDS kerosene accounted for 73% of kerosene consumption in May 2026, against 27% non-PDS. Kerosene is the classic diesel adulterant.

The enforcement record is consistent with it. In Bengaluru in 2025, the Central Crime Branch arrested four people siphoning diesel destined for BMTC and KSRTC bus depots, seizing roughly 60,000 litres from three tankers; the method was to draw about 50 litres from each tanker in transit using duplicate keys and report the shortfall to depot managers as spillage. In Udupi, a tanker driver was arrested with 1,020 litres recovered, charged under the Bharatiya Nyaya Sanhita, the Essential Commodities Act 1955 and the Petroleum Act. The central government has separately directed state chief secretaries to act against fuel adulteration.

No national figure exists, and we are not going to invent one. These are individual seizures reported in the press, not a measured rate. They establish that the mechanism operates; they say nothing about its scale. A defensible national estimate would have to come from CAG audits of state transport undertakings, whose fuel-consumption-per-kilometre variances are auditable. We have not obtained those.

## The recommendation

Convert the depot-based fleet; close the wedge; do not cut the retail price

Three independent lines of evidence point at the same segment of demand.

Structure. Heavy and light commercial vehicles plus buses were roughly 38% of diesel in the last economy-wide survey — the largest single block, and the one least likely to have shrunk since.

Feasibility. That segment is depot-based and route-bound. Refuelling infrastructure for compressed natural gas is tractable where vehicles return to a known point each night, and intractable where they do not. Agriculture, at around 13% of diesel, is dispersed and seasonal; it is the wrong target. Private diesel cars are solving themselves.

Leakage. Compressed gas is physically far harder to divert than a liquid. It cannot be siphoned into a can, decanted at the roadside, or blended with kerosene. It is dispensed under pressure into a sealed, metered vessel. For state transport undertakings and municipal fleets — exactly the buyers in the Bengaluru case — conversion removes a whole category of loss alongside the emissions case.

Which leaves the price question, and here the evidence cuts against the obvious ask. Arguing for a cut in retail diesel prices is arguing against PPAC’s own report. Retail diesel already sits ₹40 below the unregulated channel. Cutting it further would widen the arbitrage that drives diversion, deepen the fiscal absorption, and weaken the economics of every fleet considering a switch.

The coherent ask is different: close the tax wedge on commercial fleet fuel while converting those fleets to gas. That shrinks the arbitrage from both ends — a smaller gap to exploit, and a fuel that is harder to exploit it with — and it preserves the relative advantage that makes conversion worth financing.

The dependency this does not solve. Gas is not an escape from imports. India’s crude import dependency reached 88.2% in FY2024-25 and self-sufficiency in products from indigenous crude fell to 11.8%. But domestic gas production also fell 0.9% while LNG imports rose 15.4%. A diesel-to-CNG shift swaps one import exposure for another, partly rupee-denominated one. It is a better exposure — but it should be argued as a swap, not an escape.

## The stationary segment

Generators and telecom towers burn diesel that never moves

The freight argument above concerns diesel that travels. A second block does not move at all, and it is the easier conversion.

Exhibit 4

Roughly an eighth of India’s diesel is burnt standing still

Stationary end-uses as a share of all diesel, retail and direct sales combined


[T4 "The stationary segment" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 End use | c1 Share of diesel (%)
  r0: Gensets, non-industry | 6.45
  r1: Gensets, industry | 4.06
  r2: Mobile towers | 1.54
  r3: Stationary total | 12.05


Source: PPAC / Nielsen India, All India Study on Sectoral Demand of Diesel & Petrol, Figure 1. Fieldwork January 2012 to June 2013. Shares are of the period studied and are not current levels; see the caution above.

A generator is the best conversion candidate in the entire fuel system. It sits on a known site, it has a fixed address for a gas connection or a cylinder cascade, it does not need a refuelling network, and its duty cycle is predictable. Gas gensets are a mature product; the constraint is piped-gas availability at the site, not technology.

Telecom towers deserve separate mention because the sector has spent fifteen years trying to leave diesel and still burned 1.54% of national consumption in the study period — more than aviation and shipping combined. Towers are the clearest case of diesel used purely as backup for an unreliable grid, and the improving power position weakens the case for it: peak demand of 270.82 GW in April–May 2026 was met in full, with a deficit of 0.0%.

Why stationary conversion is not already done. Freight can refuel wherever a station exists; a generator can only use the gas that reaches its plot. City gas distribution geography, not economics, is the binding constraint — which makes genset conversion a question about CGD network rollout rather than about fuel prices. That is a different policy lever from the one this article has been discussing, and a more tractable one.

## Doorstep delivery

The arbitrage, formalised and licensed

There is now a legal industry built on the gap this article has been describing. Doorstep diesel delivery brings fuel to the consumer in a licensed mobile dispenser rather than requiring the consumer to reach a pump.

The operators are real businesses at scale. FuelBuddy, founded in 2020, acquired MyPetrolPump in May 2021. Humsafar, founded in 2016, supplies non-automotive diesel to industrial, healthcare and hospitality customers. Repos Energy, backed by Ratan Tata, reports a presence in 130 cities. Pepfuels operates in the same segment, and the public-sector oil marketing companies have themselves invited start-ups into doorstep delivery.

The regulatory shape matters more than the company list. Delivery is licensed by the Petroleum and Explosives Safety Organisation, which specifies the tankers, requires periodic inspection of mobile dispensers, and mandates documentation of quantity, quality and delivery location for every transaction. Critically, it is permitted for approved business locations and generators, not for private vehicles or personal use.

Two things follow. First, the customer base is precisely the stationary segment above — gensets and industrial sites — so doorstep delivery and genset conversion are competing answers to the same problem. Second, a licensed channel with per-transaction documentation of quantity and location is the opposite of the siphoning described earlier. The same demand that fuels diversion also supports a formal channel; policy determines which one grows.

An open question this article cannot answer. Does doorstep delivery price off the retail rate or the direct-sales rate? Given the ₹40-per-litre gap, the answer decides whether this channel arbitrages the wedge or merely adds convenience on top of retail. Nothing read for this piece states it, and the operators do not publish it. It is the single most useful fact anyone could add here.

## The running-cost gap

Where CNG’s advantage is actually measured

The clearest argument for switching is not environmental — it is arithmetic. A companion piece on this blog models cost per kilometre from 303 ARAI-certified SIAM fuel-efficiency declarations and OMC-published city fuel boards, on a Delhi July 2026 basis.

Exhibit 5

CNG runs at roughly three-quarters of the diesel cost per kilometre

Modelled running cost, Delhi, July 2026 basis, four-wheeler segments


[T5 "The running-cost gap" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Segment | c1 Petrol E20 (₹/km) | c2 Diesel (₹/km) | c3 CNG (₹/km) | c4 CNG vs diesel (%)
  r0: Sedan | 7.09 | 4.33 | 3.20 | −26
  r1: Compact SUV | 8.18 | 5.01 | 3.78 | −25
  r2: Hatchback | 6.65 | — | 2.97 | —
  r3: Two-wheeler | 1.93 | — | 0.81 | —


Source: [State by State: Who Actually Earns From the Fuel You Buy](https://blog.vertistratsolution.com/2026/08/state-by-state-who-actually-earns-from.html), modelled in the vehicle_fuel_mileage repository from 303 ARAI-certified SIAM BS-VI fuel-efficiency declarations and OMC city fuel boards. Diesel is modelled only for sedan and compact SUV, consistent with what the market actually offers. CNG-vs-diesel column is the author’s calculation from the modelled costs.

A quarter off the per-kilometre running cost is the switching case, and it does not depend on any claim about inflation or emissions. Two features of the comparison are worth drawing out. The CNG gain comes from combustion efficiency and per-unit price together, and — unlike ethanol blending, which dilutes one liquid with another and costs 2–6% in mileage on the ARAI/SIAM range — a petrol-to-CNG conversion on the same nameplate vehicle shows a mileage gain. The two fuel shifts move in opposite directions on efficiency.

This table is four-wheelers; the recommendation is not. The segments modelled are passenger cars. This article’s conversion case is about heavy and light commercial vehicles, buses and gensets, where duty cycles, load factors and gas pricing all differ. The direction of the advantage transfers; the per-kilometre numbers do not. A commercial-fleet equivalent would need bowser or bulk CNG pricing and real duty-cycle data, and has not been built.

On “greener”. Nothing above is an emissions figure, and this article does not carry one. CNG’s environmental case against diesel is strongest on particulates and oxides of nitrogen, weaker on carbon dioxide, and methane slip erodes part of the well-to-wheel advantage. Those are real claims that need real measurement, and until this blog publishes that measurement the case made here is a cost, import-exposure and leakage case — not a carbon one.

Sources. Cost per kilometre — vehicle_fuel_mileage repository, calibrated on 303 ARAI-certified SIAM BS-VI fuel-efficiency declarations and OMC city fuel boards. Wholesale price indices — DPIIT, Office of the Economic Adviser, base 2011-12 = 100, April 2012 to April 2026; consumer price indices — MoSPI; correlations are the author’s calculation on April-anchored annual growth rates, FY2012–FY2026. Consumption, channel shares, the direct-versus-retail price gap, sectoral direct-sales breakdown, kerosene shares, e-way bills, port cargo and vehicle sales — PPAC, Industry Consumption Report POL & NG, May 2026. Economy-wide diesel end-use — PPAC / Nielsen India, All India Study on Sectoral Demand of Diesel & Petrol, fieldwork January 2012 to June 2013, report dated 20 December 2013. Import dependency and self-sufficiency — PPAC, Snapshot of India’s Oil & Gas Data, March 2025. Peer-reviewed study cited but not read: P. P. Ghosh, “Impact of India’s diesel subsidy reforms and pricing policy on growth and inflation”, Energy Economics 113 (2022), [doi:10.1016/j.eneco.2022.106195](https://doi.org/10.1016/j.eneco.2022.106195). Diesel siphoning cases — Deccan Herald reporting on the Bengaluru and Udupi arrests; fuel-adulteration directive — Autocar India. Press reports are secondary sources and are labelled as such in the text.

## What would fix this

[kept verbatim, open: What would fix this; 4 items]
