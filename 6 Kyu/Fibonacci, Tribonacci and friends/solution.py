def next_num(lst, x):
    return sum(lst[-x:])


def Xbonacci(signature, n):
    if len(signature) > n:
        return signature[:n]
    repeat_num = n - len(signature)
    x = len(signature)
    result = signature
    for _ in range(repeat_num):
        result.append(next_num(result, x))
    return result
