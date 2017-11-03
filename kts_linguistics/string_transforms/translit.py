from transliterate import translit

from kts_linguistics.string_transforms.abstract_transform import AbstractTransform, AbstractByWordTransform


class TranslitTransform(AbstractTransform):
    def transform(self, s: str) -> str:
        return translit(s, 'ru')


class TranslitByWordTransform(AbstractByWordTransform):
    def transform_word(self, s: str) -> str:
        return translit(s, 'ru')
