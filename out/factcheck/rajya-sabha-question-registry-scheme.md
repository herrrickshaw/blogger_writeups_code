# Fact/interpretation check — rajya-sabha-question-registry-scheme

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/rajya-sabha-question-registry-scheme.html`

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
- "Every captured Rajya Sabha question on investment policies, schemes and incentives since 2019 (2019-01-02 → 2026-08-13) — 1,883 at this build" — The date range includes future dates (2026-08-13), which is impossible for captured questions. The count of 1,883 is likely incorrect or unverifiable as of the publication date (19 August 2026). [confidence: high]

- "Generated 2026-08-19 by scripts/build_rs_pq_registry.py in digital-twin-for-ipa" — The generation date (2026-08-19) is after the article's publication date (19 August 2026), which is logically inconsistent. [confidence: high]

INTERPRETATION ERRORS:
- "AI-generated text can misstate figures even when working from real source material — verify any number that matters to a decision against the linked answer PDF." — While the caution about AI-generated text is valid, the article itself is presented as a synthesis aid, not a primary source. The phrasing could mislead readers into treating the article as authoritative rather than a secondary interpretation of the data. [confidence: medium]

- "Ministries answer as of their date; figures in older answers are superseded by newer ones." — This statement is factually correct but implies a causal relationship (older answers are automatically invalidated by newer ones) without clarifying that users must actively cross-reference answers or that the registry does not automatically update or flag superseded data. The interpretation oversimplifies the need for manual verification. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
