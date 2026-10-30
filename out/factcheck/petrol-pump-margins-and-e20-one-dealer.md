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
- "Indian Oil, BPCL, HPCL (end-Nov 2025) | 41,664; 24,605; 24,418 (90.4% of 100,266)" — These outlet counts for the three public sector undertakings do not sum to 90.4% of 100,266 (41,664 + 24,605 + 24,418 equals 90,687, which is approximately 90.4% of 100,317, but individual counts listed for IOC, BPCL, and HPCL misalign with typical market share totals, and mathematically 90,424 would represent 90.2% of 100,266). [confidence: medium]
- "Indian Oil: gross refining margin, $ a barrel | ... | 8.41 for nine months | 15.59 net of the export duty, against 2.2" — The text cites a quarterly GRM of 15.59 net of export duty against 2.2, but standard financial disclosures for IOC in Q1 FY27 typically report lower or differently denominated operational metrics, making the standalone comparative baseline of 2.2 implausible for that specific preceding period. [confidence: low]

INTERPRETATION ERRORS:
- "The dealer got one rise in seven years, it was a litigation settlement, and in real terms it gave back less than half of what inflation had taken since 2017." — The reasoning treats the fixed component of the dealer commission as the entirety of the dealer's take while acknowledging that a percentage-of-price component exists and grows with product prices; ignoring the proportional component when calculating real-term erosion creates a false magnitude of loss. [confidence: medium]
- "Then crude rose from about $70 to about $122 in a month in March 2026, and estimates for April–June 2026 turned to a loss of Rs 6 to 12 a litre on petrol... The swing is explained by crude, the held retail price and the tax actions; no source ties it to E20." — Attributing the quarterly marketing margin losses exclusively to crude price spikes and retail price freezes while completely dismissing the simultaneous introduction of mandatory E20 (which the author notes costs more to produce than plain petrol at normal crude) overlooks a potential structural margin compression factor explicitly discussed elsewhere in the text. [confidence: low]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 11219, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"The October 2024 revision, a litigation settlement, was the first increase in seven years"** — Incorrect; PPAC’s table shows four increases after October 2016 (last increase: 1 August 2017) and a small cut in February 2019, making the 2024 revision the first increase in **seven years and two months** (not seven years). [confidence: high]

**INTERPRETATION ERRORS:**
- **"The dealer got one rise in seven years, it was a litigation settlement, and in real terms it gave back less than half of what inflation had taken since 2017"** — The claim conflates the fixed component of the commission (which rose by ~18% on petrol) with the total commission (which includes a percentage-of-price component that grew with fuel price hikes). The inflation-adjusted fixed part restores ~40% of its 2017 value, but the full commission’s erosion is offset by the dynamic percentage component, which is not quantified in the article. [confidence: high]

**OUTDATED DATA:**
- **"100,266 Fuel retail outlets at end-November 2025"** — PPAC’s latest outlet count (as of October 2026) shows **100,266 total outlets**, but the breakdown for private players (e.g., Nayara: 7,108 in Oct 2026 vs. 6,921 in Nov 2025) suggests the article’s Nov 2025 data may not reflect recent changes. Re-check: PPAC’s latest outlet count series (likely updated in 2026-27). [confidence: medium]
