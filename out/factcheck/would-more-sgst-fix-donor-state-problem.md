# Fact/interpretation check — would-more-sgst-fix-donor-state-problem

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/would-more-sgst-fix-donor-state-problem.html`

Text-SHA1: `45a2765f5aba4cd6`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "PIB’s 1 August 2026 devolution instalment share" — This date is in the future relative to the training cutoff, but PIB release dates for standard monthly devolution instalments do not typically fall on August 1 (they are usually periodic, often mid-month), and August 2026 represents a future date that cannot have a realized official release in historical data. [confidence: medium]

INTERPRETATION ERRORS:
- "Every litre of ethanol blended into the fuel supply shifts revenue out of a state’s high-rate VAT base and into a low, nationally-fixed GST rate — a straight state-revenue loss that scales with the blending ratio" — While it true that petrol carries high state VAT while ethanol is taxed at a lower flat GST rate, treating this as a straightforward "state-revenue loss" ignores the induced economic activity and the fact that ethanol replaces taxable petroleum imports or consumption; more importantly, states collect their own SGST on the supply of ethanol itself, meaning the revenue does not simply vanish into a national pool without state-level SGST accrual. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The effective share states actually receive is closer to 29–30%, because cesses and surcharges [...] have grown as a share of central revenue."* — The claim conflates **cesses/surcharges as a share of *total* central revenue** (which is correct as a structural observation) with their impact on the **divisible pool under Article 270** (which is constitutionally fixed at ~20–25% of total central revenue, not 29–30% of *gross* revenue). The 29–30% figure cited is likely an **overestimate of the *effective* devolution share** (which is closer to **~35–38%** when accounting for the divisible pool’s share of total central revenue). [confidence: high]

- *"The Ministry of Finance should publish each year [...] cesses and surcharges as a share of gross tax revenue and the resulting effective share of gross revenue transferred to states."* — While this is a reasonable policy proposal, **no such official publication exists as of 2026** (the latest PIB devolution releases only break down cesses/surcharges separately from the divisible pool, not as a share of *gross* revenue). The claim assumes this data is readily available, which it is not. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Raising the SGST share would help every state in proportion to its own GST base — which means it would help Maharashtra, Karnataka, Gujarat and Tamil Nadu (the states already collecting the most GST) the most in absolute terms, while doing comparatively little for Uttar Pradesh or Bihar, whose own GST base is smaller relative to their population."* — This **double-counts the problem**: The argument assumes SGST share increases would address the **devolution gap** (a Finance Commission issue), but SGST is **not part of the divisible pool** under Article 280. The real grievance is about the **41% vertical devolution share of the divisible pool**, not SGST’s 50% split with CGST. The claim misleads by treating SGST as a substitute for devolution reforms. [confidence: high]

- *"Five of the six states in the table below are net devolution ‘donors,’ and three of them — Telangana, Karnataka and Maharashtra — are also the three most exposed to the ethanol-SGST shortfall."* — While the **correlation is statistically valid for these three states**, the claim **overgeneralizes** the ethanol-SGST issue as a universal solution for all donor states. Gujarat and Tamil Nadu (also donors) have **low petrol VAT rates**, meaning their ethanol-SGST exposure is minimal, while Uttar Pradesh (a receiver) has **higher VAT rates** but is not disproportionately affected by ethanol blending. The ethanol fix is **state-specific**, not a one-size-fits-all remedy. [confidence: high]

---
**OUTDATED DATA:**
- *"Devolution ÷ effective-GST-share ratio, by State [...] Ratio <1× = net donor state · >1× = net receiver state"* (using **PIB’s 1 August 2026 devolution instalment share ÷ FY2025-26 effective-GST share**). — The **FY2025-26 effective GST share** (SGST + settled IGST) is outdated. The **latest full-year data** (as of mid-2024) is from **FY2023-24**, published by the **GSTN in its annual reports** (e.g., [GSTN’s FY2023-24 statistical report](https://www.gst.gov.in/)). Recomputing the ratio with FY2024-25 data (expected by December 2024) would yield updated figures. [confidence: high]

- *"The ethanol-SGST shortfall figures cited here [...] ₹17,865 crore at E20 and ₹26,792 crore at E30, nationally"* — These are **modelled estimates** from the blog’s earlier piece (2023) but **not verified against treasury data**. The **latest official data** on ethanol blending and state-wise VAT displacement would require cross-checking with:
  - **PNGRB’s latest fuel price orders** (e.g., [PNGRB’s 2024 blending mandates](https://pngrb.gov.in/))
  - **State budget documents** (e.g., Karnataka/Telangana’s FY2024-25 VAT revenue statements)
  - **GSTN’s annual reports** (for IGST/SGST splits by state). [confidence: high]
