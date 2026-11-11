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

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 13700, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India’s exports of CBAM-covered goods to the EU in 2024, fourth after China, Türkiye and the UK; 85% of it iron and steel"* — The claim that India was **4th** in CBAM-covered exports to the EU in 2024 is **incorrect** based on the later-cited **RIS Policy Brief (2026)** and **UN Comtrade data**, which place India at **USD 6.32 billion** (4th after China, Türkiye, and the UK). However, the **GTRI data** for **2024-25** (fiscal year) shows **steel and aluminium exports to the EU fell 24.4% to USD 5.82 billion**, meaning the **2024 figure (USD 6.32 bn) is likely for 2024-25 (April 2024–March 2025)**, not calendar 2024. The article conflates fiscal and calendar years without clarification. [confidence: **high**]

- *"India’s share of EU finished-steel imports, January–June 2026 (EUROFER); its shipments to the EU fell 19.8% in the same months"* — The **19.8% fall** in shipments to the EU (BigMint data) **contradicts** the **EUROFER claim of a 7.7% share in H1 2026** (which is a **volume share**, not a percentage change). The article mixes **volume share (7.7%)** with **value-based percentage decline (19.8%)** without specifying units, creating ambiguity. [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- *"India’s own carbon credits, expected at €6–13 a tonne and not yet traded, are not recognised by the EU and would deduct little if they were"* — While correct that **Indian CCTS credits are not yet recognised by the EU**, the claim that they would **"deduct little"** is **misleading**. The **real issue** is **design flaws in CCTS**:
  - **Free allocation loophole**: CCTS allows plants that **meet their targets** to pay **zero effective price**, meaning no deduction applies. Only plants that **miss targets** pay on shortfalls (e.g., ~€1.71/t at €13/credit for a 2.5 tCO₂/t mill missing a 5% cut). Thus, **even if recognised, CCTS would not reduce CBAM costs meaningfully** for compliant mills. The article **overstates the potential impact** by implying a uniform deduction. [confidence: **high**]

- *"The cost of complying is small. Vendors quote €5,000–50,000 per installation for CBAM verification; industry experts put the upfront cost for a small Indian unit at ₹15–20 lakh for emissions accounting, auditors and reporting. At €177 a tonne, a mill recovers €50,000 on its first 300 tonnes."* — The **€177/t savings** (default vs. verified) is **correct for hot-rolled coil**, but the **recovery calculation is flawed**:
  - **€50,000 / 300 tonnes = €166.67/t saved**, not €177/t. The article **rounds inconsistently** and **double-counts** the €177 figure in the preceding sentence. More critically, **small firms (e.g., fasteners) cannot access verified data** (they rely on mill suppliers), so the **€177/t savings only applies to integrated mills**, not the **80% of CBAM-exposed exports that are processed goods** (e.g., pipes, fittings). The article **generalises** without distinguishing between **direct exporters (mills) and indirect exporters (traders)**. [confidence: **high**]

---

**OUTDATED DATA:**
- *"India’s exports of CBAM-covered goods to the EU at USD 6.32 billion in 2024, from UN Comtrade data"* — The **2024 figure is outdated**; the article later cites **GTRI’s 2024-25 (fiscal year) data (USD 5.82 bn)** and **TradeStat’s 2025-26 (USD 24.4 bn globally, ~33% to EU for steel)**. The **latest official UN Comtrade data for 2025** (not 2024) would reflect **post-CBAM reporting obligations** (since Oct 2023) and **2026 quota effects**. Re-check: **UN Comtrade (2025 calendar year)**. [confidence: **high**]

- *"EUROFER’s European Steel in Figures 2026 and quarterly outlooks"* — The article cites **EUROFER’s Q3 2026 outlook (1 Oct 2026)** for **H1 2026 data**, but **EUROFER’s latest annual report (2026) may have been updated** with **Q4 2026 or 2027 projections** by the time of publication (24 Oct 2026). Re-check: **EUROFER’s 2026 Annual Report (latest version)** and **Q4 2026 outlook** for **2026–27 forecasts**. [confidence: **medium**]

---
**Note:** The article’s **2026 publication date** means some claims (e.g., **CBAM certificate prices, EU default values**) are **time-sensitive but not inherently "outdated"** unless superseded by later EU regulations (e.g., **2026/1740 corrections**). No such updates were flagged in the text.
