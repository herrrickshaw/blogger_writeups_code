# Fact/interpretation check — 028-unit-diesel-math-behind-indias-data

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/028-unit-diesel-math-behind-indias-data.html`

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
- "Diesel generation costs roughly $0.28 a kilowatt-hour against grid power at $0.085 and solar-charged battery storage at $0.076–0.08." — The article cites these figures from the Takshashila Institution, but the dollar and rupee figures are quoted as sourced and not converted to a common currency, which could lead to confusion or misinterpretation. The methodology differences between national grid-tariff averages and state-specific commercial/industrial backup-power models mean these numbers are not directly comparable without adjustment. [confidence: high]

- "The Ministry of Power formally built a projection of 13.56 GW of data-centre electricity demand by FY2031–32 into national transmission planning, published via the Press Information Bureau in March 2026." — The article cites this figure as an official government anchor, but the source is the Ministry of Power's transmission planning published via PIB in March 2026. However, the article does not provide a direct link or primary document to verify this claim independently. [confidence: medium]

INTERPRETATION ERRORS:
- "Diesel backup power costs roughly 3x the Indian grid average and 3.5x round-the-clock renewable PPAs — figures the post cites from the Takshashila Institution." — The article uses the cost comparison to argue that diesel is economically unviable for backup power, but it does not account for the operational differences between diesel generators and renewable PPAs. Diesel generators are typically used for short-duration backup during grid outages, while renewable PPAs provide continuous power. The comparison assumes similar usage patterns, which is not accurate. [confidence: high]

- "A straight comparison of two backup architectures — Diesel Rotary UPS (DRUPS) against Static UPS with a battery bank (SUPS) — found DRUPS has a 9-month payback against SUPS on a 1.5 MW system, purely from lower operating cost ($1.84 million versus $5.46 million OpEx), even before counting emissions." — The article presents this as a generalizable finding, but the comparison is based on a single vendor's technical documentation for a 1.5 MW reference system. It does not provide evidence that this payback period holds across different system sizes, usage patterns, or real-world deployments. [confidence: high]
