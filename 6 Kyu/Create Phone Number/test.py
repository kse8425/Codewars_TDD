from solution import create_phone_number, join_number


def test_create_phone_number():
    assert create_phone_number([0, 2, 3, 4, 5, 6, 7, 8, 9, 2]) == "(023) 456-7892"
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 2]) == "(123) 456-7892"


def test_join_number():
    assert join_number([1, 2, 4]) == '124'
