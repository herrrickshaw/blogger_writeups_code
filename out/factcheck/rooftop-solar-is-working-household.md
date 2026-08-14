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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99213, Requested 2493. Please try again in 24m33.984s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "~12 GW Rooftop capacity added since Feb 2024, ~33 lakh systems (May 2026)" — The claim conflates two different timeframes. The 9,566.89 MW (9.57 GW) figure is explicitly dated as of 20 March 2026, while the "above 12 GW" figure is stated as of May 2026. The article does not clarify whether the 12 GW includes the 9.57 GW or is cumulative over a different period, creating ambiguity in the total capacity added. [confidence: high]

- "₹78,000 Maximum central subsidy, 3 kW and above, under PM Surya Ghar" — The subsidy table shows ₹78,000 as the maximum for 3 kW and above, but the article does not specify that this is the *maximum* subsidy (i.e., it is the same for all systems ≥3 kW). The phrasing could mislead readers into thinking ₹78,000 is the subsidy for *any* system ≥3 kW, which is correct but not explicitly clarified as the cap. [confidence: medium]

INTERPRETATION ERRORS:
- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — The article presents these projections as direct outcomes of the PM Surya Ghar scheme without clarifying the assumptions behind them (e.g., average system size, capacity utilization factor, or grid emission factors). These figures likely rely on modeling that assumes optimal performance and may not reflect real-world variability in household adoption, system efficiency, or grid conditions. [confidence: high]

- "A domestic battery of that size is roughly ₹1.5–3 lakh installed at current prices, which is comfortably more than the entire subsidy on the panels it would serve." — While the battery cost estimate is plausible, the article does not provide a source or methodology for this figure, nor does it account for potential economies of scale, regional price variations, or future cost reductions. The comparison to the ₹78,000 subsidy is presented as a straightforward cost-benefit analysis without acknowledging these uncertainties. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
