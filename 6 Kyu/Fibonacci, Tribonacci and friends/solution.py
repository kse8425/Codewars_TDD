def next_num(lst, x):
    return sum(lst[-x:])


def Xbonacci(signature, n):
    result = signature[:n]
    x = len(signature)
    while len(result) < n:
        result.append(next_num(result, x))
    return result
