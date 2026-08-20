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
- "~25% Share of world seaborne crude & products trade that normally transits the Strait of Hormuz (2025 baseline, pre-crisis)" — The cited source (Congress.gov/CRS) likely refers to a pre-2025 baseline, as the 25% figure is a long-standing estimate (e.g., EIA and IEA have cited ~20–25% for years). The article incorrectly labels it as a "2025 baseline," which is not supported by the cited source or historical data. [confidence: high]

- "China does not publish this figure. Every number for China's reserves in circulation... is a third-party estimate... The EIA's own figure (~1.4 billion barrels of combined government and commercial inventory as of December 2025) is one of the more conservatively sourced estimates available..." — The article claims China's reserves are entirely estimated, but the IEA and other official sources (e.g., China's National Bureau of Statistics) do publish *some* official data on strategic petroleum reserves (e.g., monthly releases or capacity announcements). The claim overstates the lack of official disclosure. [confidence: medium]

---

INTERPRETATION ERRORS:
- "Iran's floating-storage buildup... is the ship-to-shore version of this same logic running in reverse for a specific, blockade-driven reason rather than a price signal: those cargoes are laden and waiting, not because holding them is profitable, but because the US port blockade is physically preventing the ship-to-shore transfer that would normally happen on a commercial timetable." — The article conflates two distinct mechanisms: (1) *forced* floating storage due to the blockade (involuntary) and (2) *voluntary* floating storage driven by contango (profit-seeking). While both involve oil sitting idle, the price impact differs: forced storage represents a *supply overhang* that could flood the market if resolved, whereas contango-driven storage is a *temporary buffer*. The article does not clearly separate these effects when discussing price signals. [confidence: high]

- "The Brent-WTI spread... is itself a shore-vs-ship signal: WTI's price is set at a hub with pipeline and limited storage access rather than direct port access, so when seaborne routes tighten (as Hormuz has), a barrel that can reach open water commands a premium over one that's landlocked at Cushing, widening the discount." — The spread reflects multiple factors (e.g., regional supply/demand imbalances, refining capacity, pipeline bottlenecks), not *solely* seaborne vs. landlocked access. The Hormuz disruption is one contributor, but the article implies it is the *primary* driver without controlling for other variables (e.g., US shale production shifts, Cushing storage constraints). [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
