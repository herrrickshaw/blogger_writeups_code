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
- "~12 GW Rooftop capacity added since Feb 2024, ~33 lakh systems (May 2026)" — The article claims "~12 GW" as of May 2026, but earlier it states "9,566.89 MW of rooftop capacity had been added as of 20 March 2026." The conversion from MW to GW is inconsistent (9,566.89 MW = 9.57 GW, not ~12 GW), and the May 2026 figure appears to be an extrapolation without clear sourcing. [confidence: high]

- "₹78,000 Maximum central subsidy, 3 kW and above, under PM Surya Ghar" — The subsidy table shows ₹78,000 for 3 kW and above, but the description states it is derived from "60% up to 2 kW, plus 40% of the additional cost from 2–3 kW." This implies the subsidy is not a flat ₹78,000 for all systems ≥3 kW but depends on the benchmark cost, which is not explicitly defined in the article. The claim oversimplifies the subsidy structure. [confidence: medium]

INTERPRETATION ERRORS:
- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — The article presents these projections as direct outcomes of the scheme without clarifying the assumptions behind them (e.g., average system size, capacity factors, grid emission factors, or degradation rates). These figures likely rely on modeling that is not transparent in the article, making it unclear whether they are realistic or achievable. [confidence: high]

- "A domestic battery of that size is roughly ₹1.5–3 lakh installed at current prices... which is comfortably more than the entire subsidy on the panels it would serve." — The article compares the cost of a battery to the subsidy for panels without accounting for the fact that the subsidy is only for the solar component, not the battery. While the comparison highlights a disparity in incentives, it does not address whether the battery's cost is justified by its benefits (e.g., energy savings, resilience) or whether the subsidy structure is the primary barrier to adoption. The reasoning gap is that the claim assumes the battery's cost is prohibitive without evaluating its economic or operational value. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
