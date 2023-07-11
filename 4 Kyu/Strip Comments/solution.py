import re


def strip_comments(st, markers):
    if not markers:
        return st
    st_arr = split_line(st)
    result = [remove_after_marker(s, markers) for s in st_arr]
    result = list(map(remove_end_space, result))
    return '\n'.join(result)


def split_line(st):
    return st.split('\n')


def remove_end_space(st):
    return re.sub(r'\s$', '', st) if st != ' ' else st


def remove_after_marker(st, markers):
    index = get_marker_position(st, markers)
    return st[:index]


def get_marker_position(st, markers):
    indexes = []
    for mk in markers:
        try:
            indexes.append(st.index(mk))
        except ValueError:
            indexes.append(len(st))
    return min(indexes)
