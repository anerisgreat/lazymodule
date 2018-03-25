import sys
import modifymodule

def main(args):
	if(args[0] == 'init'):
		modifymodule.init_module(args[1], args[2])

if __name__ == '__main__.py':
	main(sys.argv[1:])