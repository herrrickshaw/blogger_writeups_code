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
- "Diesel generation costs roughly $0.28 a kilowatt-hour against grid power at $0.085 and solar-charged battery storage at $0.076–0.08." — The article cites these figures as sourced from Takshashila Institution and Auroville Consulting, but the dollar and rupee figures are quoted separately without conversion, and the methodology for blending national grid averages with state-specific backup-power models is inconsistent. The claim implies a direct comparison that the sources do not support. [confidence: high]

- "The Ministry of Power formally built a projection of 13.56 GW of data-centre electricity demand by FY2031–32 into national transmission planning, published via the Press Information Bureau in March 2026." — The article cites this figure as published in March 2026, but the referenced PIB release is not provided, and the date is inconsistent with the article's own publication date of 20 August 2026 (suggesting the PIB release would logically precede the article by months, not coincide with it). [confidence: medium]

INTERPRETATION ERRORS:
- "Telecom towercos have already proven the alternative works at scale; data centres, still writing their backup-power playbook, have not yet caught up." — While the telecom sector has demonstrated diesel phase-out where grid reliability permits, the article does not establish that the same backup-power alternatives (e.g., solar-charged BESS) are directly comparable in cost or performance for data centres due to differences in load profiles, uptime requirements, and scale. The claim implies a straightforward transferability of telecom tower solutions to data centres without sufficient evidence. [confidence: high]

- "A straight comparison of two backup architectures — Diesel Rotary UPS (DRUPS) against Static UPS with a battery bank (SUPS) — found DRUPS has a 9-month payback against SUPS on a 1.5 MW system, purely from lower operating cost ($1.84 million versus $5.46 million OpEx), even before counting emissions." — The payback calculation is based on a single vendor's reference system (1.5 MW) and not an independently audited multi-project average. The claim extrapolates from a narrow case to a general conclusion about backup-power economics for data centres, which may not hold across different system sizes, configurations, or operational contexts. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
