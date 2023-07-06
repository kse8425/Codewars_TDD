from solution import format_duration, Timer


def test_format_duration():
    assert format_duration(0) == 'now'
    assert format_duration(1) == '1 second'
    assert format_duration(62) == '1 minute and 2 seconds'
    assert format_duration(3662) == '1 hour, 1 minute and 2 seconds'


def test_timer():
    t = Timer(3662)
    assert t.hours == 1
    assert t.minutes == 1
    assert t.seconds == 2


def test_get_str_seconds():
    t = Timer(1)
    assert t.get_str_seconds() == '1 second'
    t = Timer(2)
    assert t.get_str_seconds() == '2 seconds'


def test_result():
    t = Timer(3662)
    assert t.result() == '1 hour, 1 minute and 2 seconds'
