−94 kJHeat released per mole of ethylene when it joins a polyethylene chain, about 3.4 MJ per kilogram of plastic made

~335°CTemperature above which breaking propane into ethylene and methane becomes thermodynamically favoured, by this blog’s calculation from NIST data

142°CHow much a ZSM-5 zeolite lowered the temperature at which polyethylene starts to break down, in one 2025 study

41%Share of India’s pyrolysed waste tyres recovered as oil in FY2024, from NITI Aayog’s tonnages: 1.10 Mt from 2.68 Mt

~₹6,000/tWhat IOCL Paradip estimated it would pay to have spent FCC catalyst taken to cement kilns, in a 2019 tender

[kept verbatim: dated update notes]

## The chain is not where the energy went in

It is easy to picture a plastic or a heavy oil as hydrocarbons that someone had to push together into long chains, so that breaking the chains gives back the energy that was put in. The chemistry runs the other way. Joining small molecules into a chain releases heat. When ethylene polymerises into polyethylene, each mole gives off about 94 kJ, which works out to about 3.4 MJ per kilogram of plastic made. Styrene releases about 73 kJ per mole and methyl methacrylate, the monomer of acrylic sheet, about 56 kJ. Polymer reactors are cooled, not heated, to stop the reaction running away.

The energy that matters — the 40-odd megajoules a kilogram that a plastic or a fuel oil gives up when it burns — is in its carbon–hydrogen and carbon–carbon bonds compared with carbon dioxide and water. For crude oil that energy was stored by photosynthesis in ancient plankton and plants. For a crop residue it was stored last season. Making a polymer chain neither creates nor stores much of it. Breaking the chain does not release it either: cracking a long molecule into shorter ones absorbs heat.

So the useful way to ask the question is the reverse: if breaking chains costs energy, why does it happen at all, and how do refineries and pyrolysis plants make it happen at the temperature they choose?

## Why heat alone eventually breaks the chain

Whether a reaction runs on its own depends on its Gibbs free energy, ΔG = ΔH − TΔS. ΔH is the heat absorbed; ΔS is the change in entropy, roughly the number of ways the molecules can arrange themselves; T is the absolute temperature. A reaction can run when ΔG is negative.

Cracking has a positive ΔH, which works against it. But one big molecule becoming two or more smaller ones increases entropy, so ΔS is positive too, and the −TΔS term grows as temperature rises. Above a certain temperature it outweighs ΔH and cracking becomes favoured. Polymerisation is the mirror image: favoured at low temperature, opposed at high. The crossover for a polymer is called its ceiling temperature; above it, the chain prefers to come apart.

Standard NIST thermochemical data make the point with two small molecules. Breaking a carbon–carbon bond in propane to give ethylene and methane absorbs about 82 kJ per mole and raises entropy by about 135 J per mole per kelvin, so it becomes favoured above roughly 610 K, or about 335°C. Pulling hydrogen off ethane to give ethylene absorbs about 136 kJ and raises entropy by about 121 J, so it needs about 1,130 K, or about 855°C. That second number is why naphtha and ethane crackers run their furnace coils at 800°C and more.


[T1 "Why heat alone eventually breaks the chain" 5 rows; use rows by number in a chart "table" spec]
  cols: c0 Reaction | c1 ΔH kJ/mol | c2 ΔS J/mol·K | c3 Favoured above
  r0: Propane → ethylene + methane | +82 | +135 | ~335°C
  r1: Ethane → ethylene + hydrogen | +136 | +121 | ~855°C
  r2: Ethylene → polyethylene | −94 | negative | Ceiling ~610°C
  r3: Styrene → polystyrene | −73 | negative | Ceiling ~310°C
  r4: MMA → acrylic (PMMA) | −56 | negative | Ceiling ~220°C


The first two rows are this blog’s calculation from NIST Chemistry WebBook standard enthalpies of formation and entropies for the gases at 25°C, assumed constant with temperature, so the crossover temperatures are approximate. Polymerisation heats and ceiling temperatures are commonly tabulated textbook values; ceiling temperatures depend on the standard state assumed for the monomer.

