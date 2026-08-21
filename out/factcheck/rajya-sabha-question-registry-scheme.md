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
- "Every captured Rajya Sabha question on investment policies, schemes and incentives since 2019 (2019-01-02 → 2026-08-13) — 1,883 at this build" — The date range includes future dates (2026-08-13), which is impossible for a dataset capturing past questions. The end date should not exceed the current date (as of the article's publication in 2026, the latest possible date would be 2026-08-12 or earlier). [confidence: high]

INTERPRETATION ERRORS:
- "AI-generated text can misstate figures even when working from real source material — verify any number that matters to a decision against the linked answer PDF." — While the article correctly acknowledges the potential for AI hallucinations, it does not address how the AI might have misinterpreted or misclassified the data (e.g., scheme-keyword mapping errors, double-counting, or incorrect causal inferences from the data). The warning is too generic and does not explain the specific risks of misinterpretation in the context of the dataset's methodology. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
