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

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 13031, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"India’s exports of CBAM-covered goods to the EU in 2024, fourth after China, Türkiye and the UK; 85% of it iron and steel"** — The claim that India’s 2024 exports were **USD 6.32 billion** (RIS/UN Comtrade) is correct, but the **ranking as "fourth"** is inconsistent with the later claim that India’s **2024-25 steel/aluminium exports to the EU fell 24.4% to USD 5.82 billion**, which would place it **below China (USD 16.3 bn), Türkiye (USD 11.0 bn), and the UK (USD 8.2 bn)** but *above* the UK if the 2024 figure is isolated. The **85% iron/steel share** is plausible but not explicitly cross-validated with the later **USD 5.4 bn (2024, RIS/UN Comtrade)** for iron/steel alone. [confidence: **medium**]

- **"India’s share of EU finished-steel imports, January–June 2026 (EUROFER); its shipments to the EU fell 19.8% in the same months"** — The **19.8% fall** in shipments (BigMint) is correct, but the **EUROFER share claim (7.7%)** conflicts with the **EUROFER Economic and Steel Market Outlook Q3 2026** (reported via GMK Center), which lists India’s **H1 2026 share as 7.7%** *but also shows Türkiye (15.7%), China (12.3%), and South Korea (12.0%) ahead of India*. The **19.8% decline** is supported by BigMint but not explicitly tied to EUROFER’s *share* data in the same period. [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- **"India’s own carbon credits, expected at €6–13 a tonne and not yet traded, are not recognised by the EU and would deduct little if they were"** — While the **€6–13 range** is plausible (analyst estimates), the claim **overstates the potential deduction**. The **EU’s draft rules (13 May 2026)** require that:
  1) The foreign carbon price **must net out free allocation, rebates, and exemptions** (CCTS’s "zero-price" for compliant plants undermines this).
  2) Only **Paris Agreement Article 6 credits** (not domestic CCTS) are eligible, and the **European Parliament voted to remove even that route** (15 Sept 2026).
  The **LiveLaw analysis** and **CII–IIM Ahmedabad report** explicitly argue CCTS **cannot clear the EU’s bar** due to design flaws. Thus, the deduction is **not "little"**—it’s **effectively zero** under current rules. [confidence: **high**]

- **"The cost of complying is small. Vendors quote €5,000–50,000 per installation for CBAM verification"** — The **€5k–50k upfront cost** is correct for **emissions accounting/auditing**, but the claim **underplays the opportunity cost**. For a **small Indian mill shipping 300 tonnes/year to the EU**, the **€177/tonne default penalty** (vs. €93 with verification) translates to **€53,100 in lost revenue**—**far exceeding** the verification cost. The article later acknowledges this for **large mills (€177M/year for 1 Mt)**, but the **small-firm implication is misleading** without quantifying the **net cost** (€5k–50k vs. €53k+). [confidence: **medium**]

---
**OUTDATED DATA:**
- **"India’s exports of CBAM-covered goods to the EU in 2024, USD 6.32 billion (RIS/UN Comtrade data)"** — The **2024 figure is correct**, but the **2025-26 data (USD 24.4 bn globally, USD 17.4 bn iron/steel)** in the later table suggests **newer TradeStat/GTRI figures (24 Oct 2026)** may supersede the 2024 RIS/UN Comtrade baseline. Re-check **TradeStat Export Import Data Bank (2025-26)** for updated EU-specific splits. [confidence: **high**]

- **"EU crude steel output fell 2.9% in 2025 to 125.8 Mt, a record low"** — The **2025 output (125.8 Mt)** is correct per **EUROFER (Oct 2026)**, but the **2026 H1 data** (not quoted) may show further declines. Re-check **EUROFER’s *European Steel in Figures 2026* (Q4 2026 release)** for **2026 annual projections**. [confidence: **medium**]

---
**Note:** No stylistic or formatting issues were requested for review.
