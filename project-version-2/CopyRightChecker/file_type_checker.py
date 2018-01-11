def get_file_type(file_name):


	### curently i am using file extensions to determine whether it is source file or not 


	### In future i would imporove it 

	### Assumptions :- 
	### filenames are perfectly formed and importantly it has only . in the name 
	### 
	def rule_1():
		try:
			a,b=file_name.split('.')

			### returns extensions
			return b
		except ValueError:

			print('-------------------\n'+'malformed file : '+file_name+'\n------------------')
			# exit()



	def rule_2():
		import os



	def rule_3():
		pass

	return rule_1()


def check_extension(extension):

	from copyright_filetype import source_files,cfg_files,data_files

	if extension in source_files:
		return 1

	if extension in cfg_files:
		return 2

	if extension in data_files:
		return 3

	return 4
	
