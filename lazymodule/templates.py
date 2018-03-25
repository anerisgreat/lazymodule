template_setup_py = """
from distutils.core import setup, Extension

setup(
	name = '$module_name',
	version	= '0.1',
	author = '$author',
	description = \"\"\"DESCRIPTION_HERE\"\"\",
	py_modules = ['$module_name'],
	install_requires=[],
	
	)
"""