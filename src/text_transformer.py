from functools import partial
from typing import List, Any, Callable

from sklearn.feature_extraction.text import TfidfVectorizer

from src.transforms.basic_normalize import basic_normalize
from src.transforms.normalize import normalize
from src.transforms.spellfix import spellfix


class TextTransformer:
    def __init__(self):
        self.fit_pipeline = []
        self.transform_pipeline = []

    def fit(self, groups: List[List[str]]):
        for func in self.fit_pipeline:
            func(groups)

    def transform(self, s: str) -> Any:
        for func in self.transform_pipeline:
            s = func(s)
        return s

    def apply_transforms_before_func(self, s: str, stopFunc: Callable) -> Any:
        for func in self.transform_pipeline:
            if func == stopFunc:
                break
            s = func(s)
        return s


class SimpleTextTransformer(TextTransformer):
    def __init__(self):
        super().__init__()

        self.transform_pipeline.append(basic_normalize)
        self.transform_pipeline.append(normalize)


class SpellfixTextTransformer(SimpleTextTransformer):
    def __init__(self, corpora):
        super().__init__()

        self.transform_pipeline.append(partial(spellfix, corpora=corpora))


class TfidfTextTransformer(SpellfixTextTransformer):
    def __init__(self, corpora, stop_words=None, pretrained_tfidf=None):
        super().__init__(corpora)

        if pretrained_tfidf is None:
            self.tfidf = TfidfVectorizer(stop_words=stop_words or [], norm=None)
        else:
            self.tfidf = pretrained_tfidf

        self.fit_pipeline.append(self._tfidf_fit)
        self.transform_pipeline.append(self._tfidf_transform)

    def _tfidf_fit(self, groups: List[List[str]]):
        sentences = [it for group in groups for it in group]
        sentences = [self.apply_transforms_before_func(it, self._tfidf_transform) for it in sentences]
        self.tfidf.fit(sentences)

    def _tfidf_transform(self, s):
        return self.tfidf.transform([s])


class WmdTextTransformer(SpellfixTextTransformer):
    def __init__(self, corpora):
        super().__init__(corpora)

        raise NotImplementedError
