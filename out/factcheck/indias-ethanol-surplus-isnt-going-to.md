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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99712, Requested 2635. Please try again in 33m47.808s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹68/L" — The article cites ₹68/L as the administered EBP procurement price, but the exchange rate used (₹95/$1) is dated August 2026, while the ethanol price is not explicitly tied to this date. The EBP price is typically revised annually (e.g., ₹60–65/L in recent years), and ₹68/L may not reflect the current rate as of January 2026. [confidence: medium]

- "$0.72/L India's own EBP administered price (₹68/L) at current INR/USD — above both" — The conversion of ₹68/L to $0.72/L assumes ₹95/$1, but this exchange rate is speculative (labeled as "August 2026"). If the ethanol price is from January 2026, the exchange rate would likely be different (e.g., ₹83–85/$1 in early 2026), making the $0.72/L figure inaccurate. [confidence: high]

INTERPRETATION ERRORS:
- "India's ethanol surplus isn't going to Brazil or the USA — and the price data explains why" — The article conflates *potential* export opportunities (e.g., pharma-grade ethanol to Africa/EU) with *fuel ethanol* surplus, which is legally restricted from export. The price data (e.g., $0.449–0.611/L for fuel ethanol) only explains why *fuel ethanol* exports are unviable, not why *no ethanol* (including pharma-grade) is exported to Brazil/USA. The claim overgeneralizes the applicability of the price data. [confidence: high]

- "The stronger diversification path redirects idle capacity toward higher-value domestic markets it's already structurally positioned to serve: pharma-grade ethanol first, alongside the potable/ENA market..." — The article assumes that pharma-grade ethanol production is a *direct* substitute for fuel ethanol capacity without addressing critical constraints: (1) pharma-grade ethanol requires specialized distillation, purification, and compliance (e.g., USP/IP standards), which may not be feasible in all existing fuel-ethanol plants; (2) the "idle capacity" (~43% of 2,100 cr L) may not align with the technical requirements of pharma-grade production. The claim extrapolates capacity utilization to an unrelated product without evidence of conversion feasibility. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
