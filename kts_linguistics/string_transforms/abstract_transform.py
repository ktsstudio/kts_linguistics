from typing import List

from kts_linguistics.string_transforms.transform_pipeline import TransformPipeline


class AbstractTransform:
    def fit(self, groups: List[List[str]], pipeline: TransformPipeline):
        pass

    def transform(self, s: str) -> str:
        pass
