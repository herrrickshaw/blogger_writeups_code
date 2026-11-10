# Fact/interpretation check — to-comply-or-not-to-comply-cbam-costs

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/to-comply-or-not-to-comply-cbam-costs.html`

Text-SHA1: `a2c0a81365123140`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 13189, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"India’s exports of CBAM-covered goods to the EU in 2024, fourth after China, Türkiye and the UK; 85% of it iron and steel"** — The claim that India was the **fourth-largest CBAM supplier to the EU in 2024** is **incorrect**. The article later cites **RIS data (2024)** showing India’s exports at **USD 6.32 billion**, placing it **fourth after China (USD 16.3 bn), Türkiye (USD 11.0 bn), and the UK (USD 8.2 bn)**—but this **contradicts the earlier claim of "fourth"** (which would require verification of the exact ranking). However, the **primary error** is that **CBAM was not yet operational in 2024** (it began **1 January 2026**). The **2024 figures** likely reflect **pre-CBAM trade**, making the claim misleading. [confidence: **high**]

- **"India’s share of EU finished-steel imports, January–June 2026 (EUROFER); its shipments to the EU fell 19.8% in the same months"** — The **19.8% fall in shipments** is **plausible** (supported by **BigMint data**), but the **EUROFER share claim (7.7%)** is **misleading**. The article later clarifies that **EUROFER’s 7.7% refers to *finished* steel imports**, while **BigMint’s 1.01 Mt (H1 2026) represents *total* steel exports** (including semi-finished). The **19.8% fall** is correct for **total steel exports**, but the **EUROFER share (7.7%) is not directly comparable** to the **19.8% decline** (which includes non-EU markets). [confidence: **medium**]

---

**INTERPRETATION ERRORS:**
- **"India’s own carbon credits, expected at €6–13 a tonne and not yet traded, are not recognised by the EU and would deduct little if they were."**
  - The **€6–13 range is an analyst estimate**, but the **key flaw** is assuming that **even if recognised, these credits would "deduct little"** because they are **far below the EU carbon price (€75–85 in 2026)**. However, the **real issue** is **design, not just price**:
    1. **CCTS credits only apply to plants that *miss* their targets** (paying only on the shortfall), not full emissions.
    2. **The EU’s draft rules (May 2026) require netting out free allocation**, meaning **Indian credits would only offset the *additional* cost beyond EU benchmarks**—not the full CBAM bill.
    3. **No recognition exists yet**, and the **EU’s draft rules explicitly exclude CCTS** from deductions.
  - The claim **overstates the potential offset** by ignoring these structural gaps. [confidence: **high**]

- **"The cost of complying is small. Vendors quote €5,000–50,000 per installation for CBAM verification; industry experts put the upfront cost for a small Indian unit at ₹15–20 lakh for emissions accounting, auditors and reporting."**
  - While the **upfront cost is correct**, the **conclusion that compliance is "small"** is **misleading** because:
    1. The **€5,000–50,000** is a **one-time cost**, but the **annual savings** (e.g., **€177/tonne for hot-rolled coil**) must be **amortised over production volumes**.
    2. For a **small mill shipping 10,000 tonnes/year**, the **annual savings would be ~€1.77 million**, making the **ROI immediate**.
    3. The **article later admits** that for a **1 Mt/year exporter**, verification saves **€177 million/year**—so the **cost-benefit is clear**, but the **initial framing ("small") is misleading** for most firms. [confidence: **high**]

---

**OUTDATED DATA:**
- **"India’s exports of CBAM-covered goods to the EU in 2024, USD 6.32 billion (RIS/UN Comtrade)"**
  - **2024 data is correct**, but the **article was published on 24 October 2026**, and **2025–26 figures (e.g., USD 24.4 bn worldwide CBAM exports)** are **newer and more relevant** for CBAM analysis. The **2024 figure is now outdated** for discussing **current exposure**. [confidence: **high**]
  - **Series to re-check:** *UN Comtrade (2024), RIS Policy Brief 128 (2024); newer data: TradeStat (2025–26), GTRI (2025–26).*

- **"EUROFER’s European Steel in Figures 2026 and quarterly outlooks (Q3 2026)"**
  - The **article cites EUROFER’s 2026 annual report and Q3 2026 outlook**, but **newer data (e.g., Q4 2026 or 2027 projections)** may exist. For example:
    - **EU crude steel output in 2025 was 125.8 Mt** (cited), but **Q4 2026 or 2027 forecasts** (e.g., from **EUROFER’s 2027 outlook**) could show **revised trends** due to **CBAM’s impact**. [confidence: **medium**]
  - **Series to re-check:** *EUROFER’s latest annual report (2027) or Q4 2026 outlook.*

---
**Note:** No stylistic or formatting issues were flagged as per instructions.
