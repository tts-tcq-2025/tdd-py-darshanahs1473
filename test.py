import pytest
from calculator import Add

@pytest.mark.parametrize(
    "expr, expected",
    [
        ("", 0),
        ("1", 1),
        ("1,2", 3),
        ("1,2,3,4", 10),
        ("1\n2,3", 6),
        ("//;\n1;2", 3),
        ("//[***]\n1***2***3", 6),
        ("2,1001", 2),
    ]
)
def test_valid_expressions(expr, expected):
    assert Add(expr) == expected

def test_negatives_raise():
    with pytest.raises(ValueError) as e:
        Add("1,-2,-3")
    msg = str(e.value)
    assert "negatives not allowed" in msg
    assert "-2" in msg
    assert "-3" in msg
