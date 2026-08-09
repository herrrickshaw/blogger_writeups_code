# Fact/interpretation check — fy2025-26-sample-report-india-trade

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fy2025-26-sample-report-india-trade.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99863, Requested 2862. Please try again in 39m14.4s. Need more tokens? Upgrade to Dev Tier today at https:]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "GDP growth (real, FAE) +7% First Advance Estimate — MoSPI's Provisional Estimate, released before this snapshot was compiled, has since superseded this figure" — The claim implies the First Advance Estimate (FAE) was superseded by a Provisional Estimate, but FAE is the earliest official estimate, followed by the Provisional Estimate later. The FAE is not "superseded" in the sense of being incorrect; it is a preliminary figure later refined. [confidence: high]

INTERPRETATION ERRORS:
- "NITI Aayog's blended goods+services trade reached $1.84 trillion in FY2025-26 (exports +4.2%, imports +6.5% y-o-y) — this repo's goods-only figures show export growth of just +0.92% over the same year, explained by services exports growing faster (+9.0% per NITI Aayog) and pulling the blended rate up, not a discrepancy." — While the explanation is plausible, the article does not provide the actual goods-only export growth rate from NITI Aayog's report to directly compare with the repo's +0.92% figure. The reasoning assumes the discrepancy is solely due to services exports without verifying the goods-only growth rate from the same source. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
