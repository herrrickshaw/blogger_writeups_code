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
- "Indian Oil, BPCL, HPCL (end-Nov 2025) | 41,664; 24,605; 24,418 (90.4% of 100,266)" — These outlet counts for Indian Oil, BPCL, and HPCL sum to 90,687, which is roughly 90.5% of the total 100,266, but the individual breakout figures themselves are historically inverted or inaccurate relative to official PSU shares (IOCL is traditionally the largest with roughly half of PSU outlets, around 35,000–36,000 at the time, while BPCL and HPCL have roughly 21,000–22,000 each). [confidence: high]

INTERPRETATION ERRORS:
- "The oil companies’ margin was high while crude was cheap and went negative when crude spiked in 2026. The party that gained directly from E20 is the ethanol supplier..." — The text links the OMCs going into the red strictly to the crude price spike while treating E20 strictly as an ethanol-supplier gain, ignoring the fact that mandatory high-blend ethanol procurement at government-fixed prices higher than prevailing petrol-equivalent energy values acts as a structural margin drain on OMCs when crude prices fluctuate or drop below the crossover threshold. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 8505, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"The October 2024 revision, a litigation settlement, was the first increase in seven years"** — Incorrect timeline; PPAC’s table (posted 3 Dec 2024) shows four increases after Oct 2016 (last before 2024 was 1 Aug 2017), making the 2024 revision the first in **7 years and 2 months**, not 7 years. [confidence: high]

**INTERPRETATION ERRORS:**
- **"The dealer got one rise in seven years, it was a litigation settlement, and in real terms it gave back less than half of what inflation had taken since 2017"** — The claim conflates the fixed commission’s inflation loss (Rs 3.91→Rs 2.69/litre in Dec-2025 ₹) with the percentage component’s growth (which offsets some erosion). The "less than half" figure ignores that the percentage-of-price part (Rs 0.6–0.8/litre) grew with fuel prices, partially compensating for the fixed part’s stagnation. [confidence: high]

**OUTDATED DATA:**
- **"100,266 Fuel retail outlets at end-November 2025"** — PPAC’s latest outlet count (Nov 2025) is superseded by **Oct 2026 figures** (e.g., Nayara: 7,108; Jio-bp: ~2,221) in the article’s own timeline. [confidence: high]
