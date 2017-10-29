from kts_linguistics.phonetics.phonetize import phonetize_word
from kts_linguistics.string_transforms.abstract_transform import AbstractByWordTransform


class PhonetizeTransform(AbstractByWordTransform):
    def transform_word(self, s: str) -> str:
        return phonetize_word(s)
