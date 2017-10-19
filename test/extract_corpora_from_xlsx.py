from pathlib import Path
from typing import List

import pandas as pd
from nltk import ToktokTokenizer
from transliterate import translit


def _load_leasing_data() -> List[List[str]]:
    path = Path(__file__).resolve().parent / '..' / 'data' / 'leasing_data.xlsx'
    df = pd.read_excel(str(path), skiprows=8)
    df = df.iloc[1:, 3:]
    return [[it for it in row if isinstance(it, str)] for i, row in df.iterrows()]


def _load_globo_data() -> List[str]:
    path = Path(__file__).resolve().parent / '..' / 'data' / 'globo_data.xlsx'
    data = []
    for sheet_i in range(8):
        df = pd.read_excel(str(path), skiprows=1, sheetname=sheet_i)
        sheet_data = [[it for it in row if isinstance(it, str)][0:] for i, row in df.iterrows()]
        data.extend(sheet_data)
    return data


if __name__ == '__main__':
    question_groups = _load_globo_data() + _load_leasing_data()
    questions = [q for group in question_groups for q in group]

    tokenizer = ToktokTokenizer()
    alphabet = 'йцукенгшщзхъфывапролджэёячсмитьбю'

    words = set()
    for question in questions:
        question = question.lower()
        question = ''.join(c if c in alphabet else '' if c == '-' else ' ' for c in question)
        for word in tokenizer.tokenize(question):
            if word != '':
                words.add(word)

    print(' '.join(words))

