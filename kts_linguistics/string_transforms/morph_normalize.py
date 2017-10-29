import pymorphy2

from kts_linguistics.string_transforms.abstract_transform import AbstractByWordTransform


class MorphNormalizeTransform(AbstractByWordTransform):
    def __init__(self, do_cache=False):
        self.morph = pymorphy2.MorphAnalyzer()
        self.cache = dict()
        self.do_cache = do_cache

    def transform_word(self, word: str) -> str:
        if word in self.cache:
            return self.cache[word]

        normalized_word = self.morph.parse(word)[0].normal_form

        if self.do_cache:
            self.cache[word] = normalized_word

        return normalized_word
