#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='django-building-blocks',
      version='0.1',
      description='composable approach to reusable building blocks for django',
      author='Laurent Peuch',
      #long_description='',
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/django-building-blocks',
      install_requires=['django>=2.1'],
      packages=['building_blocks'],
      license= 'MIT',
      keywords='django components composition generic reusable',
     )
