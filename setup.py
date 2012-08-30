#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
import os
import re

root_dir = os.path.abspath(os.path.dirname(__file__))


def get_version(package_name):
    version_re = re.compile(r"^__version__ = [\"']([\w_.-]+)[\"']$")
    package_components = package_name.split('.')
    path_components = package_components + ['__init__.py']
    with open(os.path.join(root_dir, *path_components)) as f:
        for line in f:
            match = version_re.match(line[:-1])
            if match:
                return match.groups()[0]
    return '0.1.0'


PACKAGE = 'lib_template'


setup(
    name="lib_template",
    version=get_version(PACKAGE),
    author="Raphaël Barrois",
    author_email="raphael.barrois@polytechnique.org",
    description="An example Python library.",
    license="Public domain",
    keywords=['project', 'library', 'template'],
    url="http://github.com/rbarrois/python_lib_template",
    download_url="http://pypi.python.org/pypi/python_lib_template/",
    packages=find_packages(),
    setup_requires=[
        'distribute',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    test_suite='tests',
)

