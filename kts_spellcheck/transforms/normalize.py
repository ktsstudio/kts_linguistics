import pymorphy2
from nltk import ToktokTokenizer


def normalize(s: str) -> str:
    tokenizer = ToktokTokenizer()
    morph = pymorphy2.MorphAnalyzer()

    words = tokenizer.tokenize(s)
    words = [morph.parse(word)[0].normal_form for word in words]
    return ' '.join(words)
