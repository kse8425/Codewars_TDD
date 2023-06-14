from solution import calculate_tip


def test_terrible_is_0_per():
    assert calculate_tip(100, 'terrible') == 0


def test_poor_is_5_per():
    assert calculate_tip(100, 'poor') == 5


def test_good_is_10_per():
    assert calculate_tip(100, 'good') == 10


def test_great_is_15_per():
    assert calculate_tip(100, 'great') == 15


def test_excellent_is_20_per():
    assert calculate_tip(100, 'excellent') == 20


def test_tip_always_round_up():
    assert calculate_tip(85, 'poor') == 5


def test_case_insensitive():
    assert calculate_tip(100, 'POOR') == 5
    assert calculate_tip(100, 'Excellent') == 20


def test_unrecognised_rating():
    assert calculate_tip(100, 'hi') == 'Rating not recognised'
