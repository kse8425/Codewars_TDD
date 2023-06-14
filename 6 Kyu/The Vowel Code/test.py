from solution import encode, encode_char, decode_char, decode


def test_encode_char():
    assert encode_char('a') == '1'
    assert encode_char('e') == '2'
    assert encode_char('i') == '3'
    assert encode_char('o') == '4'
    assert encode_char('u') == '5'


def test_decode_char():
    assert decode_char('1') == 'a'
    assert decode_char('2') == 'e'
    assert decode_char('3') == 'i'
    assert decode_char('4') == 'o'
    assert decode_char('5') == 'u'


def test_encode():
    assert encode('hello') == 'h2ll4'
    assert encode('How are you today?') == 'H4w 1r2 y45 t4d1y?'


def test_decode():
    assert decode('h2ll4') == 'hello'
