# Language audit — How to use market_screener_rag: backtested stock strategies by country

*https://masaladeutsch.blogspot.com/2026/10/how-to-use-marketscreenerrag-backtested.html*

**This is a report, not an applied fix.** LanguageTool has a high false-positive rate on this blog's prose (chart captions, code identifiers, valid constructions it misparses) — review each item before touching the post.

- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...e repo and create a virtual environment.git clone https://github.com/herrrickshaw/m...
  suggested:  Git,  git
- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...ctivate  Install the three dependencies.pip install -r requirements.txt  Quick star...
  suggested:  Pip,  pip
- **[CASING/IN_CHINA]** Capitalize this word if you mean the country, not white porcelain.
  context: ...screener_rag.py ask "does value work in china"  The line (best match: China), then th...
  suggested: China
- **[GRAMMAR/THE_SUPERLATIVE]** A determiner may be missing.
  context: ...sk "does value work in china"  The line (best match: China), then the China page. The...
  suggested: ( the best
