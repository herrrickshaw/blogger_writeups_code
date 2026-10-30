# Fact/interpretation check — how-to-use-focus-sector-investor-map

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-focus-sector-investor-map.html`

Text-SHA1: `1362cde5f1b22d7b`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "The pairing file keeps its negative findings (a stalled steel JV, a lapsed battery award, a shrinking beneficiary list), so it is a safer starting point than a list of announcements." — The article later explicitly describes the POSCO row as "MoU-STAGE (clearance-proof of stall)" and lists a total of 19 pairs (12 verified, 7 prospective), which does not account for or list a "lapsed battery award" or a "shrinking beneficiary list" within the actual dataset summary. [confidence: medium]

INTERPRETATION ERRORS:
- "Medical Devices has 7 foreign names and 0 India names in the final list, so that sector looks one-sided; check why before relying on it." — The absence of India-listed names in the final filtered shortlist is attributed to the sector being one-sided, while earlier text notes that the underlying pipeline relies on a conservative ticker-to-country join and trailing, unaudited free data filters. Zero Indian names on a profitability and growth-screened list could be an artifact of strict screening criteria rather than an indicator that India lacks companies in that focus sector. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- none found  

**INTERPRETATION ERRORS:**  
- *“The pairing file keeps its negative findings (a stalled steel JV, a lapsed battery award, a shrinking beneficiary list), so it is a safer starting point than a list of announcements.”* — The article infers that the inclusion of negative findings automatically makes the dataset “safer” for users. Safety depends on many factors (completeness, timeliness, verification standards); merely adding negative cases does not guarantee a more reliable or less risky source. This is a causal claim that is not supported by evidence. [confidence: high]  

**OUTDATED DATA:**  
- *“19,795 companies in the global catalog … The totals add up to 19,795.”* — The figure is presented as the current size of the global listed‑company universe, but the underlying market data (e.g., Damodaran industry classification, exchange listings) is updated continuously. A newer snapshot (e.g., Q4 2026 or Q1 2027) is likely to show a different total. The series to re‑check is the count of listed companies classified into the twelve focus sectors (source: author’s market‑data stack / Damodaran classification). [confidence: high]  

- *“Pairings were retrieved on 2026‑07‑20 and policy status changes quickly.”* — The pairing information is tied to a specific retrieval date. Since Indian trade‑policy schemes and foreign‑investor commitments evolve rapidly, a later update (e.g., after August 2026) is likely to have added, removed, or altered pairings. The relevant series is the “foreign_investor_initiative_pairs.json” dataset; it should be refreshed to the most recent PIB releases or cabinet approvals. [confidence: medium]

## Mistral open-mistral-nemo

Here’s the structured fact-checking report based on the provided article:

---

**FACTUAL ERRORS:**
- *"19,795 companies in the global catalog"* — The article claims this total is derived from a "country matrix" summing to 19,795, but the **underlying data source (Damodaran industry classification + author’s proprietary market stack)** is not publicly verifiable. The article itself notes that the **screening universe was 38,495 names**, of which only **2,217 were joined** (a 94% drop rate), making the 19,795 figure implausible as a direct count of "listed companies." [confidence: high]
- *"147 verified-profitable names in the final list"* — The article states this is an aggregate count, but the **per-sector breakdown (e.g., Medical Devices: 7 Foreign, 0 India)** suggests the 147 may include duplicates or misclassifications (e.g., "India-listed" vs. "foreign-listed" overlaps). No source cross-checks this claim against official PIB approvals or audited financials. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"The pairing file keeps its negative findings (a stalled steel JV, a lapsed battery award, a shrinking beneficiary list), so it is a safer starting point than a list of announcements."* — **Gaps in reasoning:**
  1. **Negative findings ≠ representative sample**: The article highlights only 3 negative cases (POSCO, battery award, etc.) out of 19 pairs, but this does not prove the dataset is "safer." The **7 prospective pairs** (e.g., Airbus, Applied Materials) lack evidence of actual commitment, and the **12 verified pairs** cite only PIB releases or Cabinet approvals—**not executed deals**. The claim conflates *documented intent* with *successful implementation*.
  2. **Double-counting risk**: The "final list" includes 147 names, but the **19 investor-scheme pairs** (12 verified + 7 prospective) suggest only a subset of these 147 are tied to government schemes. The article does not clarify how the 147 were filtered from the 2,217 joined names or whether some overlap with the 19 pairs.
  [confidence: high]
- *"Medical Devices has 7 foreign names and 0 India names in the final list, so that sector looks one-sided; check why before relying on it."* — **Apples-to-oranges comparison**:
  The article attributes the imbalance to an **unexplored "why,"** but the claim ignores that **India’s medical devices sector is dominated by foreign MNCs** (e.g., Johnson & Johnson, Siemens Healthineers) due to **IPR protections, R&D costs, and supply-chain dependencies**. The "one-sided" framing ignores **structural market realities** (e.g., India’s pharma sector is global leader in generics, but medical devices rely on foreign tech). The article treats this as a data quirk rather than a **policy-driven outcome**.
  [confidence: high]

---

**OUTDATED DATA:**
- *"Pairings were retrieved on 2026-07-20"* — The article was **revised on 29 October 2026**, but the **foreign_investor_initiative_pairs.json** (cited as the source) is not linked to a newer PIB release or Cabinet approval database. **Series to re-check**:
  - **PIB Press Releases (PRID numbers)** for verified pairs (e.g., Foxconn, Micron) — [PIB website](https://pib.gov.in/) (check for updates post-July 2026).
  - **Department for Promotion of Industry and Internal Trade (DPIIT) FDI data** — [DPIIT FDI portal](https://www.dpiit.gov.in/) (latest quarterly/annual reports).
  [confidence: high]
- *"19,795 companies in the global catalog"* — The article’s **country matrix** (focus_sector_country_matrix.csv) is dated to **19 October 2026**, but the **Damodaran industry classification** (underlying source) is typically updated **quarterly**. For a **current snapshot**, re-check:
  - **Damodaran’s "Global Industry Classification Standard (GICS)" updates** — [MSCI GICS](https://www.msci.com/gics) (latest version as of 2024).
  - **Bloomberg Terminal/Refinitiv Eikon** (if accessible) for live listed-company counts by sector.
  [confidence: medium]

---
