from collections import Counter
from typing import List


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

    def words(self):
        return self._counter.keys()

    def words_with_counts(self):
        return self._counter.items()

    def __contains__(self, item):
        return item in self._counter.keys()
