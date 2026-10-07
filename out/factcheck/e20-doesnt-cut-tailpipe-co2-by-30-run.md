# Fact/interpretation check — e20-doesnt-cut-tailpipe-co2-by-30-run

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/e20-doesnt-cut-tailpipe-co2-by-30-run.html`

Text-SHA1: `1315a48f0911ddc9`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Road Transport Minister Nitin Gadkari's written Lok Sabha reply of 30 July 2026, states that E20 can reduce fuel efficiency by 2% to 6%" — The article references future/fictional events and dates (July and September 2026) that post-date reality and cannot be verified as factual past events. [confidence: high]

INTERPRETATION ERRORS:
- "a reader does not care about CO2 per litre burned. They care about CO2 per kilometre driven. And because ethanol's energy-content ratio to petrol (65.8%) and its carbon-content ratio to petrol (66.1%) are almost identical, the extra fuel a car must burn to cover the energy shortfall very nearly cancels the lower carbon content of that fuel. Run the arithmetic for a fully uncompensated engine [...] and the net change in CO2 per kilometre driven [...] comes out at essentially zero" — The reasoning assumes that a vehicle's volumetric fuel consumption scales inversely and linearly with the lower heating value (LHV) of the fuel blend. In internal combustion engines, thermal efficiency is also a function of octane rating and compression ratio; higher ethanol blends increase the octane rating, which can partially offset thermal efficiency losses even in uncalibrated or legacy engines, meaning the energy shortfall does not translate to a 1:1 increase in physical volume burned. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India's ethanol-blending programme has live test data at exactly two blend levels"* — The claim that **no Indian body has published a directly tested mileage figure for E5, E15, E25, or E30** is **partially misleading**. While **no official, peer-reviewed or government-published data** exists for these blends, **ARAI is reported to be evaluating E25’s effect on E10/E20-compliant vehicles** (as stated in the article itself). This suggests **some testing is underway**, even if unpublished. The phrasing risks implying **zero testing** has occurred for these blends, which is not strictly true. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"The 30%+ figures attached to E20 in Indian coverage appear to conflate... tailpipe CO2 reduction... and lifecycle GHG claims"* — **While the article correctly identifies the conflation, it overstates the discrepancy in lifecycle claims**. The piece cites **NITI Aayog’s roadmap (2021) suggesting ~65% lower GHG for sugarcane ethanol and ~50% for maize**, which—when applied proportionally to E20—would imply **~10–13% lifecycle reduction at E20**. However, the article later states:
  > *"several secondary sources state a round '40%' without a traceable derivation"*
  This **does not fully reconcile the gap**: The **65% pure-ethanol figure** (if applied linearly) would yield **~13% at E20**, not 40%. The **40% claim likely stems from either**:
  1. **Double-counting** (e.g., adding tailpipe CO2 + lifecycle benefits), or
  2. **A misinterpretation of feedstock-specific credits** (e.g., including indirect land-use changes or non-GHG benefits like CO/HC reductions).
  The article **does not explore whether the 40% figure could arise from a different methodology** (e.g., well-to-wheel including upstream ethanol production inefficiencies). [confidence: high]

---

**OUTDATED DATA:**
- *"India's E20 petrol mandate is routinely credited with cutting vehicle CO2 emissions by roughly 30%"* — **No direct outdated data issue**, but the **source for the "30%" claim is not pinned to a specific official document**. The article relies on **secondary citations (PRS India, IEA policy database)** rather than the **primary NITI Aayog roadmap (2021)**, which was **unreachable for direct verification**. To confirm whether the **30% figure originated from a specific government statement (e.g., a 2020–2021 policy brief) or was a media aggregation**, readers should:
  - Check the **original NITI Aayog roadmap (2021)** for the first appearance of the 30% claim.
  - Cross-reference with **earlier government press releases** (e.g., PIB statements from 2018–2020) or **SIAM/ARAI communications** from the E20 rollout phase.
  [confidence: high]
