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

FACTUAL ERRORS:
- "GDP growth (real, FAE) +7% First Advance Estimate" — The article states that this figure has been superseded by MoSPI's Provisional Estimate, but it does not provide the updated figure, making the claim outdated [confidence: medium]
- "Forex reserves (MoSPI connector) | 698,100.0 | 2025-06 | 13 months stale" — The article itself states that this figure is 13 months stale and should not be used as the current reserve, instead, it should be 675,157.0 [confidence: high]

INTERPRETATION ERRORS:
- "Imports and PIB's export/deficit figures agree with TRADESTAT to within rounding. TIA Portal's export total alone reads ~US$9,300M (2.1%) higher than both other sources" — The article attributes the difference to a data-vintage/provisional-revision difference, but it does not consider the possibility of a methodology error, which could lead to incorrect conclusions [confidence: medium]
- "NITI Aayog's pharma-sector thematic figure ($35.8bn pharma+API exports) is ~$10.7bn higher than this report's own HS30-only figure ($25,073.4M) because it includes API exports that sit in HS29, not HS30" — The article assumes that the difference is due to the inclusion of API exports in HS29, but it does not provide evidence to support this claim, and other factors could contribute to the discrepancy [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "GDP growth (real, FAE) +7% First Advance Estimate — MoSPI's Provisional Estimate, released before this snapshot was compiled, has since superseded this figure" — The claim implies the FAE figure was superseded by a Provisional Estimate, but the Provisional Estimate is typically released *after* the FAE. The FAE is the first estimate, followed by the Provisional Estimate, so the FAE is not "superseded" in a way that invalidates it as a historical record. [confidence: high]

INTERPRETATION ERRORS:
- "NITI Aayog's pharma-sector thematic figure ($35.8bn pharma+API exports) is ~$10.7bn higher than this report's own HS30-only figure ($25,073.4M) because it includes API exports that sit in HS29, not HS30 — consistent with this repo's existing PLI Bulk Drugs finding." — While the explanation of the discrepancy (HS29 vs. HS30) is correct, the phrasing suggests this is a *finding* of the repo, when in fact it is merely restating the reason for the difference provided by NITI Aayog. The repo does not independently verify or analyze the $35.8bn figure; it merely notes the definitional difference. This risks implying an unwarranted conclusion about the accuracy or completeness of the figures. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
