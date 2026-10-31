# Fact/interpretation check — how-to-use-global-stock-screener-rule

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-global-stock-screener-rule.html`

Text-SHA1: `92c927eb144221c9`

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
- **“Python 3 with pip … (the demo used Python 3.14)”** — Python 3.14 has never been released; the latest stable series as of the training cut‑off is 3.12. The statement is therefore factually incorrect. [confidence: high]  
- **“Piotroski for India caps at 8 because the cache has no gross‑margin field.”** – The Piotroski F‑Score does **not** include a gross‑margin metric; it is based on nine accounting items (ROA, CFO, change in ROA, accruals, etc.). Missing a gross‑margin field cannot limit the maximum score to 8. [confidence: high]  

**INTERPRETATION ERRORS**
- **“Piotroski for India caps at 8 because the cache has no gross‑margin field.”** – This links a missing data column (gross margin) to a lower possible Piotroski score, implying a causal relationship that does not exist. The Piotroski methodology simply omits any test for which data are unavailable, but the score can still reach 9 if the other eight tests are satisfied. The claim therefore misinterprets how the scoring works. [confidence: high]  

**OUTDATED DATA**
- **“The price cache ends between 26 and 30 June 2026.”** – The article was revised on 18 October 2026 and states the cache ends in late June 2026. If the repository has been updated after that date (e.g., a newer cache covering July 2026 onward), the “latest” cache date cited would be outdated. The series to re‑check is the cached price‑data timestamps in the repository’s `cache_seed/` folder; verify whether a more recent cache (e.g., July 2026 or later) exists. [confidence: medium]

## Mistral open-mistral-nemo

Here’s the structured feedback based on the provided article:

---

**FACTUAL ERRORS:**
- *"India it evaluated 16 names and 1 passed (ICICIBANK, 7)"* — The claim that **ICICIBANK scored 7/9 on the Piotroski F-Score** is plausible but contradicts the later caveat: *"Piotroski for India caps at 8 because the cache has no gross margin field."* Since the F-Score requires 9 criteria (including gross margin), a score of 7 is impossible with the available data. The article likely conflated the *maximum possible score* (8) with an actual score. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Coffee Can evaluated 338 US names and 11 passed (for example NVDA, ANET, META)"* — The claim that **NVDA, ANET, and META passed the Coffee Can screen** is unsupported by the later caveat: *"Coffee Can: negative revenue crashes the cagr() calculation (3 US rows crashed)."* If these stocks had negative revenue (or missing fields) in the cache, they would have been excluded, making the claim misleading. [confidence: high]

**OUTDATED DATA:**
- *"The price cache ends between 26 and 30 June 2026"* — No newer official release is cited, but the article was published on **18 October 2026**, suggesting the data is already outdated by ~4 months. The source (cached prices) is not a dynamic dataset (e.g., a live API or updated survey), so no "newer period" exists to re-check. [confidence: high]

---
