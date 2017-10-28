from typing import List

import sklearn.feature_extraction.text as sklearn_text

from kts_linguistics.corpora.corpora import Corpora
from kts_linguistics.string_transforms.abstract_transform import AbstractTransform
from kts_linguistics.string_transforms.transform_pipeline import TransformPipeline


class TfidfTransform(AbstractTransform):
    def __init__(self, corpora: Corpora, stop_words: List[str] = None, pretrained_tfidf: sklearn_text.TfidfVectorizer = None):
        if pretrained_tfidf is None:
            self.tfidf = sklearn_text.TfidfVectorizer(vocabulary=corpora.words(), stop_words=stop_words or [])
        else:
            self.tfidf = pretrained_tfidf

    def fit(self, groups: List[List[str]], pipeline: TransformPipeline):
        sentences = [s for group in groups for s in group]
        sentences = [pipeline.custom_transform(s, apply_before_transform=self) for s in sentences]
        self.tfidf.fit(sentences)

    def transform(self, s) -> str:
        return self.tfidf.transform([s])
