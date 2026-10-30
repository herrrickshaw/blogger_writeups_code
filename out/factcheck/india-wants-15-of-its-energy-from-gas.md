# Fact/interpretation check — india-wants-15-of-its-energy-from-gas

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-wants-15-of-its-energy-from-gas.html`

Text-SHA1: `e363b04c239a8503`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Taking the fleet back to its 2017-18 load would need roughly 10 bcm more gas a year, on this blog’s scaling of PPAC’s figure for gas burned in power. That would add about 1.0 percentage points to gas’s share of primary energy." — Adding 10 bcm of gas (roughly 384 PJ) to a projected primary energy supply of nearly 49,000 PJ (48,782 PJ) amounts to an increase of less than 0.8% of total primary energy supply, not a full 1.0 percentage point increase in gas's overall share of the energy mix. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b network error: <urlopen error _ssl.c:1126: The handshake operation timed out>]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Gas’s share of primary energy slipped from 7.5% to 7.0% over the decade to 2023-24"* — The article later states the share was **6.4% in 2025-26** (blog’s estimate) and **6.7% in 2022-23** (MoSPI data), contradicting the 7.0% claim for 2023-24. [confidence: high]
- *"India used about 189 MMSCMD in 2025-26"* — The article’s own table shows **69 bcm (≈690 MMSCMD)** for 2025-26, not 189 MMSCMD. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Reaching the target would need consumption to grow about 29% a year for four years"* — This assumes a linear projection from 2025-26 to 2029-30, ignoring:
  1. **Declining domestic output** (IEA caps it at ~38 bcm by 2030, flat since 2023-24).
  2. **LNG capacity constraints** (58.5 Mt/year terminal capacity vs. 112 Mt needed).
  3. **Price sensitivity** (idle power plants only run at $6–7/MMBtu, far below 2026 spot prices).
  The claim conflates *potential demand* with *feasible supply* without addressing bottlenecks. [confidence: high]

**OUTDATED DATA:**
- *"Gas share of India’s primary energy supply, % (MoSPI energy balance, 2014-15 to 2023-24)"* — MoSPI’s latest energy balance (as of 2026) likely includes **2024-25 and 2025-26** data; the article’s 2025-26 estimate is derived from PPAC volumes and may not align with MoSPI’s updated ratios (e.g., 2023-24’s 38.4 PJ/bcm vs. 2015-16’s 43.2 PJ/bcm). [confidence: high]
- *"Terminals worked at about 47% of capacity in 2025"* — The **International Gas Union’s 2026 World LNG Report** (cited) may have updated 2025–2026 utilization rates post-Hormuz disruption (e.g., Dahej’s 92% vs. others’ 10–40%). [confidence: medium]
