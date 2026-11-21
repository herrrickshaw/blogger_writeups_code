# Fact/interpretation check — indias-spare-crop-residue-could-make-57_0594387739

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-spare-crop-residue-could-make-57_0594387739.html`

Text-SHA1: `4a28044c4b6b6822`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "In the 2025 season Madhya Pradesh, not Punjab, had the most farm fires of the six states ICAR tracks: 17,067 of 33,028, more than half." — The article contrasts Madhya Pradesh's 17,067 farm fires with Punjab's 5,114 (shown in the subsequent table) to claim MP had the most fires of the tracked states. However, this is an apples-to-oranges comparison of absolute counts without adjusting for total cropped area, agricultural output, or farm size, creating a misleading conclusion about stubble-burning intensity relative to Punjab, which is geographically much smaller and more intensively farmed for paddy/wheat. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 10080, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Punjab’s rice straw is the biggest single feedstock by a wide margin: about **72 lakh tonnes of char a year** if all of its spare straw were charred."* — The claim conflates **surplus straw (50 Mt total for rice, with Punjab’s share at ~21 Mt)** with **char yield (35% of dry weight, so ~7.4 Mt char max for Punjab’s surplus)**. The 72 lakh tonnes figure appears to misrepresent either the **surplus itself (50 Mt total rice straw surplus, not 72 Mt)** or the **char yield (35% of 21 Mt = ~7.4 Mt, not 72 Mt)**. The table later confirms Punjab’s rice-straw char at **72.3 lakh tonnes (7.23 Mt)**, which aligns with 35% yield on ~21 Mt surplus. The error lies in the **preceding sentence’s phrasing**, which suggests 72 lakh tonnes is the surplus (it’s not) or the char (it’s not). [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The link between harvest growth and low soil carbon is weaker than the story suggests. Across the eighteen states, the rank correlation between **fertiliser use per hectare and the organic-carbon index is only -0.24**."* — While the correlation is weak, the claim **misrepresents causality**. The article later notes that **soil carbon reflects decades of climate and practice**, not just recent fertiliser use. The -0.24 correlation suggests **no strong recent relationship**, but the story’s framing implies fertiliser use *directly* drives soil carbon depletion—a **false causal link**. The data only show **association**, not mechanism. [confidence: high]

- *"Only rice straw in **Odisha** and cotton stalk in **Maharashtra** stay in the top ten under every set of weights tried."* — This is **technically correct but misleadingly framed**. The sensitivity analysis shows that **Odisha’s rice straw and Maharashtra’s cotton stalk are the only pairs that remain in the top ten across *all six weightings***, but the article’s **earlier claim** (*"only two pairings stay in the top ten under all six weightings"*) is **redundant** because the table already lists 119 pairs. The **real gap** is that the article **does not clarify why these two pairs are uniquely robust**—e.g., whether it’s due to **soil need (Odisha’s acid soils) + openness (Maharashtra’s ICAR projects)** or just **data artifacts**. The reasoning could be strengthened by **explicitly linking the weights to these states’ unique attributes**. [confidence: medium]

---
**OUTDATED DATA:**
- *"47.7% Soil Health Card samples in **2024-25** with organic carbon below 0.5%"* — The **2024-25 Soil Health Card data** is cited from **MoSPI’s EnviStats 2024**, but the **latest official release (as of Nov 2026)** may include **2025-26 updates** (e.g., Rajya Sabha USQ 2258, Aug 2025, covers 2024-25 but could be superseded by newer state-level reports). The article’s **source (EnviStats 2024)** is correct for the period named, but readers should verify if **MoSPI or state agriculture departments** have released **2025-26 SHC data** (e.g., via **MoA&FW or state agricultural universities**). [confidence: medium]

- *"The **2025 season** Madhya Pradesh had the most farm fires of the six states ICAR tracks: 17,067 of 33,028"* — The **ICAR CREAMS fire counts** are sourced to the **New Indian Express (4 Dec 2025)**, but **2025-26 data** (e.g., **2026 season fires**) may now be available from **ICAR’s latest CREAMS dashboard** or **state pollution control boards**. The claim is not outdated in its period (2025), but **newer seasonal data** could alter the narrative (e.g., if 2026 fires spiked elsewhere). [confidence: low]
