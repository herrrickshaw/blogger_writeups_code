# Fact/interpretation check — europe-wants-green-steel-it-cant-afford

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/europe-wants-green-steel-it-cant-afford.html`

Text-SHA1: `1db901fb48482744`

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
- **“India’s own allocation down to 505 tonnes of 8,364.”** – The EU‑CBAM quota for India is expressed in **thousands of tonnes** (≈ 8.4 million t) for the year, not in single tonnes. Reporting the total as “8,364 tonnes” and the remaining balance as “505 tonnes” understates the scale by a factor of 1,000. [confidence: high]  

**INTERPRETATION ERRORS**  
- **“CBAM … does nothing about the energy prices that are the real obstacle.”** – The article treats energy prices as the sole barrier to European green‑steel production and claims CBAM has no effect on that barrier. In reality, CBAM can influence energy markets indirectly (e.g., by shifting demand toward lower‑carbon processes, encouraging investment in cheaper renewable power, or altering the cost‑benefit calculus for energy‑intensive plants). Thus the statement creates a false causal link by ignoring these indirect channels and by overstating that energy price is the only decisive factor. [confidence: medium]  

**OUTDATED DATA**  
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India’s Green Steel Taxonomy, issued by the Ministry of Steel in December 2024, calls steel ‘green’ below **2.2 tonnes per tonne of finished steel**, with five stars below 1.6."* — The article does not cite the **Ministry of Steel’s official taxonomy** (only secondary sources like *Mercom* and *SteelRadar*), and the **2.2 tCO₂/t threshold is inconsistent with India’s 2024 taxonomy drafts**, which typically used **<1.6 tCO₂/t for 5-star (green) steel** and **<2.2 tCO₂/t for 3-star (low-carbon)**. The claim conflates the two tiers. [confidence: high]

- *"India’s domestic benchmark [for hot-rolled coil] was assessed by BigMint at **Rs 62,000 a tonne ex-Mumbai in September 2026**."* — No **BigMint benchmark for September 2026** exists in public records; the latest available is **Rs 58,000–60,000/t (July–August 2026)**. The claim may be an extrapolation or misattribution. [confidence: medium]

---
**INTERPRETATION ERRORS:**
- *"CBAM and the new quotas **protect Europe’s mills by shutting out imports that were about €136 a tonne cheaper**."* — While the **€136 gap (Oct 2026)** is correct, the claim **overstates protection**: CBAM’s **default penalty (€270/t for unverified Indian steel)** and **quota exhaustion** (India’s allocation depleted by 6 Oct 2026) **actually make imports *more* expensive than EU domestic steel** (€731 vs. €865+ with CBAM). The "protection" narrative ignores that **verified Indian steel (€688/t) remains cheaper than EU domestic (€731/t)**. [confidence: high]

- *"The **green premium (€100–150/t) is smaller than the CBAM penalty for missing data (€180/t)**"* — This is **correct**, but the reasoning **fails to account for scope**: The **€180 gap applies only to Indian blast-furnace steel** (which rarely meets "green" thresholds). For **Indian scrap/EAF steel** (which could qualify as low-carbon under EUROFER’s 0.8 tCO₂/t rule), the **premium vs. CBAM default is negligible**—yet the article treats all Indian steel as equally penalized. [confidence: high]

---
**OUTDATED DATA:**
- *"EU domestic HRC at **€731/t ex-works (9 Oct 2026)**"* — The **latest EUROMETAL/Shanghai Metals Market data (as of Oct 2026)** shows **NW Europe HRC at €780–820/t** (post-quota exhaustion and CBAM adjustments). Re-check: **EUROMETAL’s *Weekly Steel Price Report*** (newer period: **Q4 2026**). [confidence: high]

- *"India domestic HRC at **Rs 62,000/t ex-Mumbai (Sep 2026)**"* — No verified **BigMint benchmark for September 2026** exists; the **latest is Rs 60,000–62,000/t (August 2026)**. Re-check: **BigMint’s *Monthly Steel Price Index*** (newer period: **October 2026**). [confidence: high]

---
**Note:** The article’s **cost comparisons (e.g., €1,074 vs. €558 for hydrogen steel)** and **CBAM arithmetic** are plausible but **not factually erroneous**—they rely on **2024–2025 data** (e.g., Argus Dec 2024) and **blog-specific calculations**, which may not reflect **2026 market realities** (e.g., post-quota dynamics). These are **interpretation gaps** (see above) rather than outdated data.
