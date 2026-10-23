# Language audit — How to use blog-consistency-check: a "is this blog post broken?" audit for HTML posts

*https://masaladeutsch.blogspot.com/2026/10/how-to-use-blog-consistency-check-is.html*

**This is a report, not an applied fix.** LanguageTool has a high false-positive rate on this blog's prose (chart captions, code identifiers, valid constructions it misparses) — review each item before touching the post.

- **[GRAMMAR/CD_NN]** Possible agreement error. The noun ‘blocker’ seems to be countable.
  context: ...hat changed  10static rules per post (4 blocker, 2 major, 4 minor)  1public post audite...
  suggested: blockers
- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...: gemini  Install  Clone the repository.git clone https://github.com/herrrickshaw/b...
  suggested:  Git,  git
- **[CASING/LC_AFTER_PERIOD]** If a new sentence starts here, add a space and start with an uppercase letter.
  context: ...s. Check the two tools it shells out to.which curl node  Quick start: commands and wh...
  suggested:  Which,  which
