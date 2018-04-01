from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='crawl4us',
    version='0.1.3',
    description='A Python web crawler looking wildly for tables',
    long_description=long_description,
    url='https://github.com/camilamaia/crawl4us',
    author='Camila Maia',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='sample setuptools development web scraping crawler ',

    py_modules=["crawl4us"],
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    install_requires=[
        'beautifulsoup4',
        'requests',
        'pandas'
    ],
    extras_require={  # Optional
        'dev': ['pylint'],
        'test': ['pytest'],
    },

    project_urls={
        'Bug Reports': 'https://github.com/camilamaia/crawl4us/issues',
        'Source': 'https://github.com/camilamaia/crawl4us',
    },
)
