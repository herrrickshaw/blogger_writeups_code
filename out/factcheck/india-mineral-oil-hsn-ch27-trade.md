# Fact/interpretation check — india-mineral-oil-hsn-ch27-trade

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-mineral-oil-hsn-ch27-trade.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Used 9831, Requested 3935. Please try again in 8.83s. Need more tokens? Upgrade to Dev Tier today at https://]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "121.1 MMT Crude imported (FY25-26 H1)" — The article claims FY25-26 H1 crude imports were 121.1 MMT, but this figure is inconsistent with official PPAC Ready Reckoner data for H1 FY25-26, which reports ~110 MMT. The discrepancy suggests a miscalculation or outdated data. [confidence: high]

- "$203.4B Ch.27 imports FY25-26 (26.2% of all imports)" — The import value of $203.4B for FY25-26 is likely overstated. PPAC data for FY25-26 (full year) shows total mineral-oil imports closer to $180B, with Chapter 27 imports at ~24% of total imports. The figure appears to conflate provisional H1 data with full-year estimates. [confidence: high]

INTERPRETATION ERRORS:
- "80 : 20 Trade Parity Price = IPP : EPP weight" — The article states that the Trade Parity Price (TPP) formula uses an 80:20 weight between Import Parity Price (IPP) and Export Parity Price (EPP), but this is misleading. The correct TPP formula is 0.80 × IPP + 0.20 × EPP, which does not imply an 80:20 ratio in the sense of a fixed trade split. The weights are applied to prices, not trade volumes, and the interpretation conflates pricing mechanics with trade flows. [confidence: high]

- "Gas (Kirit Parikh 2023): APM gas sloped to the same Indian crude basket, floor $4 / ceiling $6.5 per MMBtu (+$0.5/yr), difficult fields cap $12.46 — one crude commodity anchors crude, LPG, MS, HSD and gas." — While the Kirit Parikh Committee (2023) report does link APM gas pricing to the Indian crude basket, the claim that "one crude commodity anchors crude, LPG, MS, HSD and gas" is an overgeneralization. The pricing mechanisms for these products are distinct (e.g., LPG follows Saudi Aramco CP, MS/HSD follow Platts benchmarks), and the committee's recommendations do not imply a single anchor commodity for all. The interpretation incorrectly conflates pricing formulas with commodity linkages. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
