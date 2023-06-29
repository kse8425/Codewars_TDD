from solution import persistence, multiple_digit


def test_persistence():
    assert persistence(39) == 3
    assert persistence(999) == 4
    assert persistence(25) == 2


def test_multiple_digit():
    assert multiple_digit(39) == 27
