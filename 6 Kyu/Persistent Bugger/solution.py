def persistence(n):
    count = 0
    while n >= 10:
        n = multiple_digit(n)
        count += 1
    return count


def multiple_digit(n):
    result = 1
    for num in str(n):
        result *= int(num)
    return result
