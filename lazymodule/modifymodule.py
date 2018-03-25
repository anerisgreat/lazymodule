import os
import templates
from helpers import quick_create, touch, make_template_file

def init_module(module_name, author):
	print(module_name)
	print(author)
	quick_create(module_name)
	touch(os.path.join(module_name, '__init__.py'))

	namespace = {
		'author' : author,
		'module_name' : module_name
	}
	
	make_template_file(
		template_str = templates.template_setup_py,
		file_name = 'setup.py',
		namespace = namespace)
	
