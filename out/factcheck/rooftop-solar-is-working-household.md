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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 98985, Requested 2094. Please try again in 15m32.256s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹78,000 Maximum central subsidy, 3 kW and above, under PM Surya Ghar" — The subsidy table shows ₹78,000 is only for 3 kW systems, not "3 kW and above." For systems larger than 3 kW, the subsidy remains capped at ₹78,000. [confidence: high]

- "₹0 Central subsidy available to a household adding a battery" — The article claims no subsidy is available for household batteries under PM Surya Ghar, but this is not explicitly stated in the cited sources (MNRE guidelines or PIB releases). The absence of evidence does not confirm the claim. [confidence: medium]

INTERPRETATION ERRORS:
- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — The article presents these projections as direct outputs of the PM Surya Ghar scheme, but it does not clarify whether these estimates account for system degradation, actual usage patterns, or grid integration challenges. The projections may overstate real-world benefits without proper caveats. [confidence: high]

- "The marginal rate also steps down from 60% to 40% in the third kilowatt. Both features push households toward small systems, which is deliberate: the scheme is designed to cover a typical domestic load, not to subsidise a household becoming a generator." — While the subsidy structure may incentivize smaller systems, the article does not provide evidence that this was an explicit policy goal. The claim assumes intent without citing supporting documentation (e.g., MNRE policy statements or scheme guidelines). [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
