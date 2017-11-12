import transliterate
from transliterate.base import TranslitLanguagePack

from kts_linguistics.string_transforms.abstract_transform import AbstractByWordTransform


class TranslitTransform(AbstractByWordTransform):
    def __init__(self):
        super().__init__()

        cls = transliterate.utils.get_language_pack('ru')
        self.language_pack: TranslitLanguagePack = cls()

    def transform_word(self, s: str) -> str:
        return self.language_pack.translit(s)
