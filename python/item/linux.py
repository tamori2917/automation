import requests
import json
from machine import Machine

class linux(Machine):

    def __init__(self,*args,**kwargs):
        super(linux,self).__init__(**kwargs)
        
    def server_check(self,*args):
        self.server_list = "({})".format("|".join(args)) 
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
    def file_check(self,file_name,dir):
#            #check whether file is there or not
        output = self.ssh.send_command("find {1}/{0}".format(file_name,dir))
        exit_code = self.ssh.send_command("echo $?")
        if exit_code == "1":
            print("File or directory {} not available ".format(file_name))
        else:
            print("File or directory {} exists".format(file_name))
        return exit_code

    def create_dir(self,dir,parent_dir)
        self.file_check("",dir)
        if exit_code = "0":
            return 
        else:
            self.ssh.send_command("mkdir - {}/{}".format(parent_dir,dir))
            exit_code = self.ssh.send_command("echo $?")
                if exit_code == "1":
                    print("mkdir failed".format(file_name))
                else:
                    print("Directory created".format(file_name))
#        def output():
#            #output anything
#
#
#


#server = ("ftp", "snmp", "syslog")  
process_id = ("ftp", "snmp", "syslog")  
test = linux(username="khaianna", password="kanna1231", ipaddr="127.0.0.1",device_type="linux")
test.login()
test.file_check("main22.py", "~/python/A10Automation/python/item")
#print(test.server_check)
