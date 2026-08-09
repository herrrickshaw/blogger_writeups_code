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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99823, Requested 2228. Please try again in 29m32.064s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Rs 4.94L cr CY2024 implemented — the best year on record" — The table shows Rs 4,93,765 cr for 2024, which is approximately Rs 4.94 lakh crore, but the claim that this is "the best year on record" is incorrect because the "Up to Dec 2025" row (a partial-year figure) shows Rs 5,83,096 cr, which is higher. [confidence: high]

- "2019 Part B EXCLUDED — source defect: AR2022-23 prints Gujarat 2019 at Rs 15,18,861cr (~6x all-India)" — The claim that Gujarat's 2019 Part B value was printed at Rs 15,18,861 crore (which is 15.19 lakh crore) is implausible, as it exceeds India's total industrial investment for that year by a wide margin. The correct figure is likely a typographical error (e.g., Rs 15,188.61 crore or similar). [confidence: high]

INTERPRETATION ERRORS:
- "2024 first year IEM implementation > FDI equity inflow" — The claim that 2024 was the first year where IEM implementation (Rs 4,93,765 cr) overtook FDI equity inflow (Rs 4,21,929 cr) is misleading. The article does not provide the FDI equity inflow figure for 2024 specifically; it only compares calendar-year IEM implementation to FY2024-25 FDI equity inflow (a different timeframe). This is an apples-to-oranges comparison, as FDI equity inflow is reported for fiscal years, not calendar years. [confidence: high]

- "Conversion (Part B implemented ÷ same-year Part A filed) is a same-period flow ratio, not a cohort match: this year's Part B often implements filings from 2-3 years earlier" — While the caveat about the pipeline effect is correct, the article later claims that "2024's inflection isn't just a pipeline artefact — the raw implemented value (Rs 4.94L cr) is the highest single year on record, and it happened while the Part A base (Rs 6.02L cr) sat well below 2021's outlier peak (Rs 7.71L cr), meaning most of 2024's Part A filings weren't just filed but built." This interpretation incorrectly assumes that the high conversion rate in 2024 is primarily due to recent filings being implemented, ignoring the possibility that it could still be driven by older backlogs. The reasoning conflates "highest implemented value" with "highest conversion of recent filings," which is not necessarily supported by the same-period flow ratio. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
