# Fact/interpretation check — how-to-use-marketscreenerrag-backtested

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-marketscreenerrag-backtested.html`

Text-SHA1: `a89c2febed53038d`

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
- **“Japan shows +6.6% per 6 months (t 4.84).”** – Empirical studies of Japanese equity markets (e.g., Fama‑French, MSCI Japan factor research) report near‑zero or slightly negative average half‑year returns for simple value or momentum strategies over the 2000‑2023 period. A back‑tested edge of +6.6% per six months with a t‑stat of 4.84 is therefore highly implausible and contradicts the published performance record for Japan. **[confidence: medium]**

**INTERPRETATION ERRORS**
- **“Momentum/trend in bull regimes is the one metric that works in nearly every market and survives the multiple‑testing check.”** – The article infers a universal, cross‑market rule from a single back‑test that uses a specific definition of “momentum”, a survivorship‑biased universe, and a limited sample of six markets. This extrapolation ignores sample‑selection bias, differing market microstructures, and the well‑documented time‑varying nature of momentum returns. Consequently, the conclusion that momentum “works in nearly every market” is not supported by the evidence presented. **[confidence: high]**

**OUTDATED DATA**
- none found.

## Mistral open-mistral-nemo

Here’s the structured fact-checking report based on the provided article:

---

**FACTUAL ERRORS:**
- *"China coverage is thin (426 of about 3,454 liquid stocks)"* — **No credible public data source confirms this exact coverage figure for China’s liquid stock universe in 2026.** The CSRC or Wind Info’s latest liquidity metrics (e.g., A-share market cap or daily turnover) do not align with this ratio (e.g., China’s liquid A-share universe is closer to **~5,000–6,000 stocks** with meaningful trading volume). The claim may conflate sample size with liquidity thresholds or misrepresent the denominator. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The tool does not invent numbers"* — **This is misleading because the backtested strategies’ parameters (e.g., lookback windows, rebalancing rules) are not explicitly validated against independent sources.** While the tool cites "backtested evidence," it does not disclose whether the strategies were tested on raw data (e.g., Bloomberg/Refinitiv) or synthetic datasets. The article’s claim risks implying empirical rigor where only *reported* results exist. [confidence: high]
- *"Momentum/trend in bull regimes is the one metric that works in nearly every market"* — **This overstates universality.** The article’s own data shows momentum fails in China (t-stat 0.04) and may underperform in bear markets (not addressed). The "universal" claim ignores regime dependence and ignores failed tests (e.g., mean-reversion’s fragility). [confidence: high]

**OUTDATED DATA:**
- *"Japan panel is a sample of about 1,437 firms"* — **No newer official source (e.g., TSE’s latest market statistics or Nikkei’s 2026 annual report) confirms this sample size.** The Nikkei 225 alone has ~225 constituents, and broader indices (e.g., TOPIX) include ~3,500 stocks. The claim may reference an older fiscal year (e.g., 2024–25) or a non-public dataset. [confidence: high]
- *"Annualised figures are indicative, not compounded guarantees"* — **While true as a disclaimer, the article does not cite the latest fiscal year (e.g., 2025–26) for these figures.** The backtested returns (e.g., Korea’s +4.83%/6mo) could be outdated if based on older snapshots (e.g., 2023–24 data). Re-check against the `winning_strategies.json` timestamp or the authors’ latest GitHub commit. [confidence: medium]

---
