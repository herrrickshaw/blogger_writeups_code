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

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 12990, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India’s exports of CBAM-covered goods to the EU in 2024, fourth after China, Türkiye and the UK; 85% of it iron and steel"* — The claim that India was the **fourth-largest CBAM supplier in 2024** is inconsistent with later data in the article. The **RIS Policy Brief (24 Oct 2026)** cites **USD 6.32 billion** for India (vs. USD 16.3B China, USD 11B Türkiye, USD 8.2B UK), but **GTRI’s FY2024-25 data** shows **steel/aluminium exports to the EU fell 24.4% to USD 5.82B**, suggesting the 2024 figure may be outdated or misaligned with the latest trade flows. [confidence: **high**]

- *"India’s share of EU finished-steel imports, January–June 2026 (EUROFER): 7.7%"* — While **EUROFER’s Q3 2026 report** (cited) lists India at **7.7%**, the **BigMint data** (also cited) shows **1.01 Mt shipped in H1 2026 (down 19.8%)**, conflicting with the **2.4 Mt share** implied by EUROFER’s **29.7 Mt total imports**. The discrepancy arises from **product scope differences** (BigMint’s tonnage vs. EUROFER’s value-weighted share). [confidence: **medium**]

---

**INTERPRETATION ERRORS:**
- *"India’s own carbon credits, expected at €6–13 a tonne and not yet traded, are not recognised by the EU and would deduct little if they were"* — The claim **misrepresents the deduction mechanism**. The **EU’s draft CBAM rules (May 2026)** require foreign carbon prices to **net out free allocation, rebates, and exemptions**—not just subtract the price. Under **CCTS**, a mill that **misses its target** pays only on the shortfall (e.g., 0.13 tCO₂/t at €13 = €1.71/t), which is **far below the €93/t verified CBAM charge** but **not a direct offset** against the full benchmark. The article conflates **potential price impact** with **actual deduction eligibility**. [confidence: **high**]

- *"The cost of complying is small... At €177 a tonne, a mill recovers €50,000 on its first 300 tonnes"* — This **double-counts savings** by ignoring that **verified emissions (e.g., 2.5 tCO₂/t) already reduce the CBAM charge** (e.g., from €270 to €93). The **€177 "extra cost of not verifying"** is the **difference between default (€270) and verified (€93)**, not an incremental cost. The phrasing implies verification is **costly without upfront savings**, which obscures the **net benefit** of €177/t. [confidence: **high**]

---
**OUTDATED DATA:**
- *"India’s exports of CBAM-covered goods to the EU in 2024, USD 6.3 billion"* — The **RIS Policy Brief (24 Oct 2026)** cites this figure, but **GTRI’s FY2024-25 data** (also cited) shows **steel/aluminium exports to the EU fell 24.4% to USD 5.82B**, implying the **2024 figure may be stale**. Re-check **UN Comtrade (latest 2024 release)** and **GTRI’s FY2025-26 projections** for alignment. [confidence: **high**]

- *"India’s share of EU finished-steel imports, January–June 2026 (EUROFER): 7.7%"* — While **EUROFER’s Q3 2026 report** (cited) is the latest, **BigMint’s H1 2026 data (29 July 2026)** shows **1.01 Mt shipped (down 19.8%)**, conflicting with EUROFER’s **2.4 Mt share of 29.7 Mt total**. Re-check **EUROFER’s Q4 2026 update** (expected Nov 2026) for revised H1 2026 figures. [confidence: **high**]

---
**Note:** The article’s **cost-per-tonne tables (e.g., €93 vs. €270)** are **not outdated** as they are derived from **2026 CBAM benchmarks** (Regulation 2023/956, simplified by 2025/2083), but the **underlying export volumes** (e.g., 2024 vs. H1 2026) require cross-verification.
