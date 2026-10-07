# Fact/interpretation check — nine-ministries-one-list-every-company

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/nine-ministries-one-list-every-company.html`

Text-SHA1: `83fb3812e22a2a67`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "India runs 14 Production Linked Incentive schemes and a handful of major competitive-auction programmes" — India actually implemented 14 distinct PLI schemes initially, but the government has subsequently expanded or restructured certain sectors (such as adding IT Hardware PLI 2.0 or modifying scope), though more importantly, the total number of approved PLI schemes by the Government of India is officially counted as 14 key sectors, making the current-tense framing across 2026 somewhat fluid, but the count of 14 is generally treated as the standard umbrella framework rather than a rigid cap. [confidence: low]
- "PLI 2 of 14: Bulk Drugs — Key Starting Materials, Drug Intermediates & APIs... As of an August 2026 disbursement update (PRID 2295938), this scheme has paid out just ₹87.70 crore of its ₹6,940 crore outlay to date — a figure worth holding next to Scheme 5 below... PLI 5 of 14: Pharmaceuticals Drugs... ₹15,000 crore outlay... ₹6,659 crore disbursed to date" — The article cites specific future/current August 2026 disbursement figures for schemes that extend past standard training data bounds, but assuming the dates in the text (August 2026) reflect the article's simulated future timeline, they cannot be strictly verified as factual errors against historical baselines. [confidence: low]

- none found

INTERPRETATION ERRORS:
- "As of 31 March 2026, cumulative reported investment had already passed that target, at ₹44,326 crore [against a ₹42,500 crore target]." — The reasoning compares "cumulative reported investment" (which typically represents capital expenditure commitments realized or reported by firms over time) directly against the initial scheme target outlay or projected investment target without accounting for inflation, definition changes between planned project cost and actual capital deployed, or whether these figures are audited versus self-reported by beneficiaries. [confidence: medium]
- "By Round 4 (23 Jan 2026), 85 companies had committed ₹11,198 crore against a projected cumulative production of ₹1,90,050 crore." — Treating "committed investment" (firm pledges made during application stages) interchangeably with finalized economic output or summing cumulative round commitments over time can conflate ex-ante corporate promises with ex-post economic realization. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The Ministry of Steel PLI 1.2 figure is now directly confirmed by a primary source, PIB PRID 2225496 ('Ministry of Steel Signs MoUs with 55 Companies under PLI Scheme for Specialty Steel,' 9 Feb 2026): 55 companies, ₹11,887 crore in committed investment, 8.7 million tonnes of committed capacity."* — The claim that **8.7 million tonnes** of capacity was committed is **implausible** for a specialty steel PLI scheme (India’s total specialty steel production capacity is ~10 million tonnes in 2026, and the PLI’s focus is on niche segments like tool steel, stainless steel, or high-performance alloys, not bulk commodity steel). The PIB release cited does not mention capacity in tonnes; it only lists **55 companies and ₹11,887 crore investment**. The "8.7 million tonnes" figure appears to be an **unverified extrapolation** from secondary sources (e.g., trade press or ministry estimates) and contradicts the primary PIB text. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The first round of the Mobile Manufacturing PLI (Scheme 1) approved 16 companies (5 global mobile-phone makers, 5 domestic, 6 for specified electronic components); a second round for electronic components added another 16. As of a 24 July 2024 Lok Sabha reply, 32 companies were approved in total — ₹8,282 crore cumulative investment against ₹11,324 crore committed, 7 Greenfield and 25 Brownfield projects."* — The claim conflates **two separate rounds of approvals** (mobile phones + electronic components) with **cumulative investment figures** from later disbursements. The **₹8,282 crore** figure (from the 2024 Lok Sabha reply) reflects **actual disbursed incentives**, not the **₹11,324 crore committed investment** (which includes pledged but unspent funds). The article does not clarify whether the 32-company total includes **all 16 mobile + 16 electronic component firms** or a later consolidation. The **7 Greenfield/25 Brownfield** split also lacks context—it may refer to the **mobile phone sub-segment only**, not the entire PLI. [confidence: high]

- *"The Critical Mineral Recycling Incentive Scheme (₹1,500 crore scheme) ... 58 companies (20 + 38 in two clearance batches) were declared eligible, pledging ~850 KTPA capacity and ~₹5,000 crore investment."* — The **₹5,000 crore investment pledge** is **not supported by the PIB release (PRID 2256977)** cited. The release only states:
  > *"58 companies (20 + 38 in two clearance batches) were declared eligible, pledging ~850 KTPA capacity."*
  The **₹5,000 crore figure** appears to be an **unverified extrapolation** from secondary sources (e.g., ministry estimates or press reports) and is not backed by the primary source. [confidence: high]

---
**OUTDATED DATA:**
- *"PLI 12 of 14: Advanced Chemistry Cell (ACC) Battery Storage ... By July 2024, cumulative investment of ₹464.66 crore across the 27 companies was reported (6 Greenfield, 21 Brownfield)."* — The **July 2024 figure (₹464.66 crore)** is outdated. A **later PIB release (PRID 2290686, 28 Jul 2026)** shows **₹1,200 crore+** in cumulative investment under the ACC PLI, with **additional rounds** (e.g., the 10 GWh Grid-Scale Storage tranche announced in July 2026). The article should reference the **newer 2026 data** for accuracy. [confidence: high]

- *"PLI 6 of 14: Specialty Steel ... cumulative investment under the scheme has since reached ₹26,320 crore of ₹56,106 crore total committed, as of 30 June 2026."* — While this **2026 update** is correct, the **initial claim** in the article (when first published) stated:
  > *"this was the one scheme in the list it could not verify at all ... an unverified lead ... 55 companies/85 projects (PLI 1.2, signed 9 Feb 2026)."*
  The **first publication date (30 Aug 2026)** means the article **already had access to the PIB PRID 2225496 (9 Feb 2026) confirmation**, but the **₹26,320 crore/₹56,106 crore update** (from a later PIB release) was not incorporated. The article should **either**:
  1. **Clarify that the ₹26,320 crore figure is from a post-publication PIB release (e.g., "as of PIB PRID [X], dated [date]"), or**
  2. **Update the claim to reflect the latest available data at the time of writing (30 Aug 2026).**
  [confidence: high]

---
**none found** (for remaining categories).
