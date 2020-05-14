try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from mnempy import __version__

config = {
    'name': 'Mnempy',
    'description': 'Tools for creating a dictionary of mnemonic substitutes',
    'author': 'Andy Culbertson',
    'author_email': 'thinkulum@gmail.com',
    'url': '',
    'download_url': '',
    'version': __version__,
    'packages': ['mnempy'],
    'install_requires': ['docutils', 'pytest', 'docopt'],
    'tests_require': ['Sphinx>=1.4.1,<2.0.0'],
}

setup(**config)
