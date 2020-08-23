from os.path import join as pathjoin
import sys
import argparse
import os
import ntpath
from glob import glob

from Cheetah.Template import Template

def quick_create(path_name):
	if not os.path.exists(path_name):
		os.makedirs(path_name)

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def make_template_file(template_str, file_name, namespace):
	newfile = open(file_name, 'w+')
	newfile.write(str(Template(template_str, searchList = [namespace])))
	newfile.close()

def quick_read(path):
	packagedir, filename = os.path.split(__file__)
	full_file_path = os.path.join(packagedir, path)
	with open(full_file_path, 'r') as file:
		ret = file.read()
	return ret

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

class lazypackage_command_parser(object):
	def __init__(self, args):
		argp = argparse.ArgumentParser('LazyPackage',
			description = '''Run the LazyPackage command you want.
''',
			epilog = 'Type -h after command name to view help about that command.',
			usage = '''python -m lazypackage <command>''')

		argp.add_argument('command', help = '''<newpackage/addsource>''')
		if(len(args) == 0):
			print('No command.')
			argp.print_help()
			exit(0)

		parsed = argp.parse_args([args[0]])
		if(not hasattr(self, parsed.command)):
			print('Unrecognized command.')
			argp.print_help()
			exit(0)

		getattr(self, parsed.command)(args[1:])

	def addsource(self, args):
		parser = argparse.ArgumentParser('addsource',
			description = 'Add a C++ code snippet from a template.',
			epilog = 'Note: You may also add code by placing it in the appropriate folder.')

		parser.add_argument('-c', action = 'store_const', const = True, default = False, help = 'Whether to create a new class file. If not present, will generate simple code file.')
		parser.add_argument('name', action = 'store', help = 'The name of the class / code file.')
		parsed = parser.parse_args(args)

		add_source(file_name = parsed.name, is_class = parsed.c)

	def newpackage(self, args):
		parser = argparse.ArgumentParser('newpackage',
			description = 'Create a new LazyPackage from the template in the current directory.',
			epilog = 'This command will create the package in the current directory and override existing files.')

		parser.add_argument('name', action = 'store', type = str, help = 'The name of the LazyPackage.')
		parsed = parser.parse_args(args)
		init_package(parsed.name)

def main(args):
	lazypackage_command_parser(args)

if __name__ == '__main__':
	main(sys.argv[1:])
