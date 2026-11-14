# Leaf brief: visual-first edition of one post (read this whole file; it is short)

Repo: /home/user/blogger_writeups_code. You own only `out/viz/<slug>/**` and `out/update-2026-11-15-<slug>.html`.
No git, no blogger_api, no edits under tools/ posts/ meta/ templates/ theme/. Nothing is published.

## Do exactly this (about 5 turns)

1. `python3 tools/viz_new.py <slug>` then Read `out/viz/<slug>/outline.md`. (Tables show as `[T3 ... rN rows]` with row numbers;
   fixes, caveats, dated notes and source links are kept by code, so do not rewrite them.)
2. Write `out/viz/<slug>/spec.json` in ONE Write call. Choose 3 or 4 findings the post's own numbers prove.
3. `python3 tools/viz_go.py <slug>`. It renders and checks. Fix every line it prints in ONE edit, run again, until `PASS <slug>`.
4. Reply in under 80 words: the 3-4 headlines, anything you left out on purpose, any figure in the original that looks wrong.
   Do not take screenshots; the driver reads the rendering.

## Spec (JSON)

```
{"top": [["66%", " of petrol's energy per litre is what ethanol carries, so E20 costs drivers 2-6% in mileage."]],   // 1-3 bullets, big number first
 "sections": [                                                                                                      // 3 or 4
  {"h2": "Energy per litre: ethanol 66% of petrol, isobutanol 74% of diesel",                                      // the finding, sentence case, <= 90 chars
   "chart": {"type":"bars", "title":"Only the two alcohols fall well short of the fuel they replace",             // takeaway, <= 90 chars
             "sub":"Share of the host fuel's energy density, %.", "source":"NITI Aayog; US DOE.",
             "unit":"%", "accent":"Ethanol in petrol", "ref":[100,"100% = same energy as the host fuel"],
             "rows":[["Ethanol in petrol",66,"E20, live"],["Isobutanol in diesel",74],["CBG in CNG",[93,95]],["Gap",null]]},
             // or "table":{"id":"T2","label":0,"value":2,"rows":"top:10","sort":"desc"}  -> rows pulled from the original's table
   "means": "One sentence.", "todo": "One sentence.",                                                              // exactly one sentence each, ending in a full stop
   "numbers": {"table":"T2"}}                                                                                       // optional collapsed table of the data
 ],
 "derived": {"190": "570/3"}}                                                                                       // numbers you computed; see rules
```
Other chart types: `{"type":"line","title":..,"series":{"A":[[2020,5],[2021,6]]},"accent":"A","unit":"%"}` (real points only; for sparse dated readings use bars, never
a line across big gaps); `{"type":"waterfall","title":..,"start":["2024",100],"steps":[["Gain",12],["Loss",-5]],"end":"2025"}`;
`{"type":"flow","events":[["Date","What happened"],["Date","What",true]]}` (a sequence; true accents one). Negative bar values draw left of zero.
Optional: `"fixes":"drop"`, `"tables":"none"|["T2"]` (default keeps every original table collapsed), `"details":[{"summary":"..","html":".."}]`.

## Rules (the checker enforces the first four)

1. Every number you write is in the original, or is arithmetic on its numbers declared in `derived` (`"190":"570/3"`; operands must be original numbers), or a count you made
   (`"7":"count: seven countries in the table"`). Never round a figure into a different number; keep "about", "reported", "projected".
2. One unit per chart. Never put a flow (a year's total), a stock (on a date) and a norm on one axis; if the post mixes them, chart what is comparable.
3. Chart titles and `h2`s state a finding. Headlines follow docs/HEADLINE_STYLE.md: sentence case, no idioms or questions.
4. `means` and `todo` are one sentence each; "What to do" follows from the post's own proposals or findings.
5. If a figure inside the original contradicts another, say so in your reply and use the figure the post uses most; do not silently pick.
6. Prefer `table` row selection over retyping: labels and values then match the original exactly.
