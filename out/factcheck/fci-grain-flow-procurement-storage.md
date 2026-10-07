# Fact/interpretation check — fci-grain-flow-procurement-storage

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fci-grain-flow-procurement-storage.html`

Text-SHA1: `2e1ebc9871a30f89`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "for RMS 2026-27, the government set a wheat procurement target of 303 LMT (later revised up to 34.497 million tonnes)" — The numbers mix units and scales inconsistently within the same clause; 303 LMT equals 30.3 million tonnes, whereas 34.497 million tonnes equals about 344.97 LMT, making the parenthetical "revised up" description mathematically confused regarding the base 303 LMT target. [confidence: high]

INTERPRETATION ERRORS:
- "That combined procurement effort moved ₹1.99 lakh crore in food subsidy in FY25 — ₹1.29 lakh crore through FCI directly and ₹0.70 lakh crore through the states running their own Decentralized Procurement Scheme." — Food subsidy expenditures primarily reflect the economic cost of foodgrains minus the central issue price (CIP) under welfare schemes plus storage and distribution costs, rather than being a direct accounting equivalent of the total procurement effort or value of grains purchased in a single season. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Punjab ≈ 47% of the wheat pool in RMS 2024-25, the latest season with a state-wise breakdown available"* — **Incorrect season reference.** The article states RMS 2024-25 is the "latest season with a state-wise breakdown," but the text earlier explicitly cites **RMS 2025-26** (not 2024-25) for wheat procurement (300.35 LMT). Punjab’s share is not provided for RMS 2025-26, and no state-wise breakdown exists for that season yet (as of mid-2026). [confidence: high]

**INTERPRETATION ERRORS:**
- *"The 832.17 LMT paddy figure and the 544.8 LMT rice figure can be reconciled without guesswork"* — **False reconciliation.** The article notes the paddy-to-rice conversion ratio (~67%) but conflates the two figures as directly comparable without clarifying that **832.17 LMT paddy ≠ 544.8 LMT rice** (the latter is already rice-equivalent procurement, not a derived figure). The "reconciliation" requires applying the ratio to the paddy figure, which isn’t done here. [confidence: high]

**OUTDATED DATA:**
- *"Central-pool stocks stood at 476.85 LMT as of 1 January 2025"* — **Stale snapshot.** The article’s update (27 Sept 2026) confirms stocks are "well over a year stale" due to RMS 2026-27 procurement (350+ LMT wheat) and lack of updates. Re-check: **DFPD’s monthly central-pool stock series** (e.g., [data.gov.in/food-stocks](https://data.gov.in/food-stocks)) for **post-Jan 2025 data**. [confidence: high]
- *"Wheat procured — RMS 2025-26: 300.35 LMT"* — **Outdated target/actual.** The revised target for RMS 2026-27 was **34.497 million tonnes (344.97 LMT)**, and actual procurement exceeded **350 LMT** by mid-2026. Re-check: **PIB PRID 2236215** and **DFPD’s latest RMS procurement bulletin** for **RMS 2026-27 figures**. [confidence: high]
