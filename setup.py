#!/usr/bin/env python3

from setuptools import setup

setup(
    name="pywebpoc",
    version='0.0.0',
    install_requires=[
        'webruntime',
        'dialite',
        'aiohttp',
        ],
    packages=[],
    scripts=['main.py'],
    description="pywebpc",
)
