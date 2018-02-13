
import requests
import json
import error 
from netmiko import ConnectHandler

class Machine(object):
        def __init__(self,**kwargs):
	    #try:	
                #self.hostname = kwargs.get('hostname',"hello")	
                self.username = kwargs['username']
                self.password = kwargs['password']	
                self.ipaddr = kwargs['ipaddr']
                self.device_type = kwargs['device_type']
                machine = {
                        'device_type':self.device_type,
                        'username':self.username,
                        'password':self.password,
                        'ip':self.ipaddr
                        }
                self.ssh = ConnectHandler(**machine)
            #except:
            #    print("Argument Error , Please check error")
               
        def logoff_ssh(self):
                self.ssh.disconnect()
        
        def json_import(self,filepath)

##For testing Class##
#test = Machine(username='admin',password='a10',ipaddr='192.168.201.15',device_type='a10')
#
#output = test.ssh.send_command("show int brief");
#print(output)        
#
#test.ssh.logoff_ssh()



