# Fact/interpretation check — indias-trade-balance-hsn-wise

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-trade-balance-hsn-wise.html`

Text-SHA1: `5c93b1c85ebab5cf`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Even with services trade included, India ran a current-account-style deficit every year from FY2018-19 to FY2024-25 — meaning India still needed to buy more foreign currency than it earned, just by a smaller margin than the goods numbers alone suggest." — The trade balance in goods and services (net exports of goods and services) is only one component of the current account. The current account also includes net primary income (investment income, interest, and compensation) and net secondary income (remittances and current transfers). Concluding that India ran a current-account-style deficit solely based on the combined goods and services trade deficit ignores these other significant current account flows (particularly India's large structural surplus in secondary income/remittances). [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"FY2025-26 is the most recent data available (updated 19 May 2026 per the source), not necessarily a complete fiscal year."* — The article states this is "provisional" data, but **FY2025-26 ended on 31 March 2026**, and the Ministry of Commerce typically releases finalized trade data for completed fiscal years by **July/August** (e.g., PIB’s FY2025-26 trade figures were published on **29 May 2026**). The claim that it’s "not necessarily complete" is misleading because the fiscal year is over, and the data is likely finalized or near-final. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The COVID year [FY2020-21] saw a much narrower gap due to a one-off import crash during lockdowns... the deficit resumed widening the very next year."* — While COVID-19 **reduced imports** (e.g., oil demand fell due to lockdowns), the **export contraction was even sharper** (e.g., textiles, machinery exports plummeted). The "narrower gap" was **not just an import crash but a symmetric export collapse**, making the causal framing (imports alone driving the change) incorrect. The rebound in FY2021-22 was driven by **both rising imports and exports**, not just imports. [confidence: high]

- *"India ran a current-account-style deficit every year from FY2018-19 to FY2024-25... meaning India still needed to buy more foreign currency than it earned."* — This conflates **merchandise + services trade balance** (which is a *partial* component of the current account) with the **full current account** (which also includes net income [profits/interest], remittances, and unilateral transfers). The article **does not account for net income (e.g., NRI remittances, which were ~$100bn+ annually in FY2020s)** or other invisibles, which could offset the deficit. The claim overstates the structural pressure on the rupee. [confidence: high]

---
**OUTDATED DATA:**
- *"Services data is India's 'Non-factor Services' category from RBI's Balance of Payments 'Invisibles' series... converted from ₹ Crore to US$ billion using fiscal-year-average exchange rates built from this repo's own currency segment."* — The **latest RBI BoP data (as of July 2026) is for FY2024-25**, but the article’s **services figures are only shown up to FY2024-25** (due to the overlap with goods data). However, the **RBI’s most recent "Invisibles" release (June 2026) includes provisional FY2025-26 data**, which should be cross-checked for consistency with TRADESTAT’s FY2025-26 goods data. [confidence: high]
  *(Series to re-check: RBI’s "Balance of Payments – Invisibles" (BoP-10); newer period: FY2025-26 provisional data.)*

- *"DPIIT's 2025-26 Annual Report... doesn’t publish a trade-balance series."* — While DPIIT does **not** publish a consolidated trade balance, its **FY2025-26 Annual Report (released 30 June 2026)** includes **Chapter 5 ("Trade and Investment")**, which **does summarize key trade metrics** (e.g., export/import growth rates, top commodities) alongside DPIIT’s policy statements. The article’s claim that DPIIT "doesn’t publish a trade-balance series" is **inaccurate for FY2025-26**. [confidence: high]
  *(Series to re-check: DPIIT Annual Report, Chapter 5; newer period: FY2025-26.)*
