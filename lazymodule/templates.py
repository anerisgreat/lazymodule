template_setup_py = """#Setup script. Made with lazymodule
from distutils.core import setup, Extension
import setup_config

module_extention = Extension('_$module_name',
	sources = setup_config.build_sources,
	include_dirs = setup_config.build_include_dirs,
	libraries = setup_config.libraries, 
	library_dirs = setup_config.lib_dirs,
	runtime_library_dirs = setup_config.lib_dirs,
	swig_opts = ['-c++', '-modern'	] + ['-I'+build_include_dir for build_include_dir in setup_config.build_include_dirs]

setup(
	name = '$module_name',
	version	= '0.1',
	author = 'setup_config.author',
	description = setup_config.description,
	ext_modules = [module_extention],
	packages = ['$module_name'],
	install_requires=[],
	)
"""

template_setup_config_py = """#Setup configuration. Made with lazymodule
module_name = '$module_name'

author = 'AUTHOR NAME HERE'
description = \"\"\"Enter a brief description of your project here.
This could be anything.
\"\"\"


#Include directories:
from glob import glob
build_include_dirs = ['$module_name/include/']
#Add this line to include another directory
#build_include_dirs += ['path/to/include']

#Extra libraries
lib_dirs = ['/usr/local/lib']
#Add  this line to use another library directory
#lib_dirs += ['/path/to/library']

#Add libraries you want to use to this list
#If the .so file is named libMyLibrary.so, add 'MyLibrary'
libraries = []

#Source files
build_sources = glob('$module_name/lib/*.cpp')
build_sources += glob('$module_name/lib/*.cxx')
build_sources += glob('$module_name/*.i')
#To add more sources, use this line to include all cpp files from a directory
build_sources += glob('some/relative/path/*.cpp')
"""

template_module_i = """//Template for swig wrapper. Made with lazymodule
%include <std_string.i>

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

template_setup_sh """#Setup bash script. Made with lazymodule
#Install dependencies here if necessary

#Generating swig file.
python -m lazymodule gen_swig

#Building project
sudo python setup.py install
"""

template_gitignore = """*.pyc
build
"""