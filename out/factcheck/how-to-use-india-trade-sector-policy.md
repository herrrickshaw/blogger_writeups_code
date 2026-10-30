# Fact/interpretation check — how-to-use-india-trade-sector-policy

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-india-trade-sector-policy.html`

Text-SHA1: `24ee8c4c29dd57d7`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- **“HS71 Gems & jewellery US$109,430.2m +69.1%”** – The figure implies that India’s gems‑and‑jewellery exports in FY 2025‑26 were about $109 billion, which is far higher than the total value of India’s merchandise exports (≈ $600 billion in 2023‑24) and far above the historically reported gems‑and‑jewellery export value (≈ $30 billion). The number is therefore implausible and likely a transcription or scaling error. [confidence: high]

- **“HS27 Mineral fuels US$203,415.4m +21.2%”** – This suggests that imports of mineral fuels (primarily crude oil and coal) amounted to roughly $203 billion in a single fiscal year, exceeding India’s total import bill (≈ $600 billion) and the known annual crude‑oil import value (≈ $150 billion). The magnitude is inconsistent with official trade statistics, indicating a factual mistake. [confidence: medium]

**INTERPRETATION ERRORS**
- **“CBAM: iron & steel + steel articles exports US$20,725.6m exposed … De‑risk: China, import exposure US$102,363.0m across 8 sectors”** – The article treats the EU’s Carbon Border Adjustment Mechanism (CBAM) exposure on Indian iron‑and‑steel exports as justification for a “De‑risk China” tier. CBAM is an EU policy that applies to imports entering the EU, not a risk specific to China. Linking EU‑centric regulatory risk to the need to de‑risk trade with China conflates two unrelated dimensions (regulatory exposure vs. source‑country concentration), creating a false causal link. [confidence: high]

- **“Tier 1 Act now – no scheme, genuine gap … HS28 Inorganic chemicals … +86.0%”** – The claim that inorganic chemicals belong in an “Act now” tier because “no scheme” exists assumes that the absence of a Production‑Linked Incentive (PLI) automatically means a policy vacuum. In reality, the sector is already supported by other non‑PLI measures (e.g., export promotion schemes, tax incentives). Using the lack of a PLI as the sole criterion overstates the policy gap and misinterprets the broader policy environment. [confidence: medium]

**OUTDATED DATA**
- **“These are the repo author’s tiers, based on a July 2026 snapshot of provisional data.”** – The article relies on a July 2026 snapshot for FY 2025‑26 values, yet the Ministry of Commerce releases monthly trade data. By the time of the article’s revision (2 Nov 2026) the September 2026 data would have been available, and the provisional July figures may have been revised. The relevant series to re‑check are the Ministry of Commerce’s “Exports/Imports by HS‑6 code (monthly)” and the PIB’s “Annual Trade Statistics” for FY 2025‑26. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"FY2025-26 value"* for import/export sectors (e.g., inorganic chemicals US$14,179.7m) — **India’s fiscal year 2025–26 ended on 31 March 2026**, but the article’s data snapshot is explicitly dated **18 July 2026** (from the JSON filename). While provisional data may be available, the claim conflates the fiscal year’s end with the *provisional* data cutoff, which could mislead readers into assuming finalized figures. [confidence: **high**]

**INTERPRETATION ERRORS:**
- *"CBAM exposure on iron and steel exports"* is flagged as a risk but **not contextualized with the timeline of EU CBAM implementation**. The EU’s CBAM regulation entered its **first compliance phase (2026)** in October 2026, but the article does not clarify whether the US$20.7bn exposure figure accounts for *upcoming* CBAM surcharges (which will apply to *imports*, not just exports) or only historical trade flows. The causal link between "exposure" and "risk" assumes CBAM will directly penalize Indian exports, which is incorrect—CBAM targets *imports* into the EU, not Indian exports. [confidence: **high**]

**OUTDATED DATA:**
- *"July 2026 snapshot"* (data/sector_and_policy_recommendations_2026-07-18.json) — **India’s trade data for FY2025–26 was finalized by the Ministry of Commerce (TRADESTAT) in October 2026**, and the **latest provisional data for FY2026–27** (ending 31 March 2027) was released in November 2026. The article’s reliance on a **July 2026 provisional cut** risks outdatedness, especially for policy recommendations tied to dynamic sectors like gems/jewellery or CBAM. Re-check: **TRADESTAT monthly bulletins (https://commerce.gov.in/trade-statistics)**; newer period: **FY2026–27 provisional or FY2025–26 final**. [confidence: **high**]

---
*Note: The article’s disclaimers (e.g., "provisional data," "July 2026 snapshot") technically acknowledge limitations, but the phrasing "FY2025-26 value" without specifying "provisional" could mislead readers into treating it as finalized data.*
