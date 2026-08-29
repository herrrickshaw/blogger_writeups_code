# Fact/interpretation check — biomass-power-at-night-dispatchable

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/biomass-power-at-night-dispatchable.html`

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

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "biomass power grew just 19% — the slowest of any renewable category, in the one slot on the grid where a dispatchable renewable should be winning" — The article correctly states biomass grew 19% from Dec 2019 to Jul 2026, but the claim that this is "the slowest of any renewable category" is incorrect. Small hydro grew only 11% in the same period, making it the slowest-growing category. [confidence: high]

INTERPRETATION ERRORS:
- "A 10–20% peak-hour premium is a percentage of the 'normal tariff' a state commission sets — for competitively bid solar and wind power in India, that normal tariff typically sits in the ₹2.5–3.5/kWh range, several times lower than biomass's own levellised cost before any ToD premium is even applied" — While the cost comparison between biomass (₹9.6–11.1/kWh) and solar/wind (₹2.5–3.5/kWh) is factually correct, the interpretation that the ToD premium alone is insufficient to bridge this gap is an oversimplification. The article does not account for potential additional revenue streams (e.g., ancillary services, capacity payments) or long-term contracts that could make biomass viable despite higher levellised costs. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
