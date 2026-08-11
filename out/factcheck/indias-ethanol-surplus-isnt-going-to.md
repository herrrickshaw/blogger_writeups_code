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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99352, Requested 2635. Please try again in 28m36.767999999s. Need more tokens? Upgrade to Dev Tier today a]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹68/L" — The article cites ₹68/L as the administered EBP procurement price, but the exchange rate used (₹95/$1) is dated August 2026, while the ethanol price is not explicitly tied to the same timeframe. The EBP price may have changed by January 2026 (the date of the USGC report), making the conversion to $0.72/L potentially inaccurate. [confidence: medium]

- "$0.449/L US ethanol, FOB Gulf — the world's cheapest major benchmark (USGC, 7 Jan 2026)" — The USGC report is cited as the source, but the article does not provide a direct link or full citation to verify the exact figure. While the claim is plausible, the lack of verifiable sourcing for this specific number raises doubt. [confidence: low]

INTERPRETATION ERRORS:
- "India's own ethanol-economics research (a July 2026 analytical report on the country's blending programme) lays out the value ladder starkly: potable alcohol (IMFL, country liquor) earns a distiller 3–35 times the producer margin of fuel ethanol, and up to roughly 75 times more in state tax yield per litre" — The claim conflates *producer margin* (a private commercial gain) with *state tax yield* (a public revenue measure), which are distinct economic concepts. The comparison is apples-to-oranges because it mixes private profitability with public fiscal benefits. [confidence: high]

- "The stronger diversification path redirects idle capacity toward higher-value domestic markets it's already structurally positioned to serve: pharma-grade ethanol first, alongside the potable/ENA market and (on a longer horizon) sustainable aviation fuel via alcohol-to-jet conversion." — The article assumes that pharma-grade ethanol and sustainable aviation fuel (SAF) can seamlessly absorb surplus capacity without addressing regulatory hurdles (e.g., USP/IP compliance for pharma-grade ethanol) or technological readiness (e.g., SAF conversion infrastructure). This is an extrapolation beyond what the cited data (industry growth forecasts) supports. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
