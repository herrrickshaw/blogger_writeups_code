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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99536, Requested 2009. Please try again in 22m14.88s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Rs 4.94L cr CY2024 implemented — the best year on record" — The article later states that the implemented value for 2024 is Rs 4,93,765 cr (4.94L cr), but the table shows Rs 493,765 cr for 2024, which is 4.94L cr. However, the claim that this is "the best year on record" is incorrect because the "Up to Dec 2025" row shows Rs 583,096 cr (5.83L cr), which is higher. [confidence: high]

- "2024 first year IEM implementation > FDI equity inflow" — The article claims that in 2024, IEM implementation (Rs 4,93,765 cr) overtook FY2024-25 FDI equity inflow (Rs 4,21,929 cr). However, the FDI figure is for a fiscal year (FY2024-25), while the IEM figure is for a calendar year (CY2024). Comparing a calendar year to a fiscal year without adjustment is misleading, as the periods do not align. [confidence: high]

INTERPRETATION ERRORS:
- "Conversion (Part B implemented ÷ same-year Part A filed) is a same-period flow ratio, not a cohort match: this year's Part B often implements filings from 2-3 years earlier, so a high ratio can mean either 'government executing faster' or 'an old backlog finally landing.'" — While the article correctly notes that conversion is a flow ratio and not a cohort match, it then uses the 2024 conversion rate (82.0%) to argue that "the 2024 inflection isn't just a pipeline artefact" and that "most of 2024's Part A filings weren't just filed but built." This is an apples-to-oranges comparison because the 2024 conversion rate includes implementations from earlier years' filings, not just 2024 filings. The conclusion that 2024's execution was stronger is not directly supported by the conversion rate alone. [confidence: high]

- "State-level Part B data ... shows the 2024-2025 jump concentrated in a few states: Gujarat alone implemented Rs 4.55L cr across just 2024-2025, and the top-3 states (Gujarat, Odisha, Maharashtra) account for 63.3% of all 2021-2025 implementation." — The article uses state-level implementation data to argue that the national conversion-rate story is "disproportionately a story about a handful of large industrial states executing faster." However, the conversion rate is a national aggregate, and the state-level data does not directly explain why the national conversion rate improved. The interpretation conflates implementation volume with conversion efficiency, which are distinct metrics. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
