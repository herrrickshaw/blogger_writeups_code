# Fact/interpretation check — where-indias-factories-actually-get

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/where-indias-factories-actually-get.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 98905, Requested 5953. Please try again in 1h9m57.312s. Need more tokens? Upgrade to Dev Tier today at htt]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Rs 1,869,333 Rs cr implemented" — The correct figure for implemented industrial projects (Part B) from 2021–Dec 2025 is Rs 19,51,828 cr (as stated later in the article), not Rs 1,869,333 Rs cr. The "Rs cr" unit is redundant and incorrect. [confidence: high]

- "Appendix V is headed 'Up to Dec 2025' while Appendix VI says 'Up to Nov 2025' — yet both grand-total to the identical Rs 5,83,096cr" — The article claims both appendices total Rs 5,83,096 cr despite different timeframes, but this figure does not appear anywhere in the provided text or standard DPIIT reports. The grand total for Part B (2021–Dec 2025) is Rs 19,51,828 cr, not Rs 5,83,096 cr. [confidence: high]

INTERPRETATION ERRORS:
- "Gujarat ... implementing 178% of same-period intent (the pre-2021 pipeline landing)" — The article attributes Gujarat's 178% conversion rate to "pre-2021 pipeline landing," but the conversion percentage is calculated as (Part B implemented / Part A filed) within the same 2021–Dec 2025 window. A 178% conversion implies more was implemented than filed in the same period, which is impossible unless prior-year filings were implemented within the window. The article incorrectly frames this as a pipeline effect without clarifying that the ratio is a same-period flow, not a cohort-matched conversion. [confidence: high]

- "Metallurgical Industries ... overwhelmingly domestic-funded (the same sector whose FDI proxy is amber and whose PLI has disbursed 0.8%)" — The article links high implementation in metallurgical industries to domestic funding and low FDI/PLI disbursal, but the IEM data does not record capital source (domestic vs. foreign). The claim that it is "overwhelmingly domestic-funded" is an unsupported inference extrapolated from the absence of FDI/PLI data in IEM, rather than a verified fact. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
