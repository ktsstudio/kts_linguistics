import pymorphy2
from nltk import ToktokTokenizer

from kts_linguistics.string_transforms.abstract_transform import AbstractTransform


class MorphNormalizeTransform(AbstractTransform):
    def __init__(self):
        self.tokenizer = ToktokTokenizer()
        self.morph = pymorphy2.MorphAnalyzer()

    def transform(self, s: str) -> str:
        words = self.tokenizer.tokenize(s)
        words = [self.morph.parse(word)[0].normal_form for word in words]
        return ' '.join(words)
