# Fact/interpretation check — india-asean-trade-5155-billion-deficit

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-asean-trade-5155-billion-deficit.html`

Text-SHA1: `d725b10e3fbf679a`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "exports to Indonesia fell from $8.5 billion to $4.5 billion, -15% a year over four years" — The math for a compound annual growth rate (CAGR) from $8.5 billion to $4.5 billion over four years is approximately -14.3% rather than -15%, but more importantly, a four-year period between FY2021-22 and FY2025-26 encompasses *five* financial years (FY22, FY23, FY24, FY25, FY26), meaning the denominator for the time exponent should be 5 rather than 4, resulting in an incorrect annualized growth rate calculation. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- **“Exports to Indonesia fell from $8.5 billion to $4.5 billion, –15 % a year over four years.”** – The total decline from $8.5 bn to $4.5 bn is about 47 % over four years. The compound annual growth rate (CAGR) that corresponds to a 47 % drop is roughly **‑12 % per year**, not ‑15 % per year. The article’s stated annual rate is therefore inaccurate. [confidence: high]

**INTERPRETATION ERRORS**
- **“What it means: The deficit is 7.4 times its 2010 level while exports fell 9 % from FY2022, so the gap grew because imports rose 32 % and exports did not follow, in a period when the agreement was in force throughout.”** – The statement implies that the AITIGA agreement (or its being “in force”) caused the widening deficit, i.e., that the increase in imports and the modest fall in exports are a direct result of the trade‑in‑goods pact. The data merely show a correlation; they do not establish causality. Other factors (global commodity price swings, domestic demand shifts, supply‑chain disruptions, etc.) could explain the import surge and export stagnation. Hence the conclusion over‑reaches what the evidence supports. [confidence: high]

**OUTDATED DATA**
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India's goods deficit with ASEAN reached **$51.55 billion in FY2025-26**"*
  – The article itself notes that the **official PIB/Hindu BusinessLine figure is $51.55 billion**, but **Mint (13 Nov 2026) reports a deficit of >$45 billion**, suggesting a discrepancy. The claim lacks resolution between sources. [confidence: medium]

- *"The ASEAN goods deficit doubled from **$25.7 billion in FY2022 to $51.5 billion in FY2026**"*
  – The **$25.7 billion figure is from Rubix Data Sciences (FY2021-22)**, not FY2022. The article conflates fiscal years, making the "doubling" claim misleading. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The deficit is **7.4 times its 2010 level** while exports fell 9% from FY2022, so the gap grew because imports rose 32% and exports did not follow."*
  – The **7.4x multiplier** (from ~$7B in 2010 to $51.55B in FY2026) ignores that **FY2022’s deficit was already $25.7B**, meaning the growth rate is **far steeper** (≈7.4x from 2010 but only ≈2x from 2022). The causal framing ("imports rose 32%") oversimplifies: **other factors** (e.g., Indonesia export collapse, tariff changes, or global commodity prices) likely contributed. [confidence: high]

- *"Three countries supply **68% of India's imports from ASEAN**; exports to Indonesia halved... The trade is concentrated... which means the deficit depends on three suppliers."*
  – While concentration is noted, the **claim conflates correlation with causation**: the deficit’s growth isn’t *solely* due to these three countries’ shares. **Indonesia’s export drop ($4B loss) is a symptom, not the root cause**—e.g., **Singapore’s import share rose from 27% (FY2025-26) to ~30%+ in recent years** (per Rubix), suggesting structural shifts beyond Indonesia. [confidence: high]

---
**OUTDATED DATA:**
- *"India's deficit with ASEAN rose from about **$7 billion in 2010**..."*
  – The **2010 figure is from Commerce Ministry sources (cited)**, but **no newer official release** (e.g., post-2020 trade data revisions or updated Commerce Ministry reports) is referenced. For context, **FY2023-24’s deficit was ~$55B** (PIB, 2025), implying the 2010 baseline may be outdated. [confidence: medium]

- *"Exports to Indonesia fell from **$8.5 billion to $4.5 billion** between FY2021-22 and FY2025-26"*
  – The **$8.5B figure is from Rubix (FY2021-22)**, but **no official Commerce Ministry data** for FY2021-22 is cross-checked. For FY2025-26, the **official export figure is $38.41B** (vs. Rubix’s $38.5B), but **Indonesia’s share isn’t broken down officially**. Re-check: **Commerce Ministry’s annual trade statistics** (e.g., [DGFT](https://dgft.gov.in/) or [PIB](https://pib.gov.in/)) for FY2021-22 and FY2025-26. [confidence: high]
