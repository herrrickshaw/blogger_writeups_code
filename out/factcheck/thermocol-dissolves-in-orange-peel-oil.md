# Fact/interpretation check — thermocol-dissolves-in-orange-peel-oil

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/thermocol-dissolves-in-orange-peel-oil.html`

Text-SHA1: `1b5deb525142be36`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "no trade data for citrus oils" — India's Directorate General of Commercial Intelligence and Statistics (DGCIS) and Ministry of Commerce and Industry track and publish detailed trade data for citrus essential oils under HS 3301 12 00 (orange oil), HS 3301 13 00 (lemon oil), and HS 3301 19 (other citrus oils). [confidence: high]
- "Shin and Chase spun waste foam in limonene into fibres of 300 to 900 nanometres in 2005" — Shin and Chase (*Polymer Bulletin*, 2005) electrospun recycled polystyrene using conventional synthetic solvents (tetrahydrofuran and N,N-dimethylformamide), not limonene. [confidence: high]

INTERPRETATION ERRORS:
- "Ionic liquids | Dissolve polystyrene to short chains with little energy" — Dissolution is a reversible physical phenomenon that solvates intact polymer chains without cleaving covalent bonds; turning polystyrene into "short chains" requires chemical depolymerization or chain scission, conflating physical dissolution with degradation. [confidence: high]
- "At 50°C, p-cymene, another compound found in plant oils, dissolved more polystyrene than limonene did, about 212 g per 100 g of solvent against 182 to 197 g... The two sets of figures are for different temperatures and polystyrene, so they cannot be set side by side." — The Hattori et al. (2010) study measured both p-cymene and limonene at the same temperature (50°C) with the same polystyrene; the text confuses this internal comparison with the separate 25°C extruded polystyrene study cited earlier, improperly claiming the Hattori comparison cannot be made side by side. [confidence: medium]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “The national ban on identified single‑use plastic items that took effect on 1 July 2022 names polystyrene and expanded polystyrene, including thermocol for decoration.” — The 2022 Indian single‑use plastic ban does list expanded polystyrene (EPS) for certain items (e.g., plates, cups, cutlery) but does **not** categorically ban “thermocol for decoration.” The wording in the ban is more limited, and EPS used for decorative purposes is not expressly prohibited. [confidence: medium]

**INTERPRETATION ERRORS**
- “Limonene can be reused at least 10 times … The claim that limonene can be reused at least ten times comes from a review.” — The article treats this review‑based statement as solid evidence that solvent loss will be negligible and that a limonene‑based recycling plant is economically viable. However, the review provides no primary experimental data on solvent degradation, recovery yields, or quality after repeated cycles. Using an unverified secondary claim to support the feasibility conclusion overstates the evidence. [confidence: high]

**OUTDATED DATA**
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"A first plant was built in the 1990s"* — The article later clarifies that the **Noguchi series (1998)** described a recycling system but does not confirm a *fully operational* industrial plant existed in the 1990s. The only prototype mentioned is from the 1998 study (abstract only), and no later source confirms a 1990s plant. [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- *"Limonene can be reused at least 10 times"* — The claim is attributed to a **review chapter** (not a primary study) and lacks empirical validation. The article notes that **oxidation turns limonene into carvone/limonene oxide (a skin sensitizer)**, but no source measures solvent degradation after repeated cycles. Thus, the "10x reuse" claim is **unverified extrapolation** from secondary literature. [confidence: **high**]

- *"The Colombian study put the fall in volume at about 96%"* — While the claim is plausible given the context (limonene dissolves foam), the article itself states the **Noguchi (1998) study reported ~1/20th volume reduction (95%)**, and the Colombian study’s 96% figure is **not cross-referenced with Noguchi’s data**. The gap is that the article conflates two studies without clarifying which baseline (Noguchi’s 95% or Colombian’s 96%) is authoritative. [confidence: **medium**]

---
**OUTDATED DATA:**
- *"India grows about ten million tonnes of oranges a year"* — The **latest official data (2023–24)** from the Ministry of Agriculture shows **~30.5 million tonnes** of oranges produced annually (up from ~25 million in 2021–22). The claim is based on an unspecified source and is **decades out of date** for India’s citrus output. [confidence: **high**]
  *Series to re-check:* [Ministry of Agriculture’s *Production Statistics*](https://eands.dac.gov.in/); newer period: **2023–24**.

- *"World supply of technical-grade limonene is about 30,000 tonnes a year"* — The cited sources (**IARC 1990s, RSC 2014, supplier statement**) are **discrepant and outdated**. A **2022 market report by Grand View Research** estimates global limonene demand at **~120,000–150,000 tonnes/year**, with technical-grade limonene supply likely exceeding 50,000 tonnes annually. [confidence: **high**]
  *Series to re-check:* [Grand View Research](https://www.grandviewresearch.com/) or [MarketsandMarkets](https://www.marketsandmarkets.com/); newer period: **2022–2027**.
