# Fact/interpretation check — india-has-27400-km-of-gas-pipeline

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-has-27400-km-of-gas-pipeline.html`

Text-SHA1: `efd6d88aa98b43b8`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 8359, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Four authorised lines have laid no pipe at all"* — The claim conflates **four lines with no pipe lowered** (Kakinada–Vijayawada–Nellore, Kanai Chhata–Panitar, Ennore–Nellore, and Kochi–Kanyakumari–Thoothukudi) with the broader assertion that *no pipe has been laid* on these lines. While the data confirms **no pipe has been lowered** on these four, the Ennore–Nellore line was *authorised in 2014 but reportedly cancelled in 2019*—meaning its authorisation may no longer be active. [confidence: high]

- *"PNGRB bid out the pipelines ran at 5% of capacity"* — The claim misattributes the **5% utilisation** to *all* bid-out pipelines, but the data shows this figure applies only to **7 bid-out lines (5,406 km total)**, while older GAIL lines (pre-PNGRB) ran at **50% capacity**. The article later clarifies this distinction but the initial phrasing risks implying all bid-out pipelines are underutilised. [confidence: high]

---
**INTERPRETATION ERRORS:**
- *"India’s natural gas grid is mostly built, slowly being finished, and barely being added to"* — This conclusion **overgeneralises** from two data points:
  1) **28,157 km of 34,978 km authorised are operational** (80% completion), but this includes **dedicated lines** (not just common-carrier) and excludes future demand (e.g., LNG terminals, city gas expansion).
  2) **7,033 km of common-carrier lines remain unbuilt**, but the article later notes **city gas distribution (3.3 lakh km) is the *actual* focus of current pipe-laying**, not trunk lines. The claim conflates **trunk pipeline stagnation** with **overall grid growth** (which is driven by CNG networks). [confidence: high]

- *"The pipelines PNGRB bid out ran at 5% of capacity"* — While true for the **7 bid-out lines (5,406 km)**, the article **fails to distinguish** this from:
  - **Older GAIL lines (pre-PNGRB, 17,970 km)**: 50% utilisation.
  - **Newer lines (e.g., Mehsana–Bhatinda)**: 7% utilisation.
  The **5% figure alone** does not prove systemic failure—it may reflect **market timing** (e.g., Kochi–Kanyakumari connects to underused LNG capacity) or **contractual delays**, not inherent inefficiency. [confidence: high]

---
**OUTDATED DATA:**
- *"27,427 of 34,273 km operating (December 2025)"* — This figure is **superseded** by PNGRB’s **June 2026 report** (28,157 km operating of 34,978 km authorised). The article acknowledges this revision in the update box but **repeats the older PPAC figure (May 2026) in the main text** without clear flagging. [confidence: high]
  - **Series to re-check**: PPAC *Monthly Ready Reckoner* (Table 20); **newer period**: PNGRB MIS Report (August 2026).

- *"Ennore–Nellore (authorised 2014; *reported cancelled in 2019*)"* — The article notes the **2019 cancellation** but **still lists it as "authorised"** in the "lines with no pipe laid" section. This creates ambiguity about its current status. [confidence: medium]
  - **Series to re-check**: PNGRB’s **August 2026 authorisation database**; **newer period**: post-2019 cancellations.
