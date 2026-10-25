"""tools/units_in_header.py on synthetic tables (no archive posts read)."""
import units_in_header as u


def tbl(head, cells, first="Item"):
    rows = "".join(f"<tr><td>r{i}</td><td>{c}</td></tr>" for i, c in enumerate(cells))
    return f"<tr><th>{first}</th><th>{head}</th></tr>{rows}"


def test_text_strips_tags_and_unescapes():
    assert u.text(" <b>&#8377;5&nbsp;cr</b> ") == "₹5\xa0cr"


def test_units_in_basic():
    assert u.units_in("US$ 14.18 bn") == {"us$", "bn"}
    assert u.units_in("12.5%") == {"%"}
    assert u.units_in("no unit here 42") == set()


def test_units_prefer_longest_match():
    """The UNITS comment says longest-first so 'US$ million' beats 'US$';
    the same must hold for 'MTPA' vs 'MT' and 'MWh' vs 'MW'."""
    assert u.units_in("73,000 MTPA") == {"mtpa"}
    assert u.units_in("5 ktpa") == {"ktpa"}
    assert u.units_in("120 MWh") == {"mwh"}
    assert u.units_in("US$ million") == {"us$ million"}


def test_audit_flags_majority_unit_not_in_header():
    viol, nrows = u.audit_table(tbl("Value", ["₹1,200 cr", "₹300 cr", "₹45 cr", "n/a"]))
    assert nrows == 5
    assert sorted(v[2] for v in viol) == ["cr", "₹"]
    assert all(v[0] == 1 and v[1] == "Value" and v[3] == 3 and v[4] == 3 for v in viol)


def test_audit_skips_unit_already_in_header():
    assert u.audit_table(tbl("Value, ₹ cr", ["₹1,200 cr", "₹300 cr", "₹45 cr"]))[0] == []


def test_audit_ignores_minority_and_mixed_units():
    assert u.audit_table(tbl("Value", ["12%", "5", "7", "9"]))[0] == []     # 1/4 < 50%
    assert u.audit_table(tbl("Value", ["$5", "€6", "₹7", "8"]))[0] == []


def test_audit_ignores_prose_and_short_columns():
    prose = ["about ₹5 cr mostly from the state", "roughly ₹2 cr in grants this year",
             "₹9 cr spread over three years"]
    assert u.audit_table(tbl("Note", prose))[0] == []
    assert u.audit_table(tbl("Value", ["5%", "6%"]))[0] == []                 # < 3 values
    assert u.audit_table("<tr><td>1</td></tr>") == ([], 0)


def test_audit_requires_numeric_column():
    assert u.audit_table(tbl("Status", ["approved %", "pending %", "done %", "1 %"]))[0] == []
