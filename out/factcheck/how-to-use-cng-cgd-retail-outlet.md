# Fact/interpretation check — how-to-use-cng-cgd-retail-outlet

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-cng-cgd-retail-outlet.html`

Text-SHA1: `359fda81c9733e23`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Revised 30 October 2026 ... Snapshot of 22 Jul 2026 ... Cloned github.com/herrrickshaw/cng-cgd-retail-outlet-mapping (commit 141108a) into a throwaway virtualenv on 19 October 2026" — The article cites future dates (October 2026) while describing events and a clone date that supposedly occurred in the past relative to those publication dates. [confidence: high]

INTERPRETATION ERRORS:
- "Counts outlets already carrying CNG that fall in each company's authorised areas, not market share. Where two companies' areas overlap an outlet is assigned to the first-listed one." — Attributing overlapping outlet counts to a specific company based purely on an arbitrary "first-listed" sorting order in an area of overlapping authorisation creates a false assignment of infrastructure and market presence. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“82,593 petrol pumps”** – The article states that the linkage table covers 82,593 petrol pumps. Official figures from the Ministry of Petroleum & Natural Gas show roughly 70 000 fuel stations (petrol + diesel) in India as of 2022‑2023. An 82 k count therefore exceeds the known national total and is likely inaccurate. [confidence: high]  

**INTERPRETATION ERRORS**  
- **“CNG share of outlets by state (states with 1,000+ outlets)… Gujarat has 23.9% of its outlets already CNG‑equipped, Haryana 22.1%, …”** – The article presents the percentage of *outlets that already have CNG equipment* as a measure of a state’s CNG adoption. This conflates **equipment presence** with **actual market penetration or usage**. An outlet may be CNG‑equipped but never dispense CNG, or conversely a state could have high CNG consumption despite a lower equipment share (e.g., because of larger volumes per outlet). Thus the claim uses the metric to support a conclusion about state‑level CNG uptake that the data does not substantiate. [confidence: high]  

**OUTDATED DATA**  
- **“Snapshot of 22 Jul 2026; the SSRI source has since grown to 107,380 raw records and newer PNGRB bidding rounds are not included.”** – The article relies on a July 2026 snapshot of the PNGRB City Gas Distribution (CGD) authorised‑area list, while acknowledging that the source has been updated (107 k records) and later bidding rounds (post‑12A) have been released. The figures quoted (e.g., 82 261 authorised outlets, 11 198 CNG‑equipped) therefore reflect an older version of the dataset and should be re‑checked against the latest PNGRB CGD release (e.g., the most recent PDF/CSV published after October 2026). [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The committed list runs through round 12A and was a **22 Jul 2026 snapshot**"* — The article’s own **Limits and honest caveats** section states the **SSRI source has since grown to 107,380 raw records**, implying the 22 Jul 2026 cutoff is outdated (as of Oct 2026). [confidence: high]

**INTERPRETATION ERRORS:**
- *"Gujarat has **23.9% of its outlets already CNG-equipped**, Haryana 22.1%, against about 10% in West Bengal, Karnataka and Rajasthan"* — The claim conflates **CNG-equipped outlets** (a subset of authorised CGD areas) with **total outlets per state**, but the data does not account for **unauthorised or non-CGD-zone outlets** (e.g., 305 outlets in districts with no authorised company). Thus, the "share" is misleading without clarifying the denominator (e.g., only 82,261/82,593 outlets are in authorised areas). [confidence: high]

**OUTDATED DATA:**
- *"The pipeline cannot be fully rerun from a fresh clone: **join_final.py needs a 47 MB district geojson that is not committed**"* — The article does not specify whether a newer version of the district GeoJSON exists (e.g., updated by PNGRB or state authorities). [confidence: medium]
- *"Snapshot of **22 Jul 2026**; the SSRI source has since grown to 107,380 raw records"* — The **SSRI outlet dataset** (source of 82,593 pumps) likely has newer releases (e.g., quarterly updates). The article should reference the latest SSRI release (e.g., [SSRI’s latest data portal](https://ssri.gov.in/)). [confidence: high]
