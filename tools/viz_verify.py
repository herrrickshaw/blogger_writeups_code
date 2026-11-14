#!/usr/bin/env python3
"""Acceptance oracle for a visual-first edition (docs/VISUAL_STORY_STYLE.md).

    python3 tools/viz_verify.py <slug>                 # checks out/update-2026-11-15-<slug>.html against posts/<slug>.html
    python3 tools/viz_verify.py <slug> --edition FILE
    python3 tools/viz_verify.py --self-test            # runs the oracle on a known-good and known-bad pair

Prints "PASS <slug>" and exits 0, or "FAIL <slug>: <reasons>" and exits 1. Nothing else prints PASS.

What it proves (each is measured, none is taken from the author):
  frame      the edition starts with the live post's head (+ optional hero figure) and accessibility/translate block
             and ends with its tail, byte for byte (title, standfirst, kicker, sources card, related links, disclaimer)
  structure  one top line of 1-3 bullets that each open with a big number; 3-4 insight sections, each with a
             takeaway h2, a chart, and exactly two sentences ("What it means" / "What to do")
  charts     every chart title is 90 characters or fewer and states a finding (has a number or 7+ words)
  numbers    every number in the new text is in the original post's text, or is declared in
             out/viz/<slug>/derived.json as arithmetic on original numbers ("190": "570/3") or as a counted
             item ("7": "count: seven countries listed in the table"); counted items are listed for review
  coverage   at least 3 of the original's 5 most repeated numbers survive; the original's caveat section and
             "Updated <date>" notes survive; every external link in the original body survives
  size       the new text is 12% to 85% of the original body
  safety     no script, iframe or old-domain link in the new text
  phone      at 375px: page not wider than the screen, no chart label under 9.5px, no table that needs swiping,
             at most 2 paragraphs over 90 words (tools/mobile_audit.js)
Gaps this cannot close: it cannot tell whether a chart type fits the data or whether a headline is fair. Those are
the manual gate in each ledger (read the rendered 375px screenshot)."""
import ast
import html as _html
import json
import operator
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from viz_frame import numbers, split, visible  # noqa: E402

DATE = "2026-11-15"
OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Pow: operator.pow}


def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.BinOp) and type(node.op) in OPS:
        return OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -_eval(node.operand)
    raise ValueError("only + - * / ** and numbers are allowed")


def derived_ok(claimed, expr, orig_nums):
    """Return (ok, manual, why). Arithmetic must use only original numbers and reproduce the claim."""
    if expr.startswith("count:"):
        return (bool(expr[6:].strip()), True, "empty count note")
    try:
        tree = ast.parse(expr, mode="eval")
        value = _eval(tree)
    except Exception as e:  # noqa: BLE001
        return False, False, f"bad expression {expr!r}: {e}"
    operands = {str(n.value) if isinstance(n.value, float) and not float(n.value).is_integer() else str(int(n.value))
                for n in ast.walk(tree) if isinstance(n, ast.Constant)}
    stray = {o for o in operands if o not in orig_nums}
    if stray:
        return False, False, f"{expr!r} uses numbers not in the original: {sorted(stray)}"
    c = float(claimed.replace(",", ""))
    if not any(abs(round(value, d) - c) < 1e-9 for d in (0, 1, 2, 3)) and abs(value - c) > 0.005 * max(1, abs(c)):
        return False, False, f"{expr!r} = {value:g}, not {claimed}"
    return True, False, ""


def external_links(html):
    return {h for h in re.findall(r'href="(https?://[^"#]+)', html) if "blog.vertistratsolution.com" not in h}


def mobile(path):
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as t:
        out = t.name
    r = subprocess.run(["node", str(ROOT / "tools/mobile_audit.js"), str(path), "--json", out], capture_output=True, text=True, cwd=ROOT)
    if r.returncode:
        return None, r.stderr.strip()[:200]
    return json.loads(pathlib.Path(out).read_text())[0], ""


