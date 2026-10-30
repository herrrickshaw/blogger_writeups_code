# Fact/interpretation check — india-has-27400-km-of-gas-pipeline

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-has-27400-km-of-gas-pipeline.html`

Text-SHA1: `aaa891a765f00065`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The pipelines PNGRB has awarded by competitive bidding since 2008 carried 15 MMSCMD in August 2026 against 315 MMSCMD of capacity, about 5%. ... The newest lines were built to reach markets that do not yet take much gas, which is the same pattern this blog found in LNG terminals." — Comparing aggregate physical throughput (gas carried) directly against maximum design capacity (or nameplate capacity) to claim "capacity used" assumes that all pipelines operate continuously at uniform baseline loads and ignores dynamic operational constraints, line-pack requirements, and upstream/downstream supply-demand synchronization. A low throughput-to-capacity ratio does not necessarily mean the infrastructure is entirely redundant or unused in economic terms, as high-pressure trunk pipelines often require surplus capacity to manage peak load swings and pressure stability. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 11032, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Four authorised lines have laid no pipe at all"* — The claim conflates *authorised* lines with *no pipe lowered*. The article later clarifies that **four lines (Kakinada–Vijayawada–Nellore, Kanai Chhata–Panitar, Ennore–Nellore, Kochi–Kanyakumari–Thoothukudi) have *zero pipe lowered* (as of August 2026), but **Ennore–Nellore was reportedly cancelled in 2019**—so it may not be "authorised" in the operational sense. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The pipelines PNGRB bid out ran at 5% of capacity"* — This **false causal claim** conflates *bid-out* pipelines (7 lines, 5% utilization) with *all common-carrier lines* (32% utilization). The 5% figure is misleading because it ignores older GAIL lines (50% utilization) and ignores that **capacity utilization ≠ demand**—many new lines may lack connected markets or contracts. [confidence: high]

**OUTDATED DATA:**
- *"27,427 of 34,273 km authorised, December 2025"* — The article later corrects this to **28,157 of 34,978 km (June 2026)** from PNGRB’s August 2026 report. The December 2025 figure (PPAC) is outdated and should be replaced with the newer PNGRB data. [confidence: high]
