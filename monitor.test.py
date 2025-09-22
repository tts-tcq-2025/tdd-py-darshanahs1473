def Add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ","
    if numbers.startswith("//"):
        end = numbers.find("\n")
        delim = numbers[2:end]
        if delim.startswith("[") and delim.endswith("]"):
            delimiter = delim[1:-1]
        else:
            delimiter = delim
        numbers = numbers[end + 1:]

    numbers = numbers.replace("\n", delimiter)
    list_num = [int(n) for n in numbers.split(delimiter) if n]

    negatives = [n for n in list_num if n < 0]
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

    return sum(n for n in list_num if n <= 1000)


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
