# Fact/interpretation check — how-to-use-blog-consistency-check-is

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-blog-consistency-check-is.html`

Text-SHA1: `edfb30e64e6f4991`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
none found

INTERPRETATION ERRORS:
none found

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**
- “Revision history. v1.0.0 — 9 November 2026 — first published.” — The article claims a revision/publication date that is **in the future** relative to today’s date (23 October 2026). A document cannot be revised on a date that has not yet occurred. [confidence: high]  
- “python3 audit.py --url https://masaladeutsch.blogspot.com/2026/10/how-to-use-ship2shorerag-offline.html” — The cited URL does **not exist** on the masaladeutsch.blogspot.com archive; a search of the blog’s posts for October 2026 shows no entry with the slug “how-to-use-ship2shorerag-offline.html”. The article therefore references a non‑existent page. [confidence: medium]  

**INTERPRETATION ERRORS:**
- “The run found a real BLOCKER (dark palette with no light‑mode lock) on a recent post, so the rules do fire on current content.” — This draws a **general conclusion** about the effectiveness of the rule set for all current posts based on a **single audit**. One instance does not constitute sufficient evidence to claim that the rules reliably detect blockers across the entire blog. [confidence: high]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- **"The run found a real BLOCKER (dark palette with no light-mode lock) on a recent post, so the rules do fire on current content."**
  — The claim conflates a *static rule violation* (CSS dark-vars-locked) with a *visual problem* (actual dark-mode usability). The tool flags the absence of a `!important` light-mode lock, but this does not guarantee a real visual issue (e.g., the dark palette might still be usable or overridden by user preferences). The article later clarifies this is a "signal to inspect, not proof of a visible fault," but the initial phrasing overstates certainty. [confidence: high]

OUTDATED DATA:
- none found
