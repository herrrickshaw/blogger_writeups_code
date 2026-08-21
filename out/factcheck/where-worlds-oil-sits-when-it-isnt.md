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
- "~25% Share of world seaborne crude & products trade that normally transits the Strait of Hormuz (2025 baseline, pre-crisis)" — The cited source (Congress.gov/CRS) likely refers to a pre-2025 baseline, as the 25% figure is a long-standing estimate (e.g., EIA and IEA have cited ~20–25% for years). The article incorrectly labels it as a "2025 baseline," which is not supported by the sources. [confidence: high]

- "298.7M bbl US Strategic Petroleum Reserve level, 10 Aug 2026 — lowest since 1983, against 714M bbl of authorised capacity" — While the SPR level is correct (per CNBC), the claim that it is the "lowest since 1983" is unverified. The SPR has historically dipped below 300M bbl in the past (e.g., 2011, 2020), and the article does not provide a primary source confirming this is the lowest since 1983. [confidence: medium]

INTERPRETATION ERRORS:
- "Iran's floating-storage buildup... is the ship-to-shore version of this same logic running in reverse for a specific, blockade-driven reason rather than a price signal" — The article conflates two distinct mechanisms: (1) *voluntary* floating storage (driven by contango/backwardation) and (2) *forced* floating storage (due to the US blockade). While both involve oil sitting idle, the price dynamics and market implications differ fundamentally. The article implies the same "logic" applies, but the blockade-driven storage is not a market-driven arbitrage; it represents a supply overhang that could flood the market if resolved, unlike contango-driven storage, which is a deliberate market response. [confidence: high]

- "The Brent-WTI spread... is itself a shore-vs-ship signal: WTI's price is set at a hub with pipeline and limited storage access rather than direct port access, so when seaborne routes tighten (as Hormuz has), a barrel that can reach open water commands a premium over one that's landlocked at Cushing" — The spread is influenced by multiple factors (e.g., pipeline bottlenecks, regional supply/demand imbalances, refining capacity), not just seaborne vs. landlocked access. The article oversimplifies the causal link by attributing the entire $5.96/bbl spread to Hormuz-related seaborne tightness, ignoring other potential drivers like Cushing's storage constraints or Midwest refining demand. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
