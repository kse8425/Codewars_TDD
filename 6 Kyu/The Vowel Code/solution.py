ENCODE_TABLE = {
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5',
}

DECODE_TABLE = {
    '1': 'a',
    '2': 'e',
    '3': 'i',
    '4': 'o',
    '5': 'u',
}


def encode_char(ch):
    return ENCODE_TABLE[ch] if ch in ENCODE_TABLE else ch


def decode_char(ch):
    return DECODE_TABLE[ch] if ch in DECODE_TABLE else ch


def encode(st):
    st = [encode_char(ch) for ch in st]
    return ''.join(st)


def decode(st):
    st = [decode_char(ch) for ch in st]
    return ''.join(st)
