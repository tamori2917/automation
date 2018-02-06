from a10 import A10
from machine import Machine

class Classlist_get(A10):
	def __init__(self,*args,**kwargs):
	    #get class-list all
	    header = {'Content-Type':'application/json','Authorization': self.signature}
	    response = requests.post( self.url + api_url + self.classlist,verify=False, headers=header )
	    print (response + "test")
