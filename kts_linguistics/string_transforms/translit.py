from transliterate import translit

from kts_linguistics.string_transforms.abstract_transform import AbstractByWordTransform


class TranslitTransform(AbstractByWordTransform):
    def transform_word(self, s: str) -> str:
        return translit(s, 'ru')
