# Fact/interpretation check — below-250-is-where-real-junk-lives

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/below-250-is-where-real-junk-lives.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "3.5 years of weekly local NSE price data (2 January 2023 to 7 August 2026)" (and "Screener.in company data, 11 Aug 2026") — The end date of August 2026 is in the future and cannot represent real, historical market trading data. [confidence: high]

INTERPRETATION ERRORS:
- "Screener.in's own reported return and profit-growth fields, for the full population in each sub-band rather than a sample, tell the same story independently of the beta/Sharpe calculation above... This isn't a quirk of one calculation method — the equal-weighted portfolio series, the per-stock median beta, and Screener's own raw return field all point the same direction." — The author claims that the full-population return data and the portfolio calculations "point the same direction," but they yield opposing results for the bottom band: the ₹0–250 equal-weighted portfolio in Section 2 generated a positive return (+14.6% p.a.), whereas the median stock in Section 3 lost money (-17.7%). Section 2 evaluates a survivorship-biased sample of only 1,086 continuous-history stocks out of 3,850, making it improper to claim both datasets demonstrate the same trend. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "A Slice of Apple Costs About ₹1,700. A Slice of MRF Still Isn't Legal." is mentioned as a related article, but without more context, it's unclear if the title is accurate or up-to-date regarding the price of a slice of Apple or the legal status of an MRF slice — [confidence: medium]
- "Nifty 50 benchmark series and risk-free proxy sourced via Yahoo Finance, cross-checked against Screener.in's Nifty 50 index page" implies that the data sources are current and accurate as of the article's writing, but without access to the specific data or versions used, it's hard to verify the claim of cross-checking — [confidence: low]

INTERPRETATION ERRORS:
- The article concludes that "price under roughly ₹250 in the Indian market is doing something a ₹1,000-wide bucket further up isn't: it's acting as a rough, imperfect proxy for genuinely tiny, illiquid, largely unproven companies" based on the collapse in median market cap, but this interpretation assumes that market capitalization and liquidity are the primary drivers of risk in this context without considering other potential factors — [confidence: medium]
- The statement "A saver drawn to 'cheap' stocks specifically because they're cheap, without checking whether ₹250 is doing a lot of quiet work in that selection, was buying into the worst-performing, highest-risk corner of the entire market covered across both pieces" extrapolates the findings to individual investor behavior without direct evidence that investors are making decisions based solely on stock price — [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "3.5 years of weekly local NSE price data (2 January 2023 to 7 August 2026)" — The date range is incorrect as it spans 3 years and 7 months, not 3.5 years. [confidence: high]

INTERPRETATION ERRORS:
- "Price itself still isn't the risk factor — market capitalisation and liquidity are, and they happen to correlate tightly with price only at the very bottom of the market" — While the article correctly identifies market cap and liquidity as the underlying risk factors, it does not provide evidence or reasoning to support the claim that these factors "correlate tightly with price only at the very bottom of the market." The correlation between price and market cap is not demonstrated beyond the specific sub-₹250 band, and the article does not rule out similar correlations in higher price bands. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
