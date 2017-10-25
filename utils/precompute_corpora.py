import pickle
from pathlib import Path

from kts_spellcheck.corpora import load_corpora, normalize_corpora, phonetize_corpora

if __name__ == '__main__':
    dest_path_root = Path(__file__).resolve().parent / '..' / 'data' / 'precomputed_corpora'
    corpora_path = Path(__file__).resolve().parent / '..' / 'data' / 'corpora'

    print('Loading corpora...')
    corpora = load_corpora(corpora_path)
    print('Normalizing corpora...')
    normalized_corpora = normalize_corpora(corpora)
    print('Phonetizing corpora...')
    phonetized_corpora = phonetize_corpora(normalized_corpora)

    print('Writing to the disk...')

    with (dest_path_root / 'corpora.pkl').open(mode='wb') as f:
        pickle.dump(corpora, f)

    with (dest_path_root / 'normalized_corpora.pkl').open(mode='wb') as f:
        pickle.dump(normalized_corpora, f)

    with (dest_path_root / 'phonetized_corpora.pkl').open(mode='wb') as f:
        pickle.dump(phonetized_corpora, f)
