import pickle
from pathlib import Path

from nltk import ToktokTokenizer

from kts_linguistics.chars import RUSSIAN_ALPHABET
from kts_linguistics.corpora.corpora import Corpora


def load_corpora_from_directory_of_txt(path: Path) -> Corpora:
    corpora = Corpora()

    tokenizer = ToktokTokenizer()
    alphabet = RUSSIAN_ALPHABET

    for i, txtfile in enumerate(path.iterdir()):
        if not txtfile.is_file():
            continue
        with txtfile.open(encoding='utf8') as f:
            for line in f:
                line = line.lower()
                line = ''.join(c if c in alphabet else ' ' for c in line)
                for word in tokenizer.tokenize(line):
                    if word != '':
                        corpora.increment_popularity(word)

    return corpora


def load_precomputed_corpora() -> Corpora:
    corpora = Corpora()

    path = Path(__file__).resolve() / 'data' / 'precomputed_corpora_counters' / 'corpora.pkl'
    with path.open(mode='rb') as f:
        corpora.update_with_counter(pickle.load(f))

    return corpora


def load_precomputed_normalized_corpora() -> Corpora:
    corpora = Corpora()

    path = Path(__file__).resolve() / 'data' / 'precomputed_corpora_counters' / 'normalized_corpora.pkl'
    with path.open(mode='rb') as f:
        corpora.update_with_counter(pickle.load(f))

    return corpora


def load_precomputed_phonetized_corpora() -> Corpora:
    corpora = Corpora()

    path = Path(__file__).resolve() / 'data' / 'precomputed_corpora_counters' / 'phonetized_corpora.pkl'
    with path.open(mode='rb') as f:
        corpora.update_with_counter(pickle.load(f))

    return corpora
