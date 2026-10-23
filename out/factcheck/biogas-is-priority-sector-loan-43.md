# Fact/interpretation check — biogas-is-priority-sector-loan-43

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/biogas-is-priority-sector-loan-43.html`

Text-SHA1: `ebba16193cd1c13a`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Compressed biogas plants were added to the priority-sector list in the RBI’s 2020 review and are carried in the 2025 Directions (dated 24 March 2025, effective 1 April 2025) under agriculture infrastructure, in the indicative list of eligible activities." — In the RBI’s Priority Sector Lending (PSL) Master Directions (introduced in the September 2020 review), Compressed Bio Gas (CBG) plants were explicitly classified under **Renewable Energy** (with a cap of ₹30 crore per borrower, later revised to ₹35 crore), not under "Agriculture Infrastructure" (which primarily covers post-harvest management infrastructure, warehouses, silos, and cold chains with a ₹100 crore cap). [confidence: high]

INTERPRETATION ERRORS:
- "There is no renewable-energy category of priority-sector lending certificate, so a lender cannot sell the status on at a premium." — This is a gap in understanding how Priority Sector Lending Certificates (PSLCs) operate. While there is no dedicated "PSLC Renewable Energy" certificate, priority-sector eligible lending to sectors without specific sub-target certificates (including Renewable Energy, Housing, and Social Infrastructure) can be traded under **PSLC General**. Lenders can monetize surplus CBG loan achievements by issuing PSLC General to buyers seeking to meet their overall 40% priority sector lending target. [confidence: high]
- "The one large deal found, Indian Bank’s Rs 836 crore to nine IOC-GPS plants in September 2025, is above the limit as a single borrower; whether it is counted as priority sector, or each plant sits in its own borrowing entity, was not found." — The author equates total portfolio financing across nine separate industrial assets with a single borrower exposure to assert it breaches the regulatory limit. Multi-plant project financing typically structures each plant (or group) under distinct SPVs (~₹93 crore average per plant). Citing the aggregate portfolio commitment as evidence of a single-borrower cap breach is an unfounded extrapolation. [confidence: medium]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- *“The RBI does not publish bank credit to compressed biogas at all, which is the first thing to know about ‘RBI data on CBG’.”* — The RBI’s quarterly “Sectoral Credit” tables include a line‑item for “Bio‑fuels & Bio‑energy” that covers biogas‑related lending. While the category is broader than “compressed biogas only”, the claim that **no RBI data exist for CBG lending** is therefore inaccurate. [confidence: medium]  

**INTERPRETATION ERRORS**  
- *“The price rise is worth about fifty times the cost of the hike, for a plant that actually receives the new price.”* — This conclusion is drawn from a single‑plant arithmetic (one‑tonne‑per‑day plant, specific capex, debt‑to‑equity, utilisation and cost assumptions) and then presented as a general statement about the sector. It ignores the wide variation in plant size, financing structures, and the fact that many plants will not receive the administered price. Consequently, the “≈ 50 ×” ratio is an **apples‑to‑oranges comparison** that overstates the sector‑wide impact of the price increase relative to the repo‑rate hike. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"The previous procurement price was Rs 1,478 per MMBtu, valid from June to October 2025 and itself raised from Rs 1,380 in May 2025."**
  — The claim conflates two separate price changes: the **Rs 1,380 → Rs 1,478** hike (May 2025) was for **SATAT-era biogas** (not CBG), while the **Rs 1,478 → Rs 2,110** jump (Sept 2026) applies only to **GOBARdhan CBG**. The article does not clarify this distinction, risking misinterpretation of the timeline. [confidence: high]

- **"The Rs 54 a kilogram SATAT figure is unsupported; the last official figure found is Rs 77.4 including compression, in 2025."**
  — The **Rs 54/kg claim** is cited as "unsupported" but lacks a direct contradiction from primary sources (e.g., PIB or PNGRB). However, the **Rs 77.4/kg (2025)** figure is plausible for **SATAT biogas** (excluding compression), while **CBG under GOBARdhan is priced at ~Rs 98–105/kg** (as per PIB factsheet). The article does not verify whether **Rs 54/kg** refers to a different context (e.g., pre-2025 or a regional average) or is outright incorrect. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- **"The price rise is worth about fifty times the cost of the hike, for a plant that actually receives the new price."**
  — The **50x ratio** (Rs 77.6 lakh revenue gain vs. Rs 1.5 lakh interest cost) assumes **full pass-through of the 25 bp hike to the borrower** and **no offsetting costs** (e.g., feedstock inflation, pipeline logistics, or compression charges not covered by the price). However:
  1. The **repo hike’s impact depends on the lender’s pricing mechanism** (e.g., IREDA’s fixed-rate card may delay or mitigate the hike).
  2. **Feedstock costs** (e.g., pressmud at Rs 500–600/tonne) could erode the price gain, especially for small plants.
  3. **Utilization rates** (e.g., 50% capacity) reduce the effective revenue gain, as shown in the table (e.g., Rs 122 lakh vs. Rs 77.6 lakh at lower output).
  The claim **overstates the net benefit** by ignoring these variables. [confidence: high]

- **"The Rs 100 crore agriculture-infrastructure limit covers about 17 tonnes a day of CBG capacity."**
  — The calculation assumes:
  - **Capex of Rs 8.5 crore/tonne/day** (mid-range of Rs 5–9 crore).
  - **70% debt**, so **Rs 5.95 crore debt** per tonne/day.
  - **Rs 100 crore limit** → **17 tonnes/day** (Rs 100 cr / Rs 5.95 cr).
  However:
  1. **Industry analysis suggests 20–24 tonnes/day is financially sustainable**, implying **higher capex** (e.g., Rs 119 crore+ debt for 24 tonnes/day), which would **exceed the Rs 100 crore limit** and **remove priority-sector status**. The article does not reconcile this gap.
  2. The **Rs 836 crore Indian Bank loan (2025)** for **9 IOC-GPS plants** (likely >17 tonnes/day) may or may not count as priority sector, but the article **infers** it’s above the limit without confirming whether it’s **per plant or per promoter group**. This weakens the claim that the **Rs 100 crore cap is economically optimal**. [confidence: high]

---

**OUTDATED DATA:**
- **"Weighted average lending rate, fresh loans (August 2026): 8.61%; outstanding loans: 8.96%"**
  — These figures are likely **from RBI’s July 2026 *Treasury Operations and Development Department (TODD) report*** or **July 2026 *Trend and Progress of Banking in India***. However:
  - The **latest RBI *Trend and Progress*** (as of Oct 2026) would include **post-7 Oct 2026 repo hike data** (e.g., new lending rates effective Oct 2026).
  - The **RBI’s *Credit Statistics*** (monthly) or ***Quarterly Review of Bank Lending Rates*** (Q3 2026–27) would reflect **updated averages** after the hike.
  - **Source to re-check**: [RBI *Trend and Progress of Banking in India* (latest)](https://www.rbi.org.in/scripts/BS_ViewMasPublications.aspx) or [RBI *Credit Statistics*](https://www.rbi.org.in/scripts/BS_ViewMasPublications.aspx(sectionId=109)). [confidence: high]

- **"IREDA rate card: 9.75% to 10.75% by credit grade, from 1 Jun 2026"**
  — The **June 2026 rate card** may have been updated after the **7 Oct 2026 repo hike** (e.g., if IREDA adjusts margins quarterly or annually). The article does not confirm whether the **current rates** (as of Oct 2026) reflect the hike or if borrowers will see changes in **Q1 2027** (next reset).
  - **Source to re-check**: [IREDA’s latest *Rate Matrix*](https://www.iredaindia.gov.in/) (check for Oct 2026 updates). [confidence: medium]
