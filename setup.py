from setuptools import find_packages
from setuptools import setup

setup(
    name='topically',
    version='0.1.0',
    description='Topic modeling using managed large language models from Cohere',
    author='Jay Alammar',
    author_email='jay@cohere.ai',
    packages=find_packages(),
    install_requires=[  # streamlit, cohere, altair, pandas, umap
        "cohere >= 2.1",
        "umap-learn >= 0.5.",
        "streamlit >= 1.12",
        "altair >= 4.2",
        "pandas >= 1.4",
        "matplotlib >= 3.5",
    ])
