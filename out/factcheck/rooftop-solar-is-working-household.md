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
- "~12 GW Rooftop capacity added since Feb 2024, ~33 lakh systems (May 2026)" — The article claims "~12 GW" as of May 2026, but earlier in the text it states "9,566.89 MW of rooftop capacity had been added as of 20 March 2026" (~9.57 GW). The jump to "~12 GW" by May 2026 is an unsupported extrapolation without a clear source or timeframe. [confidence: high]

- "₹78,000 Maximum central subsidy, 3 kW and above, under PM Surya Ghar" — The subsidy table shows ₹78,000 as the maximum for 3 kW and above, but the article later states: "The central financial assistance is not a vague percentage. It is a fixed slab...". However, the ₹78,000 figure is derived from a 60% subsidy up to 2 kW and 40% for the additional 1 kW (2–3 kW), implying the subsidy is not a flat ₹78,000 for *all* systems 3 kW and above but varies based on benchmark costs. The claim oversimplifies the subsidy structure. [confidence: high]

INTERPRETATION ERRORS:
- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — The article presents these projections as if they are directly attributable to the PM Surya Ghar scheme, but it does not clarify whether these estimates account for system degradation, actual usage patterns, or grid conditions. The projections may assume idealized conditions (e.g., consistent sunlight, no shading, full utilization) that are unlikely in practice. [confidence: medium]

- "A domestic battery of that size is roughly ₹1.5–3 lakh installed at current prices, which is comfortably more than the entire subsidy on the panels it would serve." — While the cost comparison is factually plausible, the article implies that the lack of battery subsidy is the sole barrier to household battery adoption without addressing other critical factors such as electricity tariff structures, payback periods, or consumer behavior (e.g., willingness to invest in storage despite long-term savings). The claim frames the issue as purely financial, ignoring non-monetary barriers. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
