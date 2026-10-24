# Fact/interpretation check — indias-2026-27-ethanol-tender-drops

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-2026-27-ethanol-tender-drops.html`

Text-SHA1: `d3d9ba2fa579c2e5`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 4368, Requested 5446. Please try again in 13.605s. Need more tokens? Upgrade to Dev Tier today at https://con]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"108 crore litres Most that FCI rice can supply in any quarter; none in August-October"* — The article states FCI rice supply is capped at **108 crore litres per quarter** (Nov-Jul) but does not clarify whether this is a **hard annual cap** (e.g., 432 crore litres/year) or a **quarterly ceiling**. The earlier claim (2025-26) mentioned **72 LMT (324 crore litres) to 30 Jun 2027**, but the **quarterly cap of 108 crore litres** (≈30 LMT) is inconsistent with the total allocation. The **2026-27 FCI rice stock position** (e.g., central pool levels) should be cross-checked with the **FCI’s latest monthly bulletin** (e.g., October 2026 release) to verify if 108 crore litres/quarter is feasible given current holdings.
  [confidence: **high**]

- *"Rs 2,390 a quintal for November 2026 to June 2027"* — While the article cites a **Rajya Sabha reply** (Business Standard) for this price, it does not confirm whether this is the **actual procurement price** or the **market price**. The **FCI’s latest procurement price for ethanol-grade rice** (e.g., from the **2026-27 procurement tender**) should be verified against the **FCI’s official procurement orders** (e.g., via [FCI’s website](https://www.fci.gov.in)) to ensure this is not an outdated or misreported figure.
  [confidence: **medium**]

---

**INTERPRETATION ERRORS:**
- *"The saving to the oil companies depends on how much maize they end up buying. At last year’s maize volume of about 479 crore litres, Rs 3 a litre is about Rs 1,440 crore a year, by this blog’s arithmetic; the actual figure will be known only after allocation."*
  **Gap:** The article **extrapolates last year’s maize volume (479 crore litres) to this year’s tender (1,100 crore litres total)** without accounting for:
  1. The **elimination of cane-based ethanol** (26% of last year’s allocation), which likely reduced maize’s share (maize was 45.7% in 2025-26).
  2. The **cheapest-first allocation rule**, which may **displace maize** in favor of FCI rice or damaged grain (even if maize is now cheaper by Rs 3/litre).
  3. The **Supreme Court’s provisional awards**, which could **reduce maize allocations** further.
  The **Rs 1,440 crore saving** assumes maize’s share remains constant, but the **new tender structure** (e.g., FCI rice cap, no cane juice) could **halve maize’s volume**, making the saving estimate **overstated**.
  [confidence: **high**]

- *"Damaged grain, mostly broken rice, at Rs 64 could take share from maize."*
  **Gap:** While damaged grain is **cheaper than maize (Rs 64 vs. Rs 68.86)**, the claim assumes:
  1. **Supply availability**: Damaged grain’s **actual production and stock levels** (e.g., from the **2026-27 Food Corporation of India’s buffer stock report**) are not provided. If stocks are low, maize may still dominate.
  2. **Quality constraints**: Damaged grain’s **ethanol yield per quintal** may be lower than maize, offsetting the price advantage.
  3. **Logistics**: Damaged grain often comes from **food grain buffer zones**, while maize is more widely distributed. The **transport cost differential** (e.g., hill/north-east surcharges) could negate the Rs 4.86 price gap.
  The article **treats damaged grain as a direct substitute** without verifying these constraints.
  [confidence: **medium**]

---
**OUTDATED DATA:**
- *"Rs 60.32 FCI rice price for ethanol (unchanged from 2025-26)"*
  **Series to re-check:** **FCI’s latest procurement price for ethanol-grade rice** (e.g., from the **2026-27 procurement tender** or **monthly bulletin**).
  - The article cites a **Rajya Sabha reply (Business Standard)** for the **market price (Rs 2,390/quintal)**, but the **FCI’s actual procurement price for ethanol-grade rice** (e.g., **MSP or special rate for distilleries**) may have changed.
  - The **2025-26 price (Rs 60.32/litre)** should be cross-checked against the **2026-27 FCI procurement orders** (e.g., via [FCI’s website](https://www.fci.gov.in)) or the **latest ethanol policy notification**.
  [confidence: **high**]

- *"Diesel benchmark: Rs 98.08 a litre (30 Sep 2026), 8.4% higher"*
  **Series to re-check:** **Latest diesel price benchmark for ethanol blending** (e.g., from the **Oil Marketing Companies’ latest circular** or **Ministry of Petroleum & Natural Gas’ monthly data**).
  - The **30 Sep 2026 benchmark** may have been **revised** in subsequent months (e.g., October/November 2026). The **transport cost adjustment** (Rs 2.36/km) is tied to this, so an outdated benchmark could misstate **actual transport subsidies**.
  [confidence: **medium**]

---
**Note:** No issues were found under **none found** for any category.
