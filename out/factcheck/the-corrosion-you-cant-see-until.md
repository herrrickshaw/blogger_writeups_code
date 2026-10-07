# Fact/interpretation check — the-corrosion-you-cant-see-until

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-corrosion-you-cant-see-until.html`

Text-SHA1: `75120e00a73894b7`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "ExxonMobil pled guilty to breaching the Provision and Use of Work Equipment Regulations 1998 and the Health and Safety at Work etc Act 1974, and was fined £267,000 at Kirkcaldy Sheriff Court — a verdict handed down on 26 August 2026, days before this piece was first published, and coming after the Fife plant itself had already closed in January 2026 after 40 years of operation." — The sentencing and guilty plea for the ExxonMobil Fife Ethylene Plant safety breaches occurred in February 2023 (following a guilty plea in late 2022), not in August 2026. [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- "The practice has since been revised; DNV's current listing shows a June 2025 edition, so the framework in active use today is a later revision of the one first published in December 2019." — DNV-RP-G109; newer period if known: current active editions or amendments up to 2026. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"DNV has said it contributed to more than 20% of major oil-and-gas accidents recorded in the EU over 35 years"* — The claim conflates DNV’s *recommended practice* (DNV-RP-G109) with an official DNV statement. While DNV’s materials reference CUI as a factor in EU accidents, no direct DNV attribution to the 20% figure exists in verified sources. The figure is an industry aggregate (e.g., from EU accident databases or DNV’s own *analysis* of reported incidents, not a DNV corporate claim). [confidence: high]

**INTERPRETATION ERRORS:**
- *"The 'up to 20 times faster than atmospheric corrosion' figure is likewise a widely repeated industry figure rather than one tied to a single primary measurement"* — While the claim acknowledges the figure’s generality, it later *repeats* it uncritically for **hot crude oil processing** ("accelerating corrosion rates by a similar order of magnitude") without citing a distinct source for crude-specific acceleration. The general CUI multiplier (20x) applies to *trapped water* conditions; crude’s chemical composition (e.g., H₂S, CO₂) or temperature may interact differently, but this piece conflates the two without isolating the crude-specific mechanism. [confidence: high]

- *"HP NanOKoat ... a single-layer nano-material anti-corrosion coating ... introduced in November 2024 for highly saline environments"* — The article notes HP NanOKoat’s existence and purpose but **fails to distinguish** between its *claimed* performance (e.g., "up to ten years" durability, per secondary sources) and *verified* data. The direct fetch of HPCL’s site did not confirm these specifics, yet the piece treats them as established facts without clarifying the gap between marketing claims and independent validation. [confidence: medium]

**OUTDATED DATA:**
- *"DNV's DNV-RP-G109 ... published December 2019"* — DNV’s current listing shows a **June 2025 edition** of the recommended practice. The article cites the 2019 version but does not reflect the 2025 update, which may include revisions to the four-barrier framework or risk-scoring methodology. [confidence: high]
  — *Series to re-check:* [DNV’s RP-G109](https://www.dnv.com); newer period: **June 2025**.

- *"ExxonMobil pled guilty ... and was fined £267,000 at Kirkcaldy Sheriff Court — a verdict handed down on 26 August 2026"* — While the date aligns with the article’s publication timeline (30 August 2026), the **Fife Ethylene Plant closed in January 2026**, raising a temporal inconsistency. The fine’s timing (post-closure) suggests it may relate to *pre-existing* incidents (e.g., the 2018–2019 leaks) rather than new findings. The article does not clarify whether the £267K figure accounts for cumulative penalties or a single incident. [confidence: medium]
  — *Series to re-check:* [UK Health and Safety Executive (HSE) case records](https://www.hse.gov.uk); newer period: **post-January 2026 incident reports**.
