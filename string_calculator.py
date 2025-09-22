
import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if self._is_empty(numbers):
            return 0

        delimiter_pattern, rest = self._extract_delimiter(numbers)
        tokens = self._split_numbers(rest, delimiter_pattern)
        ints = self._to_ints(tokens)
        self._raise_if_negatives(ints)
        return self._sum_ignore_large(ints)

    # --- Small helpers ---

    def _is_empty(self, s: str) -> bool:
        return s == ""

    def _extract_delimiter(self, numbers: str):
        if self._has_custom_delimiter(numbers):
            return self._parse_custom_delimiter(numbers)
        return r",|\n", numbers

    def _has_custom_delimiter(self, numbers: str) -> bool:
        return numbers.startswith("//")

    def _parse_custom_delimiter(self, numbers: str):
        match = re.match(r"^//(\[.*?\]|.)\n(.*)$", numbers, re.S)
        if not match:
            return r",|\n", numbers
        delim, rest = match.groups()
        if delim.startswith("[") and delim.endswith("]"):
            delim = delim[1:-1]
        return re.escape(delim), rest

    def _split_numbers(self, numbers: str, delimiter_pattern: str):
        return re.split(delimiter_pattern, numbers)

    def _to_ints(self, tokens):
        return [int(t) for t in tokens if t]

    def _raise_if_negatives(self, values):
        negatives = [n for n in values if n < 0]
        if negatives:
            raise ValueError(
                "negatives not allowed: " + ", ".join(map(str, negatives))
            )

    def _sum_ignore_large(self, values):
        return sum(n for n in values if n <= 1000)
