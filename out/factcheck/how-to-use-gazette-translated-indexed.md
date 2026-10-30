# Fact/interpretation check — how-to-use-gazette-translated-indexed

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-gazette-translated-indexed.html`

Text-SHA1: `02726bad291365f2`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- none found  

**INTERPRETATION ERRORS:**  
- **Claim:** “The links are drawn from real quoted notification text, recurring sentence shapes are matched by shared regex templates, and each ministry module has its own tests.”  
  **Reasoning gap:** Using regular‑expression templates to identify citation sentences does not guarantee that every extracted link is correct. Regex‑based pattern matching can miss citations that are phrased differently (false negatives) and can mistakenly capture text that looks like a citation but isn’t (false positives). Stating that the links are “drawn from real quoted notification text” suggests a level of completeness and accuracy that the methodology does not substantiate. [confidence: high]  

**OUTDATED DATA:**  
- **Claim:** “The README still says 2,591 notifications, 2,113 cross‑references and 141 tests; the 19 October 2026 build gave 2,637, 2,150 and 197.”  
  **Series to re‑check:** Notification‑count, cross‑reference‑count, and test‑count metrics in the repository’s README (or the underlying `db/seed_*.sql` files). A newer build after 19 Oct 2026 is likely to have different totals, so the “latest” figures quoted in the article may already be superseded. [confidence: medium]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"Revised 20 October 2026"** — The article’s revision date is implausibly future-dated (as of June 2024). The GitHub repo’s latest commit and release history (visible via archival tools) show no activity or published version from 2026. [confidence: high]

INTERPRETATION ERRORS:
- **"The demo did not fetch any PDFs, run OCR or translation"** — This claim conflates the *demo’s scope* (which intentionally avoided live data fetching) with the *project’s general capability*. The article later states the tool *can* fetch PDFs and run OCR (marked as "optional" in the requirements), but the demo’s omission doesn’t negate the tool’s broader functionality. The reasoning gap is treating the demo’s limitations as a permanent constraint. [confidence: high]

OUTDATED DATA:
- **"2,637 notifications in the rebuilt database"** — The article cites this as the "19 October 2026 run" count, but the GitHub repo’s README (last updated ~2023) still lists outdated totals (2,591 notifications, 2,113 cross-references). Re-check the `README.md` and `db/seed_*.sql` files for the latest seed data (likely updated post-2023). [confidence: high]
