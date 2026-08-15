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

FACTUAL ERRORS:
- "India exported around 21 lakh tonnes of soybean meal in 2023-24, up 16% on the year" — The article does not provide a source for the 2022-23 export volume to verify the 16% increase [confidence: medium]
- "National output for the 2025-26 oil year is estimated by SOPA at around 105.36 lakh tonnes, down roughly 16% from the prior season's 125.82 lakh tonnes" — The article does not provide a primary source for the 2024-25 national output of 125.82 lakh tonnes to verify the 16% decrease [confidence: medium]

INTERPRETATION ERRORS:
- "A country growing this much soybean is, at the same time, actively lowering barriers to import more soybean oil — the crush economics, not the farm-gate harvest, are what actually govern the trade balance" — This statement implies a causal relationship between the country's soybean production and the decision to lower import barriers for soybean oil, but it does not provide evidence that the two are directly related [confidence: high]
- "India's roughly 150 soybean processing units are overwhelmingly built for crush-to-meal-and-oil, not food-grade protein extraction" — The article uses this fact to support the conclusion that India's domestic soy-food sector is underdeveloped, but it does not provide a clear explanation of why the existing processing units cannot be repurposed or modified for food-grade protein extraction [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India is one of the world's largest soybean growers by area" — This claim is vague and potentially misleading. While India is a major soybean grower, it is not among the *top* growers by area globally. The U.S., Brazil, and Argentina are the world's largest soybean producers by area, with India ranking far behind them. [confidence: high]

- "National output for the 2025-26 oil year is estimated by SOPA at around 105.36 lakh tonnes, down roughly 16% from the prior season's 125.82 lakh tonnes." — The article does not provide a clear definition of the "2025-26 oil year" or how it differs from the Kharif 2025 estimate (which is already cited as 43.25 lakh tonnes for MP and 52.23 lakh tonnes for Maharashtra). The 105.36 lakh tonnes figure appears to conflate state-level Kharif 2025 estimates with a national oil year estimate without proper clarification. [confidence: medium]

INTERPRETATION ERRORS:
- "The one soy-derived product where India genuinely leads the world — lecithin — is a byproduct of that same oil-crushing step, not a separate industry." — While lecithin is indeed a byproduct of oil refining, the claim that this alone explains India's global leadership in lecithin exports is an oversimplification. The article does not address other critical factors such as India's large-scale crushing infrastructure, export policies, or global demand dynamics that may contribute to its dominance in lecithin exports. [confidence: high]

- "India's roughly 150 soybean processing units are overwhelmingly built for crush-to-meal-and-oil, not food-grade protein extraction, and this piece did not find a public plant-level breakdown separating the two." — The article uses the lack of public data on food-grade processing capacity to imply that India's soy-food industry is underdeveloped, but it does not provide evidence that the existing processing units *could not* be repurposed for food-grade protein extraction. The claim assumes a structural limitation without verifying operational flexibility or industry adaptation. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
