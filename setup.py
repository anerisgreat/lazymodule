from distutils.core import setup, Extension
from glob import glob

setup(
	name = 'lazypackage',
	version	= '1.0',
	author = "Aner Zakovitch",
	description = """Creates python projects easily from terminal!""",
	packages = ['lazypackage'],
	entry_points = {
        'console_scripts': [
        'lazypackage=lazypackage.__main__:main',
        ],
    },
    package_data = {'templates':glob('lazypackage/templates/*')},
    install_requires = [], #Requires cheetah but local repository does not have it
	include_package_data = True
	)
