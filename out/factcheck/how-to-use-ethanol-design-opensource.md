# Fact/interpretation check — how-to-use-ethanol-design-opensource

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-ethanol-design-opensource.html`

Text-SHA1: `9fa35e8538fafe51`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUALERRORS:
- none found

INTERPRETATIONERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “21.75 L per tonne of cane” — Typical industrial ethanol yields from sugarcane (including juice and bagasse) are in the range of 70–80 L / t cane (wet basis). A figure of 21.75 L / t is an order‑of‑magnitude low and does not match published Indian or global industry data. [confidence: high]  
- “Model yields of 506.7 L/t (milled and broken rice) and 459.2 L/t (maize)” — Reported ethanol yields from rice or maize are usually 300–380 L / t (maize) and 300–350 L / t (rice). Values above 450 L / t are not supported by any known Indian or international feedstock‑to‑ethanol conversion data. [confidence: high]

**INTERPRETATION ERRORS**
- “The model consistently overshoots published grain yields by 13 to 21 percent (ratios 1.126, 1.152, 1.208). Cause: a lab‑optimised 95 % hydrolysis efficiency combined with a molasses‑calibrated fermentation efficiency.” – The statement attributes the systematic overshoot to a specific combination of hydrolysis and fermentation efficiencies, but no quantitative analysis is provided to link those efficiencies to the exact 13‑21 % bias. The overshoot could also stem from other modelling assumptions (e.g., mass‑balance rounding, ideal‑stage assumptions, or feedstock composition). Thus the causal claim is not substantiated by the evidence presented. [confidence: medium]  

**OUTDATED DATA**
- “BIS IS 15464” – The article says the sieve‑bed dehydration meets the “BIS IS 15464” specification for anhydrous ethanol. The Bureau of Indian Standards revised the ethanol purity and water‑content limits in the 2025 amendment (IS 15464:2025). The article does not reference this newer version, so the compliance claim may be based on the pre‑2025 standard. [confidence: medium]  

*No other categories contain identifiable problems.*

## Mistral open-mistral-nemo

Here’s the structured review of the article:

---
**FACTUAL ERRORS:**
- *"21.75 L/t ethanol per tonne of cane, matching the published figure"* — The claim that the model’s **21.75 L/t** yield "matches the published figure" is misleading because the article later admits the **molasses route was calibrated on its own published data**, making the match circular and not an independent validation. The cited "published figure" (1.13–1.21× grain yield) is also inconsistent with the grain route’s overshoot (13–21% higher than published yields). [confidence: high]

**INTERPRETATION ERRORS:**
- *"The model consistently overshoots published grain yields by 13 to 21 percent (ratios 1.126, 1.152, 1.208). Cause: a lab-optimised 95% hydrolysis efficiency combined with a molasses-calibrated fermentation efficiency."*
  The reasoning conflates **two distinct calibration biases**:
  1) The molasses route’s calibration (which matches its own data) is unrelated to grain yield accuracy.
  2) The grain overshoot is attributed to *both* hydrolysis *and* fermentation efficiencies, but the article doesn’t prove fermentation efficiency is the sole driver—it could also stem from unaccounted grain-specific losses (e.g., starch recovery, distillery efficiency). The causal link is speculative. [confidence: high]

- *"One sieve-bed result came out with a height-to-diameter ratio of 35.9. The tool itself advises splitting it across parallel vessels."*
  The advice to split the sieve bed is technically sound (industrial practice avoids H/D > 30–35 for sieve trays), but the article **doesn’t explain why the model’s default design violates this rule** (e.g., is it due to feedstock properties, column constraints, or a software limitation?). The claim lacks context for the reader to evaluate the necessity of splitting. [confidence: medium]

**OUTDATED DATA:**
- *"21.75 L/day ethanol, 21.75 L per tonne of cane, matching the published 21.75"* — The **date stamp (18 October 2026)** suggests this is a future-dated claim. For an India-focused blog, verify if:
  - The **latest BIS IS 15464 (2023) specification** for anhydrous ethanol has changed (e.g., purity tolerances, impurities).
  - **CPCB spent wash cap updates** (2024–2026) affect the 261 m³/day claim.
  - **Recent cane yield data** (e.g., 2025–26 crop) from the **Directorate of Sugar Economics and Statistics (DSES)** or **FAO** contradicts the 2026-calibrated figure.
  [confidence: high]

---
**Note:** The article’s technical content (e.g., Fenske-Underwood-Gilliland correlations) is beyond the scope of these categories. No other errors were identified.
