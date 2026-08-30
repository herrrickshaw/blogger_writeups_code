# Fact/interpretation check — 028-unit-diesel-math-behind-indias-data

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/028-unit-diesel-math-behind-indias-data.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "India is building two new diesel-dependent industries at the same time — a gigawatt-scale AI data-centre pipeline and a five-fold expansion of telecom tower sites for 5G" — The article later states that the telecom tower base is projected to grow from roughly 750,000 (or 606,300) towers to around 1.2 million. Expanding to 1.2 million is an increase of roughly 60% to 100% (1.6x–2x), not a "five-fold" (5x) expansion. [confidence: high]

INTERPRETATION ERRORS:
- "Diesel generation costs roughly $0.28 a kilowatt-hour against grid power at $0.085 and solar-charged battery storage at $0.076–0.08." / "...roughly three-and-a-half times what solar-charged battery storage costs" — Apples-to-oranges comparison and misattribution: The $0.076–0.112/kWh figure represents wholesale round-the-clock (RTC) renewable power-purchase agreements (grid supply tariffs), not the levelised cost of on-site solar-plus-battery backup storage. The article's own cited backup storage study (Auroville Consulting) places the levelised cost of storage (LCOS) for on-site solar BESS backup at ₹39.71–61.72/kWh (roughly $0.48–0.74/kWh), which is comparable to or higher than the diesel backup cost ($0.28/kWh or ₹49.58–57.63/kWh). [confidence: high]
- "A straight comparison of two backup architectures — Diesel Rotary UPS (DRUPS, which uses flywheel kinetic energy) against Static UPS with a battery bank (SUPS) — found DRUPS has a 9-month payback against SUPS on a 1.5 MW system, purely from lower operating cost ($1.84 million versus $5.46 million OpEx), even before counting emissions." — Inverted evidence: The author uses this comparison to argue that data centre backup economics are shifting away from diesel and toward batteries/clean alternatives. However, DRUPS is a diesel-driven generator architecture and SUPS is a battery-based system; citing a 9-month payback and lower OpEx for DRUPS demonstrates the economic superiority of the diesel option over the battery option in that scenario, contradicting the article's core thesis. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Diesel generation costs roughly $0.28 a kilowatt-hour against grid power at $0.085 and solar-charged battery storage at $0.076–0.08." — The article cites these figures from the Takshashila Institution, but the dollar and rupee figures are quoted as sourced and not converted to a common currency, which could lead to confusion or misinterpretation. The methodology differences between national grid-tariff averages and state-specific backup-power models mean these figures should not be directly compared without adjustment. [confidence: high]

- "The Ministry of Power formally built a projection of 13.56 GW of data-centre electricity demand by FY2031–32 into national transmission planning, published via the Press Information Bureau in March 2026." — The article cites this figure as an official government projection, but the source is the Ministry of Power's transmission planning, which may not represent a formal government projection or policy. The PIB release in March 2026 is referenced, but the distinction between transmission planning and formal government projections is not clarified. [confidence: medium]

INTERPRETATION ERRORS:
- "Diesel backup power costs roughly 3x the Indian grid average and 3.5x round-the-clock renewable PPAs — figures the post cites from the Takshashila Institution." — The article uses the cost comparison to argue that diesel is economically unviable for backup power, but it does not account for the operational differences between diesel generators and renewable PPAs. Diesel generators are typically used for short-term backup during outages, while renewable PPAs provide continuous power. The comparison assumes similar usage patterns, which may not hold true in practice. [confidence: high]

- "The DRUPS-vs-SUPS payback comparison is drawn from one vendor/industry source describing a 1.5 MW reference system, not an independently audited multi-project average." — The article uses this single-vendor comparison to generalize about the payback period for diesel vs. battery backup systems in data centers, but it does not address the variability in system sizes, usage patterns, or site-specific conditions that could significantly impact the payback period. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
