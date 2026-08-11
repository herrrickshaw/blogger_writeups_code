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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99062, Requested 2278. Please try again in 19m17.76s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026" — The date is impossible as the article references data up to FY2024-25 (ending March 2025) and cites sources dated May 2026 (e.g., PNGRB's count). The publication date is likely a typo or hallucination. [confidence: high]

- "Delhi’s gas-infrastructure counts (CNG stations and domestic PNG connections, as on 31.05.2026, source PNGRB)" — The PNGRB data is cited as of May 2026, but the article claims these figures are used in the analysis. However, the analysis covers FY2008-09 to FY2024-25, and the May 2026 data would not be available for the entire period. The use of future-dated data for historical analysis is incorrect. [confidence: high]

INTERPRETATION ERRORS:
- "Delhi is exactly what its gas and metro build-out was meant to achieve" — The article attributes Delhi's slow fuel growth to its CNG, metro, and vehicle-age policies, but it does not quantify the contribution of these factors. The causal claim is asserted without decomposition or evidence, making it an unsupported interpretation. [confidence: high]

- "The frontier moved east to Odisha and Chhattisgarh — and the slowest-growing fuel market in India is Delhi" — While the growth rates are correctly stated, the framing implies a causal or structural shift (e.g., "frontier") without explaining why these states (Odisha, Chhattisgarh) are leading growth. The interpretation conflates correlation (growth rates) with causation (e.g., industrialization, motorization) without clarifying the underlying drivers. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
