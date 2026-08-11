# Fact/interpretation check — below-250-is-where-real-junk-lives

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/below-250-is-where-real-junk-lives.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99009, Requested 2334. Please try again in 19m20.351999999s. Need more tokens? Upgrade to Dev Tier today a]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "3.5 years of weekly local NSE price data (2 January 2023 to 7 August 2026)" — The end date (7 August 2026) is in the future relative to the article's publication date (11 August 2026), making the data range impossible. The correct end date should likely be 7 August 2025 or earlier. [confidence: high]

- "Only 1,086 of the 1,267 ₹0–250-band stocks with an NSE/BSE ticker in this article's data actually had sufficient local price history to compute a reliable beta" — The article claims 1,267 stocks exist in the ₹0–250 band, but earlier it states there are 3,850 stocks in this band. This inconsistency suggests a miscalculation or misreporting of the number of stocks. [confidence: high]

INTERPRETATION ERRORS:
- "Price itself still isn't the risk factor — market capitalisation and liquidity are, and they happen to correlate tightly with price only at the very bottom of the market" — While the article correctly identifies that market cap and liquidity are the true risk factors, it implies that price is only a proxy for these factors *at the very bottom* (below ₹250). However, the data shows that median market cap increases sharply even within the ₹250–500 band (₹1,154 crore), suggesting that price may correlate with market cap across a broader range, not just at the bottom. The article underplays this broader correlation. [confidence: medium]

- "A saver drawn to 'cheap' stocks specifically because they're cheap, without checking whether ₹250 is doing a lot of quiet work in that selection, was buying into the worst-performing, highest-risk corner of the entire market covered across both pieces." — The article conflates "cheap" (low price) with "worst-performing" (negative returns) without acknowledging that low price alone does not inherently imply poor performance. The negative returns in the ₹0–250 band could be due to other factors (e.g., sectoral trends, company-specific issues), and the article does not establish a causal link between low price and poor performance independent of these confounders. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
