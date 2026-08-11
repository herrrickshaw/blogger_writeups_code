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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99567, Requested 2604. Please try again in 31m15.744s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "GDP growth (real, FAE) +7% First Advance Estimate — MoSPI's Provisional Estimate, released before this snapshot was compiled, has since superseded this figure" — The claim that MoSPI's Provisional Estimate has superseded the First Advance Estimate is incorrect. The First Advance Estimate (FAE) is the earliest official GDP growth estimate released by MoSPI, followed later by the Provisional Estimate. The Provisional Estimate does not supersede the FAE; both are sequential estimates with the Provisional Estimate being more refined. [confidence: high]

INTERPRETATION ERRORS:
- "NITI Aayog's pharma-sector thematic figure ($35.8bn pharma+API exports) is ~$10.7bn higher than this report's own HS30-only figure ($25,073.4M) because it includes API exports that sit in HS29, not HS30 — consistent with this repo's existing PLI Bulk Drugs finding." — The reasoning gap here is that the article assumes the difference between NITI Aayog's pharma+API exports ($35.8bn) and the report's HS30-only figure ($25.07bn) is solely due to HS29 API exports being excluded. However, HS30 includes more than just APIs (e.g., vitamins, hormones), and NITI Aayog's broader pharma+API category may include additional subcategories or adjustments not accounted for in the HS30 figure. The explanation oversimplifies the discrepancy without verifying whether HS29 alone accounts for the full $10.7bn difference or if other factors (e.g., methodological differences, inclusion of services, or re-exports) are at play. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
