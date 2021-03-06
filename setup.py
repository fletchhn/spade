#!/usr/bin/env python
from setuptools import setup

setup(
    name='spade',
    version='0.1',
    description='File format reverse engineering tool.',
    url='https://github.com/nyxxxie/spade',
    author='Nyxxie et al.',
    author_email='nyxxxxie@gmail.com',
    license='GNU GPL v3',
    packages=['spade'],
    install_requires=[
        'PyQt5',
        'pyyaml',
        'sqlalchemy',
        'Sphinx',
        'pytest'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    zip_safe=False
)
