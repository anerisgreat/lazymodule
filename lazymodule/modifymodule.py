import os
import ntpath
from glob import glob

import templates
from helpers import quick_create, touch, make_template_file

def init_module(module_name, author):
	print(module_name)
	print(author)

	#Creating Python directory
	quick_create(module_name)

	quick_create(module_name + '/lib')
	quick_create(module_name + '/include')
	
	#Creating __init__.py file in Python directory
	touch(os.path.join(module_name, '__init__.py'))

	namespace = {
		'author' : author,
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

	
def gen_swig():
	#try:
		print('Generating swig module')
		config_mod = __import__('setup_config', fromlist=[''])
		module_name = config_mod.module_name
		header_names = [ntpath.basename(full_name) for full_name in glob(module_name + '/include/*.h')]

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
	#except:
		#print('Error generating swig file.!')