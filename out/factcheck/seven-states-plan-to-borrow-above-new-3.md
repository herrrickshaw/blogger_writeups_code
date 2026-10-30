# Fact/interpretation check — seven-states-plan-to-borrow-above-new-3

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/seven-states-plan-to-borrow-above-new-3.html`

Text-SHA1: `84f04dc8ec3f7d40`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The effect is visible in the aggregate. PRS estimates the states’ combined 2025-26 deficit at 3.2% of GSDP including SASCI loans and 2.8% excluding them, a difference of 0.4 percentage points." — The reasoning has a directionality or arithmetic reversal error based on the definitions provided. If SASCI loans are traditional borrowings that are *excluded* when calculating the headline borrowing ceiling (keeping them out of headline numbers), then including them should result in a *higher* deficit figure relative to excluding them. However, if the headline reported deficit is 2.8% and the deficit including SASCI is 3.2%, it means the 0.4 percentage points are *added* to the headline figures due to these loans, which contradicts the earlier statement that the loans "keep about 0.4% of GSDP out of the headline numbers" (implying headline numbers would be 0.4% higher if they were included). If headline figures exclude them and report 2.8%, then including them makes the total 3.2%. The confusion lies in whether 2.8% or 3.2% is the headline number. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 4266, Requested 5414. Please try again in 12.6s. Need more tokens? Upgrade to Dev Tier today at https://conso]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The 16th Finance Commission caps state deficits at 3% of GSDP from 2026-27"* — The 16th Finance Commission’s recommendations cover **2026-31**, not just 2026-27. The 3% limit is explicitly stated as applying to the entire period (2026-31) in its reports. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Seven of 17 budgets plan more [than 3%], seven of the nine states with revised figures overshot last year, and the Centre’s 50-year loans keep about 0.4% of GSDP out of the headline numbers"* — The claim conflates **budgeted deficits (plans)** with **actual overshooting (outcomes)** without clarifying that the 7/9 states overshooting last year is a separate data point from the 7/17 states planning to exceed the limit this year. The 0.4% figure (from SASCI loans) is also presented as a general "headline adjustment," but the article later notes it varies significantly by state (e.g., Meghalaya’s deficit would drop by 4 percentage points if SASCI were counted). The implication that SASCI loans uniformly reduce headline deficits by 0.4% is misleading without context. [confidence: high]

**OUTDATED DATA:**
- *"The Finance Commission put discom debt across states at about 2.3–2.5% of GSDP in 2024-25"* — The 16th Finance Commission’s recommendations (March 2026) explicitly cite **2023-24** as the reference year for discom debt estimates (2.3–2.5% of GSDP). A 2024-25 figure would require checking the **PRS *State of State Finances* report (October 2025) or CRISIL’s latest state finance reviews** for updates. [confidence: high]
