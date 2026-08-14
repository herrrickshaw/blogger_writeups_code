# Fact/interpretation check — lok-sabha-question-registry-1843-scheme

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/lok-sabha-question-registry-1843-scheme.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99419, Requested 1358. Please try again in 11m11.328s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "17th and 18th Lok Sabha (2019-06-17 → 2026-08-04)" — The 17th Lok Sabha's term was from 2019 to 2024, not starting on 2019-06-17. The 18th Lok Sabha's term began in 2024, but the end date of 2026-08-04 is incorrect as it extends beyond the typical 5-year term of a Lok Sabha. [confidence: high]

- "Generated 2026-08-04 by scripts/build_pq_registry.py in digital-twin-for-ipa" — The date 2026-08-04 is in the future relative to the current date (June 2025) and is likely a placeholder or error. [confidence: high]

INTERPRETATION ERRORS:
- "This registry is the parliamentary companion to the Quarterly Reportage: where the reportage tracks what government announced, this tracks what Parliament asked — and the ministry's answer of record." — While the registry tracks parliamentary questions and answers, it does not inherently establish a direct causal or comparative relationship between what the government announced and what Parliament asked. The claim implies a systematic linkage that may not exist in the data. [confidence: medium]

- "AI-generated text can misstate figures even when working from real source material — verify any number that matters to a decision against the linked answer PDF." — The article warns about potential AI errors but does not provide evidence or context for how frequently such errors occur or their potential impact on the registry's accuracy. This is an overgeneralization without supporting data. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
