from distutils.core import setup

dependencies = []
with open('requirements.txt') as f:
    for line in f:
        if line != '':
            dependencies.append(line)

setup(
    name='kts_spellcheck',
    version='',
    packages=['kts_spellcheck', 'kts_spellcheck.transforms'],
    description='',
    install_requires=dependencies,
)
