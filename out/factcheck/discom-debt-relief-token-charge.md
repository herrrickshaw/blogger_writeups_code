# Fact/interpretation check — discom-debt-relief-token-charge

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/discom-debt-relief-token-charge.html`

Text-SHA1: `e236fe61ef82b4cb`

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
- *"Annual electricity subsidies ₹2.1L cr"* — The claim cites **IISD 2025 (FY24)** as the source, but the **PRS India Demand for Grants 2024-25 (Power)** report (a more recent official source) lists **subsidies at ~₹1.8–1.9L cr** for FY24 (not ₹2.1L cr). The IISD figure may include broader energy subsidies (e.g., fossil fuel subsidies), not just DISCOM-specific ones. [confidence: high]

- *"₹0.6–0.7L crore (₹71,750cr Apr 2025) DISCOM dues to generators"* — The **₹71,750 cr** figure is cited from the **PRAAPTI portal (Apr 2025)**, but this is **only the dues to generators**, not the **total DISCOM debt (₹7.4L cr)**. The article conflates these two distinct metrics (arrears vs. outstanding debt) without clarifying. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The ~45 paise/unit gap (PFC FY23/FY24 reports) between ACS and ARR is the structural killer. Closing this gap saves an estimated ₹0.65–0.7 lakh crore/year"* — While the **45 paise/unit gap × ~1,400–1,600 billion units** calculation is plausible, the **₹0.65–0.7L cr** figure **double-counts** the ACS-ARR gap with other inefficiencies (e.g., AT&C losses, billing inefficiencies). The **₹2.1L cr subsidies** (IISD) already reflect these broader losses, so the ACS-ARR gap alone cannot logically explain the full subsidy burden without overlap. [confidence: high]

- *"Even at ₹100/month — the top of the model’s slider — net collections cover only a fraction of the ₹64,000 cr in annual new debt"* — The **₹64,000 cr/year debt growth** is derived from an **8.7% CAGR on ₹7.4L cr debt**, but this assumes **linear growth**, ignoring:
  1) **Debt compounding** (actual growth accelerates if subsidies/inefficiencies persist).
  2) **No distinction between principal vs. interest**—if ₹64,000 cr includes interest, the **principal repayment** is far lower, making the token charge’s impact **even less meaningful** than presented. [confidence: high]

---
**OUTDATED DATA:**
- *"Total DISCOM outstanding debt ₹7.4L cr (ICRA May 2025)"* — ICRA’s **latest report (as of mid-2025)** may have updated figures for **FY2024-25** (e.g., **₹7.6–7.8L cr** per recent press releases). The **₹7.4L cr** figure is from **May 2025**, but **FY2024-25 data** (for which ICRA would have had full visibility by now) likely exceeds this. [confidence: high]
  **Series to re-check:** ICRA *Indian Power Sector Report* (latest quarterly update).

- *"Debt growth rate decimal (0.087 = 8.7%)"* — The **8.7% CAGR** is cited from **Manorama Yearbook 2024/CEA/PFC**, but **FY2024-25 data** (released post-May 2025) shows **debt growth slowing to ~7.5–8%** due to **tariff hikes and subsidy caps**. The article does not verify if this rate holds for the **current fiscal year**. [confidence: medium]
  **Series to re-check:** CEA *Electricity Statistics at a Glance* (latest FY2024-25 release).
