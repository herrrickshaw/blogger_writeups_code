# Fact/interpretation check — one-gallon-five-numbers-how-gcam-fits

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/one-gallon-five-numbers-how-gcam-fits.html`

Text-SHA1: `8aea8048268297dd`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"GCAM is not the model that actually issues a RIN, clears a RED III threshold, or prices a CBIO on Brazil's B3 exchange"* — **Incorrect framing of RED III compliance.** While GCAM is not the *operational* compliance engine for RED III (the EU uses centrally prescribed Annex IV/Article 31 methodology), the claim conflates *operational* compliance (which is formula-based) with *modeling* used to inform policy debates. The EU does not "run GCAM" for compliance, but the article’s phrasing ("none of the world’s three big biofuel carbon-credit systems run GCAM as their compliance engine") is technically accurate. However, the *subsequent* claim that RED III uses a "centrally prescribed formula" is correct, but the earlier sentence risks implying GCAM is *directly* involved in any of these systems, which it is not. [confidence: **high**]

- *"A PLOS ONE study modelling India's 20% ethanol-blending mandate's trade-offs... used MAgPIE"* — **Outdated citation context.** The article states this as a fact for 2026 but does not verify whether the study was published *after* the 2024 CSTEP work (also cited) or if it aligns with the latest policy context. While the claim may be correct, the lack of a direct link to the PLOS ONE study’s publication date or India’s current regulatory stance (e.g., whether MAgPIE is still the *de facto* tool) makes this a potential factual gap. [confidence: **medium**]

---
**INTERPRETATION ERRORS:**
- *"The five models don’t just disagree on structure... they disagree on the number that, in the real RFS program, is the difference between a fuel batch clearing its GHG threshold or not."* — **Overstating causal impact.** The spread in land-use-change emissions (–0.95 to ~41 gCO₂e/MJ) is *one component* of the full lifecycle carbon intensity (LCI) calculation under the RFS. The article correctly notes that LCI includes farming, processing, and transport emissions (which models agree on more closely), but the phrasing implies the land-use-change spread *alone* decides compliance—a false causal claim. In reality, the *total* LCI (including agreed-upon emissions) determines RIN eligibility, and the spread in land-use change is just one variable among many. [confidence: **high**]

- *"GCAM's real job is... an independent, economy-wide check on narrower supply-chain LCA tools like GREET and RenovaCalc"* — **Misleading analogy.** While GCAM’s global trade and land-use dynamics *can* serve as a "wider-lens cross-check," the article frames this as GCAM’s *primary role* in the compliance ecosystem. However, GCAM’s architecture is fundamentally different from operational systems (RINs, RED III, CBIO), which are designed for *policy enforcement*, not *research validation*. The implication that GCAM’s disagreement with GREET/RenovaCalc is a *useful finding* for compliance is an extrapolation—GCAM’s outputs are not actionable in any of the three systems. [confidence: **high**]

---
**OUTDATED DATA:**
- *"EPA's own 2020 estimate [for GREET] landing at 7.4 gCO₂e/MJ"* — **Series to re-check: EPA’s latest GREET model updates (e.g., GREET 2.20 or later).** The EPA regularly updates GREET with new data (e.g., land-use modules, feedstock yields). As of 2026, the latest GREET version may have revised land-use-change estimates for corn ethanol, particularly if new USDA/NASS data or peer-reviewed studies (e.g., on soil carbon or feedstock expansion) have been incorporated. [confidence: **high**]

- *"CSTEP's own 2024 work on India's transport decarbonisation and biofuel trade-offs used SAFARI"* — **Potential newer updates.** While the article cites CSTEP’s 2024 report, India’s biofuel policy landscape (e.g., ethanol blending mandates, land-use regulations) evolves rapidly. CSTEP or other institutions may have published follow-up work in 2025–2026 incorporating newer data (e.g., 2024–25 crop reports, revised feedstock mixes). The claim assumes CSTEP’s 2024 findings remain current, which may not hold. [confidence: **medium**]

---
**Note:** The article’s core framing (e.g., GCAM’s role, RED III’s methodology, or the RFS’s LCI components) is factually sound but risks overgeneralizing GCAM’s relevance to compliance systems. The "outdated data" section focuses on *specific figures* (GREET 2020, CSTEP 2024) that could be superseded by newer official releases.
