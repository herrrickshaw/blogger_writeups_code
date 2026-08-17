# Fact/interpretation check — the-fcc-lever-trading-petrol-yield-for

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-fcc-lever-trading-petrol-yield-for.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99747, Requested 5059. Please try again in 1h9m12.384s. Need more tokens? Upgrade to Dev Tier today at htt]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "ONGC Board gave in-principle approval, July 2026 — adds to the existing 1.5 MMT Mangalore facility" — The date is incorrect; the approval was given in **June 2024**, not July 2026. [confidence: high]

- "India's existing ISPRL reserves total 5.33 MMT across Visakhapatnam (1.33), Mangalore (1.5) and Padur (2.5)" — The Padur reserve capacity is **2.5 MMT**, but the Visakhapatnam reserve is **1.33 MMT**, and Mangalore is **1.5 MMT**, totaling **5.33 MMT**, which is correct. However, the article later states "ISPRL's own stated ambition is to roughly triple total capacity to about 15 MMT within a decade," which is outdated as the current total is already **5.33 MMT**, and tripling would imply **15.99 MMT**, not 15 MMT. [confidence: high]

INTERPRETATION ERRORS:
- "That surplus opens a narrow but real opportunity: the petrol a refinery no longer needs to blend can, with real (not cosmetic) modifications to the FCC unit's gas-recovery train, come out as LPG instead — directly addressing India's import-heavy cooking-gas supply." — The claim implies a direct causal link between diverting petrol-equivalent crude fractions to LPG and reducing India's LPG import bill. However, the article later acknowledges that the incremental C3/C4 olefins from the FCC could instead be routed to petrochemical production (e.g., polypropylene), which would not reduce LPG imports. The conclusion that this shift "directly addresses India's import-heavy cooking-gas supply" is not supported without resolving the allocation choice between LPG and petrochemical feedstock. [confidence: high]

- "The FCC-yield lever in Sections 2–3 is a comparatively small, low-capex debottlenecking move next to the scale of capital India's refiners are currently putting into petrochemical capacity outright — new crackers, integrated refinery-petrochemical complexes, and polymer units, several of which broke ground or reached board approval within the last twelve months." — While the capex figures for petrochemical projects are large, the article does not provide a direct comparison of the costs of the FCC modifications (e.g., debottlenecking vs. new crackers). The claim assumes the FCC lever is "low-capex" without quantifying the actual costs of the modifications (e.g., replacing WGC or other equipment), which could vary significantly. The comparison is an apples-to-oranges extrapolation. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
