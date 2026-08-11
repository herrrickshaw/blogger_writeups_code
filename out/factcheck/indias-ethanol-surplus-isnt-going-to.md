# Fact/interpretation check — indias-ethanol-surplus-isnt-going-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-ethanol-surplus-isnt-going-to.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99362, Requested 2635. Please try again in 28m45.408s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹68/L" — The article cites ₹68/L as the administered price for ethanol under the EBP programme, but the exchange rate used (₹95/$1) is dated August 2026, which is inconsistent with the article's other dates (e.g., 7 January 2026 for USGC pricing). The exchange rate should align with the pricing date for accuracy. [confidence: high]

- "$0.72/L India's own EBP administered price (₹68/L) at current INR/USD — above both" — The conversion of ₹68/L to $0.72/L assumes ₹95/$1, but this exchange rate is not contemporaneous with the 7 January 2026 pricing data for USGC/Brazil benchmarks. The exchange rate should be from January 2026, not August 2026, leading to a miscalculation. [confidence: high]

INTERPRETATION ERRORS:
- "India's own ethanol-economics research (a July 2026 analytical report on the country's blending programme) lays out the value ladder starkly: potable alcohol (IMFL, country liquor) earns a distiller 3–35 times the producer margin of fuel ethanol, and up to roughly 75 times more in state tax yield per litre — which is exactly why capacity gravitates to liquor wherever licensing allows it." — The claim conflates *producer margin* (a private cost/revenue metric) with *state tax yield* (a public revenue metric), which are fundamentally different economic measures. The comparison is apples-to-oranges because one reflects private profitability while the other reflects fiscal revenue for governments. [confidence: high]

- "The practical case for pharma-grade diversification is that it doesn't require competing head-on with Brazilian sugarcane or U.S. corn economics on a commodity export market where India is structurally not the low-cost producer." — The argument assumes that pharma-grade ethanol production is insulated from feedstock cost pressures (e.g., sugarcane or corn prices), but high-purity ethanol production still depends on feedstock availability and pricing. The claim ignores that feedstock costs (e.g., molasses, grains) are a major input for pharma-grade ethanol, just as they are for fuel ethanol. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
