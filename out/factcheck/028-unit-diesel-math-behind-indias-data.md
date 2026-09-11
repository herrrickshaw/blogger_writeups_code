# Fact/interpretation check — 028-unit-diesel-math-behind-indias-data

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/028-unit-diesel-math-behind-indias-data.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Diesel generation costs roughly $0.28 a kilowatt-hour against grid power at $0.085 and solar-charged battery storage at $0.076–0.08." — The $0.076–0.08/kWh (or $0.076–0.112/kWh) figure is the cost of round-the-clock (RTC) renewable PPAs, not solar-charged battery storage. As the article's own chart and Section 2 table note, that range applies to RTC renewable PPAs; levelised cost of solar-charged BESS is given in Section 2 as ₹39.71–61.72/kWh (roughly $0.48–0.74/kWh), which is several times higher. [confidence: high]
- "a five-fold expansion of telecom tower sites for 5G" — The article's own cited numbers state that India's telecom tower base needs to grow from roughly 750,000 to around 1.2 million (an addition of ~450,000 towers). That represents an increase of 60% (a 1.6-fold total), not a five-fold (5x) expansion. [confidence: high]

INTERPRETATION ERRORS:
- "The economics inside that design standard are already shifting, though. A straight comparison of two backup architectures — Diesel Rotary UPS (DRUPS, which uses flywheel kinetic energy) against Static UPS with a battery bank (SUPS) — found DRUPS has a 9-month payback against SUPS on a 1.5 MW system, purely from lower operating cost ($1.84 million versus $5.46 million OpEx), even before counting emissions." — DRUPS stands for Diesel Rotary UPS; it relies on an integrated diesel engine. Citing a study where DRUPS outperforms battery-based Static UPS (SUPS) on OpEx and payback does not show that the economics are shifting away from diesel; it demonstrates that a diesel-driven system was found to be more economical than a battery-backed alternative. [confidence: high]
- "Diesel backup power costs roughly 3x the Indian grid average and 3.5x round-the-clock renewable PPAs — figures the post cites from the Takshashila Institution." — This is an apples-to-oranges comparison used to argue that the economics of backup power are tipping against diesel. Grid tariffs and RTC renewable PPAs represent baseload, continuous utility power. Diesel generators are installed for emergency backup during outages, where low utilization inherently drives up the levelised cost per unit generated. A lower grid or PPA per-unit rate does not demonstrate that diesel backup is economically unviable, because grid power cannot supply a facility when the grid fails. [confidence: high]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- “India’s telecom tower base needs to grow from roughly **750,000 towers** already in place to around 1.2 million…” — Industry data (TRAI, TowerXchange) place the current tower count at **≈ 600 k** (2023‑24), not 750 k. The figure appears overstated. [confidence: medium]  
- “PNGRB had authorised **307 geographical areas by 2026**, reaching close to 100 % of India’s landmass outside the islands…” — The 307‑area count was **recorded in March 2023**; the article projects it to 2026 without a source, making the statement unverifiable and likely inaccurate. [confidence: medium]  

**INTERPRETATION ERRORS**  
- “Diesel generation runs about **$0.28 per kWh**, against an Indian grid average of **$0.085/kWh** and round‑the‑clock renewable PPAs of **$0.076–0.112/kWh**…” — This compares the **per‑kWh cost of a rarely‑used backup generator** with the **per‑kWh cost of continuous grid or renewable supply**. Because diesel generators operate at a very low capacity factor, the cost per kWh of *energy actually delivered* is not directly comparable to base‑load tariffs; the claim overstates the economic disadvantage of diesel as a backup. [confidence: high]  
- “Telecom tower diesel‑elimination figures … are a **precedent** for data‑centre backup‑power decisions.” — The article infers that data‑centres will follow the telecom sector’s diesel‑phase‑out, but provides no evidence that data‑centre operators face the same cost‑or‑reliability incentives, nor that their load profiles and regulatory constraints are comparable. The causal link is therefore speculative. [confidence: medium]

## Mistral mistral-small-latest

[Mistral API error 429: {"object":"error","message":"Rate limit exceeded","type":"rate_limited","param":null,"code":"1300","raw_status_code":429}]
