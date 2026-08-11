# Fact/interpretation check — why-bet-on-one-horse-when-you-can-buy

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/why-bet-on-one-horse-when-you-can-buy.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "this article built an equal-weighted portfolio for each band — buy one unit of every stock in the band, nothing else" — Buying one share ("one unit") of each stock creates a price-weighted portfolio (similar to the Dow Jones Industrial Average), not an equal-weighted portfolio. An equal-weighted portfolio allocates equal monetary capital to each stock, whereas buying one unit gives higher-priced stocks a larger weighting in the portfolio than lower-priced ones. [confidence: high]

INTERPRETATION ERRORS:
- "at 1,987 constituent stocks it is, by a wide margin, the most internally diversified portfolio in this table" — The article uses the raw count of stocks to claim the under-₹1,000 band is the most diversified. However, because the portfolio is price-weighted (buying one share of each stock), capital allocation is heavily skewed toward higher-priced stocks within the band (for example, a ₹900 stock gets 900 times the portfolio weighting of a ₹1 penny stock). Raw stock count does not measure effective diversification when individual position weights are heavily unequal. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Harry Markowitz's 1952 mean-variance framework" — The mean-variance framework was indeed introduced by Harry Markowitz, but the specific date of publication is 1952 for the paper "Portfolio Selection" in the Journal of Finance, which is correct. However, the claim that this is the basis for how Indian mutual-fund researchers evaluate real portfolios might be too broad or not verifiable without more specific information on current practices in India [confidence: medium].
- "Desai, Pranjal & Vaidya, Mansi. 'To Build Portfolios Using Markowitz Model with Evaluation of Performance of Mutual Fund in India.' International Journal of Creative Research Thoughts (IJCRT), Vol. 6, Issue 1, March 2018" — Without access to the specific journal or database, it's difficult to verify the existence, volume, issue, and date of this publication, which could be a factual error if the details are incorrect [confidence: medium].

INTERPRETATION ERRORS:
- "The above-₹10,000 portfolio has the best Sharpe ratio (2.27) of the five — 'very good' on the ranges above — combining the highest return with volatility no higher than the cheaper bands" — This statement might imply a causal relationship between the price band and the Sharpe ratio, which is not necessarily supported by the data. The better Sharpe ratio of the above-₹10,000 portfolio could be due to various factors other than the price band itself [confidence: high].
- "A professionally run mutual fund scheme is doing something a price filter cannot — actively weighing sector exposure, company quality, valuation and correlation between holdings" — This statement compares the outcomes of price-filtered portfolios with professionally managed mutual funds without considering that the latter's performance could be influenced by factors not directly related to the filtering method, such as management fees, trading costs, and the skill of the fund managers [confidence: medium].

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "the same five price bands from this blog's earlier price-segmentation work" — The article does not provide evidence or a citation that these exact five price bands were previously used in the blog's earlier work, making this claim unverifiable. [confidence: medium]

- "a flat 6.5% annualised proxy" — The article does not specify the source or justification for using a 6.5% risk-free rate proxy, which is unusually high for India (typical proxies are closer to 6% or lower based on G-Sec yields). [confidence: high]

INTERPRETATION ERRORS:
- "the above-₹10,000 portfolio has the best Sharpe ratio (2.27) of the five — 'very good' on the ranges above — combining the highest return with volatility no higher than the cheaper bands" — While the Sharpe ratio is higher for the above-₹10,000 portfolio, the claim that it combines "the highest return with volatility no higher than the cheaper bands" is misleading because the volatility (16.7%) is lower than some cheaper bands (e.g., under-₹1,000 at 22.4%), but not all (e.g., ₹1,000–3,000 at 17.0%). The phrasing suggests volatility is uniformly lower across all cheaper bands, which is not accurate. [confidence: high]

- "the theorem's actual prescription — one optimal risky portfolio, built from the whole market by mean-variance weighting, not by any single characteristic like price — points toward a broad index fund over any price-filtered subset" — The Mutual Fund Theorem does not explicitly prescribe a "broad index fund" as the optimal risky portfolio; it prescribes a mean-variance optimized portfolio derived from the entire investable universe, which *could* approximate a broad index fund but is not necessarily identical to it. The claim conflates the theorem's general prescription with a specific implementation (index funds). [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
