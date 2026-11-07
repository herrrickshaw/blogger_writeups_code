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
- "The pipelines PNGRB has awarded by competitive bidding since 2008 carried 15 MMSCMD in August 2026 against 315 MMSCMD of capacity, about 5%." — Comparing the actual gas carried (flow rate) directly against nameplate design capacity to claim a 5% utilization rate conflates volume with capacity, assuming that low throughput implies idle physical capacity rather than contractual allocation patterns, line-pack dynamics, or upstream supply availability. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 10490, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"Four authorised lines have laid no pipe at all"** — The claim conflates *authorised* lines with *bid-out* lines. While **four lines (Kakinada–Vijayawada–Nellore, Kanai Chhata–Panitar, Ennore–Nellore, and Kochi–Kanyakumari–Thoothukudi)** show **no pipe lowered**, the article earlier states that **Ennore–Nellore was "reported cancelled in 2019"** (implying it may no longer be active). Additionally, **Kochi–Kanyakumari–Thoothukudi was authorised in March 2026** (not a long-standing project), so calling it part of a broader trend of "stalled" lines is misleading without context. [confidence: high]

- **"PNGRB bid out the pipelines ran at 5% of capacity"** — The **5% utilisation figure (15 MMSCMD vs. 315 MMSCMD capacity)** applies only to **pipelines awarded via PNGRB’s competitive bidding (regulation 5) since 2008**, not all "bid-out" pipelines. Older GAIL lines (pre-PNGRB) and dedicated lines (e.g., GSPL’s Gujarat grid) run at **50–89% capacity**, showing the comparison is **apples-to-oranges**. [confidence: high]

---
**INTERPRETATION ERRORS:**
- **"India’s natural gas grid is mostly built, slowly being finished, and barely being added to"** — While the **28,157 km operating out of 34,978 km authorised (June 2026)** suggests completion is near, this ignores:
  1. **Capacity utilisation**: Only **32% of common-carrier pipeline capacity is used**, with **bid-out lines at 5%**, implying **demand-side constraints** (e.g., lack of end-user connections or contracts), not just supply gaps.
  2. **Geographic skew**: The **North-East grid (1,471 km under construction)** and **city gas networks (81% of pro-rata targets met but only 38% of homes connected)** show **active expansion in underserved regions**, contradicting the "barely being added to" claim. [confidence: high]

- **"The pipelines PNGRB bid out ran at 5% of capacity"** — The **5% figure (15/315 MMSCMD)** is **correct for regulation 5 pipelines**, but the article **fails to distinguish this from**:
  - **Pre-PNGRB GAIL lines (50% utilisation)**, which dominate capacity.
  - **Dedicated lines (e.g., GSPL Gujarat grid at 75%)**, which are excluded from the 5% claim.
  The **causal leap**—that "bid-out pipelines" are inherently underutilised due to PNGRB’s policies—**ignores that demand may not exist yet** (e.g., new LNG terminals like Kochi lack connected markets). [confidence: high]

---
**OUTDATED DATA:**
- **"27,427 km operating of 34,273 km authorised (December 2025, PPAC Ready Reckoner)"** — The article **compares this to PNGRB’s June 2026 figure (28,157 km)**, but the **PPAC data is from May 2026** (as per the source citation). A **newer PPAC update (e.g., June/July 2026)** likely exists and could show revised totals. [confidence: high]

- **"Target dates as printed"** — Multiple lines (e.g., **Dabhol–Bangalore, authorised Feb 2013 but still 0% pipe lowered**) have **no updated target dates** in the PNGRB August 2026 report. The article notes this as a **systemic issue** but does not check if PNGRB has **published revised timelines** in later 2026 reports. [confidence: medium]
