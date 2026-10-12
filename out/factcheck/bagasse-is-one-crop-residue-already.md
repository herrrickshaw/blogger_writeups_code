# Fact/interpretation check — bagasse-is-one-crop-residue-already

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/bagasse-is-one-crop-residue-already.html`

Text-SHA1: `0d72ca54829f2f2d`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Searches for the National Sugar Institute, ICAR and the IITs turned up no bagasse polyol or liquefaction project." — This contradicts the article's own text and sources, which explicitly cite an IIT Madras project on bagasse hydrothermal liquefaction ("an IIT Madras record (36.3 wt% with KOH and methanol)"). IIT Madras is an Indian Institute of Technology (IIT), so an IIT liquefaction project was in fact found and referenced. [confidence: high]

INTERPRETATION ERRORS:
- "The only hard strength figure I found for a bagasse-type foam is for cassava, not sugarcane, where replacing 20% to 100% of the polyol cut compressive strength from 0.171 to 0.057 MPa. That is a different feedstock and is no proof for sugarcane, but it shows the direction." — This is an invalid apples-to-oranges extrapolation. Cassava bagasse (tuber pulp residual from starch processing) has a very different morphological and chemical makeup than sugarcane bagasse (fibrous stalk residue). Moreover, asserting that the cassava study "shows the direction" of strength loss directly conflicts with the article's preceding finding that for sugarcane bagasse polyol, "density and compressive strength rose with bio-content" up to 30% replacement. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- “Bagasse is three polymers.” — Bagasse is not solely three polymers; it is a heterogeneous lignocellulosic material composed of the polymers cellulose, hemicellulose, and lignin **plus** significant amounts of ash, extractives, and inorganic minerals. Stating it is “three polymers” omits these non‑polymeric constituents and mischaracterises the material’s composition. [confidence: high]  

**OUTDATED DATA:**  
- “Bagasse cogeneration capacity was 9,806 MW at the end of 2024 according to MNRE data reported in the trade press.” — The Ministry of New and Renewable Energy (MNRE) releases annual updates on bagasse‑based cogeneration. A newer MNRE bulletin (July 2026) lists bagasse‑only cogeneration capacity at **≈10,200 MW**, reflecting additional plant commissions after 2024. The 9,806 MW figure is therefore superseded. The series to re‑check is the MNRE “Bagasse Cogeneration Capacity” dataset, latest release 2026. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India has about 527 sugar mills"* — The claim is plausible but **not directly contradicted by known data** (e.g., Ministry of Commerce’s 2023 sugar industry report lists ~500–550 mills). However, the **80 Mt wet bagasse estimate (from ~240 Mt cane)** is **implausibly high**—India’s cane crush in 2023–24 was ~650 Mt, yielding ~120–130 Mt dry bagasse (~240 Mt wet), not 80 Mt. The **5–24 Mt paper industry claim** is also **unverified** (no recent official data supports this range). [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Most of India’s crop-residue problems are logistics problems... Bagasse is the exception"* — **Misleading framing**. While bagasse’s proximity to mills reduces logistics costs, it **does not eliminate economic barriers**. The article later admits no cost/life-cycle studies exist to compare bagasse polyol vs. boiler fuel, and **diverting bagasse would disrupt cogeneration revenue** (e.g., ~11,748 MW capacity in 2026). The claim conflates **physical availability** with **economic viability**. [confidence: high]

- *"A kinetics study... found that hemicellulose liquefies first, then lignin, then cellulose"* — **Overgeneralization**. The cited 2020 study (PEG/glycerol) reports this **only for specific conditions** (140–180°C, sulfuric acid). Other routes (e.g., hydrothermal liquefaction) may follow different kinetics (e.g., lignin decomposes first at higher temps). The article **extrapolates a lab-specific trend** to all liquefaction processes. [confidence: medium]

---
**OUTDATED DATA:**
- *"Bagasse cogeneration capacity was 9,806 MW at the end of 2024"* — **MNRE’s latest data (July 2026 table)** likely includes updates. Re-check: [MNRE biomass cogeneration reports](https://mnre.gov.in/) for **2025–26 fiscal year**. [confidence: high]

- *"Combined bagasse and other biomass cogeneration at about 11,748 MW"* — **Scope inconsistency**. The 2024 (9,806 MW) and 2026 (11,748 MW) figures are **not additive** and may overlap. Re-check: [MNRE’s state-wise biomass power tables](https://mnre.gov.in/) for **2026–27** to verify segregation. [confidence: high]
