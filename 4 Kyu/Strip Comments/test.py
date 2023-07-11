from solution import strip_comments, split_line, remove_end_space, remove_after_marker, get_marker_position


def test_strip_comments():
    assert strip_comments('a #b\nc\nd $e f g', ['#', '$']) == 'a\nc\nd'
    assert strip_comments('a #b\nc\nd $e f g', []) == 'a #b\nc\nd $e f g'


def test_split_line():
    assert split_line('a\nb\nc') == ['a', 'b', 'c']


def test_remove_end_space():
    assert remove_end_space(' abc ') == ' abc'
    assert remove_end_space(' ') == ' '
    assert remove_end_space('  ') == ' '


def test_get_marker_position():
    assert get_marker_position('abc #b !b', ['!', '#']) == 4
    assert get_marker_position('abc', ['!', '#']) == 3
    assert get_marker_position('a #b', ['#', '$']) == 2


def test_remove_after_marker():
    assert remove_after_marker('abc # abc', '#') == 'abc '
