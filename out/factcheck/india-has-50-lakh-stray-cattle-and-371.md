# Fact/interpretation check — india-has-50-lakh-stray-cattle-and-371

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-has-50-lakh-stray-cattle-and-371.html`

Text-SHA1: `84ca0627df69dc3f`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "The government told the Rajya Sabha in August 2025 that both numbers had fallen since 2012, by 3.2% for cattle and 10.7% for dogs." — According to the official 19th (2012) and 20th (2019) Livestock Censuses published by the Department of Animal Husbandry and Dairying, stray cattle declined from 52,87,767 in 2012 to 50,21,587 in 2019. That represents a decline of 5.03% (or ~5.0%), not 3.2%. (The 10.7% decrease stated for stray dogs—from 1.71 crore to 1.53 crore—is mathematically correct). [confidence: high]

INTERPRETATION ERRORS:
- "In an Italian test that fed bags into a digester along with food waste, the way a real plant runs, paper bags broke down by about 82%, compostable-plastic bags by under 27%, and pieces of the plastic bags were left over." — This is an apples-to-oranges comparison. An anaerobic digester is an enclosed, oxygen-free biogas reactor (typically operated at mesophilic temperatures around 37°C), whereas compostable plastic bags certified under IS/ISO 17088 are designed and tested specifically for aerobic industrial composting (which requires oxygen and sustained temperatures near 58°C). Using anaerobic digestion performance to generalize that compostable plastic fails "the way a real plant runs" mischaracterizes the technology, as most composting facilities operate as aerobic windrows or in-vessel aerobic systems. [confidence: high]
- "Where and how many | Plastic | ... Faridabad, 2021: one cow, which died | 71 kg |" — The table labels the entire 71 kg extracted in the Faridabad case strictly as "Plastic." Rumen impaction masses of this magnitude are polymaterial trichobezoars/foreign body knots consisting of plastic bags bound together with cloth, ropes, metal wires, nails, coins, and stones. Attributing the entire 71 kg mass solely to plastic overstates the plastic figure. [confidence: medium]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- “The 2019 livestock census counted 50,21,587 stray cattle, about 50.2 lakh” — The 2019 (20th) Livestock Census reports total cattle numbers (≈5.02 crore), not stray cattle. Stray‑cattle figures are estimates from separate surveys; the census does not provide a “50.2 lakh stray cattle” count. [confidence: high]  

**INTERPRETATION ERRORS:**  
- “Plain paper is the one a rumen can break down, and the one most likely to pass if a cow swallows it.” — The article bases this claim on digestibility data for shredded newsprint, cardboard, and other paper grades, and on the fact that cellulose is a natural rumen substrate. It does **not** provide evidence that intact paper bags (which may contain wet‑strength resins, inks, or coatings) are actually broken down in a cow’s rumen, nor that they are “most likely to pass” compared with other bag types. The conclusion extrapolates from laboratory feed‑digestibility studies to real‑world bag ingestion, which is an apples‑to‑oranges comparison. [confidence: high]  

**OUTDATED DATA:**  
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"50.2 lakh stray cattle counted in the 2019 livestock census"* — The article later clarifies the **2019 census total was 50,21,587 (50.21587 lakh)**, not 50.2 lakh. The rounded figure (50.2 lakh) is misleadingly imprecise for a precise census count. [confidence: high]
- *"Balrampur Chini had spent about ₹2,400 crore by mid-October 2026"* — No independent verification (e.g., audited financials or regulatory filings) is cited for this claim. The source is a **press release (4 Nov 2026)**, which may not reflect actual capex or accounting. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"Compostable plastic bags are tested at 58°C (IS/ISO 17088), but a cow’s rumen is 40°C—so they won’t break down in a stomach. Therefore, compostable bags are useless for preventing plastic ingestion by cattle."*
  **Gap:** The claim conflates **industrial composting conditions** (58°C, weeks-long exposure) with **rumen physiology** (40°C, transient exposure). While compostable plastics degrade *slower* in a rumen than in compost, the **laboratory study cited** shows *some* surface degradation over 72 hours—suggesting partial breakdown, not total inefficacy. The article later admits "no study was found in which cattle were fed compostable bags," but the causal leap from "doesn’t break down in compost" to "won’t help in a rumen" is unjustified. [confidence: high]
- *"Paper bags are the ‘kindest’ to animals because ruminants digest cellulose, but their digestibility is only 30–98%—so they’re still not safe feed."*
  **Gap:** The article **narrows the claim** to "the one a rumen can break down" (kraft/bagasse paper) but then **overgeneralizes** by citing digestibility rates for *shredded paper* (not bags) and ink/toxin risks. The **fairer claim** (as stated earlier) is that paper bags are *more likely to pass* than plastic/compostable ones, but the article’s conclusion ("kindest") implies *absolute safety*, which isn’t supported by the data (e.g., wet-strength resins, ink lead risks). [confidence: high]

---
**OUTDATED DATA:**
- *"50.2 lakh stray cattle (2019 census); 21st census results unpublished as of writing (Nov 2026)"* — The **21st Livestock Census (2022)** was supposed to include stray cattle counts by sex. Check the **2022 census data** (released by the Ministry of Fisheries, Animal Husbandry & Dairying) for updated figures. [confidence: high]
- *"India’s cities produced about 1,62,468 tonnes of waste/day (80.31% processed)"* — The **latest CPCB waste generation data** (as of 2026) should reflect:
  - **2025–26 municipal solid waste (MSW) generation** (published in CPCB’s *Annual Report 2025–26* or *Solid Waste Management Rules, 2026* amendments).
  - **Processing rates** may have changed post-April 2026 (when new SWM rules took effect). Verify against **CPCB’s solid waste portal** or **PIB updates**. [confidence: high]
