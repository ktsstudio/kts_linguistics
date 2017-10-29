from typing import List, Any

from kts_linguistics.string_transforms.transform_pipeline import TransformPipeline


class AbstractTransform:
    def fit(self, groups: List[List[str]], pipeline: TransformPipeline):
        pass

    def transform(self, s: Any) -> Any:
        return s


class AbstractByWordTransform(AbstractTransform):
    def transform(self, l: List[str]) -> List[Any]:
        return [self.transform_word(w) for w in l]

    def transform_word(self, s: str) -> Any:
        return s
