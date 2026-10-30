# Fact/interpretation check — how-to-use-india-ec-subsector-analysis

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-india-ec-subsector-analysis.html`

Text-SHA1: `1d77bd0596678f57`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "grant_rate = granted / (granted + ToR-granted + in-process), the repo's own definition." — This formula mathematically evaluates to approximately 48.8% for 5(f) (using the values: granted 669, tor 505, in_proc 136 -> 669 / 1310 = 51.06%), but the table directly above states Gujarat's grant rate as 51.1% and the summary table earlier in the text states the 5(f) grant rate as 48.8%, introducing an internal mathematical contradiction regarding how the rate is computed versus reported. [confidence: medium]

INTERPRETATION ERRORS:
- "Grant rate excludes delisted proposals (roughly 22% of the register), so it reflects live decisions only." — Excluding delisted proposals and defining the grant rate strictly as `granted / (granted + ToR-granted + in-process)` creates an upward bias in the "grant rate" metric, because applications that were abandoned, withdrawn, or administratively closed (delisted/dead) are dropped from the denominator rather than being treated as non-successes in the clearance pipeline. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“56.2% Gujarat's share of chemicals (5(f)) grants”** – The state‑wise table shows Gujarat received 669 granted proposals out of a total of 1,103 granted proposals for sub‑sector 5(f), which is **≈60.6 %**, not 56.2 % (or 53 % of total proposals). The figure quoted does not match the underlying CSV data. [confidence: high]  

- **“Grant rates differ sharply by activity (Construction 80.6 %, Mining 69.9 %, Townships 37.8 %, River valley 21.5 %)”** – The article lists “River valley 21.5 %” but the table labels this sub‑sector as **1(c) River Valley/Irrigation** with a grant rate of **21.5 %**; however the activity code for “River Valley/Irrigation” is **1(c)**, not “River valley” as a separate category. The wording conflates two distinct schedule codes, creating a mis‑labelled activity. [confidence: medium]  

**INTERPRETATION ERRORS**  
- **“Grant rate excludes delisted proposals (roughly 22 % of the register), so it reflects live decisions only.”** – Excluding delisted proposals removes a substantial portion of the dataset (≈22 %). This omission **inflates** the grant‑rate metric and does **not** guarantee that the resulting percentage represents “live decisions only”; it simply measures the proportion of *non‑delisted* proposals that have been granted. The conclusion that the rate “reflects live decisions” is therefore unsupported. [confidence: high]  

- **“Grant rates differ sharply by activity … pointing to where clearances actually stall.”** – A low grant‑rate can arise from many proposals being **still in‑process** rather than being stalled. Without distinguishing between pending and abandoned cases, using grant‑rate as a proxy for “stalling” is an **apples‑to‑oranges** comparison that overstates the causal link between low grant‑rate and procedural bottlenecks. [confidence: high]  

**OUTDATED DATA**  
- **“snapshot built 2026‑07‑22”** – The article was published on **28 October 2026** and presents the July snapshot as the definitive picture, yet the PARIVESH register is continuously updated. A newer snapshot (e.g., August/September 2026) is likely available and would change totals, grant‑rates, and the share calculations. The series to re‑check is the **PARIVESH Environmental Clearance register** for the period **July 2026 → October 2026**. [confidence: high]  

- **“roughly 22 % of the register” are delisted** – The 22 % figure is derived from the July 2026 snapshot. Given the acknowledged “live PARIVESH register has moved on,” the current proportion of delisted proposals may have shifted (e.g., higher after recent policy changes). The delisted‑percentage series should be refreshed against the latest PARIVESH data. [confidence: medium]

## Mistral open-mistral-nemo

Here’s the structured feedback based on the provided article text:

---

**FACTUAL ERRORS:**
- *"56.2% Gujarat's share of chemicals (5(f)) grants"* — The article later states Gujarat’s grant rate for sub-sector 5(f) is **51.1%** (from the state-wise table), not 56.2%. The 56.2% figure appears in the top-subsector table as Gujarat’s *share of total grants* (not grant rate) for 5(f), but the claim conflates these metrics. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Grant rates differ sharply by activity (Construction 80.6%, Mining 69.9%, Townships 37.8%, River valley 21.5%), pointing to where clearances actually stall."*
  The grant rates are calculated as **granted / (granted + ToR-granted + in-process)**, excluding delisted proposals. However, the article implies these rates directly indicate "stalling" (e.g., low rates = delays), which ignores:
  1. **Delisted proposals** (22% of the register) are excluded from the denominator, skewing rates upward for sectors with high delisting (e.g., River Valley).
  2. **ToR-granted** (terms-of-reference approvals) may not be final grants but are included in the denominator, inflating rates for sectors where ToRs are common.
  3. **In-process** proposals could reflect pending reviews, not necessarily stalled clearances (e.g., due to procedural delays vs. substantive rejections).
  The causal link between low grant rates and "stalling" is tenuous without accounting for these nuances. [confidence: high]

**OUTDATED DATA:**
- *"113,970 EC proposals in the committed snapshot (matches README)"* — The snapshot date is **2026-07-22**, but the article was revised on **28 October 2026**. While the data itself isn’t outdated, the claim of "latest" or "current" figures is misleading unless explicitly stated as of 2026-07-22. The PARIVESH 2.0 register likely has newer entries post-2026-07-22.
  - **Series to re-check**: PARIVESH 2.0 Environmental Clearance register (MoEFCC portal); newer period: **post-2026-07-22** (no official release date provided, but the article’s revision date suggests a gap). [confidence: high]

---
**Note**: No other distinct factual, interpretive, or outdated-data issues were identified in the provided text. The article’s methodological caveats (e.g., snapshot vs. time series, delisted exclusions) are correctly noted, but the quoted claims above require clarification.
