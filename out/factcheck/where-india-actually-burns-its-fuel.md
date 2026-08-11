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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99853, Requested 2278. Please try again in 30m41.184s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026" — The date is impossible as the article references data up to FY2024-25 (ending March 2025) and cites sources dated August 2026, which is a logical inconsistency. [confidence: high]

- "Delhi’s gas-infrastructure counts (CNG stations and domestic PNG connections, as on 31.05.2026, source PNGRB)" — The date 31.05.2026 is in the future relative to the article's publication context and the data cutoff (FY2024-25). [confidence: high]

INTERPRETATION ERRORS:
- "Delhi is exactly what its gas and metro build-out was meant to achieve" — The article attributes Delhi's slow fuel growth to substitution via CNG, metro, and vehicle-age rules but does not quantify or decompose the contributions of these factors. The causal claim is plausible but unsupported by the data presented. [confidence: high]

- "The frontier moved east; the plateau is in the north-west" — While the article correctly identifies Odisha and Chhattisgarh as fast-growing markets, the claim that the "plateau is in the north-west" is an overgeneralization. Punjab (+23%) and Rajasthan (+49%) are in the north-west but show different growth patterns, and Maharashtra (+46%) is in the west but not a "plateau." The interpretation lacks nuance and conflates regional trends. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
