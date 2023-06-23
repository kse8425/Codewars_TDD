def reverse(lst):
    result = list()
    for _ in range(len(lst)):
        result.append(lst.pop())
    return result

