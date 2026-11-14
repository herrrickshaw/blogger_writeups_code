Revised
13 August 2026
· v1.0.0 · [what changed](#changelog)

A corn harvest in South Dakota, the feedstock whose land-use-change emissions the five government models in this piece disagreed on so sharply. [South Dakota Farm Corn Harvest Aerial 5](https://commons.wikimedia.org/wiki/File:South_Dakota_Farm_Corn_Harvest_Aerial_5.jpg), Carl Young, CC BY-SA 4.0, via Wikimedia Commons.

5models EPA ran on the same corn-ethanol scenario in 2023

−0.95 → ~41gCO₂e/MJ spread in their land-use-change results

1tonne CO₂e avoided = 1 CBIO, Brazil's tradable credit

50–65%GHG savings a transport biofuel must clear under EU RED II/RED III, by plant start date

An earlier piece on this site worked through how GCAM's price-mediated, no-foresight architecture actually links energy, land, water and the economy. This one asks a narrower, more practical question: when a government has to decide how many carbon credits a batch of ethanol earns, does it actually run GCAM to find out — and if not, what is GCAM's real job in that decision?

[kept verbatim: dated update notes]

## 1. GCAM's own biofuel accounting is already a credit system, just not a market

GCAM treats raw biofuel — corn for ethanol, wood pellets, whatever the feedstock — as removing carbon from the atmosphere at the point of cultivation, and pays an implicit subsidy for that removal, equal to the model's own carbon price. If that biofuel is later burned without carbon capture, the carbon is re-emitted and the subsidy is repaid in full: a wash, net-zero over the full cycle. Only bioenergy paired with carbon capture and storage (BECCS) gets to keep the original subsidy, because that carbon never comes back out. The GCAM-CDR documentation is explicit that this "can seem like a natural consequence of pricing GHG emissions rather than a specific policy" — it's not a bolt-on carbon-credit module, it falls straight out of putting one consistent price on every carbon flow in the model, the same "price is the wire" mechanism described in the earlier piece.

That structure is a genuine analogue to how real biogenic-carbon credit accounting works: growing biomass gets provisional credit, and only permanent sequestration (capture and storage, in GCAM's case) converts that provisional credit into something that sticks. But it's an internally consistent accounting identity inside one model's own carbon market — not a certification a real ethanol producer can present to a real regulator. For that, three separate, genuinely different real-world systems exist, and none of them are GCAM.

## 2. Where GCAM actually shows up: an EPA exercise that exposed a real, unresolved disagreement

In February–March 2022 the US EPA ran a public workshop specifically on biofuel greenhouse-gas modeling, in consultation with USDA and DOE, because the agency is legally required under the Renewable Fuel Standard (via the Clean Air Act) to determine whether a given biofuel pathway clears a lifecycle GHG-reduction threshold before it can generate compliance credits. Off the back of that workshop, EPA ran a formal Model Comparison Exercise across five frameworks — ADAGE, GTAP-BIO, GCAM-T, GLOBIOM and GREET (with its separate induced-land-use-change module, CCLUB) — putting the identical corn-ethanol and soybean-biodiesel scenarios through each one.


[T1 "2. Where GCAM actually shows up: an EPA exercise that exposed a real, " 5 rows; use rows by number in a chart "table" spec]
  cols: c0 Model | c1 Developer | c2 Structure | c3 Modelled period
  r0: ADAGE | RTI International | Computable general equilibrium | 2020–2050
  r1: GTAP-BIO | Purdue University | Computable general equilibrium | 2014
  r2: GCAM-T | PNNL | Partial equilibrium | 2020–2050
  r3: GLOBIOM | IIASA | Partial equilibrium | 2020–2050
  r4: GREET + CCLUB | Argonne National Laboratory | Supply-chain LCA + separate induced-land-use module | 2030


The results, published in June 2023 as EPA-420-R-23-017, showed exactly the kind of spread that makes this more than an academic exercise: reported land-use-change GHG estimates for corn ethanol ranged from ADAGE's −0.95 gCO₂e/MJ (implying land-use change was a net carbon sink in that model's run) up to roughly 41 gCO₂e/MJ at the high end across the five frameworks, with GREET's own 2020 estimate landing at 7.4 gCO₂e/MJ. EPA's own framing of the exercise's goal was blunt: "identify differences across the models and understand how these differences affect biofuel GHG estimates." The five models don't just disagree on structure (three are documented as partial-equilibrium, two as general-equilibrium) and disagree on which historical year they're calibrated to — 2014 for GTAP-BIO's baseline versus 2020–2050 for GCAM-T and GLOBIOM versus 2030 for GREET — they disagree on the number that, in the real RFS program, is the difference between a fuel batch clearing its GHG threshold or not.

Caveat. This spread is specifically the land-use-change component of lifecycle emissions, not the full lifecycle carbon intensity number regulators ultimately use (which also includes farming, processing, and transport emissions that the models agree on far more closely). Land-use change is the single most contested piece precisely because it depends on how each model represents land availability, competition between food/feed/fuel/forestry, and how far the ripple effects of one country's biofuel mandate are traced through global trade — which is exactly the kind of cross-system question GCAM's architecture (described in the earlier piece) is built to trace, and exactly why its answer differs from a narrower supply-chain tool like GREET.

## 3. Even inside one model family, how you draw "available land" swings the number by a third

A separate, more targeted study makes the same point without needing five different models at all: it ran three variants of the same GCAM v5.1.2 base (labelled GCAM-T) that differ only in how much non-commercial land is protected from conversion. The baseline variant protects 36% of non-commercial land, empirically calibrated; a stricter "90% Protection" variant assumes the default GCAM v5.1 approach of protecting 90% of it; a third variant mimics GTAP-BIO's structure by eliminating the non-commercial land category altogether, forcing every land conversion onto already-commercial cropland, pasture and forestry.

Switching land-protection assumptions alone — nothing else in the model — moved the resulting land-use-change carbon-intensity estimate by 7 gCO₂e/MJ (19%) between the baseline and the GTAP-style variant, and by 11 gCO₂e/MJ (32%) between the baseline and the 90%-protection variant. The study ranks land representation as the third most influential parameter on the final number, behind only the assumed competition dynamics between forest, grassland and cropland, and the assumed soil carbon density. None of this is a modelling error being caught and fixed — it's a real, documented sensitivity: the same model, same code, same scenario, produces a meaningfully different carbon-credit-relevant number purely from a defensible methodological choice about what counts as "available" land.

## 4. Three real systems, three different architectures — and none of them run GCAM as the compliance engine

With that spread as the backdrop, here is what each of the world's three major biofuel carbon-credit systems actually does, mechanically:


[T2 "4. Three real systems, three different architectures — and none of the" 3 rows; use rows by number in a chart "table" spec]
  cols: c0 System | c1 Jurisdiction | c2 Unit | c3 Mechanism | c4 Underlying LCA tool
  r0: RIN (RFS) | United States | 1 gallon ethanol = 1 RIN; 1 gallon biodiesel = 1.5 RINs | Tradable volumetric credit, tiered by GHG-reduction category (conventional ≥20%, advanced/BBD ≥50%, cellulosic ≥60% vs 2005 petroleum baseline) | EPA-approved pathway-specific LCA (GREET-based determinations); GCAM used only in the separate, non-binding model comparison exercise above
  r1: RED II / RED III | European Union | Pass/fail GHG-savings threshold, not a traded quantity | A fuel either clears the threshold and counts toward national renewable targets, or it doesn't — thresholds tightened from 35% (pre-2017) to 50% (plants operating by 5 October 2015), 60% (started 2015–2020) and 65% (started from 2021); RED III left these transport thresholds unchanged and set 70–80% only for biomass used for electricity, heating and cooling | European Commission default emission values, Annex V/Article 31 methodology — a centrally prescribed formula, not an open multi-model competition
  r2: CBIO (RenovaBio) | Brazil | 1 CBIO = 1 tonne CO₂e avoided vs. fossil baseline | Tradable decarbonisation credit, traded on the B3 stock exchange, issued per certified production unit | RenovaCalc, Brazil's own lifecycle tool, third-party-verified per mill


The three designs solve the same underlying problem — how much less carbon does this fuel really cost, and how should that be rewarded — with three structurally different answers. The US treats it as a tiered, tradable commodity market where the tier a fuel qualifies for depends on a contested lifecycle number. The EU treats it as a regulatory gate with no market in the credit itself, calculated off a centrally fixed formula rather than each producer's own submitted data. Brazil treats it as a directly tradable, tonne-denominated credit, verified mill-by-mill against the country's own calculator. Independent life-cycle work on Brazilian sugarcane ethanol, run through the GREET model using data actually submitted under RenovaBio, put its carbon intensity at 35.2 gCO₂e/MJ — a 62% reduction against US gasoline blendstock, before land-use change is even added — giving a real, checkable cross-system comparison point against the corn-ethanol land-use-change spread from Section 2.

GCAM is the compliance engine for none of the three. Its actual, demonstrated role — the EPA exercise, the land-representation sensitivity study — is as an independent, economy-wide check on narrower supply-chain LCA tools like GREET and RenovaCalc, precisely because its architecture (five systems solved jointly through prices, described in the earlier piece) can trace indirect land-use change through global agricultural trade in a way a single-pathway LCA tool structurally cannot. That breadth is also exactly why GCAM's numbers disagree with the narrower tools as much as they do — it isn't answering a subtly different version of the same question, it's tracing a longer causal chain to get there.

## 5. Where India actually stands in this picture

The GCAM-CEEW build discussed on this site is a real, published, India-specific version of GCAM. But it is not, at the time of the sources checked for this piece, the tool being used for India's own ethanol land-use and sustainability tradeoff work. A PLOS ONE study modelling India's 20% ethanol-blending mandate's trade-offs against land, nitrogen emissions and food security used MAgPIE, a different global land-use partial-equilibrium model, not GCAM — finding that molasses-heavy blending pathways increase land-use-change and fertiliser emissions, while sugarcane-juice-heavy pathways can turn into a net carbon removal of 8–9 Mt CO₂e/year by 2050, with an all-sugarcane-juice scenario swinging from +46 Mt CO₂e/year of land-use emissions by 2030 to −11 Mt CO₂e/year by 2050 as afforestation catches up. Separately, CSTEP's own 2024 work on India's transport decarbonisation and biofuel trade-offs used SAFARI, a system-dynamics model built in-house, again not GCAM.

Context. This isn't a criticism of either study — MAgPIE and SAFARI are each purpose-built for exactly this question. It's a genuine gap worth naming plainly: India already has an India-specific GCAM build with detailed energy and macroeconomic representation (covered in the earlier piece), but its own ethanol land-use and carbon-credit-relevant work is currently being done with other tools. Whether that changes is a live question, not something this piece can resolve.

## What this actually settles

GCAM's biofuel carbon accounting is real, internally consistent, and philosophically close to how a biogenic-carbon credit ought to work — provisional credit at growth, repaid at combustion, kept only with permanent sequestration. But that accounting lives inside GCAM's own model economy. In the actual world, three different governments have built three structurally different real systems to answer the same question, and GCAM's demonstrated, checkable role in that world is as an independent, wider-lens cross-check on the narrower tools those systems actually run — a role that produced a genuinely useful finding (the models disagree by tens of grams of CO₂e per megajoule) precisely because it disagrees with them, not despite it.

Sources: Zhang, X. et al., "GCAM-CDR v1.0: enhancing the representation of carbon dioxide removal technologies and policies in an integrated assessment model," Geoscientific Model Development, 16, 1105–1129 (2023), on GCAM's biofuel/BECCS carbon subsidy-and-repayment mechanism; US EPA, "Workshop on Biofuel Greenhouse Gas Modeling" (epa.gov/renewable-fuel-standard) and the resulting Model Comparison Exercise Technical Document, EPA-420-R-23-017 (June 2023), covering ADAGE, GTAP-BIO, GCAM-T, GLOBIOM and GREET+CCLUB; EPA presentation slides on the Model Comparison Exercise (Ramig, foragforum.org, March 2024), for model-structure and calibration-year detail; a peer-reviewed study on land-representation sensitivity in modified GCAM v5.1.2 (GCAM-T variants), PMC9132210, for the 19%/32% carbon-intensity swings from land-protection assumptions; US EPA and Growth Energy materials on Renewable Identification Numbers (RINs) under the Renewable Fuel Standard; IEA and ICCT summaries of the EU Renewable Energy Directive (RED II/RED III) GHG-savings thresholds, and (added 7 November 2026) the 2BSvs voluntary scheme’s RED III guidance quoting Article 29(10) and Annex V/Article 31 methodology; UNICA and peer-reviewed sources on Brazil's RenovaBio programme, CBIOs and the RenovaCalc lifecycle tool; a peer-reviewed GREET-model evaluation of Brazilian sugarcane ethanol carbon intensity using RenovaBio-submitted data, PMC10433513; a PLOS ONE study on India's biofuel-blending land-use, nitrogen and food-security trade-offs using the MAgPIE model; CSTEP's 2024 work on India's transport decarbonisation trade-offs using the SAFARI system-dynamics model. An earlier piece on this site, "Price Is the Wire," covers GCAM's own five-system architecture and the India-specific GCAM-CEEW/GCAM-IIM build in more depth.

Revision history.

- v1.0.0 — 13 August 2026 — first published.

- v1.0.1 — 7 November 2026 — corrected the EU greenhouse-gas savings thresholds for transport biofuels and the RED annex reference.

Related on this blog: [RIN, RED and CBIO: What India's Ethanol Programme Could Borrow From Three Different Carbon-Credit Machines](https://blog.vertistratsolution.com/2026/08/rin-red-and-cbio-what-indias-ethanol.html) · [Ethanol's Coal Boilers, the Briquette Gap, and What US Carbon Capture Actually Delivers](https://blog.vertistratsolution.com/2026/08/ethanols-coal-boilers-briquette-gap-and.html) — on the two carbon-accounting questions this piece's land-use-change numbers feed into: what a credit-trading system built on those numbers should look like, and what a distillery's own fuel choice actually costs in practice.

## What would fix this

[kept verbatim, open: What would fix this; 4 items]
