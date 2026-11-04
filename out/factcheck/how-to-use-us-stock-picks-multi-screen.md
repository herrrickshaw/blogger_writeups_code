# Fact/interpretation check — how-to-use-us-stock-picks-multi-screen

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-us-stock-picks-multi-screen.html`

Text-SHA1: `deb1edbf020b3917`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “the full 7,500‑stock universe was not scanned.” — The commonly accepted size of the U.S. equity universe (excluding ETFs) is roughly 5 000–6 000 listed stocks. A figure of 7 500 is inflated and does not match standard market data. [confidence: medium]

**INTERPRETATION ERRORS**
- “It replaces juggling separate screens: one run gives a sector‑capped shortlist, a full ranked CSV and a paper‑portfolio file with transparent screen hits for each name.” — The package does **not** perform the underlying factor calculations (Darvas, Piotroski, Magic Formula, etc.); it merely consumes a pre‑generated scan workbook that already contains those screen results. Therefore it does not truly eliminate the need for separate screen implementations, making the claim of “replacing” them misleading. [confidence: high]

**OUTDATED DATA**
- none found

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- **"The universes differ by design (300 versus 5,814), so the counts are not comparable."**
  — The claim conflates *universe size* (300 vs. 5,814) with *ranked stock counts* (181 vs. 721) as if they are directly comparable after filtering. While the universe size is explicitly narrowed (e.g., liquidity gate, sector caps), the *ranked counts* are still influenced by the same screening logic (e.g., conviction thresholds, missing data handling). The "not comparable" framing ignores that the 300-universe run used the same screening weights/configuration (e.g., CORE score ≥48, ≥2 screens passed) as the 5,814-universe run, just on a subset of stocks. The difference in ranked counts (181 vs. 721) is partly due to the smaller universe but also reflects the absence of the *Quality* and *Actionable* screens in the 300-run, which likely contributed to higher ranked counts in the 5,814-run. [confidence: high]

OUTDATED DATA:
- none found
