# Fact/interpretation check — green-energy-corridor-iii-is-15-times

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/green-energy-corridor-iii-is-15-times.html`

Text-SHA1: `2152fbb55c928481`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "The Ministry of Power reported in 2025 that Phase I had built 9,161 of its 9,700 circuit kilometres and charged 21,925 of its 22,600 MVA of substations by 31 March 2025" / "GEC-I from Ministry of Power" — The Intra-State Green Energy Corridor (both Phase I and Phase II) is a scheme under the Ministry of New and Renewable Energy (MNRE), not the Ministry of Power. Central financial assistance, target tracking, and progress reporting for intra-state GEC lines are administered and published by MNRE. [confidence: high]

INTERPRETATION ERRORS:
- "The urgency is real. Ember estimated that 470 GWh of renewable power was curtailed on the inter-state grid in January to March 2026, nearly two thirds of it because lines were not ready... Much of that loss is on the inter-state system, which Phase III does not cover" — The article cites renewable power curtailment and temporary-connection bottlenecks occurring specifically on the Inter-State Transmission System (ISTS) to demonstrate the urgency of GEC Phase III. However, GEC Phase III is an Intra-State Transmission System (InSTS) scheme executed by state utilities, meaning the cited curtailment data reflects constraints on a completely different network jurisdiction that Phase III does not build or resolve. [confidence: high]

OUTDATED DATA:
- "9,161 ckm built by March 2025; 4 of 8 states finished... Andhra Pradesh, Gujarat, Himachal Pradesh and Maharashtra were given extensions to June 2025 and have asked for more." — MNRE Green Energy Corridor Phase I progress updates / physical progress monitoring dashboard; by the article's stated date of late 2026, newer official status reports superseding the March/June 2025 figures exist for FY 2025-26. [confidence: medium]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- none found  

**INTERPRETATION ERRORS:**  
- *“Much of that loss is on the inter‑state system, which Phase III does not cover; … Phase III deals with the other half: the lines inside each state … Both halves have to arrive for a solar plant to run at noon.”* — The article implies that building intra‑state transmission (Phase III) will directly alleviate the inter‑state curtailment of 470 GWh reported by Ember. However, the curtailment cited occurs on the inter‑state grid, which Phase III does not address. Linking intra‑state capacity expansion to a reduction in inter‑state curtailment is a causal leap that is not supported by the data. [confidence: high]  

- *“Phase III gives the same state utilities about fifteen times as much money to spend, in seven years.”* — The comparison multiplies the total outlay of Phase III (₹186,405 cr) by the outlay of Phase II (₹12,031 cr) to obtain a ~15× factor, but it ignores that Phase III also includes a ₹50 billion (₹5,000 cr) battery‑storage component and different cost structures (e.g., higher line‑length targets, inflation). Presenting the figure as a simple “15‑times” increase is an apples‑to‑oranges comparison that overstates the relative scale of the two phases. [confidence: medium]  

**OUTDATED DATA:**  
- *“by March 2026, 26 of 44 GW Renewable capacity connected so far under the two earlier phases.”* — The article cites a connectivity figure that is current only up to March 2026. Given that the article is dated 9 October 2026, more recent data (e.g., for the period April 2026 – September 2026) is likely available from the Ministry of Power or parliamentary replies. The figure should be re‑checked against the latest official status report. [confidence: high]  

- *“Ember estimated that 470 GWh of renewable power was curtailed on the inter‑state grid in January to March 2026.”* – This curtailment statistic is presented as the latest evidence of system bottlenecks, but newer Ember or CEA reports covering the latter half of 2026 are probably released. The “latest” figure may therefore be outdated. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"26 of 44 GW Renewable capacity connected so far under the two earlier phases, by March 2026"* — The claim conflates **connected capacity** (26 GW) with **tendered/approved capacity** (44 GW). The 44 GW figure refers to the *planned* or *tendered* capacity under Phases I & II, not the actual connected capacity. The Ministry of New and Renewable Energy (MNRE) and Rajya Sabha replies (March 2026) confirm only **~26 GW** has been *physically connected* as of March 2026, while the remaining 18 GW is either stalled, under construction, or not yet tendered. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The Centre pays 29%. The two earlier phases, a fraction of the size, have connected 26 of their 44 GW, and **part of the new money pays their old bills**."* — This implies that the **₹3,050 crore** allocated to settle liabilities from Phases I & II is a *direct cause* of the delays in those phases. However, the delays (right-of-way disputes, court cases, land clearances) are systemic and unrelated to funding shortfalls. The ₹3,050 crore merely covers *unspent commitments* from earlier phases, not the root causes of their slow progress. [confidence: high]

- *"Phase I built 9,161 ckm in about nine years. **Phase III, if those figures are right, needs about 7,300 ckm a year from 2026-27 to 2032-33**."* — This assumes **linear scalability** of Phase I’s pace to Phase III’s scope, ignoring:
  1. **Geographic complexity**: Phase III spans **51,126 ckm** (vs. Phase I’s 9,700 ckm), with varied terrain (e.g., hilly states like Himachal Pradesh vs. Rajasthan’s flatlands).
  2. **Land acquisition hurdles**: The article itself cites **right-of-way disputes** as a recurring issue, which Phase III’s larger scale may exacerbate.
  3. **Battery storage addition**: Phase III includes **50 GWh of batteries**, a new component with its own logistical and regulatory challenges not present in Phase I.
  The claim overstates feasibility without accounting for these variables. [confidence: high]

---
**OUTDATED DATA:**
- *"26 of 44 GW Renewable capacity connected so far under the two earlier phases, by March 2026"* — The **March 2026** cutoff is outdated. As of the article’s publication date (**9 October 2026**), MNRE or the **Central Electricity Authority (CEA)** would have released **quarterly progress updates** (e.g., June 2026 or September 2026 data). The **latest official figure** should reflect any changes in connected capacity (e.g., new tenders, stalled projects, or completions) post-March 2026. [confidence: high]
  *Series to re-check*: MNRE’s *Monthly/Quarterly Renewable Energy Progress Reports* or CEA’s *Grid Integration Status Updates*.

- *"₹3,050 crore of the new scheme’s central money goes to liabilities from Phases I and II"* — The **₹3,050 crore** figure is derived from the **30 September 2026 Cabinet approval**, but the **actual disbursement status** (how much has been released vs. still owed) may have changed by October 2026. The article does not cross-check whether this amount has been **fully sanctioned** or if any revisions occurred in the interim. [confidence: medium]
  *Series to re-check*: **Public Financial Management System (PFMS) disbursement data** for GEC phases or MNRE’s *Financial Progress Reports*.

---
**Note on battery storage figures:**
While the **₹50,000 crore** cost for 50 GWh is plausible given current market prices (₹1 crore/MWh), the **₹12 lakh/MWh subsidy** in GEC-III is **lower than the second viability-gap funding round (₹18 lakh/MWh)**. This suggests either:
1. **Price declines** since June 2025 (possible but unconfirmed), or
2. **A miscalculation** in the article’s comparison (the second round’s ₹18 lakh/MWh was for **30 GWh**, not directly comparable to GEC-III’s 50 GWh). This does not qualify as a factual error but warrants clarification from the **Cabinet’s scheme guidelines** or **MNRE’s battery storage tender documents**. [Not flagged as an error but requires verification.]
