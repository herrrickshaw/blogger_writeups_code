[kept verbatim: dated update notes]

## 1. The trigger: an oversupplied ethanol tender meets an LPG supply gap

An earlier piece on this site, drawing on CareEdge-sourced tender data, put a number on the scale of the surplus: grain-based ethanol producers alone offered 13,040 million litres for ESY2025-26 against OMCs' combined stated requirement of roughly 10,500 million litres, and the total industry-wide offer — grain plus sugarcane-based — came to approximately 17,760 million litres, an oversubscription of about 1.7× the requirement. That capacity is idle the moment it isn't absorbed by the blending mandate, and it sets up an obvious question: if ethanol can safely take a larger share of the petrol pool (moving from E20 toward E25 or beyond), refineries need somewhere else useful to put the petrol-equivalent crude fraction that ethanol is no longer leaving room for. Update, 26 September 2026: the regulatory groundwork for this has moved since this piece's earlier coverage was first written. BIS has since notified technical standards for E22, E25, E27 and E30 blends (IS 19850:2026, effective 15 May 2026), and the central excise exemption already available on petrol up to E20 has been extended to those higher blends too — neither of which is, or ever was, a GST Council decision specifically, since petrol sits outside GST. What has not happened is an actual blending-mandate rollout: the petroleum ministry has directed ARAI to study E25's effect on engine life and mileage in the existing E10/E20-compliant vehicle fleet first, and government sources describe the excise notification as a prerequisite, not a rollout announcement. The oversupply argument in this section holds regardless of which specific gate E25 clears next.

