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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99926, Requested 2604. Please try again in 36m25.92s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "GDP growth (real, FAE) +7% First Advance Estimate — MoSPI's Provisional Estimate, released before this snapshot was compiled, has since superseded this figure" — The claim implies the First Advance Estimate (FAE) was superseded by a Provisional Estimate, but the FAE is the earliest official estimate, followed by the Provisional Estimate later. The FAE is not "superseded" in the sense of being incorrect; it is a preliminary figure replaced by more refined estimates. [confidence: high]

INTERPRETATION ERRORS:
- "NITI Aayog's pharma-sector thematic figure ($35.8bn pharma+API exports) is ~$10.7bn higher than this report's own HS30-only figure ($25,073.4M) because it includes API exports that sit in HS29, not HS30 — consistent with this repo's existing PLI Bulk Drugs finding." — While the explanation correctly notes the difference in coverage (HS29 vs. HS30), it does not address why the discrepancy is framed as a methodological issue rather than a definitional one. The claim implies the report's figure is incomplete or incorrect, but it is simply narrower in scope. The interpretation conflates a definitional boundary (HS chapters) with an error in measurement. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
