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

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 11870, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India’s share of EU finished-steel imports, January–June 2026 (EUROFER); its shipments to the EU fell 19.8% in the same months"* — **India’s EU steel exports fell 19.8% in H1 2026 (per BigMint), but its *share* of EU imports was **7.7%** (EUROFER), not a percentage decline. The phrasing conflates volume and share metrics. [confidence: high]
- *"India exported about US$24.4 billion of CBAM goods to all countries in 2025-26; the EU took 33% of its chapter 72 iron and steel"* — **The $24.4B figure includes *all* CBAM-covered exports (not just EU-bound), while the 33% EU share applies only to *chapter 72* (iron/steel) exports. The article misrepresents the scope of the 33% claim. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Indian carbon credits, expected at €6–13 a tonne and not yet traded, are not recognised by the EU and would deduct little if they were"* — **The claim assumes Indian credits could *ever* offset CBAM costs at their current price range (€6–13), but the EU’s draft rules require:
  1) Recognition of the *entire* domestic carbon price (not just credits for overperformance),
  2) Netting out of free allocations/exemptions (which CCTS lacks),
  3) A formal deduction mechanism (none exists yet).
  Even if credits traded at €13/t, the *effective* deduction would likely be near-zero due to these design flaws. [confidence: high]
- *"The EU’s carbon bill for steel in 2026 is €3.4 billion (€27/t average), so CBAM is ‘generous’ for EU mills"* — **This ignores that the €27/t figure is the *net* bill after free allocation (97.5% of the benchmark). The *gross* emissions cost for EU mills is far higher (e.g., ~1.8–2.2 tCO₂/t for blast-furnace steel), and the "generosity" stems from the benchmark being set at the *most efficient* EU plants—most mills pay more. The article conflates net and gross costs. [confidence: high]

---
**OUTDATED DATA:**
- *"India’s exports of CBAM-covered goods to the EU in 2024, USD 6.32 billion (RIS/UN Comtrade)"* — **The latest UN Comtrade data (as of October 2026) for 2024 CBAM-covered exports to the EU should be cross-checked with the *2025* UN Comtrade release (expected mid-2026) and India’s *2025-26* TradeStat figures (published 24 Oct 2026). The 2024 figure may now be superseded by 2025 data. [confidence: high]
- *"EU crude steel output fell 2.9% in 2025 to 125.8 Mt"* — **EUROFER’s *Q3 2026 Economic and Steel Market Outlook* (1 Oct 2026) likely includes updated 2025 production data (e.g., revised estimates or preliminary 2026 figures). The 125.8 Mt figure may have been updated in the latest report. [confidence: high]
