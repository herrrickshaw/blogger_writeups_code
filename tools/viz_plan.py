#!/usr/bin/env python3
"""Generate the unlazy pipeline for the visual-first rewrite: .unlazy/viz/PLAN.md and one gate ledger per post.

    python3 tools/viz_plan.py init                      # PLAN.md + root GATES.md (writes nothing for posts)
    python3 tools/viz_plan.py wave N slug [slug ...]    # leaf ledgers for those posts, appended to the PLAN tree and table

Ledger gates are the oracle (tools/viz_verify.py) plus a manual reading gate. See docs/VIZ_LEAF_BRIEF.md."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
D = ROOT / ".unlazy/viz"

PLAN = """# Plan: visual-first edition of every live article

Scope: viz
Depth: tree 3
Mode: orchestrated

## Contract

- Interfaces: out/viz/<slug>/edition.html is a full post body = live head + [hero figure] + accessibility/translate block + new middle + live tail (tools/viz_frame.py); middle built with tools/exec_viz.py
- Ownership: each leaf owns out/viz/<slug>/** (the edition is out/viz/<slug>/edition.html), nothing else; posts/ and meta/ are never edited (CLAUDE.md rule 1)
- Dependencies: none between leaves; branch = one wave
- Host launch mode: Claude background Agents (the Dynamic Workflow tool needs the user's explicit opt-in)
- Wave policy: waves of up to 6 until the pass rate and cost per leaf are measured, then larger; every leaf in a wave launches before any result is read
- Toolchain: python3, node 22, Playwright Chromium (mobile_audit.js); run from the repo root; shell /bin/sh
- Conventions: docs/VISUAL_STORY_STYLE.md, docs/HEADLINE_STYLE.md, docs/VIZ_LEAF_BRIEF.md
- Manual review: the driver reads the 375px screenshot of every edition before it counts as VERIFIED

## Current contract inventory

Contract revision: 1.

| ID | Required outcome or constraint | Owner | Observing gate or manual review | Disposition | Revision |
|---|---|---|---|---|---|
| C1 | Every live article gets a visual-first edition, or a stated reason it does not (interactive, walkthrough, too little data, other template) | root | out/viz/triage.json; node-wave gates | ACTIVE | 1 |
| C2 | Each edition has a 1-3 bullet top line and 3-4 sections of takeaway headline, one chart, two sentences | leaves | G1 (viz_verify structure) | ACTIVE | 1 |
| C3 | Chart titles state the takeaway, 90 characters or fewer | leaves | G1 (viz_verify charts) | ACTIVE | 1 |
| C4 | Grey with one accent, no gridlines, no dense tables, no dual axis | leaves | G2 (manual, screenshot) | ACTIVE | 1 |
| C5 | Every number comes from the original post or declared arithmetic on it | leaves | G1 (viz_verify numbers) | ACTIVE | 1 |
| C6 | Caveats, dated update notes, sources, related links and disclaimer survive | leaves | G1 (viz_verify coverage, frame) | ACTIVE | 1 |
| C7 | Phone: no sideways page scroll, labels readable, no open wide table | leaves | G1 (viz_verify phone) | ACTIVE | 1 |
| C8 | Nothing is published to the live blog by this pipeline; editions stay in out/ for the owner's reviewed publish | root | manual: no blogger_api call in this pipeline | ACTIVE | 1 |
| C9 | The oracle itself catches an invented number and a broken frame | root | GATES.md R1 | ACTIVE | 1 |

## State vocabulary

Leaf state is exactly one of WAITING, READY, IN-FLIGHT, VERIFIED, ABANDONED. Branch state is OPEN, VERIFIED or ABANDONED.

## Tree

- 1 visual-first rewrite ........ GATES.md

## Leaf dispatch table

| Leaf | Owns | Needs | Tier | Planned wave | State |
|---|---|---|---|---|---|

## Status log

Append events with gate-check.mjs --scope viz --log "...".
"""

ROOT_GATES = """# Gates: visual-first rewrite, root

Scope: the oracle works, and every wave branch is verified

- [ ] R1: the oracle passes a known-good edition and rejects an invented number and a broken frame
  CHECK: python3 tools/viz_verify.py --self-test
  EXPECT: self-test passed
  EVIDENCE: pending
"""

LEAF = """# Gates: viz {slug}

OWNS: out/viz/{slug}/**

Scope: a visual-first edition of {slug} that passes the oracle and reads correctly at 375px

- [ ] G1: the edition passes frame, structure, charts, numbers, coverage, size, safety and phone checks
  CHECK: python3 tools/viz_verify.py {slug}
  EXPECT: /^PASS {slug}/m
  EVIDENCE: pending

- [ ] G2: the driver read the 375px screenshot of every section: each chart type fits its data, each headline is supported by its chart, and no argument of the original was reversed or lost
  EVIDENCE: pending
"""


def init():
    D.mkdir(parents=True, exist_ok=True)
    (D / "gates").mkdir(exist_ok=True)
    if not (D / "PLAN.md").exists():
        (D / "PLAN.md").write_text(PLAN)
    (D / "GATES.md").write_text(ROOT_GATES)
    print("wrote .unlazy/viz/PLAN.md and GATES.md")


def wave(n, slugs):
    plan = (D / "PLAN.md").read_text()
    tree_add, rows = [], []
    for i, s in enumerate(slugs, 1):
        lid = f"1.{n}.{i}"
        (D / "gates" / f"leaf-{lid}.md").write_text(LEAF.format(slug=s))
        tree_add.append(f"  - 1.{n} wave {n} ........ gates/node-1.{n}.md" if i == 1 else None)
        tree_add.append(f"    - {lid} {s} ...... gates/leaf-{lid}.md")
        rows.append(f"| {lid} | out/viz/{s}/** | - | judgment | {n} | READY |")
    tree_add = [t for t in tree_add if t]
    plan = plan.replace("- 1 visual-first rewrite ........ GATES.md\n", "- 1 visual-first rewrite ........ GATES.md\n" + "\n".join(tree_add) + "\n", 1)
    plan = plan.replace("|---|---|---|---|---|---|\n\n## Status log", "|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n\n## Status log", 1)
    (D / "PLAN.md").write_text(plan)
    kids = " ".join(f".unlazy/viz/gates/leaf-1.{n}.{i}.md" for i in range(1, len(slugs) + 1))
    (D / "gates" / f"node-1.{n}.md").write_text(
        f"# Gates: wave {n} integration\n\nScope: integrate wave {n} leaves into one verified result\n\n"
        f"- [ ] N1: every leaf in the wave is reverified from its exact ledger\n"
        f"  CHECK: node /home/user/leonxlnx/unlazy/scripts/gate-check.mjs --root . --cwd . --reverify --jobs 1 {kids}\n"
        f"  EXPECT: ALL MET\n  EVIDENCE: pending\n\n"
        f"- [ ] N2: no edition in the wave is published or edited outside out/ (posts/ and meta/ unchanged)\n"
        f"  CHECK: python3 tools/viz_guard.py\n  EXPECT: guard passed\n  EVIDENCE: pending\n")
    print(f"wave {n}: {len(slugs)} leaf ledgers")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["init"]:
        init()
    elif a[:1] == ["wave"]:
        wave(int(a[1]), a[2:])
    else:
        sys.exit(__doc__)
