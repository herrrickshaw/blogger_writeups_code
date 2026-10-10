# Fact/interpretation check — india-and-mercosur-are-expanding-450

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-and-mercosur-are-expanding-450.html`

Text-SHA1: `a8e1ba805b9c9223`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "it gives preferences on about 450 Indian and 452 MERCOSUR tariff lines." — The concession schedules are reversed. Under the 2009 India–MERCOSUR Preferential Trade Agreement, India granted tariff concessions on 452 tariff lines to MERCOSUR, while MERCOSUR offered concessions on 450 tariff lines to India. [confidence: high]
- "India and MERCOSUR, the trade bloc of Argentina, Brazil, Paraguay and Uruguay" — Bolivia officially completed its accession and became the fifth full member of MERCOSUR in July 2024. Describing MERCOSUR as consisting solely of the four founding members is factually inaccurate. [confidence: high]

INTERPRETATION ERRORS:
- "Argentina’s ambassador has said India was the main destination for Argentine soybean oil in 2025, worth about $3.7 billion, with the sunflower complex adding $0.8 billion; trade press reports Argentina overtaking Ukraine as India’s sunflower oil supplier in the 2025-26 marketing year, with a record 530,000 tonnes shipped between September and April. Those figures use different periods, but together they come to most of the $5.0 billion." — This is an apples-to-oranges aggregation. The article sums partner-country export estimates from calendar year 2025 ($3.7 billion + $0.8 billion) alongside partial-year oil marketing data to explain and substantiate India's official fiscal year (April–March 2025–26) import figures ($4.96 billion). These accounting periods and trade valuation bases do not align and cannot be summed to explain the fiscal-year total. [confidence: high]
- "India and MERCOSUR Are Expanding a 450-Line Trade Pact. India’s Deficit With the Bloc Has Nearly Quadrupled in a Year, and 81% of It Is Argentina" — The article frames the quadrupled deficit as a key backdrop and risk factor for expanding the PTA, even while documenting that over 80% of the deficit is driven by Argentine edible oils (soybean and sunflower oils). These commodities are entirely outside the 2009 PTA and are traded under standard MFN tariffs; attributing or tying this bilateral imbalance to the existing preferential trade arrangement represents a false causal link. [confidence: medium]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- “The 2009 pact gives preferences from 10 % to 100 % of the duty.” — The original India‑MERCOSUR Preferential Trade Agreement provides preferential tariffs that can be **0 % (full exemption)** up to the MFN rate; there is no minimum 10 % floor. [confidence: high]  

**INTERPRETATION ERRORS:**  
- “The deficit went from about $1.2 billion to about $4.9 billion, nearly four times as large.” — This statement compares a 2024‑25 deficit figure taken from press‑reported totals with a 2025‑26 deficit derived from the Commerce Ministry portal (and a separate, unverified table for Uruguay and Paraguay). Because the two years rely on different data sources and vintages, the apparent quadrupling is not a reliable measurement of change; the claim overstates the magnitude of the shift. [confidence: medium]  

**OUTDATED DATA:**  
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India’s trade with the four members reached about $21.8 billion in 2025-26"* — The article later clarifies that the **$21.8 billion figure is incorrect** and that the **actual two-way trade for 2025-26 is $8.46 billion (exports) + $13.32 billion (imports) = $21.78 billion** (rounding difference). However, the **earlier claim of "$21.8 billion" is inconsistent with the table’s breakdown** (which sums to ~$21.78 billion) and the later corrected phrasing ("$21.8 bn India’s two-way trade" is likely a misstatement for the **$17.5 billion** mentioned in the first sentence). The **$17.5 billion (2024-25) and $21.8 billion (2025-26) figures are not directly supported by the table’s data** (which shows $17.48 billion for 2024-25 and $21.78 billion for 2025-26). [confidence: high]

- *"India’s deficit with the bloc in 2025-26, against about −$1.2 billion a year earlier"* — The **$1.2 billion deficit for 2024-25 is correct**, but the **$4.9 billion deficit for 2025-26 is inconsistent with the table’s data** (which shows a deficit of **$4.86 billion**). The article later states the deficit is **−$4.9 billion**, but the table’s arithmetic yields **−$4.86 billion**. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"India’s deficit with the bloc has nearly quadrupled in a year"* — While the deficit **did increase from ~$1.2 billion to ~$4.9 billion** (a ~4x rise), this **misrepresents the underlying drivers**. The **$3.7 billion increase is primarily due to Argentina’s surge in edible oil exports (reported as ~$3.7 billion in soybean oil alone)**, not a broad-based trade imbalance. The claim **overgeneralizes** by ignoring that:
  1. **Brazil’s trade balance with India is near-even** (exports: $8.05B; imports: $7.02B), and
  2. **Paraguay’s trade shifted from a deficit to a surplus** (+$162M).
  The **quadrupling figure obscures the fact that the imbalance is concentrated in Argentina’s oil exports**, not systemic trade policy failures. [confidence: high]

- *"Whether India’s own exports to the bloc are wider than the 450 lines now covered, and how much of the current trade uses the preferences at all"* — The article **correctly notes that utilization data is missing**, but the **implied causal link is flawed**:
  - The claim suggests that **expanding the pact (to >450 lines) would logically follow from proving current lines are underutilized**, but this **ignores that MERCOSUR’s push is driven by Argentina’s oil exports**—a product **not covered by the current 450 lines** (as per the article’s own note that "Argentina’s sales to India are led by edible oils"). Thus, the **expansion’s rationale is not tied to utilization but to Argentina’s commercial interests**, which the article does not address. [confidence: high]

---

**OUTDATED DATA:**
- *"India’s two-way trade with the four MERCOSUR members in 2025-26, about 25% more than the $17.5 billion of 2024-25"* — The **$17.5 billion figure for 2024-25 is outdated**. The **official Commerce Ministry data** (as cited in the article’s footnotes) reports **$17.48 billion** for 2024-25 (from PIB 2180058, 16 Oct 2025). The **$21.8 billion claim for 2025-26 is also inconsistent** with the table’s data ($21.78 billion). For **up-to-date figures**, check:
  - **Commerce Ministry’s Trade Intelligence and Analytics portal** (for Brazil/Argentina data).
  - **DGCI&S trade statistics** (for Uruguay/Paraguay).
  [confidence: high]

- *"The 2009 pact is narrow: it gives preferences on about 450 Indian and 452 MERCOSUR tariff lines"* — While this is **factually correct for the 2009 pact**, the **article does not verify whether the latest "expansion talks" (launched 14 Sep 2026) have updated the line count or scope**. For **current coverage**, re-check:
  - **Department of Commerce’s official request lists** (submitted to WTO in 2013, still under review).
  - **MERCOSUR’s latest tariff schedules** (published by the bloc’s secretariat).
  [confidence: medium]
