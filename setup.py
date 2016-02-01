#!/usr/bin/env python
# -*- coding: utf-8 -*-

# setuptools import
from setuptools import setup, find_packages

# package information import
from ggraph import __version__, __name__

# find requirement import
from pip.req import parse_requirements

# find requirement
install_reqs = parse_requirements("requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name = __name__,
    version = __version__,
    packages = find_packages(),

    author = "Pierre Marijon",
    author_mail = "pierre@marijon.fr",
    description = "Webservice for generate graphviz",
    long_description = "Please see README on https://github.com/natir/ggraph",
    keywords = "web graphviz",
    url = "https://github.com/natir/ggraph",

    install_requires = reqs,
    include_package_data = True,

    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta"
    ]
)
