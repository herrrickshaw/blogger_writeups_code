# Fact/interpretation check — india-has-27400-km-of-gas-pipeline

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-has-27400-km-of-gas-pipeline.html`

Text-SHA1: `33bad6212e433f88`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "almost all of that length belongs to lines authorised between 2011 and 2020, and 4 of them, with 1,629 km between them, have not lowered a single kilometre of pipe." — The four unstarted lines totaling 1,629 km comprise Kakinada–Vijayawada–Nellore (667 km), Kanai Chhata–Panitar (317 km), Ennore–Nellore (220 km), and Kochi–Kanyakumari–Thoothukudi (425 km). As stated elsewhere in the article, Kochi–Kanyakumari–Thoothukudi was authorised in March 2026, not between 2011 and 2020. Only three of those lines (totalling 1,204 km) belong to the 2011–2020 period. [confidence: high]

INTERPRETATION ERRORS:
- "The pipelines PNGRB has awarded by competitive bidding since 2008 carried 15 MMSCMD in August 2026 against 315 MMSCMD of capacity, about 5%... The newest lines were built to reach markets that do not yet take much gas, which is the same pattern this blog found in LNG terminals." — The 315 MMSCMD denominator represents the total authorized design capacity of the completed pipeline systems, but several major lines in this category are only partially built and operating in isolated sections (e.g., Mallavaram–Bhopal–Bhilwara–Vijaipur has only 365 km operating out of 1,881 km authorized). Comparing current throughput on partial segments against the full authorized design capacity of the unfinished networks is an apples-to-oranges metric; attributing the resulting 5% capacity utilization to missing market demand ignores that the physical pipelines required to transport gas to those demand centres have not yet been completed. [confidence: high]
- "Four authorised lines show no pipe lowered at all: Kakinada–Vijayawada–Nellore (authorised 2018), Kanai Chhata–Panitar (2019), Ennore–Nellore (2014; its authorisation was reported cancelled in 2019, yet it is still listed), and the newly authorised Kochi–Kanyakumari–Thoothukudi (March 2026, due March 2029)." — Kochi–Kanyakumari–Thoothukudi was authorised in March 2026 with a scheduled target date of March 2029. Conflating a newly authorised project that is only a few months into a three-year project lifecycle with legacy projects stalled for 7 to 12 years creates a false equivalence to support the claim of regulatory or execution inertia. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 11160, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Four authorised lines have laid no pipe at all"* — The claim conflates **four lines with no pipe lowered** (Kakinada–Vijayawada–Nellore, Kanai Chhata–Panitar, Ennore–Nellore, and Kochi–Kanyakumari–Thoothukudi) with the broader statement that "no pipe has been laid" on these lines. While the data shows **no pipe lowered** on these four, the article later clarifies that *Ennore–Nellore* was **reportedly cancelled in 2019** but still appears in PNGRB’s August 2026 report. The phrasing risks implying all four are still active with zero progress, which is misleading for Ennore–Nellore. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The pipelines PNGRB has awarded by competitive bidding since 2008 carried 15 MMSCMD in August 2026 against 315 MMSCMD of capacity, about 5%"* — This **false causal claim** conflates **low utilization (5%)** with **bid-out pipeline failures**. The 5% figure could stem from:
  1. **Lack of demand** (e.g., new markets not yet connected),
  2. **Contractual delays** (e.g., buyers not yet operational),
  3. **Capacity underutilization** (e.g., overbuilt pipelines), or
  4. **Data reporting gaps** (e.g., PNGRB not distinguishing contracted vs. actual usage).
  The article later notes that **GAIL’s older lines (pre-PNGRB) run at 50–89% capacity**, implying the 5% figure may reflect **structural issues in bid-out pipelines** (e.g., poor contract enforcement) rather than a systemic problem with competitive bidding alone. [confidence: high]

---
**OUTDATED DATA:**
- *"PNGRB’s own monthly pipeline report for August 2026 puts 28,157 km in operation out of 34,978 km authorised, as of June 2026"* — While the **August 2026 report** is cited as the source, the article itself was **updated on 9 November 2026** with newer Gazette notices (e.g., S.O. 5949(E) for Siliguri–Gangtok, dated 30 October 2026). For **real-time pipeline lengths**, readers should cross-check with:
  - **PNGRB’s latest MIS report** (likely September/October 2026 updates),
  - **PPAC’s latest Ready Reckoner** (e.g., December 2026 data if released),
  - **Company-specific filings** (e.g., GAIL’s quarterly updates).
  The **June 2026 baseline** may now be outdated by ~5 months. [confidence: high]

---
**none found** (for other categories).
