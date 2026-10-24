# Fact/interpretation check — indias-cheapest-lng-capacity-is-extra

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-cheapest-lng-capacity-is-extra.html`

Text-SHA1: `b277feba1ad06ad0`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "QatarEnergy declared force majeure after the March 2026 attack on Ras Laffan" — Ras Laffan is a major industrial city and port in Qatar, and while it is a critical hub for LNG production, there is no factual record of a "March 2026 attack on Ras Laffan" causing QatarEnergy to declare force majeure; this appears to be a fabricated or hallucinated geopolitical event. [confidence: high]

INTERPRETATION ERRORS:
- "PPAC still lists Dahej at 17.5 MMTPA on 1 June 2026, two months after its 22.5 MMTPA expansion was commissioned. Petronet’s own results put Dahej at 65.6% of the enlarged capacity in April–June 2026, against about 92% a year earlier; on the old base the same volume would have been about 85%... The expansion arrived just as Dahej’s main long-term supplier, QatarEnergy, declared force majeure... so for now the new 5 MMTPA is mostly headroom." — The author attributes the drop in capacity utilisation of the newly expanded plant to a supply shock (force majeure), but mathematically, expanding nameplate capacity while total throughput remains constant or decreases will mechanically lower the percentage utilisation rate even if absolute volumes delivered were steady, representing an apples-to-oranges comparison of utilisation rates across two different base capacities. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 10590, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"Dahej ran at 92% of capacity"** — The article states Dahej’s utilisation was **91.9% in April–May 2026** (PPAC data), not 92%. The 92% figure appears in the earlier context (old 17.5 MMTPA base), but the claim conflates the two metrics without clarifying the distinction. [confidence: high]

**INTERPRETATION ERRORS:**
- **"The pipeline out, not the tank, is the constraint"** — While PNGRB’s expert committee correctly identifies pipeline evacuation as the primary reason for low utilisation at most terminals, the article **overgeneralises this to all terminals** (e.g., Dahej’s high utilisation despite pipeline constraints in Gujarat). Dahej’s case is an exception due to its direct GAIL pipeline access, not a universal rule. The claim misrepresents the **terminal-specific nature of constraints**. [confidence: high]

**OUTDATED DATA:**
- **"PPAC lists Dahej at 17.5 MMTPA on 1 June 2026"** — PPAC’s latest data (May 2026 Ready Reckoner) should reflect the **22.5 MMTPA expansion commissioned on 31 March 2026**. The article notes this discrepancy but does not flag it as outdated data requiring verification against the **PPAC Monthly Ready Reckoner (Table 21, June 2026 release)**. [confidence: high]

---
*Note: No other distinct factual, interpretive, or outdated-data issues were identified based on the provided text.*
