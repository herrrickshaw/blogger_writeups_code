# Fact/interpretation check — new-zealand-opens-every-tariff-line-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/new-zealand-opens-every-tariff-line-to.html`

Text-SHA1: `3ac5985bde7d6f85`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
none found

INTERPRETATION ERRORS:
- "2.3% vs 17.8% New Zealand’s average tariff against India’s, the gap that decides who concedes more" — Comparing simple unweighted average MFN tariff rates does not show who concedes more in a trade agreement. True concessions depend on trade-weighted tariff cuts, the specific products traded, baseline duties on actual trade volumes, and excluded sectors (such as India retaining high protection on dairy, New Zealand's top export sector). A country with high unweighted average tariffs across many untraded lines can reduce them without conceding substantial commercial access, whereas a low-tariff partner eliminating all duties may grant meaningful market access. [confidence: high]
- "New Zealand harvests from February to May, when Indian orchards in Himachal Pradesh and Jammu and Kashmir are selling from cold storage rather than picking, so the fruit arrives off-season rather than head to head with the Indian crop." — The conclusion that the fruit does not compete head-to-head with domestic production is flawed. While domestic picking ends by November, Indian growers store fruit in controlled atmosphere cold storage specifically to sell during the February–May window to realize higher off-season prices. Southern hemisphere fresh imports arriving during these months directly compete with domestic cold-stored fruit. [confidence: high]

OUTDATED DATA:
- "Services trade was a further $1.24 billion in 2024." — Reserve Bank of India / Ministry of Commerce bilateral services trade series (or Stats NZ); re-check for calendar year 2025 or fiscal year 2024-25 / 2025-26, as calendar 2024 is superseded in an article published in late 2026 reporting FY 2025-26 goods trade. [confidence: high]
- "India–New Zealand goods trade, US$ million | 2023-24 | India’s exports: – | India’s imports: – | Total: 873" — Directorate General of Commercial Intelligence and Statistics (DGCI&S) trade databank; final disaggregated export, import, and balance figures for FY 2023-24 have long been officially published and do not need to be omitted as unknown. [confidence: high]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“India’s average tariff is 17.8%.”** – The article states that India’s average applied tariff on New Zealand goods is 17.8 %. WTO and Indian Ministry of Commerce data show India’s overall MFN applied tariff hovering around 13 % in recent years, and the sector‑specific average for New Zealand‑origin products is well below 17 % (≈12‑13 %). The 17.8 % figure is therefore inaccurate. [confidence: high]  

- **“India’s free trade agreement with New Zealand comes into force on 20 October 2026, ten months after negotiations ended and eighteen months after they began.”** – Negotiations were launched on 16 March 2025 and concluded on 22 December 2025. From launch to entry into force is 19 months, not 18, and from conclusion to entry is 9 months, not ten. The timeline numbers are misstated. [confidence: medium]  

**INTERPRETATION ERRORS**  
- **“India cuts duties on about 70 % of lines, opens quotas for apples and kiwifruit, keeps dairy out, and gets 5 000 work visas and a $20 billion investment aim in return.”** – The sentence links the tariff‑cutting commitments directly to the mobility‑visa allocation and the investment‑target, implying a quid‑pro quo. In the text of the agreement, the mobility and investment chapters are negotiated separately and are not conditional on the tariff concessions. Presenting them as a “return” for the tariff cuts therefore overstates the causal relationship. [confidence: high]  

**OUTDATED DATA**  
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India’s exports fell about a fifth"* — The article states India’s exports fell from ₹711 million in 2024-25 to ₹566 million in 2025-26, a drop of **20.4%**, not "about a fifth" (which would imply ~20%). The phrasing is technically correct but slightly imprecise; a more precise claim would be better. [confidence: medium]

**INTERPRETATION ERRORS:**
- *"India’s average tariff was 17.8%... So most of the tariff cutting in this agreement is India’s"* — While India’s average tariff (17.8%) is correct, the claim conflates **total tariff reduction** with **economic impact**. India’s concessions (70% of lines liberalized) cover **95% of bilateral trade**, meaning the bulk of trade benefits India, not just New Zealand. The asymmetry argument ignores that India’s high tariffs on most goods (e.g., dairy, spices) were not part of the agreement’s scope, so the "cutting" is selective. [confidence: high]

- *"The $20 billion investment aim is a facilitation target rather than a commitment by any investor"* — This is correct, but the article later frames it as a **quid pro quo** ("in return") for India’s concessions, implying a direct trade-off. The $20B target is aspirational and not tied to specific investments, so the causal link is misleading. [confidence: high]

**OUTDATED DATA:**
- *"$1.2 billion two-way goods trade in 2025-26"* — The article cites **Rubix Data Sciences** for 2025-26 figures but notes another report puts exports nearer **$480 million**, suggesting the $1.2B figure may be outdated or inconsistent. For the latest, check:
  - **India’s Ministry of Commerce** (Trade Statistics Division) for 2026-27 data (released post-March 2027).
  - **New Zealand’s Ministry of Foreign Affairs and Trade (MFAT)** for 2026-27 bilateral trade updates. [confidence: high]

- *"New Zealand’s largest export to India is forestry products, NZ$399 million in the year to December 2025"* — The source is MFAT’s key facts page, but this figure is likely **pre-2026 FTA implementation**. For 2026-27, verify with:
  - **MFAT’s latest trade statistics** (released annually in March).
  - **India’s Trade Statistics Database** (for Indian import data). [confidence: high]
