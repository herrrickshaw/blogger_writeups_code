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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99585, Requested 4989. Please try again in 1h5m51.936s. Need more tokens? Upgrade to Dev Tier today at htt]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹100.35/l PPAC published: ₹94.77/l" — The article incorrectly states the PPAC published petrol RSP in Delhi as ₹100.35/l when the table clearly shows ₹94.77/l. This is a direct contradiction of the cited source. [confidence: high]

- "$78.87/bbl Brent Crude, live (OilPriceAPI & Rigzone agree to 2¢)" — While the Brent crude price is correctly cited as $78.87/bbl, the claim that OilPriceAPI and Rigzone agree to 2¢ is unverifiable and not supported by the data-quality note, which highlights conflicting fields in OilPriceAPI's response. [confidence: medium]

INTERPRETATION ERRORS:
- "a 97% swing in crude (past-year low to high) would, on a naive full pass-through, move Delhi petrol by ≈43% (₹87.65 to ₹125.71)" — The article assumes a "naive full pass-through" scenario where only the dealer price and VAT layers scale with crude, but this ignores that VAT is a percentage-based tax applied on top of the dealer price, excise, and commission. The actual pass-through would be higher because VAT compounds on the increased dealer price, making the 43% estimate an understatement. [confidence: high]

- "Because ethanol's cost is fixed annually by government notification rather than tracking crude, a higher blend share structurally dampens how much a crude spike passes through to the pump" — The article correctly notes that ethanol's cost is fixed, but it incorrectly implies that this alone reduces volatility. In reality, the excise exemption on ethanol (not its fixed cost) is the primary reason for reduced volatility, as the excise duty is only applied to the non-ethanol portion of the blend. The fixed cost of ethanol does not directly affect the pass-through of crude price changes. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
