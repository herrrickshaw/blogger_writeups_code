# Fact/interpretation check — how-to-use-process-safety-design

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-process-safety-design.html`

Text-SHA1: `255d4ff69c14d776`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "For India, the Manufacture, Storage and Import of Hazardous Chemical Rules 1989 treat a modification likely to cover major accident hazards as a new activity (rule 6) and need a further safety report at least 90 days before a material modification (rule 11), which is the central constraint on a derogation there." — The Manufacture, Storage and Import of Hazardous Chemical (MSIHC) Rules, 1989 do not have a Rule 11 requiring a safety report 90 days before a material modification; Rule 11 pertains to updating safety reports or providing information on industrial activities, whereas safety report submission timelines and major accident hazard controls follow different statutory provisions under the rules and the Factories Act, 1948. [confidence: medium]

INTERPRETATION ERRORS:
- "For India, the Manufacture, Storage and Import of Hazardous Chemical Rules 1989 treat a modification likely to cover major accident hazards as a new activity (rule 6)... which is the central constraint on a derogation there." — Rule 6 of the MSIHC Rules governs the "Approval of sites" and obligations of industrial activities upon initial notification or expansion, rather than functioning specifically as a regulatory enforcement mechanism or "central constraint" on engineering "derogations" (which are internal corporate departures from engineering standards). [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 14651, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- **"The toolkit warns on this very study: propane is heavier than air, and the flash-fire and toxic footprints use a neutral Gaussian plume, so consider a dense-gas override."**
  The claim conflates two distinct modeling approaches (neutral plume vs. dense-gas dispersion) without clarifying that the neutral-plume results are *only* valid for lighter-than-air gases (e.g., methane). Propane’s heavier-than-air behavior invalidates the neutral-plume model entirely, but the article does not explicitly state that the reported distances/risk estimates are *optimistic* or *invalid* for propane—only that they should be cross-checked. This risks misleading readers into treating the neutral-plume outputs as directly applicable to propane without recognizing their fundamental flaw.
  [confidence: high]

- **"The toolkit’s own use cases found that its point-source pool-fire distances and this solid-flame method disagree by about four times in the far field."**
  The claim implies a direct equivalence between point-source and solid-flame models for the same scenario, but the disagreement arises because they model *different physical phenomena* (radiant fraction assumptions). The article does not clarify that the "four-times" discrepancy is not a validation failure but a documented difference in methodology, which users must reconcile contextually (e.g., near-field vs. far-field applicability). This could lead readers to misinterpret the toolkit’s outputs as inconsistent when they are, in fact, complementary.
  [confidence: high]

OUTDATED DATA:
- **"The toolkit ships UK and Dutch presets; supply a custom criterion for an Indian site."**
  — *MSIHC Rules 1989* (cited in section 14) are outdated for current Indian hazardous chemical regulations. The **Hazardous Chemical (Restraint During Transportation) Rules, 2021**, and **Hazardous and Solid Waste Management Rules, 2016** (amended 2022) supersede the 1989 rules. While the toolkit’s legal-clauses module flags MSIHC-1989 as "grade B" (unverified), it does not reference the newer rules or their risk criteria (e.g., **IS 15225:2017** for QRA tolerables).
  [confidence: high] *(Series to re-check: Indian Ministry of Environment’s latest hazardous chemical regulations; newer period: 2021/2022 amendments.)*

---
**Note on scope**: The article is primarily a *tool demonstration* (not an India-specific policy analysis), so factual errors in technical outputs (e.g., unit conversions, fluid properties) were not flagged unless they contradicted universally accepted standards (e.g., API 520, ISO 13855). The above errors focus on *interpretive gaps* and *regulatory obsolescence* relevant to an India-focused audience.
