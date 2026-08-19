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
- "India Grows the Soybean, Exports the Meal, Leads in Lecithin — and Barely Makes Tofu Yet" (headline) — The headline implies that India barely produces tofu, but the article itself later states that soya chunks/nuggets/granules (e.g., Nutrela) are a mass-market staple in India, which contradicts the headline's framing of the soy-food industry as minimal. [confidence: high]

- "National output for the 2025-26 oil year is estimated by SOPA at around 105.36 lakh tonnes, down roughly 16% from the prior season's 125.82 lakh tonnes." — The article cites SOPA estimates for 2025-26, but the 2024-25 final production figures for MP and Maharashtra (55.40 and 50.17 lakh tonnes, respectively) sum to 105.57 lakh tonnes, which does not align with the national output figure of 125.82 lakh tonnes for 2024-25. This suggests a discrepancy in the national production totals. [confidence: high]

INTERPRETATION ERRORS:
- "The one soy-derived product where India genuinely leads the world — lecithin — is a byproduct of that same oil-crushing step, not a separate industry." — While lecithin is indeed a byproduct of oil refining, the article implies that this alone explains India's leading position in lecithin exports. However, it does not address whether India's dominance is due to processing capacity, export infrastructure, or other factors like cost competitiveness or trade policies. The claim oversimplifies the causal factors behind India's lecithin export leadership. [confidence: medium]

- "A crushed soybean splits, roughly, into about 80% meal and 18-20% oil by weight — which is why the export story and the domestic-shortage story point in opposite directions for the same crop." — The article correctly states the split ratio but incorrectly implies that this split alone explains the opposing export and import dynamics. The domestic shortage of edible oil is driven by refining capacity and import dependence, not just the split ratio. The claim conflates the physical composition of the soybean with trade and processing economics. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
