from transliterate import translit

from kts_linguistics.chars import RUSSIAN_ALPHABET, DIGITS
from kts_linguistics.string_transforms.abstract_transform import AbstractTransform


class BasicNormalizeTransform(AbstractTransform):
    def transform(self, s: str) -> str:
        s = s.strip()
        s = s.lower()
        s = translit(s, 'ru')
        s = remove_non_russian_chars(s, keep_digits=True)
        return s


def remove_non_russian_chars(source: str, keep_digits: bool) -> str:
    if keep_digits:
        allowed_chars = RUSSIAN_ALPHABET + DIGITS
    else:
        allowed_chars = RUSSIAN_ALPHABET

    return ''.join(c if c in allowed_chars else ' ' for c in source)
