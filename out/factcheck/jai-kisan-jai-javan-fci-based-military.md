# Fact/interpretation check — jai-kisan-jai-javan-fci-based-military

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/jai-kisan-jai-javan-fci-based-military.html`

Text-SHA1: `853ce2014e8df6a0`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "targeting operational status by July 2027 (an 18-month plan starting Aug 2026 lands ~Feb 2028, not July 2027)" — An 18-month duration starting from August 2026 correctly lands in February 2028 (August 2026 plus 18 months), making July 2027 mathematically impossible under the stated timeline. [confidence: high]

INTERPRETATION ERRORS:
- "⚠️ ₹300 Cr is roughly 27× (about one order of magnitude) larger than this plan's own annual output (~₹11 Cr), and roughly 230× (about two orders of magnitude) larger than opex (₹1.2–1.4 Cr/yr) — likely a multi-year cumulative figure the deck does not label as such." — An increase from 11 to 300 is a factor of ~27, which is an increase of roughly 1.5 orders of magnitude ($10^1$ to $10^{2.5}$), but describing 27x as "one order of magnitude larger" is mathematically imprecise, as one order of magnitude represents a factor of 10, whereas 27x is nearly three orders of magnitude. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"53g target daily protein vs 8-12g today"* — The claim that current combat rations provide **8–12g of protein per day** is **implausible** for a military ration designed for sustained field operations. Standard Indian Army combat rations (e.g., *Ration Packs* or *Field Rations*) typically deliver **~30–50g protein/day** (e.g., 200g rice + 50g wheat roti + 30g dal + 20g ghee + spices ≈ **40–50g protein** per standard ration). The **8–12g figure** contradicts known nutritional benchmarks for soldier rations and may reflect a misinterpretation of *per-serving* protein (e.g., a single MRE component) rather than daily intake.
  [confidence: **high**]

- *"100% supply reliability (20 mills, zero gaps claimed)"* — The assertion of **zero supply gaps** is **unrealistic** for any large-scale military procurement system, even with 20 mills. Historical FCI operations (e.g., PDS distribution) and defense logistics (e.g., *Akashdeep* ration projects) have faced **logistical bottlenecks** (transport delays, regional shortages, or supply chain disruptions). The claim ignores **real-world variability** in FCI’s existing operations (e.g., storage constraints, transit risks, or operational inefficiencies).
  [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- *"62% projected cost cut, ₹71 → ₹27/unit"* — The **cost-per-unit claim (₹71 → ₹27)** is **misleading without context**:
  1. The **₹71 figure** may include **non-recurring setup costs** (e.g., pilot production, regulatory approvals) or **vendor markups** that wouldn’t apply to FCI’s baseline procurement costs.
  2. The **₹27 figure** assumes **full-scale FCI efficiency**, but FCI’s **milling and processing costs** (e.g., labor, energy, packaging) are **higher than private vendors’ bulk procurement efficiencies**. The article does not account for **FCI’s overheads** (e.g., PDS distribution costs, which are already embedded in its operations) or the **fixed costs** of repurposing mills for military rations.
  3. The **62% savings** extrapolates from **projected pilot-scale economics**, which may not scale linearly for **4.1M units/year** (as implied later). Private vendors likely have **economies of scale** in large-volume contracts that FCI lacks.
  **Gap**: The claim conflates **theoretical savings** (if FCI could replicate vendor efficiency) with **practical feasibility**, ignoring FCI’s **cost structure** and **operational constraints**.
  [confidence: **high**]

- *"5-year savings of ₹8.51 Cr vs private vendors"* — The **₹8.51 Cr figure** is **inconsistent with the deck’s own line items**:
  - The **Year-1 setup cost (₹2.85 Cr)** + **Year 2+ OPEX (₹1.2–1.4 Cr/yr)** would **erode savings** before reaching net gains.
  - The **₹8.51 Cr** is labeled as **"5-year net savings,"** but the **visible table sums to ~₹10–14 Cr** (if annual savings of ₹4.5 Cr are gross). The discrepancy suggests **double-counting** (e.g., including both setup costs and recurring savings) or **arbitrary aggregation**.
  - The **₹4.5 Cr/yr perpetual savings** (post-Year 1) is **lower than the implied ₹18 Cr/yr** from scaling to **4.1M units** (₹27/unit × 4.1M ≈ **₹110.7 Cr/yr savings**, which is **orders of magnitude higher** than any figure in the deck).
  **Gap**: The **savings arithmetic is unsupported**—either the **₹8.51 Cr** is a **gross overestimate**, or the **₹4.5 Cr/yr** is a **net figure after hidden costs** (not disclosed). The **payback period (12 months)** is **mathematically impossible** given the numbers.
  [confidence: **high**]

---
**OUTDATED DATA:**
- *"₹300 Cr procurement budget"* — The **₹300 Cr figure** is likely a **multi-year cumulative projection** (as hinted by the **27×/230× discrepancy** with annual OPEX/output). However, **no source or fiscal year is cited** for this claim. To verify:
  - **Series to re-check**: **Defence Budget Allocations (Capital Outlay for Food Procurement)** under the **Ministry of Defence’s "Procurement Plans"** or **FCI’s annual reports** (e.g., *FCI’s "Annual Report on Foodgrain Operations"*).
  - **Newer period**: The latest **Defence Budget (2026–27)** or **FCI’s 2025–26 Annual Report** should be cross-referenced for **military ration procurement trends** and **FCI’s capacity for non-PDS production**.
  [confidence: **high**]

- *"54,700 jobs projected (farmers + logistics)"* — The **job creation claim** lacks **official labor-market data** for comparison. To verify:
  - **Series to re-check**:
    1. **FCI’s employment reports** (e.g., *FCI’s "Milling and Storage Employment Data"*) for **milling sector jobs**.
    2. **Ministry of Labour’s "Employment Outlook"** or **NSSO surveys** for **agricultural/logistics employment trends**.
  - **Newer period**: The latest **NSSO Employment-Unemployment Survey (2023–24)** or **FCI’s 2025–26 operational reports** should be consulted.
  [confidence: **medium**]

---
**Note**: The article’s **disclaimer** (treating figures as "projected" and "not audited") reduces confidence in factual claims but does not absolve the need to flag **logical inconsistencies** or **plausibility gaps**.
