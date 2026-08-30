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

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹78,000 Maximum central subsidy, 3 kW and above, under PM Surya Ghar" — The article later contradicts this by stating the subsidy is capped at ₹78,000 for systems of 3 kW and above, with the marginal rate stepping down from 60% to 40% in the third kilowatt. The claim implies the subsidy remains ₹78,000 for all systems 3 kW and above, which is incorrect as it only applies up to 3 kW. [confidence: high]

- "₹0 Central subsidy available to a household adding a battery" — While the article correctly states no subsidy is provided for batteries under PM Surya Ghar, it does not acknowledge that some state-level subsidies or incentives for batteries may exist (e.g., Gujarat, Delhi, or other states offering additional support). The claim implies a complete absence of any subsidy for batteries, which may not be accurate. [confidence: medium]

INTERPRETATION ERRORS:
- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — The article does not provide the source or methodology for these projections (e.g., assumptions about system performance, degradation, or grid emission factors). Without this context, the figures cannot be verified as reasonable or accurate. [confidence: high]

- "A domestic battery of that size is roughly ₹1.5–3 lakh installed at current prices (an indicative market price, not an official figure), which is comfortably more than the entire subsidy on the panels it would serve." — The article compares the cost of a battery to the subsidy for panels without accounting for the additional value a battery provides (e.g., energy arbitrage, backup power, or reduced grid dependency). This apples-to-oranges comparison ignores the potential economic benefits of storage, making the conclusion unsupported. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
