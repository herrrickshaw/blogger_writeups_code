# Fact/interpretation check — indias-cheapest-lng-capacity-is-extra

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-cheapest-lng-capacity-is-extra.html`

Text-SHA1: `b277feba1ad06ad0`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "QatarEnergy declared force majeure after the March 2026 attack on Ras Laffan" — Ras Laffan is a major industrial city and port in Qatar, and while geopolitical tensions or strikes affecting Persian Gulf energy infrastructure are plausible hypothetical scenarios, there was no factual March 2026 military attack on Ras Laffan. [confidence: high]

INTERPRETATION ERRORS:
- "At PNGRB’s own conversion (190 MMSCMD = 52.7 MMTPA) that is about 55.5 MMTPA of LNG, which at an 85% utilisation ceiling needs about 65 MMTPA of regas capacity." — The reasoning contains a logical gap in applying a utilization ceiling: dividing required throughput (55.5 MMTPA) by an 85% utilization cap results in a required capacity of roughly 65.3 MMTPA, but treating this as a strict requirement assumes that terminals must never operate above 85% or that aggregate nameplate capacity must match peak rather than seasonal/average throughput plus redundancy. Furthermore, the article's own data shows Dahej routinely operating above 90–100%, demonstrating that terminals can exceed an 85% ceiling. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 9726, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"Dahej ran at 92% of capacity while PNGRB’s own data point to the pipeline out, not the tank, as the constraint"** — The claim conflates Dahej’s utilisation (91.9% in April–May 2026 on its *old* 17.5 MMTPA base) with the broader pipeline constraint argument. While Dahej’s expansion (22.5 MMTPA) was only 65.6% utilised in April–June 2026 due to QatarEnergy’s force majeure, the article later clarifies that **Dahej’s *old* 17.5 MMTPA capacity was already at 91.9%**, not 92%. The 92% figure is likely a misstatement or rounding error (91.9% is cited elsewhere). [confidence: high]

- **"PNGRB’s April 2025 demand paper prints PPAC’s terminal utilisation for 2023-24 and the eight-year average from 2015-16 to 2022-3"** — The article states this as fact, but **PPAC’s May 2026 Ready Reckoner (published June 2026) is the latest official source**, and it does not explicitly confirm the 2023-24 or 2015-22 averages in the April 2025 PNGRB paper. The article’s reliance on this unchecked claim risks misattribution. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- **"Expanding Dahej cost about ₹370 crore per million tonnes a year of capacity; India’s new onshore terminals cost ₹950–1,290 crore, ran 22–35 months late, and worked at 24–37% capacity while Dahej ran at 92%"** — The cost comparison is **apples-to-oranges** because:
  1. The ₹370 crore/MMT figure for Dahej’s expansion (2021–26) includes **reused infrastructure** (jetties, land, pipelines), while new terminals require **new marine works, breakwaters, and grid connections**, inflating costs.
  2. The 92% utilisation claim is **misleadingly aggregated**: Dahej’s *old* 17.5 MMTPA was at 91.9%, but its *new* 22.5 MMTPA expansion was only 65.6% utilised in April–June 2026 due to external shocks (Qatar force majeure). The 24–37% figure for new terminals is **correct**, but the contrast ignores that Dahej’s high utilisation predates the expansion and relies on **existing pipeline capacity** (GSPL’s 40 MMSCMD vs. 95–100 MMSCMD regas demand).
  **Gap**: The article treats cost and utilisation as **directly comparable** without accounting for infrastructure reuse or supply-side constraints. [confidence: high]

- **"The other seven [terminals] have mostly run at a fifth to a half of theirs [Dahej’s utilisation]"** — This **double-counts** the comparison:
  - Dahej’s *old* 17.5 MMTPA averaged **98.2%** (2015–22), while new terminals averaged **10.5–40.1%** in April–May 2026.
  - The article later notes that **Dahej’s *new* 22.5 MMTPA expansion was only 65.6% utilised** in April–June 2026, yet still frames the contrast as "Dahej at 92% vs. others at 24–37%." This **cherry-picks** the highest historical utilisation (pre-expansion) while ignoring the **current underperformance of Dahej’s expansion** and the **systemic pipeline constraints** affecting all terminals. [confidence: high]

---

**OUTDATED DATA:**
- **"PPAC’s latest Ready Reckoner lists 53.5 million tonnes a year (MMTPA) of regasification capacity"** — As of **June 2026**, PPAC’s *May 2026 Ready Reckoner* (published June 2026) **still lists Dahej at 17.5 MMTPA**, despite its **22.5 MMTPA expansion being commissioned on 31 March 2026**. The article acknowledges this discrepancy but does not flag it as a **data lag**:
  - **Series to re-check**: PPAC *Monthly Ready Reckoner* (Table 21, capacity as of 1 June 2026).
  - **Newer period**: The expansion should reflect in **June 2026+ editions** (e.g., July 2026 Ready Reckoner). [confidence: high]

- **"LNG imports for 2025-26 and for June, August and September 2026"** — The article cites **PPAC’s provisional data** for these months but does not note that:
  - **PPAC’s May 2026 Ready Reckoner (published June 2026) is the latest official release** for 2025-26 imports.
  - The **June, August, and September 2026 figures** are **press reports of PPAC’s preliminary data**, not yet confirmed in a formal PPAC publication. The article treats them as verified when they may be **interim estimates**.
  - **Series to re-check**: PPAC *Monthly Ready Reckoner* (Tables 18/27 for LNG imports).
  - **Newer period**: Finalised data will appear in the **July 2026 Ready Reckoner**. [confidence: high]
