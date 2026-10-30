# Fact/interpretation check — india-got-record-945-billion-of-fdi

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-got-record-945-billion-of-fdi.html`

Text-SHA1: `910e1d000f233f00`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Net FDI, which helps pay for the current-account deficit, has fallen from about $43 billion a year to single digits." — In India's balance of payments accounts, Foreign Direct Investment (FDI) inflows are recorded *net* of repatriation by convention (gross foreign investment into India minus disinvestment/repatriation by foreign direct investors). The article treats the RBI's standard net foreign investment figure as if it includes outward FDI by Indian companies, and then subtracts outward FDI a second time to calculate a new "Net FDI" metric, creating a double-subtraction of outward investment. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 5272, Requested 5753. Please try again in 22.6875s. Need more tokens? Upgrade to Dev Tier today at https://co]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Net FDI was about $43 billion a year [in 2019-20 and 2020-21]"* — The article’s own table shows **$43.0 bn in 2019-20** and **$44.0 bn in 2020-21**, not "about $43 billion a year" (which implies a rounded average). The phrasing conflates the two years’ distinct figures. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Indian companies’ investment abroad also climbed, from $13 billion to $33 billion a year, and in 2024-25 it alone absorbed 36% of gross inflow"* — While the $13 bn→$33 bn increase is correct, the claim that **outward FDI "absorbed" 36% of gross inflow in 2024-25** conflates two distinct flows: (1) **repatriation by foreign investors** (51.5 bn, 64% of gross) and (2) **Indian outward FDI** (29.2 bn, 36% of gross). The latter does not "absorb" inflow but represents a separate outflow. The wording misleads readers into thinking outward FDI offsets gross inflow, when it actually compounds the net outflow. [confidence: high]

**OUTDATED DATA:**
- *"Net FDI in 2024-25 was $0.35 billion"* — The article notes that a **later report revised 2024-25 net FDI to about $1 billion**, and the 2025-26 figures are also provisional (reported in May 2026). The claim should specify that these are preliminary estimates subject to revision. [confidence: high]
- *"2023-24 outward FDI is a residual, not a published number"* — The article acknowledges this but does not flag that **RBI’s 2023-24 balance-of-payments data (published in May 2024) likely includes a definitive outward FDI figure**, which the blog’s residual calculation may not fully align with. [confidence: medium]
