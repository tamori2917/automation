
import requests
import json
import error 
class Machine(object):
	
	def __init__(self,*args,**kwargs):
		try:	
			#self.hostname = kwargs.get('hostname',"hello")	
			self.username = kwargs['username']
			self.password = kwargs['password']	
			self.ipaddr = kwargs['ipaddr']
		except:
			print("Argument Error , Please check error")

