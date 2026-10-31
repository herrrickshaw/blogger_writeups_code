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
- "The pipelines PNGRB has awarded by competitive bidding since 2008 carried 15 MMSCMD in August 2026 against 315 MMSCMD of capacity, about 5%. The older GAIL lines authorised before the regulator existed ran at 50%, and GSPL’s Gujarat grid at 75%." — Comparing nameplate design capacity directly with actual throughput (utilization percentage) across differently structured grids does not inherently prove a "reasoning gap" in economic reporting, but attributing the low utilization solely to "markets that do not yet take much gas" conflates network topology, tariff structures, and upstream supply constraints with pure demand-side failure without accounting for contractual bottlenecks or lack of interconnectivity. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 9326, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"Four authorised lines have laid no pipe at all"** — The claim conflates *authorised* lines with *active construction status*. While **Kakinada–Vijayawada–Nellore (2018), Kanai Chhata–Panitar (2019), Ennore–Nellore (2014, reportedly cancelled in 2019), and Kochi–Kanyakumari–Thoothukudi (2026)** show **zero pipe lowered**, the article later clarifies that **Ennore–Nellore’s authorisation was cancelled in 2019** (so it shouldn’t be counted as "authorised" in the same sense). The phrasing risks implying all four are still validly authorised with no progress, which is misleading for **Ennore–Nellore**.
  [confidence: **high**]

- **"PNGRB bid out the pipelines ran at 5% of capacity"** — The **5% figure (15 MMSCMD/315 MMSCMD capacity)** applies only to **pipelines awarded via PNGRB’s competitive bidding (regulation 5) since 2008**, not all "bid-out" pipelines. The article later notes that **older GAIL lines (regulation 17) run at 50%**, and **GSPL’s Gujarat grid at 75%**, creating an **apples-to-oranges comparison**. The claim misrepresents the subset being analyzed.
  [confidence: **high**]

---
**INTERPRETATION ERRORS:**
- **"India’s natural gas grid is mostly built, slowly being finished, and barely being added to"** — While **28,157 km of 34,978 km authorised are operational (81%)**, this ignores:
  1. **Capacity utilization**: Only **32% of total common-carrier capacity is used**, with **bid-out pipelines at 5%**—suggesting **demand constraints**, not just "barely being added to."
  2. **Geographic skew**: The **North-East grid (1,471 km under construction)** and **city gas networks (81% of pro-rata targets met)** show **active expansion**, contradicting the "barely being added to" claim.
  3. **Authorised-but-stalled lines**: **4 lines (1,629 km) have no pipe laid**, but the article later admits **Ennore–Nellore was cancelled in 2019**, leaving **3 valid but stalled projects**—a gap in reasoning about "addition."
  [confidence: **high**]

- **"The pipelines PNGRB bid out ran at 5% of capacity"** — The **5% figure (15/315 MMSCMD)** is **correct for regulation 5 pipelines**, but the article **fails to distinguish this from**:
  - **Regulation 17 pipelines (GAIL’s older lines)**: **50% utilization** (192/388 MMSCMD).
  - **Regulation 18 pipelines (pre-PNGRB, e.g., GSPL)**: **75% utilization** (40/53 MMSCMD).
  The claim **generalizes bid-out pipelines** without clarifying the regulatory subset, leading to **false causality** (e.g., implying all PNGRB bids perform poorly).
  [confidence: **high**]

---
**OUTDATED DATA:**
- **"27,427 km operating of 34,273 km authorised (December 2025)"** — The article **compares this to PNGRB’s June 2026 figure (28,157/34,978 km)**, but **PPAC’s December 2025 data is superseded by PNGRB’s August 2026 report** (the article’s primary source). The **730 km increase** in operating length between Dec 2025 and Jun 2026 suggests **PPAC’s figure is outdated** and should be cross-checked against PNGRB’s **latest monthly report** (August 2026).
  [confidence: **high**]

- **"Right-of-user notices in the table below were checked against the Gazette of India’s own text... Two S.O. numbers were wrong and are corrected"** — While the **corrections (e.g., S.O. 3577(E) instead of 3574(E) for Silchar–Panisagar)** are noted, the article **does not flag that three S.O. numbers (5085(E), 2993(E), 3755(E)) could not be found in the SansadSaar index**, implying they may be **erroneous or missing from the Gazette**. Readers should **verify these against the latest Gazette archives** (e.g., [eGazette](https://egazette.gov.in/)).
  [confidence: **medium**]

---
**Note**: The article’s **data sources (PNGRB August 2026 reports)** are current as of publication (23 Oct 2026), so no broader "outdated data" issues apply beyond the specific PPAC comparison.
