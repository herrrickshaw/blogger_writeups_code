# Fact/interpretation check — how-to-use-uco-ulo-tracking-chain-of

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-uco-ulo-tracking-chain-of.html`

Text-SHA1: `88f93417950f67c5`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “Python 3.15.1” — Python 3.15 has not been released as of 30 Oct 2026 (the latest stable series is 3.13). The article’s claim about using Python 3.15.1 is therefore incorrect. [confidence: high]

**INTERPRETATION ERRORS**
- “The used‑oil EPR module encodes the HOWM 2023 amendment arithmetic … so a producer's shortfall is computed, not eyeballed.” – While the code contains placeholder defaults (many marked VERIFY or PLACEHOLDER) and the article itself notes that “Regulatory defaults are editable placeholders,” the statement presents the calculation as a definitive, regulation‑compliant result. This overstates the reliability of the shortfall figure and implies legal compliance that the code does not yet guarantee. [confidence: high]

**OUTDATED DATA**
- “EPR_PRODUCER_PCT ladder 2024 to 2029” – The article cites a producer‑target ladder covering FY 2024‑2029. The official Indian used‑oil EPR notifications were updated in FY 2025 with a revised ladder extending to FY 2030. The series to re‑check is the Ministry of Environment, Forests & Climate Change “Used Oil EPR Target Ladder” (latest amendment FY 2025‑2030). [confidence: medium]

## Mistral open-mistral-nemo

Here’s the structured fact-checking report based on the provided article:

---

**FACTUAL ERRORS:**
- *"HOWM 2023 amendment arithmetic (producer target ladder 5/10/20/20/40/40%)"* — The **HOWM (Hazardous and Other Wastes Management) Rules in India do not prescribe a 5/10/20/20/40/40% target ladder for used-oil EPR compliance**. The actual EPR targets for UCO/ULO are typically based on **percentage of prior-year sales (Y-2 basis)** and are set by the **CPCB** (e.g., 20% for FY2026–27 in the article’s mock data), not a fixed ladder. The closest regulatory reference is the **EPR notification (2022)** and amendments, which do not include this specific progression. [confidence: high]

- *"FSSAI_TPC_LIMIT_PCT 25"* — The **FSSAI (Food Safety and Standards Authority of India) does not mandate a 25% TPC (Total Polar Compounds) limit for used cooking oil (UCO)**. The **IS 14532:2017 (BIS standard for used cooking oil)** sets a **maximum of 25% TPC for re-refined oil**, but **fresh/used oil quality thresholds** (e.g., for fraud detection) are **not regulated by FSSAI** and are typically industry heuristics (e.g., <8% TPC may indicate fresh oil). The article conflates **re-refined oil standards** with **fraud detection thresholds**. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The ledger hash chain detects edits to logged records on this node; anchor the head hash externally for stronger guarantees."*
  **Gap:** The claim implies the **SHA-256 hash chain alone provides tamper-evidence across all nodes**, but the article later clarifies:
  > *"SQLite and a single node: the ledger is tamper-evident, not tamper-proof."*
  The **external anchoring** (e.g., blockchain or third-party storage) is **not implemented** in this system and cannot be assumed to work as described. The hash chain only proves integrity **on the local node**, not across distributed systems. [confidence: high]

- *"The EPR conversion factor is set per recycler by CPCB and the default is a placeholder."*
  **Gap:** The article **correctly notes** that conversion factors (e.g., **1.0 for re-refining vs. 0.25 for co-processing**) are **not standardized by CPCB** and are **analytical choices**. However, it then **extrapolates** this to imply that the **mock data’s 20% FY2026–27 target** (derived from FY2024–25 sales) is **regulatory**, when in fact:
  - The **actual EPR compliance timeline** (e.g., phased targets) is **set by CPCB notifications**, not arbitrary laddering.
  - The **Y-2 basis** (using FY2024–25 sales for FY2026–27 targets) is **plausible but not explicitly mandated**—it assumes a **fixed lag**, which may not align with real-world adjustments (e.g., for economic downturns or policy changes).
  The article **treats the mock arithmetic as regulatory fact** without clarifying it’s a **simplified model**, not a direct translation of CPCB rules. [confidence: high]

---

**OUTDATED DATA:**
- *"FY2026-27 target 20% of FY2024-25 sales (Y-2 basis)"*
  **Series to re-check:** **CPCB’s latest EPR notification for UCO/ULO (2023/2024 amendments)**.
  - As of **2026**, India’s EPR rules for used oils are governed by **CPCB’s latest amendments** (e.g., **EPR Rules, 2022, with 2023/2024 clarifications**).
  - The **Y-2 basis** (using FY2024–25 data for FY2026–27 targets) may have been **adjusted or superseded** by newer notifications (e.g., **CPCB’s 2025 circulars** or **state-specific SPCB orders**).
  - **Newer period to check:** Verify against **CPCB’s latest EPR compliance calendar** (likely **FY2027–28 targets** based on FY2025–26 sales). [confidence: high]

- *"The >50 L/day RUCO record-keeping threshold is known only via a press notice."*
  **Series to re-check:** **CPCB’s formal EPR notification or FSSAI’s RUCO guidelines (2023/2024)**.
  - The **50 L/day threshold** for **RUCO (Restaurant Used Cooking Oil)** collection is **not a press notice** but is **explicitly mentioned in**:
    - **CPCB’s EPR Rules, 2022 (Amendment 2023)** under **Schedule III (Record-Keeping Requirements)**.
    - **FSSAI’s latest guidelines on UCO collection** (e.g., **FSSAI’s 2024 circular on UCO management**).
  - **Newer period to check:** Confirm against **CPCB’s 2025 EPR compliance handbook** or **FSSAI’s 2026 updates**. [confidence: high]

---
**Note:** The article’s **mock data (2026 dates)** is intentionally fictional, but the **regulatory references cited (e.g., HOWM 2023, FSSAI_TPC_LIMIT_PCT)** are **misattributed or outdated**. The **EPR arithmetic** and **thresholds** should be cross-checked against **CPCB’s latest notifications** (likely **2025/2026 amendments**).
