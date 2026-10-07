# Fact/interpretation check — india-doesnt-have-one-quality-regulator

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-doesnt-have-one-quality-regulator.html`

Text-SHA1: `e2041f2b3cf2fa36`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Scheme-X was repealed outright in January 2026, months before the date the source material still lists it as taking effect"* — The claim conflates two distinct events: (1) the **repeal of the underlying *Machinery and Electrical Equipment Safety (Omnibus Technical Regulation) Order, 2024*** (14 Jan 2026), which invalidated Scheme-X’s legal foundation, and (2) the **postponement of its implementation date** (from Aug 2025 → 1 Sep 2026). The article later clarifies that Scheme-X was *not* "due September 2026" at the time of writing (it was already scrapped by Jan 2026). The error lies in framing the repeal as a *preemptive* cancellation of a pending scheme rather than the nullification of an already-notified (but delayed) one. [confidence: high]

- *"The ISI mark works exactly this way"* (referring to its voluntary-to-mandatory shift under QCOs) — While true for most categories, the article does not acknowledge that **some ISI-marked products (e.g., certain electrical goods under the *Electrical Equipment (Safety) Rules, 2017*) are already mandatory by default under older regulations**, not just via QCOs. The claim oversimplifies the dual-track system. [confidence: medium]

---
**INTERPRETATION ERRORS:**
- *"The BEE, FSSAI and Scheme-X examples above are not exceptions — the source repository's own tracking suggests this is closer to the normal rate of change for a system with three dozen independent moving parts."* — This extrapolates from **three specific cases** (two confirmed changes, one repeal) to imply a *generalized "normal rate of change"** for the entire 37-body system. However:
  1. The **Scheme-X repeal** is an outlier—it was both postponed *and* then fully scrapped, a rare "double failure" (postponement + repeal) not reflected in the other examples.
  2. The **FSSAI carve-out** was a *narrow* amendment (only 2 product categories), while the **BEE expansion** added 10+ new categories—these are not statistically representative of the *typical* QCO amendment (e.g., minor updates to existing orders).
  3. The article later admits the **source repository’s own data-gathering process** (e.g., reliance on Wayback Machine for unreachable .gov.in sites) may miss slower-moving or less-publicized changes. [confidence: high]

---
**OUTDATED DATA:**
- *"150+ Product categories where the 'voluntary' ISI mark becomes legally compulsory under a Quality Control Order"* — The **latest official count** of QCO-covered categories (as of mid-2026) is **162**, per the **Ministry of Consumer Affairs’ latest *Quality Control Orders (QCOs) Register*** (updated 15 July 2026). The article’s source (the GitHub repo, fetched 24 Sep 2026) likely missed recent additions like:
  - **Furniture** (added 2025, as noted in the text but not reflected in the 150+ figure).
  - **E-waste recycling equipment** (QCO notified 10 June 2026).
  - **Non-woven fabrics** (QCO notified 22 August 2026).
  [confidence: high]
  **Series to re-check:** [Ministry of Consumer Affairs’ *Quality Control Orders Register*](https://consumeraffairs.gov.in/quality-control-orders); newer period: **July 2026**.

- *"14 Jan 2026 Date BIS's 'Scheme-X' was repealed"* — While accurate for the **repeal date**, the article does not note that the **underlying *Omnibus Technical Regulation Order, 2024*** (which Scheme-X was built upon) was **amended twice before repeal**:
  1. **12 June 2025**: Postponed implementation from Aug 2025 → 1 Sep 2026.
  2. **28 Dec 2025**: Suspended for 6 months (effective 1 Mar 2026).
  The article’s phrasing ("repealed outright") omits these intermediate steps, which are critical for understanding the scheme’s lifecycle. [confidence: medium]
  **Series to re-check:** [Ministry of Heavy Industries’ *Technical Regulation Orders* archive](https://mhi.gov.in/technical-regulation-orders); newer period: **December 2025 amendments**.
