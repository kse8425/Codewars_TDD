import pytest

from solution import snail, Snail


def test_snail():
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert snail(array) == expected
    assert snail([None]) == []


@pytest.fixture
def _snail():
    arr = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    return Snail(arr)


def test_go_up(_snail):
    s = _snail
    s.go_up()
    assert s.result == [7, 4, 1]
    assert s.matrix == [[2, 3], [5, 6], [8, 9]]


def test_go_left(_snail):
    s = _snail
    s.go_left()
    assert s.result == [9, 8, 7]
    assert s.matrix == [[1, 2, 3], [4, 5, 6]]


def test_go_down(_snail):
    s = _snail
    s.go_down()
    assert s.result == [3, 6, 9]
    assert s.matrix == [[1, 2], [4, 5], [7, 8]]


def test_go_right(_snail):
    s = _snail
    s.go_right()
    assert s.result == [1, 2, 3]
    assert s.matrix == [[4, 5, 6], [7, 8, 9]]


def test_go_right_go_down(_snail):
    s = _snail
    s.go_right()
    s.go_down()
    assert s.result == [1, 2, 3, 6, 9]
