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
- "The USA takes 11 of India's 12 fastest-growing export chapters." — This claim is unverifiable as stated because the article does not provide the list of the 12 fastest-growing export chapters or their growth rates. Without this list, the claim cannot be fact-checked against TRADESTAT data. [confidence: medium]

- "The PLI Scheme for Textiles (₹10,683 crore, notified September 2021; 91 companies selected as of September 2025, ₹7,731 crore invested, but only ₹733 crore of exports reported so far)" — The claim that "only ₹733 crore of exports reported so far" is unverifiable because the article does not cite a specific source for this figure. The PLI scheme's reported exports are not typically published in a way that allows direct verification of this exact number. [confidence: medium]

INTERPRETATION ERRORS:
- "The USA is the top-8 destination in 11 of the 12 fastest-growing export chapters, ranking #1 or #2 in 9 of them — $63.9bn combined across just these tracked chapters (India's total exports to the US were $87.31bn in FY2025-26 per IBEF/commerce data), more concentrated by both breadth and depth than China's grip on the import side (8 of 12 chapters, $102.4bn but spread across more evenly-ranked positions)." — The claim implies a causal or comparative relationship between the USA's concentration in export chapters and China's import-side concentration, but the article does not provide evidence or data to support that the USA's concentration is *more* significant than China's in a meaningful economic or policy context. The comparison is an apples-to-oranges comparison because it does not account for differences in the number of chapters, total trade volumes, or the economic significance of the sectors involved. [confidence: high]

- "PLI Bulk Drugs ... generating ₹1,962 crore in sales (₹479 crore of it exports) and avoiding an estimated ₹1,483 crore in imports — explicitly aimed at cutting India's roughly 70% dependence on Chinese bulk-drug imports." — The claim that the PLI Bulk Drugs scheme is "explicitly aimed at cutting India's roughly 70% dependence on Chinese bulk-drug imports" is an overstatement. While reducing import dependence is a stated objective, the article does not provide evidence that the scheme's design or outcomes directly target or measure progress against the 70% figure. The 70% dependence is a general statistic, and the scheme's impact on it is not directly quantified or linked to the scheme's performance metrics. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
