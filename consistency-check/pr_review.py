#!/usr/bin/env python3
"""PR-time review pipeline for blogger_writeups_code.

Chains two independent, deterministic checks over a pull request's changed
files, run as sequential stages -- the same shape as an LLM prompt-chaining
pipeline (Stage A's output frames what Stage B looks for), but with no model
calls, no API key, and no per-PR cost:

  Stage 1 (static rules)  -- consistency-check/checks.py's STATIC_RULES,
                              run against every changed out/**/*.html draft.
                              This is the same check every post in this repo
                              has been hand-run against before publishing;
                              running it in CI just makes it automatic.
  Stage 2 (content-loss)  -- flags any changed posts/**/*.html or
                              out/**/*.html file that shrank by more than
                              --shrink-threshold percent versus its version
                              on the PR's base ref. This is the exact failure
                              mode CLAUDE.md documents from the 2026-08-07 WPI
                              incident (and the top-15-chemicals-for-import.html
                              regression this repo hit again on 2026-08-30):
                              a bad fetch or a bad edit silently drops real
                              content, and nothing catches it unless someone
                              happens to diff byte counts by hand.

Routing (stage 3) lives in the calling GitHub Actions workflow: it decides
whether to post a clean summary or a flagged one based on this script's exit
code and stdout. A future LLM-based stage (e.g. a tone/fact-check pass) could
be inserted into the same pipeline -- read this script's JSON output, add a
third stage -- without restructuring stages 1-2.

This script never writes to posts/, meta/, or the live blog, and never calls
tools/blogger_api.py. It only reads git history already present in the
checkout (git show against the PR's base/head refs) -- no network calls.
"""
import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from checks import STATIC_RULES, BLOCKER, SCRIPT_RE  # noqa: E402

_HAS_NODE = shutil.which("node") is not None


def _sh(*args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def changed_files(base_ref, head_ref):
    out = _sh("git", "diff", "--name-only", f"{base_ref}...{head_ref}")
    return [line for line in out.splitlines() if line]


def file_at(ref, path):
    try:
        return _sh("git", "show", f"{ref}:{path}")
    except subprocess.CalledProcessError:
        return None  # file didn't exist at this ref (new or deleted)


def node_check_for(body):
    """Replicates the manual `node -e "new Function(src)"` sweep this repo's
    posts have been checked with by hand all session -- STATIC_RULES'
    js-parses rule (r_scripts_parse) is a no-op unless the caller supplies
    this list itself; passing node_check=None (as a naive caller would)
    silently skips the one check most likely to catch a real BLOCKER.
    Returns the list of 1-based indices of scripts that fail to parse, or
    None if node isn't available (the rule then reports itself as skipped,
    same as it would for any other caller lacking node)."""
    if not _HAS_NODE:
        return None
    bad = []
    for i, m in enumerate(SCRIPT_RE.finditer(body), start=1):
        src = m.group(1)
        tag = m.group(0)
        if not src.strip() or re.search(r"\bsrc\s*=", tag):
            continue  # external <script src="...">, or empty -- nothing to parse
        proc = subprocess.run(
            ["node", "-e", "new Function(require('fs').readFileSync(0,'utf8'))"],
            input=src,
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            bad.append(i)
    return bad


def stage1_static_rules(head_ref, files):
    """Static rules only make sense on drafts, so this stage is scoped to
    out/**/*.html -- posts/ is a generated output (see CLAUDE.md rule 1),
    not something a PR should be hand-editing anyway."""
    results = []
    for f in files:
        if not (f.startswith("out/") and f.endswith(".html")):
            continue
        body = file_at(head_ref, f)
        if body is None:
            continue
        node_check = node_check_for(body)
        for name, sev, fn in STATIC_RULES:
            try:
                ok, detail = fn(body, node_check=node_check)
            except TypeError:
                ok, detail = fn(body)
            if not ok:
                results.append(
                    {"file": f, "rule": name, "severity": sev, "detail": detail}
                )
    return results


def stage2_content_loss(base_ref, head_ref, files, threshold_pct):
    """Covers both posts/ (a snapshot commit that silently truncated a live
    post) and out/ (a draft that got smaller than its previous revision on
    this same branch) -- the mechanism that produces bad data is the same
    either way: a fetch or edit that lost content without anyone noticing."""
    results = []
    for f in files:
        if not (
            (f.startswith("posts/") or f.startswith("out/")) and f.endswith(".html")
        ):
            continue
        before = file_at(base_ref, f)
        after = file_at(head_ref, f)
        if before is None or after is None or len(before) == 0:
            continue  # new or deleted file in this diff -- not a shrink
        before_len, after_len = len(before), len(after)
        drop_pct = (before_len - after_len) / before_len * 100
        if drop_pct >= threshold_pct:
            results.append(
                {
                    "file": f,
                    "before_bytes": before_len,
                    "after_bytes": after_len,
                    "drop_pct": round(drop_pct, 1),
                }
            )
    return results


def render_markdown(stage1, stage2):
    if not stage1 and not stage2:
        return (
            "Clean. No static-rule failures on changed `out/**` drafts, "
            "and no unexplained content shrinkage on changed `posts/**` or "
            "`out/**` files."
        )
    lines = []
    if stage1:
        lines.append("**Static rule failures (`out/**`):**\n")
        for r in stage1:
            lines.append(f"- **{r['severity']}** `{r['rule']}` in `{r['file']}`: {r['detail']}")
        lines.append("")
    if stage2:
        lines.append("**Possible content loss:**\n")
        for r in stage2:
            lines.append(
                f"- `{r['file']}`: {r['before_bytes']:,} → {r['after_bytes']:,} bytes "
                f"(−{r['drop_pct']}%) vs. the base branch — verify this isn't "
                f"unintended loss before merging (see `CLAUDE.md`'s WPI-incident note)"
            )
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base-ref", required=True)
    ap.add_argument("--head-ref", required=True)
    ap.add_argument(
        "--shrink-threshold",
        type=float,
        default=8.0,
        help=(
            "Flag a file if it lost at least this percent of its bytes (default 8). "
            "Calibrated against this repo's own CHANGELOG.md history: legitimate edits "
            "shrink posts by double digits too, so this is a nudge for a human to look, "
            "not a high-confidence signal on its own -- see the exit-code note below."
        ),
    )
    ap.add_argument("--json", action="store_true", help="Print raw JSON instead of Markdown")
    args = ap.parse_args()

    files = changed_files(args.base_ref, args.head_ref)
    stage1 = stage1_static_rules(args.head_ref, files)
    stage2 = stage2_content_loss(args.base_ref, args.head_ref, files, args.shrink_threshold)

    if args.json:
        print(json.dumps({"stage1_static_rules": stage1, "stage2_content_loss": stage2}, indent=2))
    else:
        print(render_markdown(stage1, stage2))

    # Only BLOCKER-severity static-rule failures fail the check ("reader sees
    # broken output" per checks.py's own severity docstring -- js-parses,
    # disclaimer-in-script, inverted-media-query, dark-vars-locked). MAJOR/MINOR
    # rule findings and content-loss are reported in the PR comment either way,
    # but don't fail CI: checking this repo's own CHANGELOG.md history, 144 of
    # 2,093 recorded changes shrank a post's byte count, many by double digits,
    # for entirely legitimate reasons -- a hard gate on that signal alone would
    # block real edits far more often than it would catch a real incident.
    blocking = [r for r in stage1 if r["severity"] == BLOCKER]
    sys.exit(1 if blocking else 0)


if __name__ == "__main__":
    main()
