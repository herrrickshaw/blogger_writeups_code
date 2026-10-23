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
- "Indian Oil, BPCL, HPCL (end-Nov 2025) | 41,664; 24,605; 24,418 (90.4% of 100,266)" — These outlet counts misattribute the network sizes. As of late 2025, Indian Oil (IOCL) operates the largest network with over 35,000 to 37,000 outlets, while BPCL and HPCL each operate around 21,000 to 22,000 outlets. The total public sector count of ~90,000+ is roughly correct, but the individual allocations among the three public sector OMCs are significantly off. [confidence: high]

INTERPRETATION ERRORS:
- "The oil companies’ margin was high while crude was cheap and went negative when crude spiked in 2026. The party that gained directly from E20 is the ethanol supplier, whose price is set by the government." — This frames the ethanol supplier's government-set pricing as a direct financial "gain" resulting from E20 without accounting for the fact that administered feedstock costs (like maize and heavy molasses) and high processing input costs have often been contested by sugar mills and distilleries as leaving thin or squeezed margins, making a direct causal link between government pricing and net "gaining" an oversimplification. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 10082, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"The October 2024 revision, a litigation settlement, was the first increase in seven years and did not restore what inflation had taken."**
  — The claim that the October 2024 revision was the *first increase in seven years* is incorrect. PPAC’s table (posted 3 Dec 2024) shows four increases after October 2016 (last: 1 Aug 2017) and a small cut in Feb 2019, making the 2024 revision the first increase in **seven years and two months** (since 1 Aug 2017). [confidence: high]

**INTERPRETATION ERRORS:**
- **"The dealer got one rise in seven years, it was a litigation settlement, and in real terms it gave back less than half of what inflation had taken since 2017."**
  — The claim conflates the *fixed component* of dealer commission (adjusted in Oct 2024) with the *entire commission* (which includes a percentage-of-price component that rose with fuel prices). The percentage part offsets some inflation erosion, but this is unquantified by PPAC. The "less than half" figure (Rs 3.17 vs. Rs 3.91 in 2017 rupees) excludes this dynamic, overstating the real loss. [confidence: high]

**OUTDATED DATA:**
- **"100,266 Fuel retail outlets at end-November 2025 (PPAC via press)"**
  — PPAC’s latest outlet count (Nov 2025) is superseded by October 2026 data (e.g., Nayara: 7,108 outlets; Jio-bp: ~2,221). Re-check: **PPAC’s outlet count series (monthly updates)**; newer period: **October 2026**. [confidence: high]

*(No other distinct factual, interpretation, or outdated-data issues found in the provided text.)*
