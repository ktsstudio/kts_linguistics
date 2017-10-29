from kts_linguistics.chars import RUSSIAN_ALPHABET, ENGLISH_ALPHABET, DIGITS
from kts_linguistics.string_transforms.abstract_transform import AbstractTransform


class BasicNormalizeTransform(AbstractTransform):
    def __init__(self):
        self.allowed_chars = RUSSIAN_ALPHABET + ENGLISH_ALPHABET + DIGITS + ' '

    def transform(self, s: str) -> str:
        s = s.strip()
        s = s.lower()
        s = ''.join(c for c in s if c in self.allowed_chars)
        return s
