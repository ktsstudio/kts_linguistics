from collections import Counter
from typing import List

from nltk import ToktokTokenizer


class Corpora:
    def __init__(self):
        self._counter = Counter()

    def get_popularity(self, word: str) -> int:
        return self._counter.get(word, 0)

    def increment_popularity(self, word: str, count: int = 1):
        self._counter[word] += count

    def update_with_list(self, words: List[str]):
        for word in words:
            self._counter[word] += 1

    def update_with_counter(self, counter: Counter):
        self._counter.update(counter)

    def update_with_str(self, s: str):
        tokenizer = ToktokTokenizer()
        self.update_with_list(tokenizer.tokenize(s))

    def update_with_list_of_str(self, l: List[str]):
        for s in l:
            self.update_with_str(s)

    def update_with_list_of_list_of_str(self, ll: List[List[str]]):
        for l in ll:
            for s in l:
                self.update_with_str(s)

    def update_with_corpora(self, corpora):
        self.update_with_counter(corpora._counter)

    def words(self) -> List[str]:
        return list(self._counter.keys())

    def words_with_counts(self) -> List[str]:
        return list(self._counter.items())

    def __contains__(self, item: str) -> bool:
        return item in self._counter.keys()
