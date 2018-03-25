from distutils.core import setup, Extension

setup(
	name = 'lazymodule',
	version	= '0.1',
	author = "Aner Zakovitch",
	description = """Creates python projects easily from terminal!""",
	py_modules = ['lazymodule'],
	install_requires=['cheetah'],
	
	)
	