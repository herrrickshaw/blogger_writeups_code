# Fact/interpretation check — the-hydrogen-behind-biofuel-mandate

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-hydrogen-behind-biofuel-mandate.html`

Text-SHA1: `23c032401563559f`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- "60 Countries with biofuel blending mandates at end-2023, the latest REN21 count found" — REN21 Global Status Report (GSR); newer survey rounds for 2024 or 2025 are likely available. [confidence: medium]

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 198319, Requested 9186. Please try again in 54m2.16s. Need more tokens? Upgrade to Dev Tier today at https://c]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"1.2% synthetic jet fuel the EU requires from 2030"* — The claim conflates **ReFuelEU Aviation** (2% SAF in 2025, rising to **6% in 2030**, with **1.2% synthetic** only as a subset of that 6%) with **FuelEU Maritime** (which sets greenhouse-gas intensity targets, not a volume quota). The article’s phrasing implies a standalone 1.2% e-fuel mandate, which does not exist. [confidence: high]
- *"India’s ethanol blend reached 20% and the compressed biogas obligation is mandatory"* — While E20 was achieved in **2025–26**, the **post-E20 steps (E21, E25)** and **SAF targets** are described as "indicative," not mandatory. The article later states no green hydrogen consumption obligation for refineries has been "notified," suggesting ambiguity. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The IEA found that announced public support fell by nearly two-thirds between its 2024 and 2025 reviews, to a cumulative $38 billion"* — The $38 billion figure is **skewed toward supply-side support** (e.g., production credits), but the article later notes this **outweighs demand-side support by $1.5 to 1**, implying a causal link between reduced funding and policy misalignment. However, the IEA’s 2025 review does not explicitly attribute the drop to **demand-side gaps** (e.g., e-fuel quotas) or suggest that supply incentives alone drive hydrogen adoption. The claim risks overstating the role of funding cuts in shaping policy design. [confidence: high]
- *"The UK’s power-to-liquid obligation is 0.2% in 2028, 0.5% in 2030 and 3.5% in 2040, with one source giving 4%"* — The article treats the **3.5% vs. 4%** discrepancy as a minor variation but does not address whether the **4% figure** (from an unspecified source) reflects a **proposed revision** or an **industry advocacy target** (e.g., Hydrogen Europe). Without clarifying the source’s authority, the claim risks misrepresenting the **binding legal obligation** vs. aspirational goals. [confidence: medium]

---
**OUTDATED DATA:**
- *"60 Countries with biofuel blending mandates at end-2023, the latest REN21 count found"* — REN21’s **Global Status Report 2024** (latest) would include updates through **2024–25** (e.g., India’s E20 achievement, Brazil’s SAF decree, or new mandates like **Malaysia’s B20 in some regions**). The article’s cutoff (end-2023) may miss recent additions. [confidence: high; series to re-check: REN21 *Global Status Report on Renewables*; newer period: 2024–25]
- *"Australia: A$2/kg Australia’s legislated hydrogen production incentive, for output from 1 July 2027"* — The **Hydrogen Production Tax Incentive (HPTI)** was legislated in **2022** but has undergone **revisions** (e.g., the **Hydrogen Headstart** program’s second round outcomes expected late 2026/early 2027). The article does not note whether the **A$2/kg rate** applies uniformly across all projects or if **new tiers** (e.g., for low-emission hydrogen) have been introduced. [confidence: medium; series to re-check: Australian Government *Hydrogen Production Tax Incentive*; newer period: 2026–27 guidance]
