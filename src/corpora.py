from collections import Counter
from pathlib import Path

import pymorphy2
from nltk import ToktokTokenizer


def load_corpora() -> Counter:
    words = Counter()
    tokenizer = ToktokTokenizer()
    alphabet = 'йцукенгшщзхъфывапролжээёячсмитьбю'

    path = Path(__file__).resolve().parent / '..' / 'data' / 'corpora'
    for i, txtfile in enumerate(path.iterdir()):
        with txtfile.open() as f:
            for line in f:
                line = line.lower()
                line = ''.join(c if c in alphabet else '' if c == '-' else ' ' for c in line)
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

