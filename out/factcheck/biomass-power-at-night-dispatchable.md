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

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "biomass power grew just 19% — the slowest of any renewable category, in the one slot on the grid where a dispatchable renewable should be winning" — The article correctly states biomass grew 19% between December 2019 and July 2026, but the claim that this is "the slowest of any renewable category" is incorrect. Small hydro grew only 11% in the same period, making it the slowest-growing category. [confidence: high]

- "the Ministry of New & Renewable Energy's state-wise installed renewable capacity table, dated 31 July 2026" — The article cites this as the source for 2026 biomass capacity figures, but the Ministry of New & Renewable Energy (MNRE) typically updates its capacity tables monthly or quarterly, not just on 31 July 2026. The exact date of the table is unverifiable as a single snapshot. [confidence: medium]

INTERPRETATION ERRORS:
- "A 10–20% peak-hour premium is a percentage of the 'normal tariff' a state commission sets — for competitively bid solar and wind power in India, that normal tariff typically sits in the ₹2.5–3.5/kWh range, several times lower than biomass's own levellised cost before any ToD premium is even applied." — While the cost comparison is factually correct, the interpretation that the ToD premium is insufficient to bridge the gap is flawed. The article does not account for the fact that biomass generators may sell power at higher rates during peak hours (including ToD premiums) while still selling at lower rates during off-peak hours, potentially improving overall project economics. The claim implies a uniform pricing structure, which is not necessarily the case. [confidence: high]

- "Biomass power, unlike solar, can be dispatched into exactly that window [night-time peak]." — While biomass can technically be dispatched at night, the article does not address the practical limitations of biomass plants, such as feedstock availability, seasonal variations in agricultural residues, and operational constraints (e.g., minimum load factors, ramp rates). These factors may prevent biomass from fully meeting the night-time demand peak, even if it is technically dispatchable. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
