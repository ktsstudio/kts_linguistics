import pickle
from pathlib import Path

from kts_linguistics.corpora.loaders import load_corpora_from_directory_of_txt
from kts_linguistics.corpora.transforms import normalize_corpora, phonetize_corpora

if __name__ == '__main__':
    dest_path_root = Path(__file__).resolve().parent / '..' / 'kts_linguistics' / 'corpora' / 'data' / 'precomputed_corpora_counters'
    corpora_path = Path(__file__).resolve().parent / '..' / 'kts_linguistics' / 'corpora' / 'data' / 'corpora'

    print('Loading corpora...')
    corpora = load_corpora_from_directory_of_txt(corpora_path)
    print('Normalizing corpora...')
    normalized_corpora = normalize_corpora(corpora)
    print('Phonetizing corpora...')
    phonetized_corpora = phonetize_corpora(normalized_corpora)

    print('Writing to the disk...')

    with (dest_path_root / 'corpora.pkl').open(mode='wb') as f:
        pickle.dump(corpora._counter, f)

    with (dest_path_root / 'normalized_corpora.pkl').open(mode='wb') as f:
        pickle.dump(normalized_corpora._counter, f)

    with (dest_path_root / 'phonetized_corpora.pkl').open(mode='wb') as f:
        pickle.dump(phonetized_corpora._counter, f)
