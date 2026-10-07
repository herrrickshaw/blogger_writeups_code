# Fact/interpretation check — the-case-for-biofuels-over-imports

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-case-for-biofuels-over-imports.html`

Text-SHA1: `79839f2bd7344557`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Raising ethanol's SGST rate is a GST Council decision requiring a 3/4 weighted-majority vote (states two-thirds, Centre one-third)" — GST Council voting rules under Article 279A of the Constitution require a majority of not less than three-fourths of the weighted votes of the members present and voting, where the Centre's vote has a weight of one-third (33.33%) of the total votes cast, and all the states combined have a weight of two-thirds (66.67%) of the total votes cast, but decisions are practically taken by consensus rather than a strict 3/4 majority split of states versus Centre. [confidence: medium]

INTERPRETATION ERRORS:
- "Lowering CNG VAT in specific states is, by contrast, entirely within each state's own budget-making power, the same lever Karnataka used in 2024 to raise its own petrol/diesel VAT... proof states will move unilaterally on fuel taxation when the decision is theirs alone, and a reminder that the CNG-VAT half of this package doesn't need Council consensus even though the ethanol-SGST half does." — CNG (compressed natural gas) and natural gas are not outside the GST framework like petrol and diesel; natural gas is subject to central excise and state VAT or GST depending on the specific product form, but natural gas was actually brought under the GST regime at a 5% rate (with differing treatment for input tax credits across states historically), meaning a state does not have unilateral discretion to set arbitrary VAT rates on CNG in the same manner as non-GST petroleum products like petrol and diesel. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India's ethanol programme has already substituted a real, cumulative **244 lakh metric tonnes of crude oil** since ESY 2014-15, saving an estimated ₹1.44 lakh crore in crude import costs and ₹1.84 lakh crore in foreign exchange overall"* —
  The Ministry of Petroleum’s figures for cumulative ethanol substitution are **not independently verified** by this article, and the methodology behind the **244 lakh MT claim** (e.g., how blending volumes translate to crude displacement) is **not disclosed**. While the Ministry reports these numbers, the article does not confirm their accuracy or provide transparency on how they were calculated (e.g., whether they account for indirect savings, refinery margins, or non-crude inputs in ethanol production). [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Raising ethanol's SGST rate from today's **2.5% to the standard 18% GST slab closes over half the national ₹17,865 crore VAT-shortfall gap**"* —
  The claim conflates **net revenue impact** with **policy feasibility**. While the modelling shows that raising the rate to 18% reduces the shortfall by 56.3%, this assumes:
  1. **All states uniformly adopt the 18% rate** (which requires GST Council consensus, a political hurdle not addressed).
  2. **No compensatory adjustments** (e.g., if states lose petrol VAT revenue, they may not pass through the full SGST increase to consumers, limiting the effect).
  3. **The ₹17,865 crore gap is static**, but actual foregone VAT depends on **real-time blending volumes**, which the article acknowledges are **modelled** (not official data). The argument treats the gap as a fixed target rather than a dynamic variable tied to policy implementation. [confidence: high]

- *"Higher blending genuinely does ease the competition between transport-fuel demand and petrochemical feedstock demand"* —
  The claim is **directionally correct** but **not empirically quantified**. The article states this is a **"structural"** argument, but it lacks:
  - **Refinery-level data** on how much crude is allocated to transport fuel vs. petrochemical feedstock (e.g., naphtha yields).
  - **Temporal evidence**: Even if blending rises, **petrochemical demand growth** (e.g., for plastics) may outpace any freed-up crude, nullifying the effect. The piece admits this requires data it doesn’t have, making the causal link **speculative**. [confidence: high]

---
**OUTDATED DATA:**
- *"Share of India's **₹17,865 crore national VAT-shortfall gap** closed, by ethanol SGST rate"* —
  The **₹17,865 crore figure** is based on **PPAC FY2024-25 state petrol consumption data** and an assumed **E20 blend**. However:
  - **No newer official estimate** of the VAT foregone gap exists (e.g., from PPAC or GST Council post-FY2024-25).
  - **Actual blending data** (e.g., monthly volumes by state) is **not published**, as the article itself notes. The claim should be rechecked against:
    - **PPAC’s latest state-wise ethanol blending reports** (if available post-FY2024-25).
    - **GST Council’s official state-by-state VAT foregone estimates** (if any). [confidence: high]

- *"Ministry of Petroleum's own figures: **244 lakh MT crude substituted since ESY 2014-15**"* —
  The article cites these as **Ministry-reported**, but:
  - **No update since ESY 2014-15** is provided (e.g., for ESY 2023-24 or 2024-25).
  - The **methodology for calculating substitution** (e.g., whether it includes indirect savings like reduced refining costs) is **not disclosed**. Recheck:
    - **Ministry of Petroleum’s latest Ethanol Supply Year (ESY) reports** (e.g., ESY 2023-24 or 2024-25) for updated substitution figures.
    - **PIB press releases** on ethanol blending milestones. [confidence: high]
