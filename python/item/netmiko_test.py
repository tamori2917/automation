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

output = connect.send_command('ls -la')
print(output)
print(type(output))
grep = re.search('.vim',output)
grep2 = re.match('.vim',output)
print("grep = {}".format(grep.group()))
print("grep = {}".format(grep2))
