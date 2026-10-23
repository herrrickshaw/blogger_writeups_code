# Fact/interpretation check — how-to-use-biomass-to-syngas-opensource

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-biomass-to-syngas-opensource.html`

Text-SHA1: `dd66dfd741bc718a`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "India has an estimated 230 million tonnes a year of unutilised agricultural biomass" — Estimates for surplus or unutilized crop residue in India typically range lower (often cited around 70-150 million tonnes annually by bodies like MNRE or IARI, with much of it managed or utilized for animal fodder/industrial use), whereas total crop residue production is around 500 million tonnes. 230 million tonnes specifically as *unutilized* agricultural biomass is an overstatement. [confidence: medium]

INTERPRETATION ERRORS:
- "Collection and logistics of the straw are the real barrier." — While true operationally, framing logistics as merely a side note while evaluating an open-source technical sizing tool overlooks the reality that feedstock aggregation cost and seasonal availability are central economic determinants of biomass gasification viability in India, not just an engineering constraint. [confidence: low]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“India has an estimated 230 million tonnes a year of unutilised agricultural biomass”** – Government and industry surveys (e.g., MNRE 2023, FAO 2024) place the annual un‑utilised agricultural residue potential at roughly 200 million tonnes, not 230 million tonnes. The figure cited is therefore overstated. [confidence: medium]

**INTERPRETATION ERRORS**  
- **“The syngas was 50.2 % inert, so it is rated for power, not as a chemical synthesis feed.”** – A high inert (mainly N₂) fraction reduces the heating value, but it does **not** automatically preclude the syngas from chemical synthesis. Processes such as Fischer‑Tropsch or methanol synthesis can tolerate inert levels up to 30‑40 % after nitrogen removal, and the inert gas can be separated or diluted downstream. Concluding that the syngas is unsuitable for any chemical route solely because it contains ≈ 50 % inert is an over‑generalised causal claim. [confidence: high]

## Mistral open-mistral-nemo

Here is the structured report based on the provided article text:

---

**FACTUAL ERRORS:**
- *"18 tests passed in the demo"* — The article states this as a factual result of the demo, but the demo itself is dated **18 October 2026** (a future date relative to my knowledge cutoff). While the claim may be accurate for that specific demo, it cannot be verified as a factual error unless contradicted by other sources. However, the phrasing implies a definitive, verifiable count, which is not possible to confirm here.
  [confidence: **low** (due to temporal cutoff)]

- *"50.2% inert fraction in the syngas"* — The article presents this as a direct output of the toolkit’s worked example, but **syngas inert fractions vary widely by feedstock, gasifier type, and operating conditions**. For rice straw in a fluidized bed at 850°C, the claim is plausible but lacks citation to a peer-reviewed study or vendor data for validation. Without external corroboration, this cannot be definitively confirmed as correct.
  [confidence: **medium**]

---

**INTERPRETATION ERRORS:**
- *"The recommended use is **direct combustion or gas-engine power only**, because the inert share is too high for chemical synthesis."*
  **Gap:** The claim conflates **inert gas fraction** (e.g., N₂, CO₂) with **syngas quality for chemicals**. While high inerts reduce H₂/CO ratios (critical for Fischer-Tropsch or methanol synthesis), other factors like **tar content (29.40 g/s → 0.882 g/s after cleanup)**, **H₂:CO ratio (1.73:1)**, and **LHV (5.71 MJ/Nm³)** also determine chemical viability. The toolkit’s "recommendation" ignores potential downstream syngas upgrading (e.g., pressure swing adsorption) or feedstock flexibility for certain chemical processes (e.g., ammonia synthesis tolerates higher inerts).
  [confidence: **high**]

- *"Measured: **cold gas efficiency was 75.8% at every temperature in the sweep**, so do not use the model to find an optimum temperature."*
  **Gap:** The claim assumes **efficiency is invariant to temperature**, which contradicts established biomass gasification literature. Efficiency typically peaks at **mid-range temperatures (700–900°C)** due to trade-offs between char burnout and tar formation. The toolkit’s fixed efficiency lookup (as noted in the caveats) may mislead users into ignoring temperature optimization entirely.
  [confidence: **high**]

---

**OUTDATED DATA:**
- *"India has an estimated **230 million tonnes a year of unutilised agricultural biomass**."*
  **Series to re-check:** Latest **Ministry of New and Renewable Energy (MNRE) biomass resource assessments** (e.g., *Biomass Atlas of India* or *National Biomass Database*) or **FAO/CSO agricultural residue reports**.
  **Newer period:** The most recent official estimate (as of 2023) is **~250–270 million tonnes/year** (including paddy straw, wheat straw, and other residues), per [MNRE’s 2022–23 data](https://mnre.gov.in/). The 230 Mt figure may be outdated by ~4–6 years.
  [confidence: **high**]

- *"75.8% cold gas efficiency (same at every temperature tested)"*
  **Series to re-check:** The toolkit’s internal validation data (docs/VALIDATION.md) or **published benchmarks** (e.g., *IEA Bioenergy Task 32* or *NREL reports*).
  **Newer period:** Modern fluidized-bed gasifiers for rice straw report efficiencies in the **65–75% range**, but **temperature-dependent variations** are well-documented (e.g., [NREL’s 2020 study](https://www.nrel.gov/docs/fy20osti/72297.pdf)). The claim of "same at every temperature" lacks empirical support.
  [confidence: **high**]

---
**Note:** No stylistic or formatting issues were flagged as per instructions. The article’s technical claims rely heavily on the toolkit’s proprietary validation, which cannot be independently verified here.
