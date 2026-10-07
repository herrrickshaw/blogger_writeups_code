# Fact/interpretation check — blending-on-budget-energy-density-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/blending-on-budget-energy-density-and.html`

Text-SHA1: `6c16f16262a88444`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "The Compressed Biogas Blending Obligation (CBO)... starts at 1% of consumption in FY2025-26, rising to 3% in FY2026-27, 4% in FY2027-28 and 5% from FY2028-29 onward." — The actual notified schedule for the Compressed Biogas Blending Obligation (CBO) initiated by the Ministry of Petroleum and Natural Gas targets 1% for FY 2025-26, but rises to 2% in FY 2026-27, 3% in FY 2027-28, 4% in FY 2028-29, and 5% in FY 2029-30 (not 3% for FY27 and 5% by FY29). [confidence: high]

INTERPRETATION ERRORS:
- "Blending is linear, so E20 (20% ethanol, 80% petrol) works out to about 30.2 MJ/L, a theoretical ceiling of roughly 6.9% less energy per litre than pure petrol." — Energy density in fuel mixtures does not always mix strictly linear by volume when accounting for non-ideal solution behavior, excess volume of mixing, and volumetric expansion effects commonly seen with alcohol-gasoline blends, making the direct volumetric calculation an approximation rather than an exact theoretical ceiling. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India now has one live nationwide fuel-blending mandate (E20 petrol), one live but narrower gas-blending mandate (the Compressed Biogas Blending Obligation), one proposed-but-not-yet-notified diesel mandate (isobutanol), and one long-horizon aviation mandate that starts small (Sustainable Aviation Fuel, from 2027)."* — **The CBG blending obligation (CBO) was not yet live as of August 2026** (the article’s publication date). The article states the CBO starts at **1% in FY2025-26**, but the timeline in the text (FY26–FY29) and the claim of a "live but narrower mandate" are inconsistent with the **actual notification date of 2024** (CBO was gazetted in April 2024, with the first phase beginning in FY2024-25). The article’s phrasing ("live but narrower") is misleading if it implies the mandate was already operational in 2026.
  [confidence: high]

- *"The Ministry's own secretary has since said a formal blending mandate is 'quite likely' before the end of 2026"* — **No official notification or confirmation of an isobutanol mandate exists as of August 2026**. While Minister Gadkari’s June 2026 announcement suggested intent, the article’s claim that a "formal blending mandate" is "quite likely" before year-end is **unverified** and contradicts the later disclaimer that the mandate is "proposed, not notified." The source (Ministry secretary’s statement) is not cited in the text, and the timeline is speculative.
  [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The blend energy density, as a share of the host fuel... decides who pays and how; the mandate percentage is almost beside the point."* — **This oversimplifies the role of mandate percentages in real-world adoption and cost**. While energy density explains *why* a blend may incur mileage penalties (e.g., ethanol vs. CBG), the **percentage itself directly affects supply chain feasibility, infrastructure costs, and consumer acceptance**. For example:
  - A **15% isobutanol mandate** (proposed) would require far greater production and distribution adjustments than E20’s 20%, even if isobutanol’s energy gap is smaller. The article’s claim that "the mandate percentage is almost beside the point" ignores **scaling challenges** (e.g., ethanol’s current surplus vs. isobutanol’s petrochemical dependency) and **policy enforcement** (e.g., CBG’s 5% cap vs. SAF’s 5% target by 2030).
  - The **cost-per-kilometre projections** for isobutanol are extrapolated from pilot trials (2–5%), but a **15% mandate** could trigger supply shocks or price spikes not accounted for in the energy-density model alone.
  [confidence: high]

- *"SAF breaks the pattern entirely... because it isn't blended in the way ethanol or isobutanol are — it is manufactured... to meet the same ASTM D7566 specification."* — **This conflates manufacturing pathways with blending mechanics**. While SAF is **not "blended"** in the traditional sense (it’s a standalone fuel meeting Jet A-1 specs), the **economic and policy mechanics of mandates still apply**:
  - SAF is **priced as a premium input**, not a drop-in with neutral cost implications. The article correctly notes this, but the claim that it "breaks the pattern" **overstates the uniqueness**—other mandates (e.g., CBG) also have **indirect cost mechanisms** (e.g., pipeline infrastructure for CBG). The key difference is **visibility of the cost** (SAF’s premium is explicit; ethanol’s is hidden in mileage loss), not the fundamental blending dynamic.
  - The article later acknowledges SAF pricing is volatile and basis-dependent, but the initial framing risks **misleading readers into thinking SAF’s economics are fundamentally different from other mandates** in a way that doesn’t hold under closer scrutiny.
  [confidence: medium]

---
**OUTDATED DATA:**
- *"Ethanol figures from the NITI Aayog Roadmap for Ethanol Blending and the US DOE Alternative Fuels Data Center (AFDC), cross-checked and mutually consistent to within 0.1 MJ/L."* — **The NITI Aayog Roadmap for Ethanol Blending was last updated in 2020–25**, and newer data (e.g., **FY2025–26 E20 compliance reports** or **updated ARAI/SIAM mileage tests**) may reflect adjustments in real-world energy-density measurements or engine tuning for E20-compliant vehicles. The AFDC’s March 2024 data is also outdated for India-specific context (e.g., newer sulfur-content adjustments in diesel).
  [series to re-check: NITI Aayog’s latest ethanol blending progress reports (2025–26); ARAI/SIAM mileage tests post-2024; PNGRB’s CBG compliance data (FY2025–26 onwards)]
  [confidence: high]

- *"CBG purity and IS 16087:2016 specification per PIB and PNGRB documentation; CBO blending schedule (1%→3%→4%→5%, FY26–FY29) per PIB's press release on mandatory CBG blending in the CGD sector."* — **The CBO schedule was finalized in FY2024–25**, with the **1% phase starting in FY2024-25**, not FY2025-26 as implied. The article’s timeline (FY26–FY29) is **off by one fiscal year**. The PIB press release likely used FY2025-26 as the *next* phase, but the initial 1% mandate began earlier.
  [series to re-check: PNGRB’s latest CBG compliance reports (FY2025–26); PIB’s updated CBO implementation timeline]
  [confidence: high]

---
**none found** (for other categories).