The ceiling temperature explains why plastics behave so differently in a pyrolysis reactor. Acrylic, with a low ceiling, “unzips” back to its monomer: heated, it gives back mostly methyl methacrylate that can be polymerised again. Polystyrene gives back a good share of styrene. Polyethylene does not unzip. Its bonds break at random points along the chain, well below its nominal ceiling, because a random break into a shorter alkane and an alkene is a different reaction from reversing polymerisation. The product is a smear of waxes, oils and gases rather than ethylene. That smear is why polyethylene pyrolysis produces a fuel oil, and why getting chemicals back from it takes a catalyst.

## What a catalyst changes, and what it cannot

Thermodynamics says where a reaction ends up. It does not say how fast it gets there. A carbon–carbon bond in a chain must be stretched to breaking point before the molecule can rearrange, and the energy needed to get over that hump, the activation energy, is what makes thermal cracking slow below about 400°C.

A catalyst lowers the hump; it does not move the end point. Acidic zeolites — crystalline aluminosilicates with pores the size of small molecules — give up a proton to a hydrocarbon and turn it into a positively charged carbocation. A carbocation breaks at the bond one position away from the charge, a step called beta-scission, much more easily than a neutral chain breaks in the heat. The zeolite pores also limit which molecules fit and which come out, so the catalyst shapes the products as well as speeding the reaction.

Laboratory studies give the size of the effect. A 2025 study in Energy & Fuels found that a ZSM-5 zeolite with a silicon-to-aluminium ratio of 22 made high-density polyethylene start losing weight at about 306°C, 142°C below the plastic on its own; more aluminium meant more acid sites and an earlier start. Other studies report near-complete conversion of polyethylene over ZSM-5 at 450°C in under 20 minutes, or at 350°C over a longer time, and activation energies about 30% lower when the zeolite is loaded with copper and cerium. Loading platinum onto ZSM-5 tips the products towards benzene, toluene and xylene; one study reported about 21% of those aromatics at 500°C, with most of the rest as light gases.

The catalyst cannot make cracking release energy. It lets the plant pick a lower temperature and a narrower set of products, and pay less heat to get there.

Because the catalyst does not change ΔG, the reactor still has to sit at a temperature where cracking is favoured, and the heat of reaction still has to be supplied. What changes is that the reactor can be held at a lower, controlled temperature, products spend less time being over-cracked into gas, and less of the feed ends up as coke.

## How a refinery pays the heat bill

A fluid catalytic cracker, the refinery unit this blog has written about for its petrol and LPG yields, is the industrial form of this chemistry. Heavy gas oil meets hot, powdered zeolite catalyst at the bottom of a tall pipe called the riser, at around 500–550°C, and cracks in a few seconds as the two rise together. The reaction absorbs heat, typically quoted at 200–700 kJ per kilogram of feed, and the mixture cools by 30–40°C on the way up.

That figure fits the free-energy picture. If a gas-oil molecule of about 350 g/mol is broken once, at about 82 kJ per break, the heat absorbed is about 230 kJ per kilogram; breaking it two or three times moves towards the top of the quoted range. This is a rough check by this blog, not an engineering number.

The heat comes from the cracking itself. A few percent of the feed is left on the catalyst as coke. The catalyst is separated from the products, sent to a regenerator and the coke burnt off in air at around 700°C. The hot, clean catalyst returns to the riser carrying the heat the next round of cracking needs. A well-run FCC unit is “heat-balanced”: the coke it makes is the fuel it burns. Steam crackers, which make ethylene and propylene for plastics, use no catalyst and get there by brute temperature instead, which is why they are among the most energy-intensive units in the chemical industry.

## The energy return on pyrolysing plastic

A pyrolysis plant for waste plastic or tyres is a small, batch version of the same trade. One analysis puts the theoretical heat needed to pyrolyse a kilogram of polyethylene at about 1.05 MJ and a measured requirement at about 1.3 MJ. That covers heating the plastic, melting it and cracking it. The products carry about 43 MJ per kilogram, so the heat input is about 3% of the energy that comes out. Pyrolysis oils from plastic are typically quoted at 25–45 MJ per kilogram depending on the plastic and the process; polyethylene and polypropylene themselves carry about 42–50 MJ per kilogram.

