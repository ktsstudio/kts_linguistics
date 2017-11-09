from typing import List

from gensim.models import Doc2Vec as GensimDoc2Vec

from kts_linguistics.string_transforms.abstract_transform import AbstractTransform
from kts_linguistics.string_transforms.transform_pipeline import TransformPipeline
from kts_linguistics.misc import Vector1D


class Doc2VecTransform(AbstractTransform):
    def __init__(self, model: GensimDoc2Vec = None, **doc2vec_params):
        if model is None:
            self.model = GensimDoc2Vec(**doc2vec_params)
        else:
            self.model = model

    def fit(self, groups: List[List[str]], pipeline: TransformPipeline):
        sentences = [s for group in groups for s in group]
        sentences = [pipeline.custom_transform(s, apply_before_transform=self) for s in sentences]
        self.model.build_vocab(sentences)
        self.model.train(sentences, total_examples=self.model.corpus_count, epochs=self.model.iter)

    def transform(self, s: List[str]) -> Vector1D:
        return self.model.infer_vector(s)
