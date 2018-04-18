import os
import ntpath
from glob import glob
import sys

import templates
from helpers import quick_create, touch, make_template_file

def init_module(module_name):
	print('Creating module: ' + module_name)

	#Creating Python directory
	quick_create(module_name)

	quick_create(module_name + '/lib')
	quick_create(module_name + '/include')
	
	#Creating __init__.py file in Python directory
	touch(os.path.join(module_name, '__init__.py'))

	namespace = {
		'module_name' : module_name
	}
	
	make_template_file(
		template_str = templates.template_setup_py,
		file_name = 'setup.py',
		namespace = namespace)

	make_template_file(
		template_str = templates.template_setup_config_py,
		file_name = 'setup_config.py',
		namespace = namespace)

	make_template_file(
		template_str = templates.template_setup_sh,
		file_name = 'setup.sh',
		namespace = namespace)

	make_template_file(
		template_str = templates.template_gitignore,
		file_name = '.gitignore',
		namespace = namespace)


def gen_swig():
	print('Generating swig module')
	
	sys.path.append(os.getcwd())
	import setup_config as config_mod
	module_name = config_mod.module_name
	print('Detected module: ' + module_name)

	header_names = [ntpath.basename(full_name) for full_name in glob(module_name + '/include/*.h')]
	header_names += config_mod.swig_wrapped_headers

	print('Headers to include: ')
	for header_name in header_names:
		print(header_name)

	print('Starting..')
	namespace = {
		'module_name' : module_name,
		'header_names' : header_names
	}

	make_template_file(
		template_str = templates.template_module_i,
		file_name = module_name + '/' + module_name + '.i',
		namespace = namespace)

	print('Finished creating ' + module_name + '.i')
	