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

FACTUAL ERRORS:
- "since 2019 (2019-01-02 → 2026-08-04)" — The start date of 2019-01-02 may be incorrect as the Rajya Sabha may not have been in session on this specific date, and the actual start date of the data collection is not verified [confidence: medium]
- "1,825 at this build" — This number may not be verifiable or up-to-date, as the article does not provide a clear source or timestamp for this figure [confidence: low]

INTERPRETATION ERRORS:
- "this split is done by case-sensitive text matching on the question-type field, which is known to miscount a small number of mixed-case rows; treat the exact starred/unstarred split as approximate" — The article acknowledges the potential for miscounting, but does not provide a clear estimate of the error margin or explain how this approximation may impact the conclusions drawn from the data [confidence: medium]
- "All three views are classified by one scheme-keyword map, so they filter identically" — The article assumes that the use of a single scheme-keyword map ensures identical filtering, but does not address potential issues with the map's comprehensiveness or accuracy [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "2026-08-04" — The date is in the future relative to the current date (2025), making it unverifiable or incorrect. [confidence: high]

INTERPRETATION ERRORS:
- "AI-generated text can misstate figures even when working from real source material — verify any number that matters to a decision against the linked answer PDF." — While the caution about AI-generated text is valid, the claim implies that the AI's output is inherently unreliable, which could mislead readers into dismissing the entire dataset without proper context. The statement does not acknowledge that the AI's role was likely limited to synthesis and that the underlying data (from official sources) is verifiable. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
