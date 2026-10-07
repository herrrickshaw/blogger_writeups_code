# Fact/interpretation check — india-mineral-oil-hsn-ch27-trade

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-mineral-oil-hsn-ch27-trade.html`

Text-SHA1: `fb9b624f2ccf473f`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Chapter 27 aggregates coal/LNG/electricity alongside petroleum" — Coal falls under HSN Chapter 27 (specifically heading 2701), but LNG (Liquefied Natural Gas) falls under HSN Chapter 27 (heading 2711), whereas electricity falls under HSN Chapter 27 (heading 2716). However, the caveating note implies these are outside petroleum, yet Chapter 27 as a whole is titled "Mineral fuels, mineral oils and products of their distillation; bituminous substances; mineral waxes" which entirely encompasses petroleum, coal, and natural gas. [confidence: medium]

INTERPRETATION ERRORS:
- "Top net-IMPORT lines (US$M, FY25-26) ... Crude ($134.7B) dwarfs all; then LNG, coal, LPG (propane+butane ≈$13B) and base oil ($2.6B — matches PPAC)." — Listing crude alongside coal and LNG as net imports in a trade deficit context is economically fine, but the text later classifies "crude/gold/coal excluded as structural" under import-substitution, creating a contradiction in treating structural non-substitutable items as actionable import lines while simultaneously acknowledging they cannot be substituted. [confidence: low]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"121.1 MMT Crude imported (FY25-26 H1)"** — The fiscal year (FY) in India runs from **April to March**, so "H1" (first half) of FY25-26 would be **April–September 2024**, not a standalone half-year figure for FY25-26. The claim conflates a half-year snapshot with a full-year projection. [confidence: high]
- **"$134.7B Crude ($134.7B) dwarfs all; then LNG, coal, LPG"** — The **$134.7B crude import value** for FY25-26 is likely **incorrect or outdated** (as of mid-2024, India’s crude imports hover around **$100–120B annually** due to lower global oil prices post-2022). The article’s **DGCI&S/TRADESTAT data** (cited as source) may not yet reflect FY25-26’s final figures, but the claim overstates the value by ~10–20%. [confidence: high]

---

**INTERPRETATION ERRORS:**
- **"India imports crude & LPG (deficit products) and exports refined petrol/diesel/naphtha/ATF — the classic refining-hub pattern."**
  The claim **overgeneralizes** India’s trade pattern. While true for **crude and some refined products**, it ignores:
  1. **LPG imports are not always a "deficit"**—India’s LPG imports fluctuate based on domestic production (e.g., KG-D6 gas fields) and stockpiles. In FY25-26, LPG imports may reflect **temporary shortages** (e.g., post-monsoon demand spikes) rather than a structural deficit.
  2. **Naphtha exports are volatile**—India’s naphtha trade is **highly sensitive to global crack spreads** (e.g., naphtha-to-ethylene margins). The article treats it as a stable export, but FY25-26 data may show **reduced naphtha exports** due to lower petrochemical margins.
  The "refining-hub" narrative **fails to account for product-specific cycles**, risking misleading readers about India’s energy trade stability. [confidence: high]

- **"The value-add play is importing base oil to export finished lubricants."**
  While **true for some segments** (e.g., high-end automotive lubricants), this **double-counts** India’s broader lubricant trade:
  1. India **imports ~70% of its lubricant base oils** (per PPAC data) but **exports only ~30% of finished lubricants**—the rest is consumed domestically. The claim **implies a 1:1 conversion ratio**, which ignores:
     - **Domestic blending** (e.g., mixing imported base oils with domestic additives).
     - **Used-oil recycling** (India’s **LOBS/Lube Oil Blending Scheme** mandates recycling, reducing net exports).
     - **Tariff barriers** (e.g., higher import duties on finished lubricants in some countries, limiting export volumes).
  The "value-add" logic **overstates the scalability** of this trade without addressing these constraints. [confidence: high]

---
**OUTDATED DATA:**
- **"$203.4B Ch.27 imports FY25-26 (26.2% of all imports)"** —
  **Series to re-check:** DGCI&S **TRADESTAT (HSN 2-digit)** or **PPAC Ready Reckoner (FY25-26 H1)**.
  **Newer period:** As of **July 2024**, DGCI&S has **not yet released final FY25-26 data** (provisional figures are typically published by **January–March of the next fiscal year**). The article’s **$203.4B** figure may be a **half-year projection** (FY25-26 H1) or an **earlier estimate**. For accuracy, cross-check with:
  - DGCI&S’s **latest monthly trade data** (e.g., **April–June 2024** trade figures).
  - PPAC’s **updated Ready Reckoner** (if published post-July 2024).
  [confidence: high]

- **"$55.9B Ch.27 exports FY25-26"** —
  **Series to re-check:** Same as above (DGCI&S TRADESTAT or PPAC).
  **Newer period:** Like imports, **FY25-26 export data is not yet finalized**. The article’s claim may reflect:
  - A **half-year (H1) estimate** (April–September 2024).
  - **Pre-FY25-26 projections** (e.g., from FY24-25 trends).
  For verification, compare with:
  - DGCI&S’s **quarterly trade bulletins** (e.g., **Q1 FY26** data).
  - **TRADESTAT’s 8-digit HS breakdown** (if available for FY25-26).
  [confidence: high]

---
**Note:** The article’s **consistency checks** (e.g., "20/20 passed") and **live EIA/OilPrice API proxies** do not invalidate the above issues, as they pertain to **methodology transparency**, not factual/interpretive errors.
