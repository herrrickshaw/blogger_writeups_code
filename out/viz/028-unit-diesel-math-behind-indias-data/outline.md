The pattern in one line: diesel generators cost roughly three times what grid power costs and roughly three-and-a-half times what solar-charged battery storage costs, and India is about to build a lot more of both data centres and telecom towers — the two infrastructure categories that lean hardest on diesel for backup power. Telecom towercos have spent a decade proving that alternative works at scale; the data-centre industry is still writing that playbook from scratch, on a much bigger build-out, on a much tighter timeline.

Diesel generator sets like this one are the default backup power source for India's telecom towers and data centres — the equipment this piece argues is already losing the cost argument to solar-charged battery storage. [Kirloskar - Silent Diesel Generator Set - Mathura](https://commons.wikimedia.org/wiki/File:Kirloskar_-_Silent_Diesel_Generator_Set_-_Mathura.jpg), Rashmi Saletify, CC BY-SA 4.0, via Wikimedia Commons.

## 1. Two build-outs, one backup-power habit

India's data-centre capacity is projected to grow from roughly 1.2–1.5 gigawatts today to somewhere between 6 and 17 gigawatts by 2030, depending on which forecaster is asked — S&P Global's consensus range is 6–6.5 GW with a 9 GW bull case, Mordor Intelligence projects 15.21 GW by 2031, and a Jefferies estimate cited by industry trackers runs as high as 17 GW.

The one figure with an official government anchor is more concrete: the Ministry of Power formally built a projection of 13.56 GW of data-centre electricity demand by FY2031–32 into national transmission planning, published via the Press Information Bureau in March 2026. Whichever number turns out right, the direction is the same — a four-to-tenfold expansion inside five years, backed by more than $210 billion in combined commitments from Adani and Reliance alone, plus tens of billions more from Google, Microsoft, and AWS.

At the same time, India's telecom tower base needs to grow from roughly 750,000 towers already in place to around 1.2 million to support a full pan-India 5G rollout, per an estimate from the Digital Infrastructure Providers Association cited in tower-industry research. Both build-outs share a structural problem neither can avoid: grid power in India is not reliable enough on its own, and both categories of site need a backup source that can run for hours during an outage. Historically, for both, that source has been diesel.

## 2. What diesel backup actually costs, in one table

The cost gap is not marginal. Diesel generation runs about $0.28 per kilowatt-hour, against an Indian grid average of $0.085/kWh and round-the-clock renewable power-purchase agreements at $0.076–0.112/kWh depending on the contract structure — figures compiled by the Takshashila Institution from grid-tariff and PPA data. Expressed in rupees for backup-specific comparisons, a Tamil Nadu-focused study by Auroville Consulting found diesel generator sets have a levelised cost of generation of ₹49.58–57.63 per kWh, while a lithium-ion battery energy storage system (BESS) charged from solar at ₹3.95/kWh has a levelised cost of storage of just ₹39.71–61.72/kWh — making solar-charged BESS the cheaper backup option across most hours-of-autonomy scenarios tested, and the only zero-emission one.


