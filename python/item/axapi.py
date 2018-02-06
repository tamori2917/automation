
import requests
import json
from a10 import A10
api_url = '/axapi/v3/'

class Axapi(A10):
	def __init__(self,**kwargs):
		super(Axapi,self).__init__(**kwargs)

	def get(self,list,abc):
		header = {'Content-Type':'application/json','Authorization': self.signature}
		response = requests.get( self.url + api_url + list + abc, verify=False, headers=header )
		print(json.loads(response.text))

#axapi.login()
#print (axapi.signature)
#class-list1 =axapi.get("class-list")
#class-list2 =axapi.get("class-list")
#axapi.get("access-list")
