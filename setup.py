#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""The setup script."""


from setuptools import setup, find_packages


with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]


# PEP 440 -- Version Identification and Dependency Specification
# https://www.python.org/dev/peps/pep-0440/

setup(
    author="Zachary Jonathan Kneupper",
    author_email="zachary.kneupper@gmail.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Inspect python object code with colorful syntax highlighting",
    entry_points={"console_scripts": ["codecolor=codecolor.cli:main",],},
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="codecolor",
    name="codecolor",
    packages=find_packages(include=["codecolor", "codecolor.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/zkneupper/codecolor",
    version="0.0.2", # version="0.0.dev2", <- last test
    zip_safe=False,
)
