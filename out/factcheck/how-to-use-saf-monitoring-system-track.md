# Fact/interpretation check — how-to-use-saf-monitoring-system-track

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-saf-monitoring-system-track.html`

Text-SHA1: `77f69a4ad8306841`

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
- “Python 3.14 on 23 October 2026.” — Python 3.14 has never been released; the latest stable version as of 2024 is 3.12, and no official 3.14 version exists. This makes the stated runtime environment factually incorrect. **[confidence: high]**

**INTERPRETATION ERRORS**
- “SAF is not yet a notified sector under India’s carbon market per the repository; its India module is a what‑if tool, not an active scheme.” – The article treats the repository’s internal “India module” as evidence of the official status of SAF in India’s carbon market. The repository is a private, archived codebase and does not determine or reflect government policy; using it to conclude that SAF is not a notified sector is an unwarranted extrapolation. **[confidence: medium]**

## Mistral open-mistral-nemo

Here’s the structured feedback based on the provided article:

---

**FACTUAL ERRORS:**
- *"The repository was not modified."* — **Incorrect.** The article explicitly states the repository is **archived (read-only)**, meaning no updates or modifications are possible (even by the author). This claim conflates "unmodified" (which is true) with "not modifiable" (which is the actual state). [confidence: high]

**INTERPRETATION ERRORS:**
- *"The dashboard summary from the seeded mock database shows **‘current_year_blending_pct: 2.28’** and **‘current_year_mandate_pct: 2.0’**, implying compliance for the year."* — **False causal claim.** The 2.28% blending rate is **above the 2.0% mandate**, but the article later shows **EGLL (0.952%) is non-compliant** while **EDDF (3.4%) and LFPG (2.5%) are compliant**. The summary’s 2.28% is a **global average** (not per-airport), so it doesn’t reflect individual compliance statuses. [confidence: high]

- *"The repo’s **‘mandate_pct_for_year’ defaults (2025: 2.0, 2030: 6.0, etc.)** are ‘frozen’ and ‘not updated’ because the repository is archived."* — **Overgeneralization.** The article clarifies these are **defaults for mock data**, but the **actual regulatory mandates** (e.g., ReFuelEU/CORSIA) are still evolving. The claim implies the repo’s defaults *replace* official rules, which is misleading. [confidence: medium]

**OUTDATED DATA:**
- *"**‘core LCA (HEFA-SPK, used cooking oil): 13.9 gCO₂e/MJ’**"* — **Series to re-check:** ICAO CORSIA/ReFuelEU lifecycle assessment (LCA) databases (e.g., [ICAO’s latest LCA values](https://www.icao.int/environmental-protection/CORSIA/Pages/default.aspx) or [EU’s NAMA Facility](https://ec.europa.eu/energy/topics/energy-efficiency/namas_en)). The 13.9 value is from the **archived repo’s defaults** (2026), but newer ICAO/EU updates may differ (e.g., ICAO’s 2023 LCA database lists HEFA-SPK at **~12.5–14.5 gCO₂e/MJ**, but pathways like HEFA-HVO may vary). [confidence: high]

- *"**‘ASTM conformance rule: SIP max 10%, blend 15% → False; HEFA max 50%, blend 30% → True’**"* — **Series to re-check:** Latest ASTM D7566/D6751 standards (e.g., [ASTM’s 2024 revision](https://www.astm.org/Standards/D7566.htm)). The repo’s defaults (2026) may not reflect **2024+ updates** (e.g., ASTM now allows **up to 100% HEFA in some blends** under D7566-24). [confidence: high]

---
**Note:** The article’s disclaimers (e.g., "mock data," "archived repo") are correct but **not consistently applied** in interpretations (e.g., treating repo defaults as "current law"). The **23 October 2026 date** suggests the article is hypothetical (or futuristic), but factual checks assume it’s a real 2026 publication. If the date is literal, the **ICAO/EU LCA and ASTM updates** would still apply.
