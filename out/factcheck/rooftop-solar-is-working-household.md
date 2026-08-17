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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99957, Requested 2094. Please try again in 29m32.064s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹78,000 Maximum central subsidy, 3 kW and above, under PM Surya Ghar" — The article later contradicts this by stating the subsidy is capped at ₹78,000 for systems of 3 kW and above, with the marginal rate stepping down from 60% to 40% in the third kilowatt. The claim implies ₹78,000 is the maximum for all systems 3 kW and above, but the subsidy does not increase beyond 3 kW, making the phrasing misleading. [confidence: high]

- "~12 GW Rooftop capacity added since Feb 2024, ~33 lakh systems (May 2026)" — The article cites PIB figures stating 9,566.89 MW as of 20 March 2026 and "above 12 GW" as of May 2026. However, 12 GW is 12,000 MW, which is a significant jump from 9,566.89 MW in just over two months. The lack of clarity on whether the "above 12 GW" figure is rounded or includes projections introduces uncertainty. [confidence: medium]

INTERPRETATION ERRORS:
- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — The article presents these projections as direct outcomes of the PM Surya Ghar scheme without clarifying whether these estimates account for system degradation, maintenance downtime, or variations in solar insolation across regions. The projections may overstate actual generation and emissions savings. [confidence: high]

- "A domestic battery of that size is roughly ₹1.5–3 lakh installed at current prices, which is comfortably more than the entire subsidy on the panels it would serve." — While the battery cost estimate may be accurate, the article does not provide a cost-benefit analysis or payback period for households considering adding a battery. The claim implies that the lack of subsidy is the sole barrier, but other factors like electricity tariffs, battery lifespan, and grid reliability also influence the decision. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
