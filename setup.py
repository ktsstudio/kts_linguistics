from setuptools import setup


dependencies = []
with open('requirements.txt') as f:
    for line in f:
        if line != '':
            dependencies.append(line)

setup(
    name='kts_linguistics',
    version='0.0.23',
    packages=['kts_linguistics',
              'kts_linguistics.corpora',
              'kts_linguistics.phonetics',
              'kts_linguistics.spellcheck',
              'kts_linguistics.string_transforms',
              'kts_linguistics.synonyms',
              'kts_linguistics.test'],
    install_requires=dependencies,
    include_package_data=True
)
