from typing import List

import pymorphy2

from kts_linguistics.phonetics.phonetize import phonetize


def find_synonyms(word: str, synsets: List[List[str]]) -> List[List[str]]:
    return [synset for synset in synsets if word in synset]


def normalize_synsets(synsets: List[List[str]]) -> List[List[str]]:
    morph = pymorphy2.MorphAnalyzer()
    new_synsets = []
    for synset in synsets:
        new_synset = []
        for word in synset:
            word = word.lower()
            word = morph.parse(word)[0].normal_form
            new_synset.append(word)
        new_synsets.append(new_synset)
    return new_synsets


def phonetize_synsets(synsets: List[List[str]]) -> List[List[str]]:
    new_synsets = []
    for synset in synsets:
        new_synset = []
        for word in synset:
            new_synset.append(phonetize(word))
        new_synsets.append(new_synset)
    return new_synsets