def verify(slug, edition=None, quiet=False):
    errs, manual = [], []
    orig_path = ROOT / f"posts/{slug}.html"
    ed_path = pathlib.Path(edition) if edition else ROOT / f"out/update-{DATE}-{slug}.html"
    if not orig_path.exists():
        return [f"no live post posts/{slug}.html"], manual
    if not ed_path.exists():
        return [f"no edition {ed_path.relative_to(ROOT) if ed_path.is_relative_to(ROOT) else ed_path}"], manual
    orig, ed = orig_path.read_text(encoding="utf-8"), ed_path.read_text(encoding="utf-8")
    fr = split(orig)
    if not fr:
        return ["live post does not have the standard frame (tools/viz_frame.py)"], manual

    back = fr.tail
    front = next((f for f in (fr.head + fr.lead + fr.mid, fr.head + fr.mid) if ed.startswith(f)), None)
    if front is None:
        errs.append("frame: the edition does not start with the live head and accessibility/translate block, byte for byte")
    if not ed.endswith(back):
        errs.append("frame: the edition does not end with the live tail, byte for byte")
    if errs:
        return errs, manual
    mid = ed[len(front):len(ed) - len(back)]
    new_text, old_body = visible(mid), visible(fr.body)

    # ---- structure ----
    tops = re.findall(r'<div class="xv-top">.*?</div>', mid, re.S)
    if len(tops) != 1:
        errs.append(f"structure: need exactly one top line, found {len(tops)}")
    else:
        lis = re.findall(r"<li>(.*?)</li>", tops[0], re.S)
        if not 1 <= len(lis) <= 3 or not all('class="xv-k"' in li for li in lis):
            errs.append("structure: top line needs 1-3 bullets, each opening with a big number (class xv-k)")
    secs = re.findall(r'<section class="xv-sec">(.*?)</section>', mid, re.S)
    if not 3 <= len(secs) <= 4:
        errs.append(f"structure: need 3 or 4 insight sections, found {len(secs)}")
    for i, s in enumerate(secs, 1):
        if not re.search(r"<h2[^>]*>.+?</h2>", s, re.S):
            errs.append(f"structure: section {i} has no h2")
        if not (re.search(r'<figure class="xv"', s) or 'class="xv-flow"' in s):
            errs.append(f"structure: section {i} has no chart")
        so = re.findall(r'<div class="xv-so"><p><b>What it means:</b> (.+?)</p><p><b>What to do:</b> (.+?)</p></div>', s, re.S)
        if len(so) != 1:
            errs.append(f"structure: section {i} must end with one What it means / What to do pair")
        else:
            for part in so[0]:
                t = visible(part)
                if not t.endswith(".") or re.search(r"\.\s+[A-Z]", t):
                    errs.append(f"structure: section {i} text is not exactly one sentence: {t[:60]!r}")
    titles = [visible(t) for t in re.findall(r'class="xv-t"[^>]*>(.*?)</span>', mid, re.S)]
    for t in titles:
        if len(t) > 90:
            errs.append(f"charts: title over 90 characters: {t[:50]!r}")
        if not re.search(r"\d", t) and len(t.split()) < 7:
            errs.append(f"charts: title does not state a finding: {t!r}")

    # ---- numbers ----
    orig_nums = numbers(visible(orig))
    new_nums = numbers(new_text)
    d_path = ROOT / f"out/viz/{slug}/derived.json"
    derived = json.loads(d_path.read_text()) if d_path.exists() else {}
    declared = set()
    for claim, expr in derived.items():
        ok, is_manual, why = derived_ok(claim, expr, orig_nums)
        if not ok:
            errs.append(f"numbers: derived {claim!r}: {why}")
        else:
            declared.add(next(iter(numbers(claim)), claim))
            if is_manual:
                manual.append(f"{claim} = {expr}")
    stray = sorted(n for n in new_nums - orig_nums - declared if not re.fullmatch(r"20\d\d|15", n) or n not in numbers(DATE))
    stray = [n for n in stray if n not in {"2026", "15"} or n in new_nums - orig_nums - declared and False]
    if stray:
        errs.append(f"numbers: not in the original post and not declared in out/viz/{slug}/derived.json: {stray[:12]}")

    # ---- coverage ----
    freq = {}
    for m in re.finditer(r"(?<![\w.])\d[\d,]*(?:\.\d+)?", old_body):
        t = next(iter(numbers(m.group(0))))
        if not re.fullmatch(r"(19|20)\d\d", t) and (len(t) > 1 or "." in t):
            freq[t] = freq.get(t, 0) + 1
    top5 = [t for t, _ in sorted(freq.items(), key=lambda kv: -kv[1])[:5]]
    kept = [t for t in top5 if t in new_nums]
    if len(top5) >= 3 and len(kept) < min(3, len(top5)):
        errs.append(f"coverage: only {len(kept)} of the original's top numbers {top5} survive")
    if re.search(r"(?:could|does|did) not establish|not established", old_body, re.I) and not re.search(r"establish", new_text, re.I):
        errs.append("coverage: the original's 'what this could not establish' caveat is missing")
    for d in set(re.findall(r"Updated \d{1,2} [A-Z][a-z]+ 20\d\d", old_body)):
        if d not in new_text:
            errs.append(f"coverage: the original's note {d!r} is missing")
    lost = sorted(external_links(fr.body) - external_links(mid) - external_links(back))
    if lost:
        errs.append(f"coverage: {len(lost)} source link(s) from the original body are missing, e.g. {lost[0]}")
    ratio = len(new_text.split()) / max(1, len(old_body.split()))
    if not 0.12 <= ratio <= 0.85:
        errs.append(f"size: new text is {ratio:.0%} of the original body (allowed 12% to 85%)")

    # ---- safety ----
    if re.search(r"<script|<iframe", mid, re.I):
        errs.append("safety: script or iframe in the new text")
    if "masaladeutsch.blogspot.com" in mid:
        errs.append("safety: old-domain link")

    # ---- phone ----
    m, why = mobile(ed_path)
    if m is None:
        errs.append(f"phone: audit failed to run: {why}")
    else:
        if m["wide"]:
            errs.append(f"phone: page is {m['pageWidth']}px wide at 375px")
        if m["smallCharts"]:
            errs.append(f"phone: {m['smallCharts']} chart(s) with labels under 9.5px")
        if m["swipeTables"]:
            errs.append(f"phone: {m['swipeTables']} table(s) need sideways swiping; put them in numbers()")
        if m["longParas"] > 2:
            errs.append(f"phone: {m['longParas']} paragraphs over 90 words (allowed 2, the sources card)")
    return errs, manual


