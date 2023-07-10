import itertools


def next_bigger(n):
    arr = sorted(combine_num(n))
    result = arr[arr.index(n) + 1] if arr.index(n) < len(arr) - 1 else -1
    return result


def combine_num(st):
    ori_arr = list(str(st))
    result = set()
    for subset in itertools.permutations(ori_arr, len(ori_arr)):
        result.add(int(''.join(subset)))
    return list(result)


def best_practices(n):
    s = list(str(n))
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            t = s[i:]
            m = min(filter(lambda x: x > t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int(''.join(s))
    return -1
