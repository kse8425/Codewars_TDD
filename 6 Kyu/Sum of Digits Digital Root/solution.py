def digital_root(input_num):
    result = sum_of_digits(input_num)
    if is_over_two_digit(result):
        result = digital_root(result)
    return result


def sum_of_digits(num):
    return sum([int(n) for n in (str(num))])


def is_over_two_digit(num):
    return len(str(num)) > 1
