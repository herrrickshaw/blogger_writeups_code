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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99526, Requested 2009. Please try again in 22m6.24s. Need more tokens? Upgrade to Dev Tier today at https:]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "2024 first year IEM implementation > FDI equity inflow" — The article claims that 2024 was the first year IEM implementation (Rs 4,93,765 cr) overtook FDI equity inflow (Rs 4,21,929 cr), but this comparison mixes calendar-year IEM data with fiscal-year FDI data (FY2024-25). The periods are not identical, making the claim unverifiable as stated. [confidence: high]

- "Rs 4.94L cr CY2024 implemented — the best year on record" — The article cites Rs 4.94 lakh crore as the implemented value for CY2024, but the table shows Rs 4,93,765 crore (Rs 4.93765 lakh crore), which is not rounded to Rs 4.94 lakh crore. The discrepancy suggests a rounding error or misstatement. [confidence: high]

INTERPRETATION ERRORS:
- "This is the year IEM implementation (Rs 4,93,765cr, CY2024 as reconciled in the Dec-2025 Annual Report vintage) overtook FY2024-25 FDI equity inflow (Rs 4,21,929cr) for the first time — domestic industrial capex outpacing foreign investment as a growth engine" — The claim implies a causal relationship between IEM implementation and domestic industrial capex outpacing foreign investment, but the comparison is flawed because:
  1. IEM implementation includes both domestic and foreign investments (as it is a record of investment intent filings, not a source-of-funds breakdown).
  2. FDI equity inflow is only one component of foreign investment and does not account for other forms of foreign capital (e.g., FDI reinvested earnings, foreign portfolio investment in manufacturing).
  Thus, the conclusion that domestic industrial capex outpaced foreign investment is not supported by the data presented. [confidence: high]

- "Supports a genuine improvement story: the 2024 inflection isn't just a pipeline artefact — the raw implemented value (Rs 4.94L cr) is the highest single year on record, and it happened while the Part A base (Rs 6.02L cr) sat well below 2021's outlier peak (Rs 7.71L cr), meaning most of 2024's Part A filings weren't just filed but built." — The article argues that the high conversion rate in 2024 reflects genuine improvement because the implemented value was high despite a lower Part A base. However, this ignores the pipeline effect: Part B in 2024 could still be implementing filings from 2021-2022 (as acknowledged earlier), meaning the high conversion rate may partly reflect the landing of older backlogs rather than solely improved execution. The conclusion conflates the timing of implementation with the efficiency of execution. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
