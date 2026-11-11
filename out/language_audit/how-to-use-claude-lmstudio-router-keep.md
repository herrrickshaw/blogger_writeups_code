# Language audit — How to use claude-lmstudio-router: keep working when Claude is unavailable

*https://blog.vertistratsolution.com/2026/10/how-to-use-claude-lmstudio-router-keep.html*

**This is a report, not an applied fix.** LanguageTool has a high false-positive rate on this blog's prose (chart captions, code identifiers, valid constructions it misparses) — review each item before touching the post.

- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...e repo and create a virtual environment.git clone https://github.com/herrrickshaw/c...
  suggested:  Git,  git
- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...uirements file, so install them by name.pip install anthropic pip install fastapi u...
  suggested:  Pip,  pip
- **[GRAMMAR/PRP_VB]** Check that the noun ‘router’ after the pronoun ‘I’ is correct. It’s possible that you may need to switch to a possessive pronoun, or use another part of speech.
  context: ...u should see  See the options.  python -I router.py --help  A usage line and options suc...
- **[GRAMMAR/PRP_VB]** Check that the noun ‘router’ after the pronoun ‘I’ is correct. It’s possible that you may need to switch to a possessive pronoun, or use another part of speech.
  context: ...dio, to see an honest failure.  python -I router.py --prompt "Summarize: tariffs"  It tr...
- **[GRAMMAR/ADVERB_OR_HYPHENATED_ADJECTIVE]** Make sure that the adjective ‘small’ is correct. Possibly, it should be an adverb (typically ~ly) that modifies ‘canned’. Possibly, it should be the first word in a compound adjective (hyphenated adjective). Possibly, it is correct.
  context: ...in server. In the demo, port 1239 was a small canned server, not LM Studio.  python -I route...
  suggested: small-canned
- **[GRAMMAR/PRP_VB]** Check that the noun ‘router’ after the pronoun ‘I’ is correct. It’s possible that you may need to switch to a possessive pronoun, or use another part of speech.
  context: ... canned server, not LM Studio.  python -I router.py --prompt "Summarize: tariffs" --loca...
