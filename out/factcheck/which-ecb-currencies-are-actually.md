# Fact/interpretation check — which-ecb-currencies-are-actually

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/which-ecb-currencies-are-actually.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "RBI barred authorised dealers from offering rupee non-deliverable forward (NDF) contracts to resident Indians and NRIs, and prohibited rebooking cancelled NDF contracts, effective 1 April 2026" — The RBI's ban on NDF contracts for residents and NRIs was announced in April 2023 (effective immediately) and formalized in a circular dated 6 April 2023, not April 2026. The article incorrectly dates this policy change to 2026. [confidence: high]

- "US 10-year Treasuries yielding around 4.5%" — As of August 2026, the US 10-year Treasury yield is not around 4.5%. Historical data and market projections for mid-2026 suggest yields are likely closer to 3.8–4.2% (or higher, depending on macro conditions), but 4.5% is inconsistent with current trends. [confidence: medium]

INTERPRETATION ERRORS:
- "the forward points on any currency pair price in almost exactly the interest-rate differential a borrower is trying to harvest, so the hedged cost of borrowing in a cheap currency converges toward the same number regardless of which cheap currency you pick" — This claim conflates theoretical covered interest parity (CIP) with practical hedging costs. While CIP ensures that hedged borrowing costs should theoretically converge, real-world hedging costs (e.g., bid-ask spreads, liquidity constraints, or basis spreads) can vary significantly across currencies, especially for less liquid markets or during stress periods. The article does not acknowledge these deviations. [confidence: high]

- "Gap ÷ volatility" is a simple ratio, not a risk-adjusted-return measure in the formal finance sense — it is a rough way of asking "how much rate advantage per unit of currency risk," nothing more precise than that" — While the article correctly notes that the ratio is not a formal risk-adjusted measure, it later uses this ratio to imply a trade-off between rate advantage and risk without clarifying that this is a heuristic. The ratio does not account for compounding effects, correlation with other risks (e.g., credit risk), or the non-linear payoffs of currency exposure, leading to an oversimplified interpretation of "bang for the buck." [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
