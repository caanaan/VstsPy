## Imports ##
import requests
from VstsPy import VstsPy

## Settings ##
vsts_url = 'https://<yourVSTSinstance>.visualstudio.com'
username = '<your_login>'
password = '<your_password>'

## Error Supression ##
#Supress the SNIMissingWarning - not needed for the demo, just supressing an annoying error I was seeing.
from requests.packages.urllib3.exceptions import SNIMissingWarning
requests.packages.urllib3.disable_warnings(SNIMissingWarning)
from requests.packages.urllib3.exceptions import InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

## Main Script ##
#Create a new VstsPy instance
vstsInstance = VstsPy.VstsPy(vsts_url, username, password)

#Example - Get all projects, all repos in each project, and looking for a
# specific file in each repo.
for proj_name in vstsInstance.get_project_name_list():
   print "+Project {}".format(proj_name)

   for repo_name in vstsInstance.get_repo_name_list(proj_name):
      print " -Repo: {}".format(repo_name)

      file = vstsInstance.get_file_from_repo(proj_name, repo_name, "/README.md")
      if(file.status_code == 200):
	 print file.text
      else:
	print "  *No {} on {} branch".format('/README.md', 'master')

#Example - Get the JSON response for a set of projects
print(vstsInstance.pprint_json(vstsInstance.get_project_json_list()))

