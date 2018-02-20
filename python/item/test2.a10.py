import os
import requests
import json
#import json_replace
from machine import Machine

#Disable Warning for Certificate Error
requests.packages.urllib3.disable_warnings()
api_url = '/axapi/v3/'

##reform json_data
#jsonData = json_replace.Json_replace("class-list1.json")
#jsonData1 = json_replace.Json_replace("access-list-exd.json")

class A10(Machine):
	def __init__(self,*args,**kwargs):
		super(A10,self).__init__(**kwargs)
		self.hostname = kwargs['hostname']
		self.session = ''
		self.signature = '' 
		self.url = 'https://' + kwargs['ipaddr']
		self.cl_count = 0
		self.acl_count = 0
		#create dir for each a10 calls
		if not os.path.exists('./json/{}'.format(self.hostname)):
			os.makedirs('./json/{}'.format(self.hostname))

	def login(self):
		self.header = {'Content-Type':'application/json'}
		body = { "credentials":{"username":self.username,"password":self.password}}
		response = requests.post( self.url + api_url + 'auth',verify=False, headers=self.header,json=body)
		signature = json.loads(response.text)
		self.signature = 'A10 ' + signature['authresponse']['signature'] 
		self.header['Authorization'] = self.signature 

	def logoff(self):
		response = requests.post( self.url + api_url + 'logoff',verify=False, headers=self.header)
		print(json.loads(response.text)) 

	def import_json(self,file_path):
		f = open(file_path, 'r')
		jsonData = json.load(f)
		jsonData = json.dumps(jsonData)
		return jsonData

	def export_json(self,target_path):
		#do we really need parser over here?
		#with open("./json/{}/classlist")
		print('hello')


	def get(self,list):
		response = requests.get( self.url + api_url + list, verify=False, headers=self.header )
		print(json.loads(response.text))

	def calist(self,list,method):
		payload = self.import_json('./json/class-list1.json')
		print('payload is {}'.format(payload))
		#self.cl = {:}
		if list == "class":
			if method == "get":
				response = requests.get( self.url + api_url + "class-list", verify=False, headers=self.header )
			elif method == "post":
				response = requests.post( self.url + api_url + "class-list", verify=False, headers=self.header, data=payload)
			elif method == "put":
				response = requests.put( self.url + api_url + "class-list/" + "a", verify=False, headers=self.header, data=payload)
			else:
				print("method is invalid")
				print ('Response Code = {}'.format(response.status_code))
				count = json.loads(response.text)
				self.cl_count = len(count["class-list-list"])
				return json.loads(response.text)
		elif list == "acl":
			if method == "get":
				response = requests.get( self.url + api_url + "ip/" + "access-list/" + "standard" + "99", verify=False, headers=self.header )
			elif method == "post":
				response = requests.get( self.url + api_url + "access-list", verify=False, headers=self.header )
			elif method == "put":
				response = requests.get( self.url + api_url + "access-list", verify=False, headers=self.header )
		else:
			print("method is invalid")	 
			print ('Response Code = {}'.format(response.status_code))
			count = json.loads(response.text)
			self.cl_count = len(count["class-list-list"])
			return json.loads(response.text)

###############################################TESTING CLASS###################################################	   
###############################################TESTING CLASS###################################################	   
###############################################TESTING CLASS###################################################	   
###############################################TESTING CLASS###################################################	   
a10 = A10(hostname='a10', username='admin',password='a10',ipaddr='192.168.201.31' ,device_type='a10')
#print(a10.import_json('./json/class-list1.json')
a10.login()
#print(json.dumps(a10.classlist("get"), sort_keys=False, indent=4, separators=(',',': ')))
print(a10.calist("class","get"))
#a10.accesslist("get")
a10.logoff()

