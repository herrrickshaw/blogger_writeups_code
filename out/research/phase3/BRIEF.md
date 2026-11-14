# Phase 3 merge brief (shared by every merge task)

Goal: combine overlapping posts into ONE better post that keeps every sourced fact worth keeping,
removes repetition, and reads as a single piece. The other posts are then moved to draft and every
link to them is pointed at the merged post (that part is done separately; do not do it).

## Inputs
- Repo: /home/user/blogger_writeups_code. Read docs/HEADLINE_STYLE.md and CLAUDE.md first.
- For each post, the CURRENT text is the newest file among out/update-*-<slug>.html (sort by name);
  if there is none, posts/<slug>.html. Read every post in your cluster in full.
- New-style titles for every post: out/retitle/titles.tsv (slug<TAB>title).

## Output
1. out/update-2026-11-14-<TARGET>.html: the merged post.
   - Start from the TARGET's current file. Keep everything before the article's first heading block
     and after its Sources/related section exactly as it is (accessibility bar, translate widget,
     disclaimer footer, scripts). Rewrite only the article itself.
   - <h1>: a title in the house style (docs/HEADLINE_STYLE.md) that covers the merged scope;
     <= 90 characters.
   - Directly after the stat tiles (or after the standfirst if there are none), add this note:
     <div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px"><b>Updated 14 November 2026.</b> This piece now combines ... (name each folded post by its subject in plain words, and say in one sentence what the combined piece adds).</div>
   - Keep the house markup and classes the posts already use (gb-stats/gb-stat, gb-h2, gb-tblwrap,
     gb-figure, gb-note, standfirst). Keep charts (inline SVG) and tables that still add information;
     drop exact duplicates. If two posts give different numbers for the same thing, use the newer
     post's figure with its date, and mention the older one only if the change itself matters.
   - Section headings: plain statements of what the section shows (style guide), no questions.
   - Keep the two house sections, merged: "What would fix this" and "What this piece could not establish".
   - One merged Sources section with every source link from every post (deduplicated).
   - Links inside the text that point to another post IN YOUR CLUSTER: replace with an in-page
     #anchor to the section that now holds that material, or remove the link and keep the words.
     Leave links to other posts alone.
   - Never invent a fact, number, date or source. Rephrase only what the posts say. Keep units.
   - Links must use https://blog.vertistratsolution.com, never masaladeutsch.blogspot.com, and the
     blog is named VertiStrat Solutions, never Masala Deutsch.
2. out/research/phase3/<TARGET>.md: short notes. Which sections came from which post, every number
   conflict and how you resolved it, and anything you dropped and why.

## Checks before you finish (fix anything that fails)
- python3 consistency-check/_local_check.py <your file> | grep -c FAIL : must be no higher than the
  same command on the TARGET's current file.
- Tag balance with Python html.parser: no unclosed or mismatched tags (void elements excepted).
- grep the file: no "masaladeutsch.blogspot.com", no "Masala Deutsch".
- The merged file should be shorter than the sum of the inputs, and the word count should be no
  more than the largest input plus about 50%.

Do not edit any other file. Do not run git. Do not publish.
Reply with: target, posts folded, new title, sizes before/after, FAIL counts before/after, and
the conflicts you resolved.
