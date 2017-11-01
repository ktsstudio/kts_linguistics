from typing import List

import pymorphy2
from nltk import ToktokTokenizer

from kts_linguistics.chars import RUSSIAN_ALPHABET
from kts_linguistics.corpora.corpora import Corpora
from kts_linguistics.phonetics.phonetize import phonetize_word, phonetize


def normalize_corpora(corpora: Corpora) -> Corpora:
    new_corpora = Corpora()
    morph = pymorphy2.MorphAnalyzer()
    for word, count in corpora.words_with_counts():
        new_corpora.increment_popularity(morph.parse(word)[0].normal_form, count)
    return new_corpora


def phonetize_corpora(corpora: Corpora) -> Corpora:
    new_corpora = Corpora()
    for word, count in corpora.words_with_counts():
        new_corpora.increment_popularity(phonetize_word(word), count)
    return new_corpora


def normalize_sentences(sentences: List[str]) -> List[str]:
    new_sentences = []
    tokenizer = ToktokTokenizer()
    morph = pymorphy2.MorphAnalyzer()
    for line in sentences:
        line = line.lower()
        line = ''.join(c if c in RUSSIAN_ALPHABET else ' ' for c in line)
        line = ' '.join(morph.parse(word)[0].normal_form for word in tokenizer.tokenize(line))
        new_sentences.append(line)
    return new_sentences


def phonetize_sentences(sentences: List[str]) -> List[str]:
    return [phonetize(s) for s in sentences]
