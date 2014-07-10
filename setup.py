


"""Setup script for Robot's DatabaseLibrary distributions"""

import sys, os
from setuptools import setup, find_packages

setup(
    name="robotframework-databaselibrary",
    version="0.6.1",
    packages=find_packages(),
    install_requires=['robotframework']
)
