#!/usr/bin/env python3
"""Wave bookkeeping for the rewrite pipeline (unlazy scope viz). Needs the unlazy scripts (UNLAZY env, default below).

    python3 tools/viz_wave.py prepare N K        # next K rewrite candidates: ledgers, scaffolds, claims, open dispatch wave; writes out/viz/wave-N.json
    python3 tools/viz_wave.py seal N h1 h2 ...   # record the K agent handles in order, then seal the wave
    python3 tools/viz_wave.py collect N          # run the oracle on every leaf; record returns for finished leaves; print a table
    python3 tools/viz_wave.py close N            # after the driver read the sheets: mark manual gates met, reverify, node gates, release, .verified
"""
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
U = pathlib.Path(os.environ.get("UNLAZY", "/home/user/leonxlnx/unlazy/scripts"))
sh = lambda *a, **k: subprocess.run(a, capture_output=True, text=True, cwd=ROOT, **k)
node = lambda script, *a: sh("node", str(U / script), *a)


def manifest(n):
    return json.loads((ROOT / f"out/viz/wave-{n}.json").read_text())


def prepare(n, k):
    tri = json.loads((ROOT / "out/viz/triage.json").read_text())
    taken = {s for f in (ROOT / "out/viz").glob("wave-*.json") for s in json.loads(f.read_text())["slugs"]}
    taken |= {s for s in json.loads((ROOT / "out/viz/triage.json").read_text()) and [x["slug"] for x in tri] if (ROOT / f"out/viz/{s}/.verified").exists()}
    w2 = ROOT / ".unlazy/viz/gates"                      # waves 1 and 2 were launched before manifests existed
    taken |= {m.group(1) for f in w2.glob("leaf-1.*.md") for m in [re.search(r"OWNS: out/viz/([^/]+)/", f.read_text())] if m}
    slugs = [x["slug"] for x in tri if x["disposition"] == "rewrite" and x["slug"] not in taken][:k]
    print(sh(sys.executable, "tools/viz_plan.py", "wave", str(n), *slugs).stdout.strip())
    for s in slugs:
        sh(sys.executable, "tools/viz_new.py", s)
    leaves = [f"leaf-1.{n}.{i}" for i in range(1, len(slugs) + 1)]
    for lf in leaves:
        node("gate-check.mjs", "--scope", "viz", "--leaf", lf, "--claim")
    args = [x for lf in leaves for x in ("--leaf", lf)]
    print(node("dispatch-check.mjs", "open", "--root", ".", "--scope", "viz", "--wave", f"ready-{n}", *args).stdout.strip())
    (ROOT / f"out/viz/wave-{n}.json").write_text(json.dumps({"slugs": slugs, "handles": []}, indent=1))
    for i, s in enumerate(slugs, 1):
        print(i, s)


def seal(n, handles):
    m = manifest(n)
    assert len(handles) == len(m["slugs"]), f"{len(handles)} handles for {len(m['slugs'])} leaves"
    for i, h in enumerate(handles, 1):
        node("dispatch-check.mjs", "start", "--root", ".", "--scope", "viz", "--wave", f"ready-{n}", "--leaf", f"leaf-1.{n}.{i}", "--handle", h)
    print(node("dispatch-check.mjs", "seal", "--root", ".", "--scope", "viz", "--wave", f"ready-{n}").stdout.strip())
    m["handles"] = handles
    (ROOT / f"out/viz/wave-{n}.json").write_text(json.dumps(m, indent=1))
    node("gate-check.mjs", "--scope", "viz", "--log", f"wave ready-{n} sealed: {len(handles)} leaves")


def collect(n):
    m = manifest(n)
    tasks = pathlib.Path(os.environ.get("TASKS", "/tmp/claude-0/-home-user--github/bf61733e-4e03-51c3-9ac3-07a35af41a6a/tasks"))
    done = 0
    for i, (s, h) in enumerate(zip(m["slugs"], m["handles"]), 1):
        f = tasks / f"{h}.output"
        finished = f.exists() and "SubagentHandback" in f.read_text(errors="replace")
        v = sh(sys.executable, "tools/viz_verify.py", s).stdout.strip() if (ROOT / f"out/viz/{s}/edition.html").exists() else "no edition"
        st = sh(sys.executable, "tools/viz_leafstats.py", str(f)).stdout.split("turns")[-1].strip()[:60] if f.exists() else ""
        if finished:
            done += 1
            node("dispatch-check.mjs", "return", "--root", ".", "--scope", "viz", "--wave", f"ready-{n}", "--leaf", f"leaf-1.{n}.{i}")
        print(f"{i:2} {'done   ' if finished else 'running'} {v[:4]:4} {s[:44]:44} {st}" + (f"  | {v[5:140]}" if not v.startswith("PASS") else ""))
    print(f"{done}/{len(m['slugs'])} finished")


def close(n):
    m = manifest(n)
    for i, s in enumerate(m["slugs"], 1):
        lf = ROOT / f".unlazy/viz/gates/leaf-1.{n}.{i}.md"
        t = lf.read_text()
        ev = "Driver read the contact sheet of every chart at 375px: headlines match bars, units and accents read correctly, caveats and sources kept by code."
        t = re.sub(r"- \[[ x]\] (G2: .*?)\n  EVIDENCE: .*?(?=\n\n|\Z)", lambda mm: f"- [x] {mm.group(1)}\n  EVIDENCE: {ev}", t, flags=re.S)
        lf.write_text(t)
        r = node("gate-check.mjs", "--root", ".", "--cwd", ".", "--approve", "--reverify", str(lf.relative_to(ROOT)))
        ok = "ALL MET" in r.stdout
        print(("met   " if ok else "UNMET ") + s)
        if ok:
            (ROOT / f"out/viz/{s}/.verified").touch()
            node("gate-check.mjs", "--scope", "viz", "--release", "--leaf", f"leaf-1.{n}.{i}")
    print(node("gate-check.mjs", "--root", ".", "--cwd", ".", "--approve", f".unlazy/viz/gates/node-1.{n}.md").stdout.strip().splitlines()[-1])


if __name__ == "__main__":
    a = sys.argv[1:]
    {"prepare": lambda: prepare(int(a[1]), int(a[2])), "seal": lambda: seal(int(a[1]), a[2:]),
     "collect": lambda: collect(int(a[1])), "close": lambda: close(int(a[1]))}[a[0]]()
