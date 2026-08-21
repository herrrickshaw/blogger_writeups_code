# Fact/interpretation check — 028-unit-diesel-math-behind-indias-data

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/028-unit-diesel-math-behind-indias-data.html`

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
- "Diesel generation costs roughly $0.28 a kilowatt-hour against grid power at $0.085 and solar-charged battery storage at $0.076–0.08." — The article cites this cost comparison from the Takshashila Institution, but the source itself notes that these figures are compiled from grid-tariff and PPA data and are not necessarily specific to backup power costs. The diesel cost of $0.28/kWh is likely an overestimate for backup power, as diesel gensets are typically used only during outages, not continuously. [confidence: high]

- "The Ministry of Power formally built a projection of 13.56 GW of data-centre electricity demand by FY2031–32 into national transmission planning, published via the Press Information Bureau in March 2026." — The article cites this figure as published in March 2026, but the PIB release date is not provided in the article, and the claim is not directly verifiable from the cited sources. The Ministry of Power's transmission planning documents are not typically published via PIB in this manner. [confidence: medium]

INTERPRETATION ERRORS:
- "Telecom towercos have already proven the alternative works at scale; data centres, still writing their backup-power playbook, have not yet caught up." — While the article correctly notes that telecom towercos have adopted alternatives to diesel, it extrapolates this precedent to data centres without sufficient evidence. The operational requirements for data centres (e.g., near-continuous uptime, higher power density) differ significantly from telecom towers, and the cost comparisons cited (e.g., Auroville Consulting's Tamil Nadu-specific study) are not tailored to data centres. The claim assumes that what works for telecom towers will work for data centres without demonstrating applicability. [confidence: high]

- "A straight comparison of two backup architectures — Diesel Rotary UPS (DRUPS) against Static UPS with a battery bank (SUPS) — found DRUPS has a 9-month payback against SUPS on a 1.5 MW system, purely from lower operating cost ($1.84 million versus $5.46 million OpEx), even before counting emissions." — The article cites a vendor-provided comparison for a single 1.5 MW system, which is not representative of the broader data-centre or telecom-tower sectors. The payback period is likely to vary significantly based on site-specific factors (e.g., diesel fuel costs, grid reliability, uptime requirements), and the claim extrapolates from a single case study to a general conclusion. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
