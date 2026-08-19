# Fact/interpretation check — soybean-mp-maharashtra-tofu-lecithin-protein

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/soybean-mp-maharashtra-tofu-lecithin-protein.html`

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
- "India is one of the world's largest soybean growers by area" — This claim is outdated or incorrect. While India is a major soybean producer, it is not among the *largest by area* globally. The top soybean-growing countries by area are the U.S., Brazil, Argentina, and China, with India ranking lower. [confidence: high]

- "National output for the 2025-26 oil year is estimated by SOPA at around 105.36 lakh tonnes, down roughly 16% from the prior season's 125.82 lakh tonnes." — The article cites SOPA estimates for 2025-26, but the 2024-25 final production figures (55.40 lakh tonnes for MP and 50.17 lakh tonnes for Maharashtra) already sum to 105.57 lakh tonnes, which is lower than the claimed 125.82 lakh tonnes for the prior season. This inconsistency suggests a miscalculation or misattribution. [confidence: high]

INTERPRETATION ERRORS:
- "The one soy-derived product where India genuinely leads the world — lecithin — is a byproduct of that same oil-crushing step, not a separate industry." — While lecithin is indeed a byproduct of oil refining, the claim that this alone explains India's global leadership in lecithin exports is an oversimplification. India's dominance in lecithin exports is likely also influenced by its large-scale crushing infrastructure, cost advantages, and export market access, not just the fact that it is a byproduct. The article does not provide evidence to support the causal claim that the byproduct status is the *primary* reason for leadership. [confidence: medium]

- "This is the same maize-for-ethanol pull this blog has covered from the ethanol side; here it shows up as an oilseed-acreage problem instead." — The article links the shift from soybean to maize to ethanol demand but does not provide data or analysis to quantify the extent to which ethanol policy (rather than other factors like price weakness or agronomic conditions) is driving this acreage shift. The causal claim is asserted without evidence of the relative contribution of ethanol demand versus other factors. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
