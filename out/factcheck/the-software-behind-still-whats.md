# Fact/interpretation check — the-software-behind-still-whats

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-software-behind-still-whats.html`

Text-SHA1: `28bb16db2997ae95`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Now in its 36th year of existence (the first ETM predates this specific numbering scheme), the 27th edition in November 2024 drew more than 1,400 delegates..." — There is a mathematical contradiction: if the event is in its 36th year, its recent edition cannot be the 27th edition. [confidence: high]

INTERPRETATION ERRORS:
- "Now in its 36th year of existence (the first ETM predates this specific numbering scheme), the 27th edition in November 2024 drew more than 1,400 delegates and featured 76 oral papers across 15 technical sessions. The 28th edition's published focus areas run across 20 themes..." — The text links an event's chronological age (36 years) to its sequential edition numbering (27th and 28th) to imply longevity, but an annual event held over 36 years should have roughly 36 editions, meaning a gap of nearly a decade is unexplained. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"IFFCO Phulpur is a fertiliser plant, not an ethanol or biofuel facility"* — **Misleading framing of the case study.** While the article correctly notes that IFFCO Phulpur is a urea plant, it groups the Nanoprecise case study under biofuel-plant maintenance software because predictive-maintenance vendors pitch the same product to both sectors. However, the claim that the case study "does not evidence a specific ethanol-distillery deployment" is accurate, but the article’s broader implication—that this is a *fertiliser plant* and thus irrelevant to biofuels—ignores that the vendor’s marketing targets both industries. The error lies in the **overcorrection**: the case study *is* relevant to biofuel-plant software discussions, even if it’s not from a biofuel facility. [confidence: high]

- *"DGS (Engineering) Circular No. 32 of 2025 [...] is a genuinely new compliance layer"* — **Unverified regulatory status.** The article cites the circular as "issued" but notes it describes itself in places as "proposed" and advises checking DG Shipping’s public register for its current status. This creates ambiguity: if the circular is still proposed, it may not be enforceable. The claim lacks confirmation that it has been **finalized** as of 2026. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The $145,000/day production loss [...] puts this case study on considerably firmer ground than most of what's in this notebook"* — **Apples-to-oranges comparison.** The $145k/day figure is a **real, named-plant case study** (IFFCO Phulpur), but the article then contrasts it with **vendor marketing claims** (e.g., iFactory’s 25% yield boost) without clarifying that the latter are **unverified, aggregated, and non-India-specific**. The implication that the IFFCO case is "firmer" because it’s a single plant ignores that the vendor claims are also **marketed as real-world deployments** (e.g., "50+ AD facility deployments"). The gap: the article conflates **documented evidence** (IFFCO) with **unverified vendor assertions** (iFactory) without distinguishing their reliability. [confidence: high]

- *"The compliance layer [...] is where digitisation is arguably furthest along"* — **Overgeneralization from US/EU models.** The article highlights LCFS (US) and CORSIA (EU) compliance platforms as mature, but **India’s biofuel compliance ecosystem is not yet aligned with these standards**. The DGS circular (2025) is new, and the article does not address whether Indian biofuel producers are **actually using** these compliance tools or if they’re merely theoretical. The claim assumes digitization follows a Western template, which may not apply in India. [confidence: medium]

---
**OUTDATED DATA:**
- *"2008 The actual publication year of a 'digital transformation' source this notebook filed as current"* — **2008 Ethanol Producer Magazine article on John Deere’s RINSTAR integration** — **Series to re-check:** *Ethanol Producer Magazine archives*; **newer period:** 2026 (but the article itself is from 2008). The issue is that the **notebook’s curation** misdated this as "current" in 2026, not the data itself. However, the article’s **relevance** is outdated because RIN management has been a **standard feature for nearly 20 years** in US biofuel software. [confidence: high]

- *"22 Jul 2025 Date of India's first dedicated regulatory circular on marine biofuel bunkering"* — **Potential supersession risk.** While the date is correct, the article notes the circular may be **"proposed"** and advises checking DG Shipping’s **public circular register** for updates. **Series to re-check:** *DG Shipping’s official circular database*; **newer period:** 2026 (for amendments/finalization). [confidence: high]
