from distutils.core import setup

dependencies = []
with open('requirements.txt') as f:
    for line in f:
        if line != '':
            dependencies.append(line)

setup(
    name='kts_linguistics',
    version='0.0.5',
    packages=['kts_linguistics',
              'kts_linguistics.corpora',
              'kts_linguistics.phonetics',
              'kts_linguistics.spellcheck',
              'kts_linguistics.string_transforms',
              'kts_linguistics.synonyms',
              'kts_linguistics.test'],
    install_requires=dependencies,
)
