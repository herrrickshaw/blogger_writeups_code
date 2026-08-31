# Fact/interpretation check — biomass-power-at-night-dispatchable

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/biomass-power-at-night-dispatchable.html`

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
- "biomass power grew just 19% — the slowest of any renewable category, in the one slot on the grid where a dispatchable renewable should be winning" — The article correctly states biomass grew 19% (from 9,861 MW in Dec 2019 to 11,747.57 MW in Jul 2026), but the claim that this is "the slowest of any renewable category" is incorrect. Small hydro grew only 11% over the same period, making it the slowest-growing category. [confidence: high]

INTERPRETATION ERRORS:
- "A 2018 Centre for Science and Environment analysis of Delhi's summer electricity demand [...] found that late-night demand exceeded afternoon demand on 21 of 31 days in May of that year, driven almost entirely by air conditioner use after commercial establishments had closed; the average day peak (5,280 MW) and average night peak (5,256 MW) were within 0.5% of each other." — While the cited 2018 Delhi data illustrates a structural mechanism (AC-driven night demand), the article extrapolates this pattern to India as a whole in 2026 without evidence. The claim implies a nationwide night-time demand peak exists, but the article itself notes that the Delhi data is cited "for the structural pattern it documents, not as current data" and lacks national-scale verification. [confidence: high]
