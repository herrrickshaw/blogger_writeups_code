#!/usr/bin/env python3
"""Branch gate: the rewrite pipeline touched nothing it must not (posts/ and meta/ are snapshot outputs;
out/ drafts are the only writes). Compares the working tree to HEAD."""
import subprocess
import sys

r = subprocess.run(["git", "status", "--porcelain", "--", "posts", "meta", "tools", "templates", "theme"], capture_output=True, text=True)
changed = [l for l in r.stdout.splitlines() if l.strip()]
if changed:
    print("guard FAILED, changed outside out/:\n" + "\n".join(changed[:20]))
    sys.exit(1)
print("guard passed")
