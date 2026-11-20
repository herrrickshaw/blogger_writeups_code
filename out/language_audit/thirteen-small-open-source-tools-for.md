# Language audit — Open-source tools for developers and AI users: 13 small tools and what each one does

*https://blog.vertistratsolution.com/2026/11/thirteen-small-open-source-tools-for.html*

**This is a report, not an applied fix.** LanguageTool has a high false-positive rate on this blog's prose (chart captions, code identifiers, valid constructions it misparses) — review each item before touching the post.

- **[GRAMMAR/PRP_VB]** Check that the noun ‘router’ after the pronoun ‘I’ is correct. It’s possible that you may need to switch to a possessive pronoun, or use another part of speech.
  context: ..._API_KEY for the Claude path).  python -I router.py --prompt "Summarize: tariffs"  With ...
- **[GRAMMAR/A_INSTALL]** The word ‘install’ is not a noun.
  context: ...ps a snapshot of 125 documents, and the install (sentence-transformers and two small mo...
  suggested: installation
- **[GRAMMAR/A_INSTALL]** The word ‘install’ is not a noun.
  context: ...th requirements.txt as written, a fresh install picked SQLAlchemy 2.1.5 and seeding fai...
  suggested: installation
- **[GRAMMAR/NOUN_APOSTROPHE_S_VERB]** An apostrophe ‘s’ denotes possession. Did you mean to use the plural form of the noun (no apostrophe)?
  context: ...rove that a copy is safe to delete. The repo’s delete_archive_twins.sh --run deletes r...
  suggested: repos
- **[CASING/ID_CASING]** This abbreviation for “identification” is spelled all-uppercase.
  context: ...u: it catches the 409 reply, stores the id and retries. It needs Python 3.9 or new...
  suggested: ID
- **[CASING/ID_CASING]** This abbreviation for “identification” is spelled all-uppercase.
  context: ... The repo has no tests, and the session id is not cached between runs. The README’...
  suggested: ID
