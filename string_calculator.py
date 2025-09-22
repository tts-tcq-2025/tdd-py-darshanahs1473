
class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        delimiter, rest = self._get_delimiter(numbers)
        values = self._parse_numbers(rest, delimiter)
        self._check_negatives(values)
        return sum(v for v in values if v <= 1000)

    def _get_delimiter(self, numbers: str):
        if numbers.startswith("//"):
            header, rest = numbers.split("\n", 1)
            delim = header.strip("/").strip("[]")
            return delim, rest
        return ",|\n", numbers

    def _parse_numbers(self, numbers: str, delimiter: str):
        import re
        return [int(x) for x in re.split(delimiter, numbers) if x]

    def _check_negatives(self, values: list[int]):
        negs = [v for v in values if v < 0]
        if negs:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negs))}")
