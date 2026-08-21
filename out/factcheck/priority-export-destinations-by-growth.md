# Fact/interpretation check — priority-export-destinations-by-growth

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/priority-export-destinations-by-growth.html`

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
- "The USA takes 11 of India's 12 fastest-growing export chapters." — This claim is unverifiable as stated because the article does not provide the list of the 12 fastest-growing export chapters or their growth metrics. Without this, the claim cannot be fact-checked against TRADESTAT data. [confidence: medium]

- "India's total exports to the US were $87.31bn in FY2025-26 per IBEF/commerce data" — The source for this figure (IBEF/commerce data) is not directly linked or cited in the article, and IBEF is not a primary government data source like TRADESTAT. The claim lacks a clear, verifiable government source. [confidence: high]

INTERPRETATION ERRORS:
- "The USA is the top-8 destination in 11 of the 12 fastest-growing export chapters, ranking #1 or #2 in 9 of them — $63.9bn combined across just these tracked chapters" — The claim conflates "top-8 destination" with "top-1 or top-2 destination," which are not equivalent. Being a top-8 destination does not imply being in the top-2, and the article does not clarify whether the $63.9bn figure is for top-8 or top-2 rankings. This creates a false equivalence in the ranking logic. [confidence: high]

- "PLI Bulk Drugs ... generating ₹1,962 crore in sales (₹479 crore of it exports) and avoiding an estimated ₹1,483 crore in imports — explicitly aimed at cutting India's roughly 70% dependence on Chinese bulk-drug imports." — The claim that the PLI Bulk Drugs scheme is "explicitly aimed at cutting India's roughly 70% dependence on Chinese bulk-drug imports" is an extrapolation beyond the data provided. The article does not cite any official policy document or TRADESTAT data to support this causal link between the PLI scheme's sales/export figures and the reduction of import dependence. The avoidance of imports is a stated goal, but the article does not provide evidence that the scheme has achieved this outcome. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
