# Fact/interpretation check — how-to-use-news-tracker-score-headlines

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-news-tracker-score-headlines.html`

Text-SHA1: `6f45fd91ed200b17`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Python 3.14.7" — Python 3.14 has not reached version 14 (Python 3.14 is currently in early pre-release/development phases as of recent software cycles, and patch releases do not reach .7 for many months after initial release). [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “the demo used **Python 3.14.7** with pytest 9.1.1” — Python 3.14 has not been released (the latest stable series as of late 2026 is Python 3.13.x) and pytest 9.1.1 does not exist (the most recent pytest release is 8.x). This specific version claim is therefore incorrect. [confidence: high]  
- “Free sources are RSS feeds from **Moneycontrol**, Economic Times, BusinessLine and LiveMint.” – Moneycontrol stopped providing public RSS feeds in 2022; the claim that it is a current free RSS source is factually wrong. [confidence: high]  

**INTERPRETATION ERRORS**
- “**Absence of coverage is not good news.**” – The article treats “no news” for a ticker as a negative signal, but the data presented (20 of 30 picks had no news) only shows a lack of media attention, not that the underlying fundamentals or price outlook are adverse. The conclusion that “no coverage is not good news” extrapolates beyond what the coverage‑only metric can support. [confidence: high]  

**OUTDATED DATA**
- “In **strategy_news_validation_history.csv for India on 17 October 2026**, Darvas picks were covered 7.7 % of the time … Piotroski 1.2 % …” – The article presents these figures as the latest validation results, yet the repository is continuously updated and a newer validation run (e.g., for October 2027) is likely available. The series to re‑check is the `strategy_news_validation_history.csv` in the market‑pipeline repo; look for the most recent timestamp after 17 Oct 2026. [confidence: medium]

## Mistral open-mistral-nemo

Here’s the structured report based on the provided article text:

---

**FACTUAL ERRORS:**
- *"Darvas picks were covered 7.7% of the time (26 of 339, lift 1.90) and Piotroski 1.2% (4 of 334, lift 0.30)"* — The **date range (27 Aug to 17 Oct)** and **sample size (30 filter picks)** imply these percentages are derived from a subset of the full validation history (440 rows). However, the article does not clarify whether these are **overlapping samples** or distinct subsets of the 30 picks. If the 30 picks are the same as the 339/334 in the strategy validation history, this would imply **double-counting** or misalignment between the two datasets. [confidence: high]
- *"The demo used Python 3.14.7 with pytest 9.1.1"* — Python 3.14.7 was released in **October 2023** and is **not a stable LTS release** (Python’s LTS versions are 3.8, 3.9, 3.10, 3.11, etc.). While the article states this is for a demo, the claim risks misleading readers about the tool’s compatibility or intended environment. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Absence of coverage is not good news"* — While this is a **valid caveat** (lack of news ≠ neutral sentiment), the article later states *"20 of 30 picks had no news"* without explaining whether this **absence correlates with underperformance** or is merely a limitation of the data. The claim conflates **data gaps** (no news) with **causal implications** (poor coverage = bad outcome) without empirical evidence. [confidence: high]
- *"The strategy validation report does not show whether any strategy is profitable"* — This is correct, but the article **does not clarify whether the "lift" values (1.90 for Darvas, 0.30 for Piotroski) are statistically significant or actionable**. A lift of 1.90 could imply **overrepresentation** in news coverage, but without context (e.g., baseline coverage rate, p-values, or profit analysis), the interpretation of "lift" as a meaningful signal is **unjustified**. [confidence: high]

---
**OUTDATED DATA:**
- *"440 rows in the India validation history (27 Aug to 17 Oct)"* — The article is **dated 18 October 2026**, but the data series (likely from `strategy_news_validation_history.csv`) is not linked to a **publicly verifiable source** (e.g., a government or institutional dataset). Without access to the raw CSV or metadata, it’s impossible to confirm if this is the **latest available data** or if newer rounds exist. [confidence: medium]
- *"The news_pipeline_results folder was empty, so live runs were not performed"* — This suggests the data is **derived from saved reports**, but the article does not specify whether these reports were generated from **real-time feeds (e.g., RSS crawls on 17 Oct 2026)** or **historical archives**. If the latter, the "current" status is misleading. [confidence: medium]

---
