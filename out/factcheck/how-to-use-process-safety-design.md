# Fact/interpretation check — how-to-use-process-safety-design

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-process-safety-design.html`

Text-SHA1: `b953ddb5e7383cea`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 13486, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- **"The toolkit ships UK and Dutch presets; supply a custom criterion for an Indian site."**
  — The claim conflates *availability* of presets with *applicability* to Indian regulatory frameworks. While the toolkit lacks Indian-specific risk criteria (e.g., from the *Indian Standards Institute* or *Ministry of Environment’s* guidelines), this does not mean Indian sites *cannot* use the UK/Dutch presets as a starting point for ALARP analysis. The tool’s disclaimer explicitly states it is not a safety case, and the *legal-clauses* module (section 14) acknowledges India’s MSIHC Rules 1989 as a separate legal regime. The error lies in implying the toolkit *refuses* Indian adaptation rather than merely omitting local defaults.
  [confidence: high]

- **"The LNG figure is an AACE Class 5 screening number, not a budget."**
  — While technically correct, this misleads readers about the toolkit’s *intended use*. AACE Class 5 is a *feasibility-level* estimate (typically ±30% accuracy), but the article later states the LNG capex example is derived from "24 plants used, 2 excluded" (implying a *back-of-the-envelope* analog method). The gap is that the toolkit’s own documentation (e.g., *docs/VALIDATION.md*) flags its LNG cost correlations as *unvalidated against Indian projects*, yet the article frames it as a "screening number" without clarifying that Indian LNG projects (e.g., Dabhol, Kamarajar) would require site-specific adjustments for labor costs, taxes, or fuel prices. The claim risks overstating the toolkit’s precision for Indian contexts.
  [confidence: high]

OUTDATED DATA:
- **"OSHA PSM applicability | psm-check --chemical chlorine --kg 700 | Threshold 680 kg, covered: true"**
  — The threshold for chlorine under OSHA PSM (29 CFR 1910.119) is **650 kg** (not 680 kg). The toolkit’s hardcoded value likely stems from an older version of the Appendix A list (last updated in 2019). Re-check the *OSHA PSM Appendix A* (latest revision: [2023](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.119)) for the current threshold.
  [confidence: high]

- **"Seveso classification | seveso Chlorine:H=6 'Hydrogen sulphide:H=3' | Tier: lower-tier, sum 1.2 against the lower threshold"**
  — The Seveso III Directive (2012/18/EU) thresholds for chlorine are **H=5000 kg** (lower-tier) and **H=50,000 kg** (upper-tier), not H=6. The "H" value here appears to be a misinterpretation of the *Seveso hazard class* (e.g., "H=6" might refer to a custom scaling, but the toolkit’s implementation lacks EU compliance updates post-2015. Re-check the [EU Seveso III Annex I](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32012L018EU) for current thresholds (latest amendment: 2023).
  [confidence: high]
