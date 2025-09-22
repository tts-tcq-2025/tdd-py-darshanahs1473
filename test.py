import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
def setUp(self):
self.calc = StringCalculator()


def test_empty_string_returns_zero(self):
self.assertEqual(self.calc.add(""), 0)


def test_single_number_returns_value(self):
self.assertEqual(self.calc.add("1"), 1)


def test_two_numbers_comma(self):
self.assertEqual(self.calc.add("1,2"), 3)


def test_unknown_amount_of_numbers(self):
self.assertEqual(self.calc.add("1,2,3,4"), 10)


def test_newline_and_comma(self):
self.assertEqual(self.calc.add("1\n2,3"), 6)


def test_custom_single_char_delimiter(self):
self.assertEqual(self.calc.add("//;\n1;2"), 3)


def test_ignore_large_numbers(self):
self.assertEqual(self.calc.add("2,1001"), 2)


def test_negatives_raise(self):
with self.assertRaises(ValueError) as cm:
self.calc.add("1,-2,-3,4")
msg = str(cm.exception)
self.assertIn("negatives not allowed", msg)
self.assertIn("-2", msg)
self.assertIn("-3", msg)


def test_multi_char_delimiter(self):
self.assertEqual(self.calc.add("//[***]\n1***2***3"), 6)


if __name__ == "__main__":
unittest.main()
