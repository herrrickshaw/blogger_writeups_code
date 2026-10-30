# Fact/interpretation check — maize-is-cheapest-in-different-state

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/maize-is-cheapest-in-different-state.html`

Text-SHA1: `b4ffe6671b1f1157`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Across all 20 state-and-grain pairs analysed, the average result was negative in every one... 0 of 20 State-and-grain pairs where buying and holding for six months made money on average since 2023" — The table and preceding text explicitly detail only 13 state-and-grain pairs (8 maize pairs and 5 rice pairs), making the claim of analyzing 20 pairs inconsistent with the data provided in the article itself. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 1220, Requested 7478. Please try again in 5.234999999s. Need more tokens? Upgrade to Dev Tier today at https:]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Madhya Pradesh accounted for 7.4 million of the 16.1 million tonnes reported to Agmarknet over the past year"* — **Madhya Pradesh’s reported arrivals (1.7M tonnes in Dec 2025) cannot sum to 7.4M tonnes over a full year** (even if scaled to 12 months, this would require ~1.4M tonnes/month, which contradicts the chart’s peak of 1.7M in Dec 2025). The claim conflates state-specific monthly peaks with annual totals. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Neither Uttar Pradesh nor West Bengal recorded a single month since 2020 in which rice fell 15% below its 12-month average"* — **This ignores the 2025-26 glut period**, where Uttar Pradesh’s price dip (May 2026) and West Bengal’s seasonal volatility (e.g., Feb 2026 arrivals spike) suggest temporary deviations. The "no dips" claim overstates stability. [confidence: high]

**OUTDATED DATA:**
- *"The national rice figure also jumped to 24% above its 12-month average in October 2026"* — **FCI’s 2026-27 MSP for rice (Rs 2,390/qtl) was announced in July 2026**; the 24% spike may reflect reporting lags or grade shifts. Re-check: **FCI’s latest MSP order (2026-27) and Agmarknet’s broken rice data (commodity 244) for grade-specific trends**. [confidence: high]

---
*Note: No other distinct factual, interpretive, or outdated data issues stand out.*
