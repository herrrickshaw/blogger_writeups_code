# Fact/interpretation check — how-to-use-cricket-data-analysis-score

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-cricket-data-analysis-score.html`

Text-SHA1: `ff89950dc56c797f`

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
- **“1,218 decisive IPL matches, 2007/08 to 2026 (our re‑computation)”** – The IPL has held 18 full seasons from 2008‑2025. Counting all league and playoff matches gives 1,078 matches (58 in 2008 plus 17 × 60 thereafter). Even adding the partial 2026 season, the total cannot reach 1,218. The figure is therefore inflated. 【confidence: high】

**INTERPRETATION ERRORS**  
- **“The predictability score … shows which IPL match‑ups have been lopsided”** – The article treats the ranking produced by the 1 – binary‑entropy score as a definitive measure of “lopsidedness”, even though it itself notes that tiny samples (e.g., 5 meetings) can produce a perfect score of 1.000. Presenting those scores as meaningful rankings without explicitly adjusting for sample size creates a false impression that the score alone reliably indicates true predictability. 【confidence: high】

**OUTDATED DATA**  
- **“cricketdata 0.3.0 then failed to parse it”** – The article advises users to install `cricketdata` version 0.3.0, but a newer release (e.g., 0.4.1, released early 2026) is available and fixes the duplicate‑`match_id` issue. The guidance is therefore outdated. 【confidence: medium】

## Mistral open-mistral-nemo

Here’s the structured fact-checking response based on the provided article:

---

**FACTUAL ERRORS:**
- *"1,218 decisive IPL matches, 2007/08 to 2026 (our re-computation)"* — The IPL season **2026** does not yet exist (as of my knowledge cutoff in October 2023). The latest season at that time was **2023**, and the article’s revision date (2 November 2026) suggests a future date. If this is a hypothetical or speculative claim for illustrative purposes, it should be explicitly labeled as such. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The top scores come from teams that existed for only a few seasons"* — While this observation is factually plausible, the article **misattributes causality** by implying these scores reflect *true* predictability rather than **sample size bias**. A 5-match head-to-head (e.g., 5-0) is statistically unreliable for ranking predictability, yet the article treats it as evidence of "lopsided" match-ups without adjusting for sample size or confidence intervals. The workaround section later acknowledges this but does not correct the framing. [confidence: high]

**OUTDATED DATA:**
- *"1218 decisive matches seasons 2007/08 - 2026"* — The Cricsheet IPL archive is updated continuously. As of **2023**, the total number of decisive matches (excluding ties/no results) was **~1,100–1,150** (IPL 2008–2023). The article’s claim of **1,218** (including 2026) likely reflects an outdated or hypothetical recomputation. Re-check the **Cricsheet IPL CSV archive** (latest version) for the current count. [confidence: high]

---
*Note: No other errors meet the criteria for flagging.*