[T1 "2. What diesel backup actually costs, in one table" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Power source | c1 Cost | c2 Basis
  r0: Diesel generator | $0.28/kWh (₹49.58–57.63/kWh for backup-specific LCOE) | Takshashila Institution; Auroville Consulting (Tamil Nadu)
  r1: Indian grid, average | $0.085/kWh | Takshashila Institution
  r2: Round-the-clock renewable PPA | $0.076–0.112/kWh | Takshashila Institution
  r3: Solar-charged battery storage (BESS) | ₹39.71–61.72/kWh (levelised cost of storage) | Auroville Consulting (Tamil Nadu)


Dollar and rupee figures are quoted as sourced and not converted to a common currency, since the underlying studies use different methodologies (national grid-tariff averages versus a state-specific commercial/industrial backup-power model) that shouldn't be blended into one number.

## 3. Data centres: diesel is written into the design standard itself

For data centres, diesel isn't an incidental choice — it's embedded in the physical design rulebook. Standard facility guidelines require on-site diesel reservoirs to hold at least 12 hours of full-load fuel (some real-world deployments store 48 hours), generator rooms must sit 9–19 metres from public areas depending on redundancy tier, and installing the generators requires a Petroleum and Explosives Safety Organisation (PESO) explosive licence. Tamil Nadu's Data Centre Policy 2021 goes further, explicitly permitting multi-level diesel generator stacking up to G+5 specifically to help operators economise on land in a high-cost state — a policy choice that bakes diesel dependency into the built environment for the life of the facility, not just its early years.

The economics inside that design standard are already shifting, though. A straight comparison of two backup architectures — Diesel Rotary UPS (DRUPS, which uses flywheel kinetic energy) against Static UPS with a battery bank (SUPS) — found DRUPS has a 9-month payback against SUPS on a 1.5 MW system, purely from lower operating cost ($1.84 million versus $5.46 million OpEx), even before counting emissions. And green data centres are starting to pilot on-site fuel cells for clean backup power, on top of the solar-charged BESS approach the telecom sector has already validated at scale — see the next section.

Telecom towercos have already run this experiment at national scale and published the result: diesel backup is being phased out wherever the grid is reliable enough, and it's cheaper to do it than not to. Data centres are building the same backup-power stack today, on a much larger and more diesel-standardised base, without yet having gone through that same phase-out.

## 4. Telecom towers already ran this experiment

India's telecom towers — 606,300 when TRAI and EY counted them for their infrastructure-sharing study, 83 per cent of them owned by neutral, non-discriminatory tower companies rather than individual operators, the second-highest towerco-penetration rate in the world after China's 100 per cent — were built on a sharing model specifically designed to cut cost: passive infrastructure sharing saves 16–35 per cent on both capex and opex, rising to 33–45 per cent capex savings when active equipment and spectrum are shared too.

Indus Towers, the market leader with 249,305 towers and a 1.63 tenancy ratio, has already converted its 50,000th cell site to run diesel-free (back in March 2016), installed solar power at roughly 30,000 sites, and committed to net-zero emissions by 2050.

Bharti Infratel separately built more than 31,000 towers that consume under a litre of diesel a day. Indus's own language for the current phase is blunt: it is "actively shifting away from DG usage at sites where grid connectivity is robust" — not as a sustainability gesture, but because it's the cheaper operating choice once grid reliability clears a threshold. The base has grown since: the Department of Telecommunications counted 8.43 lakh mobile towers and 31.44 lakh base stations on 31 October 2025.

Smaller towercos are experimenting further out on the technology curve. Suyog Telematics, which operates 5,704 towers, is trialling zinc batteries (abundant and cheaper than lithium) as a lower-cost VRLA replacement at multi-operator sites, alongside pilot wind turbines at select towers specifically to cut the electricity bill. None of this is presented as an environmental programme first — it's cost engineering that happens to also cut diesel and emissions, which is exactly the argument the data-centre sector's own BESS-versus-diesel numbers are starting to make too.

## 5. The option this piece hasn't covered yet: gas gensets, not just batteries

The diesel-versus-BESS framing above skips a third option that's already commercially available and doesn't require a new battery supply chain: swapping the generator's fuel, not its architecture. A gas genset running on piped natural gas costs roughly ₹6.06 per kVA-hour to operate against a diesel genset's ₹12.6, per a Centre for Science and Environment feasibility comparison — fuel cost alone runs about half of diesel's, and gas gensets emit no visible smoke or particulates and substantially less NOx and CO₂ per unit generated.

The trade-off runs the other way on capex: a gas genset of comparable size costs roughly 50 per cent more upfront than an equivalent diesel unit, because it needs either a pipeline tap or on-site compression and storage, so the economics favour high-utilisation backup (frequent, longer outages) over the occasional short outage a diesel set is sized for.

What makes this option specifically live for India's current build-out is the same city-gas network this blog has covered before: PNGRB had authorised 307 geographical areas by 2026, reaching close to 100 per cent of India's landmass outside the islands and around 784 districts, with over 5,665 CNG stations already built out as of March 2023. A data centre or tower site sitting inside an authorised GA can in principle tap piped natural gas (PNG) directly for a genset, the same infrastructure already delivering gas to industrial and commercial users in that geography.

For sites outside pipeline reach — which, given India's tower and data-centre footprint spans well beyond the geographies PNGRB has reached with distribution pipe so far, will be most of them for years yet — the same CNG cascade-cylinder logistics that already supply CNG stations without a direct pipeline connection could supply a genset instead: a cascade is simply a bank of interconnected high-pressure cylinders (a common commercial unit holds around 530 kg of CNG at 250 bar) trucked in and swapped out like an LPG cylinder exchange, rather than piped continuously.

Compressed biogas (CBG) plants under the SATAT scheme are explicitly built to distribute through the same cascade-cylinder or pipeline routes to fuel-station networks, which means a CBG-fed cascade could serve the identical genset with a renewable, India-sourced fuel instead of imported diesel or fossil natural gas — the same CBG production capacity this blog's own reporting on the sector has tracked, applied to a demand category (backup power for digital infrastructure) it hasn't yet been pointed at.

## 6. Who's actually selling gas gensets in India today

This isn't a hypothetical product category waiting to be invented — every major genset manufacturer serving the Indian market already sells a gas-fuelled line alongside its diesel range, priced and specced for exactly this kind of backup-power decision:


[T2 "6. Who's actually selling gas gensets in India today" 7 rows; use rows by number in a chart "table" spec]
  cols: c0 Company | c1 Gas genset offering
  r0: Cummins India | CPCB IV+ compliant gaseous gensets up to 800 kVA, running on natural gas, biogas, or LPG depending on the model
  r1: Mahindra Powerol | Launched India's first CPCB-II-approved CNG/PNG genset; India's largest genset manufacturer by volume now carries gas alongside diesel across its range
  r2: Caterpillar (via Gainwell India, its authorised Indian dealer) | Natural gas and biogas generator sets from 100 to 4,500 kVA in a single unit, including a dedicated biogas product line
  r3: Kirloskar | CNG/gas genset range distributed in India through partners including Green Power International
  r4: Greaves Cotton | CPCB IV+ compliant range spanning 5–2,250 kVA, gas and diesel variants sharing the same emissions-control platform
  r5: Jakson Group | CPCB IV+ gensets, plus a partnership with Cummins specifically to co-market solar-plus-storage hybrid systems alongside its generator business
  r6: Wärtsilä (global, India-serving) | Gas-fired reciprocating engine gensets used globally for pipeline gas, biogas, and coal-bed methane applications, positioned for grid-scale and large captive installations rather than single-site backup


The pattern across this list is telling: gas gensets aren't a niche import or a startup product — they're a standard SKU next to the diesel model at every one of India's established genset makers, priced with the same CPCB IV+ emissions compliance the diesel range needs anyway (India's current emissions standard for gensets, tightened in phases through 2024). Nobody on this list has announced a data-centre- or telecom-tower-specific gas genset product line, which matches the point made earlier: the option is commercially available off the shelf, but the demand signal from these two specific buyer categories hasn't shown up yet.

