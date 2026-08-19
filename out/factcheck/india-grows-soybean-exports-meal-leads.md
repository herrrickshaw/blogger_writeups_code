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
- "India Grows the Soybean, Exports the Meal, Leads in Lecithin — and Barely Makes Tofu Yet" (headline) — The headline implies India barely produces tofu, but the article later notes that soya chunks/nuggets/granules (TVP) are a long-standing, mass-market staple in India, led by brands like Nutrela. This contradicts the headline's framing of India's soy-food industry as minimal. [confidence: high]

- "National output for the 2025-26 oil year is estimated by SOPA at around 105.36 lakh tonnes, down roughly 16% from the prior season's 125.82 lakh tonnes." (text) — The article cites SOPA estimates for 2025-26 output but does not provide a clear source or verification for this specific figure. The cited "Global Agriculture reporting" is vague, and SOPA's own tables do not explicitly list a 2025-26 estimate in the provided data. [confidence: medium]

---

INTERPRETATION ERRORS:
- "A country growing this much soybean is, at the same time, actively lowering barriers to import more soybean oil — the crush economics, not the farm-gate harvest, are what actually govern the trade balance." (text) — While the claim about crush economics influencing trade balance is plausible, the article does not provide evidence linking the specific import duty cut (from 20% to 10% in May 2025) to the trade balance outcome. The duty cut could have other objectives (e.g., controlling retail prices), and the article does not establish causality between the policy change and the trade balance. [confidence: high]

- "Lecithin didn't require India to build a new industry. It required India to keep the one it already had for meal and oil, and sell what used to be a processing waste stream." (text) — While lecithin is indeed a byproduct of oil refining, the claim that India "leads the world" in lecithin exports (8,582 shipments vs. Argentina's 1,499 and China's 586) is presented as a direct result of repurposing waste. However, the article does not explain whether India's leadership is due to processing capacity, export infrastructure, or other factors like global demand shifts. The causal link between India's existing infrastructure and its export dominance is implied but not substantiated. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
