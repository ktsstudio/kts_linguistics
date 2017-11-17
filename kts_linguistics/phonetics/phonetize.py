from kts_linguistics.chars import RUSSIAN_ALPHABET


def phonetize(sentence: str) -> str:
    new_sentence_array = []
    for word in sentence.split(' '):
        if word == '':
            continue
        new_sentence_array.append(phonetize_word(word))
    return ' '.join(new_sentence_array)


def phonetize_word(word: str) -> str:
    # http://forum.aeroion.ru/topic461.html
    if len(word) == 0:
        return word
    word = word.lower()
    word = _replace_chars(word)
    word = _remove_doubles(word)
    word = _defeanate_consonants(word)
    word = _remove_doubles(word)
    word = _simplify_endings(word)
    word = _delete_hard_and_soft_sign(word)
    return word


def _replace_chars(word):
    # Замены

    for c in ['о', 'ы', 'а', 'я']:
        word = word.replace(c, 'а')
    for c in ['ю', 'у']:
        word = word.replace(c, 'у')
    for c in ['е', 'ё', 'э', 'и']:
        word = word.replace(c, 'и')
    for c in ['тс', 'дс']:
        word = word.replace(c, 'ц')
    for c in ['йо', 'ио', 'йе', 'ие']:
        word = word.replace(c, 'и')

    return word


def _defeanate_consonants(word):
    # Оглушение согласных в слабой позиции
    #
    # Слабой считается такая позиция (место в слове) звука,
    # при которой он слышится неясно, неотчётливо.
    #
    # Такими позициями для согласных звуков являются
    # 1) расположение согласного звука в конце слова: дуб [дуп], верблюд [вирблют];
    # 2) расположение согласного звука перед другим согласным (кроме сонорных) -
    #     при так называемом стечении согласных, когда их несколько в слове:
    #     пробка [пропка], скобка [скопка];

    voiced_chars_to_voiceless = {'б': 'п', 'в': 'ф', 'г': 'к', 'д': 'т', 'ж': 'ш', 'з': 'с'}
    voiced_chars = list(voiced_chars_to_voiceless.keys())

    for c in voiced_chars:
        if word[-1] == c:
            word = _replace_end(word, c, voiced_chars_to_voiceless[c])

    new_chars_array = list(word)
    for i in range(1, len(new_chars_array)):
        if new_chars_array[i - 1] in voiced_chars and new_chars_array[i] in voiced_chars:
            new_chars_array[i - 1] = voiced_chars_to_voiceless[new_chars_array[i - 1]]
    word = ''.join(new_chars_array)

    return word


def _simplify_endings(word):
    # Сжатие окончаний

    ends_map = [
        (['ук', 'юк'], 'Q'),
        (['ина'], 'W'),
        (['ик', 'ек'], 'E'),
        (['нко'], 'R'),
        (['ов', 'иев', 'еев', 'ев'], 'T'),
        (['ых', 'их'], 'Y'),
        (['ая'], 'U'),
        (['ий', 'ый'], 'I'),
        (['ин'], 'O'),
        (['ова', 'иева', 'еева', 'ева'], 'P'),
        (['овский'], 'A'),
        (['евский'], 'S'),
        (['овская'], 'D'),
        (['евская'], 'F'),
    ]

    for ends_map_row in ends_map:
        for end in ends_map_row[0]:
            if word.endswith(end):
                return _replace_end(word, end, ends_map_row[1])
    return word


def _remove_doubles(word):
    # Исключение повторяющихся символов

    new_chars_array = []

    for i in range(len(word)):
        if i != 0 and word[i - 1] == word[i] and word[i] in RUSSIAN_ALPHABET:
            continue
        new_chars_array.append(word[i])

    return ''.join(new_chars_array)


def _delete_hard_and_soft_sign(word):
    # Исключение Ъ, Ь

    for c in ['ъ', 'ь']:
        word = word.replace(c, '')

    return word


def _replace_end(word, old, new):
    return word[:-len(old)] + new
