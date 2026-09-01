# Fact/interpretation check — india-grows-soybean-exports-meal-leads

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-grows-soybean-exports-meal-leads.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

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
- "India is one of the world's largest soybean growers by area" — This claim is incorrect. India is one of the world's largest soybean growers by **area**, but it is not among the largest by **production** due to low yields. The article later contradicts this by stating India's low yields (e.g., MP's 1,065 kg/ha and Maharashtra's 1,115 kg/ha), which are far below global averages (e.g., Brazil's ~3,000 kg/ha). [confidence: high]

- "National output for the 2025-26 oil year is estimated by SOPA at around 105.36 lakh tonnes, down roughly 16% from the prior season's 125.82 lakh tonnes." — The article cites these figures without providing a direct source or context for the "2025-26 oil year" definition. SOPA typically reports crop years (e.g., Kharif 2025), and the 16% decline is not clearly verifiable against standard reporting periods. [confidence: medium]

---

INTERPRETATION ERRORS:
- "Madhya Pradesh's soybean output fell and Maharashtra's rose between the two most recent seasons — a reversal tied to a Yellow Mosaic Virus outbreak in MP's Mandsaur belt." — While the virus outbreak is a plausible explanation for MP's yield decline, the article does not provide quantitative evidence linking the virus to the specific yield drop (e.g., comparative yield data from unaffected MP districts or historical trends). The causal claim is asserted without sufficient proof. [confidence: high]

- "India's oilmeal exports fell 51% year-on-year to just 1.62 lakh tonnes in November 2025, because Indian soymeal is currently priced out of the global market against Brazil and Argentina." — The article attributes the export decline solely to price competitiveness but does not account for other potential factors, such as domestic demand shifts, policy changes (e.g., export duties), or global supply fluctuations (e.g., Brazil/Argentina's own export volumes). The causal claim is oversimplified. [confidence: high]
