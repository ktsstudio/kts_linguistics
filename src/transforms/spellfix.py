from collections import Counter

import Levenshtein


def spellfix(s: str, corpora: Counter) -> str:
    new_words = []

    for word in s.split(' '):
        best_match = None
        best_match_distance = None
        best_match_popularity = None

        for corpora_word, popularity in corpora.items():
            distance = Levenshtein.distance(word, corpora_word)
            if best_match is None \
                    or (distance < best_match_distance) \
                    or (distance == best_match_distance and popularity > best_match_popularity):
                best_match = corpora_word
                best_match_distance = distance
                best_match_popularity = popularity

        new_words.append(best_match)

    return ' '.join(new_words)
