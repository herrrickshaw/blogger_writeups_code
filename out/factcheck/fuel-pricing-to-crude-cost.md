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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Used 8874, Requested 5317. Please try again in 10.954999999s. Need more tokens? Upgrade to Dev Tier today at ]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹100.35/l PPAC published: ₹94.77/l" — The article incorrectly states that the PPAC published petrol RSP in Delhi is ₹100.35/l when it is actually ₹94.77/l (as shown in the table under "Past-year low" and "PPAC Jul–Sep 2025 baseline"). This appears to be a typographical error in the text, not the table itself. [confidence: high]

- "$78.87/bbl Brent Crude, live (OilPriceAPI & Rigzone agree to 2¢)" — While the article acknowledges a data-quality note about conflicting fields in OilPriceAPI's response, it does not correct the claim that Brent Crude is $78.87/bbl. However, the note reveals that OilPriceAPI's "BRENT_SPOT_USD" field shows $91.82, which is significantly different. The article uses $78.87, but the discrepancy suggests potential unreliability in the source. [confidence: medium]

INTERPRETATION ERRORS:
- "Because none of these four components move with crude, they are the lever government has historically pulled to cushion pump prices when crude spikes, and the reason the 'full pass-through' scenarios below likely overstate how much of a crude rally would actually reach the pump." — The article correctly notes that excise duties are fixed and do not move with crude prices, implying they act as a cushion. However, it does not provide evidence that the government has *historically* adjusted these duties in response to crude spikes to cushion pump prices. The claim assumes a causal relationship without citing historical policy actions or data. [confidence: medium]

- "a 97% swing in crude (past-year low to high) would, on a naive full pass-through, move Delhi petrol by ≈43% (₹87.65 to ₹125.71) — a smaller swing than crude's own, because the flat-rate excise and commission layers don't move at all, and only the dealer-price and VAT layers scale." — The article correctly calculates the percentage change in petrol prices based on crude swings, but it does not account for the fact that VAT is a percentage of the total price (including excise and commission), which means VAT itself would scale non-linearly with the dealer price. This could lead to an overestimation of the pass-through effect, as VAT is not purely linear with crude price changes. The interpretation oversimplifies the compounding effect of VAT. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
