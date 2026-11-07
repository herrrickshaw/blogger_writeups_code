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
- "+1.66% India breakout-buy bull-regime 21-day excess (t 14.7; was +2.08%)" — The article compares the fresh replay result (+1.66%) directly against the committed file result (+2.08%) while noting that the underlying panel changed (using split-adjusted prices and a different number of symbols), making this an apples-to-oranges comparison that attributes a data revision difference to a pure temporal or model update. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- none found  

**INTERPRETATION ERRORS:**  
- **Claim:** “*daily large‑cap returns are close to unpredictable, and the Markov layer is useful as a regime gate rather than a forecaster.*”  
  **Reasoning gap:** The article’s evidence consists of 21‑day excess‑return statistics for breakout signals and model‑level Sharpe ratios, not a direct test of the predictability of *daily* returns. Moreover, the Markov model’s Sharpe (0.736) is essentially identical to the buy‑and‑hold Sharpe (0.738), providing little support for the assertion that the Markov regime gate adds value. The conclusion extrapolates from a specific 21‑day signal‑based back‑test to a broader claim about daily return predictability and the utility of the Markov gate, which the presented data do not substantiate. [confidence: high]  

**OUTDATED DATA:**  
- **Claim:** “*China’s panel stops on 1 July 2026, so its numbers did not change.*”  
  **Series to re‑check:** The China OHLCV panel used for the replay (reports/replay_signals_cn.parquet). Since the article was published on 23 October 2026, a more recent data cut‑off (e.g., up to at least 23 Oct 2026) is likely available and would affect the reported excess‑return and t‑statistics. [confidence: medium]

## Mistral open-mistral-nemo

Here is the structured report based on the provided article text:

---

**FACTUAL ERRORS:**
- **"India breakout-buy bull-regime 21-day excess (t 14.7; was +2.08%)"** — The article claims the *fresh* re-run result is **+1.66%** (t 14.69) for India, but the headline still cites the *old* **+2.08%** (t 17.58) as a comparison, creating a misleading contrast. The newer data (22 Oct 2026) explicitly shows **+1.66%**, not **+2.08%** [confidence: **high**].

---

**INTERPRETATION ERRORS:**
- **"The repo’s conclusion is modest: daily large-cap returns are close to unpredictable, and the Markov layer is useful as a regime gate rather than a forecaster."** — The conclusion conflates two distinct claims:
  1. **Forecasting accuracy**: The Markov model’s directional accuracy (0.528 vs. naive baselines) is *slightly* better than random but not meaningfully so (e.g., Sharpe ratios match buy-and-hold). This suggests *no* predictive edge, not "close to unpredictable."
  2. **Regime-gating utility**: The Markov layer *does* filter breakout signals (e.g., bull-regime breakouts earn +1.66% in India), but this is a *conditional* edge, not a general forecasting claim. The article conflates these as equivalent [confidence: **high**].

- **"Overlapping 21-day windows make the clustered t-statistics optimistic"** — While true for *within-sample* t-stats, the article does not acknowledge that the **fresh re-run t-values (e.g., India: t 14.69)** are still inflated due to:
  - **Autocorrelation in returns** (common in financial time series), which t-stats clustered by date do not fully address.
  - **No adjustment for multiple testing** across signals/trends (e.g., 6 groups in the India table), inflating the effective significance [confidence: **high**].

---

**OUTDATED DATA:**
- **"China’s panel stops on 1 July 2026 (stale, identical)"** — The article notes China’s data is unchanged but does not prompt readers to check for:
  - **Newer official releases** (e.g., SSE/NSE updates post-July 2026) or
  - **Split-adjusted data** (like India), which may now be available for China (e.g., from Wind Info, Bloomberg, or local exchanges). The claim assumes no updates, but the repo’s disclaimer about "local warehouse copy" suggests potential gaps [confidence: **medium**].

---
**Note**: No stylistic or formatting issues were flagged as per instructions. The article’s core methodological caveats (costs, lookahead, frictionless P&L) are correctly disclosed, but the gaps above warrant correction for accuracy and rigor.
