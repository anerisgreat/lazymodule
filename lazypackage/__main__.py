import sys
import modifypackage
import argparse

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

		modifypackage.add_source(file_name = parsed.name, is_class = parsed.c)

	def newpackage(self, args):
		parser = argparse.ArgumentParser('newpackage',
			description = 'Create a new LazyPackage from the template in the current directory.',
			epilog = 'This command will create the package in the current directory and override existing files.')

		parser.add_argument('name', action = 'store', type = str, help = 'The name of the LazyPackage.')
		parsed = parser.parse_args(args)
		modifypackage.init_package(parsed.name)

def main(args):
	lazypackage_command_parser(args)

if __name__ == '__main__':
	main(sys.argv[1:])
