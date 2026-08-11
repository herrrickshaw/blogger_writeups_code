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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99202, Requested 911. Please try again in 1m37.631999999s. Need more tokens? Upgrade to Dev Tier today at ]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "2019-06-21 → 2026-08-04" — The date range for the 17th Lok Sabha is incorrect. The 17th Lok Sabha was constituted on June 17, 2019, and dissolved on March 16, 2024, not June 21, 2019, or August 4, 2026. The 18th Lok Sabha's term is projected but not yet confirmed to end on August 4, 2026. [confidence: high]

- "Generated 2026-08-04 by scripts/build_pq_registry.py in digital-twin-for-ipa" — The date "2026-08-04" is in the future relative to the current date (2023) and is likely a placeholder or error. The actual generation date should be a past or present date. [confidence: high]

INTERPRETATION ERRORS:
- "Questions are classified by the same scheme-keyword map, so the two views filter identically." — This claim assumes that the classification method used for the Lok Sabha Question Registry is identical to that of the Quarterly Reportage, but the article does not provide evidence or methodology to confirm this equivalence. The claim implies a direct comparability that may not be substantiated. [confidence: medium]

- "Use it to find the answer, then read the answer." — This statement suggests a direct utility of the registry for finding answers, but the article itself notes limitations (e.g., "coverage is of scheme-titled questions, not of every mention"). The claim overstates the registry's comprehensiveness without addressing these constraints. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
