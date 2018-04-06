template_setup_py = """#Setup script. Made with lazymodule
from distutils.core import setup, Extension
import setup_config

module_extention = Extension('_$module_name',
	sources = setup_config.build_sources,
	include_dirs = setup_config.build_include_dirs,
	swig_opts = ['-c++', '-modern'	] + ['-I'+build_include_dir for build_include_dir in setup_config.build_include_dirs]

setup(
	name = '$module_name',
	version	= '0.1',
	author = '$author',
	description = \"\"\"DESCRIPTION_HERE\"\"\",
	cmdclass={'build_ext': lazy_build_ext}
	ext_modules = [module_extention]
	py_modules = ['$module_name']
	install_requires=[],
	)
"""

template_setup_config_py = """#Setup configuration. Made with lazymodule
module_name = '$module_name'

#Include directories:
from glob import glob
build_include_dirs = ['$module_name/include/']

#Source files
build_sources = glob('$module_name/lib/*.cpp')
build_sources += glob('$module_name/lib/*.cxx')
build_sources += glob('$module_name/*.i')
"""

template_module_i = """//Template for swig wrapper. Made with lazymodule
%module $module_name
%{
#for $header_name in $header_names
	\#include "$header_name"
#end for
%}

#for $header_name in $header_names
%include "$header_name"
#end for

"""