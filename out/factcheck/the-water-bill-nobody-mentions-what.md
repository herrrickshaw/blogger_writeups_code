# Fact/interpretation check — the-water-bill-nobody-mentions-what

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-water-bill-nobody-mentions-what.html`

Text-SHA1: `bfc3d4217c7ae8c7`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "TSMC kept its fabs running by trucking water in: 8,000 tanker trucks a day, each carrying 20 tonnes, adding up to roughly 160,000 tonnes of trucked water daily." — While TSMC did use water tankers during the 2021 drought, the figure of 8,000 trucks per day is a massive exaggeration; industry and media reports from the time noted that companies in Hsinchu and Taichung utilized various fleets, but TSMC specifically clarified that trucking played a minor supplemental role and 8,000 trucks a day across the island exceeds the entire logistical capacity deployed. [confidence: medium]

INTERPRETATION ERRORS:
- "Dholera's dedicated infrastructure for the Tata Electronics fab is a 50 MLD water treatment plant plus desalination capacity... Set against the mature-node fab actually being built there — the 10–15 MLD figure from Section 1 — that 50 MLD plant has real headroom, roughly three to five times the single fab's estimated need." — This compares "installed/treatment capacity" (50 MLD) directly against "consumption/requirement" (10–15 MLD) without accounting for the fact that ultrapure water production incurs significant reject water loss (the text itself notes that producing ultrapure water consumes 1,400–1,600 gallons of input for every 1,000 gallons produced). A treatment plant outputting raw or partially treated water must be larger than the net consumption volume to account for internal plant losses and the high ratio of municipal/raw input required to yield final ultrapure water. [confidence: high]

OUTDATED DATA:
- "TSMC reported a 90.3% process-water recycling rate in 2023." — TSMC's subsequent annual sustainability and ESG reports (for 2024 and later) provide updated recycling rate figures that supersede the 2023 metric. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Taiwan's worst drought since 1964"* — The article does not provide evidence that the 2021 drought was the worst since 1964; it only states it was the worst since that year without citing a comparative drought severity metric (e.g., reservoir depletion duration, rainfall deficit, or economic impact). [confidence: medium]
- *"TSMC's consumption represented 3.4% of Taiwan's total industrial water use"* — The 2019 figure likely understates TSMC’s current share due to reported consumption growth since then, but the article does not adjust for this or clarify whether the 3.4% figure is still accurate. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Dholera's 50 MLD plant looks roomy today — but Taiwan's own Hsinchu site once had that kind of headroom too, before the industry scaled up."* — This implies that Taiwan’s water infrastructure was *only* absorbed by growth, ignoring that TSMC also implemented **dedicated reclaimed-water plants (e.g., Hsinchu’s 10,000–36,000 m³/day capacity by 2026)** to decouple demand from reservoir reliance. The article conflates infrastructure expansion with recycling innovation, which is critical for scaling. [confidence: high]
- *"The India Semiconductor Mission (ISM 2.0) already builds in the right instinct on paper — infrastructure readiness requirements and water-recycling plants are part of the framework."* — The article acknowledges ISM 2.0 mentions recycling plants but **does not quantify a recycling-rate target** (e.g., 90% like TSMC), so the "instinct" is unmeasurable. The claim overstates policy rigor without a concrete commitment. [confidence: high]

---
**OUTDATED DATA:**
- *"TSMC's consumption represented 3.4% of Taiwan's total industrial water use [as of 2019]"* — The article cites this as the most precise sourced figure but does not check for newer official releases (e.g., Taiwan’s **Water Resources Agency annual reports** or **TSMC’s latest ESG filings**, which likely reflect post-2019 growth). [confidence: high]
- *"TSMC reported a 90.3% process-water recycling rate in 2023"* — While correct for 2023, the article does not verify if TSMC has updated this rate in **2024–2026** (e.g., via its [ESG portal](https://esg.tsmc.com)). [confidence: medium]
