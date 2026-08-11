# Fact/interpretation check — iem-conversion-historical-performance

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/iem-conversion-historical-performance.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99886, Requested 2009. Please try again in 27m17.28s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Rs 4.94L cr CY2024 implemented — the best year on record" — The article later states that the implemented value for 2024 is Rs 4,93,765 cr (which is Rs 4.93765L cr), not Rs 4.94L cr. The rounding is incorrect. [confidence: high]

- "2019 Part B EXCLUDED — source defect: AR2022-23 prints Gujarat 2019 at Rs 15,18,861cr (~6x all-India)" — The claim that Gujarat's 2019 Part B value is ~6x all-India is unverifiable without the actual source data. The article does not provide a reliable cross-check or primary source to confirm this ratio. [confidence: medium]

INTERPRETATION ERRORS:
- "2024 first year IEM implementation > FDI equity inflow" — The article claims that 2024 was the first year IEM implementation (Rs 4,93,765cr) overtook FDI equity inflow (Rs 4,21,929cr). However, the comparison is flawed because IEM implementation is measured on a calendar year basis (Jan-Dec 2024), while FDI equity inflow is measured on a fiscal year basis (FY2024-25). These periods do not align, making the comparison apples-to-oranges. [confidence: high]

- "Conversion (Part B implemented ÷ same-year Part A filed) is a same-period flow ratio, not a cohort match: this year's Part B often implements filings from 2-3 years earlier" — While the article correctly notes that conversion is a flow ratio, it then uses this to support the claim that "the 2024 inflection isn't just a pipeline artefact." This is an overreach: the high conversion rate in 2024 could still be driven by older filings landing, not necessarily improved execution. The article conflates the two interpretations without resolving the ambiguity. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
