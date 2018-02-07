import requests
import json
from machine import Machine

class linux(Machine):

        def __init__(self,*args,**kwargs):
            #for arg in args:
            self.server_list = "({})".format("|".join(args)) 
            
        def server_check():
            output = self.ssh.send_command("ps aux | egrep ({})".format(self.server_list))
            return output
#            #check all server from list
#        def syslog():
#            #check syslog is there
#
#        def snmp():
#            #check snmp server is on or not
#
#        def ftp():
#            #check ftp server is there or not
        def file_check(file_name):
#            #check whether file is there or not
            output = self.ssh.send_command("find {} ./".format(file_name))
#        def output():
#            #output anything
#
#
#


#server = ("ftp", "snmp", "syslog")  
#test = linux(username=khairul, password=, ipaddr=127.0.0.1, *server)
#print(test.server_check)
