from solution import duplicate_count


def test_duplicate_count():
    assert duplicate_count("") == 0
    assert duplicate_count("Indivisibilities") == 2
