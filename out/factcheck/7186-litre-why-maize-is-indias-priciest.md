# Fact/interpretation check — 7186-litre-why-maize-is-indias-priciest

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/7186-litre-why-maize-is-indias-priciest.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

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
- "Maize-based ethanol volumes went from zero to nearly 500 crore litres in three years" — The article cites maize-based ethanol supply to OMCs as 498.49 crore litres in ESY 2024-25, but does not provide data for ESY 2021-22 (the starting point). The claim implies zero ethanol production from maize in ESY 2021-22, which is unverifiable and likely incorrect, as maize ethanol production may have existed prior to ESY 2024-25. [confidence: medium]

- "Wheat is a rabi (winter) crop and maize/rice/sugarcane figures above are kharif; the four aren't measured in the same sowing window" — While the article correctly notes that wheat is a rabi crop and maize/rice/sugarcane are kharif crops, it incorrectly implies that the four crops are not measured in the same sowing window. In reality, kharif and rabi are distinct sowing seasons, but the article's phrasing suggests a lack of alignment in measurement windows, which is misleading. The comparison is valid because each crop is measured against its own sowing season. [confidence: high]

INTERPRETATION ERRORS:
- "Maize is now India's most expensive ethanol feedstock by government-set price — ₹71.86 a litre, ahead of sugarcane juice, rice, and every grade of molasses" — The article correctly states the government-set price for maize ethanol (₹71.86/litre) but does not establish that this price is the *only* factor determining feedstock choice. The claim implies a direct causal link between price and feedstock preference, but farmers' planting decisions are influenced by multiple factors (e.g., input costs, weather, competing crop economics), which the article acknowledges but does not fully address in this context. [confidence: high]

- "Maize's ethanol price didn't just rise — it started at the top of the scale the moment the category existed, and the volume response was immediate and large. That's a real, working demand signal." — The article correctly notes that maize ethanol price was set at ₹71.86/litre from ESY 2024-25 and that maize-based ethanol volumes surged. However, it does not establish a causal relationship between the price and the volume response. The volume increase could be due to other factors (e.g., ethanol blending mandates, OMC procurement policies, or pre-existing capacity), and the article does not rule out these alternatives. [confidence: medium]
