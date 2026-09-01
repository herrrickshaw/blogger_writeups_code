# Fact/interpretation check — 028-unit-diesel-math-behind-indias-data

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/028-unit-diesel-math-behind-indias-data.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "India is building two new diesel-dependent industries at the same time — a gigawatt-scale AI data-centre pipeline and a five-fold expansion of telecom tower sites for 5G" — The article itself notes in Section 1 and Section 7 that telecom towers need to grow from roughly 750,000 to 1.2 million (an addition of ~450,000 towers). That represents a ~1.6x (60%) expansion, not a "five-fold" (5x / 500%) expansion. [confidence: high]

INTERPRETATION ERRORS:
- "Diesel generation costs roughly $0.28 a kilowatt-hour against grid power at $0.085 and solar-charged battery storage at $0.076–0.08... right as the economics of backup power tip decisively against diesel." — Comparing primary baseload grid power ($0.085/kWh) and round-the-clock renewable PPAs ($0.076–0.112/kWh) directly against diesel generation ($0.28/kWh) is an apples-to-oranges comparison. Grid power and PPAs represent primary continuous electricity tariffs, not standalone emergency backup power sources that can operate autonomously when the grid fails. [confidence: high]
- "A straight comparison of two backup architectures — Diesel Rotary UPS (DRUPS, which uses flywheel kinetic energy) against Static UPS with a battery bank (SUPS) — found DRUPS has a 9-month payback against SUPS on a 1.5 MW system... The economics inside that design standard are already shifting, though." — DRUPS (Diesel Rotary Uninterruptible Power Supply) integrates a diesel engine with a kinetic flywheel. It replaces chemical battery banks (Static UPS), but still relies entirely on diesel fuel for sustained backup generation. Citing the cost advantage of DRUPS as evidence that data centre economics are moving away from diesel dependency is contradictory, as adopting DRUPS entrenches diesel generator use. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Diesel generation costs roughly $0.28 a kilowatt-hour against grid power at $0.085 and solar-charged battery storage at $0.076–0.08." — The article cites these figures from the Takshashila Institution, but the dollar and rupee figures are quoted as sourced and not converted to a common currency, which could lead to misleading comparisons. The underlying studies use different methodologies (national grid-tariff averages versus a state-specific commercial/industrial backup-power model), making a direct comparison inappropriate. [confidence: high]

- "The Ministry of Power formally built a projection of 13.56 GW of data-centre electricity demand by FY2031–32 into national transmission planning, published via the Press Information Bureau in March 2026." — The article cites this figure as published in March 2026, but the PIB release date is not verifiable in the provided text or sources. The claim lacks a verifiable date or link to the PIB document. [confidence: medium]

INTERPRETATION ERRORS:
- "Diesel backup power costs roughly 3x the Indian grid average and 3.5x round-the-clock renewable PPAs — figures the post cites from the Takshashila Institution." — The article uses the cost comparison to argue that diesel is economically unviable, but it does not account for the operational differences between diesel generators and renewable PPAs. Diesel generators are typically used for backup during outages, while renewable PPAs provide continuous power. The comparison is an apples-to-oranges scenario because it conflates backup power costs with baseload power costs. [confidence: high]

- "The DRUPS-vs-SUPS payback comparison is drawn from one vendor/industry source describing a 1.5 MW reference system, not an independently audited multi-project average." — The article presents the 9-month payback period as a generalizable finding, but it is based on a single vendor's technical documentation for a specific system size. This does not provide sufficient evidence to conclude that such payback periods are typical or achievable across the broader data-centre industry. [confidence: high]
