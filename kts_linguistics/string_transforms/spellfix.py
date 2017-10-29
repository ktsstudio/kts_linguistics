from kts_linguistics.corpora.corpora import Corpora
from kts_linguistics.spellcheck.spellfix import spellfix
from kts_linguistics.string_transforms.abstract_transform import AbstractTransform, AbstractByWordTransform


class SpellfixTransform(AbstractByWordTransform):
    def __init__(self, corpora: Corpora, do_cache: bool = False):
        self.corpora = corpora
        self.cache = dict()
        self.do_cache = do_cache

    def transform_word(self, word: str) -> str:
        if word in self.cache:
            return self.cache[word]

        spellfixed_word = spellfix(word, corpora=self.corpora)

        if self.do_cache:
            if spellfixed_word != word:
                self.cache[word] = spellfixed_word

        return spellfixed_word
