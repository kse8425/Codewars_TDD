from solution import find_outlier


def test_find_outlier():
    assert find_outlier([1, 2, 3]) == 2
    assert find_outlier([1, 2, 3, 5, 7, -1]) == 2
