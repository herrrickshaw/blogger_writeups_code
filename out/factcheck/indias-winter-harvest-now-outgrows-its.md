# Fact/interpretation check — indias-winter-harvest-now-outgrows-its

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-winter-harvest-now-outgrows-its.html`

Text-SHA1: `242e66d776240a8e`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Arrivals as share of production, 2024 ... Maize: 22% ... Wheat: 23% ... Soybean: 43%" — Comparing calendar-year mandi arrivals (e.g., total arrivals in 2024) directly against crop-year production figures (e.g., production of the 2024-25 crop year) creates an apples-to-oranges comparison. Crop production harvested in spring or autumn of 2024 enters mandis across different calendar months and overlapping agricultural years, making a simple calendar-year to crop-year percentage distortionary. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 2213, Requested 6188. Please try again in 3.0075s. Need more tokens? Upgrade to Dev Tier today at https://con]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"In 2002-03, rabi first produced more foodgrain than kharif"* — **2002-03 was not a drought year for kharif** (confidence: **high**)
  *(Kharif droughts in India are typically linked to monsoon failures, e.g., 2009-10, 2014-15, or 2002 was a near-normal monsoon year with only mild deficits in some regions. The claim conflates drought years with the first rabi-kharif output crossover.)*

- *"Summer foodgrain area rose from 62.0 lakh hectares in 2022-23 to 76.6 in 2025-26 (+24%)"* — **The 2025-26 figure is a third advance estimate**, which historically has a higher margin of error and may not reflect final data (confidence: **medium**)
  *(Advance estimates often revise downward; the +24% growth could shrink post-finalization. The article notes this but does not flag it as a potential overstatement.)*

---
**INTERPRETATION ERRORS:**
- *"Kharif has not grown in land [since 2003-06], while rabi and summer foodgrain area grew +32%"* — **This ignores that kharif *foodgrain* area was flat, but kharif *total* cropped area (including non-foodgrains like cotton, soybean, and oilseeds) expanded** (confidence: **high**)
  *(The claim misleads by focusing only on foodgrains, while kharif’s non-foodgrain crops (e.g., soybean +77%) drove total cropped area growth. The article later corrects this but the initial framing is misleading.)*

- *"The yield gap between seasons reflects irrigation and crop mix as much as season"* — **This is true, but the article then uses it to claim "rabi matters more" without addressing that kharif’s *monoculture vulnerability* (e.g., rice/maize dominance) still makes it the riskier season for food security** (confidence: **medium**)
  *(The "what doesn’t follow" section acknowledges kharif’s importance, but the earlier causal framing ("rabi’s growth ≠ kharif’s decline") downplays kharif’s systemic role in food security.)*

---
**OUTDATED DATA:**
- *"Mandi arrivals: Agmarknet, all states, 2019–2024 average"* — **Agmarknet’s coverage expanded in November 2025**, invalidating the 2019–2024 baseline for post-2025 comparisons (confidence: **high**)
  *(The article notes this in a caveat but uses the 2019–2024 average to analyze *current* (2025-26) trends, which may overstate mandi penetration due to the coverage gap.)*

- *"Summer (zaid) area, lakh hectares: 2022-23 vs 2025-26"* — **Only four years of separate summer data exist (2022-23 to 2025-26)**, making trends statistically unreliable (confidence: **high**)
  *(The article acknowledges this but extrapolates "fastest-growing season" claims without addressing the short timeframe or advance-estimate risks.)*
