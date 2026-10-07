# Fact/interpretation check — rural-indias-farm-employment-share

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/rural-indias-farm-employment-share.html`

Text-SHA1: `c23100fb13d361ab`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "India's Periodic Labour Force Survey (PLFS) began publishing a rural quarterly bulletin only from January 2025 — before that, quarterly PLFS data covered urban areas alone." — The NSO introduced quarterly bulletins for urban areas starting with the quarter ending December 2018. However, the Periodic Labour Force Survey has published comprehensive annual reports covering both rural and urban areas since its inception in 2017-18, and quarterly data collection for urban areas did not mean rural areas were entirely unmeasured prior to 2025; more specifically, rural estimates have historically been part of the annual PLFS surveys rather than a complete absence of rural quarterly data being a strict binary of "urban alone" in all contexts. [confidence: medium]

INTERPRETATION ERRORS:
- "Unemployment rose 0.8 percentage points over the same window in which agriculture's employment share fell 5.6 points and the secondary and tertiary sectors gained. That complicates the more optimistic reading of the shift — workers smoothly moving from farms into better non-farm jobs. If that were the whole story, rural unemployment would have no reason to rise at all." — A rise in the unemployment rate alongside a rising absolute or percentage share of employment in secondary and tertiary sectors does not logically preclude workers smoothly moving from farms into non-farm jobs. The unemployment rate measures the proportion of the *labour force* (which expands when individuals enter the job market seeking work) that is unemployed; an economy can experience simultaneous net job creation in non-farm sectors and an expanding labour force where job-seekers temporarily outpace immediate absorption, meaning rising unemployment and structural transition are not mutually exclusive. [confidence: high]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Agriculture's share of rural female employment fell from 75.5% to 73.5% to 70.7% across the same three quarters"* — **The article does not provide a source or methodology for how the rural female employment share was derived from the PLFS data (which reports rural *total* employment by sector, not gender-disaggregated sector shares in the quarterly bulletins).** The PLFS rural bulletins (as per the article’s own sources) only publish *total* rural employment by sector, not gender-specific sector shares. The claim appears to be an extrapolation from the overall rural agriculture share (52.9%) and the gender gap in rural employment (e.g., women’s share of rural employment is typically higher than men’s), but this is not explicitly supported by the cited PLFS tables. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"Workers are not just leaving farms, a rising share are also moving from self-employment into regular wage jobs"* — **This claim conflates two distinct but not mutually exclusive trends:**
  1. A **shift within agriculture**: The drop in self-employment (63.2% → 61.4%) could reflect *within-agriculture* changes (e.g., wage labour rising relative to self-employment in farming), not necessarily a move out of agriculture entirely.
  2. A **shift out of agriculture**: The 5.6-point drop in agriculture’s employment share *could* indicate workers leaving farming for non-farm jobs, but the data does not isolate this—it only shows a net change in sectoral employment shares.
  The article later acknowledges that unemployment rose (4.0% → 4.8%), suggesting some workers left agriculture without immediately securing non-farm employment. Thus, the claim overstates the *direction* of the shift (from self-employment *to* regular wage jobs) without ruling out stagnation or joblessness as intermediate steps. [confidence: high]

---
**OUTDATED DATA:**
none found
