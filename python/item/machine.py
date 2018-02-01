
import requests
import json
import error 
from netmiko import ConnectHandler

class Machine(object):
        def __init__(self,**kwargs):
	    #try:	
                #self.hostname = kwargs.get('hostname',"hello")	
                print(kwargs)
                self.username = kwargs['username']
                self.password = kwargs['password']	
                self.ipaddr = kwargs['ipaddr']
            #except:
            #    print("Argument Error , Please check error")
        def to_ssh

