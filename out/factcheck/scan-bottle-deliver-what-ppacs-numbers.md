# Fact/interpretation check — scan-bottle-deliver-what-ppacs-numbers

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/scan-bottle-deliver-what-ppacs-numbers.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99937, Requested 3608. Please try again in 51m2.88s. Need more tokens? Upgrade to Dev Tier today at https:]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "PSU oil companies' domestic LPG sales in April-June 2026 actually fell 15.6% year-on-year" — The article cites PPAC's Q1 FY2026-27 report for this claim, but the report's actual date is 1 July 2026, and FY2026-27 would not begin until April 2026. The sales data for April-June 2026 cannot be year-on-year compared to April-June 2025 because 2025-26 would not yet be complete at the time of the report. [confidence: high]

INTERPRETATION ERRORS:
- "Active domestic LPG connections have grown from 14.9 crore in 2015 to 33.14 crore this July, a genuine, government-verified expansion" — While the growth in connections is real, the article implies this directly reflects increased LPG consumption or usage, which is not necessarily true. The number of active connections does not account for deactivated or dormant connections, refill rates, or actual consumption per connection. The 15.6% drop in sales volume in Q1 FY2026-27 suggests that the increase in connections does not directly translate to increased consumption. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
