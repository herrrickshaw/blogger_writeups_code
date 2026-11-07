# Fact/interpretation check — doubling-indias-csr-profit-trigger

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/doubling-indias-csr-profit-trigger.html`

Text-SHA1: `b4a45740e8596cad`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUALERRORS:
- none found

INTERPRETATIONERRORS:
- "Their combined obligation is about Rs 1,282 crore, against Rs 40,794 crore spent in 2024-25... about 3.1% of the Rs 40,794 crore companies reported spending in 2024-25" — The article compares an estimated obligation figure for one future period (2025-26) directly against actual reported spending figures from a past period (2024-25) to derive a percentage share. Obligations (what companies are legally required to set aside) and actual expenditures frequently differ due to unspent amounts, carry-forwards, or voluntary overspending, making this an apples-to-oranges comparison of mismatched metrics and timeframes. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “The penalty is twice the unspent amount or Rs 1 crore, whichever is lower.” — Under Section 135(5) of the Companies Act 2013 the penalty is *twice the unspent amount, but not less than* Rs 1 crore (i.e., the higher of the two). The article reverses the “higher/lower” condition. [confidence: high]

**INTERPRETATION ERRORS**
- “The 11,204 companies that would leave are about 46 % of them, and their obligation is about 3.1 % of the money… the loss will be small.” — The article equates the *obligation* share (3.1 %) with the *actual spending* share that would be lost. Obligations are statutory targets; many firms under‑spend or over‑spend relative to them. Therefore, using the obligation proportion to infer the magnitude of the real spending loss is a false causal inference. [confidence: high]

**OUTDATED DATA**
- “In 2024‑25, 24,228 companies reported CSR spending, totalling Rs 40,794 crore.” — By November 2026 the CSR data for FY 2025‑26 (ending March 2026) should have been released by the MCA/National CSR Data Portal. The article relies on the prior‑year figure as “latest complete year,” which is likely superseded. The series to re‑check is the MCA CSR spending data for FY 2025‑26. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Rs 40,794 crore spent in 2024-25"* — The article cites this as the **latest complete year** for CSR spending, but the **MCA’s National CSR Data Portal** (as referenced in the IICA Factbook) shows **Rs 34,909 crore** for FY 2023-24 (the most recent *fully* reported fiscal year in the portal’s historical data). The Rs 40,794 crore figure appears to be a **forward projection or preliminary estimate** (not yet finalized), not a confirmed total for 2024-25. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Their combined obligation is about Rs 1,282 crore, against Rs 40,794 crore spent in 2024-25"* — The claim conflates **obligations (2025-26 estimates)** with **actual spending (2024-25 reported totals)**. While the comparison highlights the *proportion* (3.1%), it ignores that:
  1. **2025-26 obligations** are based on *projected* company data (not yet realized spending).
  2. **2024-25 spending** includes *voluntary* contributions from companies **not** in the Rs 5–10 crore profit band (e.g., the 380 companies with no obligation that spent Rs 809 crore). The Rs 1,282 crore figure thus **understates** the actual loss if voluntary spending by exiting companies is factored in. [confidence: high]

- *"93 companies spending Rs 50 crore or more each account for 42.4% of all CSR money"* — This is **correct data**, but the article **overgeneralizes** its implication: it suggests these 93 companies are the *only* major spenders, ignoring that:
  - The **Rs 1–10 crore spend band** (15.4% of companies) contributes **44.3%** of total CSR (per IICA’s partial data). The article’s focus on outliers (top 0.4% of firms) **distorts** the distribution’s true concentration. [confidence: medium]

**OUTDATED DATA:**
- *"Reported CSR spend, Rs crore [FY15: 10,066 → FY25: 40,794]"* — While the trend is accurate, the **FY2018-19 to FY2020-21 figures** (marked with asterisks) are **not strictly comparable** to later years due to:
  - **Portal revisions**: The MCA portal updates historical data as late filings are processed (e.g., FY2020-21’s Rs 26,211 crore was later revised upward).
  - **Source gaps**: FY2019-20 uses an **MCA statement (Feb 2026)**, while FY2020-21 relies on a **Factly snapshot (Aug 2023)**, which may not reflect finalized MCA data.
  **Re-check**: MCA National CSR Data Portal (latest fiscal year updates); newer period: **FY2025-26 (if published)** or **FY2026-27 (next full release)**. [confidence: high]
