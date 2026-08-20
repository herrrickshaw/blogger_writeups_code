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
- "54.17% year-on-year, from 12 MT to just 5.5 MT by December 2025 (down from 35 MT in 2022-23)" — The claim incorrectly states "December 2025" when the article text refers to "December 2024" in the context of FY2024-25 data. [confidence: high]

INTERPRETATION ERRORS:
- "Stamp-charging is a coke-making technique that compacts the coal blend before it goes into the oven, which allows a higher proportion of India's own (lower-quality) coking coal to be blended in without compromising coke strength. The Ministry states this raises the domestic-coal share of the blend from roughly 10% to 30% — a real substitution of imported coking coal, achieved through process technology on India's own coal, not through a different material altogether." — The claim implies that stamp-charging directly substitutes imported coking coal by increasing domestic coal usage, but it does not account for the fact that the domestic coal being used is still coking coal (albeit lower-grade), not a replacement material. The substitution is within the same material category (coking coal), not a replacement of imported coking coal with a different input. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
