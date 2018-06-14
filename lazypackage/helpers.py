import os
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