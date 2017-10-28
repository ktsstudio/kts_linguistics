from kts_linguistics.phonetics.phonetize import phonetize
from kts_linguistics.string_transforms.abstract_transform import AbstractTransform


class PhonetizeTransform(AbstractTransform):
    def transform(self, s: str) -> str:
        return phonetize(s)
