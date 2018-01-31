
import requests 
import json
from machine import Machine


class A10(Machine):

	def __init__(self,username,password,ipaddr):
		Machine.__init__(self,username,password,ipaddr)
		self.session = ''
		self.signature = ''	
		self.url = 'https://' + ipaddr 	

	def login(self):
		header = {'Content-Type':'application/json'}
		body = { "credentials":{"username":self.username,"password":self.password}}
		response = requests.post( self.url+ '/axapi/v3/auth',verify=False, headers=header,json=body)
		signature = json.loads(response.text)
		self.signature = signature['authresponse']['signature'] 
		print(signature)

#	def logoff(self):

a10 = A10('admin','a10','192.168.201.34')
a10.login()

