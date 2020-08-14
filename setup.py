# -*- coding: utf-8 -*-

from setuptools import setup

kwargs = dict(
    name="general-marktoc",
    license="whatever",
    version="0.0.0.1",
    description="Generates a TOC given a Markdown file",
    author="Dan Nguyen",
    author_email="dansonguyen@gmail.com",
    url="https://github.com/dannguyen/general-marktoc",
    packages=["marktoc"],
    python_requires=">=3.7",
    install_requires=["click>=7.1.2", "regex>=2020.7"],

    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Programming Language :: Python :: 3 :: Only",

    ],


    entry_points = {
        'console_scripts': ['marktoc=marktoc.cli:main'],
    },

)


setup(**kwargs)
