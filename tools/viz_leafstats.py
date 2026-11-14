#!/usr/bin/env python3
"""Turns, output tokens and peak context per leaf agent, from the task transcripts.

    python3 tools/viz_leafstats.py <transcript.output> [...]      # prints one line per file
Transcripts are JSONL files under the session's tasks/ directory (agent output files)."""
import json
import sys

for f in sys.argv[1:]:
    turns = out = peak = ctx_sum = pngs = verifies = 0
    for line in open(f, encoding="utf-8", errors="replace"):
        try:
            m = json.loads(line).get("message") or {}
        except ValueError:
            continue
        u = m.get("usage") or {}
        if m.get("role") == "assistant" and u:
            turns += 1
            out += u.get("output_tokens", 0)
            c = u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
            peak, ctx_sum = max(peak, c), ctx_sum + c
        for b in (m.get("content") if isinstance(m.get("content"), list) else []):
            if b.get("type") == "tool_use":
                s = json.dumps(b.get("input", {}))
                verifies += "viz_go" in s
                pngs += s.endswith('.png"}') and b["name"] == "Read"
    print(f"{f.split('/')[-1][:20]:20} turns {turns:3} output {out:6,} peak-context {peak:7,} context-read-total {ctx_sum:9,} viz_go runs {verifies} png reads {pngs}")
