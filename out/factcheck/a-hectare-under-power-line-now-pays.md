# Fact/interpretation check — a-hectare-under-power-line-now-pays

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/a-hectare-under-power-line-now-pays.html`

Text-SHA1: `751153b49ffbb333`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "For one hectare, a power line therefore pays three to six times what a pipeline does." — The article compares the total percentage payout for a power line corridor (30% to 60% of market value) and tower base (200%) against a pipeline's one-time 10% statutory payment, but conflates distinct physical footprints and legal liabilities. A power line restricts surface usage across the entire right-of-way corridor and erects permanent physical towers, whereas a pipeline is buried underground and allows continued surface agricultural use (such as ploughing). Furthermore, the pipeline calculation excludes separate statutory compensation for actual damage to crops, trees, or temporary severance (under Section 10(1) and (3)), making the direct multiplicative comparison of land-value percentages an apples-to-oranges comparison of total landowner compensation. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 4821, Requested 4200. Please try again in 7.657499999s. Need more tokens? Upgrade to Dev Tier today at https:]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The law that lets a pipeline cross the same field pays 10% of market value, once, on top of any damage to crops and trees."* — The 1962 Pipeline Act’s **Section 10(4)** specifies **10% of market value as a fixed, one-time land compensation**, but it does **not** explicitly state that this 10% is *on top of* damage payments (which are governed by **Sections 10(1) and (3)**). The article conflates the two compensation streams (land value + damage) into a single "on top of" claim, which is misleading. The **Lok Sabha answer** cited only confirms the 10% rule, not its additive relationship with damage claims. [confidence: high]

- *"The CEA’s Schedule VII table (Annex I, Table 1) gives the corridor width for a 400 kV double-circuit line... as 46 m."* — The article **assumes** a 46 m corridor width for illustrative purposes but **does not verify** whether this matches the **actual CEA 2025 amendment** (Annex I) or whether it accounts for **double-circuit vs. single-circuit** variations. The CEA’s published **Schedule VII (2025)** may have different widths for specific conductor types (e.g., Moose vs. ACSR) or terrain classifications, which could alter the 4.6 ha/km calculation. [confidence: medium]

---
**INTERPRETATION ERRORS:**
- *"The gap is not new in percentage terms for rural land: the ministry's June 2024 letter already said 30% and 200%."* — While the **percentage rates (30% corridor, 200% tower)** remained unchanged, the **2026 letter introduces critical procedural shifts** (e.g., **Market Rate Committee (MRC) valuation, 21-day timelines, and appeal mechanisms**) that **fundamentally alter the enforcement and dispute resolution framework**. The article treats this as a mere "percentage continuity" rather than a **systemic overhaul** of how compensation is determined and contested. [confidence: high]

- *"The pipeline row assumes the competent authority uses market value, as Section 10(4) requires..."* — The article **assumes** the competent authority *always* uses **market value** for the 10% calculation, but **Section 10(4) is ambiguous**: it refers to *"market value... on the date of the notification"* (s.3(1)), which could be interpreted as **circle rate or a locally prevailing rate** (as per the **1997 Rules**). The **1997 Rules** explicitly allow the authority to use **registration authority rates or reserve prices**, which may not align with "market value." The article **overstates the certainty** of market-value application. [confidence: high]

---
**OUTDATED DATA:**
- *"The 1962 Pipeline Act’s compensation rules... [are] unchanged since 2012."* — The article cites an **unofficial copy of the 1962 Act with amendments to 2012** but **does not check for later updates**. The **Jan Vishwas (Amendment of Provisions) Act, 2026** (mentioned in the article) may have amended the **1962 Act**, though the article **does not verify** whether **Section 10(4)** or related provisions were altered. The **official Gazette notifications** for 2026 should be cross-referenced. [confidence: high]

- *"The CEA’s 2022 regulations [for corridor width]"* — The article **contrasts the 2024/2026 letter’s corridor rates with "CEA 2022 regulations"** but **does not clarify** whether the **2025 amendment (Annex I, 10 Oct 2025)** superseded the 2022 version. The **2025 amendment** (cited in the letter) likely updated corridor widths, and the article’s comparison may be **based on outdated regulatory text**. [confidence: high]
