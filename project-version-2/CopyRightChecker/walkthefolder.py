def walk_the_folder(dirname):
	## import os 
	import os

	# print "---------------XXXXXXXXXXXXXXXXXX--------------------------"
	## import app_copy_right function

	from appendcopyright import app_copy_right


	## get current working directory 

	curr_dir=os.getcwd()


	from copyright_filetype import current_user_dir


	### get name of the directory where user cloned directory is downloaded to 


	working_dir = curr_dir+"//"+dirname
	# print working_dir,"working dir"

	### walk the dir and get dirName and filelist and send it to the append copyright function

	for dirName, subdirList, fileList in os.walk(working_dir, topdown=True):

		for fname in fileList:
				# try:
				app_copy_right(path_name=dirName,file_name=fname)
				# except FileNotFoundError:

					# print('\n-------------********------------'+'\n'+dirName,fname+'\n--------------************--------------\n')

# walk_the_folder()


