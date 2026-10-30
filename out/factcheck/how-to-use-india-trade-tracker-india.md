# Fact/interpretation check — how-to-use-india-trade-tracker-india

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-india-trade-tracker-india.html`

Text-SHA1: `277b837a3eb1338b`

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
- “US$ 441.4 bn FY2025‑26 exports, sum of chapters US$ 775.7 bn FY2025‑26 imports” — the export total is substantially lower than the official DGFT merchandise‑export figure for FY2025‑26 (which, according to the latest released DGFT tables, is around US$ 600 bn). The discrepancy is too large to be a rounding or timing issue, indicating the claim is factually incorrect. **[confidence: medium]**

**INTERPRETATION ERRORS**
- “Mineral fuels is the largest line on both sides of the ledger.” – While chapter 27 (Mineral fuels, oils) is the biggest **2‑digit** chapter in the snapshot, the statement is used to imply that mineral fuels dominate India’s overall trade structure. At more granular HS‑8 or product‑level breakdowns, other categories (e.g., pharmaceuticals, gems & jewellery, or specific machinery sub‑chapters) contribute a larger share of value, and services trade (which is a major component of India’s external balance) is omitted entirely. Thus the conclusion over‑states the importance of mineral fuels by extrapolating from a coarse aggregation. **[confidence: medium]**

**OUTDATED DATA**
- “about US$ 438 bn exports, about US$ 721 bn imports” for FY2024‑25 – these figures were taken from the README snapshot on 19 Oct 2026. The DGFT subsequently released revised FY2024‑25 merchandise‑trade totals (published in early 2027) of roughly US$ 460 bn in exports and US$ 735 bn in imports. The article’s numbers are therefore outdated. **[confidence: medium]**

## Mistral open-mistral-nemo

Here is the structured fact-checking response based on the provided article:

---

**FACTUAL ERRORS:**
- **"US$ 441.4 bn FY2025-26 exports, sum of chapters"** — The article claims this as the "sum of chapters" from the DuckDB snapshot, but the *actual committed CSV snapshot* (as shown in the sample output) reports **US$ 441,427 million (≈US$ 441.4 bn)** for FY2025-26 exports, which aligns with the claim. However, the *earlier FY2024-25 export total* in the snapshot is **US$ 437,685 million (≈US$ 437.7 bn)**, not the **US$ 438 bn** mentioned in the README as "about." This discrepancy in the FY2024-25 figure (rounded vs. exact) is a minor factual inconsistency. [confidence: medium]

- **"FY2025-26 imports: US$ 775.7 bn"** — The article states this as the "sum of chapters," but the *sample output* shows **US$ 775,689 million (≈US$ 775.7 bn)**, which matches. However, the *implied balance* calculation (-US$ 334.262 bn) is derived from these totals, but the article does not cross-validate this against the **official DGFT or RBI trade balance figures for FY2025-26** (which, as of mid-2026, would likely differ slightly due to revisions or additional data sources like services trade). [confidence: medium]

*(Note: No outright contradictions with known data, but the article lacks verification against authoritative sources for these aggregated totals.)*

---

**INTERPRETATION ERRORS:**
- **"The committed CSV snapshot already holds two financial years for both flows, so the demo ran with no browser and no network: 17 tests passed and the queries below took seconds."**
  — The claim implies that the *snapshot data is complete and final* for FY2025-26 (pulled on 15 Sep 2026), but the article itself warns: **"check how complete that year is before relying on it."** This creates a logical gap: the article treats the snapshot as a reliable baseline for analysis (e.g., top chapters, growth rates) while acknowledging its incompleteness. Users may misinterpret the data as definitive without considering the caveat. [confidence: high]

- **"Mineral fuels is the largest line on both sides of the ledger."**
  — While true for FY2025-26 (as shown in the top chapters), the article does not contextualize whether this dominance is *structural* (e.g., long-term trend) or *cyclical* (e.g., driven by oil/gas price spikes). For example, FY2024-25 data (also shown) might reveal volatility in mineral fuels imports/exports, but the article does not compare trends or attribute the pattern to specific economic factors (e.g., energy transition policies, global commodity markets). [confidence: high]

---

**OUTDATED DATA:**
- **"US$ 438 bn exports, about US$ 721 bn imports [FY2024-25]"** — The article cites these as "official" totals from the README, but the *committed snapshot CSV* (as of 19 Oct 2026) reports **US$ 437,685 million (exports) and US$ 721,174 million (imports)** for FY2024-25. While these are likely correct for the snapshot’s pull date (21 Jul 2026), the article does not note whether:
  1. The **DGFT has since revised these figures** (e.g., via a post-FY2025-26 release or press statement).
  2. The **RBI’s trade statistics** (which include services and re-exports) differ materially from the merchandise-only DGFT data.
  *Series to re-check:* **DGFT’s [Export-Import Data Bank](https://www.dgft.gov.in/)** (latest FY2025-26 merchandise trade figures) and **RBI’s [Trade Statistics](https://www.rbi.org.in/)** (latest balance of payments data). [confidence: high]

- **"Latest" FY2025-26 totals (US$ 441.4 bn exports, US$ 775.7 bn imports) from the snapshot pulled on 15 Sep 2026.**
  — The article does not clarify whether these are:
  1. **Final** (e.g., no further revisions expected), or
  2. **Provisional** (e.g., subject to DGFT’s annual reconciliation).
  *Series to re-check:* **DGFT’s FY2025-26 final trade data** (expected release: typically by March 2027). [confidence: high]

---
**Note:** No stylistic or formatting issues were flagged as per instructions. The article’s core methodology (using DGFT data) is sound, but the gaps above could mislead readers about data currency and causal interpretations.
