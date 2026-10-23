# Fact/interpretation check — how-to-use-amazon-product-selector

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-amazon-product-selector.html`

Text-SHA1: `8c57242240094025`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Revised 19 October 2026 ... v1.0.0 — 19 October 2026" — The article is dated in the future relative to the current knowledge cutoff. [confidence: high]

INTERPRETATION ERRORS:
- "moringa oil median price 18.99 below 2000 ... The B2B price floor is INR 2,000, so a cheap consumer item fails it." — Comparing a per-unit price in US Dollars (implied by 18.99) or an unscaled unit against an absolute INR 2,000 threshold without currency conversion creates an apples-to-oranges comparison error. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “Evidence from the run: … the offline dry run shortlisted **3 of 4 keywords for B2C and 2 of 4 for B2B** with reasons for each rejection.” — The B2B output shown later lists **only two rejected keywords and no shortlisted items**, meaning **0 of 4** were shortlisted, not 2 of 4. The claim contradicts the sample output. [confidence: high]

**INTERPRETATION ERRORS**
- “The B2B price floor is INR 2,000, **so a cheap consumer item fails it**.” — The “price floor” is a user‑defined threshold in the tool’s MARKETS table, not an external market rule or regulatory barrier. Using it to conclude that “cheap consumer items cannot be sold B2B” overstates the implication of an arbitrary configuration setting. The tool could simply be re‑configured with a lower floor, so the causal link is unsupported. [confidence: high]

**OUTDATED DATA**
- “The B2B price floor is INR 2,000.” — The price‑floor value is stored in the MARKETS table and may have been revised in later releases of *amazon‑product‑selector* (e.g., v1.1.0 or later). The article cites the value from the v1.0.0 release (19 Oct 2026) without checking whether a newer default or recommended floor exists. Re‑check the MARKETS table in the current repository version (or the changelog) for the latest floor value. [confidence: medium]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- **"The volume scales for India are estimates and nothing is calibrated against observed data"** — This claim conflates two distinct limitations: (1) the tool’s scoring system uses *unobserved* (i.e., uncalibrated) volume estimates for India, and (2) the dry-run fixture data is *not* market data. The first is a technical limitation of the tool’s design (confidence: high), while the second is explicitly stated as a caveat for the dry-run mode. The phrasing risks misleading readers into thinking the *entire* tool’s volume estimates are untested, when in fact the live mode (with API keys) would use real data from NEXSCOPE and OPENWEB NINJA (confidence: high).

OUTDATED DATA:
- none found
