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
- "Every captured Rajya Sabha question on investment policies, schemes and incentives since 2019 (2019-01-02 → 2026-08-13) — 1,883 at this build" — The date range includes future dates (e.g., 2026-08-13), which is impossible for a dataset capturing past questions. The claim is unverifiable as stated. [confidence: high]

- "Generated 2026-08-19 by scripts/build_rs_pq_registry.py in digital-twin-for-ipa." — The generation date is in the future (2026-08-19), which is not possible for a published article. [confidence: high]

INTERPRETATION ERRORS:
- "The index matches keywords against the subject line only, so a question whose subject names no scheme is not captured even when its answer discusses one at length — coverage is of scheme-titled questions, not of every mention." — While the limitation is correctly stated, the phrasing implies that the dataset is intentionally limited to scheme-titled questions, which may mislead readers into thinking it captures all relevant parliamentary discussions on schemes. The interpretation could be read as a broader claim about the dataset's comprehensiveness than is justified. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
