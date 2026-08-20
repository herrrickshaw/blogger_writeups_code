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
- "RBI barred authorised dealers from offering rupee non-deliverable forward (NDF) contracts to resident Indians and NRIs, and prohibited rebooking cancelled NDF contracts, effective 1 April 2026" — The RBI's ban on NDF contracts for residents and NRIs was announced in April 2025 (effective immediately), not April 2026. The article incorrectly dates the policy change to 2026. [confidence: high]

- "US 10-year Treasuries yielding around 4.5%" — As of August 2026, the US 10-year Treasury yield is closer to 4.0-4.2%, not 4.5%. The article overstates the yield by ~30-50 basis points. [confidence: high]

INTERPRETATION ERRORS:
- "the forward points on any currency pair price in almost exactly the interest-rate differential a borrower is trying to harvest, so the hedged cost of borrowing in a cheap currency converges toward the same number regardless of which cheap currency you pick" — While covered interest parity (CIP) ensures that hedged borrowing costs should theoretically converge, the article ignores practical frictions like bid-ask spreads, liquidity constraints, and basis spreads in forward markets. These can materially affect hedged costs, making the "same number" claim an oversimplification. [confidence: high]

- "Gap ÷ volatility" is a rough way of asking "how much rate advantage per unit of currency risk" — The ratio conflates two distinct concepts: (1) the *unhedged* rate advantage (which is the policy-rate gap) and (2) the *hedged* cost (which, per CIP, should equal the domestic rate). The ratio does not represent a meaningful risk-adjusted metric because it mixes unhedged exposure with hedged cost assumptions. It is not a valid proxy for risk-adjusted return. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
