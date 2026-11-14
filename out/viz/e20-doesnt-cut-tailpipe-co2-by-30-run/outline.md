Revised
18 September 2026
· v1.0.0 · [what changed](#changelog)

65.8%ethanol's energy density as a share of petrol's

6.8%maximum per-litre tailpipe CO2 cut at E20 (stoichiometric)

~0%net per-km CO2 cut at E20 in an uncalibrated engine

2–6%India's own measured E20 mileage loss range (govt. data)

India's E20 petrol mandate is routinely credited with cutting vehicle CO2 emissions by roughly 30%, and lifecycle claims for the programme run as high as 40–65%. The government's own written Lok Sabha reply of 30 July 2026 repeats a version of the first claim, putting E20’s CO2 cut at about 30% compared with E10; the reports of that reply do not say whether this is per kilometre, at the tailpipe or over the fuel’s lifecycle. Neither of those numbers survives being checked against the same combustion chemistry that produces India's own measured mileage-loss figures. This piece runs that chemistry across the full blend ladder — E0 through E30, in 5-point steps — and is explicit throughout about which numbers are real Indian test data, which are this piece's own first-principles calculations, and which are official claims this piece could not reconcile.

[kept verbatim: dated update notes]

## What India has actually measured: two points on the ladder

India's ethanol-blending programme has live test data at exactly two blend levels. The government's most recent figure, from Road Transport Minister Nitin Gadkari's written Lok Sabha reply of 30 July 2026, states that E20 can reduce fuel efficiency by 2% to 6%, depending on vehicle category and age; that figure comes from a single PTI report of the reply. A reply a week earlier, on 23 July 2026, put the loss at 3–5% for vehicles built for E10. That range matches the more detailed breakdown in the NITI Aayog-commissioned Expert Committee roadmap (via ARAI/SIAM/IOCL joint testing, June 2021): roughly 6–7% mileage loss for four-wheelers designed for E0 and only calibrated for E10, 3–4% for two-wheelers in the same category, and 1–2% for four-wheelers actually designed and calibrated for E10→E20. SIAM's own independent figure for E20 is 2–4%. No Indian body has published a directly tested mileage figure for E5, E15, E25 or E30 — ARAI is reported to be evaluating E25's effect on E10/E20-compliant vehicles, but that work is not yet public.

Every figure for E5, E15, E25 and E30 mileage in this piece is this blog's own calculation, not an official measurement. They are derived below from the energy-density gap between ethanol and petrol — a defensible ceiling, not a substitute for the vehicle testing that does not yet exist at those blend levels.

## The energy-content ceiling: what pure physics predicts, at every 5-point step

Ethanol's lower heating value (about 26.8 MJ/kg at a density of 0.789 kg/L, giving roughly 21.15 MJ/L) is 65.8% of petrol's (about 43.4 MJ/kg at 0.74 kg/L, roughly 32.12 MJ/L) — consistent with this blog's own earlier reporting of a 66% ratio. Blending the two on a simple volumetric basis, with no engine compensation at all, gives the maximum mileage loss physics allows at each blend level:


[T1 "The energy-content ceiling: what pure physics predicts, at every 5-poi" 7 rows; use rows by number in a chart "table" spec]
  cols: c0 Blend | c1 Energy density, MJ/L | c2 Energy-ceiling mileage loss vs E0, % | c3 India's own measured range, %
  r0: E0 (pure petrol) | 32.12 | 0.0 | —
  r1: E5 | 31.57 | 1.7 | not tested
  r2: E10 | 31.02 | 3.4 | up to ~4 (SIAM, implied)
  r3: E15 | 30.47 | 5.1 | not tested
  r4: E20 | 29.92 | 6.8 | 2–6 (Gadkari, 30 Jul 2026); 3–5 in E10 vehicles (23 Jul 2026 reply); 1–7 by vehicle category (NITI/ARAI)
  r5: E25 | 29.37 | 8.5 | ARAI testing reported underway, unpublished
  r6: E30 | 28.82 | 10.2 | not tested


The measured E20 range brackets the energy-ceiling figure of 6.8% almost exactly at its upper end (uncalibrated engines) and sits well below it at the lower end (engines actually tuned for the blend) — which is the whole story in miniature: engine calibration can claw back most, but not all, of the pure energy-content loss. It cannot exceed it.

## The combustion-CO2 ladder, from the same physics

The same blending arithmetic, applied to each fuel's carbon content instead of its energy content, gives the maximum tailpipe CO2 reduction per litre burned. Petrol (modelled as octane, C8H18) emits about 2.281 kg CO2 per litre burned; ethanol (C2H5OH) emits about 1.507 kg CO2 per litre — 66.1% of petrol's, almost the identical ratio to the energy-content figure above, because both differences trace to the same underlying fact: ethanol already carries an oxygen atom, so it releases less energy and less carbon per litre than a hydrocarbon does.


[T2 "The combustion-CO2 ladder, from the same physics" 7 rows; use rows by number in a chart "table" spec]
  cols: c0 Blend | c1 CO2 per litre burned, kg | c2 Per-litre CO2 cut vs E0, %
  r0: E0 | 2.281 | 0.0
  r1: E5 | 2.242 | 1.7
  r2: E10 | 2.203 | 3.4
  r3: E15 | 2.165 | 5.1
  r4: E20 | 2.126 | 6.8
  r5: E25 | 2.087 | 8.5
  r6: E30 | 2.049 | 10.2


At E20, burning a litre of blended fuel releases 6.8% less CO2 than burning a litre of pure petrol — nowhere close to the 30% figure attached to E20 in most press and even some official coverage.

## Why the two ladders nearly cancel each other out

Here is the part that does not get said out loud often enough: a reader does not care about CO2 per litre burned. They care about CO2 per kilometre driven. And because ethanol's energy-content ratio to petrol (65.8%) and its carbon-content ratio to petrol (66.1%) are almost identical, the extra fuel a car must burn to cover the energy shortfall very nearly cancels the lower carbon content of that fuel. Run the arithmetic for a fully uncompensated engine — one whose mileage loss exactly tracks the energy-ceiling numbers above — and the net change in CO2 per kilometre driven, at every blend level from E5 to E30, comes out at essentially zero (within a few hundredths of a percentage point).

This is why engine calibration is the whole ballgame. A net tailpipe CO2 benefit only appears once an engine is tuned to claw back some of the mileage loss — exploiting ethanol's higher octane rating to run a bit more efficiently than the pure energy-content math implies. Using India's own measured E20 mileage-loss range: an uncalibrated vehicle (6–7% mileage loss) gets close to zero net tailpipe CO2 benefit from switching to E20. A vehicle actually designed and calibrated for E20 (1–2% mileage loss) gets a real, positive net benefit of roughly 5% less CO2 per kilometre — genuine, but still a long way from 30%.

## Where the bigger numbers actually come from

The 30%+ figures attached to E20 in Indian coverage appear to conflate at least two different claims that are not the same measurement:

- Tailpipe CO and HC reduction — NITI Aayog's roadmap cites real reductions in carbon monoxide (around 50% for two-wheelers, 30% for four-wheelers) and unburnt hydrocarbons at E20. These are genuine and chemically sound: ethanol's oxygen content improves combustion completeness, so it really does cut CO and HC sharply. But CO and HC are not CO2, and a large cut in one is sometimes reported as if it were the CO2 figure.

- Lifecycle (well-to-wheel) GHG claims — separate from tailpipe combustion, NITI Aayog's own lifecycle figures for pure ethanol versus pure petrol cite roughly 65% lower GHG for sugarcane-based ethanol and roughly 50% lower for maize-based ethanol, capturing upstream effects like avoided crude extraction and refining, and (for sugarcane) bagasse cogeneration credits. Applied in proportion to a 20% blend fraction, that would imply a lifecycle GHG cut on the order of 10–13% at E20 — well above the pure tailpipe figure this piece derives, but still not 30–40%. This piece could not locate an official document that states a clean, methodology-attached "X% lifecycle reduction at E20" figure reconciling with the feedstock-specific numbers; several secondary sources state a round "40%" without a traceable derivation, and it is flagged here as unreconciled rather than repeated.

Government domains were not reachable to verify this section against the primary NITI Aayog roadmap PDF directly from this research environment. The CO/HC and feedstock-specific lifecycle figures above come from secondary citations of that roadmap (PRS India's legislative summary, IEA's policy database), not the primary document itself. Treat this section's official-claim figures as reported, not independently confirmed against the source PDF.

## The case against grain-based ethanol's lifecycle numbers

Independent of the reconciliation problem above, several analysts argue India's official lifecycle-GHG framing is too generous specifically for the feedstock India has leaned on hardest — maize and, increasingly, surplus FCI rice, rather than sugarcane. IEEFA's 2022 assessment argued food-crop ethanol is a land-inefficient climate lever, estimating the full blending roadmap could need roughly 30,000 additional sq km under cultivation. The ICCT's global lifecycle work on food-grain ethanol found its carbon intensity only about 22% below petrol in some markets — which would translate to a lifecycle cut of only a few percentage points at low blend levels, far below headline claims. And an India-specific analysis (Ideas for India, 2026) on rice-based ethanol argues that once post-harvest transport, processing energy and effluent treatment are counted, the net environmental benefit of that specific pathway is "negligible, if not negative." None of these fully settle the question; they are cited here as a genuine, credentialed counter-argument to the official lifecycle figures, not as a rebuttal this piece treats as final.

## The good, separated from the overstated

Stripped of the inflated CO2 number, the case for blending still has real components: measurable CO/HC reductions at the tailpipe, a genuine (if smaller than advertised) net CO2-per-km benefit in calibrated vehicles, avoided crude-oil imports and the forex/farmer-income effects this blog has covered separately (see the cross-links below), and octane benefits that support more efficient engine designs over time. What does not hold up is the specific claim that switching to E20 alone cuts a car's CO2 output by something close to a third — that number is not supported by the combustion chemistry of the fuels actually being blended.

## The takeaway

India has real, government-tested mileage data at exactly two points on the ethanol ladder, E10 and E20, and no tested emissions ladder at all — only headline claims that mix tailpipe CO2, tailpipe CO/HC, and lifecycle GHG into one number. Run the physics honestly across the full E0–E30 range and the story is more modest than the marketing: a real but small net CO2-per-km benefit that depends entirely on whether the engine burning the fuel was built for it.

Sources: fuel energy-density and combustion-CO2 figures calculated directly for this piece from standard physical constants (petrol modelled as octane C8H18, ~43.4 MJ/kg LHV, ~0.74 kg/L; ethanol C2H5OH, ~26.8 MJ/kg LHV, ~0.789 kg/L density) — the calculation method is shown in full above so it can be checked or repeated. Mileage figures: Lok Sabha written reply by the Minister of Road Transport and Highways, 30 July 2026 (reported by Scroll.in, The Federal, Outlook Business); NITI Aayog Expert Committee, "Roadmap for Ethanol Blending in India 2020-25" (June 2021, via ARAI/SIAM/IOCL joint testing), accessed via PRS India's summary and the IEA policy database, not the primary PDF directly (niti.gov.in unreachable from this research environment). Critical literature: IEEFA, "India's Ethanol Roadmap Off Course" (March 2022); ICCT life-cycle GHG report (July 2025); Ideas for India, rice-ethanol lifecycle analysis (2026).

### Related on this blog

See also: [Blending on a Budget: Energy Density and Cost Per Kilometre, Across Four Fuel Pairs](https://blog.vertistratsolution.com/2026/08/blending-on-budget-energy-density-and.html) · [Annadata to Urjadata: The Farmer-Income Case for Ethanol Blending](https://blog.vertistratsolution.com/2026/08/annadata-to-urjadata-farmer-income-case.html) · [Ethanol Freed Up Refinery Capacity for Petrochemicals](https://blog.vertistratsolution.com/2026/09/ethanol-freed-up-refinery-capacity-for.html) · [India Hit E20 on Maize and Rice, Not Sugarcane](https://blog.vertistratsolution.com/2026/08/india-hit-e20-on-maize-and-rice-not.html).

Revision history.

- v1.0.0 — 18 September 2026 — first published.

## What would fix this

[kept verbatim, open: What would fix this; 4 items]
