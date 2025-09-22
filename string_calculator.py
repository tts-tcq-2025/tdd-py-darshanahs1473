def Add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ","
    if numbers.startswith("//"):
        end = numbers.find("\n")
        delimiter = numbers[2:end]
        numbers = numbers[end + 1:]

    numbers = numbers.replace("\n", delimiter)
    list_num = [int(n) for n in numbers.split(delimiter) if n]

    negatives = [n for n in list_num if n < 0]
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

    return sum(n for n in list_num if n <= 1000)
