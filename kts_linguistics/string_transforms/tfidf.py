from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer as SklearnTfidfVectorizer

from kts_linguistics.string_transforms.abstract_transform import AbstractTransform
from kts_linguistics.string_transforms.transform_pipeline import TransformPipeline
from kts_linguistics.misc import SparseMatrix2D


class TfidfTransform(AbstractTransform):
    def __init__(self, tfidf: SklearnTfidfVectorizer = None, **tfidf_params):
        if tfidf is None:
            self.tfidf = SklearnTfidfVectorizer(**tfidf_params)
        else:
            self.tfidf = tfidf

    def fit(self, groups: List[List[str]], pipeline: TransformPipeline):
        sentences = [s for group in groups for s in group]
        sentences = [pipeline.custom_transform(s, apply_before_transform=self) for s in sentences]
        self.tfidf.fit(sentences)

    def transform(self, s: str) -> SparseMatrix2D:
        return self.tfidf.transform([s])
