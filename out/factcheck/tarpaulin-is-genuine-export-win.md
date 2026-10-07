# Fact/interpretation check — tarpaulin-is-genuine-export-win

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/tarpaulin-is-genuine-export-win.html`

Text-SHA1: `4520e4cd06bb0a17`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Agrotech FY2025-26 exports of $193M against imports of $100M, a net +$93M — down from FY25's $231M/$92M as exports softened 16.4% year-on-year" — The article cites data for a future fiscal year (FY2025-26) relative to its publication date of August 2026, but presents these figures alongside a backward-looking comparison ("down from FY25's..."), while the article is published halfway through FY2025-26, making a full fiscal year's trade data for that period impossible to compile [confidence: high]

INTERPRETATION ERRORS:
- "The claim that India imports 'substantial volumes' of agrotextiles and geotextiles from China, South Korea and Germany combines both NTTM segments in the original source; it should be read as directional, not as a precise Agrotech-only import figure — Section 2's own TradeStat-based Agrotech numbers (a genuine surplus) are the more reliable segment-specific figure here." — The author dismisses an aggregate source as merely "directional" while simultaneously relying on their own unpublished, proxy-mapped blog figures (TradeStat 314-code mapping) to claim a precise net export surplus, committing an apples-to-oranges comparison of official aggregate data against unverified proprietary estimates. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India is the world's largest exporter of HDPE tarpaulin by shipment count"* — The claim of India leading in shipment count (6,763 vs. Vietnam’s 991 and China’s 166) is **implausible** given that **China is the world’s dominant HDPE tarpaulin exporter by volume and value** (per UN Comtrade, WTO, and industry reports like Textile School). While shipment *counts* can vary by trade-data provider (e.g., Volza’s methodology), **India’s share of global HDPE tarpaulin exports by value is far smaller** (e.g., ~5–10% vs. China’s ~40–50%). The UAE, UK, and Bhutan destinations also lack corroboration in official trade data (e.g., India’s DGFT or UAE’s trade statistics). [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- *"Geotextiles for canal lining and highway embankments... where Indian MSMEs meet under a third of even flagship national-highway demand"* — The **30% MSME fulfillment rate is specific to NHAI projects**, not the broader geotextile market (including canal lining, farm ponds, etc.). The article **extrapolates this to imply a systemic import dependency in geotextiles**, but:
  1. Canal lining (agriculture-adjacent) may have **higher domestic capacity** due to Jal Shakti’s push for *in-situ* solutions (e.g., state-level geotextile mandates).
  2. The **highway figure is a proxy**, not a segment-wide benchmark. For example, **nonwoven geotextiles for erosion control** (a sub-segment) might have higher domestic penetration.
  3. The claim conflates **volume dependency** (e.g., high-end geosynthetics for tunnels) with **value dependency** (e.g., bulk nonwovens for road bases). [confidence: **high**]

---
**OUTDATED DATA:**
- *"FY2025-26 exports of $193M against imports of $100M [for Agrotech]"* — This is **not an official Ministry of Textiles figure** but a **blog’s TradeStat-based proxy mapping** (cited as "same-methodology" but unpublished). For **official data**, check:
  - **Ministry of Textiles’ *Technical Textiles Annual Report*** (latest: FY2024–25, released ~June 2026) for **HSN 5602–5604** (agrotextiles) trade data.
  - **DGFT’s *Trade Statistics Database*** (monthly/quarterly updates) for **Agrotech/Geotech HSN codes** (e.g., 5602.10–5602.90 for tarpaulins, 5604.10–5604.90 for geotextiles).
  [confidence: **high**]

---
**OUTDATED DATA (additional):**
- *"Domestic shade-net/mulch-film consumption estimated at roughly ₹487 crore"* — The **base year for this estimate is unstated**, but given the article’s 2026 publication date, it likely pre-dates:
  - **2025–26 *Agricultural Statistics of India*** (released by MoA&FW ~March 2026), which may include updated **agrotextile input consumption** data.
  - **CII/Assocham’s *Technical Textiles Market Report*** (latest: 2025–26 edition, expected ~Q4 2026).
  [confidence: **medium**]
