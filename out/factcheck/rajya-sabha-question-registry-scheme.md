# Fact/interpretation check — rajya-sabha-question-registry-scheme

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/rajya-sabha-question-registry-scheme.html`

Text-SHA1: `d6be51dec376682c`

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
- *"Of the 1,883 Rajya Sabha questions on scheme/incentive policy captured since 2019, only 141 were starred (answered orally) — the rest, 1,742, were unstarred written answers."*
  — The claim that **1,883 questions** were captured since **2019-01-02** is **plausible but unverifiable** without cross-checking the raw `rsdoc.nic.in` index (which is the source). However, the **date range (2019–2026-08-13)** includes **8 years of parliamentary sessions**, and **1,883 questions** is a **low count** for a Rajya Sabha registry covering schemes/incentives (comparable Lok Sabha registries often exceed 5,000+ for similar periods). The **141 starred vs. 1,742 unstarred split** is **mathematically correct** (141 + 1,742 = 1,883), but the **total count itself may be underreported** due to:
    - **Keyword-matching limitations** (e.g., excluding questions where schemes are mentioned in the body but not the subject line).
    - **Potential exclusion of older questions** (e.g., pre-2019 keyword lists may not align with 2019+ data).
  **[Confidence: medium]** *(Low confidence in the total count; high confidence in the starred/unstarred arithmetic.)*

---
**INTERPRETATION ERRORS:**
- *"A scheme that draws mostly written questions is being tracked quietly, ministry-to-member, while a scheme drawing a disproportionate share of the 141 starred slots is one members consider worth a public floor exchange — oral answers are a scarcer, contested slot in the House's own calendar, so a scheme that keeps attracting them is, by revealed preference, a live political concern rather than a routine ask."*
  — The **causal leap from "starred questions" to "live political concern"** is **overstated**. While starred questions **do** indicate higher parliamentary interest (due to oral debate opportunities), they are also influenced by:
    1. **Procedural biases**: Some members **prefer written answers** for complex technical schemes (e.g., semiconductor missions) to avoid time-consuming floor debates.
    2. **Ministry pushback**: Schemes with **high political sensitivity** (e.g., land acquisition, subsidies) may be **avoided as starred questions** to prevent embarrassing oral exchanges.
    3. **Calendar constraints**: The Rajya Sabha’s **limited floor time** means even politically salient schemes may not always get starred due to **prioritization by party whips**.
  The article **treats the starred/unstarred ratio as a pure "revealed preference"** but ignores these **alternative explanations**. A stronger claim would require **comparing starred rates across schemes with other proxies of political salience** (e.g., media coverage, opposition party focus).
  **[Confidence: high]**

---
**OUTDATED DATA:**
- *"Harvested from the rsdoc.nic.in per-question index by subject keyword (same keyword lists as the Lok Sabha registry, from 2019)"*
  — The **keyword lists used for classification** (e.g., for schemes like **PM MITRA, Semiconductor Mission**) may be **outdated**. The **Rajya Sabha’s question index (rsdoc.nic.in)** is updated **daily**, but the **article’s registry was generated on 2026-08-19** using a **static keyword map from 2019**. Newer schemes (e.g., **PLI 2.0 extensions, new PSUs**) or **renamed programs** (e.g., **PM-Kisan → PM-Kisan Samman Nidhi**) would not be captured unless the keyword list was updated. The **source series to re-check** is:
    - **rsdoc.nic.in** (Rajya Sabha Q&A index) → **Latest keyword lists** (should align with **2024–2026 scheme names**).
    - **Lok Sabha registry keyword lists** (if reused) → **Verify if updated post-2019**.
  **[Confidence: high]** *(The 2019 keyword cutoff likely misses recent schemes.)*
