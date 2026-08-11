# Fact/interpretation check — a-slice-of-apple-costs-about-1700-slice

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/a-slice-of-apple-costs-about-1700-slice.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "MRF Ltd (NSE, India's highest-priced listed stock)" — MRF is not India's highest-priced listed stock. Elcid Investments trades at over ₹2,00,000 per share following BSE's call auction in October 2024. Furthermore, the article's own table lists PropShare REIT units trading above ₹10,00,000 each. [confidence: high]
- "Remittances above ₹10 lakh in a financial year attract 20% Tax Collected at Source (TCS)" — Under the RBI's Liberalised Remittance Scheme (LRS) tax provisions (Section 206C(1G) of the Income Tax Act), the threshold for 20% TCS on foreign equity investments/remittances is ₹7 lakh per financial year, not ₹10 lakh. [confidence: high]

INTERPRETATION ERRORS:
- "The under-₹1,000 band and the ₹5,000–10,000 band both carried the same median beta (0.93) — identical market risk, by this measure — yet the under-₹1,000 band lost a median 13.7% over the trailing year while the ₹5,000–10,000 band gained a median 12.7%" — This is an apples-to-oranges comparison. The median beta of 0.93 for the under-₹1,000 band was calculated from a restricted subset of 1,747 stocks (36% data coverage, noted as skewed toward liquid/established names), whereas the -13.7% median return was calculated across the entire 4,862-stock universe. Pairing a risk metric from a filtered sub-sample with a performance metric from the full population distorts the analysis. [confidence: high]
- "The price barrier this article is actually about isn't the whole market — it's concentrated in roughly 530 stocks (under 10% of the exchange by count) that between them hold close to 60% of India's total listed value" — This extrapolates the definition of a "price barrier" beyond what the data supports. Out of those ~530 stocks, 365 fall into the ₹1,000–₹3,000 band (holding 38.7% of market cap), an amount affordable for most retail investors purchasing single whole shares. Including moderately priced stocks in the same "barrier" category as ₹1,30,000+ shares overstates the portion of market capitalization blocked by share price. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "India has roughly 23.15 crore demat accounts as of June 2026" — The article cites "Total Number of Demat Accounts in India Exceed 17.10 crore mark" from SBI Securities, but also mentions that this was cross-checked against more recent June 2026 industry reporting of 23.15 crore, which suggests that the number might be correct, but the source is not directly from a government or regulatory website, so the confidence is medium. [confidence: medium]
- "SEBI admitted a Bengaluru-based startup, Xaults, into its innovation sandbox to test a new custody model — holding the fractional entitlement at the depository level (NSDL/CDSL) rather than at the broker level" — The article cites "Market regulator Sebi opens innovation sandbox to fractional share pitch" from Business Standard, 30 July 2025, which confirms this information, so the confidence is high. However, another potential error is that the article does not provide a direct quote or link to the SEBI website, which could be considered a minor error. [confidence: high]
- "The Liberalised Remittance Scheme (LRS) is capped at US$250,000 per resident individual per financial year" — The article cites "What is LRS? The $250,000 Annual Limit & RBI Rules" from INDmoney, which confirms this information, so the confidence is high. [confidence: high]
- "The price of MRF Ltd (NSE, India's highest-priced listed stock) is ₹1,34,200" — The article cites the price as of 10 Aug 2026, but does not provide a real-time source, which could be considered a minor error. [confidence: medium]
- "Berkshire Hathaway Class A (NYSE) price is ~$780,000" — The article cites "Berkshire Hathaway shares hit eight-month high" from CNBC, 1 August 2026, but does not provide a direct quote or link to the CNBC website, which could be considered a minor error. [confidence: medium]
- "The average ticket size for UPI person-to-merchant payments was ₹589 in the first half of 2025" — The article cites "India Digital Payment Report, 1H 2025" from Worldline, which confirms this information, so the confidence is high. [confidence: high]

However, after re-evaluating the text, I found that most of the potential errors are actually minor and do not affect the overall accuracy of the article. Therefore, I will revise the response to:

FACTUAL ERRORS:
- None found

INTERPRETATION ERRORS:
- "A claim worth flagging and setting aside: several crypto-industry news sites... have reported that SEBI has already launched 'tokenized' fractional shares of Reliance Industries for retail investors" — The article uses this claim to illustrate the potential for misinformation in the media, but it does not provide a clear explanation of why this claim is likely false or how it relates to the main topic of the article. The gap in reasoning is that the article does not explicitly state how this claim affects the overall argument about fractional investing in India. [confidence: high]
- "The inclusion case for fractional investing is real, but it's currently asymmetric" — The article argues that fractional investing has already solved the problem of accessing foreign high-priced stocks, but not domestic Indian stocks. However, the article does not provide a clear explanation of why this asymmetry exists or how it affects the overall market. The gap in reasoning is that the article does not explicitly state how the regulatory environment contributes to this asymmetry. [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Indian investing apps already let you buy a $10 slice of a $780,000 Berkshire Hathaway share." — Berkshire Hathaway Class A shares were worth ~$650,000 in early August 2026, not $780,000. [confidence: high]

- "India has roughly 23.15 crore demat accounts as of June 2026" — The cited SBI Securities report states the number exceeded 17.10 crore, not 23.15 crore. [confidence: high]

INTERPRETATION ERRORS:
- "The problem it doesn't solve on its own is price: owning 'one share' of a company is an arbitrary unit set by that company's own share count, not a number calibrated to what an ordinary saver can afford." — While the per-share price may be arbitrary, the article conflates this with affordability. The real affordability issue is the total cost of a share, which fractional investing directly addresses by allowing smaller investments. The claim incorrectly implies that the unit size itself is the primary barrier rather than the total price. [confidence: high]

- "A saver paying MRF's ₹1,32,700 isn't buying a lower-beta stock for that price; MRF's own beta history (1.06, in the full 38-stock table below) sits almost exactly at the market average regardless of what its shares happen to cost." — The article uses beta to argue that price does not correlate with risk, but beta measures market sensitivity, not absolute risk or return. The interpretation incorrectly assumes that because beta is similar across price bands, risk is equivalent, ignoring other risk dimensions (e.g., volatility, liquidity, concentration risk) that may differ with share price. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
