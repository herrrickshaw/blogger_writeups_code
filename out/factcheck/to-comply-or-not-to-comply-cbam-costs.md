# Fact/interpretation check — to-comply-or-not-to-comply-cbam-costs

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/to-comply-or-not-to-comply-cbam-costs.html`

Text-SHA1: `fcf86b671fc91d3c`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 11805, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"India’s exports of CBAM-covered goods to the EU at USD 6.32 billion in 2024"** — The article cites a **RIS policy brief** (likely from the commerce ministry’s think tank) for this figure, but the **GTRI data** (also referenced) shows **USD 5.82 billion** in steel/aluminium exports to the EU in **2024-25** (FY25), which overlaps with 2024. The **UN Comtrade/GTRI discrepancy** suggests either:
  - A **misalignment in fiscal years** (GTRI’s FY25 includes April 2024–March 2025, while RIS may use calendar 2024).
  - **Double-counting** of certain products (e.g., ferro-alloys split between CBAM-covered and safeguard-covered exports).
  *Confidence: high* (data sources conflict on scope and period).

- **"India’s share of EU finished-steel imports, January–June 2026 (EUROFER): 7.7%"** — While **EUROFER’s Q3 2026 report** (via GMK Center/IndexBox) states **7.7%**, the **BigMint data** (also cited) shows **India shipped 1.01 Mt in H1 2026**, which is **~8% of EU’s 12.5 Mt total imports** (EUROFER’s 2025 figure was 29.7 Mt, but 2026 data isn’t yet published). The **7.7% claim assumes a 2025 baseline**, but **EU imports fell 5% YoY in H1 2026** (EUROFER), making the share likely **higher than 7.7%** if total imports shrank. The article conflates **volume share (8%)** with **value share (7.7%)** without clarifying.
  *Confidence: medium* (EUROFER’s 2026 data isn’t fully released; BigMint’s tonnage suggests a higher share).

---

**INTERPRETATION ERRORS:**
- **"India’s own carbon credits (€6–13/t) would deduct little if they were recognised"** — The claim **misrepresents the deduction mechanism**: The **EU’s draft rules (May 2026)** require that **only the carbon price "effectively paid" in India** (after accounting for **free allocations, rebates, and exemptions** under CCTS) can offset CBAM. Since:
  - **CCTS credits are zero-sum** (plants that meet targets pay nothing; those that miss pay only on shortfalls).
  - **No Indian credit has traded**, and **CERC hasn’t set a floor/ceiling**.
  - **EU recognition is non-existent** (draft rules cap deductions at 10% of emissions via Article 6 credits, which India lacks).
  The **€6–13 estimate is irrelevant** because:
  1. **No plant pays €6–13/t under CCTS** (e.g., a mill at 2.5 tCO₂/t missing a 5% target pays ~€1.71/t, per the article’s own calculation).
  2. **Even if recognised, the deduction would apply only to the shortfall**, not the full emissions bill.
  *Gap*: The article **treats CCTS as a standalone carbon price** rather than a **conditional, non-linear offset** tied to compliance.
  *Confidence: high*.

- **"CBAM will cost India’s exports their EU market"** — The article **overstates the economic impact** by:
  - **Ignoring EU producers’ exposure**: EU mills face the **same carbon price** as free allocation falls (e.g., **€27/t average bill in 2026** per EUROFER), so **EU steel prices will rise too**. Sandbag’s estimate that **80% of CBAM costs pass into EU prices** (reducing India’s net loss to **€79M in 2034**) is **not engaged with**.
  - **Double-counting quota effects**: The **steel safeguard quota (18.3 Mt)** and **50% duty above quota** are **additional to CBAM**, but the article **treats them as separate** without quantifying the **combined impact** on Indian exporters’ margins.
  *Gap*: The **asymmetry in protection** (EU mills + quotas + anti-dumping) is **not weighed against India’s adaptive capacity** (e.g., shifting exports to Vietnam/UK/UAE, as BigMint data shows).
  *Confidence: high*.

---
**OUTDATED DATA:**
- **"EU crude steel output fell 2.9% in 2025 to 125.8 Mt"** — This is **correct for 2025**, but the article’s **context (October 2026)** should reference the **latest EUROFER Q4 2026 update** (not yet cited). As of **October 2026**, EUROFER’s **Q3 2026 report** (1 October) likely includes **2026 H1 data** (e.g., **May 2026 output at 67% capacity utilization**). The **2025 figure is stale** for a discussion of **2026 dynamics**.
  *Series to re-check*: **EUROFER’s *European Steel in Figures 2026*** (annual) + **Q4 2026 Economic and Steel Market Outlook**; **newer period**: **2026 H1/H2 data**.
  *Confidence: high*.

- **"India’s default CBAM values (e.g., 4.28 tCO₂/t for hot-rolled steel)"** — These are **correct as of Implementing Regulation (EU) 2025/2621**, but the article **does not note that the EU’s default values are subject to annual review**. For **2027**, the **20% mark-up** will apply, and **2028+ sees 30%**. The **latest correction (2026/1740)** may have **fine-tuned values** for specific Indian products (e.g., DRI vs. blast-furnace steel). The article **should flag that these are 2026 baselines** and urge re-checking for **2027+**.
  *Series to re-check*: **EU Commission’s *CBAM Implementing Regulations*** (annual updates); **newer period**: **2027 draft values**.
  *Confidence: high*.
