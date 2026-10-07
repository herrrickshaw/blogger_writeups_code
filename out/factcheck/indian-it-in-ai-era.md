# Fact/interpretation check — indian-it-in-ai-era

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indian-it-in-ai-era.html`

Text-SHA1: `e8958c7bed9275a4`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "The 2025-26 Survey praises the services performance as “creditable and macro-stabilising” and then says something harder... and that currency stability “has always eluded countries that could not become successful and significant exporters of manufactured goods.”" — The Economic Survey published by the Ministry of Finance in India is released for the fiscal year preceding the current one (e.g., the Economic Survey 2024-25 corresponds to the budget for FY2025-26, and the Economic Survey 2025-26 corresponds to FY2026-27), making direct quotes of a 2025-26 Survey describing events up to July 2026 anachronistic or misattributed relative to official publication timelines. [confidence: medium]

INTERPRETATION ERRORS:
- "Net services receipts hit $216.6bn in FY2025-26... They cover 64% of India's goods trade deficit on their own, and 107% once remittances are added." — The article compares gross or net flows directly as coverage percentages without accounting for the corresponding factor outflows and import components embedded within services (such as software royalty payments, travel, and business service imports) that also affect the current account, creating a misleading partial-equilibrium ratio of the trade imbalance. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India's gross services exports reached **$421.3 billion in FY2025-26**, up from $387.5 billion."* — The RBI’s *Developments in India’s Balance of Payments (Q4 2025-26)* reports **net services receipts** at $216.6 bn for FY2025-26, not gross exports. Gross exports (including reinvested earnings) are not published by the RBI in this series; the $421.3 bn figure likely conflates gross exports with net receipts or includes unreported data. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Net services receipts rose **$27.8 billion in one year, the largest increase on record**."* — While true for FY2025-26, the claim ignores that **gross services exports (including reinvested earnings) grew by ~$33.8 bn** (from $387.5 bn to ~$421.3 bn), suggesting the "record jump" in net receipts may reflect **repatriation patterns** (e.g., higher profit remittances) rather than pure export volume growth. The article treats net receipts as a proxy for export performance, but net figures are distorted by capital flows (e.g., retained earnings). [confidence: high]

- *"The distance between the merchandise trade deficit and current account deficit is what services and remittances do."* — This oversimplifies causality. The **$82.1 bn gap** (FY2025-26) is closed by *net* services (+$216.6 bn) and remittances (+$143.6 bn), but **primary income outflows** (investment income paid abroad, −$48.2 bn) and **secondary income** (worker remittances net of foreign aid, ~+$143.6 bn) interact dynamically. The article frames services as the sole stabilizer, but **capital account movements** (e.g., FDI, portfolio flows) and **official reserves** also absorb shocks. [confidence: high]

---
**OUTDATED DATA:**
- *"Merchandise trade deficit was **$337.3 billion** in FY2025-26"* — The RBI’s latest *Monthly Statistics of Trade* (August 2026) shows the **FY2026 trade deficit at $389.1 bn** (preliminary), with services receipts rising to **$230.4 bn** (net). The article’s FY2025-26 data is correct for its cited source (*Q4 2025-26 BoP report*), but the claim of "$337.3 bn" as the "latest" figure is outdated. [confidence: high]
  *(Series to re-check: RBI’s *Monthly Statistics of Trade* and *Developments in India’s Balance of Payments*; newer period: FY2026 preliminary data.)*

- *"NASSCOM’s FY2024 industry revenue was **$268.8 bn** (restated)"* — The article notes NASSCOM’s **FY2024 restatement** from $253.9 bn to $268.8 bn but does not reconcile this with the **$282.6 bn FY2025 figure** (which implies ~11.5% growth, contradicting NASSCOM’s stated 5.1%). Press reports suggest FY2025 revenue was closer to **$297 bn**, but this remains unconfirmed in NASSCOM’s official reports. [confidence: medium]
  *(Series to re-check: NASSCOM’s *Strategic Review 2026*; newer period: FY2025 revenue restatement pending.)*
