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
- "Indian Oil, BPCL, and HPCL announced together after a pending case was resolved, with no change in pump prices." — In India, retail selling prices (RSPs) of petrol and diesel are technically deregulated, but OMCs historically coordinate price revisions and major revisions (like the October 2024 dealer commission hike) often coincide with minor retail price adjustments or are absorbed via state-level tax tweaks rather than strictly "no change in pump prices" universally across all circles, though the October 2024 revision specifically saw no immediate hike in base pump prices. However, a more concrete error is the outlet count breakdown: "Indian Oil, BPCL, HPCL (end-Nov 2025) | 41,664; 24,605; 24,418 (90.4% of 100,266)" — summing these three figures gives 90,687, which is roughly 90.4% of 100,266, but the individual numbers assigned to IOCL, BPCL, and HPCL are transposed or inaccurate for standard public-sector counts (IOCL alone typically operates around 35,000–36,000 outlets, not 41,664 while BPCL and HPCL have ~21,000–22,000 each). [confidence: medium]

INTERPRETATION ERRORS:
- "The party that gained directly from E20 is the ethanol supplier, whose price is set by the government." — This is a false causal/beneficiary claim in an economic sense because while ethanol suppliers receive guaranteed off-take volumes and government-fixed prices, they face heavily regulated input costs (such as cane and maize prices fixed by state/central governments) and capacity constraints, meaning higher gross revenue from E20 does not automatically translate to a net margin "gain" superior to other agricultural or industrial diversions without factoring in feedstock cost inflation. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 9102, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"The October 2024 revision, a litigation settlement, was the first increase in seven years"** — Incorrect; PPAC’s table (posted 3 Dec 2024) shows four increases after Oct 2016 (last before 2024 was 1 Aug 2017), making the 2024 revision the first in **7 years and 2 months** (not 7 years). [confidence: high]

**INTERPRETATION ERRORS:**
- **"The dealer got one rise in seven years, it was a litigation settlement, and in real terms it gave back less than half of what inflation had taken since 2017."**
  The claim conflates the **fixed component** (revised in Oct 2024) with the **percentage-of-price component** (which grew with inflation). The fixed part alone restored ~40% of its 2017 value (in Dec 2025 ₹), but the percentage component offset some erosion. The article’s inflation-adjusted calculation excludes this offset, overstating the "loss." [confidence: high]

**OUTDATED DATA:**
- **"100,266 Fuel retail outlets at end-November 2025"** — PPAC’s latest outlet count (as of Oct 2026) shows **100,266 total outlets**, but the breakdown for private players (e.g., Nayara: 7,108 in Oct 2026 vs. 6,921 in Nov 2025) suggests the Nov 2025 figure may be outdated. Re-check: PPAC’s **annual outlet census** (likely FY26-27, released post-Oct 2026). [confidence: medium]
