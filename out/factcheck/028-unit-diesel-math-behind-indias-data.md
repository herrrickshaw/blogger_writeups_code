# Fact/interpretation check — 028-unit-diesel-math-behind-indias-data

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/028-unit-diesel-math-behind-indias-data.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "a five-fold expansion of telecom tower sites for 5G" — The article's own text in Section 1 states that telecom towers need to grow from ~750,000 to ~1.2 million (an increase of ~60% or 1.6x, adding ~450,000 towers), which directly contradicts the claim of a "five-fold" (5x) expansion. [confidence: high]
- "solar-charged battery storage at $0.076–0.08" / "diesel generators cost... roughly three-and-a-half times what solar-charged battery storage costs" — The $0.076–0.08/kWh (or $0.076–0.112/kWh) figure refers to round-the-clock (RTC) renewable utility PPAs, not backup battery energy storage (BESS). The actual backup BESS levelised cost cited in Section 2 is ₹39.71–61.72/kWh (~$0.48–$0.74/kWh), which is higher than the $0.28/kWh diesel figure. [confidence: high]

INTERPRETATION ERRORS:
- "The economics inside that design standard are already shifting, though. A straight comparison of two backup architectures — Diesel Rotary UPS (DRUPS, which uses flywheel kinetic energy) against Static UPS with a battery bank (SUPS) — found DRUPS has a 9-month payback against SUPS on a 1.5 MW system, purely from lower operating cost ($1.84 million versus $5.46 million OpEx), even before counting emissions." — The author presents this as evidence that data centre economics are moving away from diesel. However, DRUPS is itself a diesel-driven generator architecture; finding that DRUPS has a fast payback over battery-based Static UPS (SUPS) demonstrates that diesel-based solutions remain cheaper than battery alternatives, directly contradicting the author's conclusion. [confidence: high]
- "Diesel generation costs roughly $0.28 a kilowatt-hour against grid power at $0.085 and solar-charged battery storage at $0.076–0.08" / "Diesel backup power costs roughly 3x the Indian grid average and 3.5x round-the-clock renewable PPAs" — This is an apples-to-oranges comparison. Comparing the per-kWh cost of backup power (an emergency asset run intermittently at low capacity factors) directly against baseload grid power tariffs and utility-scale RTC renewable PPAs misrepresents the economic purpose of backup infrastructure, which is sized for reliability during grid failure rather than primary baseload generation. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Diesel generation costs roughly $0.28 a kilowatt-hour against grid power at $0.085 and solar-charged battery storage at $0.076–0.08." — The article cites these figures from the Takshashila Institution, but the dollar and rupee figures are quoted as sourced and not converted to a common currency, which could lead to misleading comparisons. The underlying studies use different methodologies (national grid-tariff averages versus a state-specific commercial/industrial backup-power model), which shouldn't be blended into one number. [confidence: high]

INTERPRETATION ERRORS:
- "Telecom towercos have already proven the alternative works at scale; data centres, still writing their backup-power playbook, have not yet caught up." — While the article correctly notes that telecom towercos have adopted alternatives to diesel, it extrapolates that the same approach will work for data centres without sufficient evidence. Data centres have much larger, near-continuous loads and stricter uptime requirements, which would need their own costing and feasibility analysis. The Auroville Consulting BESS-vs-diesel cost comparison is a Tamil Nadu-specific commercial/industrial-sector study, not a data-centre- or telecom-tower-specific one, and is used here as the best available Indian LCOE/LCOS comparison rather than a claim that data centres or towers would see identical numbers. [confidence: high]