On energy, then, pyrolysis is not the problem. The problem is control. The temperature at which the plastic is held, how long the vapours stay hot and whether they meet a catalyst decide whether the output is a usable oil, a waxy mixture, mostly gas, or a mess of tar and char. A unit that cannot hold its temperature, or that vents its gas instead of burning it, wastes the feed and pollutes as it does so.

## Spent refinery catalyst and new catalysts, in stages

A refinery’s FCC unit does not keep its catalyst for ever. Nickel and vanadium from the crude settle on it, steam in the regenerator slowly strips aluminium out of the zeolite, and its activity falls. To hold activity steady, the refinery adds fresh catalyst every day and withdraws an equal amount of the aged mixture, called equilibrium catalyst or ECAT. A 2015 review by Vogt and Weckhuysen in Chemical Society Reviews estimated that about 2,300 tonnes of FCC catalyst are made worldwide every day, about 840,000 tonnes a year, or about 0.16 kg for every barrel of feed. Much of what comes out is landfilled. Spent hydroprocessing catalysts, which carry nickel, molybdenum, cobalt and vanadium, add another 150,000–170,000 tonnes a year worldwide, a figure widely cited in reviews of their management.

At that average rate, an FCC unit cracking a million tonnes of feed a year would withdraw roughly 1,000 tonnes of catalyst, and a unit the size of Indian Oil’s 4.17 million-tonne INDMAX cracker at Paradip roughly 4,000–4,500 tonnes. These are this blog’s estimates from the global average; heavy-residue units use more catalyst per barrel and units on clean feed use less. India has 17 FCC units, five of them residue crackers, according to Industrial Info Resources, an industry data provider. No public figure exists for how much catalyst they withdraw.

Spent catalyst and new research catalysts are not rivals. Each suits a different temperature, a different stage of the job and a different degree of dirtiness in the feed. Put in sequence, they can push yields further than either could alone.


[T2 "Spent refinery catalyst and new catalysts, in stages" 4 rows; use rows by number in a chart "table" spec]
  cols: c0 Stage | c1 Catalyst | c2 What it is for
  r0: 1. Primary cracking of melted plastic or wax | Spent FCC catalyst (ECAT) | Cheap, already tolerant of metals; takes the coke, chlorine and additives
  r1: 2. Upgrading the vapours | Tuned zeolite: ZSM-5 by Si/Al ratio, Ga, P or Pt-loaded | Steers clean vapours towards olefins or aromatics
  r2: 3. Finishing the oil | Refinery FCC or hydrotreater | Co-processes pyrolysis oil with crude-derived feed
  r3: 4. End of life | Metal recovery, cement, new zeolite | Recovers Ni, Mo, V and Co; uses spent FCC catalyst as a pozzolan or to make new zeolite


Stage 1: spent catalyst where the feed is dirtiest. The first contact with melted plastic is the hardest on a catalyst. The feed carries chlorine from PVC, fillers, pigments and additives, and it lays down coke fast. A fresh designer zeolite here would be used up quickly. Equilibrium catalyst is cheap and already conditioned to metals, and its reduced acidity helps: it cracks less aggressively, so less of the plastic goes to gas. Lin and Yang, in Applied Catalysis A in 2007, found that refinery ECAT gave the same aromatics content as fresh FCC catalyst when cracking polyolefins while forming markedly less coke. A 2023 study in the Journal of Thermal Analysis and Calorimetry found spent FCC catalyst lowered the temperature at which polypropylene starts to break down by about 59 K. A 2021 study of waste polypropylene showed the trade-off: the catalyst cut liquid oil from 83% to 78% and raised gas from 13% to 20%, at a catalyst-to-plastic ratio of 0.1. Spent FCC catalyst has also been tested for upgrading the wax that thermal pyrolysis leaves behind into liquid fuel.

