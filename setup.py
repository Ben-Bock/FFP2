#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


with open('README.md', 'r') as fp:
    README = fp.read()


setup(
    name='ffp2',
    version='0.1',
    description='File-Finger-Print generator ',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Ben Bock',
    author_email='benbock@live.de',
    url='https://github.com/Ben-Bock/FFP2',
    license='MIT License',
    packages=find_packages(),
    platforms='any',
    python_requires='>=3.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)