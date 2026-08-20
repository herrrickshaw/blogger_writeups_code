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
- "₹78,000 Maximum central subsidy, 3 kW and above, under PM Surya Ghar" — The article later contradicts this by stating the subsidy is capped at ₹78,000 for systems of 3 kW and above, with the marginal rate stepping down from 60% to 40% in the third kilowatt. The claim implies the full ₹78,000 applies to all systems 3 kW and above, which is incorrect. [confidence: high]

- "~12 GW Rooftop capacity added since Feb 2024, ~33 lakh systems (May 2026)" — The article cites "9,566.89 MW of rooftop capacity had been added as of 20 March 2026, and by May 2026 the figure was above 12 GW." This is inconsistent because 12 GW is 12,000 MW, which is significantly higher than the 9,566.89 MW figure just two months prior. The jump from ~9.57 GW to >12 GW in two months is implausible without clarification. [confidence: high]

INTERPRETATION ERRORS:
- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — The article does not provide the source or methodology for these projections (e.g., average system size, capacity factor, or CO₂e calculation assumptions). Without this context, the figures cannot be verified as reasonable or accurate interpretations of the scheme's potential impact. [confidence: medium]

- "A domestic battery of that size is roughly ₹1.5–3 lakh installed at current prices (an indicative market price, not an official figure), which is comfortably more than the entire subsidy on the panels it would serve." — While the battery cost claim may be correct, the article does not explain how the subsidy on the panels (₹78,000 for a 3 kW system) relates to the battery's cost in terms of economic viability or payback period. The comparison is apples-to-oranges because the subsidy is for panels, not batteries, and does not account for the value of storage in reducing electricity bills or grid dependence. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
