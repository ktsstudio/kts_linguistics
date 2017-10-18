from transliterate import translit


def basic_normalize(s: str) -> str:
    s = s.strip()
    s = s.lower()
    s = translit(s, 'ru')
    return s
