from transliterate import translit


def basic_normalize(s: str) -> str:
    s = s.strip()
    s = s.lower()
    s = translit(s, 'ru')
    s = _remove_non_russian_chars(s)
    return s


def _remove_non_russian_chars(source):
    alphabet = 'йцукенгшщзхъфывапролджэёячсмитьбю'
    digits = '1234567890'
    allowed_chars = alphabet + digits
    return ''.join(c if c in allowed_chars else ' ' for c in source)
