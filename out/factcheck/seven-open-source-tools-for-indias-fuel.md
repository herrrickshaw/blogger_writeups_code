# Fact/interpretation check — seven-open-source-tools-for-indias-fuel

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/seven-open-source-tools-for-indias-fuel.html`

Text-SHA1: `dc51d028bb1efe92`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
none found  

**INTERPRETATION ERRORS:**  
- *“The mechanism: blended fuel has less energy per litre, so drivers buy more litres, which raises pump throughput and so oil‑company income.”* — The claim treats the increase in litres sold as automatically translating into higher oil‑company revenue, ignoring that pump margins are typically expressed per litre and that price per litre may fall with lower‑energy blends. Without accounting for price adjustments or demand‑elasticity effects, the causal link between extra volume and higher income is overstated. [confidence: high]  

- *“The model assumes a 4% mileage drop at E20, while the energy‑content script implies about 6.8% less energy per litre and 7.3% more litres; that choice drives the extra‑income result.”* — By selecting a mileage‑drop assumption that is substantially lower than the physical energy loss, the model biases the outcome toward a larger income gain for oil companies. The reasoning conflates a modelling convenience with a factual effect, creating an apples‑to‑oranges comparison between assumed mileage loss and calculated energy loss. [confidence: medium]  

**OUTDATED DATA:**  
- *“PPAC Ready Reckoner, FY2025‑26 H1 edition”* — The article relies on the half‑year edition of the FY2025‑26 Ready Reckoner. By November 2026, the FY2026‑27 H1 (and possibly full‑year) edition would have been released, providing more current refining margins and fuel‑sales figures. The series to re‑check is the PPAC Ready Reckoner tables for FY2026‑27 (H1 and later). [confidence: high]  

- *“The populations are older census‑based numbers.”* — The population figures used for per‑capita pump density are drawn from the 2011 Census (or earlier estimates). Updated population estimates from the 2021 Census or the Ministry of Statistics and Programme Implementation’s 2024 mid‑year estimates are now available and should replace the older numbers. The series to re‑check is “India state‑wise population estimates, 2024‑2025” from the official statistical releases. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"21% of rows in the raw pump crawl (16 Oct 2026 file) are duplicates"* — The article later states the deduplication removed **22,343 duplicates** (21.3% of 104,945 rows), not 21%. The claim of "21%" is inconsistent with the worked example’s precise calculation. [confidence: high]

**INTERPRETATION ERRORS:**
- *"4% vs about 7% the E20 mileage drop two models assume, against the extra litres implied by energy content alone"* — The article conflates two distinct metrics: (1) the **assumed mileage drop** (4% vs. 6.8%) and (2) the **energy-content-based volume increase** (7.3%). While both are relevant, the claim implies a direct contradiction between the two, but the 7% figure is derived from energy density calculations (not mileage drop) and doesn’t directly "refute" the 4% assumption. The reasoning conflates apples and oranges. [confidence: high]

**OUTDATED DATA:**
- *"100 tables from PPAC’s Ready Reckoner (FY2025-26 H1 edition)"* — The article does not specify if this is the latest edition. PPAC’s Ready Reckoner is typically updated annually; the FY2026-27 edition (or later) may exist. [confidence: medium]
- *"July 2026 price basis"* (vehicle_fuel_mileage model) — Fuel prices fluctuate; no indication this was updated post-July 2026. [confidence: medium]
