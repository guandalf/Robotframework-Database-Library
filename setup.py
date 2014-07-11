

"""Setup script for Robot's DatabaseLibrary distributions"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

setup(
    name="robotframework-databaselibrary",
    version="0.6.1",
    package_dir  = { '' : 'src'},
    packages = ['DatabaseLibrary'],
    install_requires=['robotframework']
)
