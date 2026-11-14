#!/usr/bin/env python3
"""Merge the retitle batches, check them, and point every local file at the new titles.

    python3 out/retitle/finalise.py          # from the repo root

1. batch1-4.tsv -> titles.tsv (live posts, applied by `blogger_api.py retitle`) and
   the <h1> of the unpublished hub posts (out/post-hub-*.html, read by phase2_stepA).
2. Checks every title: <= 90 characters, no banned words, no question, no second sentence,
   and every number in the new title appears in that post's own title/standfirst/headings.
3. Pending update files (out/update-*-<slug>.html) get the new <h1>, and phase1_titles.tsv
   the new titles, so a later publish cannot put an old title back.
4. Writes review.tsv (slug, old, new, characters) for reading the whole list.
Exit 1 if any check fails.
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
D = ROOT / "out/retitle"
sys.path.insert(0, str(ROOT / "tools"))
from blogger_api import set_h1  # noqa: E402

src = {}
for f in sorted(D.glob("batch*.jsonl")):
    for line in f.read_text().splitlines():
        r = json.loads(line)
        src[r["slug"]] = r
new = {}
for f in sorted(D.glob("batch*.tsv")):
    for line in f.read_text(encoding="utf-8").splitlines():
        if "\t" in line:
            s, t = line.split("\t", 1)
            new[s.strip()] = t.strip()

BANNED = r"\b(nobody|no one|actually|just|still|only|finally|anyway|really|you|your|we|our)\b"
WORDS = {"one": 1, "single": 1, "two": 2, "twice": 2, "double": 2, "both": 2, "pair": 2, "three": 3, "thrice": 3,
         "triple": 3, "four": 4, "quadruple": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
         "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
         "twenty": 20, "thirty-one": 31, "thirty": 30, "first": 1, "second": 2, "sixth": 6, "decade": 10}
def num(s):
    out = {n.replace(",", "") for n in re.findall(r"\d[\d,]*(?:\.\d+)?", s)}
    out |= {str(v) for w, v in WORDS.items() if re.search(r"\b" + w + r"\b", s, re.I)}
    return out
problems = []
missing = sorted(set(src) - set(new))
if missing:
    problems.append(f"no new title for {len(missing)}: {missing[:5]}")
for s, t in new.items():
    r = src.get(s)
    if not r:
        problems.append(f"{s}: not in the batches")
        continue
    why = []
    if len(t) > 90:
        why.append(f"{len(t)} chars")
    if re.search(BANNED, t, re.I):
        why.append("banned word " + re.search(BANNED, t, re.I).group(0))
    if "?" in t or re.search(r"\.\s+[A-Z]", t) or " — " in t:
        why.append("question/second sentence/dash")
    if t.count(":") > 1:
        why.append("two colons")
    seen = num(" ".join([r["title"], r["standfirst"], " ".join(r["sections"]), s]))
    extra = {n for n in num(t) if n not in seen and n.rstrip("0").rstrip(".") not in seen}
    if extra:
        why.append(f"number not in source: {sorted(extra)}")
    if why:
        problems.append(f"{s}: {t!r} -> {'; '.join(why)}")

live = {s: t for s, t in new.items() if src.get(s, {}).get("status") == "live"}
hubs = {s: t for s, t in new.items() if src.get(s, {}).get("status", "").startswith("hub")}
(D / "titles.tsv").write_text("".join(f"{s}\t{t}\n" for s, t in sorted(live.items())), encoding="utf-8")
(D / "review.tsv").write_text("slug\told\tnew\tchars\n" + "".join(
    f"{s}\t{src[s]['title']}\t{t}\t{len(t)}\n" for s, t in sorted(new.items()) if s in src), encoding="utf-8")

for s, t in hubs.items():
    f = ROOT / f"out/{s}.html"
    f.write_text(set_h1(f.read_text(encoding="utf-8"), t), encoding="utf-8")
touched = 0
for s, t in live.items():
    for f in ROOT.glob(f"out/update-*-{s}.html"):
        b = f.read_text(encoding="utf-8", errors="surrogateescape")
        nb = set_h1(b, t)
        if nb != b:
            f.write_text(nb, encoding="utf-8", errors="surrogateescape")
            touched += 1
p1 = ROOT / "out/gsc_index/phase1_titles.tsv"
rows = [l.split("\t", 1) for l in p1.read_text(encoding="utf-8").splitlines() if "\t" in l]
p1.write_text("".join(f"{s}\t{live.get(s, t)}\n" for s, t in rows), encoding="utf-8")

L = sorted(len(t) for t in new.values())
print(f"{len(live)} live titles -> titles.tsv; {len(hubs)} hub h1s set; {touched} pending update files retitled; "
      f"phase1_titles.tsv synced")
print(f"length: median {L[len(L) // 2]}, max {L[-1]}, over 80: {sum(l > 80 for l in L)}; "
      f"unchanged apart from case: {sum(t.lower() == src[s]['title'].lower() for s, t in new.items() if s in src)}")
for p in problems:
    print("CHECK", p)
sys.exit(1 if problems else 0)
