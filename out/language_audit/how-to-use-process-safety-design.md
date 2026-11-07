# Language audit — How to Use the Process-Safety Design Toolkit: A Complete Walkthrough, Command by Command

*https://masaladeutsch.blogspot.com/2026/11/how-to-use-process-safety-design.html*

**This is a report, not an applied fix.** LanguageTool has a high false-positive rate on this blog's prose (chart captions, code identifiers, valid constructions it misparses) — review each item before touching the post.

- **[GRAMMAR/A_INSTALL]** The word ‘install’ is not a noun.
  context: ... say “not implemented”. If you skip the install step and run from another folder, Pytho...
  suggested: installation
- **[GRAMMAR/THE_PUNCT]** Articles like ‘a’ are rarely followed by punctuation. A word may be missing after ‘a’, or the punctuation mark may not be necessary.
  context: ... print(h.surge_screen(L_m=300000, a_m_s=a, closure_s=30, rho=560, dv_m_s=1.5))" 12...
  suggested: a
- **[GRAMMAR/A_MD_VB]** Did you mean “I”?
  context: ...is complied with or formally derogated. A should is comply-or-explain. A can is o...
  suggested: I
- **[GRAMMAR/MD_BASEFORM]** The modal verb ‘MUST’ requires the verb’s base form.
  context: ...json --as-of 2026-11-06 "by_tier": MUST complied 1, derogated 3, open 0 SHOULD complied ...
  suggested: comply
- **[GRAMMAR/MD_BASEFORM]** The modal verb ‘SHOULD’ requires the verb’s base form.
  context: ... complied 1, derogated 3, open 0 SHOULD complied 0, derogated 1, open 1 CAN adopted 0, n...
  suggested: comply
- **[GRAMMAR/MD_BASEFORM]** The modal verb ‘CAN’ requires the verb’s base form.
  context: ...ULD complied 0, derogated 1, open 1 CAN adopted 0, not-adopted 1 "must_compliance": 1 o...
  suggested: adopt
