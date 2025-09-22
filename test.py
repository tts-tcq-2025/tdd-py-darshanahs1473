import pytest
from string_calculator import StringCalculator


@pytest.fixture
def calc():
return StringCalculator()


@pytest.mark.parametrize("input_str, expected", [
("", 0),
("1", 1),
("1,2", 3),
("1,2,3,4", 10),
("1\n2,3", 6),
("//;\n1;2", 3),
("2,1001", 2),
("//[***]\n1***2***3", 6),
])
def test_valid_cases(calc, input_str, expected):
assert calc.add(input_str) == expected




def test_negatives_raise(calc):
with pytest.raises(ValueError) as excinfo:
calc.add("1,-2,-3,4")
msg = str(excinfo.value)
assert "negatives not allowed" in msg
assert "-2" in msg
assert "-3" in msg

if __name__ == "__main__":
unittest.main()
