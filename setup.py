# This Python file uses the following encoding: utf-8
from setuptools import setup
from glob import glob

with open("README.md", "r") as f:
    long_description = f.read()

settings = {
    'name': 'Verteste',
    'version': '1.0.0b',
    'description': 'Aplicativo construído para teste da Vertesis',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'url': 'http://github.com/Chum4k3r/Verteste',
    'author': 'João Vitor Paes',
    'author_email': 'joaovitorgpaes@gmail.com',
    'license': 'MIT',
    'install_requires': ['PySide6'],
    'packages': ['verteste', 'verteste.model', 'verteste.ui'],
    'package_dir': {'verteste': 'verteste',
                    'verteste.model': 'verteste/model',
                    'verteste.ui': 'verteste/ui'},
    'data_files': [('examples', glob('examples/*'))],
    'classifiers': [
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", ],
    'python_requires': '>=3.6',
}

setup(**settings)
