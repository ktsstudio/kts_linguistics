from typing import Callable, Any, List

from nltk import ToktokTokenizer

from kts_linguistics.string_transforms.abstract_transform import AbstractTransform, AbstractByWordTransform


class FuncTransform(AbstractTransform):
    def __init__(self, func: Callable[[Any], Any]):
        self.func = func

    def transform(self, s: Any) -> Any:
        return self.func(s)


class FuncByWordTransform(AbstractByWordTransform):
    def __init__(self, func: Callable[[str], Any]):
        self.func = func

    def transform_word(self, s: str) -> Any:
        return self.func(s)


class TokenizeTransform(AbstractTransform):
    def __init__(self, tokenizer=None):
        self.tokenizer = tokenizer or ToktokTokenizer()

    def transform(self, s: str) -> List[str]:
        return self.tokenizer.tokenize(s)


class JoinTransform(AbstractByWordTransform):
    def __init__(self, join_str=' '):
        self.join_str = join_str

    def transform(self, l: List[str]) -> str:
        return self.join_str.join(w for w in l if w != '')


class StartOneWordPipelineUtilityTransform(AbstractTransform):
    def transform(self, s: str) -> List[str]:
        return [s]


class EndOneWordPipelineUtilityTransform(AbstractTransform):
    def transform(self, l: List[str]) -> str:
        return l[0]


class RemoveEmptyWordsTransform(AbstractTransform):
    def transform(self, l: List[str]) -> List[str]:
        return [w for w in l if w != '']
