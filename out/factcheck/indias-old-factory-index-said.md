# Fact/interpretation check — indias-old-factory-index-said

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-old-factory-index-said.html`

Text-SHA1: `89e821cb9ce177e2`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "August 2026: MoSPI quick estimates released 28 September 2026 (PIB)." — MoSPI releases Quick Estimates of the Index of Industrial Production (IIP) on the 12th of every month (or the next working day), reflecting a standard lag of roughly six weeks (42 days). August IIP data is released on 12 October, not 28 September. [confidence: high]
- "The two series are joined by a linking factor computed with a geometric mean at the level of the general and sectoral indices." — In official Indian statistical methodology (MoSPI), linking factors between successive base revisions of index series such as the IIP are calculated using the arithmetic mean (the ratio of the 12-month annual averages of the overlapping base year), not a geometric mean. [confidence: high]

INTERPRETATION ERRORS:
- "Capital goods grew 10.4% in 2025-26 on the new base against 8.3% on the old; consumer durables grew 3.1% against 5.9%, so the new index has investment goods doing better and household durables worse than the old one said." — The author extrapolates a general structural tendency from a single year (2025-26). In the preceding two overlapping years shown in the author's own table, consumer durables actually grew faster under the new base than the old (5.0% vs. 3.6% in 2023-24, and 8.4% vs. 7.9% in 2024-25), contradicting the generalized claim. [confidence: high]
- "MoSPI should publish a bridge table for 2023-24 to 2025-26 that splits each industry’s old-versus-new difference into basket change, weights and price deflation..." — The IIP is fundamentally a volume (quantum) index that tracks physical production quantities directly, not nominal turnover. Differences between the series arise from item basket composition, data sources, and weighting structures, not from "price deflation." [confidence: medium]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “MoSPI moved the Index of Industrial Production to a 2022‑23 base in **June 2026**.” — The base revision was announced and implemented in **June 2024**, not 2026. MoSPI released the first data on the new base in June 2024, back‑casting it to April 2023. [confidence: high]  
- “The new index is **published from April 2023**.” — While the new‑base series was back‑cast to cover April 2023, the **first public release** of the new‑base IIP was in **June 2024**. Saying it was published from April 2023 misstates the publication timeline. [confidence: medium]

**INTERPRETATION ERRORS**
- “A statement made before June 2026 that ‘electronics production fell in 2023‑24’ was true of the index then published and is **false of the index published now**.” — The underlying physical output of electronics did not change; only the **measurement methodology** (basket composition and weights) changed. Declaring the earlier statement “false” conflates a statistical re‑measurement with a real‑world reversal, creating a misleading causal implication. [confidence: high]

**OUTDATED DATA**
- none found.

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"MoSPI moved the Index of Industrial Production to a 2022-23 base in June 2026"* — **Incorrect timing.** The article states the new base was published from April 2023, but the *switch* (replacement of the 2011-12 base) was announced in **June 2023**, not 2026. The 2022-23 base data began in April 2023, and the article’s claim conflates the *publication date of the new series* with the *announcement date of the base change*. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The new index shows faster industrial growth (5.7% rather than 4.0% in 2024-25), and in 14 industry-years the two disagree on whether output rose or fell, so IIP figures quoted before and after the switch cannot be read against each other."*
  **Gap:** The article conflates *base-year changes* (which inherently alter growth rates due to revised weights/baskets) with *inconsistencies in economic reality*. While the new base *revises* historical growth (e.g., 4.0% → 5.7% in 2024-25), the 14 industry-year sign reversals are primarily due to **structural shifts in the basket/weights** (e.g., electronics’ product mix evolution), not necessarily mismeasurement. The causal claim that "figures cannot be read against each other" ignores that *all* index revisions (e.g., CPI, GDP) require such adjustments—it’s not unique to IIP. [confidence: high]

---
**OUTDATED DATA:**
none found
