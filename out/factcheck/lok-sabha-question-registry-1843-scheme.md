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

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "its regional-connectivity viability-gap funding accounts for 273 of the 1,890 Lok Sabha questions captured here" — The claim states that 273 out of 1,890 questions pertain to UDAN/RCS, but the article does not provide a verifiable source or methodology to confirm this exact number. The registry's methodology is described, but the specific count is not directly linked to an official or independently verifiable dataset. [confidence: medium]

- "Generated 2026-08-19 by scripts/build_pq_registry.py in digital-twin-for-ipa" — The date "2026-08-19" is in the future relative to the current date (2023), making this claim factually impossible. [confidence: high]

INTERPRETATION ERRORS:
- "Questions are classified by the same scheme-keyword map, so the two views filter identically." — While the classification method is described, this claim implies a perfect alignment between the registry's classification and the Quarterly Reportage, which may not account for potential inconsistencies in keyword matching or acronym handling (e.g., "Sanchar Mitra" not filing under PM MITRA). The assumption that identical filtering ensures identical classification accuracy is an overgeneralization. [confidence: medium]

- "Use it to find the answer, then read the answer." — This claim suggests a direct utility of the registry for locating answers, but it does not address potential limitations, such as questions where the subject line does not mention the scheme but the answer discusses it (as acknowledged in the "Known limits" section). The recommendation oversimplifies the registry's practical use. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
