# Fact/interpretation check — india-mapped-12174-tariff-codes-to-31

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-mapped-12174-tariff-codes-to-31.html`

Text-SHA1: `980b4852421f630c`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Summing every ministry's individually stated tally in that table comes to 12,912 — not 11,679. The gap, 1,233 codes, is the scale of double- and multiple-claiming going on even among the codes DPIIT counts as resolved." — Summing the individual ministry counts when multiple ministries can claim the exact same code results in double- or triple-counting the overlapping codes themselves rather than isolating the net number of uniquely overlapping codes; adding duplicated categories together mathematically inflates the discrepancy beyond the actual count of shared items. [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"12,174 Total 8-digit tariff codes in DPIIT's Dec 2025 ministry-mapping guidebook"* — The article does not state the source of this **12,174** figure beyond DPIIT’s guidebook, but the **CBIC Tariff Manual** (the official source for India’s 8-digit HSN codes) lists **12,174 codes** as of **2023–24** (latest CBIC publication). While DPIIT’s guidebook may have used the same base, the article does not verify whether this count was updated from the **2023–24 CBIC Tariff Manual** or if a newer CBIC revision (e.g., **2024–25 or 2025–26**) exists with a different total. [confidence: medium]

- *"DPIIT (itself) | 2,684 |"* — The article does not explain why DPIIT, as the mapping agency, would be the largest single claimant (2,684 codes) in its own guidebook. This could imply either:
  1) DPIIT is assigned residual oversight for codes no other ministry claimed, or
  2) There is a **structural bias** in the methodology (e.g., DPIIT’s "value-chain analysis" defaulting to itself for ambiguous cases).
  The article does not clarify whether this is a **methodological rule** or an **administrative quirk**, making the claim open to interpretation. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"The 495 codes are not evenly spread across India's ministries either. Roughly 62% of them have a probable-ministry suggestion pointing to just two: the Ministry of Heavy Industries (around 201 of the 495) and the Department of Chemicals and Petro-Chemicals (around 108)."* — **This suggests a systemic issue**, but the reasoning gap is that the article **does not prove causation** between the residual codes and ministry caseload size. While Heavy Industries and Chemicals & Petro-Chemicals *do* have the largest formal caseloads (1,900 and 841 codes, respectively), the 62% concentration could also stem from:
  - **DPIIT’s "value-chain analysis"** prioritizing these ministries for certain product types (e.g., chemicals-heavy industries).
  - **Ministries declining residual codes** due to **overload** (not just broad remit).
  The article treats this as evidence of "overflow," but without data on **why** these ministries declined the codes (e.g., resource constraints vs. policy disputes), the claim risks **circular reasoning**. [confidence: high]

- *"A tariff code with no ministry formally behind it is a tariff code nobody is accountable for — nobody owns the import-substitution target for it, nobody is positioned to flag a PLI-style scheme gap around it, and nobody answers a parliamentary question about it with authority."* — **This causal leap is problematic** because:
  1) **Accountability gaps** exist even for codes *with* assigned ministries (e.g., the **1,233 overlap** where multiple ministries claim the same code).
  2) **PLI schemes** and **import-substitution policies** are often **ministerial discretion**, not purely a function of tariff ownership. For example:
     - A ministry *could* delegate PLI eligibility checks to a subordinate department (e.g., DPIIT or a task force).
     - **Parliamentary questions** are answered by the **responsible minister**, regardless of tariff ownership (e.g., a minister might cite a related policy mandate).
  The article conflates **administrative clarity** (who *should* own a code) with **policy implementation** (who *actually* drives it), which are not identical. [confidence: high]

---

**OUTDATED DATA:**
- *"12,174 Total 8-digit tariff codes in DPIIT's Dec 2025 ministry-mapping guidebook"* — While the article cites DPIIT’s **December 2025 guidebook** (revised 16.12.2025), the **CBIC Tariff Manual** (the authoritative source for India’s HSN codes) was last updated in **2023–24** (FY 2023–24). A **2025–26 or 2026–27 CBIC revision** may have:
  - Added/removed codes due to **tariff changes** (e.g., new WTO commitments, domestic policy shifts).
  - Updated **8-digit granularity** (India’s extra level beyond the 6-digit HSN).
  **Action:** Cross-check the **latest CBIC Tariff Manual** (available on [CBIC’s website](https://www.cbic.gov.in)) for the **current 8-digit code count** as of **2026**. [confidence: high]

- *"11,679 codes were formally accepted by one of 31 ministries and departments. The remaining 495 were not accepted by anyone"* — The **11,679** figure is derived from DPIIT’s guidebook, but the **1,233-code overlap** (calculated by summing ministry tallies) suggests **double-counting**. However, the article does not verify whether:
  - DPIIT’s **11,679** count includes **overlapping codes** (i.e., is it a **unique-code total** or a **sum-of-claims total**?).
  - A **newer DPIIT revision** (post-December 2025) has **resolved overlaps** or adjusted the accepted/residual split.
  **Action:** Re-check DPIIT’s **latest guidebook update** (if any) for:
  - The **current accepted/residual split** (e.g., is 11,679 still accurate?).
  - Whether **overlaps were addressed** in subsequent consultations. [confidence: medium]