Stage 2: new catalysts where the feed is clean. Once stage 1 has turned the plastic into vapour and kept the worst contaminants behind, a more selective catalyst can work on the vapour alone, often in a separate bed at its own temperature. This is where catalyst research pays off. ZSM-5’s silicon-to-aluminium ratio sets its acidity; its pore size limits the products to small molecules; gallium, phosphorus or platinum on the zeolite push it towards aromatics or protect it from losing aluminium. Contact time is the other control. Studies with very short vapour contact on HZSM-5 report light olefins — ethylene, propylene, butenes, the building blocks of new plastic — as the main product, while longer contact lets those olefins cyclise into aromatics. Staging also works within stage 2: Ratnasari, Nahil and Williams, in the Journal of Analytical and Applied Pyrolysis in 2017, put a mesoporous MCM-41 catalyst ahead of ZSM-5 so that the larger molecules were cracked in the wider pores before reaching the narrower ones, and got an oil yield of about 83%, mostly in the gasoline range.

Stage 3: the refinery finishes the job. Pyrolysis oil can go back to where the spent catalyst came from. Co-processing a small share of plastic pyrolysis oil in an FCC unit needs no extra hydrogen and little change to the unit, according to industry papers on the practice, provided the oil is cleaned of chlorine and metals first, which is easier if stage 1 has already held them back.

Stage 4: the catalyst’s own end of life. Once ECAT is too coked or poisoned to use even in stage 1, it still has uses. Spent FCC catalyst is an aluminosilicate and has been tested as a partial substitute for cement, and as a raw material for synthesising new zeolite. Spent hydroprocessing catalysts are worth more for their nickel, molybdenum, vanadium and cobalt, which can be leached out and recovered. In India, spent catalyst is a hazardous waste under the Hazardous and Other Wastes (Management and Transboundary Movement) Rules, 2016, and can be sent only to authorised recyclers.

The yield logic in one line. The cheapest catalyst takes the dirtiest, lowest-value step and protects the expensive one; the expensive catalyst sees only clean vapour at the temperature and contact time that suit the product wanted; the refinery takes the oil; and the metals in the spent catalyst go back into new catalyst. The thermodynamics of each step is the same — heat in, entropy up — but each stage is run at the temperature at which its catalyst performs best.

What the staged model has not shown is economics at Indian scale. Most of the results above come from laboratory reactors processing grams or kilograms of clean, sorted plastic. Mixed post-consumer waste is harder, and no Indian plant has published a staged-catalyst yield.

## What Indian refineries do with spent catalyst now: the tender record

Public tenders show what spent FCC catalyst is worth to an Indian refinery today: usually less than nothing. Listings on tender portals, collected by the aggregator TenderDetail, show Indian Oil’s refineries mostly paying contractors to take FCC catalyst away, while catalysts carrying platinum, nickel, molybdenum or tungsten are sold.


[T3 "What Indian refineries do with spent catalyst now: the tender record" 8 rows; use rows by number in a chart "table" spec]
  cols: c0 Refinery, date | c1 What | c2 Who pays
  r0: IOCL Paradip, Dec 2019 | 3,500 t of FCC catalyst from the INDMAX unit, for co-processing in cement kilns; estimate ₹2.10 crore | Refinery
  r1: IOCL Paradip, 2018–2026 | Repeat disposal contracts: ₹70.33 lakh (2018–19), ₹3.62 crore (2023), ₹2.26 crore (Dec 2025, “dry waste”), ₹2.62 crore (Aug 2026) | Refinery
  r2: IOCL Panipat, 2020–2026 | Annual contracts to lift and dispose of FCC catalyst through an authorised agency: ₹1.14 crore (2021, 2024), ₹1.08 crore (May 2026) | Refinery
  r3: IOCL Bongaigaon, 2021–2024 | INDMAX catalyst for co-processing, ₹1.28 crore (2021); then expressions of interest to dispose of it by auction (2022, 2024) | Refinery, then buyer
  r4: Haryana, Sep 2025 | Auction of two lots: FCC catalyst from the “PR FCC unit”, apparently Panipat Refinery, and from an INDMAX unit | Buyer
  r5: HPCL Visakh, Oct 2018 | Auction of spent FCC catalyst from FCCU-I and II | Buyer
  r6: Numaligarh, Jun 2020 | 400 t of hydrocracker and hydrogen-unit catalysts (nickel, tungsten, molybdenum oxides); bidding from zero | Buyer
  r7: IOCL Paradip, closes 5 Oct 2026 | Outright sale of platinum-bearing reformer catalyst and fines | Buyer


