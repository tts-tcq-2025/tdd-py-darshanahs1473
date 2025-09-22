from calculator import Add

def test_valid_expressions():
    assert Add("") == 0
    assert Add("1") == 1
    assert Add("1,2") == 3
    assert Add("1,2,3,4") == 10
    assert Add("1\n2,3") == 6
    assert Add("//;\n1;2") == 3
    assert Add("//[***]\n1***2***3") == 6
    assert Add("2,1001") == 2

def test_negatives_raise():
    try:
        Add("1,-2,-3")
    except ValueError as e:
        msg = str(e)
        assert "negatives not allowed" in msg
        assert "-2" in msg
        assert "-3" in msg
    else:
        assert False, "Expected ValueError for negatives"

if __name__ == "__main__":
    test_valid_expressions()
    test_negatives_raise()
    print("All tests passed!")
