from kts_linguistics.corpora.loaders import load_precomputed_corpora
from kts_linguistics.string_transforms.basic_normalize import BasicNormalizeByWordTransform
from kts_linguistics.string_transforms.spellfix import SpellfixTransform
from kts_linguistics.string_transforms.transform_pipeline import TransformPipeline
from kts_linguistics.string_transforms.translit import TranslitTransform
from kts_linguistics.string_transforms.utility_transforms import TokenizeTransform, JoinTransform

if __name__ == '__main__':
    # setup
    pipeline = TransformPipeline()

    corpora = load_precomputed_corpora()

    pipeline.add_transform(TokenizeTransform())
    pipeline.add_transform(TranslitTransform())
    pipeline.add_transform(BasicNormalizeByWordTransform())
    pipeline.add_transform(SpellfixTransform(corpora=corpora, fix_threshold=0.3))
    pipeline.add_transform(JoinTransform())

    # test
    initial_str = 'Придложение с ашибками'
    fixed_str = pipeline.transform(initial_str)

    print(initial_str, '->', fixed_str)
