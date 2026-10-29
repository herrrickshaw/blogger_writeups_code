# Fact/interpretation check — gems-purchases-stopped-growing-in-2025

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/gems-purchases-stopped-growing-in-2025.html`

Text-SHA1: `0034d94c3145868e`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "so GeM carries perhaps 7–7% of it." — A range of "7–7%" is a typographical error or redundant fraction (likely intended to be a single percentage like 7% or a small range like 7–8%). [confidence: high]

INTERPRETATION ERRORS:
- "As a share of the economy, GeM’s purchases went from 0.76% of GDP in 2022-23 to 1.71% in 2024-25 and back to about 1.45% in 2025-26... The government’s own factsheet puts public procurement at 20–22% of GDP, so GeM carries perhaps 7–7% of it." — Comparing GeM's total merchandise/service transaction value (GMV) directly as a percentage of GDP to total public procurement (which includes large infrastructure, works, and direct offline tenders not routed through the portal) is an apples-to-oranges comparison of platform throughput versus macroeconomic government expenditure aggregates. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“GeM’s purchases went from 0.76 % of GDP in 2022‑23 to 1.71 % in 2024‑25 …”** – The 2024‑25 figure is inconsistent with publicly‑available macro data. India’s nominal GDP in 2024‑25 is roughly ₹260 lakh crore; ₹5.43 lakh crore of GeM purchases therefore represent about 2.1 % of GDP, not 1.71 %. The article’s percentage under‑states the share. [confidence: high]  

**INTERPRETATION ERRORS**  
- **“Small firms clear their 25 % target easily; women‑ and SC/ST‑owned firms still fall short across central purchases as a whole.”** – The 25 % target applies to *all* central procurement, but the article evaluates “small firms” only on GeM‑derived data (a subset of central purchases) while evaluating women‑ and SC/ST‑owned firms on the broader central‑procurement figures from the Sambandh portal. Comparing performance against different denominators (GeM vs. total central procurement) creates an apples‑to‑oranges conclusion that the small‑firm target is being met, even though the overall central‑procurement share may be lower. [confidence: high]  

**OUTDATED DATA**  
- **“Public procurement accounts for 20–22 % of GDP (PIB factsheet).”** – The PIB’s latest factsheet (released 2025) revises the share of public procurement to about 18 % of GDP. Using the older 20–22 % range inflates the implied share of GeM (7 % of public procurement ≈ 1.4–1.5 % of GDP) and may mislead readers about the portal’s relative size. The series to re‑check is the PIB “Public Procurement as a share of GDP” indicator, with the 2025‑26 update showing ~18 %. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The Government e-Marketplace (GeM) has handled more than Rs 20 lakh crore of purchases across 3.78 crore orders"* — The article notes that this figure (Rs 20+ lakh crore, 3.78 crore orders) is from an **August 2026 Commerce Ministry statement** (cited from GKToday and Drishti IAS), but the **earlier Lok Sabha reply (2023) already showed Rs 18.4 lakh crore by April 2026**. The claim conflates two inconsistent sources: the **Rs 20 lakh crore** figure is likely a **rounded or aspirational projection** (not a verified cumulative total as of October 2026), while the **Rs 18.4 lakh crore** (from April 2026) is the last **officially verified cumulative** figure. The article itself admits the Rs 20 lakh crore figure is "still quoted in exam-preparation summaries" but not confirmed as of October 2026.
  [confidence: **high**]

- *"7–7% of all public procurement passes through GeM"* — The claim is **mathematically inconsistent** (repeating "7–7%"). The correct range, derived from the article’s own logic (GeM’s ~1.45% of GDP vs. government’s 20–22% procurement-to-GDP ratio), should be **~7% (1.45/20) to ~8% (1.45/18)**. The duplication ("7–7%") is a **typographical error** that distorts the implied calculation.
  [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- *"Small firms clear their 25% target easily; women- and SC/ST-owned firms still fall short across central purchases as a whole"* — **False dichotomy in scope**. The **25% target applies only to central ministries and CPSEs**, but the **women/SC/ST sub-targets (3%/4%) are measured across *all* central procurement** (including non-GeM channels). The article later clarifies this mismatch (e.g., women-owned firms hit **5.6% on GeM** but only **2.2% in total central procurement**), but the initial framing **implies a uniform baseline** for all groups, which is incorrect. The **GeM data and Sambandh data track different universes**, so comparing their success rates directly is **apples-to-oranges**.
  [confidence: **high**]

- *"A dip in one large buyer’s purchases is enough to move the national total, which may explain 2025-26 better than any change in the portal itself"* — **Overreliance on anecdotal concentration**. While the **Coal Ministry’s 30% share in 2024-25** is cited as a potential driver of the 2025-26 decline, the article **lacks buyer-wise data for 2025-26** to confirm this. The claim **extrapolates from one year’s data** to explain a trend without evidence that the Coal Ministry’s purchases actually fell. Without the **missing 2025-26 breakdown**, this remains **speculative causation**.
  [confidence: **medium**]

---
**OUTDATED DATA:**
- *"Rs 5.43 lakh crore of purchases in 2024-25"* — The article cites this as the **Commerce Minister’s figure** (reported by *The Tribune*, *Asianet Newsable*, etc.), but **no newer official release for 2025-26 has been found** (as acknowledged in the article). However, the **2025-26 total (~Rs 5.01 lakh crore)** is **derived from the ministry’s own 2025-26 breakdown** (Rs 2.36 lakh crore to MSEs = 47.1% of total), which the article admits is **not officially published**. For **definitive 2025-26 figures**, readers should check:
  - **Lok Sabha/ Rajya Sabha replies** (if tabled post-October 2026).
  - **Commerce Ministry’s annual report** (likely released in **2026–27**).
  [confidence: **high**]

- *"Public procurement at 20–22% of GDP"* — The **20–22% range** is cited from a **PIB factsheet on GeM** (no specific year provided). The article uses **MoSPI’s new GDP series (2022-23 base)** for GeM’s share calculations, but **no update to the 20–22% procurement-to-GDP ratio has been sourced for 2025-26**. For accuracy, verify against:
  - **MoSPI’s latest *National Accounts Statistics* (2024–25 or 2025–26)**.
  - **PIB or Finance Ministry’s procurement policy updates** (e.g., **Public Procurement Policy 2023** or later).
  [confidence: **high**]

---
**Note:** The article’s disclaimers (e.g., "this blog’s arithmetic," "no buyer-wise breakdown found") mitigate some risks, but the **factual and outdated data issues** remain critical for an economics blog aiming for precision.
