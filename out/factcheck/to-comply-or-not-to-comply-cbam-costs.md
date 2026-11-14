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

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 13101, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"India’s share of EU finished-steel imports, January–June 2026 (EUROFER); its shipments to the EU fell 19.8% in the same months"** — The claim conflates two inconsistent metrics: EUROFER’s *share* (7.7%) and BigMint’s *volume* decline (19.8%). The 19.8% figure is correct for total EU-bound shipments (1.01 Mt in H1 2026 vs. 1.26 Mt in H1 2025), but the EUROFER share (7.7%) refers to a different baseline (total EU imports of 29.7 Mt in 2025). The article does not reconcile these conflicting data points.
  [confidence: high]

- **"India’s exports of CBAM-covered goods to the EU at USD 6.32 billion in 2024"** — The RIS/UN Comtrade figure (USD 6.32 bn) contradicts GTRI’s fiscal-year data (USD 5.82 bn in 2024–25), which shows a *decline* in steel/aluminium exports to the EU. The article does not clarify whether the USD 6.32 bn figure is for calendar 2024 or fiscal 2024–25, or reconcile it with GTRI’s downward revision.
  [confidence: high]

---
**INTERPRETATION ERRORS:**
- **"India’s own carbon credits, expected at €6–13 a tonne and not yet traded, are not recognised by the EU and would deduct little if they were"** — While correct that EU recognition is absent, the claim *overstates* the potential deduction even hypothetically. The EU’s draft rules (May 2026) require netting out *all* free allocations/rebates from the foreign carbon price, meaning CCTS credits (which often cover *only* shortfalls, not full emissions) would likely yield negligible deductions (e.g., a mill missing its 5% intensity target might buy credits for ~0.13 tCO₂/t, translating to ~€1.71/t at €13/credit, far below the €93–270 CBAM charge).
  [confidence: high]

- **"The cost of complying is small"** (referring to verification costs of ₹15–20 lakh for small mills) — This ignores the *tonnage-dependent* economics. For a small mill shipping 300 tonnes/year to the EU, the €177/t savings on verified data (vs. defaults) would indeed offset verification costs, but the claim generalizes without noting that *large exporters* (e.g., 1 Mt/year) face €177 million in annual savings—making verification a *mandatory* cost-cutting measure, not a "small" one.
  [confidence: high]

---
**OUTDATED DATA:**
- **"India’s exports of CBAM-covered goods to the EU at USD 6.3 bn in 2024"** — The latest official UN Comtrade data for 2024 (released ~June 2026) should be cross-checked against the RIS/UN Comtrade figure cited. For 2025–26, TradeStat’s country-specific data (generated 24 Oct 2026) is the most recent, but the article does not verify whether it aligns with GTRI’s downward revision or Crisil’s quota estimates.
  [confidence: high]

- **"EUROFER’s 2026 annual report, *European Steel in Figures 2026*, and quarterly outlooks"** — EUROFER’s Q3 2026 report (cited as of 1 Oct 2026) may have been superseded by later updates (e.g., Q4 2026 or 2027 projections). The article does not confirm whether the "record-low" crude steel output (125.8 Mt in 2025) was revised in subsequent releases.
  [confidence: medium]

---
**Note:** The article’s reliance on *search-summary sources* (e.g., EUROFEL, CERC regulations) without direct links to primary documents increases risk for factual gaps, but no outright contradictions with known data (e.g., CBAM benchmarks, default values) were found.
