# Fact/interpretation check — blending-on-budget-energy-density-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/blending-on-budget-energy-density-and.html`

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
- "Ethanol and isobutanol fall well short of their host fuel's energy density, which is why those mandates cost drivers mileage; CBG and SAF sit near parity, which is why their cost shows up as price instead." — The claim is correct, but the article later states that isobutanol carries ~74% of diesel's energy density, not "well short" (which implies a larger gap). The phrasing is misleadingly absolute. [confidence: high]

- "SAF traded globally in 2026 at roughly $1,817 per tonne, on the order of five times a conventional jet-fuel benchmark in tight markets" — The article cites this as a global 2026 figure, but no primary source is provided for this specific claim, and the context suggests it may be an extrapolation or misinterpretation of spot market data. [confidence: medium]

INTERPRETATION ERRORS:
- "Ethanol in petrol — the fuel that actually loses mileage" (Section 3) — The article correctly notes that E20 causes a 2–6% mileage loss, but it then calculates a "permanent tax" of ₹0.27–0.33 per km based on this loss, implying a direct financial cost to drivers. However, this assumes no offsetting benefits (e.g., lower fuel prices due to ethanol blending subsidies or carbon credits), which are not accounted for. The conclusion that the cost is a "permanent tax" overstates the net impact without considering broader policy or market dynamics. [confidence: high]

- "The pattern in one line: ethanol carries 66% of petrol's energy per litre and isobutanol carries 74% of diesel's, so both mandates cost the driver mileage." — While the energy density ratios are correct, the conclusion that *both* mandates cost mileage is an oversimplification. The article later clarifies that isobutanol's mileage loss is "smaller than ethanol's" (Section 5), but the initial framing suggests parity in impact, which is misleading. The interpretation conflates the *existence* of a mileage penalty with its *magnitude*. [confidence: high]
