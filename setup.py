from distutils.core import setup, Extension

setup(
	name = 'lazymodule',
	version	= '0.1',
	author = "Aner Zakovitch",
	description = """Creates python projects easily from terminal!""",
	packages = ['lazymodule'],
	entry_points = {
        'console_scripts': [
        'lazymodule=lazymodule.__main__:main',
        ],
    },
	install_requires=['cheetah'],
	)
	