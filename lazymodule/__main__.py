import sys
import modifymodule

def main():
	args = sys.argv[1:]
	if(args[0] == 'init'):
		modifymodule.init_module(args[1])

	if(args[0] == 'gen_swig'):
		modifymodule.gen_swig()

if __name__ == '__main__':
	main()