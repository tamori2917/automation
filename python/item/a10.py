
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

        def login(self):
            header = {'Content-Type':'application/json'}
            body = { "credentials":{"username":self.username,"password":self.password}}
            response = requests.post( self.url + api_url + 'auth',verify=False, headers=header,json=body)
            signature = json.loads(response.text)
            self.signature = 'A10 ' + signature['authresponse']['signature'] 

        def logoff(self):
            header = {'Content-Type':'application/json','Authorization': self.signature}
            response = requests.post( self.url + api_url + 'logoff',verify=False, headers=header)
            print(json.loads(response.text))
            
        def ssh(self,command):

a10 = A10(username='admin',password='a10',ipaddr='192.168.201.15')
<<<<<<< HEAD
print(a10.signature)
helllo my name is khairul
print(a10.signature).my best
this is the latest please try
=======
print(a10.signature).my best
this is the latest please try
>>>>>>> refs/remotes/origin/master
