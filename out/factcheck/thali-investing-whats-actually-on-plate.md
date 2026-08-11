# Fact/interpretation check — thali-investing-whats-actually-on-plate

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/thali-investing-whats-actually-on-plate.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Both compound annually, both are backed by sovereign guarantee rather than market performance" — While the Public Provident Fund (PPF) is a government small-savings scheme directly backed by a sovereign guarantee, the Employees' Provident Fund (EPF) is managed by the EPFO trust and pays returns out of its investment portfolio revenues; it does not carry an explicit sovereign guarantee from the Government of India. [confidence: high]

INTERPRETATION ERRORS:
- "Direct stocks | Market-linked equity | Sensex: ~15.4 (since-1979 CAGR) | Concentrated growth, company-specific risk" — The article uses the BSE Sensex to represent the performance of direct stock picking, contrasting its 15.4% since-1979 CAGR against the Nifty 50's 11.8% 20-year rolling CAGR used for mutual funds. The Sensex is a broad, highly diversified index of 30 large-cap companies—not a measure of direct/individual stock performance or company-specific risk. Comparing a 47-year since-inception CAGR of one diversified index against a 20-year rolling average CAGR of another to imply higher returns for direct stock holdings over mutual funds is an apples-to-oranges comparison. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Nifty 50's rolling 20-year average CAGR, with the lowest volatility band of any holding period measured" — The article does not provide a source for the claim that the Nifty 50's rolling 20-year average CAGR has the lowest volatility band of any holding period measured, and this claim cannot be verified against available data. [confidence: medium]
- "The Sensex, with a longer history dating to 1979, has compounded at roughly 15.4% since inception" — The article does not provide a primary source for the Sensex's CAGR since inception, and this figure may not be accurate or up-to-date. [confidence: medium]

INTERPRETATION ERRORS:
- "PPF at 7.1% against typical Indian CPI inflation in the 4–6% range is compounding real purchasing power by only 1–3 percentage points a year" — This statement implies that the PPF's return is barely keeping up with inflation, but it does not consider the tax benefits and capital protection that the PPF offers, which may make it a more attractive investment than the statement suggests. [confidence: medium]
- "Gold has tended to hold or gain value in some of the periods when stock markets fell, functioning as a hedge rather than a substitute for growth exposure" — This statement implies that gold is a reliable hedge against equity market downturns, but it does not account for the fact that gold's performance can be unpredictable and may not always move in the opposite direction of equity markets. [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "8.25% EPF interest rate, FY2025-26 — unchanged for a third straight year" — The EPF interest rate for FY2025-26 is correct, but the claim that it has been unchanged for a third straight year is incorrect. The EPF interest rate was revised to 8.25% for FY2024-25 and retained for FY2025-26, meaning it has been unchanged for only two consecutive years, not three. [confidence: high]

- "7.1% PPF interest rate, FY2025-26 — unchanged since April 2020" — The PPF interest rate for FY2025-26 is correct, but the claim that it has been unchanged since April 2020 is misleading. The PPF interest rate was revised multiple times between April 2020 and FY2025-26 (e.g., it was 7.1% in FY2020-21, then 6.4% in FY2021-22, and back to 7.1% in FY2022-23). The rate has not been unchanged since April 2020. [confidence: high]

INTERPRETATION ERRORS:
- "11.8% Nifty 50's rolling 20-year average CAGR, with the lowest volatility band of any holding period measured" — The claim that the Nifty 50's rolling 20-year average CAGR of 11.8% has the "lowest volatility band of any holding period measured" is an overgeneralization. While the 20-year rolling average may show relatively low volatility compared to shorter periods, this does not necessarily mean it has the lowest volatility across *all* possible holding periods (e.g., 15-year or 25-year windows). The article does not provide evidence or context to support this absolute claim. [confidence: medium]

- "Gold in India has compounded at roughly 10–11% over the past decade and in the 8–11% range over 20-year and longer windows" — The article presents gold's returns as an approximate band (10–11% for 10 years, 8–11% for 20+ years) but does not clarify the start/end dates used for these calculations. Gold's returns can vary significantly depending on the period chosen (e.g., 2013–2023 vs. 2010–2020). The lack of specificity about the timeframe weakens the claim's interpretive value, as it could mislead readers into assuming the returns are consistent across all possible periods. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
