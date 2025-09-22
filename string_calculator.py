
import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter_pattern, rest = self._extract_delimiter(numbers)
        tokens = self._split_numbers(rest, delimiter_pattern)
        ints = self._to_ints(tokens)
        self._raise_if_negatives(ints)
        return sum(n for n in ints if n <= 1000)

    def _extract_delimiter(self, numbers: str):
        m = re.match(r"^//(\[.*?\]|.)\n(.*)$", numbers, re.S)
        if m:
            delim, rest = m.groups()
            if delim.startswith("[") and delim.endswith("]"):
                delim = delim[1:-1]
            return re.escape(delim), rest
        return r",|\n", numbers

    def _split_numbers(self, numbers: str, delimiter_pattern: str):
        return re.split(delimiter_pattern, numbers)

    def _to_ints(self, tokens):
        return [int(t) for t in tokens if t]

    def _raise_if_negatives(self, values):
        negatives = [n for n in values if n < 0]
        if negatives:
            raise ValueError("negatives not allowed: " + ", ".join(map(str, negatives)))
