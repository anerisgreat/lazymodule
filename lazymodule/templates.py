template_setup_py = """#Setup script. Made with lazymodule
from distutils.core import setup, Extension

setup(
	name = '$module_name',
	version	= '0.1',
	author = '$author',
	description = \"\"\"DESCRIPTION_HERE\"\"\",
	packages = ['$module_name'],
	install_requires=[],
	)
"""