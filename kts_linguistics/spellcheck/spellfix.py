import Levenshtein
from nltk import ToktokTokenizer

from kts_linguistics.chars import DIGITS
from kts_linguistics.corpora.corpora import Corpora


def spellfix(s: str, corpora: Corpora) -> str:
    tokenizer = ToktokTokenizer()
    return ' '.join(spellfix_word(word, corpora) for word in tokenizer.tokenize(s))


def spellfix_word(word: str, corpora: Corpora) -> str:
    if len(word) <= 3:
        return word
    if word in corpora:
        return word
    if word.isdigit():
        return word

    if _has_digits(word):
        return ' '.join([spellfix_word(it, corpora) for it in _split_chars_and_digits(word)])

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

    return best_match


def _has_digits(s: str):
    return any(d in s for d in DIGITS)


def _split_chars_and_digits(s: str):
    words = []
    current_word_array = []
    is_digit_mode = None
    for c in s:
        if is_digit_mode is None:
            is_digit_mode = c.isdigit()
        elif is_digit_mode != c.isdigit():
            words.append(''.join(current_word_array))
            current_word_array = []
            is_digit_mode = not is_digit_mode
        current_word_array.append(c)
    words.append(''.join(current_word_array))
    return words
