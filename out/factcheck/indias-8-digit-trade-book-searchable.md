# Fact/interpretation check — indias-8-digit-trade-book-searchable

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-8-digit-trade-book-searchable.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

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
- "Trade value on codes absent nine years earlier" — The chart title claims to show "Share of FY2025-26 value on 8-digit codes that did not exist in FY2017-18," but the article text later states "31.8 per cent of 2025-26 export value sits on codes that did not exist in 2017-18" and "about 39 per cent on the import side." The chart's 31.8% (exports) and ~39% (imports) values are inconsistent with the chart's own title, which incorrectly states "nine years earlier" (FY2017-18 is 8 years before FY2025-26, not 9). [confidence: high]

- "The export series has no FY2021-22" — The article claims the export series lacks FY2021-22 data, but the DGCI&S TradeStat EIDB portal (the cited source) typically includes all fiscal years in its commodity-wise reports. The absence of FY2021-22 is likely a data-processing error or omission in the dashboard, not a source limitation. [confidence: high]

INTERPRETATION ERRORS:
- "Renumbering, not trade collapse: HS8 codes churn by a third; HS4 headings barely move." — While the churn percentages (31.8% exports, 39% imports) are correctly calculated for HS8 codes, the conclusion that this "barely moves" at HS4 level is misleading. The article aggregates HS8 codes to HS4 headings to show reduced churn, but this aggregation masks the fact that HS4 headings themselves may undergo reclassifications or splits that are not captured by simple aggregation. The claim implies HS4 headings are static, which is not necessarily true. [confidence: medium]

- "Aggregating 8-digit codes up to the 4-digit HS heading removes almost all the churn" — The article presents this as a definitive solution to HS8 churn, but it does not account for cases where HS4 headings are themselves redefined or split over time (e.g., due to HS nomenclature updates). The reduction in churn at HS4 level may partly reflect these redefinitions rather than true stability, and the claim overgeneralizes the effectiveness of aggregation. [confidence: medium]
