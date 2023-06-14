import math


def multiply_itself(lit):
    return [n * n for n in lit]


def add_together(lit):
    return sum(lit)


def take_square_root(num):
    return num ** (1 / 2)


def divide_by_two(num):
    return num / 2


def predict_age(*ages):
    res = multiply_itself(ages)
    res = add_together(res)
    res = take_square_root(res)
    res = divide_by_two(res)
    return math.floor(res)
