from typing import List, Callable

from kts_linguistics.string_transforms.abstract_transform import AbstractTransform
from kts_linguistics.string_transforms.func_transform import FuncTransform


class TransformPipeline:
    def __init__(self):
        self.transforms = []

    def add_transform(self, transform: AbstractTransform):
        self.transforms.append(transform)

    def add_tranform_func(self, func: Callable[[str], str]):
        self.add_transform(FuncTransform(func))

    def fit(self, groups: List[List[str]]):
        for t in self.transforms:
            t.fit(groups, pipeline=self)

    def transform(self, s: str) -> str:
        for t in self.transforms:
            s = t.transform(s)
        return s

    def custom_transform(self, s: str, apply_before_transform: AbstractTransform) -> str:
        for t in self.transforms:
            if t == apply_before_transform:
                break
            s = t.transform(s)
        return s
