try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from sys import exit,version
import sys

setup(
    name='VstsPy',
    packages=["vstspy"],
    install_requires=['requests'],
    requires=['requests'],
    version='1.0',
    url='http://www.github.com/caanaan/VstsPy',
    keywords="visual studio online api",
    license='BSD',
    author='Thomas, N Luke',
    description='Python wrapper for the VSTS API.',
    )

