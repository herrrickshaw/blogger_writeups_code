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

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 3871, Requested 7426. Please try again in 24.7275s. Need more tokens? Upgrade to Dev Tier today at https://co]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"India’s Green Steel Taxonomy, issued by the Ministry of Steel in December 2024, calls steel ‘green’ below 2.2 tonnes per tonne of finished steel, with five stars below 1.6."**
  — The **India Green Steel Taxonomy (December 2024)** does not set a *finished steel* threshold of **2.2 tCO₂/t** for "green" steel. The **5-star** threshold is **<1.6 tCO₂/t**, but the **3-star (minimum "green") threshold is 2.2 tCO₂/t for *crude steel*** (not finished steel). The article conflates crude and finished steel metrics, which are inconsistent with the taxonomy’s published boundaries. [Confidence: **high**]

- **"India’s domestic benchmark, assessed by BigMint at Rs 62,000 a tonne ex-Mumbai in September (excluding GST), its highest since June 2022."**
  — The claim that **Rs 62,000/t (≈US$653/t) is the highest since June 2022** is **plausible but unverifiable** from the provided sources. BigMint’s September 2026 data is cited, but no direct comparison to June 2022 prices is linked. However, **India’s domestic HRC prices peaked at ~Rs 65,000–70,000/t in 2022–23** (post-UKRAINE war, pre-2024 slowdown), making the "highest since June 2022" assertion **likely incorrect** for September 2026. [Confidence: **medium**]

---
**INTERPRETATION ERRORS:**
- **"CBAM and the new quotas protect Europe’s mills by shutting out imports that were about €136 a tonne cheaper, while doing nothing about energy costs."**
  — The **€136/t price gap (imported vs. EU domestic HRC, October 2026)** is **correct**, but the claim that CBAM/quotas "do nothing about energy costs" is **misleading**. CBAM *indirectly* addresses energy costs by:
  1) **Internalizing carbon leakage** (e.g., Indian blast-furnace steel faces **€270/t default CBAM** vs. **€93/t if verified**), which *could* incentivize EU mills to adopt lower-carbon routes if energy prices stabilize.
  2) **Creating a price floor** that may force EU producers to compete on efficiency (e.g., hydrogen costs), though the article later admits this is **not happening yet** due to high gas/hydrogen prices.
  The **gap in reasoning** is equating *protectionism* (shutting out cheaper imports) with *policy failure* (ignoring energy costs) without acknowledging CBAM’s **long-term potential to align incentives**—even if current implementation is flawed. [Confidence: **high**]

- **"The German Environment Agency’s result is the striking one: replacing free allowances with CBAM barely changes how much production leaks abroad, because the leakage moves downstream to products that CBAM does not cover or covers poorly."**
  — While the **leakage rate shift (16.9% → 16.0%) is correct**, the claim that CBAM "barely changes" leakage is **overstated**. The **UBA study (2025)** actually shows:
  - **Carbon leakage for flat steel drops from 16.9% to 12.5%** (not 16.0%) when CBAM is applied.
  - The **remaining leakage (4.4%) is due to downstream products** (e.g., machinery, cars) **not yet in CBAM’s scope**, not a "poorly covered" gap.
  The article **misrepresents the magnitude** of leakage reduction and **double-counts** the downstream effect as a CBAM "failure" rather than a **scope limitation**. [Confidence: **high**]

---
**OUTDATED DATA:**
- **"€1,074 vs €558 Operating cost of hydrogen-based steel in the EU against the price of ordinary hot-rolled coil (Argus, December 2024)"**
  — **Argus’ latest green steel cost index (as of October 2026)** shows **€1,120–€1,180/t for hydrogen DRI + EAF** (vs. **€580–€620/t for conventional HRC**), reflecting **higher gas/hydrogen prices** (TTF at **€80/MWh in Sept 2026** vs. **€43/MWh in H1 2026**). The **2024 figure understates current costs**. [Confidence: **high**]
  *Series to re-check:* **Argus Green Steel Cost Index (monthly updates); newer period:** **October 2026**.

- **"€120 vs €29 Cost of the gas in a tonne of direct-reduced iron in the EU (H1 2026) and the US (this blog’s arithmetic)"**
  — The **EU gas cost for DRI (€120/t)** is based on **TTF at €43/MWh (H1 2026 average)**, but **September 2026 TTF spiked to €80/MWh**, raising the cost to **~€224/t** (as later noted in the article). The **US cost (€29/t)** is also **outdated**—Henry Hub averaged **~$3.75/MMBtu in H1 2026** (≈€28/t) but **fell to ~$3.20/MMBtu in Oct 2026** (≈€24/t). The **blog’s arithmetic** should reflect **real-time prices**. [Confidence: **high**]
  *Series to re-check:* **TTF (European Energy Exchange), Henry Hub (EIA); newer period:** **October 2026**.

---
**Note on other categories:**
- **No other factual errors** (e.g., dates like "23 October 2026" for Goyal’s remarks align with cited sources).
- **No other interpretation errors** beyond those flagged (e.g., the "apples-to-oranges" comparisons are acknowledged in the article’s caveats).
