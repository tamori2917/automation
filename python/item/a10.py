
import requests 
import json
from machine import Machine


class A10(Machine):
	def __init__(self,*args,**kwargs):
		super(A10,self).__init__(**kwargs)
		self.session = ''
		self.signature = ''	
		self.url = 'https://' + kwargs['ipaddr'] 	

	#def login(self):
		#header = {'Content-Type':'application/json'}
		#body = { "credentials":{"username":self.username,"password":self.password}}
		#response = requests.post( self.url+ '/axapi/v3/auth',verify=False, headers=header,json=body)
		#signature = json.loads(response.text)
		#self.signature = signature['authresponse']['signature'] 
		#print(signature)

#	def logoff(self):

a10 = A10(username='admin',password='a10',ipaddr='192.168.201.34')
#a10.login()

