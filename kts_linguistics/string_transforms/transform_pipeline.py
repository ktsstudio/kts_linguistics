from typing import List, Callable, Any

from kts_linguistics.string_transforms.abstract_transform import AbstractTransform


class TransformPipeline:
    def __init__(self):
        self.transforms = list()

    def add_transform(self, transform: AbstractTransform):
        self.transforms.append(transform)

    def fit(self, groups: List[List[str]]):
        for t in self.transforms:
            t.fit(groups, pipeline=self)

    def transform(self, s: Any) -> Any:
        transformed_s = s
        for t in self.transforms:
            transformed_s = t.transform(transformed_s)
        return transformed_s

    def custom_transform(self, s: Any, apply_before_transform: AbstractTransform) -> Any:
        for t in self.transforms:
            if t == apply_before_transform:
                break
            s = t.transform(s)
        return s
