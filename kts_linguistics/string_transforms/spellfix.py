from kts_linguistics.corpora.corpora import Corpora
from kts_linguistics.spellcheck.spellfix import spellfix
from kts_linguistics.string_transforms.abstract_transform import AbstractTransform


class SpellfixTransform(AbstractTransform):
    def __init__(self, corpora: Corpora):
        self.corpora = corpora

    def transform(self, s: str) -> str:
        return spellfix(s, corpora=self.corpora)
