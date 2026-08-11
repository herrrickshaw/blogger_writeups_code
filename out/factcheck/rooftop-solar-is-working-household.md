# Fact/interpretation check — rooftop-solar-is-working-household

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/rooftop-solar-is-working-household.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99941, Requested 2048. Please try again in 28m38.496s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "~12 GW Rooftop capacity added since Feb 2024, ~33 lakh systems (May 2026)" — The article claims "~12 GW" capacity added since February 2024, but later states "9,566.89 MW of rooftop capacity had been added as of 20 March 2026" and "above 12 GW across roughly 33 lakh installations" by May 2026. The figures are inconsistent (9.57 GW vs. >12 GW), and the "~12 GW" claim is unverifiable as a standalone figure. [confidence: high]

- "₹78,000 Maximum central subsidy, 3 kW and above" — The subsidy table shows ₹78,000 as the maximum for 3 kW and above, but the text also states "The central financial assistance is not a vague percentage. It is a fixed slab," implying the ₹78,000 is the *exact* maximum. However, the table's derivation suggests it is a *capped* amount (₹60,000 for 2 kW + 40% of additional cost from 2–3 kW), not a flat ₹78,000 for all systems ≥3 kW. The phrasing is misleading. [confidence: high]

INTERPRETATION ERRORS:
- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — The article presents these projections as direct outputs of the PM Surya Ghar scheme, but it does not clarify whether these estimates account for *actual* generation (which depends on system performance, shading, maintenance, etc.) or assume ideal conditions. The gap is that the projections may overstate real-world impact without adjusting for potential underperformance. [confidence: medium]

- "The time taken to add one lakh households has fallen from 118 days to under eight" — The article implies this dramatic acceleration is solely due to the PM Surya Ghar scheme's effectiveness, but it does not address external factors (e.g., pre-existing rooftop solar growth, state-level policies, or vendor-driven adoption) that could contribute to the trend. The causal claim lacks supporting evidence. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
