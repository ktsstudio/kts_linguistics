import pickle
from collections import Counter
from pathlib import Path

import pymorphy2
from nltk import ToktokTokenizer

from kts_spellcheck.transforms.phonetize import phonetize


def load_precomputed_corpora(path: Path) -> Counter:
    with path.open() as f:
        return pickle.load(f)


def load_corpora(path: Path) -> Counter:
    words = Counter()
    tokenizer = ToktokTokenizer()
    alphabet = 'йцукенгшщзхъфывапролджэёячсмитьбю'

    for i, txtfile in enumerate(path.iterdir()):
        with txtfile.open() as f:
            for line in f:
                line = line.lower()
                line = ''.join(c if c in alphabet else ' ' for c in line)
                for word in tokenizer.tokenize(line):
                    if word != '':
                        words[word] += 1

    return words


def normalize_corpora(corpora: Counter) -> Counter:
    new_corpora = Counter()
    morph = pymorphy2.MorphAnalyzer()
    for word, count in corpora.items():
        new_corpora[morph.parse(word)[0].normal_form] += count
    return new_corpora


def phonetize_corpora(corpora: Counter) -> Counter:
    new_corpora = Counter()
    for word, count in corpora.items():
        new_corpora[phonetize(word)] += count
    return new_corpora
