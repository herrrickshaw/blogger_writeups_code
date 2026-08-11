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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99096, Requested 1924. Please try again in 14m41.28s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "The USA takes 11 of India's 12 fastest-growing export chapters." — This claim is incorrect because the article later states that the USA is the top-8 destination in 11 of the 12 fastest-growing export chapters, not that it "takes" 11 chapters outright. The phrasing implies exclusive dominance, which is not supported by the subsequent data. [confidence: high]

- "HS61 (knitted apparel) and HS62 (not-knitted apparel), together $15.8bn of exports to a USA-and-EU-heavy buyer base" — The article does not provide a source or breakdown for the $15.8bn figure, and it is not verifiable against the cited TRADESTAT or PIB/Ministry releases. The claim lacks a clear citation or methodology for this specific aggregation. [confidence: medium]

INTERPRETATION ERRORS:
- "The USA is the top-8 destination in 11 of the 12 fastest-growing export chapters, ranking #1 or #2 in 9 of them — $63.9bn combined across just these tracked chapters (India's total exports to the US were $87.31bn in FY2025-26 per IBEF/commerce data), more concentrated by both breadth and depth than China's grip on the import side (8 of 12 chapters, $102.4bn but spread across more evenly-ranked positions)." — The comparison between the USA's export concentration ($63.9bn across 11 chapters) and China's import concentration ($102.4bn across 8 chapters) is an apples-to-oranges comparison. The article does not adjust for differences in the number of chapters tracked, the total value of trade, or the underlying economic context (e.g., import substitution vs. export growth). The conclusion that the USA's concentration is "more concentrated by both breadth and depth" is not justified by the raw numbers alone. [confidence: high]

- "PLI Bulk Drugs ... generating ₹1,962 crore in sales (₹479 crore of it exports) and avoiding an estimated ₹1,483 crore in imports — explicitly aimed at cutting India's roughly 70% dependence on Chinese bulk-drug imports." — The claim that the PLI Bulk Drugs scheme is "explicitly aimed at cutting India's roughly 70% dependence on Chinese bulk-drug imports" is an overinterpretation. While the scheme may reduce import dependence, the article does not provide evidence that this was a stated or primary objective of the scheme. The 70% figure is also not sourced or explained in the context of the PLI scheme's goals. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
