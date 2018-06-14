from os.path import join as pathjoin
import os
import ntpath
from glob import glob
import sys

from helpers import quick_create, make_template_file, quick_read

def init_package(package_name):
	print('Creating package: ' + package_name)
	#Creating Python directory
	quick_create(package_name)

	quick_create(pathjoin(package_name, 'lib'))
	quick_create(pathjoin(package_name, 'include'))
	
	namespace = {
		'package_name' : package_name
	}
	
	make_template_file(
		template_str = quick_read(pathjoin('templates', 'temp_setup.py')),
		file_name = 'setup.py',
		namespace = namespace)

	make_template_file(
		template_str = quick_read(pathjoin('templates', 'temp_setup_config.py')),
		file_name = 'setup_config.py',
		namespace = namespace)

	make_template_file(
		template_str = quick_read(pathjoin('templates', 'temp_setup.sh')),
		file_name = 'setup.sh',
		namespace = namespace)

	make_template_file(
		template_str = quick_read(pathjoin('templates','temp_.gitignore')),
		file_name = '.gitignore',
		namespace = namespace)

	make_template_file(
		template_str = quick_read(pathjoin('templates','temp___init__.py')),
		file_name = pathjoin(package_name, '__init__.py'),
		namespace = namespace)

	make_template_file(
		template_str = quick_read(pathjoin('templates','temp_MANIFEST.in')),
		file_name = 'MANIFEST.in',
		namespace = namespace)

	make_template_file(
		template_str = quick_read(pathjoin('templates','temp___main__.py')),
		file_name = pathjoin(package_name, '__main__.py'),
		namespace = namespace)

#Creates class or code
def add_source(file_name, is_class):
	sys.path.append(os.getcwd())
	import setup_config as config_mod
	package_name = config_mod.package_name

	print('Detected package: ' + package_name)
	if(is_class):
		new_class(package_name, file_name)
	else:
		new_code(package_name, file_name)

#Creates new class files
def new_class(package_name, class_name):
	namespace = {
		'package_name' : package_name,
		'file_name' : class_name
	}

	print('Creating new class: ' + class_name)

	header_fname = pathjoin(package_name, 'include', (class_name + '.h'))
	print('Creating file: ' + header_fname)
	make_template_file(
		template_str = quick_read(pathjoin('templates', 'temp_class.h')),
		file_name = header_fname,
		namespace = namespace)

	code_fname = pathjoin(package_name, 'lib', (class_name + '.cpp'))
	print('Creating file: ' + code_fname)
	make_template_file(
		template_str = quick_read(pathjoin('templates', 'temp_class.cpp')),
		file_name = code_fname,
		namespace = namespace)

#Creates new simple code file
def new_code(package_name, file_name):
	namespace = {
		'package_name' : package_name,
		'file_name' : file_name
	}

	print('Creating code: ' + file_name)

	header_fname = pathjoin(package_name, 'include', (file_name + '.h'))
	make_template_file(
		template_str = quick_read(pathjoin('templates', 'temp_code.h')),
		file_name = header_fname,
		namespace = namespace)

	code_fname = pathjoin(package_name, 'lib', (file_name + '.cpp'))
	make_template_file(
		template_str = quick_read(pathjoin('templates', 'temp_code.cpp')),
		file_name = code_fname,
		namespace = namespace)