import pymorphy2

from kts_linguistics.string_transforms.abstract_transform import AbstractByWordTransform


class MorphNormalizeTransform(AbstractByWordTransform):
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()

    def transform_word(self, s: str) -> str:
        return self.morph.parse(s)[0].normal_form
