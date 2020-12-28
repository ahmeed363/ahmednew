# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ahmednew/__init__.py
from ahmednew import __version__ as version

setup(
	name='ahmednew',
	version=version,
	description='ahmedNew',
	author='ahmed',
	author_email='d',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
