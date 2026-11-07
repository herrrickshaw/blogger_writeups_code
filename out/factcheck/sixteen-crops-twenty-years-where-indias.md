# Fact/interpretation check — sixteen-crops-twenty-years-where-indias

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/sixteen-crops-twenty-years-where-indias.html`

Text-SHA1: `6ca35b2bf41fc518`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The crops with the most room to grow output without more land are those with the widest gaps between their best and worst states: jowar, maize, moong, urad and bajra." — A wide yield gap between states does not logically imply that there is "room to grow output without more land" (i.e., that laggard states can easily catch up to frontier states). High yield variance across states often reflects structural, agro-climatic, soil, or water availability constraints (such as rainfed versus irrigated conditions) rather than simple inefficiencies that can be closed to boost national output. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 10363, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"0.0% Annual soybean yield growth over twenty years; every tonne of extra output came from more land"** — This claim is **incorrect** based on the later data in the article. The soybean yield in 2023-26 is stated as **~1,060 kg/ha**, identical to the 2003-06 baseline, but the article itself later confirms that **area expanded from 73 to 129 lakh hectares** while yield remained flat. However, the **2025-26 production peak (15.3 million tonnes) contradicts the 2023-26 average (13.6 million tonnes)**, suggesting yield may have risen temporarily. The **2023-26 average yield (1,060 kg/ha) is likely an underestimate**—UPAG’s 2025-26 third advance estimate (used for 2023-26 averages) may not reflect recent yield gains. [confidence: **high**]

- **"11% Share of India’s tur grown in one district, Kalaburagi in Karnataka"** — This is **misleading**. While Kalaburagi’s share is **11% of national tur output**, the article later clarifies that **Kalaburagi alone accounts for 11% of India’s tur**, but **Vijayapura (7%) and Bidar (4%)** also contribute significantly. The phrasing implies **monopoly-like concentration**, which is exaggerated. [confidence: **medium**]

---

**INTERPRETATION ERRORS:**
- **"The crops with the most room to grow output without more land are those with the widest gaps between their best and worst states: jowar, maize, moong, urad and bajra."**
  - **Gap in reasoning:** The claim conflates **yield potential** (state-level gaps) with **scalability**. While jowar, maize, and moong show **high yield disparities**, their growth is also driven by **expanding area** (e.g., maize’s 50% area contribution). The "room to grow" argument ignores that **land constraints** (e.g., jowar’s shrinking area) or **yield stagnation** (e.g., bajra’s flat yields) limit output increases. The causal link is **circular**: wide gaps *exist* because some states already exploit high-yield niches, but this doesn’t prove those crops can grow without land expansion. [confidence: **high**]

- **"The crops that matter most for price stability... are also the steadiest harvests, while the rain-fed oilseeds and pulses swing by a fifth or more in a typical year."**
  - **Gap in reasoning:** The article **correlates harvest volatility with irrigation status** but **ignores other drivers**. For example:
    - **Groundnut (22% swing)** is rain-fed but has **high yield potential** (Gujarat’s 2,706 kg/ha vs. national 2,155 kg/ha), suggesting **management variability** (e.g., water access, pests) plays a role beyond irrigation alone.
    - **Sugarcane (8% swing)**, primarily irrigated, still faces **climate shocks** (e.g., 2003-04 drought), proving even irrigated crops aren’t immune to volatility.
    The claim **overgeneralizes** by treating irrigation as the sole determinant of stability. [confidence: **high**]

---

**OUTDATED DATA:**
- **"Output averaged 147 million tonnes in 2023-26, up from 88 million in 2003-06"** — The **2025-26 third advance estimate (154 million tonnes)** is newer and likely supersedes the 2023-26 average. Re-check: **UPAG’s *all-India production data* (2025-26 third advance estimates)**. [confidence: **high**]

- **"Yield rose from 2,055 to 2,909 kg a hectare [for rice]"** — This is based on **2003-06 vs. 2023-26 averages**, but the **2025-26 record yield (3,000+ kg/ha in Punjab)** may not be reflected. Re-check: **UPAG’s *state-wise yield data* (2025-26 third advance estimates)**. [confidence: **medium**]

- **"Cotton production is in bales of 170 kg of lint; UPAG’s download labels it lakh tonnes"** — The **2025-26 production figure (29.0 million bales)** is newer than the 2023-26 average (30.4 million bales). Re-check: **UPAG’s *cotton production data* (2025-26 third advance estimates)**. [confidence: **high**]

---
**Note:** The article’s **methodology section** confirms reliance on **third advance estimates for 2025-26**, which may not yet be finalized. All claims referencing 2023-26 averages could be **outdated** if newer data contradicts them.
