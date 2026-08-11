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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99804, Requested 2383. Please try again in 31m29.568s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "2024 first year IEM implementation > FDI equity inflow" — The claim is incorrect because the article itself notes that the comparison is between calendar-year IEM implementation (Rs 4,93,765cr) and fiscal-year FDI equity inflow (Rs 4,21,929cr), which are not directly comparable due to differing time periods. The statement implies a direct comparison without acknowledging this methodological mismatch. [confidence: high]

- "Rs 4.94L cr CY2024 implemented — the best year on record" — The article does not provide a verifiable source or context for this claim beyond the DPIIT Annual Reports. While the figure is cited, the absence of a clear baseline comparison (e.g., historical range, methodology for "best year") makes it difficult to assess its factual accuracy without cross-referencing the primary source. [confidence: medium]

INTERPRETATION ERRORS:
- "Conversion (Part B implemented ÷ same-year Part A filed) is a same-period flow ratio, not a cohort match: this year's Part B often implements filings from 2-3 years earlier, so a high ratio can mean either 'government executing faster' or 'an old backlog finally landing.'" — While the caveat about the ratio being a flow measure is correct, the article then uses the 2024 conversion rate (82.0%) to argue that "the 2024 inflection isn't just a pipeline artefact" and that it reflects genuine improvement. This is an interpretation error because the high conversion rate could still be driven by the landing of older backlogs (e.g., 2021-22 filings) rather than faster execution of recent filings. The article does not disentangle these effects to justify the conclusion. [confidence: high]

- "State-level Part B data [...] shows the 2024-2025 jump concentrated in a few states: Gujarat alone implemented Rs 4.55L cr across just 2024-2025, and the top-3 states (Gujarat, Odisha, Maharashtra) account for 63.3% of all 2021-2025 implementation." — The article correctly reports the state-level concentration but then implies that this disproportionality undermines the national conversion-rate story. This is an apples-to-oranges comparison because the conversion rate is a national aggregate, while the state-level data highlights distribution. The interpretation error lies in conflating national performance with state-level disparities without explaining how the latter invalidates the former. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
