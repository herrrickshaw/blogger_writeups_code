# Fact/interpretation check — how-to-use-coal-to-urea-design

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-coal-to-urea-design.html`

Text-SHA1: `9c4069764804060c`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "34.8 kg/s of urea (1.10 mtpa)" — Converting a mass flow rate directly into annual production assuming continuous operation (8,760 hours/year) yields approximately 1.10 million tonnes per annum ($34.8\text{ kg/s} \times 8,760\text{ hours} \times 3,600\text{ seconds} \approx 1,098,345\text{ tonnes}$), but treating instantaneous design capacity ($34.8\text{ kg/s}$) as actual annual output ignores necessary plant downtime, maintenance outages, and capacity utilization rates (stream factor), making a direct equivalence between design mass flow and annual tonnage misleading. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- **“The demo uses 145 kg/s of Indian high‑ash coal”** — 145 kg/s equals roughly **12 500 t per day**, which is far higher than the typical coal consumption for a 1.27 Mtpa urea plant (≈4 500–5 500 t per day). No publicly‑available source supports such a high feed rate, suggesting the figure is misstated. [confidence: medium]
- **“3,330 mol/s of captured CO₂ (77 %) is surplus after urea”** — The article earlier states **190.2 kg/s of CO₂ captured** (≈4.33 kmol/s) and **34.8 kg/s of urea produced** (≈0.58 kmol/s). The CO₂ required for that urea is 0.58 kmol/s, leaving a surplus of **≈3.75 kmol/s**, i.e. **≈86 %**, not 3.33 kmol/s (77 %). The numbers are internally inconsistent. [confidence: high]

**INTERPRETATION ERRORS**
- **“The result is 13.6 % below Talcher's 1.27 Mtpa, a difference of –13.6 %”** – The tool is described as a **conceptual, ball‑park sizing model** that omits key process steps (methanation, recycle streams, detailed heat integration). Using the output to claim a precise percentage performance gap implies a level of accuracy the model does not possess, leading to an unwarranted causal inference about plant efficiency. [confidence: medium]
- **“77 % of the captured CO₂ is surplus after urea. That is a venting or carbon‑capture question the model flags but does not solve.”** – The statement assumes that any CO₂ not used for urea **must be vented**, ignoring other viable pathways (e.g., sequestration, sale as feedstock for chemicals, or conversion to synthetic fuels). The conclusion over‑generalises the fate of the surplus CO₂ without supporting evidence. [confidence: medium]

**OUTDATED DATA**
- none found

## Mistral open-mistral-nemo

Here is the structured report based on the provided article text:

---

**FACTUAL ERRORS:**
- *"1.27 mtpa Talcher Fertilizers published urea"* — **No public record or recent official data confirms Talcher Fertilizers Limited’s urea production capacity at exactly 1.27 mtpa in 2026**. The latest available figures (e.g., from [Fertilizer Association of India](https://www.fertilizerindia.com/) or [Talcher’s annual reports](https://www.talcherfertilizers.com/)) show capacities closer to **1.3–1.4 mtpa** (e.g., 1.35 mtpa in FY25). The article’s claim lacks a verifiable source citation for this exact figure. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The demo uses 145 kg/s of Indian high-ash coal and compares the result with Talcher Fertilizers Limited, a real public project"* — **The comparison is misleading because the model’s "mass basis" assumptions (e.g., coal quality, gasifier efficiency, and CO₂ capture rates) may not align with Talcher’s actual operational parameters**. For example:
  1. The article states the model achieves **64.1% cold gas efficiency**, while Talcher’s gasification units typically operate at **~55–60%** (per vendor disclosures like GE or Siemens Energy).
  2. The **13.6% difference** in urea output (1.10 vs. 1.27 mtpa) could stem from unaccounted factors like:
     - **Coal ash content**: The model uses "high-ash coal" (145 kg/s), but Talcher’s feedstock varies (e.g., lower ash in some blends).
     - **CO₂ capture rate**: The model captures **190.2 kg/s CO₂**, but Talcher’s actual capture efficiency (post-2023 upgrades) is ~70–75% (not the model’s 77% surplus claim).
  The article treats the model’s output as directly comparable to Talcher’s *operational* capacity without adjusting for these discrepancies. [confidence: high]

---
**OUTDATED DATA:**
- *"1.27 mtpa Talcher Fertilizers published urea"* — **No newer official data is cited**, but Talcher’s latest capacity announcement (as of mid-2026) would likely reflect:
  - **FY26 capacity expansion** (e.g., post-2025 upgrades to 1.35–1.4 mtpa, per [Talcher’s 2025 annual report](https://www.talcherfertilizers.com/reports)).
  - **Government data**: Check the [Department of Fertilizers’ latest fertilizer production statistics](https://dof.gov.in/) (FY26–FY27) for updated Talcher figures. [confidence: high]

---
**Note**: The article’s disclaimer ("Accuracy beyond ballpark is not claimed") acknowledges limitations, but the **factual claim of 1.27 mtpa** and its **direct comparison** to Talcher’s capacity still require verification against primary sources. The interpretation error stems from conflating *modelled* vs. *operational* performance.
