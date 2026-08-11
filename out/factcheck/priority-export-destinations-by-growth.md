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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99138, Requested 1924. Please try again in 15m17.568s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "The USA takes 11 of India's 12 fastest-growing export chapters." — This claim is unverifiable as stated because the article does not provide the list of the 12 fastest-growing export chapters or their growth metrics. Without this, the claim cannot be fact-checked against TRADESTAT data. [confidence: low]

- "The PLI Scheme for Textiles (₹10,683 crore, notified September 2021; 91 companies selected as of September 2025, ₹7,731 crore invested, but only ₹733 crore of exports reported so far)" — The article cites specific figures (₹10,683 crore, ₹7,731 crore, ₹733 crore) without providing a primary source or verification link. These numbers cannot be independently confirmed from the given text. [confidence: medium]

INTERPRETATION ERRORS:
- "The USA is the top-8 destination in 11 of the 12 fastest-growing export chapters, ranking #1 or #2 in 9 of them — $63.9bn combined across just these tracked chapters (India's total exports to the US were $87.31bn in FY2025-26 per IBEF/commerce data)" — The claim implies a causal link between the concentration of exports to the USA in these 12 chapters and the overall export performance to the USA, but the $63.9bn figure is only for the tracked chapters, not the total $87.31bn. The comparison is apples-to-oranges because the $63.9bn is a subset of the total exports to the USA. [confidence: high]

- "PLI Bulk Drugs ... generating ₹1,962 crore in sales (₹479 crore of it exports) and avoiding an estimated ₹1,483 crore in imports — explicitly aimed at cutting India's roughly 70% dependence on Chinese bulk-drug imports." — The article claims the PLI Bulk Drugs scheme is "explicitly aimed at cutting India's roughly 70% dependence on Chinese bulk-drug imports," but the figures provided (₹1,962 crore in sales, ₹479 crore in exports, ₹1,483 crore in import substitution) do not directly quantify or demonstrate a reduction in import dependence. The causal link between the scheme's outputs and the 70% import dependence is not supported by the data presented. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
