from transliterate import translit

from kts_linguistics.string_transforms.abstract_transform import AbstractTransform


class TranslitNormalizeTransform(AbstractTransform):
    def transform(self, s: str) -> str:
        return translit(s, 'ru')
