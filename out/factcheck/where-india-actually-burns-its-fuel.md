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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99147, Requested 2278. Please try again in 20m31.2s. Need more tokens? Upgrade to Dev Tier today at https:]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026" — The publication date is impossible as the article references data up to FY2024-25 (ending March 2024) and future projections (FY2024-25 is not yet complete as of August 2026). The PPAC workbook is likely dated August 2025, not 2026. [confidence: high]

- "Delhi’s gas-infrastructure counts (CNG stations and domestic PNG connections, as on 31.05.2026)" — The date is impossible as the article was published before May 2026 (per the "Published 8 August 2026" claim). The PNGRB data would not be available for a future date. [confidence: high]

INTERPRETATION ERRORS:
- "Delhi is exactly what its gas and metro build-out was meant to achieve" — The article attributes Delhi's slow fuel growth to CNG, metro expansion, and vehicle-age rules, but does not provide quantified evidence or decomposition to support this causal claim. The correlation is asserted without isolating the contribution of these factors. [confidence: high]

- "The increment is two-wheelers and cars, not trucks and tractors — which is why the ethanol-blending programme (petrol-side) keeps gaining policy leverage while diesel-side interventions fade" — While the shift toward petrol demand is noted, the article does not provide data or analysis to directly link this shift to the ethanol-blending program or to demonstrate that diesel-side interventions have "faded" in relevance. This is an unsupported causal extrapolation. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
