def duplicate_count(text):
    text = text.lower()
    duplicate_char = [ch for ch in set(text) if text.count(ch) > 1]
    return len(duplicate_char)
