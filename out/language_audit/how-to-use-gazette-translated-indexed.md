# Language audit — How to use gazette-translated-indexed: a citation index of Indian gazette notifications

*https://blog.vertistratsolution.com/2026/10/how-to-use-gazette-translated-indexed.html*

**This is a report, not an applied fix.** LanguageTool has a high false-positive rate on this blog's prose (chart captions, code identifiers, valid constructions it misparses) — review each item before touching the post.

- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...e repo and create a virtual environment.git clone https://github.com/herrrickshaw/g...
  suggested:  Git,  git
- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...e.  python3 -c " import sqlite3 from db.crud import get_lineage c=sqlite3.connect('g...
  suggested:  Crud,  crud
