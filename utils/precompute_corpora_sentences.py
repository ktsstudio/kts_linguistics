from pathlib import Path

from kts_linguistics.corpora.loaders import load_default_sentences
from kts_linguistics.corpora.transforms import normalize_sentences, phonetize_sentences

if __name__ == '__main__':
    dest_path_root = Path(__file__).resolve().parent / '..' / 'kts_linguistics' / 'corpora' / 'data' / 'precomputed_sentences'

    print('Loading sentences...')
    sentences = load_default_sentences()
    print('Normalizing sentences...')
    normalized_sentences = normalize_sentences(sentences)
    print('Phonetizing sentences...')
    phonetized_sentences = phonetize_sentences(normalized_sentences)

    print('Writing to the disk...')

    with (dest_path_root / 'normalized_rus_texts.txt').open(mode='w', encoding='utf-8') as f:
        for line in normalized_sentences:
            f.write(line)
            f.write('\n')

    with (dest_path_root / 'phonetized_rus_texts.txt').open(mode='w', encoding='utf-8') as f:
        for line in phonetized_sentences:
            f.write(line)
            f.write('\n')
