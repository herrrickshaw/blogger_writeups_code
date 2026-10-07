# Fact/interpretation check — hsn-wise-historical-importexport-trends

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/hsn-wise-historical-importexport-trends.html`

Text-SHA1: `b1a7b27f7ceec4ab`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Growth and CAGR are computed FY2018-19 → FY2025-26 (7 growth periods over 8 fiscal years)." — The mathematical span from FY2018-19 to FY2025-26 covers 7 fiscal years of growth (2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26), not 8 fiscal years. [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Mineral fuels & oils grew only 21.2% over the same eight years"* — The claim conflates **value growth (21.2%)** with **price-driven vs. volume-driven growth**, which cannot be distinguished without quantity data. While the 21.2% figure may be correct for nominal value, it does not account for whether this growth reflects higher prices, increased imports, or both. [confidence: **high**]
  *(Note: The article later acknowledges this limitation in the "What would fix this" section, but the initial claim stands as a factual gap.)*

- *"Pearls, gems & jewellery (HS71) is the one major chapter moving the wrong way for exports: -29.9% since FY2018-19"* — The **-29.9% decline** is plausible based on the provided table, but the article does not verify whether this aligns with **official export data** (e.g., DGFT or PIB) or whether it accounts for **reclassifications** (e.g., shifts in HS coding for precious stones). [confidence: **medium**]

---
**INTERPRETATION ERRORS:**
- *"Fertilisers (HS31) posted the highest eight-year growth rate among India's dozen largest imports, +118.9% since FY2018-19"* — The **CAGR of 118.9%** is misleading because it **ignores volatility**: The article later states that fertiliser imports *"sat flat near $6.7bn for three years, jumped to $12.8bn in FY2021-22, peaked at $15.3bn in FY2022-23, collapsed back to $8.3bn by FY2024-25, then spiked again to $14.6bn."* This **non-linear trajectory** means the CAGR does not reflect a consistent trend but rather **compensates for a collapse with later spikes**, distorting the narrative of "fastest-growing." [confidence: **high**]

- *"Mineral fuels imports have grown a modest 21.2% over eight years (largely price-driven, not a structural shift)"* — While the **21.2% growth** may be correct, the **attribution to "price-driven"** is an **unverified extrapolation**. Without **quantity data** (e.g., barrels imported vs. price per barrel), it cannot be confirmed whether the growth is due to higher prices, increased volumes, or both. The claim assumes a causal link that cannot be proven with the given data. [confidence: **high**]

---
**OUTDATED DATA:**
- *"FY2025-26 is the most recent data available (updated 19 May 2026 per source)"* —
  **Series to re-check:** DGCI&S TRADESTAT (Commodity-wise Import/Export reports).
  **Newer period:** As of **July 2026**, DGCI&S may have released **FY2026-27** data (or revised FY2025-26 figures) via their portal or **Commerce Ministry’s TIA Portal**. The article’s note that FY2025-26 is "provisional" suggests a check for updates is warranted. [confidence: **high**]

- *"Top 12 import chapters account for 81.5% of all FY2025-26 imports"* —
  **Series to re-check:** DGCI&S TRADESTAT (aggregate import data by HS chapter).
  **Newer period:** The **81.5% share** may have changed in **FY2026-27** due to shifts in import composition (e.g., new tariffs, supply chain disruptions). The article’s reliance on FY2025-26 data risks obscuring recent trends. [confidence: **medium**]

---
**Note:** The article’s **self-identified caveats** (e.g., volatility in fertiliser data, provisional FY2025-26 figures) align with the gaps flagged above, but the initial claims do not sufficiently qualify their limitations.
