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
- "The crops with the most room to grow output without more land are those with the widest gaps between their best and worst states: jowar, maize, moong, urad and bajra." — A wide yield gap between states does not necessarily mean a crop has high "room to grow output without more land" at the national level; large yield variations across states are often driven by fundamental, hard-to-change agro-climatic, soil, or water constraints (such as dryland rainfed conditions versus intensive irrigation) rather than a simple capacity for laggard states to easily catch up to the best-performing states. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 193569, Requested 9549. Please try again in 22m26.976s. Need more tokens? Upgrade to Dev Tier today at https:/]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"0.0% Annual soybean yield growth over twenty years; every tonne of extra output came from more land"** — This claim is **incorrect** because the article later states that soybean yield remained at about **1,060 kg/ha in both 2003-06 and 2023-26**, implying **no yield growth**, but the **2025-26 production peak (15.3 million tonnes) and subsequent drop (12.6 million in 2025-26)** suggest yield fluctuations beyond the stated 20-year average. The **area expansion (73→129 lakh ha)** is correct, but the **zero-yield-growth claim is misleading** given the 2024-25 spike and the **2025-26 dip**, which contradicts a strict "no yield growth" narrative. [confidence: high]

- **"11% Share of India’s tur grown in one district, Kalaburagi in Karnataka"** — This is **factually accurate** based on the article’s own data (Kalaburagi grows **11% of India’s tur**), but the phrasing could be **misleading** if readers assume this is the *only* district contributing significantly, when in fact **Vijayapura (7%) and Bidar (4%)** also contribute heavily. The claim stands as a true fact but lacks context. [confidence: medium]

---
**INTERPRETATION ERRORS:**
- **"The crops with the most room to grow output without more land are those with the widest gaps between their best and worst states: jowar, maize, moong, urad and bajra."**
  The reasoning **confuses correlation with causation**. While **yield gaps** (e.g., Andhra Pradesh’s 2.9× jowar yield vs. Rajasthan’s) indicate **untapped potential**, they do not *prove* these crops can grow output **without more land**—they simply show **inefficient land use**. For example, **jowar’s area shrank by 57%** (90→39 lakh ha) despite yield gains, meaning **land loss was the dominant driver of decline**, not yield potential. The claim **overstates the policy leverage** of yield gaps to offset area contraction. [confidence: high]

- **"The crops that matter most for price stability, the irrigated cereals, are also the steadiest harvests, while the rain-fed oilseeds and pulses swing by a fifth or more in a typical year."**
  This **oversimplifies volatility drivers**. While **irrigated crops (wheat, rice)** are steadier, **rain-fed pulses/oilseeds** also exhibit volatility due to **climate shocks, policy interventions (e.g., MSP support), and market demand**—not just irrigation. For instance, **moong’s 21% swing** is partly due to **summer crop timing conflicts** (not just rain dependency), and **groundnut’s 22% swing** reflects **both drought and storage/transport inefficiencies**. The **causal link is too narrow**. [confidence: high]

---
**OUTDATED DATA:**
- **"Output averaged 147 million tonnes in 2023-26, up from 88 million in 2003-06"** — The **2025-26 third advance estimate (154 million tonnes for rice)** and **2024-25 soybean peak (15.3 million tonnes)** suggest these figures are **already outdated** for the article’s 2026 publication date. Re-check **UPAG’s latest fiscal year (2025-26 final estimates)** and **2026-27 advance estimates** for rice, soybean, and other crops. [confidence: high]

- **"Cotton production is in bales of 170 kg of lint; UPAG’s download labels it lakh tonnes, but the figures only reconcile with its published yield as bales."**
  While the **unit conversion is clarified**, the **2025-26 production figure (29.0 million bales)** is **not yet finalized**—UPAG’s **2025-26 final estimates** (expected by early 2027) may revise this. Re-check **Cotton Corporation of India (CCI) or UPAG’s latest cotton module** for 2025-26. [confidence: medium]
