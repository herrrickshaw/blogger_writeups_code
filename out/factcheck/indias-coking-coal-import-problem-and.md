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
- "54.17% year-on-year, from 12 MT to just 5.5 MT by December 2025 (down from 35 MT in 2022-23)" — The claim incorrectly states "December 2025" when the correct period should be "December 2024" (as the article itself later refers to FY2024-25 data). The 5.5 MT figure is for December 2024, not 2025. [confidence: high]

- "₹60,681.67 crore" — The article cites this foreign exchange savings figure without a clear source or methodology for the calculation. While the Ministry of Coal's Year End Review may provide the 7.9% import decline, the conversion to ₹60,681.67 crore (assuming a specific exchange rate and coal price) is not explicitly sourced or verified in the article. [confidence: medium]

INTERPRETATION ERRORS:
- "Stamp-charging is a coke-making technique that compacts the coal blend before it goes into the oven, which allows a higher proportion of India's own (lower-quality) coking coal to be blended in without compromising coke strength. The Ministry states this raises the domestic-coal share of the blend from roughly 10% to 30% — a real substitution of imported coking coal, achieved through process technology on India's own coal, not through a different material altogether." — The claim implies that stamp-charging directly substitutes imported coking coal by increasing domestic coal usage. However, the article does not provide evidence that the domestic coal share increase (from 10% to 30%) directly reduces import dependence proportionally. The 30% domestic share could still include a mix of higher-quality imported coking coal and lower-quality domestic coal, meaning the net import reduction may be smaller than suggested. [confidence: high]

- "The SAMARTH mandate isn't the only biomass-co-firing rule in force, and the sourcing for this section turned up something worth flagging rather than smoothing over: there appear to be two related but not fully reconciled compliance tracks, run by different bodies, with different phase-in percentages for the same period." — While the article correctly notes the discrepancy between the 3% (CAQM) and 5% (SAMARTH) biomass co-firing mandates for FY2024-25, it does not explain why this inconsistency exists or whether it reflects overlapping but distinct policy goals (e.g., air quality vs. stubble burning). The article presents the discrepancy as a fact without clarifying the underlying rationale or implications for enforcement, leaving the reader without context for why two different mandates apply. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
