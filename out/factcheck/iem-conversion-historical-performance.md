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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99605, Requested 2009. Please try again in 23m14.496s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Rs 4.94L cr CY2024 implemented — the best year on record" — The article later states that the implemented value for 2024 is Rs 4,93,765 cr (which is Rs 4.94L cr), but the table shows Rs 493,765 cr for 2024 Part B Implemented, which is Rs 4.94L cr. However, the "Up to Dec 2025" row shows Rs 583,096 cr, which is higher than 2024. The claim that 2024 is the best year on record is incorrect because the partial-year 2025 data already exceeds it. [confidence: high]

- "2019 Part B EXCLUDED — source defect: AR2022-23 prints Gujarat 2019 at Rs 15,18,861cr (~6x all-India)" — The article claims Gujarat's 2019 Part B value was printed at Rs 15,18,861 cr in AR2022-23, which is implausibly high (6x the all-India total). However, the table shows no value for 2019 Part B, and the explanation for exclusion is provided. The factual error is in the magnitude of the Gujarat figure (Rs 15,18,861 cr is Rs 15.19 lakh crore, which is indeed ~6x the all-India total for that year, but the source of this figure is not verifiable in the article's context). [confidence: medium]

INTERPRETATION ERRORS:
- "2024 first year IEM implementation > FDI equity inflow" — The article claims that 2024 was the first year where IEM implementation (Rs 4,93,765 cr) overtook FY2024-25 FDI equity inflow (Rs 4,21,929 cr). This is an apples-to-oranges comparison because:
  1. IEM implementation is a calendar-year figure (Jan-Dec 2024), while FDI equity inflow is a fiscal-year figure (Apr 2024-Mar 2025).
  2. The FDI figure is for FY2024-25, which overlaps with but is not identical to the calendar year 2024.
  3. The comparison mixes calendar-year and fiscal-year data without adjustment, making the conclusion unreliable. [confidence: high]

- "Supports a genuine improvement story: the 2024 inflection isn't just a pipeline artefact — the raw implemented value (Rs 4.94L cr) is the highest single year on record, and it happened while the Part A base (Rs 6.02L cr) sat well below 2021's outlier peak (Rs 7.71L cr), meaning most of 2024's Part A filings weren't just filed but built." — The reasoning gap here is that the article conflates "highest implemented value" with "genuine improvement in conversion efficiency." While the implemented value is high, the conversion rate (82%) is still influenced by pipeline effects (earlier years' filings being implemented now). The claim that "most of 2024's Part A filings weren't just filed but built" is not supported by the data because the conversion rate is a same-period flow ratio, not a cohort match. The high implemented value could still be from older filings, not necessarily 2024's filings. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
