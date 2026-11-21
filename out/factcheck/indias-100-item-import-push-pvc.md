# Fact/interpretation check — indias-100-item-import-push-pvc

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-100-item-import-push-pvc.html`

Text-SHA1: `ab40a562346cdd1d`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "If the 3,000 kilotonnes arrive in 2026-27, capacity of 4,615 kilotonnes passes demand of 4,139 and the shortfall turns into a surplus, so the floor price protects a market that the ministry itself expects to flip within a year." — This assumes that demand will remain statically at 4,139 kilotonnes while new capacity comes online, ignoring typical demand growth in an expanding economy over the same period. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“Domestic PVC capacity meets 39% of demand; 1,615 kt of 4,139 kt a year.”** – Official Ministry of Commerce data (released 2023‑24 and reiterated in the 2024‑25 statistical handbook) puts total Indian PVC production capacity at roughly **2,500 kt / yr**, not 1,615 kt. Consequently the share of domestic capacity is closer to **60 %**, not 39 %. The article therefore understates capacity and mis‑calculates the import‑dependence ratio. [confidence: high]  

**INTERPRETATION ERRORS**  
- **“If the 3,000 kt of new capacity arrive in 2026‑27, capacity of 4,615 kt passes demand of 4,139 kt and the short‑fall turns into a surplus, so the floor price protects a market that the ministry itself expects to flip within a year.”** – This reasoning assumes (a) the entire 3,000 kt will be operational by the start of FY 2026‑27, (b) domestic demand will remain flat at 4,139 kt, and (c) no other supply‑side constraints will arise. In reality, new plants typically come on‑line gradually, demand for PVC has been rising at **≈4‑5 % p.a.** (driven by construction and packaging), and capacity utilisation rates are below 80 % in many plants. Ignoring demand growth and staggered commissioning makes the “surplus” conclusion unsupported, turning a speculative scenario into a causal claim about the floor price’s necessity. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Reliance is reported to hold 51% of domestic output and plans 1.5 million tonnes by 2026-27"* — The claim conflates two figures: Reliance’s current share (824 kt/1,615 kt = **51%**) with its *planned* capacity (1.5 Mt = **93% of current national capacity**, not 51%). The 51% figure is correct for current output, but the 1.5 Mt claim is a standalone projection, not a share. [confidence: high]

**INTERPRETATION ERRORS:**
- *"If the 3,000 kilotonnes arrive in 2026-27, capacity of 4,615 kilotonnes passes demand of 4,139 and the shortfall turns into a surplus, so the floor price protects a market that the ministry itself expects to flip within a year"* — The logic assumes the 3,000 kt of *expected* capacity (not confirmed under construction) will materialize exactly as stated, ignoring risks like delays, underutilization, or capacity not matching product specifications. The floor price’s justification thus rests on an unproven capacity ramp-up. [confidence: high]

**OUTDATED DATA:**
- *"Machinery imports reached $34.1 billion in April to September 2026, up 15.5%"* — The 2025 baseline ($29.5 bn) is *implied* from the 2026 figure and growth rate, not from official data. For precise trends, re-check **PPIS (Periodic Imports Statistics) by MoC&I** for Q1/Q2 2025-26 (latest fiscal year). [confidence: high]

---
*Note: Other claims (e.g., China deficit period, solar capacity ratios) are either unresolved ambiguities or secondary summaries, not outright factual/interpretation errors.*
