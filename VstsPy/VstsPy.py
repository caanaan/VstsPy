from Rest import RestHelper 

class VstsPy(RestHelper):
   'VSTS Api helper'

   #Class constructor
   def __init__(self, vsts_base_path, username, password):
      self.vsts_base_path = vsts_base_path
      self.username = username
      self.password = password
      RestHelper.__init__(self, vsts_base_path)
  
   ### Private Methods ###

   ### Public Methods ###
   #Project related
   def get_project_json_list(self):
      pathList = [ 'defaultcollection', '_apis', 'projects' ]
      queryDict = { 'api-version' : '1.0' }
      self.geturl_generic(pathList, queryDict)
      resp = self.issue_request()
      list = []
      for x in resp.json()['value']:
         list.append(x)
      return list

   def get_project_name_list(self, ignore_name_list = []):
      list = []
      jsonlist = self.get_project_json_list()
      for x in jsonlist:
         if x['name'] not in ignore_name_list:
            list.append(x['name'])
      return list

   def get_project_json(self, project, include_capabilities=False):
      pathList = [ 'defaultcollection', '_apis', 'projects', project ]
      queryDict = { 'api-version' : '1.0', 'includeCapabilities' : include_capabilities }
      self.geturl_generic(pathList, queryDict)
      return self.issue_request()

   #Team Related
   def get_team_json_list(self, project):
      pathList = [ 'defaultcollection', '_apis', 'projects', project, 'teams' ]
      queryDict = { 'api-version' : '1.0' }
      self.geturl_generic(pathList, queryDict)
      resp = self.issue_request()
      list = []
      for x in resp.json()['value']:
         list.append(x)
      return list

   def get_team_name_list(self, project, ignore_name_list = []):
      list = []
      jsonlist = self.get_team_json_list(project)
      for x in jsonlist:
         if x['name'] not in ignore_name_list:
            list.append(x['name'])
      return list

   #Board related
   def get_board_json_list(self, project, team):
      pathList = [ 'defaultcollection', project, team, '_apis', 'work', 'boards' ]
      queryDict = { 'api-version' : '2.0' }
      self.geturl_generic(pathList, queryDict)
      resp = self.issue_request()
      list = []
      for x in resp.json()['value']:
         list.append(x)
      return list

   def get_board_name_list(self, project, team, ignore_name_list = []):
      list = []
      jsonlist = self.get_board_json_list(project, team)
      for x in jsonlist:
         if x['name'] not in ignore_name_list:
            list.append(x['name'])
      return list

   def get_board_json(self, project, team, board):
      pathList = [ 'defaultcollection', project, team, '_apis', 'work', 'boards', board ]
      queryDict = { 'api-version' : '2.0' }
      self.geturl_generic(pathList, queryDict)
      return self.issue_request()

   #Repo related
   def get_repo_json_list(self, project):
      pathList = [ 'defaultcollection', project, '_apis/git/repositories' ]
      queryDict = { 'api-version' : '1.0' }
      self.geturl_generic(pathList, queryDict)
      resp = self.issue_request()
      list = []
      for x in resp.json()['value']:
         list.append(x)
      return list

   def get_repo_name_list(self, project, ignore_name_list = []):
      list = []
      jsonlist = self.get_repo_json_list(project)
      for x in jsonlist:
         if x['name'] not in ignore_name_list:
            list.append(x['name'])
      return list

   #File in repo related
   def get_file_from_repo(self, project, repo, file_path, branch = 'master' ):
      pathList = [ 'defaultcollection', '_apis', 'git', project, 'repositories', repo, 'items' ]
      queryDict = { 'api-version' : '1.0', 'scopepath' : file_path, 'versionType' : 'branch', 'version' : branch}
      self.geturl_generic(pathList, queryDict)
      return self.issue_request()

   #Work item related
   # Getting a 404 error on this one???
   def get_workitem_list(self, project_name):
      pathList = [ 'defaultcollection', project_name, '_apis', 'wit', 'workitems' ]
      queryDict = { 'api-version' : '1.0' }
      self.geturl_generic(pathList, queryDict)
      return self.issue_request()

   def get_workitem(self, item_num):
      pathList = [ 'defaultcollection', '_apis', 'wit', 'workitems' ]
      queryDict = { 'api-version' : '1.0', 'ids' : item_num }
      self.geturl_generic(pathList, queryDict)
      return self.issue_request()

   def get_workitem_updates(self, item_num):
      pathList = [ 'defaultcollection', '_apis', 'wit', 'workitems', item_num, 'updates' ]
      queryDict = { 'api-version' : '1.0' }
      self.geturl_generic(pathList, queryDict)
      return self.issue_request()

   #Query related
   # NOTE - this only gets 1 level of queries...
   def get_query_json_list(self, project):
      pathList = [ 'defaultcollection', project, '_apis', 'wit', 'queries' ]
      queryDict = { 'api-version' : '1.0', '$depth' : '1' }
      self.geturl_generic(pathList, queryDict)
      resp = self.issue_request()
      list = []
      for x in resp.json()['value']:
         list.append(x)
         try:
            for _x in x['children']:
               list.append(_x)
         except:
            pass
      return list

   def get_query_dict(self, project, ignore_name_list = []):
      dict = {}
      jsonlist = self.get_query_json_list(project)
      for x in jsonlist:
         if x['name'] not in ignore_name_list:
            dict[x['name']] = x['id']
      return dict

   def run_query_named_json(self, proj_name, query_id):
      pathList = [ 'defaultcollection', proj_name, '_apis', 'wit', 'wiql', query_id ]
      queryDict = { 'api-version' : '1.0' }
      self.geturl_generic(pathList, queryDict)
      return self.issue_request()

   #Test Plan and Suite Related
   def get_test_plans_json(self, proj_name):
      pathList = [ 'defaultcollection', proj_name, '_apis', 'test', 'plans' ]
      queryDict = { 'api-version' : '1.0' }
      self.geturl_generic(pathList, queryDict)
      return self.issue_request()

   def get_test_plans_list(self, proj_name):
      resp = self.get_test_plans_json(proj_name)
      list = []
      for x in resp.json()['value']:
         list.append(x)
      return list

   def get_test_suites_json(self, proj_name, plan):
      pathList = [ 'defaultcollection', proj_name, '_apis', 'test', 'plans', plan, 'suites' ]
      queryDict = { 'api-version' : '1.0' }
      self.geturl_generic(pathList, queryDict)
      return self.issue_request()

   def get_test_suites_list(self, proj_name, plan):
      resp = self.get_test_suites_json(proj_name, plan)
      list = []
      for x in resp.json()['value']:
         list.append(x)
      return list
