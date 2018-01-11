
# 
# 	(C) Copyright ${year} Nuxeo (http://nuxeo.com/) and others.
# 	
# 	Licensed under the Apache License, Version 2.0 (the "License");
# 	you may not use this file except in compliance with the License.
# 	You may obtain a copy of the License at
# 	
# 	    http://www.apache.org/licenses/LICENSE-2.0
# 	
# 	Unless required by applicable law or agreed to in writing, software
# 	distributed under the License is distributed on an "AS IS" BASIS,
# 	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# 	See the License for the specific language governing permissions and
# 	limitations under the License.
# 	
# 	Contributors:
# 
# 
from git import Repo 
import git
import os
import stat
import shutil,sys

# get the current working directory
cwd = os.getcwd()

dirname = ''

# handling folder download
def folder_Create_Update(git_url,repo_dir,user,repo_name,branch_name):

	# checking if the directory already exists
	if(os.path.isdir(cwd+"/"+user+"/"+ repo_name + "/" + branch_name) == False):
		
		# creating one if does not exits
		Repo.clone_from(git_url, repo_dir,branch = branch_name)
		print "cloned to "+cwd.replace("\\","/")+"/"+user+"/"+ repo_name + "/" + branch_name


		dirname = user

	# quitting the program if it already exits
	else:

		print "folder already exists"
		print "folder is in "+cwd.replace("\\","/")+"/"+user+"/"+ repo_name + "/" + branch_name
		sys.exit(0)

# get the url from which the repository has to be downloaded
def getUrl():
	
	# reading the url from command prompt
	try:
		git_url = sys.argv[1]
		branch_name = "master"
		if (len(sys.argv) == 3):
			branch_name = sys.argv[2]

		modified_git_url = git_url.replace("@","/")
		modified_git_url = modified_git_url.replace(":","/")

		user = ""
		repo_name = ""

		# splitting the url for naming the folders and subfolders													
		split_url = modified_git_url.split("/")

		print split_url

		#if the url given is ssh
		if (len(split_url) == 4):
			user = split_url[2]
			repo_name = split_url[3][:-4]
		
		# if the url given is https
		else :
			user = split_url[4]
			print user
			repo_name = split_url[5][:-4]

		# creating the download path
		repo_dir = cwd+"/"+user+"/"+ repo_name + "/" + branch_name

		folder_Create_Update(git_url,repo_dir,user,repo_name,branch_name)
	except IndexError:
		print "please check the arguments passed"
	except git.GitCommandError as e:
		print "branch does not exists"


getUrl()	

from walkthefolder import walk_the_folder


walk_the_folder(dirname)
###################################################### end of cloning the github repository ###########################################
###################################################### traversing the files and folders     ###########################################



