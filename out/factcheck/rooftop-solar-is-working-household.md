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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99309, Requested 2048. Please try again in 19m32.448s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹78,000 Maximum central subsidy, 3 kW and above" — The article later contradicts this by stating that the subsidy is capped at ₹78,000 for systems of 3 kW and above, implying no additional subsidy for larger systems. However, the table shows that the subsidy is derived as 60% of benchmark cost up to 2 kW, plus 40% of the additional cost from 2–3 kW, effectively capping the subsidy at 3 kW. The claim that ₹78,000 is the maximum for 3 kW and above is correct, but the phrasing could be misinterpreted as implying a higher subsidy for larger systems, which is not the case. [confidence: high]

- "₹0 Central subsidy available to a household adding a battery" — The article claims no central subsidy is available for household batteries under PM Surya Ghar. While this is likely correct based on the scheme's design, the article does not provide an official government source explicitly stating this. The claim is plausible but unverified in the given text. [confidence: medium]

INTERPRETATION ERRORS:
- "Rooftop under this one scheme is therefore roughly 8% of all solar capacity in the country, built in two years." — The article calculates 12 GW of rooftop solar as 8% of India's total solar fleet (150.26 GW in FY2025-26). However, this comparison mixes installed capacity (GW) with generation capacity (units of electricity). Rooftop solar's contribution to total solar capacity is not the same as its contribution to electricity generation, as rooftop systems typically have lower capacity factors than utility-scale solar. The comparison is apples-to-oranges. [confidence: high]

- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — The article presents these figures as projections without clarifying the assumptions behind them (e.g., average system size, capacity factor, or CO₂e per unit of electricity). Without these details, the projections are not verifiable and could be misleading if taken at face value. The claim extrapolates from unspecified assumptions to a broad conclusion. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
