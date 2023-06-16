from solution import Xbonacci, next_num


def test_next_num():
    assert next_num([1, 2], 2) == 3


def test_Xbonacci():
    assert Xbonacci([0, 1], 10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_n이_signature_길이보다_작을_때():
    assert Xbonacci([0, 1], 1) == [0]
    assert Xbonacci([0, 1], 0) == []
