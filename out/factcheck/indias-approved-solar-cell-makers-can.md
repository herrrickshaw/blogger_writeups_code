# Fact/interpretation check — indias-approved-solar-cell-makers-can

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-approved-solar-cell-makers-can.html`

Text-SHA1: `8263be84706061ed`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "India’s Approved Solar-Cell Makers Can Now Make 37.8 GW a Year. Rooftop Projects Have Until 31 December to Use Them" — The headline asserts the exact reverse of the actual policy explained in the text. Net-metering/rooftop projects have until 31 December 2026 to commission *without* domestically enlisted List-II cells (an exemption window); after 31 December 2026, compliance is mandatory and projects are required to use them. [confidence: high]

INTERPRETATION ERRORS:
- "A developer in a state with no enlisted cell plant must buy from Gujarat, Tamil Nadu or Telangana, which together hold 67% of the list." — False dilemma / unwarranted restriction. While Gujarat, Tamil Nadu, and Telangana account for 67% of enlisted cell capacity, the article's own data shows that the remaining 33% is distributed across six other states (Maharashtra, Himachal Pradesh, Karnataka, West Bengal, Uttar Pradesh, and Andhra Pradesh). A developer outside those states is not restricted to procuring only from the top three states. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- **“The list has roughly tripled in fourteen months, from 13,067 MW to 37,796 MW.”** – A three‑fold increase would be about 39,200 MW; the actual growth factor is ≈2.89×, not a full triple. [confidence: high]

**INTERPRETATION ERRORS**
- **“A developer in a state with no enlisted cell plant must buy from Gujarat, Tamil Nadu or Telangana, which together hold 67 % of the list.”** – The article treats the domestic‑only List‑II capacity as the sole source for such developers, ignoring that they can import cells or source from other Indian states not on List‑II. The conclusion that purchases are forced to come from those three states is not supported by the data. [confidence: medium]

**OUTDATED DATA**
- **“Energetica India … reports cumulative enlisted module capacity of 228,524 MW after the September 2026 update.”** – MNRE’s List‑I is updated periodically; a later revision (e.g., the November 2026 update) likely supersedes the September figure, so the module‑capacity number may be outdated. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"MNRE’s approved list of domestic solar-cell makers now holds **37.8 GW** a year of enlisted capacity"* — The article’s own sum of unit capacities (37,796 MW) does not round to 37.8 GW (which would imply 37,800 MW). The discrepancy is minor but inconsistent with the detailed breakdown provided later (37,796 MW). [confidence: high]

**INTERPRETATION ERRORS:**
- *"Enlisted cell capacity of 37.8 GW is about **85% of the all-segment total** and 4.3 times the rooftop figure"* — The claim conflates **enlisted capacity** (nameplate manufacturing potential) with **actual installations** (which include utility-scale projects exempt from List-II requirements). The 44.6 GW FY2026 total includes ground-mounted projects (34.8 GW) that may not use List-II cells, and rooftop demand is unquantified. The comparison is misleading without isolating only List-II-dependent segments. [confidence: high]

**OUTDATED DATA:**
- *"Cumulative enlisted module capacity of **228,524 MW** after the September 2026 update"* — The article cites Energetica India’s tracking as of September 2026 but does not verify if MNRE’s **List-I (3 August 2026 PDF)** has a newer revision or updated total. [confidence: medium]
