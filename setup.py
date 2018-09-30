#!/usr/bin/env python
"""
Copyright 2018 Sigvald Marholm <marholm@marebakken.com>

This file is part of pyJunk.

pyJunk is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyJunk is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pyJunk  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup
from io import open # Necessary for Python 2.7

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

with open('.version') as f:
    version = f.read().strip()

setup(name='pyJunk',
      version=version,
      description='A junkyard of Python functions, classes and snippets I find myself using surprisingly often! Sometimes there's gold in a junkyard.',
      long_description=long_description,
      author='Sigvald Marholm',
      author_email='marholm@marebakken.com',
      url='https://github.com/sigvaldm/pyJunk.git',
      py_modules=['pyJunk'],
      #install_requires=['scipy','frmt'],
      license='LGPL',
      classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        ]
     )

