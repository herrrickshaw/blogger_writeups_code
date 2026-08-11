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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99844, Requested 5907. Please try again in 1h22m48.864s. Need more tokens? Upgrade to Dev Tier today at ht]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Rs 1,869,333 Rs cr implemented" — The correct figure for implemented industrial projects (Part B) from 2021–Dec 2025 is Rs 19,51,828 cr (as stated later in the article), not Rs 1,869,333 Rs cr. The notation is also inconsistent (mixing "Rs cr" with "Rs"). [confidence: high]

- "Appendix V is headed 'Up to Dec 2025' while Appendix VI says 'Up to Nov 2025' -- yet both grand-total to the identical Rs 5,83,096cr" — The article claims both appendices total Rs 5,83,096 cr despite different time labels, but the grand total for Part B implementation in the article is Rs 19,51,828 cr (5-year total). The Rs 5,83,096 cr figure appears to be a misstatement or misattribution (possibly from a different dataset or timeframe). [confidence: high]

INTERPRETATION ERRORS:
- "Gujarat ... implementing 178% of same-period intent (the pre-2021 pipeline landing)" — The article attributes Gujarat's 178% conversion rate to pre-2021 pipeline projects landing in 2021–2025, but the conversion percentage is calculated as (Part B implemented / Part A filed) within the same period (2021–2025). This is a flow ratio, not a cohort-matched analysis, meaning it does not account for projects filed before 2021. The claim implies a causal link between "pre-2021 pipeline" and the high conversion rate, but the data only shows that Gujarat implemented more in the period than it filed, which could reflect either pre-existing backlogs or new filings. [confidence: high]

- "Metallurgical Industries ... overwhelmingly domestic-funded (the same sector whose FDI proxy is amber and whose PLI has disbursed 0.8%)" — The article uses the low disbursal of PLI (0.8%) for metallurgical industries to argue that the sector is "overwhelmingly domestic-funded," but PLI disbursal is not a direct proxy for funding sources (domestic vs. foreign). The PLI scheme could be underutilized for other reasons (e.g., bureaucratic delays, eligibility criteria), and FDI data may not capture all foreign investment in the sector. The conclusion conflates funding sources with policy uptake. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
