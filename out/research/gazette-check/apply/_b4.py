"""Shared helpers for gazette-check batch 4 (28 Oct 2026)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "factcheck-explainers" / "apply"))
import common
from common import load, rep, ROOT
common.NOTE = common.NOTE.replace("Updated 27 October 2026.", "Updated 28 October 2026.")
insert_note = common.insert_note
SRC = "the SansadSaar index of the archive.org Gazette of India collection"

def save(slug, t):
    out = ROOT / "out" / f"update-2026-10-28-{slug}.html"
    out.write_text(t, encoding="utf-8")
    print("wrote", out.name, len(t))
