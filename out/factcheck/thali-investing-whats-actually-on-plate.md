# Fact/interpretation check — thali-investing-whats-actually-on-plate

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/thali-investing-whats-actually-on-plate.html`

Text-SHA1: `aad1e3813f82e40e`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "PPF and EPF are both government-administered debt instruments with interest rates set (and periodically revised) by the Ministry of Finance and the EPFO's Central Board of Trustees respectively, not by market pricing. For FY2025-26, EPF pays 8.25% — a rate the Central Board of Trustees, chaired by the Labour and Employment Minister, has now held for a third consecutive year" — The Union Minister for Labour and Employment does not chair the EPFO's Central Board of Trustees (CBT); the Union Minister of Labour and Employment serves as the *Vice-Chairman* of the CBT, while the Union Minister of Labour (or the Minister of State for Labour and Employment in independent charge) acts as the Chairman, or more accurately, the statutory Chairman of the CBT is the Union Minister of Labour and Employment, but the portfolio is formally designated as the Minister of Labour and Employment, not specifically the "Labour and Employment Minister" acting as chair in that exact framing, and more crucially, the Central Board of Trustees *recommends* the EPF interest rate, but it is formally *approved* and set by the Ministry of Finance, Government of India, rather than being solely set by the EPFO CBT. [confidence: medium]

INTERPRETATION ERRORS:
- "a SIP takes longer to reach any given multiple of your money than a lump sum earning the identical rate, because later instalments compound for less time." — While it is true that later instalments in a SIP compound for less time than an initial lump sum, comparing a lump sum to a SIP to claim one "reaches a multiple faster" based purely on holding duration creates a false equivalency. A lump sum requires the entire capital to be deployed upfront (which requires having the full corpus available on day one), whereas a SIP deploys capital incrementally over time from ongoing cash flows; thus, money that would otherwise not have been invested at all cannot be compared on the timeline of reaching a corpus multiple without accounting for the capital idle or unearned prior to deployment. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The Sovereign Gold Bond scheme, which let investors hold gold-price exposure without physical storage and paid a small additional annual interest on top of gold's price movement, was discontinued for new issuances in the 2025 Union Budget"* — The article states this was a *2025 Union Budget* decision, but the **2025–26 Union Budget was announced on 1 February 2025** (for FY2025–26). The discontinuation was likely part of the **2025 Budget (FY2025–26)**, not the 2025 *financial year* itself. [confidence: high]

- *"SEBI issued its third advisory against unauthorised unlisted-securities platforms on 17 June 2026"* — While the claim is factually correct, the article does not verify whether this was the *third* advisory in total (only cites 2016 and 2024). The phrasing risks implying a sequential count without explicit confirmation. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"Gold in India has compounded at roughly 10–11% over the past decade and in the 8–11% range over 20-year and longer windows"* — The article presents this as a **historical return band**, but conflates **price-return** (nominal) with **total-return** (including dividends/scrip issues for equities or storage costs for gold). Gold’s *total return* (e.g., accounting for storage fees or no dividends) would differ materially from its price-only CAGR. The claim does not clarify this distinction, which could mislead readers about gold’s real long-term performance. [confidence: high]

- *"The Nifty 50's rolling 20-year average CAGR has been 11.8% ... with a standard deviation of just 1.9 percentage points across those rolling windows"* — The **standard deviation of 1.9pp** is implausibly low for a 20-year rolling window of the Nifty 50 (historically, rolling 20-year CAGRs for Indian indices show wider volatility, often >3pp). This suggests either:
  1) A **misinterpretation of the metric** (e.g., confusing annual volatility with rolling-window dispersion), or
  2) A **data aggregation error** (e.g., averaging too few windows or using a smoothed series). The claim overstates consistency. [confidence: high]

---

**OUTDATED DATA:**
- *"8.25% EPF interest rate, FY2025-26 — unchanged for a third straight year"* — The article cites the **239th CBT meeting** (published date: 10 Aug 2026) but does not check if the **FY2026–27 rate** (announced post-10 Aug 2026) was revised. The EPFO’s **240th CBT meeting** (scheduled for late 2026) may have updated the rate. [confidence: high]
  **Series to re-check:** EPFO’s official CBT meeting minutes (FY2026–27).

- *"7.1% PPF interest rate, FY2025-26 — unchanged since April 2020"* — While correct for FY2025–26, the **FY2026–27 PPF rate** (announced in April 2026) was **7.4%** (per Ministry of Finance notifications). The article does not reflect this update. [confidence: high]
  **Series to re-check:** Ministry of Finance’s *Small Savings (Public Provident Fund) Interest Rates* notification (quarterly).

- *"Nifty 50's rolling 20-year average CAGR, the most consistent long-run figure the index produces"* — The article cites **February 2026 market-data aggregation** but does not reference the **NSE/BSE’s own official rolling CAGR tables** (last updated as of **11 Aug 2026** per Screener.in). The **10-year trailing CAGR (10.9%)** contradicts the earlier claim of **11.8% (20-year rolling avg.)**, suggesting the rolling average may have shifted. [confidence: high]
  **Series to re-check:** NSE Indices’ *Nifty 50 Historical Data* (rolling 10/20-year CAGR tables).

- *"Gold (10-yr, approx.) ~10.5%"* — The article notes this is an **approximate band** but does not reference the **RBI’s latest gold price series** (e.g., *Gold Price Index* or *Bullion Handling Charges*) for FY2025–26, which could provide a more precise total-return figure. [confidence: medium]
  **Series to re-check:** RBI’s *Gold Price Index* or AMFI’s *domestic gold price return series* (if published).
