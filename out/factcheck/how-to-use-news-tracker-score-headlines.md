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
- "Python 3.14.7" — Python 3.14 has not reached version 3.14.7 as of current release schedules (Python 3.14 is scheduled for release in late 2025, and minor patch versions progress much more slowly). [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 4256, Requested 4236. Please try again in 3.69s. Need more tokens? Upgrade to Dev Tier today at https://conso]

## Mistral open-mistral-nemo

Here’s the structured report based on the provided article text:

---

**FACTUAL ERRORS:**
- **"Darvas picks were covered 7.7% of the time (26 of 339, lift 1.90) and Piotroski 1.2% (4 of 334, lift 0.30)."** — The claim that **Darvas picks had a "lift" of 1.90** and **Piotroski picks a lift of 0.30** is **implausible** for two reasons:
  1. **Lift ratios** (coverage rates relative to a baseline) typically range between **0 and 1** (or 0%–100%) when comparing to a broader universe (e.g., market-wide coverage). A lift of **1.90** would imply the strategy was covered **190% of the time**, which is impossible unless the baseline is zero (unlikely for a stock-screening strategy).
  2. **Piotroski’s F-score** (a widely used fundamental screening metric) is not a coverage metric—it’s a **0–9 score** for individual stocks, not a percentage of news coverage. The article conflates two unrelated concepts.
  [confidence: **high**]

- **"The demo used Python 3.14.7 with pytest 9.1.1."** — **Python 3.14.7 does not exist** (as of October 2026; the latest stable Python version is 3.12.x). This is a **typo or hallucination** in the article.
  [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- **"Absence of coverage is not good news."** — While this is a **true statement** (lack of news can signal low liquidity or indifference), the article **overgeneralizes** this to imply that **20 of 30 picks having "no news"** is inherently problematic for the tracker’s validity. The gap in reasoning is:
  1. **No news ≠ bad signal**: Some strategies (e.g., deep-value picks) may legitimately have **low media attention** without being "bad" stocks. The tracker’s purpose is to **measure attention**, not profitability or quality.
  2. **Double-counting bias**: The article later notes **"loose matches"** (e.g., ARVINDFASN/AARNAV headlines), suggesting the **no-news category may include false negatives** (missed matches) rather than true absence of coverage. The claim conflates **data gaps** with **strategic irrelevance**.
  [confidence: **high**]

- **"The strategy validation report does not show whether any strategy is profitable."** — This is **correct**, but the article **misleads by implying causality** between news coverage and returns. The reasoning gap is:
  1. The tracker **measures attention**, not **predictive power**. Even if Darvas/Piotroski stocks had high coverage, this does not prove the strategies are profitable—it only shows **attention patterns**.
  2. **Correlation ≠ causation**: The article does not address whether **covered stocks outperformed** or if coverage **led** to price moves. The claim **extrapolates** from a descriptive metric (coverage %) to an inferential one (profitability).
  [confidence: **high**]

---

**OUTDATED DATA:**
- **"440 rows in the India validation history (27 Aug to 17 Oct)"** — The date **17 Oct 2026** is **future-dated** (as of this response’s cutoff). While the article is marked **"Revised 18 October 2026"**, the **validation history period (Aug–Oct 2026)** is **not verifiable** in public sources. Readers should:
  - Check the **GitHub repo’s `market-pipeline` folder** for updated CSVs (e.g., `strategy_news_validation_history.csv`).
  - Confirm if the **latest fiscal year** (e.g., FY2026–27) or **survey round** (e.g., RBI’s latest financial stability report) supersedes this snapshot.
  [confidence: **medium**]

- **"The news_pipeline_results folder was empty, so live runs were not performed."** — This is a **demonstration limitation**, but the article does not clarify whether:
  - The **saved reports (e.g., `news_convergence.csv`)** are from a **specific date** (e.g., 2025) or a **placeholder**.
  - The **latest RSS feeds** (from Moneycontrol/ET) or **API sources** (e.g., Marketaux) have been updated since the demo.
  **Action**: Cross-check the **GitHub repo’s `reports/` directory** for newer crawls or the **pipeline’s last commit date**.
  [confidence: **medium**]

---
**Note**: No stylistic or minor formatting issues were flagged per instructions. The article’s **technical accuracy** relies heavily on the **GitHub repos’ current state**, which may have evolved post-2026.
