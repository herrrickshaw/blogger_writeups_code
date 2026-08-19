# Fact/interpretation check — indias-coking-coal-import-problem-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-coking-coal-import-problem-and.html`

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
- "54.17% year-on-year, from 12 MT to just 5.5 MT by December 2025 (down from 35 MT in 2022-23)" — The claim incorrectly states "December 2025" when the correct timeframe should be "December 2024" (as the article itself later references FY2024-25 data). The 35 MT figure for 2022-23 is correct, but the December 2025 reference is factually wrong. [confidence: high]

- "140 MT Mission Coking Coal's domestic production target for FY2029-30" — The article cites this figure without clarifying that it is a *target* (not a confirmed production level). While the target is stated in the Ministry of Coal's Year End Review, presenting it as a fact without explicitly labeling it as a target could mislead readers into treating it as a guaranteed outcome. [confidence: medium]

INTERPRETATION ERRORS:
- "Stamp-charging is a coke-making technique that compacts the coal blend before it goes into the oven, which allows a higher proportion of India's own (lower-quality) coking coal to be blended in without compromising coke strength. The Ministry states this raises the domestic-coal share of the blend from roughly 10% to 30% — a real substitution of imported coking coal, achieved through process technology on India's own coal, not through a different material altogether." — While the claim about stamp-charging improving domestic coal usage is correct, the phrasing "a real substitution of imported coking coal" is misleading. The substitution is *within the coking coal blend* (i.e., replacing some imported coking coal with domestically mined coking coal), not a substitution of coking coal itself with another material. The conclusion conflates *source* substitution (domestic vs. imported) with *material* substitution (coking coal vs. biomass). [confidence: high]

- "The SAMARTH mandate isn't the only biomass-co-firing rule in force, and the sourcing for this section turned up something worth flagging rather than smoothing over: there appear to be two related but not fully reconciled compliance tracks, run by different bodies, with different phase-in percentages for the same period." — The article highlights a discrepancy between the national SAMARTH mandate (5% for FY2024-25) and the CAQM Delhi-NCR rule (3% for FY2024-25) but does not explain why this discrepancy exists or whether it reflects overlapping jurisdictions, exemptions, or enforcement priorities. The lack of reconciliation or context leaves readers without clarity on whether this is an oversight, a phased rollout, or a deliberate divergence. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
