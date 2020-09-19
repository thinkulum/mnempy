
from setuptools import setup, find_packages
from mnempy.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='mnempy',
    version=VERSION,
    description='Tools for creating a dictionary of mnemonic substitutes',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Andy Culbertson',
    author_email='thinkulum@gmail.com',
    url='https://github.com/thinkulum/mnempy',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'mnempy': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        mnempy = mnempy.main:main
    """,
)
