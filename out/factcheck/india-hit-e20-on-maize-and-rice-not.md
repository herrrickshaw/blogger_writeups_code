# Fact/interpretation check — india-hit-e20-on-maize-and-rice-not

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-hit-e20-on-maize-and-rice-not.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

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
- "Blending is at 20 per cent through ESY 2025-26, held month after month." — The article later contradicts this by stating that only 59% of offered capacity (1,048 crore litres) was allocated, implying blending may not have consistently reached 20% throughout the year. The claim is unverifiable as stated. [confidence: medium]

- "Maize alone is 45.7 per cent, up from 6.2 per cent in ESY 2022-23 — a sevenfold shift in three years." — The article later cites maize's share as 45.68% in ESY 2025-26 and 6.2% in ESY 2022-23, but the "sevenfold shift" phrasing is misleading because 45.68 / 6.2 ≈ 7.37, not exactly sevenfold. [confidence: high]

INTERPRETATION ERRORS:
- "The target has been met. Blending has held at 20 per cent through the current Ethanol Supply Year. And the assumption behind the question turned out to be wrong." — The article conflates *allocation* (1,048 crore litres) with *actual blending* (which may be lower due to unplaced capacity). The 20% blending target is based on actual supply, not allocations, creating a false equivalence. [confidence: high]

- "The most expensive feedstock became the largest one. Cost was not the binding constraint. Availability was." — While maize is indeed the largest feedstock, the claim that cost was irrelevant ignores the economic reality that distilleries would not have switched to maize if it weren’t profitable at the given price (₹71.86/litre). The reasoning incorrectly separates cost from availability as mutually exclusive factors. [confidence: high]
