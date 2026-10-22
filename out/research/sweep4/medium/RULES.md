# Rules for applying sweep-4 MEDIUM findings (22 Oct 2026)

Repo: /home/user/blogger_writeups_code. Live post copies: posts/<slug>.html (do NOT edit these).
Output: out/update-2026-10-22-sweep4m/<slug>.html (a full copy of posts/<slug>.html with ONE new note inserted) and append one line per post to your log file.

For each post in your group JSON:
1. Read the finding(s) for that post (claim, current, sources, suggested wording, confidence).
2. Open posts/<slug>.html (strip tags with python to read). Confirm the quoted claim is actually in the live post. If it is not there, or an existing dated note (div class="warn") already covers the point, SKIP and log the reason.
3. SKIP (log reason) if: the reviewer's confidence is Low; the reviewer says to check a primary source before adding a note; or the finding is only that something "has not happened yet" with no new fact.
4. Otherwise write ONE note for the post covering all its applicable findings, in plain English, using the reviewer's suggested wording as a base but tightening it:
   - Start with "<b>Updated 22 October 2026.</b>"; end with "<i>The original text below is unchanged.</i>"
   - State what the post said, what is now reported, and the date of the new fact. Attribute: "according to X" / "as reported by Y". Say "reported" for single-source items. Never add facts not in the finding.
   - Include 1-3 source links from the finding as <a href="URL">short name</a>. Use only URLs present in the finding.
   - Rupees as Rs or the ₹ already used by the post; keep the post's units. No jargon; short sentences. Max ~120 words per finding.
   - Exact HTML wrapper:
     <div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;margin:1.2em 0;border-radius:4px"> ... </div>
5. Insert the note: if the post already has a <div class="warn" ...> between <h1 and the first <h2, insert the new note immediately ABOVE the first such warn div (newest on top). Otherwise insert immediately before the first <h2 that follows <h1. Change nothing else in the file.
6. Write the result with python (read/replace/write, utf-8). Then check: the only difference from posts/<slug>.html is the inserted div (assert len(new)-len(old)==len(note)+newline and new.replace(note+"\n","",1)==old); tags balanced in the note.
7. Log line format (tab-separated): slug<TAB>APPLIED|SKIPPED<TAB>items applied (file#n)<TAB>one-line reason/summary

Do not use WebSearch/WebFetch. Do not commit. Do not touch other files.
