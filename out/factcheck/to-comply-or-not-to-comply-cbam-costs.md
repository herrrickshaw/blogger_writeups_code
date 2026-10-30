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

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 12929, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"India’s exports of CBAM-covered goods to the EU in 2024 were USD 6.32 billion"** — The article cites a **RIS policy brief (2024)** and **UN Comtrade data**, but the **GTRI report (2024-25)** shows a **sharp decline** to **USD 5.82 billion** in steel/aluminium exports to the EU, with iron/steel down **35.1%** to **USD 3.05 billion**. The **2024 figure of USD 6.32 bn** conflates **total CBAM-covered exports** (including cement/fertilisers) with **steel/aluminium-only exports**, which were **USD 5.4 bn** (RIS/UN Comtrade). The **USD 6.3 bn claim** (first paragraph) is **misleadingly aggregated** and contradicts the **later GTRI data** for 2024-25.
  [confidence: **high**]

- **"India’s share of EU finished-steel imports in H1 2026 was 7.7% (EUROFER)"** — While **EUROFER’s Q3 2026 report** lists India at **7.7%**, the **same source** (via GMK Center/IndexBox) shows **Türkiye at 15.7%**, **China at 12.3%**, and **South Korea at 12.0%**, making India **5th**, not **4th** (as the article initially states in the headline). The **ranking error** distorts India’s relative position.
  [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- **"India’s own carbon credits (€6–13/t) would deduct little if recognised"** — The claim **misrepresents the deduction mechanism**: Under **CBAM’s draft rules (May 2026)**, only **carbon prices "effectively paid" in India** (after accounting for **free allocations, rebates, and exemptions**) can offset the CBAM charge. Since **CCTS credits are zero-cost for compliant plants** (only penalised for shortfalls), their **effective price is €0**, not €6–13. Even if recognised, they **cannot offset the full CBAM bill** (e.g., a mill at **2.5 tCO₂/t** missing its target would only deduct **~€1.71/t**, per the article’s own calculation). The **€6–13 range is irrelevant** for CBAM offsets.
  [confidence: **high**]

- **"CBAM costs Indian steel €93–€270/t in 2026, matching Argus/Shanghai Metals Market estimates"** — While the **€93 (verified) vs. €270 (default) range** aligns with **Argus (€269.78)** and **Shanghai Metals Market (€278)**, the article **overstates the policy impact** by ignoring:
  1. **EU free allocation (97.5% in 2026)** means **EU mills pay ~€27/t**, while Indian exporters face **€93–€270/t**—a **disproportionate burden** not fully captured in the cost comparison.
  2. The **€270 default charge assumes 10% mark-up (2026)**, but **India’s actual default values (e.g., 4.28 tCO₂/t for HRC)** are **already 60–80% higher than EU benchmarks (1.37 tCO₂/t)**, making the **€270 figure a ceiling**, not a baseline.
  The **apples-to-oranges comparison** (Indian costs vs. EU costs) **hides the asymmetry** in free allocation.
  [confidence: **high**]

---
**OUTDATED DATA:**
- **"India’s exports of CBAM-covered goods to the EU in 2024: USD 6.3 bn (RIS/UN Comtrade)"** — The **latest official UN Comtrade data (2024)** is **superseded by GTRI’s 2024-25 report (October 2026)**, which shows **steel/aluminium exports to the EU fell 24.4% to USD 5.82 bn**. For **2025-26**, **TradeStat (Department of Commerce, October 2026)** reports **USD 17.4 bn in iron/steel exports globally**, with **33% to the EU (USD 5.73 bn)**—a **higher and more precise figure** than the **USD 6.3 bn aggregate** (which included cement/fertilisers).
  [series to re-check: **UN Comtrade (2024), GTRI 2024-25 report, TradeStat 2025-26**; newer period: **2025-26**]
  [confidence: **high**]

- **"EUROFER’s 2026 annual report (European Steel in Figures 2026) shows EU crude steel output at 125.8 Mt in 2025"** — While **EUROFER’s Q3 2026 outlook (1 October 2026)** confirms **125.8 Mt in 2025**, the **latest EUROSTAT data (as of October 2026)** would include **Q3 2026 figures**, which may show **further declines** (e.g., **BigMint reports EU output fell 5% in H1 2026**). The article **does not reference the most recent quarterly data**.
  [series to re-check: **EUROSTAT (2026 Q3/Q4), EUROFER Q4 2026 report**; newer period: **2026 H2**]
  [confidence: **medium**]

---
**Note:** No stylistic or formatting issues were flagged. The article’s **cost-per-tonne calculations** and **CBAM mechanics** are otherwise well-sourced but **require context** for the errors above.
