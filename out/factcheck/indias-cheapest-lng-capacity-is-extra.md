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
- "QatarEnergy declared force majeure after the March 2026 attack on Ras Laffan" — Ras Laffan is a major industrial city and port in Qatar, and while geopolitical tensions and attacks in the wider Middle East (such as involving the Houthis or Iran) have occurred, there is no factual record of a March 2026 military attack directly on Ras Laffan resulting in a force majeure declaration by QatarEnergy of this nature. [confidence: medium]

INTERPRETATION ERRORS:
- "At PNGRB’s own conversion (190 MMSCMD = 52.7 MMTPA) that is about 55.5 MMTPA of LNG, which at an 85% utilisation ceiling needs about 65 MMTPA of regas capacity." — There is a mathematical/logical gap in applying an 85% utilisation ceiling to calculate required nameplate capacity. If demand is 55.5 MMTPA, dividing by an 85% utilization factor yields roughly 65.3 MMTPA of required capacity, but treating 85% as a hard operational ceiling across all terminals ignores geographic mismatch, pipeline constraints, and the fact that nameplate capacity is a nominal rating often exceeded by efficient terminals (like Dahej running at 95-100%+). [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 10453, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"Dahej ran at 92% of capacity while the new onshore terminals worked at 24–37% in April–May 2026"** — The claim conflates two metrics: Dahej’s utilisation is reported as **91.9%** (on its old 17.5 MMTPA base) in the PPAC data, while the newer terminals’ utilisation ranges from **10.5% (Chhara) to 40.1% (Dabhol)**. The 92% figure does not align with the cited PPAC data for April–May 2026 (confidence: **high**).

**INTERPRETATION ERRORS:**
- **"The pipeline out, not the tank, is the constraint"** — While pipeline evacuation capacity is cited as a key issue (e.g., GSPL’s 40 MMSCMD vs. 95–100 MMSCMD regas capacity in Gujarat), the claim oversimplifies the problem. The article itself notes that **destination clauses in LNG contracts** and **buyer fuel-switching** also contribute to low utilisation, not just pipeline bottlenecks (confidence: **high**).

**OUTDATED DATA:**
- **"PPAC’s latest Ready Reckoner lists 53.5 MMTPA of regasification capacity"** — PPAC’s **May 2026 Ready Reckoner** (published June 2026) already reflects Petronet’s Dahej expansion to **22.5 MMTPA**, raising total nameplate capacity to **~58.5 MMTPA**. The claim understates the current capacity (confidence: **high**).

*(No other distinct errors found in the requested categories.)*