## 7. What's actually at stake if the switch doesn't happen this time

The reason this matters now rather than as a slow multi-decade transition is timing: both build-outs are happening in the same five-year window. If new data-centre capacity is designed and licensed today around the diesel-heavy standard — 12–48 hour diesel reservoirs, PESO-licensed generator halls, G+5 DG stacking in states like Tamil Nadu — that design choice is largely locked in for the operating life of the facility, the same way telecom's diesel-generator base was locked in during the 2000s tower build-out and has taken over a decade of active phase-out (2016 onward, still ongoing in 2026) to unwind.

The 4–13 GW of new data-centre capacity coming this decade, and the roughly 450,000 additional telecom tower sites needed for 5G, are both decisions being made now about a backup-power architecture that will still be running in 2035 and beyond.

The Ministry of Power's own transmission planning already treats grid reliability as the binding constraint on India's AI ambitions, not compute hardware. Every unit of data-centre or tower demand met by a diesel generator instead of grid power or storage is also a unit of diesel import demand added at exactly the moment India's other energy policy work — ethanol blending, CBG mandates, green hydrogen pilots — is aimed at reducing fuel-import dependency from the other direction.

Updated 2 November 2026. The “roughly 1.2–1.5 gigawatts today” of data-centre capacity below is the Takshashila Institution’s estimate used when this piece was written. A more recent count from Cushman & Wakefield put India’s operational data-centre capacity at about 1,789 MW in the first half of 2026, about half of it in Mumbai; see [Closed Loop or Open Loop? How India’s New Data Centres Should Be Cooled, Site by Site](https://blog.vertistratsolution.com/2026/10/closed-loop-or-open-loop-how-indias-new.html). The two sources count capacity differently, so the figures are not strictly comparable.

Updated 13 October 2026. The 13.56 GW data-centre demand projection described below as “the one figure with an official government anchor” has been superseded. In a written Rajya Sabha reply reported around 28 July 2026, the Ministry of Power said it now projects about 26.3 GW of AI data-centre load by FY2031-32, almost double the earlier figure, based on proposals submitted to states rather than built capacity. Read “the most recent official figure” for the 13.56 GW; one report also suggests the 13.56 GW figure was already in circulation in December 2025, so the March 2026 attribution is uncertain. Sources: [Inc42](https://inc42.com/buzz/ai-data-centres-to-consume-26-3-gw-power-by-fy32-mos-power/), [S&P Global](https://www.spglobal.com/energy/en/news-research/latest-news/lng/072826-india-power-sector-to-face-26-gw-load-from-ai-data-centers-by-fy-2031-32-ministry). The original text below is unchanged.

## What would fix this

[kept verbatim, open: What would fix this; 5 items]
