# Fact/interpretation check — fuel-pricing-to-crude-cost

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fuel-pricing-to-crude-cost.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99874, Requested 5150. Please try again in 1h12m20.736s. Need more tokens? Upgrade to Dev Tier today at ht]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "5 August 2026" (article dateline) — The article references data and sources dated up to 5 August 2026 (e.g., Rigzone/OilPriceAPI queries at 02:3x UTC), but the PPAC Ready Reckoner edition cited is "FY2025-26 H1 edition," which would logically cover data up to September 2025. The dateline date appears to be a future projection, not a real publication date, as no data from August 2026 is available in the cited sources. [confidence: high]

- "₹71.16/litre" (ethanol cost in Section 5) — The article states this is the "OMCs' ESY2025-26 weighted-average delivered procurement cost (ex-mill average ₹66.61/l plus GST and transport)." However, ₹66.61/l is not a plausible ex-mill ethanol price in India (typical ex-mill prices are closer to ₹45–55/l in recent years). The addition of GST (18%) and transport would not push it to ₹71.16/l. This suggests a miscalculation or misattribution of the ethanol cost figure. [confidence: high]

---

INTERPRETATION ERRORS:
- "a 67% swing in crude (past-year low to high) would, on a naive full pass-through, move Delhi petrol by ≈43% (₹87.65 to ₹125.71)" — The article correctly notes that the flat excise duty and commission layers do not move with crude, but it then implies that the remaining layers (dealer price and VAT) scale proportionally with crude. However, VAT is a percentage of the total price (including excise and commission), so it compounds non-linearly. The 43% swing is an overestimate because it treats VAT as a simple linear addition rather than a compounding tax. The actual pass-through would be smaller due to this compounding effect. [confidence: high]

- "Because ethanol's cost is fixed annually by government notification rather than tracking crude, a higher blend share structurally dampens how much a crude spike passes through to the pump" — The article correctly notes that ethanol blending reduces the taxable base (since ethanol is excise-exempt), but it does not account for the fact that the ethanol cost itself is not fixed in absolute terms relative to crude. Ethanol prices are influenced by feedstock costs (e.g., maize, sugarcane), which are indirectly linked to crude via energy inputs and agricultural commodity markets. Thus, the claim that ethanol blending "structurally dampens" crude pass-through ignores potential indirect correlations between ethanol costs and crude prices. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
