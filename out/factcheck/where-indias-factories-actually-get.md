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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99798, Requested 6277. Please try again in 1h27m28.8s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "1,869,333 Rs cr implemented, top 15 states, 2021–Dec 2025" — The correct figure for all-India Part B implementation (2021–Dec 2025) is Rs 19,51,828 cr (as stated later in the article), not Rs 1,869,333 cr. The latter number appears to be a misformatted or incorrect total. [confidence: high]

- "Rs 4.55 lakh cr in 2024-2025 alone" (Gujarat) — The Gujarat 2025 column shows Rs 246,595 cr, not Rs 4.55 lakh cr (which would be Rs 455,000 cr). This is a clear numerical error in the state's 2025 implementation figure. [confidence: high]

INTERPRETATION ERRORS:
- "Gujarat ... implementing 178% of same-period intent (the pre-2021 pipeline landing)" — The article claims Gujarat's 178% conversion rate is due to a "pre-2021 pipeline landing," but the conversion percentage is calculated as (Part B / Part A) within the same period (2021–Dec 2025). A 178% conversion implies more implementation than intent filed in the same window, which is impossible unless pre-2021 filings are included. The article acknowledges this in the caveat ("Part A/B are period flows; A-B over the window approximates the unconverted backlog but is not a clean stock"), but still uses the 178% figure as evidence of a pipeline effect without clarifying that the ratio is not cohort-matched. This misrepresents the meaning of the conversion rate. [confidence: high]

- "The 2023 Rs 18,778cr registers in IEM well before the Tata Electronics Assam OSAT plant's Feb–Mar 2024 approval, so it is unlikely to be that specific project — more likely earlier-stage electronics capex in the same broader investment wave" — While the timing discrepancy is noted, the article implies that the Rs 18,778cr in Assam's 2023 IEM data is unrelated to the Tata Electronics project because the project was approved later. However, large industrial projects often file IEMs (Part A) years before implementation (Part B), and the Rs 18,778cr could plausibly represent the Tata project's pre-approval filing. The article dismisses this possibility without evidence, suggesting an unwarranted causal inference that the IEM figure is unrelated to the Tata project. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
