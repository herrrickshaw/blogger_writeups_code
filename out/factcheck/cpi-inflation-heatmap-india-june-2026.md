# Fact/interpretation check — cpi-inflation-heatmap-india-june-2026

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/cpi-inflation-heatmap-india-june-2026.html`

Text-SHA1: `00013b63e8097f50`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "The Reserve Bank of India's flexible inflation-targeting mandate sets a CPI target of 4%, with a tolerance band of 2–6% either side." — The RBI's inflation-targeting framework sets a target of 4% consumer price inflation with a tolerance band of +/- 2 percentage points around it (meaning 2% to 6% in total), not "2-6% either side" (which would imply a band of -2% to 10%). [confidence: high]

INTERPRETATION ERRORS:
- "That's a 3.4-percentage-point spread between two states reporting on the same combined-CPI series, in the same month, under the same MoSPI methodology — which means the divergence isn't a measurement artefact, it's real variation in what a rupee buys from one state to the next." — The inflation rate measures the *change* in prices over a year, not the absolute price level ("what a rupee buys") at a single point in time. A higher inflation rate in Telangana than in Delhi means prices are rising faster there, but it does not directly demonstrate differences in the baseline cost of living or what a rupee buys across states. [confidence: high]

OUTDATED DATA:
- "SOURCE: api.mospi.gov.in via MoSPI MCP connector · CPI base year 2024, series 'Current'" — The official base year for India's Consumer Price Index (CPI) published by MoSPI is 2012 (with ongoing plans or discussions for a revision, but 2024 is not an established official base year for published historical series as of standard data releases). Series to re-check: MoSPI CPI base year revisions and current index series. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"All-India rate is 4.38%"* — No official MoSPI data for June 2026 is publicly available (as of my knowledge cutoff in October 2023), and the latest confirmed All-India CPI (combined) for June 2023 was **4.87%** (MoSPI). The claim lacks verifiable source validation for June 2026. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The gap between the hottest and coolest state... is real variation in what a rupee buys from one state to the next"* — While the spread is statistically valid, the article conflates **state-level CPI differences** (which reflect local price dynamics) with **purchasing power parity (PPP) adjustments**—the latter would require a separate methodology (e.g., Big Mac Index or PPP surveys). The claim overstates the causal link to "what a rupee buys" without PPP data. [confidence: high]

**OUTDATED DATA:**
- *"CPI base year 2024"* — The latest official CPI base year is **2023** (MoSPI’s 2023 CPI series), and the 2024 base year was never implemented. The article should cite the **2023 series** as the current benchmark. [confidence: high]

*(Note: No other categories triggered errors based on the provided text.)*
