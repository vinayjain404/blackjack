#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='Blackjack',
      version='1.0',
      description='Blackjack gambling game',
      author='Vinay Jain',
      author_email='vinayjain404@gmail.com',
      install_requires=['Flask']
     )
