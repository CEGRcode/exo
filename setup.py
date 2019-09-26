#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=7.0','matplotlib','numpy', 'pyfiglet' ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Prashant Kumar Kuntala",
    author_email='prashantkuntala@gmail.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    description="Quality Control and Visualization utilities for Yeast Epigenome Project ",
    entry_points={
        'console_scripts': [
            'exo=exo.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='exo',
    name='exo',
    packages=find_packages(include=['exo',]),
    url='https://github.com/CEGRcode/exo',
    version='0.1.0',
)
