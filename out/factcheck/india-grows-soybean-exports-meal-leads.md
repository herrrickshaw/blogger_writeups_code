# Fact/interpretation check — india-grows-soybean-exports-meal-leads

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-grows-soybean-exports-meal-leads.html`

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
- "India is one of the world's largest soybean growers by area, concentrated almost entirely in two states." — This claim is misleading because India is not among the world's largest soybean growers by area. The top soybean-growing countries by area are the United States, Brazil, Argentina, and China, with India ranking much lower (around 5th-6th globally). The article later correctly states that MP and Maharashtra account for the majority of India's soybean area, but the initial claim overstates India's global ranking. [confidence: high]

- "National output for the 2025-26 oil year is estimated by SOPA at around 105.36 lakh tonnes, down roughly 16% from the prior season's 125.82 lakh tonnes." — The article cites SOPA estimates for 2025-26 output but does not provide a clear source or verification for this specific figure. The "oil year" terminology is also ambiguous (could refer to the marketing year or calendar year), and the 16% decline calculation is not explicitly sourced or explained in the text. [confidence: medium]

INTERPRETATION ERRORS:
- "The one soy-derived product where India genuinely leads the world — lecithin — is a byproduct of that same oil-crushing step, not a separate industry." — While lecithin is indeed a byproduct of oil refining, the claim that this alone explains India's global leadership in lecithin exports is an oversimplification. India's dominance in lecithin exports is likely also influenced by factors such as processing capacity, export infrastructure, and global demand dynamics, not just the byproduct status. The article does not explore these additional factors. [confidence: high]

- "India still imports roughly two-thirds of its total vegetable-oil demand — palm oil alone covers 55-60% of that import bill, with soybean oil (mainly from Argentina and Brazil) and sunflower oil making up most of the rest." — While the import dependence is correctly stated, the article does not adequately explain why India, despite being a major soybean producer, still imports soybean oil. The crush economics (e.g., meal exports being more profitable than oil refining for domestic use) are mentioned later, but the causal link between crush economics and import dependence is not clearly established in this section. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
