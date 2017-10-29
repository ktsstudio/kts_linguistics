from typing import List, Callable, Any

from kts_linguistics.string_transforms.abstract_transform import AbstractTransform
from kts_linguistics.string_transforms.utility_transforms import FuncTransform


class TransformPipeline:
    def __init__(self):
        self._transforms = list()
        self._cache = dict()
        self._is_caching = False

    def add_transform(self, transform: AbstractTransform):
        self._transforms.append(transform)

    def add_transform_func(self, func: Callable[[Any], Any]):
        self.add_transform(FuncTransform(func))

    def cache_transforms(self):
        self._is_caching = True

    def stop_cache_transforms(self):
        self._is_caching = False

    def clear_cache_transforms(self):
        self._cache.clear()

    def fit(self, groups: List[List[str]]):
        for t in self._transforms:
            t.fit(groups, pipeline=self)

    def transform(self, s: str) -> Any:
        if s in self._cache:
            return self._cache[s]

        transformed_s = s
        for t in self._transforms:
            transformed_s = t.transform(transformed_s)
        if self._is_caching:
            self._cache[s] = transformed_s
        return transformed_s

    def custom_transform(self, s: str, apply_before_transform: AbstractTransform) -> Any:
        for t in self._transforms:
            if t == apply_before_transform:
                break
            s = t.transform(s)
        return s
