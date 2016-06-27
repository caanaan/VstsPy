import json
import requests
from requests.compat import urljoin
import urllib
import urlparse
import os.path
import posixpath

class RestHelper:
   'Default Restful API URL creation and usage class'

   #Private class attributes
   __PATH_URL_PARTS_EL = 2
   __QUERY_URL_PARTS_EL = 4

   #Class constructor
   def __init__(self, rest_base_path):
      self.__get_base_url_list()
   
   ### Private Methods ###
   #Function to split a path into a list
   def __path_split(self, path):
      #Create default empty list to return
      return_path = []
      #If the input path was empty, just return
      if(path == ""):
         return return_path
      #Otherwise, process the path
      tmp = path
      while tmp != "/":
         (tmp, item ) = posixpath.split(tmp)
         return_path.insert(0, item)
      return return_path

   #Function to create a path string from a list of its component elements
   def __path_join(self, path_list):
      return "/".join(path_list)

   #Function to append a string to the current path in inUrlParts
   def __path_append(self, url_list, path_list):
      path = self.__path_split(url_list[self.__PATH_URL_PARTS_EL])
      path.append(path_list)
      url_list[self.__PATH_URL_PARTS_EL] = self.__path_join(path)
      return

   #Function to parse the URL parts from a base VSTS URL
   def __get_base_url_list(self):
      #NOTE - this urlparse function assumes you have a valid path, and will not return the right stuff if not.  Should handle this...
      self.url_list = list(urlparse.urlparse(self.vsts_base_path, True))
      return self.url_list

   #Function to set the query portion of the URL using the dictionary of arguments and values.
   def __update_query(self, url_list, query_dict):
      query = dict(urlparse.parse_qsl(url_list[self.__QUERY_URL_PARTS_EL]))
      query.update(query_dict)
      url_list[self.__QUERY_URL_PARTS_EL] = urllib.urlencode(query)
      return

   #Function to create a URL string from a set of URL parts parsed by urlparse
   def __create_url(self, url_list):
      return urlparse.urlunparse(url_list)

   ## Public Methods ##
   #Function to generate a generic VSTS RESTful API from a path list and query dictionary
   def geturl_generic(self, path_list, query_dict):
      #Get the URL parts
      url_list = self.__get_base_url_list()
      #Update the path
      self.__path_append(url_list, self.__path_join(path_list))
      #Update the query
      self.__update_query(url_list, query_dict)
      #Create the URL
      url = self.__create_url(url_list)
      self.url = url

   #Function to issue a get request to the RESTful API, enabling default users and passwords
   def issue_request(self):
      return requests.get(self.url, auth=(self.username, self.password))           

   #Function to pretty print a Json object
   def pprint_json(self, inJson):
      print json.dumps(inJson, indent=2, sort_keys=True)
      return
