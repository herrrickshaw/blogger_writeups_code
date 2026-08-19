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
- "Published 8 August 2026" — The article claims a publication date of 8 August 2026, but this is impossible as the current date is before that. [confidence: high]

- "Delhi’s gas-infrastructure counts (CNG stations and domestic PNG connections, as on 31.05.2026, source PNGRB)" — The date 31.05.2026 is in the future relative to the publication date (8 August 2026), making this claim unverifiable or incorrect. [confidence: high]

INTERPRETATION ERRORS:
- "Delhi is the finding hiding in the slow column. The capital’s fuel sales grew 22% in sixteen years — a period in which its vehicle stock multiplied. The explanation is substitution, not stagnation: Delhi runs India’s densest gas transport network — 458 CNG station clusters and 19.6 lakh piped-gas connections on PNGRB’s May 2026 count — a metro carrying millions of trips, and the country’s most aggressive vehicle-age rules." — While the claim about Delhi's fuel sales growth and infrastructure is likely correct, the article does not provide evidence or data to quantify the contribution of CNG, metro, or vehicle-age rules to the observed 22% growth in fuel sales. The causal link is asserted without decomposition or statistical backing. [confidence: high]

- "Sixteen years ago India sold 4.6 tonnes of diesel for every tonne of petrol; it now sells 2.3. The increment is two-wheelers and cars, not trucks and tractors — which is why the ethanol-blending programme (petrol-side) keeps gaining policy leverage while diesel-side interventions fade..." — The article correctly notes the shift in the diesel-to-petrol ratio and the growth in petrol demand, but it does not provide evidence to support the causal claim that the rise in two-wheelers and cars (rather than other factors) is the primary driver of this shift. The reasoning assumes a direct link without data on vehicle composition or usage trends. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
