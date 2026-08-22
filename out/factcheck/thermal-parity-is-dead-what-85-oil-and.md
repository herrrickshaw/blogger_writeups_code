# Fact/interpretation check — thermal-parity-is-dead-what-85-oil-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/thermal-parity-is-dead-what-85-oil-and.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026 · v1.0.0" — The date is in the future relative to the current date (2025), making it unverifiable and likely incorrect. [confidence: high]

- "5.55 MMBtu of energy in one barrel of crude — the thermal-parity anchor" — While the article cites Mittal (2016) for this conversion, the standard conversion is approximately 5.8 MMBtu per barrel of crude oil (based on API gravity and energy content). The 5.55 figure may be an outdated or region-specific estimate. [confidence: medium]

INTERPRETATION ERRORS:
- "India’s notified APM gas ceiling, $7.86 India’s notified APM gas ceiling, $/MMBtu, against $85 crude" — The claim that the $7.86 gas price is "against $85 crude" implies a direct causal link where the gas price is derived from the crude price via the 10% formula. However, the article later notes that the notified price is below the raw formula output ($8.4–8.5/MMBtu), indicating a policy choice (ceiling) is constraining the pass-through. The framing oversimplifies the relationship by ignoring the ceiling's role in decoupling the price from crude. [confidence: high]

- "The 2015 cointegration study’s empirical finding is the after-the-fact confirmation of what the 2006 review predicted was possible." — The article conflates correlation with causation. The 2006 review predicted a *mechanism* (fuel-switching) that could weaken the oil-gas link, but the 2015 study only confirmed a *statistical break* in cointegration. The claim implies the review's mechanism *caused* the decoupling, which is not supported by the evidence presented. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
