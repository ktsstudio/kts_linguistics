import copy
from typing import List, Any

from kts_linguistics.string_transforms.abstract_transform import AbstractTransform


class TransformPipeline:
    def __init__(self, do_cache=False):
        self.transforms = list()

        self.cache = dict()
        self.do_cache = do_cache

    def add_transform(self, transform: AbstractTransform):
        self.transforms.append(transform)

    def remove_transform_by_class(self, cls):
        self.transforms = [t for t in self.transforms if not isinstance(t, cls)]

    def copy(self):
        c = copy.copy(self)
        c.transforms = [it for it in c.transforms]  # copy list
        return c

    def fit(self, groups: List[List[str]]):
        for t in self.transforms:
            t.fit(groups, pipeline=self)

    def transform(self, s: Any) -> Any:
        if isinstance(s, list):
            s = tuple(s)

        if s in self.cache:
            return self.cache[s]

        transformed_s = s
        for t in self.transforms:
            transformed_s = t.transform(transformed_s)

        if self.do_cache:
            if isinstance(transformed_s, list):
                transformed_s = tuple(transformed_s)
            self.cache[s] = transformed_s

        return transformed_s

    def custom_transform(self, s: Any, apply_before_transform: AbstractTransform) -> Any:
        for t in self.transforms:
            if t == apply_before_transform:
                break
            s = t.transform(s)
        return s
