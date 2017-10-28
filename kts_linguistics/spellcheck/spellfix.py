import Levenshtein

from kts_linguistics.chars import DIGITS
from kts_linguistics.corpora.corpora import Corpora


def spellfix(s: str, corpora: Corpora) -> str:
    new_words = []

    for word in s.split(' '):
        if word == '':
            continue

        if word in corpora:
            new_words.append(word)
            continue

        if word.isdigit():
            new_words.append(word)
            continue
        elif any(d in word for d in DIGITS):
            # TODO: digits handling
            # dfjk1222sdfk
            number = ''.join(c for c in word if c in DIGITS)
            word = ''.join(c for c in word if c not in DIGITS)
            new_words.append(number)

        best_match = None
        best_match_distance = None
        best_match_popularity = None

        for corpora_word, popularity in corpora.words_with_counts():
            distance = Levenshtein.distance(word, corpora_word)
            if best_match is None \
                    or (distance < best_match_distance) \
                    or (distance == best_match_distance and popularity > best_match_popularity):
                best_match = corpora_word
                best_match_distance = distance
                best_match_popularity = popularity

        new_words.append(best_match)

    return ' '.join(new_words)
