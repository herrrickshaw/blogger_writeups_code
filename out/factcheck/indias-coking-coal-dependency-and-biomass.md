# Fact/interpretation check — indias-coking-coal-dependency-and-biomass

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-coking-coal-dependency-and-biomass.html`

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

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "54.17% year-on-year, from 12 MT to just 5.5 MT by December 2025 (down from 35 MT in 2022-23)" — The claim incorrectly states that the 5.5 MT figure is as of December 2025, which is impossible since December 2025 is in the future relative to the article's publication date (the article references FY2024-25 data). The correct timeline should align with past fiscal years. [confidence: high]

- "140 MT Mission Coking Coal's domestic production target for FY2029-30" — While the target is quoted correctly, the article does not clarify that this is a *raw* coking coal production target, not a *washable* or *usable* coking coal target. This distinction is critical because raw coal requires washing to meet metallurgical standards, and the washery capacity target (58 MT by FY2030) suggests a bottleneck in processing. The article conflates raw production with usable output. [confidence: high]

INTERPRETATION ERRORS:
- "Stamp-charging is a coke-making technique that compacts the coal blend before it goes into the oven, which allows a higher proportion of India's own (lower-quality) coking coal to be blended in without compromising coke strength. The Ministry states this raises the domestic-coal share of the blend from roughly 10% to 30% — a real substitution of imported coking coal, achieved through process technology on India's own coal, not through a different material altogether." — The claim implies that stamp-charging directly substitutes imported coking coal by increasing domestic coal usage. However, the article does not provide evidence that the 30% domestic share replaces imported coal on a one-to-one basis. It is possible that the increase in domestic coal usage is additive (i.e., total coking coal usage rises) rather than substitutive (i.e., imports decline proportionally). Without data showing a decline in imports corresponding to the increased domestic share, the causal claim is unsupported. [confidence: high]

- "The SAMARTH mandate isn't the only biomass-co-firing rule in force, and the sourcing for this section turned up something worth flagging rather than smoothing over: there appear to be two related but not fully reconciled compliance tracks, run by different bodies, with different phase-in percentages for the same period." — The article highlights a discrepancy between the national SAMARTH mandate (5% for FY2024-25) and the CAQM Delhi-NCR rule (3% for FY2024-25) but does not explain why this discrepancy exists or whether it reflects overlapping, complementary, or conflicting policies. The lack of reconciliation or context for the discrepancy risks misrepresenting the policy landscape as inconsistent when it may be intentionally tiered (e.g., stricter local rules vs. national standards). [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
