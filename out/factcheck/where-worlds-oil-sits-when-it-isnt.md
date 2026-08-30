# Fact/interpretation check — where-worlds-oil-sits-when-it-isnt

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/where-worlds-oil-sits-when-it-isnt.html`

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
- "~25% Share of world seaborne crude & products trade that normally transits the Strait of Hormuz (2025 baseline, pre-crisis)" — The claim cites a 2025 baseline, but the article later references a Congressional Research Service source stating the ~25% figure as a general baseline without a specific year. The 2025 attribution is unsupported and potentially incorrect. [confidence: high]

- "Iran's floating-storage buildup... is the ship-to-shore version of this same logic running in reverse for a specific, blockade-driven reason rather than a price signal" — While the blockade is a cited reason, the article does not provide primary evidence linking the floating storage buildup *directly* to the blockade as the sole or primary driver, rather than other factors like demand destruction or logistical constraints. The claim assumes causation without sufficient verification. [confidence: medium]

INTERPRETATION ERRORS:
- "The US Strategic Petroleum Reserve has an authorised capacity of 714 million barrels across its Gulf Coast salt-cavern sites — a figure widely (and correctly) cited as the SPR's size. But the actual level in the reserve fell below 300 million barrels in early August 2026, the lowest since 1983..." — The article correctly distinguishes between authorised capacity and actual stock levels but then implies that the SPR's role as "insurance rather than working inventory" is undermined by the drawdown. This conflates policy purpose with operational reality; strategic reserves are *designed* to be drawn down in emergencies, so the drawdown does not invalidate their insurance function. [confidence: high]

- "The Brent-WTI spread... is itself a shore-vs-ship signal: WTI's price is set at a hub with pipeline and limited storage access rather than direct port access, so when seaborne routes tighten (as Hormuz has), a barrel that can reach open water commands a premium over one that's landlocked at Cushing, widening the discount." — The spread reflects multiple factors (e.g., regional supply/demand imbalances, refining capacity, pipeline constraints), not solely seaborne route tightness. The article overgeneralizes the spread as a direct proxy for shore-vs-ship storage pressure without accounting for other drivers. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
