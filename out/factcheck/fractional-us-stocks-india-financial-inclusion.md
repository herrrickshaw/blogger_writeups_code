# Fact/interpretation check — fractional-us-stocks-india-financial-inclusion

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fractional-us-stocks-india-financial-inclusion.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Remittances above ₹10 lakh in a financial year attract 20% Tax Collected at Source (TCS) — reclaimable against your income tax return, but a real upfront cash-flow cost in the meantime..." — Under Section 206C(1G) of the Indian Income Tax Act governing the Liberalised Remittance Scheme (LRS), the statutory threshold above which a 20% TCS applies to foreign equity investments/other remittances is ₹7 lakh per financial year, not ₹10 lakh. [confidence: high]

INTERPRETATION ERRORS:
- "India has roughly 23.15 crore demat accounts as of June 2026... That's a real, broad base of retail savers with somewhere to put money." — This double-counts retail investors. A single individual investor can open and maintain multiple demat accounts across different brokers and depositories (NSDL and CDSL), so the total number of demat accounts significantly overstates the number of unique retail savers in the market. [confidence: high]
- "MRF is the extreme example, but the underlying issue — high per-share prices as an unintentional wealth filter on which Indian companies an ordinary saver can own directly, one whole share at a time — sits entirely on the Indian side of the barrier..." — This is an extrapolation from an extreme outlier. MRF is a unique anomaly on Indian exchanges due to its choice never to split shares; the vast majority of major Indian blue-chip listed stocks (such as Reliance Industries, TCS, ICICI Bank, or Infosys) trade at per-share prices below ₹3,000, making high unit share price an isolated exception rather than a broad systemic barrier across the domestic market. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "India has roughly 23.15 crore demat accounts as of June 2026" — This claim cannot be verified against what is known, as the article cites "Total Number of Demat Accounts in India Exceed 17.10 crore mark" from SBI Securities, but also mentions that this number has been cross-checked against more recent June 2026 industry reporting of 23.15 crore, which is not a primary source [confidence: medium]
- "The Company Law Committee recommended in 2022 that the Companies Act be amended to permit issuance and transfer of fractional shares in dematerialised form" — This claim is based on the article's text, but the article does not provide a primary source for this information, only mentioning it as a fact [confidence: medium]

INTERPRETATION ERRORS:
- "The inclusion case for fractional investing is real, but it's currently asymmetric" — The article concludes that fractional investing has not solved the domestic problem of high per-share prices, but it does not provide a clear explanation of why the same regulatory framework that allows fractional ownership of foreign stocks cannot be applied to Indian stocks, beyond stating that Indian company law does not currently recognize fractional shareholding as valid [confidence: high]
- "A claim worth flagging and setting aside: several crypto-industry news sites... have reported that SEBI has already launched 'tokenized' fractional shares of Reliance Industries for retail investors" — The article dismisses this claim as unverified, but it does not provide a clear explanation of why this claim is unlikely to be true, beyond stating that it could not be independently verified against SEBI's official communications [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India has roughly 23.15 crore demat accounts as of June 2026" — The cited source (SBI Securities) actually reports 17.10 crore as of an earlier date, and the article itself notes this discrepancy ("cross-checked against more recent June 2026 industry reporting of 23.15 crore"). The 23.15 crore figure appears to be an unverified projection or error. [confidence: high]

- "MRF Ltd (NSE, India's highest-priced listed stock) | ₹1,34,200 | 10 Aug 2026" — The cited source (StockAnalysis.com) shows MRF's price as ₹1,34,200 **per share** as of **10 Aug 2025**, not 2026. The article incorrectly states the year as 2026. [confidence: high]

INTERPRETATION ERRORS:
- "Fractional ownership of an Indian-listed share is a different problem, and it's a legal one, not a plumbing one" — While the legal barrier is correctly identified, the framing implies that the "plumbing" (technical infrastructure) is irrelevant for Indian stocks. However, the article later acknowledges that even if legal hurdles are resolved (e.g., via the Xaults sandbox), the custody model must still work within India's depository system (NSDL/CDSL). The claim oversimplifies the problem by separating "legal" and "plumbing" as mutually exclusive categories, ignoring that legal changes may require concurrent technical adaptations. [confidence: medium]

- "The inclusion case for fractional investing is real, but it's currently asymmetric" — The article correctly notes that fractional investing for US stocks is available while Indian stocks are not. However, it does not address whether the **demand** for fractional Indian stocks is empirically validated or merely assumed. The claim extrapolates the "inclusion case" from the existence of fractional US-stock platforms to an unproven demand for fractional Indian stocks, without citing data on retail investor preferences or price sensitivity for Indian equities. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
