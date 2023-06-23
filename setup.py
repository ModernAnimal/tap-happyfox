#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="tap-happyfox",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_gem"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-happyfox=tap_happyfox:main
    """,
    packages=find_packages(),
    package_data={"schemas": ["tap_gem/schemas/*.json"]},
    include_package_data=True,
)
