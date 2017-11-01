import pickle
from pathlib import Path
from typing import List

from nltk import ToktokTokenizer

from kts_linguistics.chars import RUSSIAN_ALPHABET
from kts_linguistics.corpora.corpora import Corpora


def load_corpora_from_directory_of_txt(path: Path) -> Corpora:
    corpora = Corpora()

    tokenizer = ToktokTokenizer()
    for i, txtfile in enumerate(path.iterdir()):
        if not txtfile.is_file():
            continue
        with txtfile.open(encoding='utf-8') as f:
            for line in f:
                line = line.lower()
                line = ''.join(c if c in RUSSIAN_ALPHABET else ' ' for c in line)
                for word in tokenizer.tokenize(line):
                    if word != '':
                        corpora.increment_popularity(word)

    return corpora


def load_precomputed_corpora() -> Corpora:
    corpora = Corpora()

    path = Path(__file__).resolve().parent / 'data' / 'precomputed_corpora_counters' / 'corpora.pkl'
    with path.open(mode='rb') as f:
        corpora.update_with_counter(pickle.load(f))

    return corpora


def load_precomputed_normalized_corpora() -> Corpora:
    corpora = Corpora()

    path = Path(__file__).resolve().parent / 'data' / 'precomputed_corpora_counters' / 'normalized_corpora.pkl'
    with path.open(mode='rb') as f:
        corpora.update_with_counter(pickle.load(f))

    return corpora


def load_precomputed_phonetized_corpora() -> Corpora:
    corpora = Corpora()

    path = Path(__file__).resolve().parent / 'data' / 'precomputed_corpora_counters' / 'phonetized_corpora.pkl'
    with path.open(mode='rb') as f:
        corpora.update_with_counter(pickle.load(f))

    return corpora


def load_default_sentences() -> List[str]:
    path = Path(__file__).resolve().parent / 'data' / 'corpora' / 'rus_texts.txt'
    with path.open(encoding='utf-8') as f:
        result = f.readlines()
        result = [l.strip() for l in result]
        return result


def load_precomputed_normalized_default_sentences() -> List[str]:
    path = Path(__file__).resolve().parent / 'data' / 'precomputed_sentences' / 'normalized_rus_texts.txt'
    with path.open(encoding='utf-8') as f:
        result = f.readlines()
        result = [l.strip() for l in result]
        return result


def load_precomputed_phonetized_default_sentences() -> List[str]:
    path = Path(__file__).resolve().parent / 'data' / 'precomputed_sentences' / 'phonetized_rus_texts.txt'
    with path.open(encoding='utf-8') as f:
        result = f.readlines()
        result = [l.strip() for l in result]
        return result
