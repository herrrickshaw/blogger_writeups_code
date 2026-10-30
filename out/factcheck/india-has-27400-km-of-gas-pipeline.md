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
- "The pipelines PNGRB has awarded by competitive bidding since 2008 carried 15 MMSCMD in August 2026 against 315 MMSCMD of capacity, about 5%. The older GAIL lines authorised before the regulator existed ran at 50%, and GSPL’s Gujarat grid at 75%... The newest lines were built to reach markets that do not yet take much gas, which is the same pattern this blog found in LNG terminals." — Comparing aggregate physical throughput against aggregate design capacity across heterogeneous pipeline networks grouped by their regulatory vintage assumes that design capacity utilization is solely a function of market demand, while ignoring structural factors such as upstream gas availability, domestic production shortfalls, imported LNG terminal constraints, and the lack of intermediate interconnectors that prevent newly built common-carrier spurs from drawing gas from mature supply basins. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 10263, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"Four authorised lines have laid no pipe at all"** — The claim conflates *authorised* lines with *active* lines. While four lines (Kakinada–Vijayawada–Nellore, Kanai Chhata–Panitar, Ennore–Nellore, and Kochi–Kanyakumari–Thoothukudi) show **no pipe lowered**, the article later clarifies that **Ennore–Nellore was reported cancelled in 2019** but remains listed as authorised. The phrasing risks implying all four are still active projects, which is misleading. [confidence: high]

**INTERPRETATION ERRORS:**
- **"The pipelines PNGRB bid out ran at 5% of capacity"** — This claim conflates **utilisation rate** (5% for bid-out lines) with **capacity underutilisation** across the entire network (32%). The 5% figure applies only to the subset of pipelines awarded via competitive bidding (7 lines, 5,406 km), while the broader 32% figure includes older GAIL lines and dedicated networks. The article does not establish whether the 5% reflects missing demand, contractual gaps, or operational issues—key distinctions not drawn. [confidence: high]

**OUTDATED DATA:**
- **"27,427 of 34,273 km authorised, December 2025"** — The article cites this as a *comparison figure* but does not note that PNGRB’s **August 2026 report** (the "latest" source) already supersedes it with **28,157/34,978 km** (June 2026). The PPAC "Ready Reckoner" (May 2026) is also outdated relative to PNGRB’s August 2026 data. [confidence: high]
