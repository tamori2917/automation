import requests
import json 
import requests 
import json
import json_replace
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
        self.session = ''
        self.signature = '' 
        self.url = 'https://' + kwargs['ipaddr']

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
    
    def import_json():
        f = open('./json/class-list1.json', 'r')
        jsonData = json.load(f)
        jsonData = json.dumps(jsonData)
        self.payload = jsonData
        return jsonData

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
#    def ssh_output():
        

###############################################TESTING CLASS###################################################    
a10 = A10(username='admin',password='a10',ipaddr='192.168.201.31' ,device_type='a10')
print(a10.import_json())
#a10.login()
##a10.classlist("put")
#a10.accesslist("get")
#a10.logoff()
