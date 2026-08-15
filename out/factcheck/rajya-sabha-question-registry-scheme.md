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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99058, Requested 1357. Please try again in 5m58.56s. Need more tokens? Upgrade to Dev Tier today at https:]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "2019-01-02 → 2026-08-04" — The date range is incorrect because the article was published on 4 August 2026, and the end date (2026-08-04) matches the publication date, implying the data only includes questions up to the publication date. However, the claim suggests the data covers questions *since* 2019, which is technically correct, but the phrasing "2019-01-02 → 2026-08-04" implies a continuous range including the exact start and end dates, which may mislead readers into thinking the data includes questions from 2 January 2019 onward (which is not standard for "since 2019"). [confidence: high]

INTERPRETATION ERRORS:
- "The index matches keywords against the subject line only, so a question whose subject names no scheme is not captured even when its answer discusses one at length — coverage is of scheme-titled questions, not of every mention." — While this is a stated limitation, the article does not clarify whether this approach introduces a systematic bias in the analysis. For example, if ministries frequently discuss schemes in answers to questions that do not explicitly name the scheme in the subject line, the dataset may underrepresent certain schemes or ministries, leading to an incomplete or skewed interpretation of parliamentary interest or government response. The article acknowledges the limitation but does not address its potential impact on conclusions drawn from the data. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
