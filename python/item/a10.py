import requests
import json 
from machine import Machine
#Disable Warning for Certificate Error
requests.packages.urllib3.disable_warnings()
api_url = '/axapi/v3/'
null = 'null'

##import pyload json  as dictionary
f = open('class-list1.json', 'r')
f1 = open ('access-list-exd.json', 'r')
##change as string
Allf = f.read()
Allf1 = f1.read()
##delete new line for linux and mac and windows
text = Allf.replace('\n','')
jsonData = text.replace('\r','')

text1 = Allf1.replace('\n','')
jsonData1 = text1.replace('\r','')

class A10(Machine):
    def __init__(self,*args,**kwargs):
        super(A10,self).__init__(**kwargs)
        self.session = ''
        self.signature = '' 
        self.url = 'https://' + kwargs['ipaddr']
        self.payload = jsonData

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

    def get(self,list):
        response = requests.get( self.url + api_url + list, verify=False, headers=self.header )
        print(json.loads(response.text))

    def classlist(self,method):
        self.class_list = {'':''}
        if method == "get":
            response = requests.get( self.url + api_url + "class-list", verify=False, headers=self.header )
        elif method == "post":
            response = requests.post( self.url + api_url + "class-list", verify=False, headers=self.header, data=self.payload)
        elif method == "put":
            response = requests.put( self.url + api_url + "class-list/" + "a", verify=False, headers=self.header, data=self.payload)
        else:
            print("method is invalid")
        print (response.status_code)
        return json.loads(response.text)

    def accesslist(self,method):
        header = {'Content-Type':'application/json','Authorization': self.signature}
        if method == "get":
            response = requests.get( self.url + api_url + "ip/" + "access-list/" + "standard" + "99", verify=False, headers=self.header )
#       elif method == "post":
#           response = requests.get( self.url + api_url + "access-list", verify=False, headers=self.header )
#       elif method == "put":
#           response = requests.get( self.url + api_url + "access-list", verify=False, headers=self.header )
        else:
            print("method is invalid")  
        return json.loads(response.text)
    def ssh_output():
        

###############################################TESTING CLASS###################################################    
###############################################TESTING CLASS###################################################    
###############################################TESTING CLASS###################################################    
###############################################TESTING CLASS###################################################    
a10 = A10(username='admin',password='a10',ipaddr='192.168.201.31' ,device_type='a10')
a10.login()
##a10.classlist("put")
#a10.accesslist("get")
a10.logoff()
