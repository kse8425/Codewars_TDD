def find_outlier(lst):
    odd_list = [n for n in lst if n % 2 == 1]
    even_list = [n for n in lst if n % 2 == 0]
    if len(odd_list) > len(even_list):
        return even_list[0]
    else:
        return odd_list[0]
