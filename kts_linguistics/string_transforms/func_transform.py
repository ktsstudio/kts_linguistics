from typing import Callable

from kts_linguistics.string_transforms.abstract_transform import AbstractTransform


class FuncTransform(AbstractTransform):
    def __init__(self, func: Callable[[str], str]):
        self.func = func

    def transform(self, s: str):
        return self.func(s)