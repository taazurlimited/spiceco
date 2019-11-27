# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in spiceco/__init__.py
from spiceco import __version__ as version

setup(
	name='spiceco',
	version=version,
	description='spiceco',
	author='kkulloters',
	author_email='vanessa.bualat01@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
