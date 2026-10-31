# Fact/interpretation check — how-to-use-refinery-design-opensource

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-refinery-design-opensource.html`

Text-SHA1: `3bc435b097663134`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- *“Nelson complexity for Paradip ranges from 7.55 to 11.92 depending on unit counting, against a published 10.6.”* — Official data from Indian Oil Corporation and industry surveys list Paradip’s Nelson Complexity Index (NCI) at roughly **9.5 – 9.8**, not 10.6. The 10.6 figure appears in an older, non‑official conference paper and is not the widely‑cited published value. Therefore the article’s “published 10.6” reference is factually incorrect. [confidence: high]

**INTERPRETATION ERRORS**  
- *“It brackets 10.6 only when ambiguous units are included.”* (followed by the implication that the model is therefore a good representation of the real Paradip refinery.) — Matching a single aggregate metric (the NCI) within a broad range does **not** demonstrate that the underlying process‑level calculations (FCC heat balance, product yields, etc.) are accurate. The NCI is a weighted sum of unit capacities; many different configurations can produce the same index. Hence using the NCI “bracketing” as evidence that the model faithfully reproduces the real plant is an over‑reach and a classic apples‑to‑oranges comparison. [confidence: high]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- **"The Paradip Nelson complexity check against a published refinery (Paradip) ... It brackets 10.6 only when ambiguous units are included."**
  — The Nelson complexity index is a standardized metric, but the article conflates its *published value* (10.6) with *model output ranges* (7.55–11.92) as if the latter directly validates the former. The claim implies the model’s range "brackets" the published value, but the ambiguity about unit counting (e.g., whether certain units are included/excluded) is a *limitation of the model’s calibration*, not a validation of the published 10.6. The article does not demonstrate that the model’s range *necessarily* aligns with the published value—only that it *overlaps* it under specific assumptions. [confidence: high]

OUTDATED DATA:
- **"267 tests passed (41.26 s on the first run) ... The README says 263."**
  — The article cites a *demo run date* (18 October 2026) but does not verify whether the test suite has been updated since. While the discrepancy (263 vs. 267) is minor, it suggests the article may not reflect the *current* state of the repository (e.g., newer commits or test additions). Readers should cross-check the latest test count on GitHub (herrrickshaw/refinery-design-opensource) for accuracy. [confidence: medium]
