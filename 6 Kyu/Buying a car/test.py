import pytest

from solution import nbMonths, BuyCar


def test_nbMonths():
    assert nbMonths(2000, 8000, 1000, 1.5) == [6, 766]
    assert nbMonths(12000, 8000, 1000, 1.5) == [0, 4000]


@pytest.fixture
def create_buy_car():
    return BuyCar(2000, 8000, 1000, 1.5)


def test_buy_car_get_need_money(create_buy_car):
    assert create_buy_car._get_need_money() == -6000


def test_next_month(create_buy_car):
    create_buy_car._next_month()
    assert create_buy_car.old_car == 1970
    assert create_buy_car.new_car == 7880


def test_end_month(create_buy_car):
    assert create_buy_car.end_month() == [6, 766]
