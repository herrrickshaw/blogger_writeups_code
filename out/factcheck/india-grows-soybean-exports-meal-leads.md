# Fact/interpretation check — india-grows-soybean-exports-meal-leads

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-grows-soybean-exports-meal-leads.html`

## Gemini gemini-flash-latest

[Gemini API error 503: {
  "error": {
    "code": 503,
    "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
    "status": "UNAVAILABLE"
  }
}
]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India is one of the world's largest soybean growers by area, concentrated almost entirely in two states." — This claim is misleading because India is not among the world's largest soybean growers by area. The top soybean-growing countries by area are the United States, Brazil, Argentina, and China, with India ranking much lower (around 5th-6th globally). The article later correctly states that MP and Maharashtra account for most of India's soybean area, but the initial claim overstates India's global ranking. [confidence: high]

- "National output for the 2025-26 oil year is estimated by SOPA at around 105.36 lakh tonnes, down roughly 16% from the prior season's 125.82 lakh tonnes." — The article cites SOPA estimates for 2025-26, but the 2024-25 final production figures (55.40 lakh tonnes for MP and 50.17 lakh tonnes for Maharashtra) already sum to 105.57 lakh tonnes, which is lower than the claimed 125.82 lakh tonnes for the prior season. This suggests a discrepancy in the numbers provided. [confidence: high]

INTERPRETATION ERRORS:
- "The one soy-derived product where India genuinely leads the world — lecithin — is a byproduct of that same oil-crushing step, not a separate industry." — While lecithin is indeed a byproduct of oil refining, the claim that this alone explains India's global leadership in lecithin exports is an oversimplification. India's dominance in lecithin exports is likely also influenced by factors such as cost competitiveness, processing infrastructure, and trade policies, not just the byproduct nature of lecithin. The article does not provide evidence to support the causal link between lecithin being a byproduct and India's export leadership. [confidence: medium]

- "This is the same maize-for-ethanol pull this blog has covered from the ethanol side; here it shows up as an oilseed-acreage problem instead." — The article conflates two separate issues: the shift from soybean to maize for ethanol feedstock (which is a demand-side pull) and the soybean acreage problem (which is a supply-side issue driven by price weakness). The claim implies that the maize-for-ethanol demand is the primary driver of the soybean acreage shift, but it does not provide evidence to support this causal relationship. The acreage shift could also be due to other factors like profitability, input costs, or policy incentives unrelated to ethanol. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
