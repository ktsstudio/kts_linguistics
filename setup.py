from distutils.core import setup

dependencies = []
with open('requirements.txt') as f:
    for line in f:
        if line != '':
            dependencies.append(line)

setup(
    name='kts_linguistics',
    version='',
    packages=['kts_linguistics', 'kts_linguistics.transforms'],
    description='',
    install_requires=dependencies,
)
