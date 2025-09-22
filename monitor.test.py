def parse_delimiter(numbers: str):
    if numbers.startswith("//"):
        end = numbers.find("\n")
        delim = numbers[2:end]
        rest = numbers[end+1:]
        if delim.startswith("[") and delim.endswith("]"):
            delim = delim[1:-1]
        return delim, rest
    return ",", numbers

def parse_numbers(numbers: str, delimiter: str):
    numbers = numbers.replace("\n", delimiter)
    nums = [int(n) for n in numbers.split(delimiter) if n]
    negatives = [n for n in nums if n < 0]
    if negatives:
        raise ValueError("negatives not allowed: " + ", ".join(map(str, negatives)))
    return [n for n in nums if n <= 1000]

def Add(numbers: str) -> int:
    if not numbers:
        return 0
    delim, rest = parse_delimiter(numbers)
    nums = parse_numbers(rest, delim)
    return sum(nums)


# --- Tests ---
assert Add("") == 0
assert Add("1") == 1
assert Add("1,2") == 3
assert Add("1,2,3,4") == 10
assert Add("1\n2,3") == 6
assert Add("//;\n1;2") == 3
assert Add("//[***]\n1***2***3") == 6
assert Add("2,1001") == 2

try:
    Add("1,-2,-3")
except ValueError as e:
    msg = str(e)
    assert "negatives not allowed" in msg
    assert "-2" in msg
    assert "-3" in msg
else:
    assert False, "Expected ValueError for negatives"

print("All tests passed!")
