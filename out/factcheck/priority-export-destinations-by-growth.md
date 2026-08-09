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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99440, Requested 1924. Please try again in 19m38.495999999s. Need more tokens? Upgrade to Dev Tier today a]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "The USA takes 11 of India's 12 fastest-growing export chapters." — This claim is incorrect because the article later states that the USA is the top-8 destination in 11 of the 12 fastest-growing export chapters, not that it "takes" them. The phrasing implies ownership or control, which is misleading. [confidence: high]

- "HS61 (knitted apparel) and HS62 (not-knitted apparel), together $15.8bn of exports to a USA-and-EU-heavy buyer base" — The article cites $15.8bn as the combined export value for HS61 and HS62, but this figure is not explicitly verified in the TRADESTAT or IBEF/commerce data cited. The $15.8bn appears to be an internal calculation not directly sourced from the provided references. [confidence: medium]

INTERPRETATION ERRORS:
- "The USA is the top-8 destination in 11 of the 12 fastest-growing export chapters, ranking #1 or #2 in 9 of them — $63.9bn combined across just these tracked chapters (India's total exports to the US were $87.31bn in FY2025-26 per IBEF/commerce data)" — The claim that the USA's concentration in these 11 chapters is "more concentrated by both breadth and depth than China's grip on the import side" is an apples-to-oranges comparison. The article compares India's export concentration to the USA with China's import concentration (which is not necessarily the same metric or scope), without providing a direct comparison of the same metric (e.g., top-8 destinations for China's imports vs. India's exports). [confidence: high]

- "PLI Bulk Drugs ... generating ₹1,962 crore in sales (₹479 crore of it exports) and avoiding an estimated ₹1,483 crore in imports — explicitly aimed at cutting India's roughly 70% dependence on Chinese bulk-drug imports." — The claim that the PLI Bulk Drugs scheme is "explicitly aimed at cutting India's roughly 70% dependence on Chinese bulk-drug imports" is an overstatement. While the scheme may reduce import dependence, the article does not provide evidence that this was the primary or explicit aim of the scheme. The reduction in imports is a potential outcome, not a stated objective. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
