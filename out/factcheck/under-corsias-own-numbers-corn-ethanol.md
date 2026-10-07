# Fact/interpretation check — under-corsias-own-numbers-corn-ethanol

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/under-corsias-own-numbers-corn-ethanol.html`

Text-SHA1: `b86e6920491ac8cb`

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
- *"India's ethanol policy has been actively promoting maize as a feedstock since November 2023"* — The claim conflates **MoPNG’s PIB release (November 2023)** with **actual policy implementation**. While the PIB noted maize’s potential, the article later acknowledges that **no maize-to-jet SAF capacity exists yet** and that maize ethanol is primarily diverted to road fuel (37% of India’s maize crop). The policy’s *active promotion* for **SAF** (not just road fuel) is unsupported by current certification or production data. [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- *"CORSIA’s own default carbon-intensity tables show corn/maize ethanol-to-jet scores worse than fossil jet fuel, proving it should be ruled out of SAF policy"* — The claim **overgeneralizes** from default values (90.8–100.6 gCO₂e/MJ) to real-world applicability. The article later notes:
  1. **Methodology differences**: The ISCC/ISCC default includes a **heavy ILUC penalty** (not applied uniformly in all models), while the US DOE’s GREET model (69.1–78 gCO₂e/MJ) or academic studies (35–69 gCO₂e/MJ) suggest corn ethanol *could* meet CORSIA’s 10% threshold under alternative assumptions.
  2. **No actual-value certification**: India’s maize ethanol is **not certified** under CORSIA’s current tables—only default values are cited. The article admits: *"A producer would need an actual-value calculation"* (a costly, audited process).
  **Gap**: The claim treats defaults as definitive proof of failure, ignoring that **real-world certification** (not just tables) determines eligibility. [confidence: **high**]

---
**OUTDATED DATA:**
- *"ICAO approved the 8th edition of its default life-cycle emissions table on 19 November 2025"* — The article cites this as a **fact**, but the **8th edition’s methodology changes** (e.g., IPCC 2019 factors, ILUC refinements) **directly affect corn/maize ethanol’s CI**, which the piece admits may now differ. The article **cannot access the 8th edition** (blocked) but infers upward pressure on corn ethanol’s CI due to methodology shifts. **Recommended check**:
  - **Series**: ICAO Document 06 (Life Cycle Emissions Tables)
  - **Newer period**: 8th edition (November 2025) + any 2026 updates.
  [confidence: **high**]

---
**OUTDATED DATA (additional):**
- *"94% share of India’s used cooking oil (UCO) goes uncollected"* — The article cites **SAF Association reporting (Sept 2026)** for this figure, but:
  - The **2026 PIB (23 April 2026)** on ATF amendments and the **SAF Feasibility Study (3 Sep 2025)** suggest **policy shifts** (e.g., 50% export duty on molasses, UCO collection incentives) may have altered collection rates post-2025.
  - **Recommended check**:
    - **Series**: Ministry of Petroleum and Natural Gas (MoPNG) UCO collection data or **SAF Association’s latest annual report** (likely 2026–27).
    - **Newer period**: 2026–27 fiscal year (if available).
  [confidence: **medium**]

---
**OUTDATED DATA (additional):**
- *"India’s indicative SAF blending targets: 1% (2027), 2% (2028), 5% (2030)"* — While the **Minister of State’s parliamentary statement (cited)** aligns with these targets, the article does **not verify** whether:
  - The **2027 target has been formally notified** (the NBCC decision in Nov 2023 was "indicative").
  - **Domestic-flight SAF mandates** (currently absent) have been introduced post-2025.
  - **Recommended check**:
    - **Series**: Directorate General of Civil Aviation (DGCA) or MoCA’s latest SAF policy updates.
    - **Newer period**: 2026–27 regulatory releases.
  [confidence: **medium**]
