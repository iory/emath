#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
from emath import __author__, __version__, __licence__

setup(
    name             = "emath",
    version          = __version__,
    description      = "Python Library for Number Theory",
    license          = __licence__,
    author           = __author__,
    author_email     = "ab.ioryz@gmail.com",
    url              = "hrrps://github.com/iory/emath.git",
    packages         = find_packages(),
    install_requires = [],
)
