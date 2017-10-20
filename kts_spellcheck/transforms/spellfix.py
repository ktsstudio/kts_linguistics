from collections import Counter

import Levenshtein


def spellfix(s: str, corpora: Counter) -> str:
    new_words = []

    for word in s.split(' '):
        if word == '':
            continue

        if word in corpora.keys():
            new_words.append(word)
            continue

        if word.isdigit():
            new_words.append(word)
            continue
        elif any(d in word for d in '1234567890'):
            number = ''.join(c for c in word if c in '1234567890')
            word = ''.join(c for c in word if c not in '1234567890')
            new_words.append(number)

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
