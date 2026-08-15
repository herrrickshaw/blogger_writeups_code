# Fact/interpretation check — fy2025-26-sample-report-india-trade

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fy2025-26-sample-report-india-trade.html`

## Gemini gemini-flash-latest

[Gemini API error 503: {
  "error": {
    "code": 503,
    "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
    "status": "UNAVAILABLE"
  }
}
]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "GDP growth (real, FAE) +7% First Advance Estimate" — The article later states that this figure has been superseded by MoSPI's Provisional Estimate, but it does not provide the updated figure, making the claim outdated [confidence: medium]
- None found for other factual errors

INTERPRETATION ERRORS:
- "India's blended goods+services trade reached $1.84 trillion in FY2025-26 (exports +4.2%, imports +6.5% y-o-y)" — The article uses this figure to compare with its own goods-only figures, but it does not account for the difference in the growth rates of goods and services exports, which could lead to an incorrect interpretation of the trade data [confidence: medium]
- None found for other interpretation errors

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "GDP growth (real, FAE) +7% First Advance Estimate — MoSPI's Provisional Estimate, released before this snapshot was compiled, has since superseded this figure" — The article incorrectly states that the First Advance Estimate (FAE) has been superseded by MoSPI's Provisional Estimate, but the FAE is the first official estimate released by MoSPI, and the Provisional Estimate is a later revision. The FAE is not superseded; it is the initial estimate that is later refined. [confidence: high]

INTERPRETATION ERRORS:
- "NITI Aayog's blended goods+services trade reached $1.84 trillion in FY2025-26 (exports +4.2%, imports +6.5% y-o-y) — this repo's goods-only figures show export growth of just +0.92% over the same year, explained by services exports growing faster (+9.0% per NITI Aayog) and pulling the blended rate up, not a discrepancy." — While the article correctly notes that services exports grew faster, it implies that the difference in growth rates between goods-only and blended trade is solely due to services exports growing faster. However, this ignores the fact that the blended trade figure includes both goods and services, so the growth rates are not directly comparable without adjusting for the composition of trade. The article does not provide the actual weights of goods and services in the blended trade figure, making the causal claim unsupported. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
