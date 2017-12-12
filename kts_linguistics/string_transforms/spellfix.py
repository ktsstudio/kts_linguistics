from kts_linguistics.corpora.corpora import Corpora
from kts_linguistics.spellcheck.spellfix import spellfix_word
from kts_linguistics.string_transforms.abstract_transform import AbstractByWordTransform


class SpellfixTransform(AbstractByWordTransform):
    def __init__(self,
                 corpora: Corpora,
                 do_cache: bool = False,
                 fix_threshold: float = 1.0):
        self.corpora = corpora
        self.cache = dict()
        self.do_cache = do_cache
        self.fix_threshold = fix_threshold

    def transform_word(self, word: str) -> str:
        if word in self.cache:
            return self.cache[word]

        spellfixed_word = spellfix_word(word, corpora=self.corpora, fix_threshold=self.fix_threshold)

        if self.do_cache:
            if spellfixed_word != word:
                self.cache[word] = spellfixed_word

        return spellfixed_word
