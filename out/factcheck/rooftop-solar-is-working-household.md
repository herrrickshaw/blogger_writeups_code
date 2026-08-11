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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99024, Requested 2048. Please try again in 15m26.208s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "~12 GW Rooftop capacity added since Feb 2024, ~33 lakh systems (May 2026)" — The article claims "~12 GW" as of May 2026, but earlier it states "9,566.89 MW of rooftop capacity had been added as of 20 March 2026," which is ~9.57 GW. The jump to ~12 GW in two months (March to May 2026) is inconsistent with the earlier figure and lacks a clear source or explanation for the rapid increase. [confidence: high]

- "₹78,000 Maximum central subsidy, 3 kW and above, under PM Surya Ghar" — The subsidy table shows ₹78,000 for 3 kW and above, but the text claims this is the "maximum" subsidy. However, the table clarifies that the subsidy is capped at ₹78,000 for systems 3 kW and above, meaning it is not a "maximum" but a fixed amount for larger systems. The term "maximum" is misleading. [confidence: high]

INTERPRETATION ERRORS:
- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — The article presents this as a factual projection but does not provide the methodology or assumptions behind these estimates (e.g., average system size, capacity factors, or grid emission factors). Without these details, the claim cannot be verified as a reasonable extrapolation from the cited sources. [confidence: medium]

- "The time taken to add one lakh households has fallen from 118 days to under eight" — The article implies this is a direct comparison of the pace of installations, but it does not clarify whether the "118 days" figure refers to the initial phase of the program or a specific period. Without context, this comparison could be misleading, as the "118 days" might not represent a consistent baseline for comparison. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
