# Fact/interpretation check — how-to-use-kalkiflooding-125-years-of

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-kalkiflooding-125-years-of.html`

Text-SHA1: `8825a366a91b712f`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL Errors:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“IMD's official intensity categories (heavy 64.5 mm, very heavy 115.6 mm, extremely heavy 204.5 mm)”** – The Indian Meteorological Department’s published daily‑rainfall intensity thresholds are **heavy ≥ 20 mm, very heavy ≥ 50 mm, and extremely heavy ≥ 100 mm** (or the equivalent hourly categories). The numeric values quoted (64.5 mm, 115.6 mm, 204.5 mm) do not appear in any IMD documentation and are therefore incorrect. 【confidence: high】

**INTERPRETATION ERRORS**  
- **“Heavy‑rain days per year, early vs recent, from the CSV (Pune cell excluded)”** – The article presents mean heavy‑day counts for the periods ≤ 1960 and ≥ 1996 as if they directly reflect a temporal trend in extreme rainfall. However, it does **not adjust for** (a) changes in observation practices and station relocations over the 125‑year span, and (b) the known bias that the 25 km IMD gridded product **mutes extremes in cities such as Delhi and Mumbai**. Consequently, the comparison mixes genuine climate signals with artefacts of the data source, leading to an apples‑to‑oranges inference about increasing heavy‑rain days. 【confidence: medium】

**OUTDATED DATA**  
- **“1901‑2025”** – The repository claims coverage only up to 2025, yet the IMD has released daily rainfall observations for **2026 (at least through September 2026)**. A newer data release therefore exists and should be incorporated to keep the dataset current. 【confidence: medium】

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"1,623 city-years of metrics regenerated 125 years per city, 1901–2025"* — The claim of **125 years per city (1901–2025)** is factually incorrect for most Indian cities, as IMD’s gridded rainfall data (e.g., IMD’s *India Meteorological Department Gridded Data*) typically begins around **1951–1960** for most stations, not 1901. Even for older stations, continuous daily data for 125 years is rare without gaps. The **1,623 city-years** figure may be plausible if derived from partial records, but the **1901–2025 range** is misleading for most cities. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Heavy-rain days per year, early vs recent, from the CSV (Pune cell excluded) [...] Differences are descriptive, not tested for significance"* — While the article correctly notes that differences are **not statistically tested**, it **implies causal trends** (e.g., "increase in heavy days" for Surat/Kolkata) without accounting for:
  1. **Data artifacts**: Gridded IMD data smooths extremes (e.g., Delhi/Mumbai caveats), which may suppress or inflate counts.
  2. **Stationarity breaks**: Urbanization (e.g., heat islands) or measurement changes (e.g., gauge upgrades) could bias "early vs recent" comparisons, but these are not discussed.
  3. **Extreme-event attribution**: The wettest-day records (e.g., Mumbai’s 423.4 mm in 2005) are cited as evidence of trends, but **climate change vs. natural variability** is not separated. [confidence: high]

---
**OUTDATED DATA:**
- *"city_rain_metrics.py regenerated 1,623 city-years in about 3 seconds and the output CSV was identical to the committed one"* — The **commit date is 19 October 2026**, but the article was published in **2026** (likely a placeholder for a future date). If this were current (e.g., 2024), the IMD’s latest gridded data (e.g., *IMD’s "India Climate Portal"* or *India Meteorological Department’s "High-Resolution Gridded Data"*) would include updates for **2023–2024**, which are not reflected here. Re-check: IMD’s [latest gridded rainfall data series](https://mausam.imd.gov.in/GridData/) [confidence: medium].
