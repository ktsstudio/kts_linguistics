from pathlib import Path
from typing import List

import pandas as pd


def load_questions_data() -> List[List[str]]:
    return load_leasing_data() + load_globo_data()


def load_leasing_data() -> List[List[str]]:
    path = Path(__file__).resolve().parent / '..' / 'data' / 'leasing_data.xlsx'
    df = pd.read_excel(str(path), skiprows=8)
    df = df.iloc[1:, 5:]
    return [[it for it in row if isinstance(it, str)] for i, row in df.iterrows()]


def load_globo_data() -> List[List[str]]:
    path = Path(__file__).resolve().parent / '..' / 'data' / 'globo_data.xlsx'
    data = []
    for sheet_i in range(8):
        df = pd.read_excel(str(path), skiprows=1, sheetname=sheet_i)
        sheet_data = [[it for it in row if isinstance(it, str)][1:] for i, row in df.iterrows()]
        data.extend(sheet_data)
    return data
