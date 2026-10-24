# Fact/interpretation check — how-to-use-fci-warehouse-mspvsmsv-grain

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-fci-warehouse-mspvsmsv-grain.html`

Text-SHA1: `429d1b8b0ec017e5`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 5111, Requested 3295. Please try again in 3.045s. Need more tokens? Upgrade to Dev Tier today at https://cons]

## Mistral open-mistral-nemo

Here is the structured fact-checking response:

---
**FACTUAL ERRORS:**
- *"16 crops in the mandi-vs-MSP comparison (23 Jul 2026)"* — The table later shows only **14 crops** (wheat, paddy, gram, maize, soybean, moong, tur, bajra, ragi, and 5 others not listed in the snippet). The claim of 16 crops is inconsistent with the provided data. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The holding-economics model produced a clear result: for every commodity tested, estimated storage and financing cost exceeded price appreciation over 12, 24, and 36 months"* — This conclusion conflates **historical CAGR data** (which may not reflect future volatility or policy changes) with **static carry-cost assumptions** (storage tariffs/financing rates). The model does not account for:
  1. Potential MSP revisions or market shocks (e.g., supply disruptions).
  2. Dynamic price trends (e.g., speculative bubbles or policy interventions).
  3. Regional variations in storage costs (the model uses uniform assumptions).
  The "verdict" thus overgeneralizes from stylized unit economics to a broad policy recommendation. [confidence: high]

- *"92% of bajra and 84% of moong market reports below MSP on 23 July 2026"* — While the claim is factually plausible (based on the snapshot), it **misrepresents the broader MSP efficacy debate** by ignoring:
  1. **Temporal variability**: Mandi prices fluctuate daily; a single date (July 2026) cannot definitively prove chronic undershooting.
  2. **Procurement dynamics**: FCI purchases may stabilize prices post-reporting, creating a disconnect between mandi data and realized support.
  3. **Sample size bias**: Ragi (14 reports) and sunflower (2 reports) are excluded from the table but likely have higher below-MSP rates, skewing the narrative. [confidence: medium]

**OUTDATED DATA:**
- *"MSP series, 2010-11 onward"* — The latest **CACP MSP reports** (as of mid-2024) cover **2024-25 and 2025-26**, but the article’s data likely stops at **2025-26** (per the 23 Jul 2026 mandi snapshot). For **2026-27 MSPs** (announced in July 2026), readers should cross-check the **CACP’s latest notification** (e.g., [DOPT.gov.in](https://dopt.gov.in)). [confidence: high]

- *"17,247 mandi records behind that comparison"* — The claim references **Agmarknet’s daily feed (23 Jul 2026)**, but Agmarknet’s **latest bulk dataset** (as of 2024) was for **2023-24**. For **2026-27**, users should verify the **Agmarknet API or FCI’s latest procurement bulletins** for updated mandi volumes. [confidence: high]

---
**Note:** No stylistic or formatting issues were flagged. The article’s caveats (e.g., "unaudited figures," "stylized models") are correctly disclosed, but the **interpretation errors** stem from overstating the models’ policy relevance.
