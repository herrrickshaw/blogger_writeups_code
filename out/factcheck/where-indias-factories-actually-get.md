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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99532, Requested 5956. Please try again in 1h19m1.632s. Need more tokens? Upgrade to Dev Tier today at htt]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "1,869,333 Rs cr implemented, top 15 states, 2021–Dec 2025" — The article later states the all-India Part B total as Rs 19,51,828 cr (1.95 lakh crore), which is significantly lower than 1.86 lakh crore. The figure appears to be a misplaced comma or formatting error (likely meant to be 1,95,1828 cr or similar). [confidence: high]

- "Rs 4.55 lakh cr in 2024-2025 alone" (Gujarat) — The table shows Gujarat's 2024 and 2025 (to Dec) values as 208,025 cr and 246,595 cr respectively, totaling ~454,620 cr (Rs 4.55 lakh cr). However, the article claims this is "2024-2025 alone," which is ambiguous (could imply FY2024-25 or CY2024-25). If FY2024-25, the data does not align with standard fiscal year definitions (April 2024–March 2025), as the 2025 column is only "to Dec 2025." [confidence: medium]

INTERPRETATION ERRORS:
- "Rs 1,22,497cr of the 5-yr total [for Glass] sits in a single year (2024) against Rs 1-3,000cr in every other year -- either one mega-project (solar glass?) or a data quirk. Not treated as a trend." — While the anomaly is correctly flagged, the article does not explain why this single-year spike should *not* be treated as a trend, especially given the context of solar glass manufacturing expansion in India. The spike could reflect a real industrial trend (e.g., PLI-driven solar glass capacity addition) rather than a data error. The dismissal as a "quirk" without further analysis is an overreach. [confidence: high]

- "Rs 70,117cr of the [Fuels] total is one year (2025) -- likely a single refinery/energy mega-filing." — The article assumes a single project caused the spike without providing evidence or acknowledging that large energy projects (e.g., refinery expansions or LNG terminals) are often filed as single IEMs. The claim implies causation (a single filing) without ruling out alternative explanations (e.g., multiple smaller projects aggregating to the total). [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
