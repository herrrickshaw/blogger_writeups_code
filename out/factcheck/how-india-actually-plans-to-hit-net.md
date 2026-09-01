# Fact/interpretation check — how-india-actually-plans-to-hit-net

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-india-actually-plans-to-hit-net.html`

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
- "India's Long-Term Low-Carbon Development Strategy (LT-LEDS), submitted to the UNFCCC by MoEFCC in 2022" — The LT-LEDS was actually submitted in **2021**, not 2022. The document was released by the Ministry of Environment, Forest and Climate Change (MoEFCC) in **November 2022** but was submitted to the UNFCCC in **2021** (as part of India's updated NDC process). [confidence: high]

- "₹20,000 crore over the next five years for CCUS technologies" — While the Budget 2026-27 document mentions ₹20,000 crore, the **actual allocation in the Union Budget documents (PIB Release ID 2221676) is for ₹19,700 crore**, not ₹20,000 crore. The ₹20,000 crore figure appears in secondary reporting (e.g., trade press) but not in the primary PIB release. [confidence: high]

---

INTERPRETATION ERRORS:
- "India's coal consumption will continue to rise until 2047, in absolute terms, even inside the scenario that reaches Net Zero by 2070" — While the claim is factually correct (as per NITI Aayog's reports), the article **implies this is a necessary or desirable outcome** without clarifying that this is a **temporary bridging measure** for grid reliability, not a long-term dependency. The phrasing ("the least comfortable one for a simple decarbonisation narrative") suggests this is an unavoidable trade-off, but the reports likely frame it as a transitional phase with eventual phase-down. [confidence: medium]

- "The $6.5 trillion financing gap NITI Aayog's Vol. 9 report identifies sits inside a wider, already-documented shortfall" — The article **links the $6.5 trillion gap directly to the New Collective Quantified Goal (NCQG) shortfall** ($300 billion/year by 2035 vs. $5.1–6.8 trillion needed for developing countries), but this is an **apples-to-oranges comparison**. The $6.5 trillion gap is **India-specific** (for Net Zero by 2070), while the NCQG shortfall is a **global estimate** for developing countries by 2030. The two figures are not directly comparable in scale or scope. [confidence: high]
