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
- "India Grows the Soybean, Exports the Meal, Leads in Lecithin — and Barely Makes Tofu Yet" (headline) — The headline implies that India barely makes tofu, but the article itself states that soya chunks/nuggets/granules (e.g., Nutrela) are a long-standing, mass-market staple in India, which contradicts the "barely makes tofu" claim. [confidence: high]

- "National output for the 2025-26 oil year is estimated by SOPA at around 105.36 lakh tonnes, down roughly 16% from the prior season's 125.82 lakh tonnes." (text) — The article cites SOPA estimates for 2025-26 output but does not provide a clear definition of the "oil year" or confirm whether this aligns with the Kharif 2025 estimates (which show lower production). The discrepancy between the 2024-25 final (125.82 lakh tonnes) and Kharif 2025 estimate (e.g., MP at 43.25 lakh tonnes) suggests potential confusion in seasonal reporting or a miscalculation. [confidence: medium]

---

INTERPRETATION ERRORS:
- "This is the same maize-for-ethanol pull this blog has covered from the ethanol side; here it shows up as an oilseed-acreage problem instead." (text) — The article conflates two separate issues: (1) maize's role as an ethanol feedstock (driving acreage shifts) and (2) soybean's price weakness (due to floor price vs. mandi prices). While both factors may contribute to reduced soybean acreage, the causal link between maize-for-ethanol and soybean's acreage decline is not directly supported by the data presented. The article does not demonstrate that ethanol demand for maize is the *primary* driver of soybean acreage reduction, nor does it rule out other factors (e.g., input costs, weather). [confidence: medium]

- "Lecithin didn't require India to build a new industry. It required India to keep the one it already had for meal and oil, and sell what used to be a processing waste stream." (text) — While lecithin is indeed a byproduct of oil refining, the claim that India "leads the world" in lecithin exports (8,582 shipments vs. Argentina's 1,499 and China's 586) is presented as a direct outcome of India's crushing infrastructure. However, the article does not establish whether India's leadership in lecithin exports is due to its crushing scale *alone* or also reflects other factors (e.g., global demand shifts, pricing advantages, or trade policies). The causal claim overstates the role of India's existing infrastructure without addressing these additional variables. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
