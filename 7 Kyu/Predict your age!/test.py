from solution import predict_age, multiply_itself, add_together, take_square_root, divide_by_two


def test_predict_age():
    assert predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86


def test_multiply_itself():
    assert multiply_itself([1, 2, 3]) == [1, 4, 9]


def test_add_together():
    assert add_together([1, 2, 3]) == 6


def test_take_square_root():
    assert take_square_root(4) == 2


def test_divide_by_two():
    assert divide_by_two(2) == 1
