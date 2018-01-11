def app_copy_right(path_name=None,file_name=None,file_object=None):

	


	### status 1 succesfully appended 
	### status 2 

	### writes log file 

	logfile = open('log1.txt','a')
	failed_files = open('failed_files.txt','a')




	if path_name==None:
		path_name=''

	#### import fileextensions from copyright_filetype module

	from copyright_filetype import copy_right	

	### import get_file_type to get the file types 


	from file_type_checker import get_file_type,check_extension

	extension=get_file_type(file_name)

	### check extensions if extensions are whether java/go/shell scripts or something


	extension_type = check_extension(extension)

	## extension_type 1 means they are source files 

	if extension_type==1:
		# print(file_name+' is source code file and  checking for Copyright\n ')
		
		# logfile.write('\n'+file_name+' is source code file and  checking for Copyright\n ')

		ibm_copyright=copy_right(extension)

		with open(path_name+'//'+file_name,'r') as file_:
			source_code=file_.read()
			file_.close()

		

		### checks 'copyright' word in file then takes action depending on the if word is present or not
		# print('copyright' in source_code.lower())



		if 'copyright' not in source_code.lower():
			# print('file : '+file_name+"   hasn't got got IBM Copyright\n")
			# print(source_code+'\n---------------------------'*2)
			with open(path_name+'//'+file_name,'w') as fil :
				fil.write(ibm_copyright.rstrip('\r\n')+'\n'+source_code)
				fil.close()
				### if file has sucesfully appended copyright then status is 1 
				logfile.write('-----'*10+'\n copy_right appended to file_name : '+file_name+'\n'+'-----'*10)
			print('-----'*10+'\n copy_right appended to file_name : '+file_name+'\n'+'-----'*10)
		else:
			logfile.write('path_name : '+path_name+'file_name : '+file_name+'status : '+str(1))
			# print('file : '+file_name+"   has already got IBM Copyright\n")

	### if extension is 3 we show allowed formats and log the failed files names 
	elif extension_type==4:
		logfile.write('\n'+'-----'*10+'\nunhandleable format file : '+file_name+'\n'+'-----'*10+'\n')
		failed_files.write('\n'+'-----'*10+'\nunhandleable format file : '+file_name+'\n'+'-----'*10+'\n')
		print('\n'+'-----'*10+'\nunhandleable format file : '+file_name+'\n'+'-----'*10+'\n')
	logfile.close()
	failed_files.close()


# app_copy_right(file_name='Test1.java')