# Language audit — Two Open-Source Health Prototypes, an ICU Vitals Dashboard and a Capsule-Endoscopy Screener, and Why Neither Is a Medical Device

*https://blog.vertistratsolution.com/2026/11/two-open-source-health-prototypes-icu.html*

**This is a report, not an applied fix.** LanguageTool has a high false-positive rate on this blog's prose (chart captions, code identifiers, valid constructions it misparses) — review each item before touching the post.

- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ..., and the guide points to FrameAnalyzer.analyze as the place to add a learned detector,...
  suggested:  Analyze,  analyze
- **[GRAMMAR/PREPOSITION_VERB]** Did you mean the noun “reception” (= the act of receiving) or “receipt” (= invoice)?
  context: ...s the study reaches the colon. The live receive and send path was not run in the guide....
  suggested: reception, receipt
- **[GRAMMAR/NEITHER_NOR]** Use “nor” with neither.
  context: ... Neither is for diagnosis, patient care or monitoring of real people, and neither ...
  suggested: nor
