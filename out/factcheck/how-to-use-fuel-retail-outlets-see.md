# Fact/interpretation check — how-to-use-fuel-retail-outlets-see

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-fuel-retail-outlets-see.html`

Text-SHA1: `6a717d46ca7a1589`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Uttar Pradesh 8,915 4.5 37.0" — The table lists Uttar Pradesh's total pump count as 8,915, but immediately preceding and following sections state the total deduplicated national outlet count is 82,602 (and 9,007 Nayara outlets are unmapped due to an 'unknown' state), making a single state having nearly 9,000 outlets while others like Maharashtra have 7,317 mathematically inconsistent with the total and the text's own per-capita/per-area calculations (4.5 per 100k people on UP's massive population implies a much higher absolute number or a math error). [confidence: medium]

INTERPRETATION ERRORS:
- "after dedup (name+address+company+lat+lon): 419 ... Delhi's low per-capita number reflects a dense city counted against its whole population and is not a real gap" — The author attributes Delhi's low per-capita ranking (2.5 pumps per 100,000 people) to it being a dense city spread across its whole population, but a low *per-capita* ratio in a densely populated urban area actually signifies a high concentration of people relative to outlets (or in Delhi's case, extreme under-counting due to unmapped/unmatched spelling variants or missing company entries), whereas density typically inflates per-area metrics (which the table correctly shows as high at 282.5 per 1000 km2). [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
none found  

**INTERPRETATION ERRORS:**  
- “Even after cleaning, 82,602 outlets compares with a PPAC official baseline described in PPAC_RETAIL_OUTLETS_MAY2026.md, so coverage is roughly 80 %.” — The article treats the 82,602 deduplicated outlets as a direct subset of the PPAC baseline and therefore infers an 80 % coverage rate. However, the dataset explicitly omits 9,007 Nayara outlets (state ‘unknown’) and many others that are lost due to spelling‑variant state names. Consequently, the 80 % figure understates the true coverage and misleads readers into believing the dataset captures the majority of retail outlets. [confidence: high]  

**OUTDATED DATA:**  
- “Pumps per 100 000 people by state (cleaned; **state populations from the repo's gap‑analysis data.js**).” — The population figures used in `data.js` are based on older census‑derived numbers (likely the 2011 Census). More recent official estimates (e.g., the 2023/2024 population projections released by the Ministry of Statistics and Programme Implementation) would change the per‑capita pump calculations. The series to re‑check is the state‑wise population data in `fuel‑station‑gap‑analysis/data.js`; update it with the latest mid‑year population estimates. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"PPAC official baseline of 103,450 (May 2026)"* — The article cites a PPAC (Petroleum Planning and Analysis Cell) baseline of **103,450 outlets in May 2026**, but this figure is **not verifiable as official** without cross-checking the latest PPAC data (e.g., the [PPAC’s latest retail outlets report](https://ppac.gov.in/) or the Ministry of Petroleum & Natural Gas’s annual statistics). The article does not provide a direct link to the PPAC source file (e.g., *PPAC_RETAIL_OUTLETS_MAY2026.md* referenced in the repo) for validation, and the gap between 82,602 (cleaned) and 103,450 could stem from methodological differences (e.g., inclusion of CNG/diesel outlets, regional variations, or timing of the crawl). [confidence: **medium**]

---

**INTERPRETATION ERRORS:**
- *"Delhi’s low per-capita number reflects a dense city counted against its whole population and is not a real gap"* — While Delhi’s **2.5 pumps per 100,000 people** (cleaned) is artificially low due to aggregating the entire state population (including rural areas outside the National Capital Region), this **does not invalidate the per-capita metric for other states**. The claim implies Delhi’s number is an "artefact" without acknowledging that **per-capita ratios are inherently comparative**—they highlight relative undersupply *within the state’s own population*, not just urban vs. rural. For example, Bihar’s 2.7 pumps/100k is similarly a state-level average, not a "gap" per se. The distinction between "real gaps" and "artefacts" is **context-dependent** and not universally applicable. [confidence: **high**]

- *"The table understates states with spelling variants (I mapped Jharkand, Uttrakhand and Jammu variants) and cannot place Nayara’s 9,007 outlets by state at all"* — The article **correctly identifies the issue** with unmatched outlets (e.g., Nayara’s 9,007 "unknown" entries), but the **extrapolation to "understated" state counts is misleading**. The table’s **82,602 outlets** already reflect the **deduplicated and state-matched subset (72,070)**, which excludes only:
  1. **Nayara’s 9,007** (due to "unknown" state labels),
  2. **10,532 with unmatched state spellings** (e.g., "Jharkand").
  The **total missing from the table is 19,539 outlets (23.6% of cleaned data)**, not just "understated" counts—it’s a **complete exclusion** of those records. The claim conflates **data gaps** with **statistical bias**. [confidence: **high**]

---
**OUTDATED DATA:**
- *"state populations from the repo’s gap-analysis data.js"* — The article uses **census-based population figures** (implied by the caveat about "older census numbers") without specifying the source or year. For **2026 data**, the latest official population estimates should come from:
  - **Registrar General of India (RGI) – Provisional Population Totals (2021 Census)** (latest available as of 2023, with projections for 2026 via [RGI’s website](https://censusindia.gov.in/)).
  - **National Statistical Office (NSO) – Annual Estimates** (e.g., [2023–24 estimates](https://www.mospi.gov.in/)).
  The **2021 Census data** (latest full census) is now **5+ years old**, and even provisional estimates may lag. Re-checking NSO’s **2024–25 or 2025–26 estimates** would be critical for accurate per-capita calculations. [confidence: **high**]

---
**none found** (for other categories).
