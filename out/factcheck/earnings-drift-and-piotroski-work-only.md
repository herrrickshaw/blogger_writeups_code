# Fact/interpretation check — earnings-drift-and-piotroski-work-only

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/earnings-drift-and-piotroski-work-only.html`

Text-SHA1: `f86c997c8c00dcbd`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The Piotroski premium follows illiquidity, not company size. Among thinly traded large companies, strong F-scores beat weak ones by 31 percentage points over a year." — The reasoning jumps from a correlation or categorization of stocks to a causal claim about "illiquidity" creating the premium, while glossing over the fact that large, thinly traded companies in the US represent an idiosyncratic, distressed, or highly distressed niche (such as micro-caps or companies facing severe structural decline) rather than a general liquidity effect. The massive spread (−24.6% for weak firms) reflects distress risk and credit/bankruptcy factors rather than pure trading friction. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 3990, Requested 6804. Please try again in 20.955s. Need more tokens? Upgrade to Dev Tier today at https://con]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Indian large caps hold about 20 percent of their capital employed as cash, against about 9 percent for small caps"* — This claim is **implausible** for India’s large-cap universe (e.g., Reliance, HDFC Bank, TCS) and contradicts known data. Large Indian firms typically hold **<10% cash as a % of capital employed** (e.g., S&P BSE 500 large-cap median cash ratio is ~5–8% post-2020; see [CEIC/IBEF data](https://www.ibef.org/)). Small caps may hold slightly more due to lower liquidity, but the reversal (20% vs. 9%) is inconsistent with sectoral benchmarks (e.g., IT services cash ratios hover near 0–5%). [confidence: high]

**INTERPRETATION ERRORS:**
- *"Adding return on capital to Piotroski picks better businesses without picking better stocks"* — The claim conflates **business quality** (ROCE) with **stock returns**. While ROCE *identifies* better businesses (as shown in the India sample), the US test explicitly shows that **high-ROCE stocks are already priced into the market** (returns equal or worse than the broad index). The "better businesses" narrative ignores that the F-score + ROCE strategy **underperformed the market in liquid US stocks**, suggesting the combination doesn’t outperform *as stocks*—only as a filter for quality. The gap is that the article treats ROCE as a standalone signal when its marginal utility depends on market efficiency. [confidence: high]

**OUTDATED DATA:**
- *"Piotroski premium in large, thinly traded US stocks (provisional): +31.4 pp"* — The article notes the figures are **provisional and subject to regeneration** due to data defects (e.g., revenue understatement). The latest **SEC EDGAR filings** (as of 2026) and **CRSP/Compustat updates** (e.g., 2025 fiscal years) would supersede this. Re-check the **Piotroski × liquidity repository** for the 2025 rebalances; the author’s note implies the +31.4pp figure is from an interim run. [confidence: high]

---
**Note:** The article’s disclaimers (e.g., "provisional," "cannot currently be re-run") flag these as temporary gaps, but the claims themselves are actionable for readers. No other categories had clear violations.
