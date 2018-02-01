
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
                self.device_type=kwargs['device']
            #except:
            #    print("Argument Error , Please check error")
        def ssh(self)
                machine = {
                        'device-type':self.device_type,
                        'username':self.username,
                        'password':self.password,
                        'ip':self.ipaddr
                        }
                self.ssh = ConnectHandler(**machine)
               
        def logoff_ssh(self)
                self.ssh.disconnect()


test = Machine(username='admin',password='a10',ipaddr='192.168.201.15',device='a10')

test.ssh.send_command("show int brief");
                


