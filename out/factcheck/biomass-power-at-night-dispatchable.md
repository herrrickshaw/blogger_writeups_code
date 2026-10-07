# Fact/interpretation check — biomass-power-at-night-dispatchable

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/biomass-power-at-night-dispatchable.html`

Text-SHA1: `48fa396cb96e23db`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "The Central Electricity Regulatory Commission's proposed RE Tariff Order for the third year of the current Control Period (FY2026-27) sets the normative capital cost for a Rankine-cycle biomass power project at ₹638–744 lakh per MW..." — The Central Electricity Regulatory Commission (CERC) typically sets multi-year tariff regulations and orders for renewable energy technologies on a control period basis (e.g., tariff periods lasting 3 to 5 years), but CERC does not issue orders specifically designated as "proposed RE Tariff Orders for the third year of the current Control Period (FY2026-27)" in this manner; tariff determinations follow public regulations and specific tariff orders issued periodically for a control period rather than rolling annual "third year" proposed orders. [confidence: medium]

INTERPRETATION ERRORS:
- "Run through CERC's levellised-tariff methodology, the resulting applicable tariff for a standard water-cooled, travelling-grate-boiler biomass plant comes out to roughly ₹9.6–11.1 per kWh across the major biomass states — split into a levellised fixed-cost component of about ₹3.4–3.5/kWh and a variable fuel-cost component of ₹6.3–7.6/kWh that dominates the bill. That figure is the real explanation the ToD story alone doesn't supply. A 10–20% peak-hour premium is a percentage of the "normal tariff" a state commission sets — for competitively bid solar and wind power in India, that normal tariff typically sits in the ₹2.5–3.5/kWh range, several times lower than biomass's own levellised cost before any ToD premium is even applied." — The reasoning commits an apples-to-oranges comparison by contrasting the high cost-plus normative tariff of a firm, legacy-style biomass plant (derived from CERC cost-plus norms) against the highly discounted, market-discovered tariffs of newly competitively bid solar and wind power (₹2.5–3.5/kWh). Biomass capacity in India (especially bagasse cogeneration) largely operates under older, historically determined cost-plus Power Purchase Agreements (PPAs) with different tariff structures, meaning comparing a theoretical CERC normative cost of new biomass against current solar auction discoveries does not accurately capture why existing biomass plants fail to respond to ToD signals or how legacy tariffs are structured. [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India's total renewable capacity (excluding large hydro) grew 178% between December 2019 and July 2026"* — The claim conflates **non-hydro renewables** (solar, wind, biomass, small hydro) with **total renewables** (which includes large hydro). The article later clarifies that large hydro is excluded for comparability, but the initial phrasing risks misleading readers into thinking large hydro is part of the 178% growth. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Biomass power can run at night. It is one of the few renewable sources that actually can. And yet... biomass power grew just 19% — the slowest of any renewable category, in the one slot on the grid where a dispatchable renewable should be winning."*
  The reasoning conflates **dispatchability** (biomass *can* run at night) with **economic viability** (whether it *should* compete with solar under current tariffs). The article later admits biomass costs ₹9.6–11.1/kWh, far above the ₹2.5–3.5/kWh solar/wind tariffs, making the ToD premium insufficient to bridge the gap. The causal link between dispatchability and growth rate is therefore flawed. [confidence: high]

**OUTDATED DATA:**
- *"A 2018 Centre for Science and Environment analysis of Delhi's summer electricity demand... found that late-night demand exceeded afternoon demand on 21 of 31 days in May of that year."*
  The article explicitly states this is cited for **structural pattern only**, not as current data. However, no newer official demand-side analysis (e.g., from CEA or state DISCOMs) is referenced to update the claim. [confidence: medium]

---
*Note: No other categories had clear issues based on the provided text.*
