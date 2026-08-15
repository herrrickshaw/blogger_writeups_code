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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99809, Requested 2324. Please try again in 30m42.911999999s. Need more tokens? Upgrade to Dev Tier today a]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026 · v1.0.0" — The article claims a publication date of 8 August 2026, which is in the future relative to the current date (June 2025). This is likely an error in the versioning or metadata. [confidence: high]

- "Delhi’s gas-infrastructure counts (CNG stations and domestic PNG connections, as on 31.05.2026, source PNGRB)" — The date 31.05.2026 is in the future and cannot be verified as of June 2025. [confidence: high]

INTERPRETATION ERRORS:
- "Delhi is the finding hiding in the slow column. The capital’s fuel sales grew 22% in sixteen years — a period in which its vehicle stock multiplied. The explanation is substitution, not stagnation: Delhi runs India’s densest gas transport network — 458 CNG station clusters and 19.6 lakh piped-gas connections on PNGRB’s May 2026 count — a metro carrying millions of trips, and the country’s most aggressive vehicle-age rules." — While the claim about Delhi's fuel sales growth being low is correct, the interpretation that substitution (via CNG, metro, and vehicle rules) is the sole or primary explanation is not established by the data presented. The article does not decompose the contributions of these factors or rule out other explanations (e.g., changes in commuting patterns, remote work, or economic activity). The reasoning gap is that correlation is presented as causation without sufficient evidence. [confidence: high]

- "The frontier moved east; the plateau is in the north-west" — The claim that the "frontier" (fastest-growing fuel markets) moved east is supported by the data (e.g., Odisha, Chhattisgarh), but the characterization of the "plateau" as being in the north-west is an overgeneralization. The data shows that some north-western states (e.g., Haryana, Rajasthan) had moderate growth, while others (e.g., Punjab) had very low growth. The "plateau" label is not uniformly accurate for the entire region, and the reasoning gap is that the conclusion oversimplifies regional variations. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
