# Language audit — How to use agentic-insurance-agent: open-source insurance workflows with safe AI

*https://blog.vertistratsolution.com/2026/10/how-to-use-agentic-insurance-agent-open.html*

**This is a report, not an applied fix.** LanguageTool has a high false-positive rate on this blog's prose (chart captions, code identifiers, valid constructions it misparses) — review each item before touching the post.

- **[CASING/AI]** For abbreviations such as ‘artificial intelligence’, use all capital letters. The rare word ‘ai’ is a synonym for ‘three-toed sloth’.
  context: ...ts.  On top sits a GenAI service in the ai/ folder: document reading, a triage age...
  suggested: AI
- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...e # or: gemini  Install  Clone the repo.git clone https://github.com/herrrickshaw/a...
  suggested:  Git,  git
- **[GRAMMAR/NON3PRS_VERB]** The pronoun ‘I’ must be used with a non-third-person form of a verb.
  context: ...0.6 seconds. The README says python3 -I tests/test_handlers.py, but on a system Pytho...
  suggested: test
- **[CASING/AI]** For abbreviations such as ‘artificial intelligence’, use all capital letters. The rare word ‘ai’ is a synonym for ‘three-toed sloth’.
  context: ...e tests.  .venv/bin/python -m pytest -v ai/tests  16 passed in about 3.6 seconds (...
  suggested: AI
- **[CASING/AI]** For abbreviations such as ‘artificial intelligence’, use all capital letters. The rare word ‘ai’ is a synonym for ‘three-toed sloth’.
  context: ...passed in about 3.6 seconds (10 in test_ai.py and 6 in test_governance_fairness.py...
  suggested: AI
- **[CASING/AI]** For abbreviations such as ‘artificial intelligence’, use all capital letters. The rare word ‘ai’ is a synonym for ‘three-toed sloth’.
  context: ....  AI_PROVIDER=mock .venv/bin/python -m ai.evals.run_evals  A JSON report. Classif...
  suggested: AI
- **[CASING/AI]** For abbreviations such as ‘artificial intelligence’, use all capital letters. The rare word ‘ai’ is a synonym for ‘three-toed sloth’.
  context: ...nything yet.  Explain the guardrails in ai/guardrails.py for personal data, prompt...
  suggested: AI
