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
- "Trade value on codes absent nine years earlier" — The article claims that 31.8% of FY2025-26 export value sits on codes that did not exist in FY2017-18, and about 39% on the import side. However, the article later states these figures are from an "independent audit of this dataset carried out for this blog," not directly from the DGCI&S TradeStat EIDB source. Without verification from the primary source, these percentages cannot be confirmed as factual. [confidence: medium]

- "The export series has no FY2021-22" — The article states that the export series lacks data for FY2021-22, but it does not provide a citation or confirmation from the DGCI&S TradeStat EIDB portal. This claim is unverified and could be incorrect. [confidence: low]

INTERPRETATION ERRORS:
- "Renumbering, not trade collapse: HS8 codes churn by a third; HS4 headings barely move." — The article uses the high percentage of trade value on new HS8 codes (31.8% exports, 39% imports) to argue that the churn is due to renumbering rather than trade collapse. However, this interpretation assumes that all new codes are solely due to renumbering and not also due to new products entering trade or shifts in classification. The claim does not account for the possibility that some of the "new" codes could represent genuine new trade flows or reclassifications unrelated to renumbering. [confidence: high]

- "Aggregating 8-digit codes up to the 4-digit HS heading removes almost all the churn" — The article suggests that aggregating to HS4 headings reduces churn to under 1%, implying that HS8-level churn is primarily due to classification changes rather than actual trade dynamics. However, this interpretation may overlook the fact that HS4 headings can also undergo revisions or reclassifications, albeit less frequently. The claim assumes that HS4 headings are static and unaffected by changes, which may not be entirely accurate. [confidence: medium]
