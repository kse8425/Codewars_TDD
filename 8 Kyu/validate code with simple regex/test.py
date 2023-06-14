from solution import validate_code


def test_validate_code():
    assert validate_code(123) == True
    assert validate_code(8) == False
