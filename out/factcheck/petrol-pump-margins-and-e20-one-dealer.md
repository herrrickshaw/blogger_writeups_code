# Fact/interpretation check — petrol-pump-margins-and-e20-one-dealer

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/petrol-pump-margins-and-e20-one-dealer.html`

Text-SHA1: `ae7efac7b1545cff`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Indian Oil, BPCL, HPCL (end-Nov 2025) | 41,664; 24,605; 24,418 (90.4% of 100,266)" — The sum of 41,664 (IOC), 24,605 (BPCL), and 24,418 (HPCL) is 90,687, which is approximately 90.4% of 100,266, but the text attributes the second figure (24,605) to BPCL and the third to HPCL when typically BPCL has the larger network or the counts are transposed in this specific breakdown against standard PSU outlet distributions. [confidence: medium]

INTERPRETATION ERRORS:
- "The oil companies’ margin was high while crude was cheap and went negative when crude spiked in 2026." — Marketing margins and refining margins are conflated or simplified into a single "oil companies' margin" that supposedly goes negative, whereas integrated OMCs typically experience sharp compression in marketing margins during retail price freezes while gross refining margins (GRMs) can remain robust or positive (as explicitly documented later in the text where HPCL and BPCL report massive positive GRMs of $17 to $41 during the exact same quarters they record net losses). [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 10107, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"The October 2024 revision, a litigation settlement, was the first increase in seven years"** — Incorrect; PPAC’s table (posted 3 Dec 2024) shows four increases after Oct 2016 (last before 2024 was 1 Aug 2017), making the 2024 revision the first in **7 years and 2 months** (not "seven years"). [confidence: high]

**INTERPRETATION ERRORS:**
- **"The dealer got one rise in seven years, it was a litigation settlement, and in real terms it gave back less than half of what inflation had taken since 2017"** — Misleading causal claim. The Rs 0.52/litre increase (Oct 2024) was a litigation settlement but unrelated to E20 (launched Feb 2023). Inflation erosion (45.3% since Aug 2017) is correctly noted, but the claim conflates the timing of the revision with E20’s impact, ignoring other factors (e.g., supply cuts, UPI fees) squeezing dealer margins. [confidence: high]

**OUTDATED DATA:**
- **"100,266 Fuel retail outlets at end-November 2025"** — PPAC’s latest outlet count (Nov 2025) is superseded by **Oct 2026 data** (e.g., Nayara: 7,108 outlets; Jio-bp: ~2,221). Re-check: [PPAC’s updated outlet data series](https://ppac.gov.in) for FY27 figures. [confidence: high]
