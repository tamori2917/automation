from netmiko import ConnectHandler
import json
import requests
import re

linuxpc = {
        'device_type':'linux',
        'ip':'127.0.0.1',
        'username':'khaianna',
        'password':'kanna1231'
} 

connect = ConnectHandler(**linuxpc)

service = "sshd"
output = connect.send_command("sudo ps aux | egrep '{}'").format(service)
print(type(output))
#grep = re.search('.vim',output)
#print("grep = {}".format(grep.group()))
print(output)
