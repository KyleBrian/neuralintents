from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'Simple interface for working with intents and chatbots.'
LONG_DESCRIPTION = 'Simple interface for working with intents and chatbots.'
setup(
    name="neuralintents",
    version=VERSION,
    author="NeuralNine (Florian Dedov)",
    author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'nltk', 'tensorflow'],
    extras_require={
        'testing': ['pytest'],  # Optional testing dependency
    },
    keywords=['python', 'neural', 'machine learning', 'chatbots', 'chat', 'artificial intelligence', 'virtual assistant', 'deep learning', 'tensorflow'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ]
)