Rupee figures are the estimated tender values shown in the listings, not awarded prices, and most listings do not state a quantity. The Numaligarh details are from the refinery’s own auction document.

The one listing with a quantity makes the price clear: ₹2.10 crore for 3,500 tonnes is about ₹6,000 a tonne, which the refinery expected to pay to have its spent catalyst taken to cement kilns. That is in line with European estimates of €300–450 a tonne to collect and landfill spent FCC catalyst. The 3,500 tonnes also fits this blog’s estimate above of 4,000–4,500 tonnes a year for a unit of Paradip’s size, though the tender does not say what period it covers.

The hydroprocessing catalysts are a different market. Numaligarh’s 2020 auction offered 400 tonnes of mixed spent catalyst — hydrocracker catalysts listed as containing 5–10% nickel oxide and 10–50% tungsten oxide or 5–10% molybdenum oxide, plus copper, zinc and nickel catalysts from the hydrogen unit — with bidding starting at zero, an earnest-money deposit of ₹1.75 lakh, and only buyers holding pollution-control-board authorisation eligible. Winning bidders had to sign confidentiality agreements with the catalyst licensors, Chevron, Axens and Haldor Topsoe, and with Engineers India. Metal recovery, not cracking, is what buyers of these catalysts are after.

There is also a quiet trade in equilibrium catalyst between refineries. HPCL’s Mumbai refinery has repeatedly tendered to buy “equilibrium catalyst or spent catalyst” for its FCC unit (2017, 2020 and 2023 contracts, the 2017 one also covering Visakh); Gujarat refinery tenders from 2012–13 sought 250 and 800 tonnes of equilibrium catalyst; and in 2023 Indian Oil tendered to truck equilibrium catalyst from its Mathura refinery to CPCL’s refinery at Manali, Chennai. Refiners use bought-in equilibrium catalyst to start up a unit or to hold activity steady without paying for fresh catalyst. Spent catalyst that one refinery pays to dispose of can be another refinery’s cheap make-up catalyst — and a pyrolysis plant’s stage-1 catalyst.

## Tyre pyrolysis in India: what comes out of the reactor

Tyres are the one feed that India already pyrolyses at industrial scale. NITI Aayog’s January 2026 report, Enhancing Circular Economy of Waste Tyres in India, puts the waste tyres recycled in FY2024 at 3 million tonnes, of which 1.6 million were generated in India and 1.4 million imported. Pyrolysis took 2.68 million tonnes of that, almost all of it (2.64 million) in batch reactors and only 0.04 million in continuous plants. A sizeable share of the feed, the report says, was probably imported tyre first shredded into crumb rubber.

From those 2.68 million tonnes the report estimates 1.10 million tonnes of tyre pyrolysis oil, 0.80 million tonnes of carbon char and 0.3 million tonnes of steel wire. That is about 41% oil, 30% char and 11% steel by weight, by this blog’s division, leaving about 18% as gas and losses. The gas can be burnt to heat the reactor. Only 0.05 million tonnes of the char was upgraded into recovered carbon black fit for rubber goods; the other 0.75 million tonnes went straight to industry as a fuel, as a substitute for petroleum coke.


[T4 "Tyre pyrolysis in India: what comes out of the reactor" 5 rows; use rows by number in a chart "table" spec]
  cols: c0 Source | c1 Oil % | c2 Char % | c3 Steel % | c4 Gas, loss %
  r0: India, FY2024, all pyrolysis (NITI Aayog) | 41 | 30 | 11 | ~18
  r1: CPCB basis for EPR credit | 35 | 32 | — | 33*
  r2: Rule of thumb, reviews and trade sources | 40–50 | 30–35 | 10–15 | 5–15
  r3: Lab fixed bed, 475°C, steel-free | 55 | 36 | — | 9
  r4: Literature range | 40–60 | 20–40 | — | 10–30


India and CPCB rows from NITI Aayog (2026), which reproduces CPCB’s conversion-factor table; percentages for the India row are this blog’s division of the report’s tonnages, rounded. *CPCB’s basis gives 35 t oil and 32 t char per 100 t of waste tyre and does not split the remaining 33 t between steel, gas and losses. The rule of thumb and literature range are as quoted in reviews of tyre pyrolysis and Indian trade sources; the laboratory row is Islam and co-authors (2011), as cited in a review of tyre pyrolysis.

