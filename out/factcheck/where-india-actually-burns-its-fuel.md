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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99600, Requested 2278. Please try again in 27m2.592s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026" — The date is impossible as the article references data up to FY2024-25 (ending March 2025) and cites sources from August 2026 (e.g., PNGRB's May 2026 count). The publication date is likely a typo or hallucination. [confidence: high]

- "Delhi’s gas transport network — 458 CNG station clusters and 19.6 lakh piped-gas connections on PNGRB’s May 2026 count" — While the PNGRB data is cited, the term "gas transport network" is misleading; CNG stations and piped-gas connections are part of the city gas distribution (CGD) network, not a "transport network." The phrasing conflates infrastructure types. [confidence: medium]

INTERPRETATION ERRORS:
- "Delhi is exactly what its gas and metro build-out was meant to achieve" — The article attributes Delhi's slow fuel growth to its CNG/metro infrastructure but does not quantify the contribution of these factors. The claim implies causation without decomposition (e.g., how much of the 22% growth is due to substitution vs. other factors like vehicle efficiency or policy). [confidence: high]

- "The increment is two-wheelers and cars, not trucks and tractors — which is why the ethanol-blending programme (petrol-side) keeps gaining policy leverage while diesel-side interventions fade" — While petrol demand grew faster, the article does not provide evidence linking this growth *directly* to ethanol blending or policy leverage. The causal chain assumes that policy interventions drove demand shifts without isolating their impact from other factors (e.g., economic growth, urbanization, fuel price differentials). [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
