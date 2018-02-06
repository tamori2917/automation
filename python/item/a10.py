
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
	    if list == "classlist":
      	    	if method == "get":
       			header = {'Content-Type':'application/json','Authorization': self.signature}
    	       		response = requests.get( self.url + api_url + list, verify=False, headers=header )
    			print(json.loads(response.text))
	    else:
	    	print("else")
	    else
	    	print("else2")

a10 = A10(username='admin',password='a10',ipaddr='192.168.201.31')
a10.login()
print(a10.signature)
#a10.get("class-list")
a10.classlist("classlist","get")

