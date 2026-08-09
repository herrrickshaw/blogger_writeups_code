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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99339, Requested 2048. Please try again in 19m58.368s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹78,000 Maximum central subsidy, 3 kW and above" — The article later contradicts this by stating the subsidy is capped at 3 kW, with the same ₹78,000 applying to systems of 3 kW or larger. The claim implies the subsidy scales beyond 3 kW, which is incorrect. [confidence: high]

- "~12 GW Rooftop capacity added since Feb 2024, ~33 lakh systems (May 2026)" — The article cites PIB figures for 9,566.89 MW as of 20 March 2026 and "above 12 GW" for May 2026, but the phrasing "~12 GW" is ambiguous and could mislead readers into thinking the 12 GW figure is exact or finalized, when it is an estimate. [confidence: medium]

INTERPRETATION ERRORS:
- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — While the government's estimate may be correct, the article does not provide the methodology or assumptions behind these projections (e.g., capacity factors, degradation rates, or grid emission factors). Without this context, the figures cannot be independently verified or assessed for reasonableness. [confidence: high]

- "The current cap makes a large array pointless; pairing a higher cap with a storage requirement would buy evening-peak relief rather than more midday export." — The article assumes that increasing the subsidy cap for households adding storage would necessarily lead to evening-peak relief, but it does not provide evidence that households would actually invest in storage under such a policy or that the storage would be used for evening-peak purposes. The causal link between policy change and outcome is speculative. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