The gap between the laboratory and the plant is the temperature-control problem in numbers. In a small fixed bed held at a steady 475°C, more than half the rubber condenses as oil. A large batch retort heated from outside, with whole tyres inside, has hot walls and a cool core. Vapour near the walls over-cracks to gas; rubber in the middle half-cracks to tar that stays on the char. The national 41% is close to what the industry quotes, and well below what controlled reactors reach.

The oil itself is not diesel. Tyre rubber is vulcanised with sulphur, and the oil carries it, along with aromatics, nitrogen and fine char. The specification German refiner H&R Group uses to buy tyre oil, reproduced by NITI Aayog, prefers sulphur below 0.9% by weight and accepts at most 1.1%, halogens below 20–30 mg/kg, and solids below 0.2%. NITI Aayog says BASF is the largest buyer of Indian tyre oil, which it uses as a feedstock. At home the oil is sold as a substitute for furnace oil or light diesel oil, has no Bureau of Indian Standards or petroleum-ministry specification, and carries GST where petroleum fuels do not. NITI Aayog estimates that using tyre oil in place of imported fuel oils could save about ₹1,520 crore in imports.

The rules shape what the plant optimises. Under the waste-tyre EPR rules, a batch plant earns EPR certificates at a weightage of 0.5 and a continuous plant at 0.8, against 1.25 for carbon black good enough for new tyres. The CPCB’s 2024 procedure bars pyrolysis of imported waste tyres, though crumb made from imported tyres still reaches pyrolysis plants. A CPCB report to the National Green Tribunal, as reported in November 2022, counted 757 tyre pyrolysis units in 17 states: 349 compliant, 216 not, and about 192 closed.

## Catalytic tyre pyrolysis for low-sulphur oil

Sulphur is what keeps tyre oil out of anything better than a furnace. A tyre is vulcanised: its rubber chains are tied together by sulphur bridges, and zinc oxide is added to speed the cure. Those bridges, carbon–sulphur and sulphur–sulphur bonds, are weaker than the carbon–carbon backbone, so they are among the first bonds to break when the rubber is heated. The sulphur leaves partly as hydrogen sulphide in the gas and partly as thiophenes, benzothiazoles and other ring compounds that condense with the oil. The oil typically ends up with 1–1.5% sulphur by weight; one 2025 study measured 1.16%. Indian BS-VI diesel allows 10 parts per million, a thousand times less. Even a 5% blend of such oil in diesel would carry several hundred parts per million.

There are two ways to get the sulphur out, and they map onto the staged model above.

Capture it in the reactor. Basic metal oxides react with hydrogen sulphide to form solid sulphides, a reaction that runs downhill. For zinc oxide, ZnO + H2S → ZnS + H2O releases about 77 kJ per mole, by this blog’s calculation from standard tables, so the sulphur stays in the solid with the char. The studies give a sense of how far that goes:


[T5 "Catalytic tyre pyrolysis for low-sulphur oil" 5 rows; use rows by number in a chart "table" spec]
  cols: c0 Additive or catalyst | c1 Result
  r0: Calcium oxide, in the reactor | Oil sulphur 0.99% → 0.91%
  r1: Copper oxide or calcium oxide, 5% | Captured 76% and 45% of the sulphur in the gas
  r2: Calcium hydroxide, pilot fixed bed, 450–600°C | Oil sulphur down to 0.82%; oil yield about 33–35%, on residues from mechanical tyre recycling
  r3: Formulated red mud (iron, calcium and sodium compounds) | Oil sulphur as low as 0.38%
  r4: Spent FCC catalyst with lime or heavy oil | 8–15% more benzene, toluene and xylenes, and less sulphur in the oil


From: “Desulfurization and upgrade of pyrolytic oil and gas during waste tires pyrolysis: the role of metal oxides”, Waste Management (2024), and the earlier calcium oxide study it cites; “Pilot-scale catalytic pyrolysis of waste tires for pyrolysis oil”, Cleaner Engineering and Technology (2026); “Production of low-sulfur fuels from catalytic pyrolysis of waste tires using formulated red mud catalyst” (2024, open access); Tian and co-authors, Fuel 328 (2022). Read through abstracts and search extracts.

