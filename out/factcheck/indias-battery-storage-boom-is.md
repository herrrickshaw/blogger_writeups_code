# Fact/interpretation check — indias-battery-storage-boom-is

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-battery-storage-boom-is.html`

Text-SHA1: `d187b4a997a3fd42`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India's installed grid-scale battery storage capacity multiplied roughly ninefold in the first three months of 2026"* — The claim conflates two distinct metrics: Mercom reports a **941% jump in capacity added** (from 442.7 MWh in Q4 2025 to 4.6 GWh in Q1 2026), not a ninefold *multiplication* of the base (1.08 GWh → ~5.9 GWh). The "84-fold" claim later in the text is similarly misleading because it compares **98.4 MWh (H1 2025)** to **9.3 GWh (H1 2026)**, which is a **95x increase**, not 84x. The base is so small that even modest additions create disproportionate year-on-year percentages. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Discovered battery-storage tariffs have fallen roughly twice as fast as the battery packs behind them actually got cheaper"* — While the **36.5% decline in battery pack costs (2022–2025)** is plausible, the claim conflates **discovered tariffs** (which reflect aggressive bidding, subsidies, and project-specific conditions) with **underlying hardware costs**. The IEEFA/JMK viability benchmark (₹2.3 lakh/MW/month) is an **analyst judgment**, not a government-verified threshold, and assumes fixed margins (e.g., 15–20% IRR) that may not hold for all projects. The "twice as fast" claim ignores:
  1. **Subsidy effects**: VGF-backed tenders (e.g., ₹2.22 lakh in Jan 2025) distort comparisons with unsubsidized ones (e.g., ₹1.48 lakh in Dec 2025).
  2. **Duration differences**: Four-hour systems (₹2.85 lakh) aren’t directly comparable to two-hour record lows (₹1.48 lakh).
  3. **Non-hardware costs**: Grid interconnection, O&M, and financing gaps aren’t factored into the "cheaper hardware" baseline. The analysis treats tariff declines as purely cost-driven, but the IEEFA/JMK report itself notes **"aggressive, possibly unsustainable bidding"** as the primary driver. [confidence: high]

---
**OUTDATED DATA:**
- *"As of 31 December 2025, India's cumulative installed BESS capacity stood at roughly 1,082 MWh (about 1.08 GWh)"* — Mercom’s **March 2026 report** (cited in the article) already shows **5.9 GWh by end-March 2026** and **9.3 GWh by mid-2026**. The 1.08 GWh figure is outdated by **6+ months** and contradicts the article’s own timeline. For the latest installed capacity, re-check Mercom India’s **quarterly tracking series** (e.g., [Mercom’s H1 2026 report](https://mercomindia.com)) or the **Central Electricity Authority’s (CEA) latest installed capacity dashboard** (though the article notes CEA’s site was unreachable). [confidence: high]

---
**Note on "none found":**
- No **apples-to-oranges comparisons** (e.g., mixing GW and GWh for tendered capacity) were flagged separately because the article explicitly acknowledges the unit inconsistencies (Section 5) and treats them as methodological gaps rather than factual errors. The discrepancies are noted as unresolved, not misrepresented.
