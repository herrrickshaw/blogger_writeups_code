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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99383, Requested 2048. Please try again in 20m36.384s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹78,000 Maximum central subsidy, 3 kW and above, under PM Surya Ghar" — The article later contradicts this by stating the subsidy is capped at 3 kW, with the same ₹78,000 applying to systems of 3 kW or larger. The claim implies the subsidy is available for systems *above* 3 kW, which is incorrect. [confidence: high]

- "~12 GW Rooftop capacity added since Feb 2024, ~33 lakh systems (May 2026)" — The article cites PIB figures for 9,566.89 MW as of 20 March 2026 and "above 12 GW" for May 2026, but the exact figure of "~12 GW" is not directly sourced from PIB and may be an approximation. The phrasing suggests a precise figure, which could be misleading. [confidence: medium]

INTERPRETATION ERRORS:
- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — While the government's estimate may be correct, the article does not provide the methodology or assumptions behind these projections (e.g., average system size, capacity factor, or grid emission factors). Without this context, the figures cannot be independently verified or assessed for plausibility. [confidence: high]

- "A domestic battery of that size is roughly ₹1.5–3 lakh installed at current prices, which is comfortably more than the entire subsidy on the panels it would serve." — The article correctly notes the lack of subsidy for household batteries but does not account for potential cost reductions due to economies of scale, technological advancements, or alternative financing models (e.g., leasing or pay-as-you-go). The claim implies the high cost is a permanent barrier without considering dynamic market changes. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
