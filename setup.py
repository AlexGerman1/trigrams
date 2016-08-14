# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="trigrams",
    description="This package will create a new story from a text file.",
    version=0.1,
    license='MIT',
    author="Victor Benavente, Alex German",
    author_email="vbenavente@hotmail.com, Alexgerman11233@gmail.com",
    py_modules=['trigrams'],
    package_dir={' ': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch']},
    entry_points={
        'console_scripts': [
            'trigrams=src.trigrams:call_all'
        ]
    }
)
