import requests
import json
from machine import Machine

class linux(Machine):

    def __init__(self,*args,**kwargs):
            #for arg in args:
        self.server_list = "({})".format("|".join(args))

    def server_check():

        output = self.ssh.send_command("ps aux | egrep '{}'".format(self.server_list))
        return output
    def syslog():
        #process for syslog goes here
    def snmp():
        #process for snmp goes here
    def ftp():
        #process for ftp goes here
    def file_check():
        #check whether that file is there or not in server
    def output():
        #produce output and parse the output 

#BELOW IS FOR TESTING CLASS ONLY!
#PLEASE UNCOMMENT AFTER USE
server = ("ftp", "snmp", "syslog")
test = linux(username=khairul, password=, ipaddr=127.0.0.1, *server)
print(test.server_check)


