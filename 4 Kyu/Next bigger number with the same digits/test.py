from solution import next_bigger, combine_num, best_practices


def test_next_bigger():
    assert next_bigger(12) == 21
    assert next_bigger(21) == -1
    assert next_bigger(2017) == 2071
    assert next_bigger(414) == 441
    assert next_bigger(144) == 414


def test_next_bigger_xx():
    assert next_bigger(2087) == 2708


def test_combine_num():
    assert combine_num(123) == [123, 132, 213, 231, 312, 321]


def test_best_practices():
    assert best_practices(2087) == 2708
