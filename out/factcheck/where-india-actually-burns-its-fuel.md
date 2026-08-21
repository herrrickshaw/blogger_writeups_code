# Fact/interpretation check — where-india-actually-burns-its-fuel

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/where-india-actually-burns-its-fuel.html`

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
- "Delhi’s gas-infrastructure counts (CNG stations and domestic PNG connections, as on 31.05.2026, source PNGRB)" — The date "31.05.2026" is in the future relative to the article's publication date of 8 August 2026, making it an impossible reference date. [confidence: high]

- "FY2024-25 figures are provisional." — While this is likely correct, the article does not provide a source or definition for what "provisional" entails (e.g., whether it refers to preliminary estimates, partial data, or subject to revision). Without verification, this cannot be confirmed as factually accurate. [confidence: medium]

INTERPRETATION ERRORS:
- "Delhi is what the CGD takeover of India’s gas demand looks like from the petrol pump’s side of the ledger." — The article attributes Delhi's slow fuel growth to substitution via CNG, metro, and vehicle-age rules but does not quantify the contribution of each factor or rule out other potential causes (e.g., policy changes, economic shifts, or data anomalies). The causal claim is plausible but not decomposed, making it an overgeneralization. [confidence: high]

- "The increment is two-wheelers and cars, not trucks and tractors — which is why the ethanol-blending programme (petrol-side) keeps gaining policy leverage while diesel-side interventions fade..." — The article links the shift in fuel demand composition to vehicle type (two-wheelers/cars vs. trucks/tractors) without providing data on vehicle sales, fleet composition, or fuel use by vehicle type. The causal inference assumes a direct relationship without supporting evidence. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
