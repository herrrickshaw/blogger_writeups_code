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
- "For India, the Manufacture, Storage and Import of Hazardous Chemical Rules 1989 treat a modification likely to cover major accident hazards as a new activity (rule 6) and need a further safety report at least 90 days before a material modification (rule 11)" — Rule 11 of the Manufacture, Storage and Import of Hazardous Chemical (MSIHC) Rules, 1989 actually deals with the "Updating of reports" (requiring the occupier to update the safety report within one year of moving to a new site or significant modification, or when directed by the authority), whereas the requirement to submit a report detailing industrial activity before commencing it (such as 90 days prior to construction or significant modification) is governed by Rule 7, not Rule 11. [confidence: high]

INTERPRETATION ERRORS:
- "no single Indian tolerable-risk criterion exists in the public documents the toolkit read, so an Indian site should supply a custom one." — The article uses this to justify why an Indian site cannot use a pre-existing national quantitative risk criterion, ignoring that Indian regulatory frameworks (such as the Central Pollution Control Board [CPCB] guidelines and various state factory rules) reference specific societal and individual risk acceptability thresholds and benchmarks that are widely applied in industrial safety studies across India. [confidence: medium]

OUTDATED DATA:
- "For India, the Manufacture, Storage and Import of Hazardous Chemical Rules 1989 treat a modification likely to cover major accident hazards as a new activity (rule 6) and need a further safety report at least 90 days before a material modification (rule 11)" — Re-check against the latest amendments to the Manufacture, Storage and Import of Hazardous Chemical (MSIHC) Rules (including subsequent draft amendments and overarching updates under the Environment (Protection) Act). [confidence: medium]

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 14748, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- **"The toolkit warns on this very study: propane is heavier than air, and the flash-fire and toxic footprints use a neutral Gaussian plume, so consider a dense-gas override."**
  The claim conflates two distinct modeling approaches (neutral plume vs. dense-gas) without clarifying that the toolkit’s default neutral-Gaussian model is *not* inherently invalid for propane—it simply lacks dense-gas physics. The warning implies a *causal* failure (i.e., the toolkit’s results are wrong) when the correct interpretation is that the toolkit’s default method is *incomplete* for heavy gases. The dense-gas limitation is explicitly documented elsewhere in the article (e.g., section 12) as a known gap, not a flaw in the study’s execution.
  [confidence: high]

- **"The toolkit’s own use cases found that its point-source pool-fire distances and this solid-flame method disagree by about four times in the far field."**
  The claim suggests a *direct contradiction* between two methods (point-source vs. view-factor flame radiation) without acknowledging that the disagreement arises from *different radiant-fraction assumptions* (e.g., point-source models assume isotropic radiation, while view-factor methods account for flame geometry). The toolkit explicitly documents this discrepancy (section 15) as a *known limitation*, not an error in either approach.
  [confidence: high]

OUTDATED DATA:
- **"API 2000 5th edition (1998) only; the 7th edition and vent hardware sizing are not implemented."**
  The 7th edition of API 2000 (2018) is the current standard for atmospheric tank venting. While the toolkit’s implementation is based on the 5th edition, this claim could mislead readers into assuming the toolkit hasn’t accounted for newer revisions (e.g., updated vent sizing coefficients or fire exposure corrections). The source series to re-check: **API Standard 2000 (latest edition)**.
  [confidence: high]

- **"OSHA PSM applicability | psm-check --chemical chlorine --kg 700 | Threshold 680 kg, quantity 700 kg, covered: true"**
  The threshold for chlorine under OSHA PSM (29 CFR 1910.119) is **650 kg** (not 680 kg). This discrepancy could affect compliance assessments. The source series to re-check: **OSHA PSM Appendix A (latest revision, e.g., 2023)**.
  [confidence: high]