def self_test():
    """Known-good: the blending pilot. Known-bad: the same file with an invented number and a broken frame."""
    slug = "blending-on-budget-energy-density-and"
    good = ROOT / f"out/update-{DATE}-{slug}.html"
    errs, _ = verify(slug, good)
    assert not errs, f"the known-good pilot failed: {errs}"
    bad = good.read_text(encoding="utf-8").replace("<h1", "<h1 data-x=1", 1)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as t:
        t.write(bad)
    errs, _ = verify(slug, t.name)
    assert any("frame" in e for e in errs), errs
    bad2 = good.read_text(encoding="utf-8").replace("3.9% vs 6.9%", "3.8% vs 6.9%", 1)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as t:
        t.write(bad2)
    errs, _ = verify(slug, t.name)
    assert any("numbers" in e and "3.8" in e for e in errs), errs
    print("self-test passed: known-good passes, invented number and broken frame are caught")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--self-test"]:
        self_test()
        sys.exit(0)
    if not a:
        sys.exit(__doc__)
    slug = a[0]
    ed = a[a.index("--edition") + 1] if "--edition" in a else None
    errs, manual = verify(slug, ed)
    if errs:
        print(f"FAIL {slug}: " + " | ".join(errs))
        sys.exit(1)
    print(f"PASS {slug}" + (f" (review counted items: {'; '.join(manual)})" if manual else ""))
