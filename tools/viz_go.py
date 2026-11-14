#!/usr/bin/env python3
"""One command for a leaf: render out/viz/<slug>/spec.json, then run the oracle. Prints PASS or the fixes needed.

    python3 tools/viz_go.py <slug>
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
slug = sys.argv[1]
r = subprocess.run([sys.executable, str(ROOT / "tools/viz_render.py"), slug], capture_output=True, text=True, cwd=ROOT)
if r.returncode:
    print(r.stderr.strip() or r.stdout.strip())
    sys.exit(1)
v = subprocess.run([sys.executable, str(ROOT / "tools/viz_verify.py"), slug], capture_output=True, text=True, cwd=ROOT)
line = (v.stdout or v.stderr).strip()
if v.returncode == 0:
    print(line)
else:
    body = line.split(": ", 1)[1] if ": " in line else line
    print("FAIL " + slug + ":\n  - " + "\n  - ".join(body.split(" | ")))
    sys.exit(1)