Jamnagar, the refining complex where FCC gas-recovery modifications like the ones described here would trade petrol yield for LPG. [Jamnagar Refinery.jpg](https://commons.wikimedia.org/wiki/File:Jamnagar_Refinery.jpg), Reliance Industries, CC BY-SA 4.0, via Wikimedia Commons.

One answer, raised directly in industry correspondence on this question and grounded in real refining engineering: redirect that freed-up FCC (fluid catalytic cracking) capacity toward LPG instead of more petrol. India's LPG supply position makes this more than an efficiency exercise — the country imports a substantial share of its LPG consumption, and any domestic yield shift that reduces that import bill is a genuine, quantifiable win, not just a refining-margin optimisation.

## 2. What "tweaking the FCC" actually means

The FCC unit is the workhorse that cracks heavy crude fractions into lighter, more valuable products — primarily petrol (gasoline), with LPG-range C3/C4 hydrocarbons and heavier cycle oils as co-products. Shifting the unit's output mix toward more LPG at petrol's expense is a real, well-documented refining lever, detailed in a technical paper from Process Consulting Services published in PTQ (Petroleum Technology Quarterly) via Digital Refining, the industry's own refining-technology publication — not a hypothetical.

Three levers move the yield: catalyst formulation changes (a ZSM-5 additive specifically cracks mid-boiling-range gasoline molecules down into LPG-range C3/C4), higher reactor temperature, and converter (reactor/regenerator) technology modifications. All three increase what the paper calls reactor wt% C3 yield — and critically, the paper's own recommendation is not to chase the highest possible yield: a moderate increase (reactor wt% C3 yields of 7.5–13.1%) fits existing operational and capital constraints better than an aggressive high-C3+ target, because every incremental point of yield cascades into equipment the refinery has to be able to compress, condense and recover it with.

7.5–13.1%Reactor wt% C3 yield range the paper recommends targeting — a moderate increase, not a maximum one, to fit existing capital constraints

90–99%Typical C3+ (propylene/LPG) recovery rate in the downstream absorber/stripper gas plant, depending on operating parameters and equipment limits

1.7×ESY2025-26 ethanol tender oversubscription, per CareEdge-sourced data — the demand-side trigger for this entire question

The catch is that the reactor yield shift is the easy part. Everything downstream of the converter — the wet gas compressor (WGC), the main-column overhead receiver, and the absorber/stripper system that recovers LPG from the wet gas stream — has to handle a higher wet gas flow rate (WGFR). The paper is explicit that replacing the WGC or its driver is a high-cost outcome refiners should try to avoid; the more cost-effective path is a set of targeted debottlenecking modifications, most of which reduce pressure drop (ΔP) rather than add new major equipment:


[T1 "2. What "tweaking the FCC" actually means" 8 rows; use rows by number in a chart "table" spec]
  cols: c0 Modification | c1 ΔP reduction, psi
  r0: Eliminate feed nozzle coke | 2–4
  r1: Main column trays to packing | 2–4
  r2: Air fin-fan bundles | 2–5
  r3: Eliminate wet gas flow meter | 1–2
  r4: CW trim cooler bundles | Varies (case-specific)
  r5: Additional cooling-water flow rate | Varies (case-specific)
  r6: Replace high-ΔP piping | Varies (case-specific)
  r7: Reduce condensing load (additional pumparound cooling) | Varies (case-specific)


Source: Campbell, D., Barletta, T., Golden, S. (Process Consulting Services), "Mitigating FCC gas plant impacts when increasing reactor LPG yields," PTQ Q2 2023, published via Digital Refining (www.digitalrefining.com). ΔP = pressure drop; reducing it lowers the wet gas compressor's suction pressure requirement, freeing compressor capacity without a full replacement.

One detail worth pulling out on its own: the paper notes that identifying these opportunities starts with detailed pressure surveys — physically measuring pressure drop across individual piping segments and equipment — because these field measurements are more accurate than calculation-tool results alone. The paper's own framing is notable: "even today, when technology allows such things as 'digital twins', old-school field measurements still have value." That is a useful corrective to a narrative (including in an earlier piece's coverage of India's petrochemical pivot) that treats digital-refining tools as a wholesale replacement for physical plant instrumentation, rather than a complement to it — the cheapest debottlenecking wins in this specific FCC-yield-shift case still come from a technician with a pressure gauge, not a simulation alone.

## 3. LPG/propylene from the FCC is a different lever from the naphtha-cracker pivot

It would be easy to fold this into the broader "India's refiners are pivoting toward petrochemicals" story — the subject of an earlier piece on this site, which tracked the Petrochemical Intensity Index (PII) rising from 7.7% to 13% nationally, IOCL's ₹1 trillion push to more than double its own PII, and the Nagapattinam/Manali reconfiguration in Tamil Nadu. But it is worth being precise about the mechanism, because they are not the same lever, even though both point in the same broad direction — less transport fuel, more chemical feedstock.

The naphtha-cracker route (an earlier piece's coverage) is about building new capability to produce chemical-grade naphtha — a heavier distillate cut than LPG — and feeding it into steam crackers for ethylene and downstream polymers like LDPE/LLDPE and PET. That piece flagged a real constraint: India actually imports petrochemical-grade naphtha because domestic naphtha isn't consistently produced to chemical-grade specification, ending up burned as industrial fuel instead.

The FCC-yield-shift lever described here works on a lighter, earlier cut of the barrel — propane and butane (C3/C4, the LPG range), recovered as propylene and LPG directly out of the FCC's own gas plant, at the expense of gasoline rather than at the expense of naphtha production. The two levers can, in principle, run in parallel on the same refinery — a unit reconfigured for higher PII and a unit tweaked for higher FCC LPG yield are pulling on different fractions of the same crude barrel — but conflating them would overstate how much a single investment decision buys. This piece treats them as complementary, not identical.

The tension the email correspondence itself raises, and which remains unresolved in public reporting: C3/C4 olefins recovered from a higher-yield FCC gas plant are also the feedstock for polypropylene (PP) and butadiene — petrochemical products, not cooking gas. If refiners route the incremental C3/C4 toward petrochemical sale rather than LPG cylinders, the LPG-import-substitution goal this entire shift is nominally aimed at doesn't actually get met. That allocation choice — LPG for households versus feedstock for petrochemical plants — is a real, unresolved policy and commercial question this piece is flagging, not one it can answer from public data.

## 4. The other side of the ledger: room to store the crude behind this diversification

A parallel and independently-verified push is underway to expand India's underground strategic crude storage, run by Indian Strategic Petroleum Reserves Limited (ISPRL) — relevant here because more storage buffer is what makes it safer for refiners to run these kinds of yield experiments and diversify crude sourcing without being caught short on a supply disruption.


[T2 "4. The other side of the ledger: room to store the crude behind this d" 3 rows; use rows by number in a chart "table" spec]
  cols: c0 Site | c1 Capacity, MMT | c2 Status, as independently reported
  r0: Bikaner, Rajasthan (salt cavern) | ~5 | Feasibility study by Engineers India Limited (EIL); would be India's first salt-cavern-based reserve and first gas reserve if it proceeds
  r1: Mangalore, Karnataka (Phase-I extension) | 1.75 | ONGC board gave in-principle approval, July 2026 — adds to the existing 1.5 MMT Mangalore facility
  r2: Bina, Madhya Pradesh (rock cavern) | 1–1.5 | Pre-feasibility study by EIL; sited inland specifically to support northern refineries during supply emergencies, unlike the existing coastal reserves


Sources: PSU Watch, "Exclusive: ISPRL exploring possibility of creating gas, Green Hydrogen reserves in Bikaner & Bina"; ANI/Tribune/India Infoline, "ONGC Board approves 1.75 MMT strategic petroleum reserve project at Mangalore" (July 2026). The Mangalore figure updates an earlier 1.5 MMT DPR-stage figure referenced in industry correspondence circulating in March 2026; this piece reports the more recent, board-approved 1.75 MMT figure as the current status. India's existing ISPRL reserves total 5.33 MMT across Visakhapatnam (1.33), Mangalore (1.5) and Padur (2.5); ISPRL's own stated ambition is to roughly triple total capacity to about 15 MMT within a decade.

The strategic logic connecting storage expansion to crude-sourcing diversification is straightforward: reducing reliance on the Strait of Hormuz as a transit chokepoint (by sourcing more crude from Nigeria, Guyana, Malaysia and Brunei, alongside existing Gulf and Russian supply) only reduces real risk if the extra shipping distance and lead time is backstopped by more buffer inventory at home. More underground storage capacity is what allows that diversification to happen without leaving refiners exposed during a transit disruption.

## 5. The LPG pipeline network this shift would actually run on

Any increase in domestic LPG output only reaches consumers as fast as the physical network that moves it can carry it. The Petroleum and Natural Gas Regulatory Board's own authorisation registry lists the dedicated LPG pipelines already built or under authorisation, rather than leaving this to estimate:


[T3 "5. The LPG pipeline network this shift would actually run on" 9 rows; use rows by number in a chart "table" spec]
  cols: c0 LPG pipeline | c1 Authorised entity
  r0: Kochi–Coimbatore–Erode–Salem | BPCL-led consortium
  r1: Mangalore–Hassan–Mysore–Sollur | HPCL
  r2: Mundra–Mithi Rohar | Adani Ports & SEZ
  r3: Kandla–Gorakhpur | Consortium of IOCL, BPCL and HPCL
  r4: Hassan–Cherlapalli | HPCL
  r5: Haldia–Panagarh | HPCL
  r6: Jamnagar–Loni | GAIL India
  r7: Uran–Chakan–Shikrapur | HPCL
  r8: Vizag–Secunderabad | GAIL India


Source: PNGRB, Petroleum & Petroleum Product Pipeline authorisation registry (pngrb.gov.in), regulation-5 and regulation-17(1) listings, accessed August 2026. This is the dedicated-LPG subset of a longer registry that also authorises non-LPG product pipelines (ATF, multi-product) and a separate category of dedicated petrochemical-feedstock pipelines, discussed below.

The same registry also lists dedicated pipelines carrying the specific feedstocks the cracker projects in Section 6 are built to run on — concrete evidence that the capital commitments in that table are being matched by physical connecting infrastructure, not standing alone: a liquid-ethane line from Reliance's Hazira manufacturing division to its Nagothane, Maharashtra complex; naphtha lines feeding ONGC Petro Additions' OPaL dual-feed cracker at Dahej from both ONGC Hazira and the Gujarat Chemical Port Terminal; a C2/C3 line running 360 km from GAIL's Vijaipur facility to its Pata petrochemical complex; and a liquid-propane line from BPCL's Uran terminal to GAIL's Usar PDH-PP plant. Read together with Section 6's investment table, these dedicated lines are the connective tissue between a refiner's cracker-investment decision and the specific downstream plant it's meant to feed.

Ethanol-based cooking solutions sit alongside this as a second, complementary demand-side lever — given the same ethanol oversupply discussed in Section 1, ethanol cookstoves could sustain India's clean-cooking transition without demand reverting to solid fuels (coal, wood) or requiring a full shift to induction stoves, which carries its own electrification and grid-capacity dependencies this piece has not evaluated.

## 6. The bigger picture: India's refiners are committing real capital to petrochemicals right now

The FCC-yield lever in Sections 2–3 is a comparatively small, low-capex debottlenecking move next to the scale of capital India's refiners are currently putting into petrochemical capacity outright — new crackers, integrated refinery-petrochemical complexes, and polymer units, several of which broke ground or reached board approval within the last twelve months:


[T4 "6. The bigger picture: India's refiners are committing real capital to" 7 rows; use rows by number in a chart "table" spec]
  cols: c0 Project | c1 Sponsor | c2 Investment, ₹ crore | c3 Scale | c4 Status, as of Aug 2026
  r0: Barmer (Pachpadra), Rajasthan | HPCL Rajasthan Refinery Ltd (JV) | 79,459 | 9 MMTPA refining + 2.4 MMTPA petrochemical | Inaugurated July 2026
  r1: Andhra Pradesh (greenfield) | BPCL & Oil India (JV) | ≈91,000 (~$11bn) | 9–11 MTPA refinery + large ethylene cracker | Planning stage
  r2: Bina, Madhya Pradesh | BPCL | 49,000 | Ethylene cracker integration | Board-approved; targeting FY2027-28 start-up
  r3: Sehore, Madhya Pradesh | GAIL | 60,000 (~$6bn) | 1.5 MMTPA ethane cracker | Announced; ~5–6 year build, targeting c. 2029-30
  r4: Koyali, Gujarat | IOCL | 17,825 | Refining 13.7→18 MMTPA + 500 KTPA polypropylene | Approved
  r5: Kochi, Kerala | BPCL | 5,514 (~$599mn) | Polypropylene unit | Foundation stone laid, March 2026
  r6: Nagapattinam, Tamil Nadu | IOCL / CPCL | 33,023 | Refinery reconfigured toward petrochemicals | Under review — detailed in an earlier piece on this site


Sources: Chemindigest, "IOCL Reviews Nagapattinam Refinery for Petrochemicals"; IOCL corporate media releases; Biltraxmedia and Energies Media, BPCL Bina cracker coverage; Hydrocarbon Processing and Offshore Technology, GAIL ethane cracker coverage; India Infoline and Business Standard, GAIL Sehore petrochemical unit; Business Standard, IOCL Gujarat refinery petrochemical/lube integration. Rupee figures as separately reported; dollar-denominated figures (Andhra Pradesh, GAIL Sehore) converted at approximate contemporaneous rates where a rupee figure wasn't independently available. This piece has not verified whether these seven figures overlap with or duplicate each other's scope (e.g., some GAIL/BPCL reporting on Bina cites overlapping but not identical investment figures across different report dates) — treat each row as a separately-sourced data point, not a reconciled master list.

Two things stand out reading this table alongside the FCC-yield question this piece opened with. First, the sums involved — roughly ₹3.35 lakh crore (~$40 billion) across just these seven projects — dwarf the cost of the debottlenecking modifications in Section 2's table, which is exactly why the FCC-yield lever is attractive as a near-term move: it works with equipment refiners already own, while these seven projects are multi-year capital commitments. Second, three of the seven (Bina, Sehore, and the Andhra Pradesh greenfield) are specifically ethylene/ethane-cracker projects, which is a different feedstock chemistry from both the FCC-LPG lever (propylene/butylene, C3/C4) and the naphtha-cracker route covered in an earlier piece on PII — India's petrochemical build-out is running on at least three distinct feedstock tracks simultaneously (FCC-derived C3/C4, naphtha-derived ethylene, and now ethane-derived ethylene), not one uniform strategy.

Also announced in the Union Budget 2026-27: a new central scheme to help states establish three dedicated Chemical Parks, through a challenge-based selection process, with an initial ₹600 crore budgetary allocation for FY2026-27, approved by the Cabinet on 24 July 2026 as BHAVYA Rasayan, a ₹3,030 crore scheme for three parks by 2030-31 — a much smaller, enabling-infrastructure commitment next to the refiner-led projects above, but a signal that the push extends to state-level industrial-park policy as well as individual refiner capex.

Verdict: The FCC-yield lever is real, technically well-documented, and moderate by design — the paper's own recommendation is 7.5–13.1% reactor C3 yield, not a maximalist redesign. It is a genuinely different mechanism from the naphtha-cracker petrochemical pivot an earlier piece covered separately, working on a lighter cut of the barrel and requiring gas-plant debottlenecking rather than new naphtha-quality capability. Whether it actually reduces India's LPG import bill, rather than simply feeding more C3/C4 into petrochemical production, depends on an allocation choice this piece could not verify from public data. What is independently confirmed is the parallel build-out of underground crude storage — Bikaner, Bina and a newly-approved 1.75 MMT Mangalore extension — which is the buffer capacity that makes crude-sourcing diversification, and refining experiments like this one, less risky to attempt.

### Related on this blog

See also: [The Barrel Really Is Shifting: India's Refiners Quantify the Petrochemical Pivot](https://blog.vertistratsolution.com/2026/08/the-barrel-really-is-shifting-indias.html), [Annadata to Urjadata: The Farmer-Income Case for Ethanol](https://blog.vertistratsolution.com/2026/08/annadata-to-urjadata-farmer-income-case.html), [State tax from ethanol blending in India: Rs 17,863 crore net loss at E20, by state](https://blog.vertistratsolution.com/2026/08/state-by-state-who-actually-earns-from.html), [LPG's Missing Number: A ₹73.08 Commission](https://blog.vertistratsolution.com/2026/08/lpgs-missing-number-7308-commission-and.html)

## What would fix this

[kept verbatim, open: What would fix this; 4 items]