Two findings stand out for India. Red mud is the caustic residue of alumina refining, which India produces in large quantities at its alumina refineries; in the red-mud study, the tyres’ own zinc oxide also deposited on the catalyst and helped fix sulphur. And the spent-FCC-catalyst composite is the refinery waste from earlier in this piece doing two jobs at once: its zeolite cracks the vapour towards light aromatics while the lime mixed with it holds sulphur back. In-reactor capture gets the oil to about the 1% ceiling the EU sets for heavy fuel oil, and in the best case well below it. It does not reach diesel quality.

Hydrotreat the oil afterwards. That takes the refinery’s hydrodesulphurisation chemistry: hydrogen over a nickel–molybdenum or cobalt–molybdenum catalyst, which turns organic sulphur into hydrogen sulphide. In batch tests, a nickel–molybdenum catalyst on alumina removed 88% of the sulphur from tyre oil at 250°C and 20 bar in 30 minutes, and 98% at 350°C and 50 bar over six hours. A 2025 pilot study in Energy & Fuels co-processed 5–20% tyre oil with atmospheric gas oil in a commercial nickel–molybdenum hydrotreater at 330–390°C and 55 bar, aiming at 10-ppm diesel. Its blends carried 1.29–1.38% sulphur — and the sulphur fell as the tyre-oil share rose, because the gas oil itself was the more sulphurous component. Sulphur alone does not make tyre oil a problem feed for a refinery hydrotreater; consistency, nitrogen, metals and solids do, which is why the H&R specification limits those too. Removing the sulphur also costs hydrogen, which this blog has covered for diesel. Oxidative routes, using hydrogen peroxide with an acid or a polyoxometalate catalyst followed by adsorption, avoid hydrogen but remain laboratory methods.

The staged version for a tyre plant is therefore: a lime, red-mud or spent-catalyst bed to fix sulphur and crack the vapour at the plant; then the oil, cleaned of solids, sold to a refinery to finish in a hydrotreater. That is the route NITI Aayog points to when it recommends that tyre oil go to refineries, and it needs the standard the report asks for.

## The other route for tyres: crumb rubber in roads

Pyrolysis breaks a tyre’s chains and sells the pieces as fuel. Crumb-rubber modified bitumen keeps the rubber whole: tyres are ground to crumb of under about 600 microns and blended into hot bitumen, where the rubber swells and makes the binder stiffer in summer and more elastic in winter. This blog covered the standards, laboratory results and companies behind it in an earlier piece on India’s tyre-waste problem. What has changed since is the policy push and the data.

Use on national highways is rising. Data that MoRTH supplied to the environment ministry’s Technical Review Committee show NHAI projects used 113,714 tonnes of CRMB in FY2023, 168,531 tonnes in FY2024 and 277,193 tonnes in FY2025 — a rise of about 2.4 times in two years. Polymer-modified bitumen, CRMB’s more expensive rival that needs imported polymer, rose faster, from 50,627 to 204,046 tonnes. A MoRTH circular of 19 April 2024 lets CRMB be used in bituminous concrete for roads designed for 20–50 million standard axles, not only above 50, and a 23 August 2023 circular bars blending modified bitumen at the project site.


[T6 "The other route for tyres: crumb rubber in roads" 2 rows; use rows by number in a chart "table" spec]
  cols: c0 NHAI use, t | c1 FY2023 | c2 FY2024 | c3 FY2025
  r0: CRMB (crumb rubber) | 113,714 | 168,531 | 277,193
  r1: PMB (polymer) | 50,627 | 94,735 | 204,046


MoRTH data recorded in the decision of the 94th meeting of MoEFCC’s Technical Review Committee, 14 July 2025.

