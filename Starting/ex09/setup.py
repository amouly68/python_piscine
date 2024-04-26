# setup.py

from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    author='tonio',
    author_email='tonio@42.fr',
    description='A sample test package',
    url='https://github.com/tonio/ft_package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
