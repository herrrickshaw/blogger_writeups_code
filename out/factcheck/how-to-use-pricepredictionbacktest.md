# Fact/interpretation check — how-to-use-pricepredictionbacktest

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-pricepredictionbacktest.html`

Text-SHA1: `85f592876952d4e4`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Universe membership uses full-sample dollar volume, a mild lookahead the repo documents." — Using full-sample dollar volume to select a universe introduces survivorship and lookahead bias, which fundamentally distorts backtest validity rather than being a "mild" issue, as it incorporates future information into past selection. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 2903, Requested 5936. Please try again in 6.2925s. Need more tokens? Upgrade to Dev Tier today at https://con]

## Mistral open-mistral-nemo

Here is the structured report based on the provided article text:

---

**FACTUAL ERRORS:**
- **"India breakout-buy bull-regime 21-day excess (t 14.7; was +2.08%)"** — The claim that the "committed files said +2.08%" is misleading because the article itself later states the *fresh replay* results are **+1.66% (t 14.69)**, not +2.08%. The "was +2.08%" appears to be an outdated or conflated reference to the *old committed signals* (from the table below), but the article’s own data shows the *current* value is +1.66%. The inconsistency suggests a failure to clearly distinguish between old and new results.
  [confidence: **high**]

- **"China's panel stops on 1 July 2026, so its numbers did not change"** — While technically true for the *mean excess return* (+2.77%), the **t-statistic (14.05)** remains unchanged because it is derived from the same overlapping-window data. However, the claim implies *no* data update occurred, which is incorrect: the panel’s end date is stale (1 Jul 2026 vs. later dates for other markets), and the article does not explain why China’s data was not refreshed to 21 Oct 2026 like other markets.
  [confidence: **medium**]

---

**INTERPRETATION ERRORS:**
- **"Breakouts earn positive excess only in bull regimes"** — While the data shows bull-regime breakouts have positive excess returns (e.g., +1.66% for India), this claim **overgeneralizes** without acknowledging:
  1. The **t-statistics are optimistic** due to overlapping 21-day windows (explicitly noted in the article), which inflates significance.
  2. The **baseline is frictionless** (no costs, slippage, or borrow fees), so real-world applicability is unproven.
  3. The **universe changes** (e.g., India’s split-adjusted prices vs. raw close) may distort comparability across regimes.
  The conclusion conflates *statistical significance* (t-values) with *economic viability* without addressing these caveats.
  [confidence: **high**]

- **"The repo’s conclusion is modest: daily large-cap returns are close to unpredictable"** — This is a **false causal claim** based on:
  1. The **Markov layer’s role** is framed as a "regime gate," not a forecaster, yet the conclusion treats its directional accuracy (0.528) as evidence of unpredictability *without* comparing it to non-frictionless benchmarks (e.g., transaction costs).
  2. The **LSTM/GRU models underperform naive baselines** in Sharpe (e.g., -0.153 vs. 0.738 for buy-and-hold), but this ignores that neural nets are sensitive to hyperparameters, random initialization, and small sample sizes (the article admits "small differences are not meaningful").
  The conclusion **extrapolates** from backtested, cost-free results to real-world unpredictability without addressing critical frictions.
  [confidence: **high**]

---

**OUTDATED DATA:**
- **"110,852 signals from 2016-09-15 to 2026-07-17 across 1,000 symbols"** — The article later states the *fresh replay* (23 Oct 2026) covers **109,127 signals** (US) and uses a **different universe (989 vs. 1,000 names for India)**. The initial claim is outdated and should reference the **rebuilt panels (last session: 21 Oct 2026 for US, 22 Oct 2026 for India)**.
  [confidence: **high**]

- **"China: +2.77 (14.05) [data ends 1 Jul 2026]"** — The China panel’s end date is **stale** compared to other markets (e.g., US/India/JPN/KR updated to Oct 2026). The source series to re-check is the **author’s OHLCV warehouse** (not publicly available), but the article should note that China’s data is **not current** and may require re-aggregation to match the other markets’ timelines.
  [confidence: **high**]

---