But very little tyre goes into it. CPCB’s EPR basis assumes 100 tonnes of waste tyre make 500 tonnes of CRMB, so NHAI’s 277,193 tonnes in FY2025 embodied roughly 55,000 tonnes of waste tyre, by this blog’s calculation. NITI Aayog estimates that 1.53 million tonnes of tyres were crumbed in FY2024 but that only 0.05 million tonnes of crumb went to direct uses of any kind; most of the rest was fed to pyrolysis plants. India grinds tyres into a product the road sector can use and then burns most of it as fuel oil.

[kept verbatim, collapsed: What this piece could not establish]

The proposed mandate. On 14 July 2025 the committee recommended that bitumen producers be given a minimum crumb-rubber-modifier utilisation mandate of 3% of their bitumen production in FY2027, 4% in FY2028 and 5% from FY2029, with MoRTH and the petroleum ministry to be consulted before it is made statutory. This blog found no notification making it binding. BPCL told the committee that India’s refiners make about 5.5 million tonnes of bitumen a year.

What it would mean depends on how it is read. If 3–5% of 5.5 million tonnes is the tonnage of rubber modifier, refiners would need 165,000–275,000 tonnes of it a year. At about 15% modifier in CRMB, that is 1.1–1.8 million tonnes of CRMB, four to seven times NHAI’s FY2025 use, and some 220,000–370,000 tonnes of waste tyre if the modifier is mostly crumb. If the 3–5% is instead the share of bitumen sold as CRMB, it is 165,000–275,000 tonnes of CRMB, which is no more than NHAI already uses. These are this blog’s calculations; the committee’s wording does not settle which it meant. Either way, the committee itself noted that domestic waste tyres are already too few to meet crumb demand, and that a mandate could draw in more imported tyre.

The two routes are not really rivals. A mandate that diverts clean crumb from pyrolysis to roads leaves the pyrolysis plants with the dirtier, steel-bearing remainder, which is where in-reactor sulphur capture and refinery finishing matter most. The rubber that can stay a polymer goes into the road; the rest is cracked, cleaned and refined.

## Where India is

Refineries. India’s refineries run catalytic crackers at scale, including Indian Oil’s own INDMAX technology, which cracks residue at a higher severity to make LPG and propylene: the first unit was at Guwahati in 2003, and the largest a 4.17 million-tonne unit at Paradip commissioned in 2015. This blog’s earlier piece on the FCC lever covered how a ZSM-5 additive in these units shifts output from petrol towards LPG. The same catalyst science is what a plastic or tyre pyrolysis plant needs.

Tyre pyrolysis rules. Acting on National Green Tribunal orders, the Central Pollution Control Board issued a revised standard operating procedure under which only units using an “Advanced Batch Automated Process” may run: a PLC-controlled cycle with controlled heating, gas handling and flaring. By an order dated 29 April 2025, units are limited to a cumulative batch capacity of 60 tonnes a day on one site, and the board asked states in January, March and May 2025 to enforce the procedure. Units must meet zero-liquid-discharge and zero-emission norms and send their carbon char to cement plants. The thermodynamics explains why control matters: a batch reactor heated unevenly gives over-cracked gas in one part and tarry, half-cracked residue in another, and the gas must be burnt rather than vented.

Plastic. Under the plastic packaging Extended Producer Responsibility rules, pyrolysis counts as “end-of-life disposal” alongside waste-to-energy and cement kilns, not as recycling. According to compliance advisers’ summaries, a notice of 19 January 2026 withdrew a temporary concession, granted by a Central Pollution Control Board notice of 28 November 2025, that had let producers use end-of-life certificates against their recycling targets; it was not an amendment to the Rules, whose amendment history in the Gazette runs from G.S.R. 73(E) of 23 January 2025 straight to G.S.R. 237(E) of 31 March 2026. That March amendment, the Plastic Waste Management (Amendment) Rules, 2026, redefines “end of life disposal” to include waste-to-oil conversion, but adds that it “shall not include processes wherein plastic waste is converted into feedstock chemicals, or for the production of new plastic, which shall be considered as recycling”. So pyrolysis to fuel stays outside the recycling credit, while pyrolysis that returns feedstock chemicals now counts as recycling. What the Rules do not say is how the Central Pollution Control Board will tell pyrolysis oil sold as fuel from pyrolysis oil sent to a cracker.

## What would fix this

[kept verbatim, open: What would fix this; 5 items]
