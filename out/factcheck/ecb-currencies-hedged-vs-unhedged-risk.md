# Fact/interpretation check — ecb-currencies-hedged-vs-unhedged-risk

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/ecb-currencies-hedged-vs-unhedged-risk.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "India's 5.25% repo" — The Reserve Bank of India's benchmark repo rate has been 6.50% (and historically moved from 4.00% to 6.50% during recent tightening cycles); a 5.25% repo rate is factually inaccurate and cannot be verified against official RBI policy rate data. [confidence: high]
- "A separate but related move on 27 March 2026 replaced banks' prior Net Open Position limit (up to 25% of Tier-I/Tier-II capital, which had let some institutions run $1 billion or more in open FX positions) with a universal $100 million cap for all banks, effective by 10 April 2026." — RBI regulations on Net Open Position Limits (NOPL) are calculated on a bank-by-bank basis relative to capital base (Tier-I capital) and risk management capacity, rather than a universal flat $100 million cap applied uniformly to all banks. [confidence: medium]

INTERPRETATION ERRORS:
- "That is not a coincidence a covered-interest-parity theorist would find surprising: a wider policy-rate gap against India generally reflects a more different monetary-policy stance, and more different stances tend to produce more currency movement, not less." — Covered Interest Parity (CIP) is a strict no-arbitrage mathematical condition linking spot rates, forward rates, and nominal interest rate differentials; it makes no theoretical claim or prediction about exchange rate volatility or monetary divergence generating greater currency variance. [confidence: high]
- "The green-debt piece's original caution about Switzerland turns out to be directionally right, now for a measured reason rather than a theoretical one — but the same caution applies just as strongly to Japan..." — The original caution was based on CIP (hedging costs via forward points consuming the rate differential for fully hedged debt). The author conflates this with historical spot volatility (a risk relevant only to unhedged borrowers), falsely treating unhedged volatility data as empirical confirmation of a theory of hedged borrowing costs. [confidence: high]
- "CHF and JPY sit at 12.5% and 12.1% annualised INR volatility respectively — roughly double the dollar's 6.0%... the two currencies with the biggest headline rate gap are also the two most volatile against the rupee." — The article introduces the "Gap ÷ volatility" metric specifically to measure "rate advantage per unit of currency risk." On this metric, CHF (0.42) and JPY (0.35) rank higher than USD (0.27) and GBP (0.16). The author focuses purely on absolute volatility to argue CHF and JPY are unfavorable, ignoring that by their own ratio, CHF and JPY provide more rate differential per unit of volatility than the low-volatility alternatives. [confidence: medium]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "US 10-year Treasuries yielding around 4.5%" — This claim cannot be verified as the article does not provide a specific date or source for this yield, and yields can fluctuate rapidly [confidence: medium]
- "Indian government securities have historically needed spreads of roughly 250–300 basis points over Treasuries" — This claim is not supported by a specific source or date, making it difficult to verify [confidence: medium]

INTERPRETATION ERRORS:
- "the two currencies with the biggest headline rate gap are also the two most volatile against the rupee" — This statement implies a causal relationship between rate gaps and volatility, but it only shows a correlation; the article acknowledges this but does not fully explore the underlying causes of the correlation [confidence: high]
- "Cheap and volatile is not the same as cheap and safe" — This conclusion extrapolates from the data on volatility and rate gaps to a broader statement about safety, but it does not provide a clear definition of "safe" in this context or account for other factors that might influence safety [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "RBI's February 2026 ECB liberalisation (raising the automatic-route ceiling to the higher of $1bn or 300% of net worth, removing the all-in-cost ceiling)" — The claim is incorrect because the RBI's ECB liberalisation in February 2026 did not remove the all-in-cost ceiling. The all-in-cost ceiling for ECBs remains in place as per RBI regulations. [confidence: high]

- "US 10-year Treasuries yielding around 4.5%" — The claim is unverifiable as of the article's publication date (14 August 2026). US Treasury yields fluctuate daily, and the article does not provide a specific date or source for this figure. [confidence: medium]

INTERPRETATION ERRORS:
- "the forward points on any currency pair price in almost exactly the interest-rate differential a borrower is trying to harvest, so the hedged cost of borrowing in a cheap currency converges toward the same number regardless of which cheap currency you pick" — The reasoning gap is that while covered interest parity (CIP) ensures that hedged borrowing costs converge, this does not account for differences in hedging costs (e.g., bid-ask spreads, liquidity constraints) across currencies. The article later acknowledges this but frames it as a secondary consideration, whereas the original claim implies a uniform hedged cost without qualification. [confidence: high]

- "the two currencies with the biggest headline rate gap are also the two most volatile against the rupee" — The reasoning gap is that the article conflates correlation with causation. While CHF and JPY have both the largest rate gaps and highest volatility, the article does not establish that the rate gap *causes* the volatility. The volatility could stem from other factors (e.g., global risk sentiment, trade flows), and the article does not test or control for these variables. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
