def create_phone_number(arr):
    return f'({join_number(arr[:3])}) {join_number(arr[3:6])}-{join_number(arr[6:])}'


def join_number(num_arr):
    result = list(map(str, num_arr))
    return ''.join(result)
