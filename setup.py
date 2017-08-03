#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

py3 = sys.version_info.major == 3

if py3:
    import io
    import configparser

    StringIO = io.StringIO
    config_parser = configparser.ConfigParser
else:
    import cStringIO
    import ConfigParser

    config_parser = ConfigParser.ConfigParser
    StringIO = cStringIO.StringIO

config_IO = StringIO()
config_IO.write("[main]\n")
with open("PackageInfo.cfg") as f:
    config_IO.write(f.read())
config_IO.seek(0, os.SEEK_SET)
config = config_parser()
config.optionxform = str
config.readfp(config_IO)
info = dict(config.items("main"))

setup(name=info['PACKAGE'],
      version="%(MAJOR)s.%(MINOR)s.%(MICRO)s%(TAG)s" % info,
      author=info['AUTHOR'],
      author_email=info['EMAIL'],
      url=info['URL'],
      description=info['DESCRIPTION'],
      license=info['LICENSE'],
      long_description=open('README.rst').read(),
      packages=find_packages(),
      package_data={'': [os.path.join('*', '*.*')]},
      include_package_data=True,
      # requires = [],
      test_suite=info['PACKAGE'] + '.tests.test_suite',
      classifiers=[
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      install_requires=[
      ],
      )
