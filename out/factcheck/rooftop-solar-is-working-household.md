# Fact/interpretation check — rooftop-solar-is-working-household

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/rooftop-solar-is-working-household.html`

Text-SHA1: `5e03329da8b68968`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The government's own estimate is that rooftop solar across one crore households would generate roughly 1,000 billion units of renewable electricity and avoid about 720 million tonnes of CO₂e over a 25-year system life." — Multiplying a lifetime output of 1,000 billion units (kWh or TWh) over 25 years by standard grid emission factors yields a much lower carbon offset than 720 million tonnes of CO₂e. At a generous emission factor of ~0.8 kg CO₂e per kWh (typical for India's grid), 1,000 billion kWh corresponds to roughly 800 million kg (0.8 million tonnes) or if units are interpreted as thousand million kWh (TWh), 1,000 TWh × 0.8 t/MWh = 800 million tonnes gross, but avoided emissions calculations must account for grid displacement factors and auxiliary losses, meaning the 720 million tonnes figure vastly overstates the carbon avoidance per unit of generation compared to standard lifecycle and grid-displacement methodologies. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"₹78,000 Maximum central subsidy, 3 kW and above"* — The subsidy slab for **3 kW and above** is **₹78,000 total**, but the **marginal rate drops to 40%** for the 2–3 kW segment (not a flat ₹78,000 for all sizes above 3 kW). The claim conflates the **cap** (₹78,000 for ≥3 kW) with the **fixed slab** (which remains ₹78,000 regardless of size beyond 3 kW, as later clarified in the table). The wording misleads readers into thinking the subsidy scales with system size beyond 3 kW. [confidence: high]

- *"12 GW Rooftop capacity added since Feb 2024"* — The **PIB figure cited (9,566.89 MW as of 20.03.2026)** is **below 12 GW**, and the **May 2026 figure (~12 GW)** is likely cumulative (including pre-Feb 2024 capacity). The claim implies **all 12 GW is post-Feb 2024**, which contradicts the later statement that the scheme "crossed 40 lakh beneficiary households within its first two years" (Feb 2024–Feb 2026). [confidence: high]

---
**INTERPRETATION ERRORS:**
- *"Rooftop under this one scheme is therefore roughly 8% of all solar capacity in the country, built in two years"* — The **8% figure (12 GW / 150 GW total)** is correct, but the **causal claim** that this is due to the **PM Surya Ghar scheme alone** is misleading. India’s rooftop growth has been driven by **multiple factors** (e.g., state-level incentives, falling panel costs, DISCOM pressure to reduce imports), not just this central scheme. The article later acknowledges **grid-scale storage subsidies** as a parallel policy, but the implication that the scheme’s design alone explains the 8% share is **overstated**. [confidence: high]

- *"The marginal rate steps down from 60% to 40% in the third kilowatt, then stops entirely — a deliberate nudge toward small, domestic-load systems"* — While the **subsidy structure** does incentivize smaller systems, the claim **overgeneralizes the intent**. The **flat cap at ₹78,000 for ≥3 kW** also **disincentivizes larger systems** (e.g., a 5 kW system gets the same subsidy as a 3 kW one), but this is **not framed as a "nudge"**—it’s a **hard constraint**. The reasoning conflates **behavioral nudges** with **policy constraints**. [confidence: medium]

---
**OUTDATED DATA:**
- *"India's total solar fleet is 150.26 GW (FY2025-26), rising to 162.15 GW in FY2026-27"* — These figures are from the **NITI Aayog dashboard (as of the article’s sources)**, but **FY2026-27 data is now outdated** (the fiscal year ended 31 March 2027). For **current capacity**, check:
  - **MNRE’s latest monthly bulletin** (e.g., [MNRE Solar Power Monthly Bulletin](https://mnre.gov.in/)) for **FY2027-28** or **April 2027 onward**.
  - **CEA’s latest "Electricity Statistics at a Glance"** (quarterly updates).
  [confidence: high]

- *"30 GWh approved, plus 13.2 GWh already underway | VGF outlay: ₹5,400 crore"* — The **₹5,400 crore VGF outlay** was announced in **2023–24**, but **new allocations or revisions** (e.g., under the **2024–25 Budget**) may have expanded the scheme. For **current status**, verify:
  - **Ministry of Power’s latest VGF updates** (e.g., [Power Ministry’s VGF page](https://powermin.nic.in/)).
  - **CEA’s latest storage requirement assessments** (e.g., [CEA’s 2024–25/2025–26 reports](https://cea.nic.in/)).
  [confidence: high]
