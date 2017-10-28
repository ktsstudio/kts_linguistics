from kts_linguistics.chars import RUSSIAN_ALPHABET, ENGLISH_ALPHABET, DIGITS
from kts_linguistics.string_transforms.abstract_transform import AbstractTransform


class BasicNormalizeTransform(AbstractTransform):
    def transform(self, s: str) -> str:
        s = s.strip()
        s = s.lower()
        s = ''.join(c for c in s if c in RUSSIAN_ALPHABET + ENGLISH_ALPHABET + DIGITS + ' ')
        return s
