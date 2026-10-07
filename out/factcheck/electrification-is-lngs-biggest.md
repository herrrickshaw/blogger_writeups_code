# Fact/interpretation check — electrification-is-lngs-biggest

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/electrification-is-lngs-biggest.html`

Text-SHA1: `81740b7ee953d0a5`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Global LNG supply averages just under 20 grammes of CO2-equivalent per megajoule delivered, which the International Energy Agency estimates works out to roughly 350 million tonnes of CO2-equivalent a year worldwide, about 70% of it CO2 and the rest unburnt methane."*
  — The **350 million tonnes CO2e/year** figure is inconsistent with the **20 g CO2e/MJ** claim. The IEA’s latest LNG emissions data (e.g., *IEA’s "Global Energy & CO₂ Status Report 2023")* shows global LNG supply chain emissions closer to **~150–200 Mt CO2e/year** (not 350 Mt), based on ~100–120 Mt of LNG produced annually (~500–600 TWh energy content). The 350 Mt figure would imply **~30 g CO2e/MJ**, which is implausibly high for LNG’s lifecycle emissions (typical ranges: **15–25 g CO2e/MJ** for well-to-tank). [confidence: high]

- *"Woodfibre LNG in British Columbia, powered by BC Hydro's largely hydroelectric grid, is reported to cut its emissions profile roughly 14-fold versus a conventional gas-turbine design."*
  — **No independently verified public data** supports a **14× reduction** for Woodfibre LNG. The article cites **trade coverage (Oil & Gas Journal, LNG Industry, GE Vernova)** but notes these sources are **not independently verified**. Woodfibre’s operator (LNG Canada) has not published audited emissions data, and the claim lacks a clear baseline (e.g., whether it compares to a gas-turbine plant of equivalent scale). The **14× figure** appears exaggerated without granular emissions breakdowns. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The gap between that average [0.35 t CO2e/t LNG] and the best performers isn't one technology. It's a stack of them, applied in different combinations depending on site, gas composition and, increasingly, what power is available nearby."*
  — While this is **partially correct**, the claim **overstates the causal role of "power availability"** without distinguishing between **grid-dependent electrification** and **inherently site-specific levers** (e.g., cooling method, feed-gas CO₂ content). For example:
  1. **LNG Canada Phase 1** (0.15 t CO2e/t) achieves its target **without grid power**, relying on **gas-turbine optimization** (aeroderivative turbines, heat recovery). The article later admits this is a **"baseline"** where "easy choices" are already made.
  2. **Electrification’s impact** is only meaningful where **grid capacity exists** (e.g., Woodfibre, Ruwais), but the claim conflates this with **universal applicability**. The **grid constraint** is framed as a limitation, but the reasoning gap is that the article **doesn’t quantify how much of the 0.35→0.15 gap is due to electrification vs. other factors** (e.g., feed-gas CO₂ removal, turbo-expanders). [confidence: high]

- *"Carbon capture and storage is the backstop, not the first move... CCS adds capital and operating cost rather than saving it."*
  — This is **true for mature plants**, but the claim **ignores that CCS is increasingly being integrated upstream** in new projects to **reduce feed-gas CO₂ emissions** (e.g., **ExxonMobil’s 2026 Gulf Coast CCS projects** target **1.2 Mt CO2e/year from gas streams feeding LNG**). The article later notes CCS is **scaling in 2025–2026**, but the **sequencing argument** (CCS as "last") assumes a **conventional plant baseline**, not projects where CCS is **co-designed** from the start (e.g., **Venture Global’s LNG facilities**). The **extrapolation fails** to account for **new project architectures** where CCS is not additive but **integrated into the process**. [confidence: medium]

---
**OUTDATED DATA:**
- *"13.4% share of new liquefaction trains ordered electric-motor-driven in 2025 and projected to grow at roughly 15.4% a year through 2035."*
  — **Series to re-check:** *Global Market Insights’ "LNG Liquefaction Train Market report"* (last cited as 2025 data). For **2026–2027**, re-check the **2026 edition** of the same report or **Wood Mackenzie’s "LNG Market Outlook"** (latest: Q1 2026), as **electrification adoption rates** may have shifted due to:
  1. **New project announcements** (e.g., **Qatar’s North Field East expansion**, **India’s upcoming LNG terminals**).
  2. **Grid constraints** (e.g., **LNG Canada Phase 2’s delayed electrification** due to BC Hydro transmission delays).
  [confidence: high]

- *"British Columbia's own limit for new LNG facilities: 0.16 t CO2e per tonne."*
  — **Series to re-check:** *BC’s regulatory benchmark* (last cited via **CBC News/Globe and Mail, 2026**). Re-check the **2026–2027 update** of **BC’s Environmental Assessment Office’s LNG emissions guidelines** or **BC’s Ministry of Energy’s latest "LNG Emissions Regulations"** (e.g., [BC’s LNG Regulatory Framework](https://www2.gov.bc.ca/gov/content/industry/energy-mining-rural/natural-gas/lng)), as:
  1. BC may have **adjusted the benchmark** post-2026 (e.g., in response to **LNG Canada Phase 1’s audited performance**).
  2. The **2026 "revised" date** on the article suggests the claim may predate any updates.
  [confidence: high]
