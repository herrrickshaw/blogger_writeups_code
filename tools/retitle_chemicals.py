#!/usr/bin/env python3
"""Disambiguate four chemical posts whose titles compete for one query.

These are NOT duplicate content. Checked before touching anything:

  chemical-import-substitution-hsn-8-registry        5.5k chars, 0 tables
      The methodology and findings page: the signal framework, the four
      categories and their counts, and a stated list of what the analysis
      cannot do. Its tables were deliberately moved out in v3.0.0.
  chemical-import-substitution-full-hsn-8_01082878313  185k chars, 8 tables
      The data companion holding the moved tables.
  top-15-chemicals-for-import          (July URL)   45k chars
      Code-by-code detail with rationale.
  top-15-chemicals-for-import (August URL, id-suffixed in the archive)  5.7k
      The FY26-30 roadmap summary. Same slug, different month path.

So nothing is deleted and no URL changes. The defect is that each pair shares
its opening words, which is what makes them compete in search and
indistinguishable in a list. The fix is to lead with the differentiator.

Both the Blogger title AND the in-body <h1> are changed. The theme hides its own
h1 when the body supplies one, so changing only the Blogger title would leave the
page heading disagreeing with the search result.
"""
import pathlib, sys, time
# blogger_api.py sits beside this file, so resolve from here rather than from
# one machine's checkout path.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import blogger_api as B

PLAN = [
    # post id, new Blogger title, old h1 text (exact), new h1 text
    ("6790374087242629357",
     "Which of 827 Chemical HSN-8 Codes Are Real Substitution Targets",
     "Chemical Import Substitution &#8212; Full HSN-8 Chapter-Wise Registry",
     "Which of 827 Chemical HSN-8 Codes Are Real Substitution Targets"),
    ("8677832990636879595",
     "Chemical Import Substitution: the Full 827-Code Data Tables",
     "Chemical Import Substitution &#8212; Full HSN-8 Registry (827 Codes)",
     "Chemical Import Substitution: the Full 827-Code Data Tables"),
    ("1336090290969568886",
     "The Top 15 Import-Substitution Chemicals, Code by Code",
     "Top\n15 Chemicals for Import Substitution: Detailed Analysis with\nRationale",
     "The Top 15 Import-Substitution Chemicals, Code by Code"),
    ("4751284523575450171",
     "India's FY26–30 Chemical Independence Roadmap: the Top 15",
     "TOP 15 CHEMICALS FOR IMPORT SUBSTITUTION",
     "India&rsquo;s FY26&ndash;30 Chemical Independence Roadmap"),
]

dry = "--apply" not in sys.argv
for pid, title, old_h1, new_h1 in PLAN:
    p = B.api(f"/blogs/{B.BLOG_ID}/posts/{pid}")
    body = p["content"]
    n = body.count(old_h1)
    print(f"\n{pid}  {p['title'][:60]}")
    print(f"   -> title: {title}")
    print(f"   h1 occurrences of old text: {n}")
    if n != 1:
        print("   SKIP: h1 text not uniquely present — refusing to guess")
        continue
    new_body = body.replace(old_h1, new_h1, 1)
    if dry:
        print("   DRY RUN")
        continue
    B.api(f"/blogs/{B.BLOG_ID}/posts/{pid}",
          data={"id": pid, "title": title, "content": new_body,
                "published": p["published"], "labels": p.get("labels") or []},
          method="PUT")
    time.sleep(B.WRITE_GAP_SECONDS)
    q = B.api(f"/blogs/{B.BLOG_ID}/posts/{pid}")
    print(f"   applied. live title now: {q['title'][:60]}")
    print(f"   published preserved: {q['published'][:19]} | labels {q.get('labels')}")
