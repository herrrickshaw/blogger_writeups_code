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
- "biomass power grew just 19% — the slowest of any renewable category" — The article claims biomass grew 19% between December 2019 and July 2026, but the table shows a growth of 19% from 9,861 MW to 11,747.57 MW, which is correct. However, the claim that it is "the slowest of any renewable category" is incorrect because small hydro grew only 11% in the same period, making it the slowest. [confidence: high]

INTERPRETATION ERRORS:
- "A 10–20% peak-hour premium is a percentage of the 'normal tariff' a state commission sets — for competitively bid solar and wind power in India, that normal tariff typically sits in the ₹2.5–3.5/kWh range, several times lower than biomass's own levellised cost before any ToD premium is even applied." — The reasoning gap here is that the article assumes the ToD premium is insufficient to bridge the cost gap for biomass power without considering whether the premium is applied to the biomass tariff itself or just the normal tariff. The ToD premium is meant to reward generators supplying power outside solar hours, but the article does not clarify if biomass generators are eligible for this premium or if the premium is applied to their existing tariffs. [confidence: medium]
