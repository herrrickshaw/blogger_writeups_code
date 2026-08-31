# Fact/interpretation check — green-gold-what-spirulina-actually-is

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/green-gold-what-spirulina-actually-is.html`

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
- "China still grows most of the world’s supply; South Korea, it turns out, mostly buys it in." — This claim is incorrect. While China dominates spirulina production (45–65% of global output), South Korea does not primarily *buy* spirulina; it imports it for processing but also has domestic microalgae cultivation (e.g., Phycoil Biotech Korea for DHA oil). The article later contradicts this by noting Korea's domestic trials and lack of large-scale spirulina cultivation. [confidence: high]

- "The Union Cabinet approved the BioE3 Policy on 24 August 2024" — The article cites this date, but the BioE3 Policy was actually approved on **19 August 2024** (as stated in the article's header and body text). The discrepancy suggests a typographical error in the claim. [confidence: high]

INTERPRETATION ERRORS:
- "A quarter-acre pond can out-earn an acre of crop" — The article cites commercial farming guides and trade press figures (e.g., ₹60,000–₹1 lakh monthly revenue) to support this claim, but these are **not audited farm-income surveys** and are presented as illustrative claims. The comparison between a quarter-acre pond and an acre of row crops is based on unverified commercial estimates, making the earnings claim speculative rather than proven. [confidence: high]

- "Spirulina biomass has been fermented to ethanol at reported yields of roughly 16% (g ethanol per g biomass) after acid pre-treatment" — While the lab-scale yield is cited correctly, the article presents this as a viable commercial pathway without clarifying that **no commercial spirulina-to-fuel plant exists in India** (or globally). The yield figure alone does not justify the biofuel application's maturity, as the broader infrastructure and economic viability remain unproven. [confidence: high]
