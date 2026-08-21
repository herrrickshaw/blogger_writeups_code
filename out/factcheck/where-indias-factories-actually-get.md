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

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "1,869,333 Rs cr implemented, top 15 states, 2021–Dec 2025" — The article later states "All-India Part B 2021-2025: Rs 19,51,828cr" (Rs 19.52 lakh cr), which is inconsistent with the initial figure of Rs 1,869,333 cr (Rs 18.69 lakh cr). The discrepancy suggests a possible typo or miscalculation in the headline figure. [confidence: high]

- "Rs 4.55 lakh cr in 2024-2025 alone" (Gujarat) — The table shows Gujarat's 2024 and 2025 (to Dec) values as Rs 208,025 cr and Rs 246,595 cr, respectively, totaling Rs 454,620 cr (Rs 4.55 lakh cr). However, the phrasing "2024-2025 alone" could imply a single fiscal year (2024-25), but the data is split into calendar years (2024 and 2025 to Dec). This risks misinterpretation of the timeframe. [confidence: high]

INTERPRETATION ERRORS:
- "Rs 1,22,497cr of the [Glass] 5-yr total sits in a single year (2024) against Rs 1-3,000cr in every other year -- either one mega-project (solar glass?) or a data quirk. Not treated as a trend." — While the article flags this as an anomaly, it does not explain why a single-year spike of Rs 1.22 lakh cr (vs. Rs 1-3k cr in other years) should *not* be treated as a trend. The spike could represent a genuine surge in glass manufacturing (e.g., solar glass capacity addition) or a data reporting issue. The lack of further analysis leaves the reader to assume it is an error without justification. [confidence: medium]

- "Rs 70,117cr of [Fuels] the total is one year (2025) -- likely a single refinery/energy mega-filing." — The article assumes the spike is due to a single project without providing evidence or citing sources. This is speculative and risks misattributing the cause, especially since fuels could include multiple unrelated projects (e.g., LNG terminals, petrochemicals). The claim conflates correlation (a spike in one year) with causation (a single mega-filing) without verification. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
