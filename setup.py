#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

from ISESolutions import __version__, __name__
from setuptools import find_packages, setup


with open("README.md", "r") as file:
    long_description = file.read()

with open("requirements/common.txt", "r") as file:
    requirements = [line.strip() for line in file]

setup(
    name=__name__,
    version=__version__,
    description="A project aimed at creating solutions"
                " solutions for Information Science exams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="0dminnimda",
    author_email="0dminnimda.contact@gmail.com",
    packages=find_packages(),
    license="MIT",
    install_requires=requirements,
    python_requires="~=3.9",
)
