
import requests 
import json
from machine import Machine

api_url = '/axapi/v3/'

class A10(Machine):
	def __init__(self,*args,**kwargs):
		super(A10,self).__init__(**kwargs)
		self.session = ''
		self.signature = ''	
		self.url = 'https://' + kwargs['ipaddr'] 	
		self.header = {'Content-Type':'application/json'}
		#self.payload = "{\"class-list\":{\"ac-list\":[\"ac-key-string\":\"abc.com\",\"ac-match-type\":\"ends-with\"],\"name\":\"test555\",\"type\":\"ac\",\"uuid\":null}}"
		self.payload = "{'class-list':{'ac-list':['ac-key-string':'abc.com','ac-match-type':'ends-with'],'name':'a','type':'ac','uuid':null}}"
		self.classlist1 = 'a'

	def login(self):
		header = self.header
		body = { "credentials":{"username":self.username,"password":self.password}}
		response = requests.post( self.url + api_url + 'auth',verify=False, headers=header,json=body)
		signature = json.loads(response.text)
		self.signature = 'A10 ' + signature['authresponse']['signature'] 
	def logoff(self):
		header = {'Content-Type':'application/json','Authorization': self.signature}
		response = requests.post( self.url + api_url + 'logoff',verify=False, headers=header)
		print(json.loads(response.text))

	def get(self,list):
		header = {'Content-Type':'application/json','Authorization': self.signature}
		response = requests.get( self.url + api_url + list, verify=False, headers=header )
		print(json.loads(response.text))

	def classlist(self,list,method):
		if list == "class-list":
			if method == "get":
				header = {'Content-Type':'application/json','Authorization': self.signature}
				response = requests.get( self.url + api_url + list, verify=False, headers=header )
				print(json.loads(response.text))
			elif method == "post":
				header = {'Content-Type':'application/json','Authorization': self.signature}
				response = requests.post( self.url + api_url + list, + self.classlist1, verify=False, data=json.dumps(self.payload))
				print(json.loads(response.text))
			elif method == "put":
				header = {'Content-Type':'application/json','Authorization': self.signature}
				response = requests.get( self.url + api_url + list, verify=False, headers=header )
				print(json.loads(response.text))
			else:
				print("method is invalid")
		elif list == "access-list":
			if method == "get":
				header = {'Content-Type':'application/json','Authorization': self.signature}
				response = requests.get( self.url + api_url + list, verify=False, headers=header )
				print(json.loads(response.text))
			elif method == "post":
				header = {'Content-Type':'application/json','Authorization': self.signature}
				response = requests.get( self.url + api_url + list, verify=False, headers=header )
				print(json.loads(response.text))
			elif method == "put":
				header = {'Content-Type':'application/json','Authorization': self.signature}
				response = requests.get( self.url + api_url + list, verify=False, headers=header )
				print(json.loads(response.text))
		else:
			print("list is invalid")

a10 = A10(username='admin',password='a10',ipaddr='192.168.201.31' ,device_type='a10')
a10.login()
print(a10.signature)
a10.classlist("class-list","post")
