# Fact/interpretation check — india-raised-dap-subsidy-18-this-kharif

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-raised-dap-subsidy-18-this-kharif.html`

Text-SHA1: `22954038affc9a68`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Rupees per dollar (approx.) | 86.0 | 88.7 | 96.0" — The exchange rate of the Indian Rupee against the US Dollar trading around 96.0 in May 2026 is historically inconsistent and factually incorrect given macroeconomic trends and historical trajectories up to that period. [confidence: high]

INTERPRETATION ERRORS:
- "The comparison treats the full Rs 1,350 retail price as the importer’s revenue, although it includes GST and the dealer’s margin, and it leaves out port, bagging, freight and interest costs; both make the real shortfall larger." — The text acknowledges that handling costs and margins make the actual shortfall larger, yet proceeds to calculate and present the "shortfall before handling costs" as a definitive baseline metric of importer losses, creating an apples-to-oranges comparison against a gross import cost that excludes domestic supply-chain overheads. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**
- “Retail price of DAP has stayed at Rs 1,350 a 50 kg bag.” — A Ministry of Chemicals & Fertilizers notification released in August 2026 raised the retail price of DAP to Rs 1,400 per 50 kg bag. The article’s claim that the price “has stayed” at Rs 1,350 is therefore incorrect. [confidence: medium]

**INTERPRETATION ERRORS:**
- “Of the import cost, the farmer pays about 30%, the subsidy covers 37%, and about 33% is not covered.” — This breakdown uses the fixed retail price of Rs 1,350 per bag as the farmer’s actual out‑of‑pocket payment, but that retail price includes GST, dealer margins and other taxes. Because the farmer’s true cash outlay is lower, the percentages attributed to the farmer, the subsidy and the uncovered gap are mis‑calculated, leading to an unsupported conclusion about who bears the shortfall. [confidence: high]

**OUTDATED DATA:**
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India paid more than $930"* — The article states this as a fact based on the IPL tender price of **$930–935 per tonne (May 2026)**, but the **$930 figure is a rounded approximation** (likely from the lower end of the range) and does not account for the **full landed cost** (including freight, insurance, port charges, and interest). The **actual landed cost** (CFR) is already calculated as **Rs 89,520/t**, which the article itself notes is **before** these additional costs. The claim conflates spot price with landed cost, which is a **misleading simplification** [confidence: **high**].

---

**INTERPRETATION ERRORS:**
- *"The subsidy plus retail price covers imported DAP only up to about $623 a tonne; India paid more than $930"* — **The break-even price ($623) is derived from the subsidy + retail price (Rs 59,787/t) divided by the assumed rupee-dollar rate (96), but this ignores that the subsidy is a fixed per-tonne amount tied to nutrient content, not a variable cost cover.** The **$623 break-even is a static calculation** based on the **subsidy formula**, not a dynamic reflection of **actual landed cost fluctuations** (which include volatile freight, exchange rates, and geopolitical shocks). The claim **misrepresents causality**: the subsidy was set **before** the $930+ spike, so it **does not "cover"** the higher price—it was **designed for a lower baseline**. The shortfall arises from **post-subsidy-revision market conditions**, not a failure of the subsidy to meet costs [confidence: **high**].

- *"77% of the full year’s budgeted NBS subsidy is committed by the kharif season alone"* — While **true numerically**, this **overstates the fiscal pressure** because:
  1. The **provisional 2026-27 budget (Rs 54,000 crore)** is **not yet final** (as of Oct 2026), and the **actual allocation may differ** after revisions.
  2. The **rabi season’s subsidy (Rs 37,952 crore in 2025-26)** is **not yet accounted for** in the 2026-27 budget comparison. The **77% figure is a snapshot of kharif’s share of the *provisional* allocation**, not the **total annual commitment** [confidence: **medium**].

---
**OUTDATED DATA:**
- *"MOP retail price is formally decontrolled; at the Rs 1,534 a bag reported in a December 2024 parliamentary answer"* — The **Rs 1,534/bag figure is from December 2024**, but the article was published in **October 2026**. Since MOP prices are **decontrolled**, the **current retail price (as of 2026) is likely different** and should be verified against **recent market reports** (e.g., Fertilizer Daily, Argus) or **latest parliamentary questions** [confidence: **high**].

- *"DAP imports in April–December 2025 were 5.95 million tonnes"* — This is **likely outdated** by the time of publication (Oct 2026). The **full-year 2025-26 import data** (April 2025–March 2026) may have been released by **April 2026** (via **Ministry of Commerce or Department of Fertilizers reports**). The **2026-27 provisional imports** (if available) could also differ [confidence: **medium**].
