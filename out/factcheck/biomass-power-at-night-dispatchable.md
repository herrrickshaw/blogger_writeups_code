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

- "A 2023 CSEP working paper analysing high-resolution 2019 Indian grid data confirms the pattern is already visible here, and warns it will sharpen" — The article cites a 2023 CSEP working paper analyzing 2019 data, but the claim that it "warns it will sharpen" is not directly supported by the quoted text. The quoted text only states that renewable energy's contribution to net demand is lower during high net demand periods (evening peak) and that storage or an alternative peaker would be required. The "will sharpen" phrasing implies a future projection not explicitly stated in the cited source. [confidence: medium]

INTERPRETATION ERRORS:
- "Biomass power can run at night. It is one of the few renewable sources that actually can. And yet, while India's total renewable capacity (excluding large hydro) grew 178% between December 2019 and July 2026, biomass power grew just 19% — the slowest of any renewable category, in the one slot on the grid where a dispatchable renewable should be winning." — The claim that biomass "should be winning" in the dispatchable renewable slot is an interpretation error. The article does not provide evidence that biomass is the *only* or *best* dispatchable renewable option for nighttime demand. Other dispatchable renewables (e.g., pumped hydro, battery storage) or even non-renewables (e.g., gas peaking plants) could also fill this role. The conclusion that biomass "should" dominate this niche lacks comparative analysis of alternatives. [confidence: high]

- "A 10–20% peak-hour premium is a percentage of the 'normal tariff' a state commission sets — for competitively bid solar and wind power in India, that normal tariff typically sits in the ₹2.5–3.5/kWh range, several times lower than biomass's own levellised cost before any ToD premium is even applied." — The reasoning gap here is that the article assumes the ToD premium is the primary factor influencing biomass growth, but it does not account for other structural barriers (e.g., feedstock supply chains, PPA structures, or biomass's role in sugar mills' captive use). The claim that the ToD premium is "not enough" is supported by cost data, but the framing implies the premium is the *main* reason for slow growth, which oversimplifies the multi-faceted challenges biomass faces. [confidence: high]
