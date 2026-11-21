# Fact/interpretation check — indias-power-mix-q2-2026-27-coal-42-of

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-power-mix-q2-2026-27-coal-42-of.html`

Text-SHA1: `b9eefb1388f60d6c`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Tenders issued by August 2026 | about 290 GWh (151 GWh batteries, 142 GWh pumped storage; the parts sum to 293)" — The text notes that 151 GWh of batteries and 142 GWh of pumped storage sum to 293 GWh, yet refers to the total as "about 290 GWh". While a minor rounding discrepancy, treating the sum of component tenders as a fixed aggregate while misstating the arithmetic total reflects an internal inconsistency in the data representation. [confidence: low]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“Coal and lignite … 231 GW (coal 224 GW)”** – This implies lignite capacity of about 7 GW. Official Indian power‑sector data (e.g., Ministry of Power and Central Electricity Authority) show lignite‑based generation capacity at roughly 2 GW (mainly Neyveli Lignite). A 7 GW lignite figure is therefore inconsistent with known statistics. [confidence: medium]  

**INTERPRETATION ERRORS**  
- **“Coal supplied 73 % of the extra power; solar 27 % and wind 19 % (hydro’s ‑27 % subtracted)”** – The article treats the decline in large‑hydro generation as a “negative contribution” that can be subtracted from the total extra electricity, then allocates the remaining “extra” to coal, solar and wind. This mixes a reduction in supply (hydro) with sources of additional supply, causing the percentages to sum to more than 100 % before the subtraction and leading to a misleading conclusion that coal “provided 73 % of the extra electricity.” The methodology double‑counts the hydro shortfall and does not correctly isolate the incremental generation attributable to each source. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Coal and lignite are 42% of capacity and 66% of generation; renewables 44% and 19%"*
  – The claim conflates **coal alone (224 GW, 68% PLF)** with **coal + lignite (231 GW, 51% PLF)** in capacity share. The 42% figure is correct for coal + lignite, but the 66% generation share is inconsistent with CREA’s own data (351 BU coal+lignite / 536 BU total = **65.5%**, not 66%). The 19% renewable generation share is accurate (101 BU / 536 BU), but the 44% capacity share excludes large hydro (52 GW), which is standard in CREA’s "renewables" definition. The error lies in the **rounding discrepancy (65.5% → 66%)** and the **misattribution of lignite’s PLF (51%) as coal’s PLF (68%)** in the explanatory text.
  [confidence: **high**]

- *"Battery storage at night peak: up to 5.5 GW (from 4.1 GW in Q1), about 1–2% of national demand"*
  – The **1–2% of demand** claim is plausible but **not directly verifiable** from the provided data. CREA’s table shows **5.5 GW** (peak supply) but does not state the **total peak demand** for Q2 2026-27. The article later cites **536 BU (536 TWh) total generation** for the quarter, but this is **annualized demand**, not peak demand. Without the **peak demand figure** (e.g., from CEA’s *Monthly Energy Review* or Grid-India’s *System Load Data*), the 1–2% claim is **unsubstantiated**. The **Q1 → Q2 increase (4.1 GW → 5.5 GW)** is correct per CREA, but the **percentage-of-demand claim lacks a source**.
  [confidence: **medium**]

---

**INTERPRETATION ERRORS:**
- *"A gigawatt of coal delivers several times the energy of a gigawatt of solar and the capacity share overstates what renewables supply."*
  – The reasoning **correctly highlights the plant load factor (PLF) disparity** (coal: 68%, solar: 18.3%), but **fails to account for intermittency and demand timing**. While coal’s higher PLF means it generates more energy per GW-capacity, **solar’s output is concentrated in daylight hours**, which aligns with peak demand on **62 of 92 days** (as noted later in the article). The claim **overgeneralizes** by ignoring that:
    1. Solar’s **energy contribution per GW-capacity is higher during daylight** (even at 18.3% PLF, it generates **~16.5 TWh/GW/year** vs. coal’s **~5.9 TWh/GW/year** at 68% PLF, assuming 8,760 hours/year). The **true "energy per GW" comparison requires hourly dispatch data**, not just PLF.
    2. The **capacity factor gap does not translate to a supply gap** if solar’s output coincides with demand. The article later admits: *"The daily peak fell in daylight on 62 of 92 days, which favours solar."* The interpretation **treats capacity as a proxy for supply without considering dispatch patterns**.
  [confidence: **high**]

- *"Coal and lignite supplied 73% of the year’s extra electricity; solar 27%, wind 19%; hydro’s fall subtracted 27 points."*
  – The **shares exceed 100% before accounting for hydro’s decline** due to **double-counting the base effect**. The article states:
    > *"Coal and lignite added 39 BU in a quarter of weak rain and record peaks."*
    > *"Large hydro generation fell 20%, which subtracts from the total."*
  The **73% (coal) + 27% (solar) + 19% (wind) = 119%** is **arithmetic nonsense** because:
    - The **53 BU increase** is the **net change** after hydro’s decline. The **73%/27%/19%** figures are **proportions of the increase relative to the previous year’s generation mix**, not additive shares of the **total increase**.
    - The **hydro’s 20% fall (15 BU)** is already embedded in the **53 BU net increase** (i.e., renewables grew by ~24 BU, but hydro fell by 15 BU, resulting in a **net 9 BU contribution** from renewables). The article **misrepresents the shares as independent contributors** rather than **weighted adjustments to the baseline**.
  [confidence: **high**]

---
**OUTDATED DATA:**
- *"Installed capacity, October 2026: about 560 GW, 55% non-fossil, solar nearly 175 GW"*
  – The **560 GW total capacity** is cited from a **secondary source (Sarkaritel, 13 November 2026)**, but **CREA’s own Q2 2026-27 snapshot (12 October 2026) reports 555 GW as of August 2026**. The **560 GW figure may reflect later additions** (e.g., post-August 2026 capacity), but:
    - **No official CEA/Grid-India source is cited** for the **October 2026 capacity**, making it **unverifiable**.
    - The **55% non-fossil claim** (243 GW renewables + 52 GW hydro / 560 GW) is **plausible but unconfirmed**—CREA’s August 2026 data shows **44% non-fossil (243 GW / 555 GW)**. The **175 GW solar figure** is also **not cross-referenced** with CEA’s latest *Monthly Capacity Addition Data*.
  **Recommended check:**
    - **CEA’s *Monthly Energy Review* (November 2026 issue)** for **October 2026 capacity breakdown**.
    - **Grid-India’s *System Load Data*** for **non-fossil capacity share**.
  [confidence: **high**]

- *"Battery storage operating: 9.1 GWh; due by December: 3 GWh; tendered: 290 GWh"*
  – The **290 GWh tendered figure** (151 GWh batteries + 142 GWh pumped storage) is from **CREA’s August 2026 snapshot**, but:
    - **No update is provided for tenders awarded or commissioned post-August 2026**. The article notes:
      > *"Storage tender volumes are tenders issued, not awards or commissioning dates."*
    - The **3 GWh "due by December"** is CREA’s **expectation**, not a confirmed figure. For **current status**, the reader should check:
      - **MNRE’s *Monthly Storage Progress Reports*** (latest issue).
      - **CEA’s *Energy Storage Tracker*** (if available).
  [confidence: **medium**]

---
**Note:** The article’s **methodology section** acknowledges data gaps (e.g., curtailment limited to July–August, storage tenders vs. awards), but the **outdated/unsourced claims above** could mislead readers relying on the article as a definitive source.
