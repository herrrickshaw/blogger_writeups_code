"""Every tool must byte-compile without SyntaxWarnings: on Python 3.12+ an invalid
escape such as "\\s" inside a normal string is a warning today and a SyntaxError in
a future release, so the index page builder would stop importing altogether."""
import pathlib
import warnings

ROOT = pathlib.Path(__file__).resolve().parent.parent


def test_build_index_page_compiles_without_invalid_escape_warning():
    src = (ROOT / "tools" / "build_index_page.py").read_text(encoding="utf-8")
    with warnings.catch_warnings():
        warnings.simplefilter("error", SyntaxWarning)
        compile(src, "build_index_page.py", "exec")  # raises SyntaxError on "\s"
