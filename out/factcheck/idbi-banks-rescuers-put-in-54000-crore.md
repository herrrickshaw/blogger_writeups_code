# Fact/interpretation check — idbi-banks-rescuers-put-in-54000-crore

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/idbi-banks-rescuers-put-in-54000-crore.html`

Text-SHA1: `6f2e821ca40e8c75`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Both fall short of what the same money would have earned at 7%, roughly the government’s own borrowing rate." — Comparing the cumulative nominal capital infusions made by the government over a multi-year period directly against a 7% annual compound benchmark involves an apples-to-oranges temporal comparison. Money injected in 2010-11 carries a vastly different inflation and compounding duration than money injected in 2019, and treating lump-sum nominal historical totals as uniform principals growing at a flat rate ignores the actual timing and cash-flow vectors of those infusions. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“The government described it as the largest foreign investment in India’s financial sector.”** – No public record shows the government making this claim. Earlier foreign‑direct investments in the Indian financial sector (e.g., SoftBank’s multi‑billion‑dollar stake in Paytm, the acquisition of a 51 % stake in HDFC Bank by a foreign consortium in 2022) were larger in monetary terms than the ₹52,878 cr deal. The statement therefore appears factually incorrect. [confidence: medium]  

**INTERPRETATION ERRORS**  
- **“Both fall short of what the same money would have earned at 7 %, roughly the government’s own borrowing rate.”** – The article treats the series of capital infusions (made at different times from 2010‑11 to 2019) as a single lump‑sum that could have been invested at a constant 7 % annual return. This ignores the timing of each tranche, the fact that the government’s borrowing cost varied over the period, and that the risk profile of sovereign bonds differs from that of a distressed bank recapitalisation. Consequently, the 7 % benchmark does not provide a valid counter‑factual comparison. [confidence: high]  

**OUTDATED DATA**  
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"LIC earns about 6% a year on its 2018-19 rescue"* — The claim conflates nominal returns (₹42,461 crore vs. ₹26,717 crore input) with an annualized rate, which is misleading without adjusting for the time value of money (e.g., the ₹26,717 crore was spread over multiple tranches from 2018–2019, not a single lump sum). The 6% figure assumes unrealistic compounding or ignores the fact that dividends and retained stakes are one-time payouts, not recurring yields. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The government gets back about 1.5 times the ₹27,441 crore it put in since 2010-11"* — This ignores that ₹12,438 crore of the ₹27,441 crore was in the form of **recapitalization bonds**, which are debt instruments with annual interest payments (not "cash" returns). The true cost includes the **present value of future interest payments**, which the article does not account for. [confidence: high]
- *"Both fall short of what the same money would have earned at 7%, roughly the government’s own borrowing rate"* — The 7% comparison is **apples-to-oranges** because:
  1. The ₹27,441 crore includes **non-cash recapitalization bonds** (whose true cost is higher due to interest).
  2. The government’s **opportunity cost** should account for the **risk-adjusted return** of alternative investments (e.g., sovereign bonds yield ~7%, but IDBI was a high-risk rescue).
  3. The **time horizon** is inconsistent—some funds were injected in 2010, while returns are calculated over a shorter period (2026). [confidence: high]

**OUTDATED DATA:**
- *"₹54,158 cr put into the bank as new capital since 2010-11"* — The article cites **CAG Report No. 28 (2017)** and **Lok Sabha Unstarred Question (2017)** for pre-2018 data, but later tranches (e.g., LIC’s 2018–2019 purchases) rely on **SEBI filings and exchange reports from 2019**, which may have been superseded by updated **LIC annual reports (2025–26)** or **DFS banking analytics (FY2026–27)**. The total should be cross-checked against the **latest DFS "Banking Analytics" report** (likely FY2026–27) for completeness. [confidence: medium]
- *"₹59.22 a share book value (September 2026)"* — The article uses **September 2026 book value** for valuation comparisons, but the **March 2026 book value (₹55.41)** was also cited earlier. For consistency, the **latest audited book value (as of March 2027, if available)** should be used, as the deal closed in October 2026. [confidence: medium]
