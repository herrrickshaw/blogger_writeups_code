"""tools/svg_label_fit.py geometry with hand-computed widths."""
import pytest

import svg_label_fit as f


def test_text_width_hand_computed():
    # "10" = 2 digits * 0.50 * 10px = 10.0; bold bump 1.08
    assert f.text_width("10", 10, bold=False) == pytest.approx(10.0)
    assert f.text_width("10", 10) == pytest.approx(10.8)
    # an entity counts as one default-width char
    assert f.text_width("&amp;", 10, bold=False) == pytest.approx(5.2)


def test_wrap_text_lines_greedy_and_never_drops_words():
    lines = f.wrap_text_lines("aaa bbb ccc", max_width=40, font_size=10)  # each word 15.6, pair 35.2
    assert lines == ["aaa bbb", "ccc"]
    assert f.wrap_text_lines("supercalifragilistic", 5, 10) == ["supercalifragilistic"]


def test_wrap_svg_text_tspans():
    svg, n = f.wrap_svg_text(50, 20, "aaa bbb ccc", 40, 10)
    assert n == 2
    assert svg.count("<tspan") == 2 and 'dy="0"' in svg and 'dy="12.5"' in svg


def test_fit_outside_when_room_right():
    r = f.fit_value_label("10", 0, 50, 0, 200, "right")
    assert r == {"x": 56.0, "anchor": "start", "font_size": 11.0, "inside": False}


def test_fit_inside_when_no_room_outside():
    r = f.fit_value_label("10", 0, 190, 0, 200, "right")       # 10px outside, label ~11.9
    assert r["inside"] and r["anchor"] == "end" and r["x"] == 186.0


def test_fit_left_direction_mirrors():
    r = f.fit_value_label("10", 100, 150, 0, 200, "left")
    assert r == {"x": 94.0, "anchor": "end", "font_size": 11.0, "inside": False}
    r = f.fit_value_label("10", 5, 150, 0, 200, "left")
    assert r["inside"] and r["anchor"] == "start" and r["x"] == 9.0


def test_fit_shrinks_but_not_below_min_font():
    r = f.fit_value_label("1,234,567", 0, 20, 0, 40, "right")
    assert f.MIN_FONT_SIZE <= r["font_size"] < 11.0


@pytest.mark.xfail(strict=True, reason="known: MIN_FONT_SIZE floor lets a label overflow; "
                   "module docstring says nothing it produces can overflow (needs a design decision)")
def test_label_never_overflows_canvas():
    r = f.fit_value_label("1,234,567", 0, 20, 0, 40, "right")
    width = f.text_width("1,234,567", r["font_size"])
    if r["inside"]:
        assert width <= 20
    else:
        assert r["x"] + width <= 40
