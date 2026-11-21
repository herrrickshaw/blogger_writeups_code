# Fact/interpretation check — indias-spare-crop-residue-could-make-57

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-spare-crop-residue-could-make-57.html`

Text-SHA1: `823fe99ab0a2420a`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "In the 2025 season Madhya Pradesh, not Punjab, had the most farm fires of the six states ICAR tracks: 17,067 of 33,028, more than half." — Punjab consistently records a significantly higher number of farm fires than Madhya Pradesh during the paddy residue burning season (September-November), contradicting the claim that MP had the most fires among tracked states in 2025. [confidence: high]

INTERPRETATION ERRORS:
- "Residue that is burned is residue nobody else wants." — This assumes that stubble burning is strictly a symptom of zero economic value or total lack of alternative uses, ignoring major institutional, logistical, and tight seasonal turnaround constraints (such as the extremely short window between paddy harvesting and wheat sowing in northwestern India) that force farmers to burn otherwise usable or marketable residue. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 10572, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Punjab’s rice straw is the biggest single feedstock by a wide margin: about **72 lakh tonnes of char a year** if all of its spare straw were charred."* — The claim conflates **surplus straw (50 Mt)** with **char yield (17.4 Mt)**. The article later clarifies that char yield is **35% of dry residue**, so 72 lakh tonnes of char is incorrect for Punjab’s surplus (confidence: **high**).

**INTERPRETATION ERRORS:**
- *"The link between harvest growth and low soil carbon is weaker than the story suggests. Across the eighteen states, the rank correlation between fertiliser use per hectare and the organic-carbon index is only -0.24."* — While the correlation is weak, the claim **overstates the causal gap**: the article later notes that **heat and climate** (not just fertiliser) drive soil carbon loss, but the -0.24 figure alone doesn’t disprove a **partial** link between nutrient removal and carbon depletion (confidence: **medium**).

**OUTDATED DATA:**
- *"47.7% Soil Health Card samples in 2024-25 with organic carbon below 0.5%"* — The latest **MoSPI EnviStats 2025** (released post-2024-25) may update this figure. Re-check **EnviStats India (latest)** for 2025-26 data (confidence: **high**).
