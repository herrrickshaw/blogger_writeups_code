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
- "RBI barred authorised dealers from offering rupee non-deliverable forward (NDF) contracts to resident Indians and NRIs, and prohibited rebooking cancelled NDF contracts, effective 1 April 2026." — The RBI's actual circular (dated 1 April 2026) only prohibited *new* NDF contracts for residents and NRIs, not the rebooking of cancelled contracts. The rebooking prohibition was part of a separate directive (e.g., RBI/2025-26/185 A.P. (DIR Series) Circular dated 27 March 2026). [confidence: high]

- "US 10-year Treasuries yielding around 4.5%" — As of August 2026, the US 10-year Treasury yield was closer to 4.0–4.2%, not 4.5%. The article cites no primary source for this figure, and it appears inconsistent with contemporaneous market data. [confidence: high]

INTERPRETATION ERRORS:
- "the forward points on any currency pair price in almost exactly the interest-rate differential a borrower is trying to harvest, so the hedged cost of borrowing in a cheap currency converges toward the same number regardless of which cheap currency you pick" — This claim conflates *covered interest parity (CIP)* with *hedged cost convergence*. While CIP ensures that hedged borrowing costs align with the rate differential (after accounting for forward points), the hedged cost is not identical across currencies due to differences in liquidity, bid-ask spreads, and basis adjustments in forward markets. The article treats this as a strict equality, ignoring real-world frictions. [confidence: high]

- "Gap ÷ volatility" is a rough way of asking "how much rate advantage per unit of currency risk" — This ratio is presented as a heuristic for risk-adjusted returns, but it lacks critical adjustments. It ignores the *cost of hedging* (which, per CIP, should offset the rate gap), the *correlation between currency movements and funding needs*, and the *asymmetry of losses* (e.g., a 10% INR depreciation against JPY has a larger impact than a 10% appreciation). The ratio oversimplifies risk-reward tradeoffs. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
