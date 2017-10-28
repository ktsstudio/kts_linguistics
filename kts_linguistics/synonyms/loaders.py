from pathlib import Path
from typing import List


def load_synsets() -> List[List[str]]:
    synsets = []

    path = Path(__file__).resolve().parent / 'data' / 'synsets.txt'
    with path.open(encoding='utf8') as f:
        for line in f:
            synset = []

            for word in line.split(','):
                word = word.strip()
                if len(word) == 0:
                    continue
                synset.append(word)

            if len(synset) <= 1:
                continue
            synsets.append(synset)

    return synsets
